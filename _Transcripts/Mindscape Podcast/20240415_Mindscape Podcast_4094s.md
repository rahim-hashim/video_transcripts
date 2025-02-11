---
Date Generated: June 06, 2024
Transcription Model: whisper medium 20231117
Length: 4094s
Video Keywords: []
Video Views: 6572
Video Rating: None
Video Description: Patreon: https://www.patreon.com/seanmcarroll
Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2024/04/15/272-leslie-valiant-on-learning-and-educability-in-computers-and-people/

Science is enabled by the fact that the natural world exhibits predictability and regularity, at least to some extent. Scientists collect data about what happens in the world, then try to suggest "laws" that capture many phenomena in simple rules. A small irony is that, while we are looking for nice compact rules, there aren't really nice compact rules about how to go about doing that. Today's guest, Leslie Valiant, has been a pioneer in understanding how computers can and do learn things about the world. And in his new book, The Importance of Being Educable, he pinpoints this ability to learn new things as the crucial feature that distinguishes us as human beings. We talk about where that capability came from and what its role is as artificial intelligence becomes ever more prevalent.

Leslie Valiant received his Ph.D. in computer science from Warwick University. He is currently the T. Jefferson Coolidge Professor of Computer Science and Applied Mathematics at Harvard University. He has been awarded a Guggenheim Fellowship, the Knuth Prize, and the Turing Award, and he is a member of the National Academy of Sciences as well as a Fellow of the Royal Society and the American Association for the Advancement of Science. He is the pioneer of "Probably Approximately Correct" learning, which he wrote about in a book of the same name.

Mindscape Podcast playlist: https://www.youtube.com/playlist?list=PLrxfgDEc2NxY_fRExpDXr87tzRbPCaA5x
Sean Carroll channel: https://www.youtube.com/c/seancarroll

#podcast #ideas #science #philosophy #culture
---

# Mindscape 272 | Leslie Valiant on Learning and Educability in Computers and People
**Mindscape Podcast:** [April 15, 2024](https://www.youtube.com/watch?v=FHW-nBIZc2g)
*  Hello everyone, welcome to the Mindscape Podcast. I'm your host, Sean Carroll. One of the problems
*  with reality, as I see it, is that there's a bunch of puzzles, questions, problems, if
*  you like, that are hard to solve. And I'm not even thinking about moral or political
*  or social problems. I mean just mathematical problems, or at least problems that you can
*  state rigorously and quantitatively. There are problems that in principle you can find
*  an algorithm for providing a solution, but that algorithm is so inefficient it would
*  take forever or a very very long time to actually do it. This is of course a whole area of knowledge,
*  right? Within theoretical computer science we have computational complexity theory, asking
*  the question if you have some kind of question like what is the shortest distance that a
*  traveling salesman would have to go through given these stops that they have to make along
*  the route, how many steps would your computer program need in order to solve it? And one
*  of the nice things about those problems is that even though it might take a lot of steps
*  to solve it, at least there's a solution, right? At least there is one right answer.
*  The difficulties become enormously larger when you imagine being a scientist, let's
*  say being a theorist within science, right? Where you have some data collected by your
*  experimentalist friends and your job as a theorist is to come up with a best fit model
*  to the data, to come up with a theory that best fits the data in the sense that you can extrapolate
*  it beyond the data you have and have a good chance of continuing to fit it. Well, that's
*  going to be a difficult problem to even conceptualize because maybe you don't have enough data to
*  uniquely fix the thing. Maybe you have lots of data but you don't have any good ideas about how
*  to fit it. That's why we theoretical physicists make the big bucks, right? Anyway, today's guest,
*  Leslie Valiant, has done incredibly important work within theoretical computer science on exactly
*  understanding this kind of puzzle, the idea of getting better at fitting some data in a way that
*  can be extrapolated, the best learning that an automated system can do. I have to read you a
*  excerpt in case you don't know who Leslie Valiant is from his Wikipedia page. Valiant was awarded
*  the Turing Award in 2010 having been described by the Association for Computing Machines as a
*  heroic figure in theoretical computer science and a role model for his courage and creativity in
*  addressing some of the deepest unsolved problems in science, in particular for his striking
*  combination of depth and breadth. So he's written a book that is named after an idea he had called,
*  he wrote, this is a while ago he wrote this book called Probably Approximately Correct,
*  Nature's Algorithms for Learning and Prospering in a Complex World. And as I say in the podcast,
*  I just love this phrase, probably approximately correct. The idea being that you have some guess
*  to how to extrapolate from your experience to what's going to happen next, there is literally
*  no way that you can guarantee ahead of time that you're going to be right in that extrapolation.
*  You can't even guarantee that you will be approximately right. You're going for that,
*  you're trying to be approximately correct, but you have a chance of being approximately correct
*  in what you can show in certain very rigorous circumstances that you can probably be approximately
*  correct, that you have a good chance of doing that. And that's what all of us scientists actually aim
*  for. So one of the great things about Les Valiant is that he thinks about these very deep ideas in
*  rigorous quantitative theoretical computer science and then does try to apply them more broadly,
*  thus the subtitle, Nature's Algorithms for Learning and Prospering in a Complex World. So he has a new
*  book that is just about to come out called The Importance of Being Educable, A New Theory of Human
*  Uniqueness. So what he wants to do is encourage everyone to shift their perspective from thinking
*  about human beings on a scale of intelligence, how smart you are, how many things you know,
*  to a scale of educability. How good are you at learning new things? He tries to make the argument
*  that knowing things, being good at solving puzzles or whatever it is, is much less important than
*  being able to learn how to solve puzzles, how to understand things. And that's also something that
*  you can quantify and you can actually think about it for machines as well as for human beings. So he
*  wants to argue that what really makes us different than other animals is that we can be educated,
*  which is a little bit different than learning, right? A cat or a dog, well, maybe not cats,
*  but dogs certainly can learn to do things, but they generally learn to do things by being shown
*  what they want, what they are wanted to do and then, you know, trial and error, right? You can't read
*  a book if you're a dog and learn to do things that way, whereas human beings can transfer new
*  information, can generalize it, can string it together in ways that according to Valiant are not
*  there elsewhere in the animal kingdom. So that may or may not be right. I think that's a good
*  empirical question. He is very, very honest about when he puts forward a conjecture and it still
*  hasn't been tested yet, but it's a nice way of thinking slightly differently about our capacities
*  and capabilities. So with that, let's go.
*  Leslie Valiant, welcome to the Mindscape Podcast.
*  Thank you for having me.
*  So if I look over your works, your research over the years and writings, the word learning is the
*  one that appears over and over again. So you're a computer scientist. Why is it that the word
*  learning became so important to how you think about things?
*  Yes. So I started in computer science looking at computational complexity, which is about the
*  inherent difficulty of doing computation. And I did various things in that field for about 10
*  years. But I regarded it as a very fundamental field of computer science, maybe the most
*  fundamental and the most basic idea, which goes to me is that if it's no good at solving the basic
*  problems of the mind and AI, then it's no good. So it was a very challenge for the field. And so then
*  I looked at AI and I saw that there were various topics discussed in AI conferences. And I quickly
*  tried to figure out, well, which one is the most fundamental? And asked that way, it seemed to me
*  that there must be learning. So I zeroed in very fast on learning and tried to understand it from
*  the point of view of it being a computational process, which wasn't so easy. There were
*  limitations and the limitations, some were statistical, but I thought the main ones were
*  computational. It just needs a lot of computation to do it well.
*  And to skip ahead a little bit, were you right?
*  Well, I think I was. These big LLMs do spend millions of dollars in being trained. So that's
*  exactly what the model was. That you have to have a model of learning, which somehow promised you
*  that the amount of computation needed may be much, but it was still polynomial time. It was still
*  doable.
*  And this is an honest question. I don't know the answer. There's machine learning, which is a
*  specific approach, a specific set of algorithms. But then there's the more broad category of
*  machines learning. Are those two separate things? Is machine learning a general term or a more
*  specific one?
*  Well, these things are used in many senses. For me, they're the same, I think. Machine learning,
*  it's the name of an academic field, which includes various things, but clearly it tries to capture
*  what happens when machines learn. It should be the same.
*  So it goes beyond neural networks.
*  Sure, sure. So neural networks are just one of many algorithms for doing learning. And from the
*  80s onwards, and maybe even before, people were exploring a whole array of different algorithms,
*  and different algorithms are used in different contexts. So in some contexts, we've got
*  enormous datasets, neural networks have been shown to be very good assets. But still, there are many
*  other algorithms which are widely used for smaller datasets.
*  Could you kind of put us in the mindset of how people were thinking in the 1980s? I have this vague
*  feeling there was super excitement about AI in maybe the 60s, and then it cools off a bit in the
*  70s, and it begins to return again in the 80s.
*  Yes, I can only speak for myself, of course. So I came into learning from a theoretical
*  perspective. So from what I was doing in this theoretical field called computational learning
*  theory grew up, which focused very much on formulating learning from examples. So maybe one
*  of the big services done by that community. So I formulated this PAC model, the probably
*  approximately correct model of learning. And basically, what it captures theoretically is how
*  you generalize is when you learn from examples, when do you declare yourself successful. So
*  clearly, you have to predict future examples accurately, as accurately as you can. But also,
*  you want to show that the effort made to predict future examples to be in the position to be able
*  to predict future examples should be doable, moderate in terms of polynomial time and things
*  like that. So in particular, the more effort you make, the more accurate your prediction should
*  be. But furthermore, the more effort you make, the more effort should be reasonably rewarded. So the
*  rewards for the more effort should go up not infinitely, but slowly. And this boils down to
*  technically algebraic curves to a constant exponent, the error being a constant exponent of the effort
*  you make. Anyway, so anyway, so this was a theoretical model. It was widely explored. And I think
*  it focused attention on just this very specialized problem of learning from examples efficiently.
*  And then soon afterwards, for reasons partly inspired by this, partly from other reasons,
*  people started to have data sets which they shared, and they systematically compared the
*  efficacy of different algorithms, how well they did on different data sets. And this started from
*  the mid 80s. And they grew this very large experimental machine learning community.
*  So the for a long time, the neural nets weren't competitive, because they just
*  performed badly on small data sets. But as we know, when the data sets became bigger,
*  they became more and more competitive. So I saw the machine learning fund, there was lots of
*  excitement because it's come theoretically, it kind of worked. I'm experimentally, it worked on
*  many data sets. And anyway, to me, it was a plausible entry into what the mind did, you know,
*  was something which was computationally feasible. Because from a theoretical perspective, the
*  previous things people tried to formalize, like logic, reasoning, you know, everything turned out
*  to be computationally intractable. So from a theoretical point of view, this was exciting
*  for the community, which is this. And but they grew this large experimental community, which,
*  from which the current success is all derived, I think.
*  I do want to mention that the phrase probably approximately correct, or pack learning, as you're
*  calling it. And there's also a book that you wrote with the title, that is one of the best titles
*  I've ever seen for a book. And I presume that is it allowed to take lessons that are implicit
*  in that phrase and go beyond computers and specific learning algorithms to sort of a more
*  general epistemological goal we should all have to probably be approximately correct?
*  Um, sure, sure. Given their license to do exactly that. But I think the phrase, although it's
*  intended as a technical one, indeed, I mean, it should be more widely used. So in fact, the
*  the sensing, which I think it should be broadly understood, is that when people try to understand
*  AI now, where the successors of AI are basically just exactly this learning phenomenon, I think
*  the important point is that, you know, the phenomenon is that there's some promise that
*  averaged over many cases, your predictions will be good. But a very single case, the promise is
*  very weak, you know, every single case, you know, it's very, the promise is weak. So certainly,
*  just knowing this phrase, you should immediately realize that you've that when you try to use AI
*  for some safety critical application, you should be very careful because in New York,
*  particular case, the promises are very weak. And it seems though, like a almost like a
*  simple philosophy of science, right? That we science is not logic. It's not something where
*  we deduce with absolute certainty a result. We have some examples, like you said, we
*  have hypotheses based on those and our aspiration should be to be approximately correct as often as
*  we can. Yes, exactly. So actually, in this earlier book, I do indulge in some philosophical
*  speculation. And I think the distinction I make there is that some tasks we do
*  are theory full and some are theory less. So by theory full, I mean something where we have a good
*  theory, for example, like physics, where we have a theory, we believe we know what's going on and
*  our predictions follow this theory. But most of what we do in everyday life is kind of theory less.
*  We don't know the rules when we make up nice flowing sentences, we don't know exactly how to do it.
*  But the point is that nevertheless, we may have some high skill in being able to do this. And we
*  get this skill from this learning process of many examples, exactly as a chat GPT, it can make
*  continuous sentences, but really flowing prose, but we don't know, we can't characterize what that
*  means. So the take I have is that much of what we do is theory less, but it doesn't mean that it's not
*  effective or predictable or predictable on the average or useful. Because we just,
*  learning processes are in some sense robust and useful.
*  It makes me think about speaking of philosophy of David Hume and his worries about induction,
*  saying that you can't know anything with certainty, even if every single example you've seen is that
*  way. And in some sense, it seems like in at least this computer science context, you can formalize
*  the fact that despite the fact that anything could happen, you have reason to believe that
*  probably you have a model that is going to give you a pretty high probability of getting it right.
*  Well, exactly. So in fact, when you were asking about the 1980s, so when I was getting into this
*  field, I was reading the philosophy and the what the philosophers call the problem of induction,
*  which probably goes back to the Greeks. And I think the philosophers have kind of,
*  their efforts kind of faded out because they didn't quite know what to do with it.
*  And I do think that computer science has solved it. I mean, they solved it in the sense that it's
*  given one meaning in which it's understandable. Of course, philosophers sometimes use the word
*  very generally, so it's more generally, but I think computer science has given a meaning to this,
*  and the domain in which it's meant, it's kind of solved. Yes, I think philosophy is important here.
*  And you said this already, but I do want to highlight it, the question of the efficiency
*  of the calculation and the computational complexity, because philosophers, again,
*  and I sometimes masquerade as a philosopher myself, but sometimes they imagine that you're
*  Laplace's demon and you have infinite calculational capacity. But in the real world, it matters if
*  something takes n steps or n squared or e to the n steps. And as I understand it, one of the
*  nice things about pack learning, probably approximately correct, is that you can show
*  that it is doable. It's efficient in some quantifiable sense.
*  Sure. So I think it's a description of some real world phenomenon. And it does explain that some
*  things we can learn effortlessly, like children learn the meaning of words in their language, and
*  fairly reliably, so that's something easy to learn somehow, although we don't know why.
*  But there are also things which are hard to learn. So we figure out the physical
*  laws of the universe just by looking at the stars. It isn't obvious somehow. People had to work very
*  hard at working that out. So not everything is easy to learn, but obviously we live off things
*  which are easy to learn. And so there are some problems that are sort of intractable. You're the
*  computer scientist here. Do we have a clean division into problems that are efficiently
*  solvable and problems that look pretty intractable to us? Well, in computation, that's a lot of
*  complexity, but even if you're restricted to learning, so what's easy to learn and how to learn,
*  the obvious thing to say is that cryptography is really the flip side of learning. So in
*  cryptography, you encode messages, and someone listening in on many of your encoded messages,
*  you don't want them to be able to decode your future messages. So cryptographic functions
*  have to be things which are hard to learn. That's their design. And so those are examples
*  of hard-to-learn functions. Things we believe are hard to learn, and we actually use them
*  every day. And it's important that they be hard to learn. So the spectrum of easy to learn and
*  hard to learn, at least the extremes are pretty clear. We use the easy ones. We use the hard ones
*  for cryptography. And then there's something in the middle which we don't understand so well.
*  And I guess that's actually very useful because it highlights the sense in which you're using the
*  word learning. It's not just memorizing information, getting more knowledge. That is not what you mean
*  by learning. Yes. So in this sense of learning, you need many examples, and you generalize from
*  many examples. You abstract something from many examples so that in the future you can act,
*  you can classify a new example. So you get labeled examples, pictures of elephants,
*  and other elephants, labeled as elephants and not elephants. In the future, someone gives you a picture,
*  and you have to label it as an elephant or not. So you are trying to invent a rule that you will
*  then test maybe against future data. In practice, how constrained is that generalizing process?
*  Do real computer scientists imagine that there is a predetermined set of possible rules that
*  we're sifting through, or are the computers really using their imagination somehow?
*  Well, they're using a learning algorithm. So it depends. You choose what learning algorithm
*  you want to use. So if you use a deep neural net, then the rule will be a deep neural net
*  which you learn. Or if you want to do something simpler, like a decision tree, there will be a
*  decision tree. So it's up to the learning algorithm produces a rule from a class of rules which
*  you're able to. And so this is stuff that you started thinking about and writing about in the
*  80s, I guess. And my impression, correct me if I'm wrong, is it's now kind of background
*  knowledge for everyone who is doing AI. This PAC learning is a good way of thinking about what is
*  going on right now. I believe so. I think it does capture the main phenomenon which
*  happens when you train a big learning algorithm. So for example, the fact that it gets better and
*  better with more data, and it gets better and better with some algebraic curve, that's what the
*  experiment shows. So I think it's it. I know there seems to be debate these days on scaling
*  and how much it will affect the future intelligence abilities of AI models, right? I mean, there
*  clearly has been enormous advances very recently with large language models, but they also still
*  make mistakes. And am I right to think that there's like a camp that says all of those mistakes are
*  going to go away as we get more and more data? And another one that says no, some mistakes are
*  kind of systematic. Well, I'm not sure they should. They should all say the same thing, that
*  the mistakes will maybe go down, but the effort made to make them go down more and more will be
*  bigger and bigger. So just following this approach, having one big learning box, kind of we understand
*  what it does, and we also understand its limitations. So in fact, from the 90s onwards, I was looking for
*  ways in which we can build on this and do different architectures than just a single box.
*  Okay. I think the future is still using the same phenomenon of learning boxes, but probably
*  in a system, you'd have many boxes, and you'd have some sort of reasoning capability, you'd have some
*  way of chaining together the conclusions they've reached to simulate something more like our
*  reasoning capability. So when you say you have many boxes, you don't just have many copies of
*  the same kind of box, you have different kinds of learning approaches that are going to collaborate
*  with each other. Well, not necessarily. Maybe they're trained on different data, different boxes.
*  We're trained on different data to have different, like the different box may recognize different
*  concepts or maybe recognize different words in the English language. And does this bear on the
*  question of whether or not, let's stick with large language models because they're so in the news
*  right now, whether these models understand things, whether they know things, or is it a different kind
*  of concept we should be using? Well, okay. So my answer is that these large language models
*  are clearly trained for one thing, which is predicting the next syllable, the next token,
*  as they call it. And that's what they're trained for. They're very good at that.
*  They're hard to beat. And any other attribute you give them is your intuition.
*  And people seem to be very generous to large language models in
*  insuring all the things they insure it. But I think if you insure other capabilities like reasoning,
*  or I think it's very hard to prove those capabilities. And I don't think they've been
*  proved. Certainly, since such a large effort has been put into these large language models,
*  people should explore what may be by luck, they're doing something else in addition.
*  But we don't know. And I think it's quite likely that they're not. They're very good at
*  very smooth prose, expressing the next thing. And obviously, the quality of any of these
*  learning systems depends crucially on the data they're given. Everything depends on the data set.
*  And certainly people who produce these large language models put an enormous effort into
*  having a very good data set, human trainers, this and that. Okay, so it wouldn't work well otherwise.
*  So besides having the learning algorithms, the other secret is the data is straight on.
*  Well, I'm pleased to hear you say that. It's very similar to things that I said in a recent
*  solo podcast myself, where I tried to make the point that what is impressive to me about large
*  language models is not that they are thinking like human beings are. That's not what they're
*  trained to do and what we should expect them to do. But they can sound like they're thinking like
*  human beings are. And that is a fascinating fact that maybe we should work to understand better.
*  Yes. I mean, that's a small comment on a psychological comment that maybe our standards
*  are low. And we're impressed by anyone who speaks smoothly and can chain together five sentences
*  coherently. That impresses us usually. But maybe it's easier to do than we think if you're given
*  a billion examples. So just in this AI world, just for a while before we're going to generalize in a
*  bit, but are there clear paths besides getting more and more data to pushing the algorithms in
*  the direction of cognition or reasoning or thought or something like that? Can we do the same kind of
*  thing but with a different twist to make it more like what we recognize as thinking?
*  Well, okay. So now you're going into an area where opinions differ.
*  So clearly in AI, initially there was this big effort in just basing it on reasoning.
*  So people tried to use classical logic to do the reasoning. So that wasn't robust enough. It was
*  hard to put in knowledge and it'd be robust. So the problem with using classical logic and somehow
*  marrying it with machine learning is that it's kind of the assumptions are rather different.
*  Classical logic is very deterministic, unforgiving to errors, unforgiving to inconsistencies,
*  whereas machine learning is very forgiving to errors, inconsistencies and everything else.
*  So the approach I've been trying to pursue is to marry learning and reasoning, but distort
*  the reasoning process to be compatible with learning. So you need some reasoning which
*  forgives errors and thinks correctly and with a certain probability. If A implies B and B implies
*  C, then A implies C would only be true with high probability. The assumptions are true,
*  that kind of thing. So anyway, I think that's the right way in which AI could go if we care more
*  about reasoning. So for example, if at the moment, even if you are impressed with large language
*  models, you probably wouldn't wake up in the morning and decide what to do depending on what
*  your large language model recommends to you, you wouldn't do that. But if you wanted to make
*  them a bit more reliable, a bit more authoritative, then I think that's the kind of thing
*  you'd have to do. You'd have to make systems which conform to what we conventionally think of it as
*  reasoning. And it is possible to combine, is to do certain kinds of reasoning on knowledge which is
*  learned. So I think it's a possible avenue. It's likely that it will be done for more limited
*  domains of knowledge initially. So the fact that large language models can talk about everything
*  is impressive. But if you really wanted to reason, then probably computationally would become
*  totally prohibitive to impose on that. But there are ways for AI to progress where some reasoning
*  capabilities are integrated with learning. I was recently, I found myself on a panel discussion
*  on AI in physics. And there's clearly very obvious applications when you have these huge
*  data sets that physics gets from particle physics or cosmology or whatever. And you want to use a
*  model to find features in those data sets. That's an obvious application. But as a theoretical
*  physicist who wants to invent new concepts to describe the world, that's harder for us. And
*  a friend of mine, fellow physicist Jesse Thaler from MIT suggested that what we need is large
*  language models, but not in the space of tokens, but in the space of concepts. That they can sort
*  of string together concepts in new ways and be creative theoretical physicists that way. Is that
*  a pipe dream or is that something like a hot research project these days? Well, I think,
*  I'm not quite sure why he talked about large language models. If you say machine learning,
*  machine learning on concepts in theoretical physics, I understand. It doesn't have to be
*  this string-like thing of large language models. I don't think it has to be presented as text and
*  sentences and paragraphs. So certainly using machine learning to predict some new law of
*  physics from lots of data. So in principle, that's something one can pursue. I don't know
*  how successful it's going to be, but it depends very much on how you represent the knowledge.
*  So yes, I think it's something to pursue for sure.
*  Okay. We've gotten the AI maybe out of our system. We'll come back to it, I'm sure.
*  I do love the fact that in your books, you are willing to go beyond computer science and draw
*  larger lessons and think about wider problems in a very sort of legitimate way in the sense that
*  here's the hypothesis, let's go test it kind of thing. So I guess one inroad here is, does nature
*  use approximately correct learning or is that a way of thinking about information processing
*  in the natural world, not just in computers or brains? So you mean nature beyond computers and
*  beyond brains as well. Yes. I'm thinking of biology and evolution and life and things like that,
*  early life. Well, I think so. So I've pursued that. So certainly in Darwinian evolution,
*  I've worked on that as well. So in fact, the book you referred to earlier, the problem is approximately
*  correct. I do have a chapter on that. So one can formulate Darwinian evolution as a learning
*  process where basically the labeling, there's no one who labels elephants and not elephants,
*  but the labeling is survival. Okay. So different things happen and some survive, some not, and
*  that's the feedback from the world. So in my opinion, this is a phenomenon of evolution and
*  I think it's a basic phenomenon of our cognition. So in fact, I think the basic question you're
*  asking is that going from computer science to natural world, okay, what am I doing here?
*  Yeah. So I think I'm really going the other way. Okay. So as a general way of looking at it,
*  so the idea that what humans can do can also be done by machines is something which Alan Turing
*  already discussed and for good scientific reasons, Turing thesis, he said, yes, everything humans do,
*  machines can do also. But I think what held back AI for a long time is that we couldn't identify
*  what we actually did. What was it that we have to simulate by machine? Okay. So it's a lack of
*  understanding of ourselves. And then we tried, we reasoned, we tried logic. It didn't work so well,
*  but it's learning from examples which humans do. So that's worked out better. There's a theory there
*  and also in practice it works. That's what everyone uses. So I think in generally computer science,
*  I think everything we ask computers to do, we got the idea from humans, okay, computers do what,
*  all the ideas come from humans having done it already in some form. And so I think in
*  pushing AI forward, we really have to understand ourselves better. So what is it that we do? Okay,
*  so we learn from examples. What else do we do? So trying to put that down on paper, I think will
*  help us understand ourselves and give us something to simulate, something to, the goals for computers.
*  So I think the two go very naturally together, I think, humans and-
*  Yes, that does make sense. But I like this connection to Darwin and natural selection,
*  because I don't really think I've thought of it this way. When you say the word learning,
*  I think about going to school, listening to lectures, doing homework, things that happen
*  in our brains. But you're saying if you conceptualize learning as coming up with the model,
*  with the algorithm that generalizes from the inputs it's had, and your goal is to be able to
*  is reproductive fitness, right? Then, you know, what nature is doing it, whether you like it or
*  not, is tuning the genome to solve this problem by this approximately correct kind of paradigm.
*  Yes, so the learning algorithm there is the mutation algorithm and whatever goes into that.
*  And it learns from the feedback is survival. And it's trying to fit the world to be good.
*  To fit the world.
*  Does it fit into our understanding of the efficiency? I mean, is Darwinian evolution
*  a good algorithm for solving that problem, or is it kind of sloppy?
*  Well, so the problem is that Darwin didn't tell us the details. He didn't, you know,
*  and we still don't know the details. So one theory is that the mutations in the genome
*  are a uniform random noise. Okay. But we know it's not exactly that. But we don't know whether
*  it's somehow a clever version, clever variant of that which helps evolution. So we, yeah, so
*  in my opinion, it has to be, answer must be yes, that, you know, this must be what nature is doing.
*  But even if it's kind of a pencil and paper explanation of what's going on that, you know,
*  if you do a mutation, how much does it change the expression level of your genes? And to mutate from
*  this to that, you know, what's needed, how many examples do you need, that kind of thing.
*  So that hasn't been, more work needs to be done there.
*  Yeah.
*  But I think there's scope even for a pencil and paper possibility analysis that evolution
*  can work as fast as it has, because I don't think there's any scientific explanation of why
*  evolution has succeeded as fast as it has.
*  Yeah.
*  That's still unsolved science, I think.
*  Right. Good. There's lots of unsolved problems. But, okay, we're going to fearlessly leap ahead
*  to human beings. Human beings, I think, we're, our audience is all going to agree, we can learn.
*  We have that capacity. And you, in your new book, you have a new book out called The
*  Importance of Being Educable, a New Theory of Human Uniqueness. And you're kind of shifting
*  from learning, which is a fact, to educability, which may be there's a gradient or a spectrum of
*  abilities there.
*  Well, yes. So, yes, so I build on learning. So I assume we can learn. I mean, that's something
*  which theory which has worked well. So, and as I said, I regard learning as a capability,
*  which you can define fairly precisely. And I think humans do it, machines do it well.
*  And so basic question I ask is, you know, what else do we do, which is fundamental?
*  And now I think the way the question is asked in the book, which I think yields the answer is,
*  so in the course of evolution, at some point, humans emerged, at some point, we became
*  capable of doing various things, which, like I said, civilization, and it happened fairly
*  suddenly. So maybe the changes were kind of sudden, weren't that great. And even it may
*  be in some some composite capability, we suddenly came together. But, you know, what
*  capability do we have, which, you know, can account for our civilization. And of course,
*  similar questions have been asked ever since Darwin by any number of people. And the usual
*  problems are that if you pick one feature, there's no feature which is totally unique to humans,
*  so everything you define, you know, some animal can do. So what the book is about,
*  so this educationality I define, so it's composed of three basic things. One is learning from
*  experience, which is exactly the same as learning from examples, packed learning. So once you can
*  do that, it's international even for low animals, you can do that, you know, the animals 100 million
*  years ago could already adapt and if food was towards the light, they would go to the food.
*  But once you do that, then you should be able to also chain together what you've learned
*  in different contexts. And this is what I alluded to this, what I hope computer systems would do
*  more, some sort of chaining of different things you've learned. And that's a very basic kind of
*  reasoning. And so here the question is, how can you put that also on some principle basis, that if you
*  chain together two pieces of knowledge, why are you so sure that you don't get nonsense?
*  Okay, so maybe they're inconsistent in some hidden way, you've learned them in different contexts.
*  So once you go away from classical logic, the guarantees of chaining things together get lost,
*  so you need some basis for training. And then the third aspect of educability is a very human one of
*  not having to learn from experience or change from experience, but being able to just
*  take from someone else their experience. So they tell you how they do things, they tell you their
*  theory of physics, they tell you the theory of politics, and you just put it into your brain,
*  and then you can apply the next minute. So this is taking theories explicitly given.
*  Right. So the difference is, you know, we can train a dog to do tricks, but basically it's learning
*  from examples, right? Like you get rewarded when you do this, you don't get rewarded when you do
*  that. As far as I know, there are no cases where I can just speak English to tell the dog to do
*  something that it's never experienced before and it goes and does it. So this is your candidate
*  for something that really makes human beings different. Well, I think even that's difficult
*  to make. I think the candidate is the integration of these three things. Okay, fair enough. Yeah.
*  On top of each other. I mean, there are cases that you can, for apes, you can sometimes by
*  physical demonstration, give them a complicated task to do to retrieve food from some tube,
*  etc., etc. So it's almost like giving instructions which they can remember and repeat.
*  Okay. So again, it's being able to give lengthy instructions once and have an animal repeat it,
*  again, isn't totally unique to humans. But we're certainly much better at this. We sit in lecture
*  rooms and listen to podcasts and take stuff in which animals don't. Right. Okay. And so
*  so that's the integration of these three things. The two things are easy to say. One is you're
*  learning from experience. The other is you're being taught. The conjoining or combining different
*  models is a little bit more slippery in my brain. Maybe you can help flesh it out a bit. I mean,
*  do we need a symbolic representation of two different theories in order to ask if they're
*  consistent or is it more implicit somehow? No, no, this is kind of the simple in some sense. So
*  it's like if you think of your mind's eye. So when you plan something, you plan how to go to
*  dinner this evening. So you imagine a situation, use some knowledge to predict what will happen
*  if you do X. And then once X happens, then you get a new situation. And then you use some new
*  knowledge to tell you what you should do next. So planning is an example where you in your mind,
*  you chain together a piece of knowledge and you run the world forward. And also with reasoning,
*  very simple reasoning that you something happens, you have some knowledge, you know what's going to
*  happen next. That's mother knowledge tells you what's going to happen next. So this training is
*  something we do all the time is for planning reasoning. And this is what we need. This seems
*  an essential part of being able to operate this. It's not just like having a single neural net
*  and applying a single neural net and saying, yes, X.
*  But it does, it's related to a hypothesis that Adam Bulley talked about on my podcast earlier.
*  And he and others have been, they're psychologists, thinking about mental time travel, the ability to
*  put yourself into a future situation hypothetically. And I just think of it as
*  imagination, but it's very close to what you're saying. It's sort of working out a set of things
*  that haven't actually happened, but you're able to have the capacity to say it would happen
*  given my theories.
*  Yes, because we can take in other people's theories. And we almost don't care whether they're
*  true or not. We don't know whether they're true or not. But we can do this mental processing with
*  these. So you can watch a movie, whether it's fact or fiction, you almost don't care.
*  But you can process it. We've got this great facility to understand what's going on,
*  to draw implications of what's going on. And whether it's fact or some fantasy or
*  some future thing which hasn't happened, we don't even care.
*  Right, right. Good. And so this net capacity to do these three things,
*  this is educability?
*  Yes, yes, in my view. That's my definition of educability.
*  And one of your mottos or slogans is that educability is perhaps more important than
*  intelligence, which we tend to talk about all the time.
*  Sure. So I think the main downside of intelligence is that no one can define it.
*  That people have complained that we give importance to intelligence, we test people
*  to do intelligence tests and things. This has consequences. And we don't even know what we're
*  testing for. Where do the questions come from? So I think it's very unfortunate that the notion
*  of intelligence has become so important because it's not explicitly defined. So I've explicitly
*  defined educability. Intelligence has no such definition. In fact, the early,
*  Sir Charles Spearman, I think, who first tried to deal with IQ, notions of IQ using statistics,
*  I mean, he defined this as an implicit statistical notion. So basically, I think for him,
*  general intelligence came from a study of how children in schools, the different subjects,
*  and it turned out that the children who were good at one thing were likely to be good at something
*  else as well, that performance in different subjects in school was correlated. And then he
*  almost defined intelligence to be the core of a correlation. But it's very implicit,
*  and we still don't know what the definition is. So the main downside of intelligence is that we
*  don't know what it is. And when people try to define it, they say it comes in 10 different
*  varieties and people disagree. So I think we should go and look for more useful notions.
*  Well, I guess that's the next question. It's nice to be able to define educability,
*  but that falls short of convincing us that it is the important feature that has enabled civilization
*  as you talk about in the book. Well, it's got some of the important components. So certainly,
*  people discuss how humans are unique as far as our culture. We've got enormous culture.
*  We can hand culture on so easily. One person in a lecture room or someone can write a book,
*  a million. If they read the book, get it the next day, animals have no such
*  access to such phenomenon. So certainly, the spread of human culture is certainly based on
*  being able to transfer explicit theories. So that part is essential, and it's part of this
*  complex process. Sure, for any model, its value depends on how useful it turns out to be.
*  So that we don't know yet, but it's a candidate.
*  Well, when would you or could we pinpoint a moment of historical time when we say,
*  oh, okay, human beings have figured out how to educate themselves or is it more gradual?
*  You mean in the past? Yeah.
*  You mean? Yeah. Historically, was it hunter-gatherers? Did they come along with agriculture?
*  Well, okay. So when we got this capability, okay, so I don't need to speculate this,
*  but I can, okay? But I think this could have come even before humans.
*  Okay. So I think it's possible that we had them
*  300,000 years ago. Some predecessor species already evolved this, and it just took a very
*  long time for it to become useful to us. It's like a snowballing effect that you need more
*  and more knowledge to share with humans before it becomes useful. So there's no evidence of any
*  mutation having spread to the whole human population in the last 10,000 years. So
*  there's no biological explanation of a new capability in the recent times of agriculture
*  and things like that. So my guess is that the capability is much, much earlier.
*  But I guess, I mean, you're a college professor, as am I. You've had students. The
*  capacity to be educated differs from person to person, right? I mean, it's not just humans have
*  it. It's a skill or a capacity that we can improve on. We can make better. We can make bigger.
*  Well, yeah, so in almost any aspect of life, individuals differ in performance if you give
*  them some test. So in the book, I do raise this question of whether educability can be enhanced
*  by some process. And I mean, I don't know the answer to that. So I mean, so I concentrate
*  on the fact that this educability, I think, is something common to all humans. But we may
*  have different levels of it. And whether it can be enhanced, I don't know. Certainly, I mean,
*  if the concept has any meaning, then it should be measurable. There should be some way of saying,
*  yes, we have so much of it. But I suggest that research could be done along these lines,
*  where people try to test educability. And so the main feature of that, in some sense, is very
*  simple, is that when you practice your educability, you're gaining new information. So if you have a
*  one-hour educability test, you should not be testing for anything which you knew beforehand.
*  Sure.
*  You should avoid any kind of skill. You shouldn't be testing for kind of skills,
*  native skills. You should be testing for information you've got in that one hour.
*  So it is slightly different from what people do currently.
*  Of course. It's the opposite of what people do currently.
*  But also, I mean, it's very hard because maybe you're giving somebody some new
*  information and asking how quickly they can learn it or new information and asking how quickly they
*  can generalize it. But it suffers from the same worries that large language models do. How do you
*  know that you're not tainted? How do you know that this person hasn't thought about similar things
*  before?
*  Yes, for sure. It's difficult to do. I suppose you just have to... The questions would have to
*  be so designed that there's a likelihood that... So maybe there's some artificiality in the questions
*  or the subject matter is so obscure, you don't expect the person to know about it. Yes,
*  that's the difficulty of the design. But I mean, that's what education is about. You're trying to
*  impart new things. So if you want to measure that, then somehow you have to solve that problem.
*  You at least asked the rhetorical question, should we care about this property of educability,
*  for example, in the leaders that we choose? Do you think that we should undergo a shift from
*  valorizing intelligence to valorizing educability more?
*  I suppose so, if only because I still don't know what people mean by intelligence. Okay, so I think
*  that's the question. But I mean, I think in leaders, I think this makes a lot of sense,
*  because as we see, when people become leaders, they come in with so much knowledge, but then
*  new things happen. And we really want them to be able to use the new things. It's not enough that
*  when they come into their leadership position, they know everything with knowing. I mean,
*  new things happen and they want to be able to pick it up and use it.
*  I guess there is a current worry about things like misinformation, right? Or just the fact that we get
*  so much input from the world, from the internet, and sifting through it and paying attention to
*  things becomes a crucial skill. Is that something that we get new insights on by thinking about
*  educability as a central concept? Well, the insight I got from thinking about this,
*  which I hadn't appreciated fully before, is that when I describe this educability model,
*  it seems a very powerful way in which we can learn information and process it. But somehow
*  there's nothing in it which is good at testing whether the information we've received, especially
*  in the third mode, if someone tells us a theory. There's nothing in my model which gives us the
*  capability to check out whether this new theory is correct. Okay, so we're very easy prey to false
*  theories, to conspiracy theories. If someone tells us their political theory, how are we to know
*  whether it's good for us or not? We're not sure. Maybe we're related to our previous knowledge.
*  I think we're very bad at evaluating theories other people give us
*  because I think it's just inherently difficult to do. I think there's no way it can be done.
*  So now that there's this deluge of information, I think human weakness may become more and more
*  dangerous for us. Although I think the important point for me is that this weakness is enough in
*  humans and we have to deal with it at the human level. So it's not just a question that there are
*  deep fakes and there's new tricks for fooling us. We could have been fooled by older methods as well.
*  We have to recognize that we're easily fooled and educated to understand it. It's not just a question
*  of the new technology. I think we have to deal with the inherent weakness. I did have a couple
*  of recent conversations that made the point about the social aspects of how human beings
*  learn and pass knowledge down. We are more trusting of other human beings than other species are of
*  their fellow beings. That's enabled us to learn faster because we have teachers that we trust and
*  believe in things like that. Maybe there's a dark side of that which makes us a little bit too
*  willing to accept what certain favored people say.
*  Yes, so certainly public education is based entirely on trusting the teacher. If you
*  go to physics course, you have to trust. There's no way the student can verify everything they've
*  learned, so you have to trust. Still, I think we're not totally trusting. Psychologists do
*  experiments where they compare if children are given information by two different people
*  and children do have preferences for who to believe. Do they believe their parents or someone
*  who seems to know more about the subject? We are born with some strategies for dealing with this
*  complicated world, but obviously the strategies aren't that powerful. The idea is who to trust
*  is critical. Does this lens of educability suggest better ways to educate people?
*  Have a school system to focus learning? Maybe the answer is no, but have we been
*  led astray by thinking too much about intelligence and not enough about educability?
*  I think more research could be done. I don't know the answer to your question, but I think
*  this formulation does certainly ask new questions. The most obvious thing to say is that
*  somehow people have talked about the science of education, but still I don't think that education
*  is pursued from a very scientific point of view. It's very much a best practices kind of thing.
*  There's some background science which you could build an education system on top of,
*  but it's not used that much. I think there's a lot of scope for putting more of a scientific
*  basis for developing more of a scientific basis for education by further research.
*  Whereas I think this notion of intelligence has provided us with very much.
*  By scientific basis, are you thinking of an empirical testing of what works and what doesn't
*  or a theoretical superstructure to explain why certain things work?
*  I think it's kind of both that in the end you do have to test whether something works,
*  but to get some assurance that this thing, this working transfers to other situations.
*  Often experiments are done in one situation, some new education technique works, but it doesn't
*  really transfer. I think some superstructure would be useful to help us understand why there's some
*  chance of some approach working. I think it's a combination. Maybe an easier question, not very
*  easy, but an easier one than reforming the school system is just reforming our individual selves.
*  Is it possible for a person to improve their own educability, to learn how to be educated better?
*  Is that just a matter of becoming a better thinker, a better scientist, or is it more to it than that?
*  Well, I don't know. I think that should be a subject of research, but if one can measure
*  educability, then you can ask the question more rigorously, that if you could do some
*  educability test and see whether something you do for yourself improves your educability.
*  If you don't measure it, then you're not clear what it means again.
*  So again, I don't know, but I think it does raise questions which I think seem to be new.
*  As usual in the podcast preparation, I can skim through the book of the person who's coming on,
*  but I can't read every word. You have a chapter entitled,
*  Education as a Model, Educability, I think, as a Model of Computation. Could you explain
*  what that means? That sounds very interesting and important.
*  Yeah, okay. So part of the book is a justification of this mixing of computation and
*  human behavior. So I think this is kind of a philosophical question of where's the science in
*  computer science, say? Okay, so like Turing had this Turing machine, so what's the science? Is
*  it just a mathematical definition and that's the end of it, or is there something more?
*  What I'm trying to explain is that with computational models, the Turing machine is
*  clearly the best example, there's a new kind of way of trying to get to knowledge,
*  where you have a definition which has some properties of robustness. For example, if you
*  make a variance of it, then it's very good if it captures the same notion still, that if you
*  define some notion of computability, you don't want the definition, you don't want the mean
*  to change if you change some little part of the definition, you want it to be robust. So there's
*  some such characterizations. So on this chapter, I try to suggest that educability satisfies some of
*  these notions, that one should have some confidence that this model has some robustness, that if you
*  try to express similar things tomorrow, you probably get a model which is kind of the same
*  or similar. So it's trying to justify why this is a scientific approach. So some people would say the
*  only scientific approach is to do experiments, so if I'm talking about anything about humans,
*  in the title I should do experiments on humans, but I'm not doing experiments on humans, so what
*  am I doing? So that's what I'm trying to answer. Good. I mean, and maybe that sort of brings us
*  full circle to the AI goings on these days. You know, it's been a lot of excitement over the last
*  year or so. We've asked, is it important for leaders to be educable? Can we improve our own
*  educability? What does it mean for a computer to be educable? Is it exactly the same meaning? Is it
*  these three things that you listed? And if so, can we or should we or are we aimed at giving
*  computers those capacities? Yeah, well, I suppose the point of my book is that the aims should be
*  about the same, but I think what, again, having written this down, what one realizes is that the
*  difficulty of being educable is that someone has to decide the content of the education.
*  Okay, so just being educable doesn't produce useful human beings if what they're educated
*  with is just bad stuff. Okay. So, and same with computers. So the difficulty is with the current
*  pure learning systems, obviously, what the training set, but if you make them educable, then
*  there are even more decisions you have to make about what knowledge you give them, because
*  depending on what knowledge you give them, the results will be different. So being educable has
*  its great dangers as well. You can educate machines very easily and also humans very easily to do
*  things you don't want done. Well, I always, you know, near the end of the podcast, I always
*  encourage the guests to let our hair down a little bit. You just touched on these looming issues that
*  a lot of people are super concerned about, about AI risks, whether literally existential risks to
*  the planet and the species or, you know, smaller scale political social risks. I mean, you're
*  someone who has made enormous contributions to helping make machines seem intelligent. Are you
*  worried that it's going to get out of control or is that something that will just keep monitoring
*  and tweak along the way? Well, I think the one thing I would say is that the most extreme fears
*  of this singularity, you know, I don't see or support because these arguments for singularity
*  usually based on the fact that, of some sort of mysticism, that machines will become super
*  intelligent in a way we don't understand and they'll take over. So my view is more that, you know,
*  what machines will do, they'll be more capable along lines we understand, you know, learning,
*  reasoning, taking our theories. So at least they'll do things, they'll do processes we understand.
*  These are the same processes we do, I believe. Okay, so we've got some scientific basis of
*  understanding what they do. So then AI is just like any other kind of dangerous science,
*  like chemistry, where bad things can happen. But, you know, if you understand
*  enough and we know what we know, we know what we don't know, we can kind of have some control of
*  what goes wrong. So something like, you know, when new in the pharmaceutical industry,
*  if there's some new drugs are released, they're very thorough tests. One can't predict ahead of
*  time, you know, whether they'll succeed or not. One can't predict what the tests will really be
*  totally foolproof, maybe mistakes are made. But the AI is kind of a similar kind of thing,
*  that, you know, we understand enough, we'll be cautious, we'll do common sense
*  precautions. But the idea that somehow they'll take over without us letting them take over,
*  I think is a misplaced fear.
*  Good. So, I mean, putting aside that the misplaced fear, what is your and this will be the final
*  question, what do you think will be the biggest impact on human lives from the fact that AI is
*  making such advances? Well, I think we'll just, you know,
*  well, it's going to be more like a mixed economy where some things are done by machines, some by
*  humans. And we'll just have to get used to that. And how it will evolve in detail, of course,
*  no one knows. Computers will get into all aspects of our lives. But we'll just have to get used to
*  the idea that, you know, that many of the things we do, computers will do. And we shouldn't be
*  upset by that. We shouldn't be upset by that. That's always good advice. To control what we
*  control and live with what we can. So, Leslie Valiant, thanks so much for being on the Mindscape
*  podcast. Thank you.

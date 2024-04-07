---
Date Generated: April 05, 2024
Transcription Model: whisper medium 20231117
Length: 4764s
Video Keywords: []
Video Views: 19
Video Rating: None
---

# Opening AI's Black Box with Prof. David Bau, Koyena Pal, and Eric Todd of Northeastern University
**Cognitive Revolution "How AI Changes Everything":** [April 05, 2024](https://www.youtube.com/watch?v=O4Opvjze8Ic)
*  Machine learning worked okay, but didn't really work in profound ways until the last 10 years or so.
*  But now it's really working. It's really working remarkably well. And so we're facing a new type
*  of software that we cannot use traditional computer science tools and traditional computer
*  science methods for dealing with how to ensure that it's correct, that it does the stuff that we want.
*  Logit Lens is essentially the tool where it projects these intermediate states into the
*  decoding layer. So essentially we can just see for that current token prediction, what is the
*  model currently thinking about? We wanted to start with a quote unquote simpler solution,
*  like having some sort of linearity with decoding future tokens. That would have been like a nice
*  final solution, but we realized that no, it's a lot more complex than that, at least at the moment.
*  We tested like 40 plus different tasks and it seems like they're all mediated by this small
*  set of heads, which is cool that it seems like the model has this sort of path that it communicates
*  this task information, even though in the prompts were never explicitly telling it what the relationship
*  between the demonstration and the label are, it's able to figure that out and communicate it forward.
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of how AI
*  technology will transform work, life and society in the coming years. I'm Nathan LeBenz joined by
*  my co-host Eric Torenberg. Hello and welcome back to the Cognitive Revolution. Today I'm excited to
*  share a conversation with Professor David Bao of Northeastern University and grad students,
*  Kowina Paul, author of the paper Future Lens and Eric Todd, who made a surprise appearance to discuss
*  their recent paper describing function vectors. Professor Bao left Google to establish this group
*  with the goal of cracking open the black boxes that are modern AI models so as to understand
*  the internal mechanisms that underlie their key capabilities and ultimately gain robust control
*  of increasingly powerful systems. And indeed, starting originally with vision models and now
*  working more on LLMs, the Bao lab has done pioneering work in this area, delivering a
*  remarkable series of mechanistic interpretability papers over the last couple of years. In this
*  conversation we go deep on a couple of the group's recent publications. First, Kowina walks us through
*  her Future Lens work, which develops techniques that show that even mid-sized language models
*  seem to be thinking multiple tokens ahead. Then Eric Todd joins to tell us about function vectors,
*  a complicated pattern of activity spread across multiple attention heads in different layers of
*  the transformer, that seem to enable in-context learning by encoding the nature of the task
*  inputs and outputs. This work is fascinating for anyone who wants to develop their intuition for
*  how today's models actually function under the hood. And they're a notable step on the path to
*  overall AI interpretability, identifying new abstractions that translate low-level patterns
*  of computation to higher order behaviors. I was a fan of this work coming into the conversation,
*  but I left as a big fan of Professor Bao as a research advisor as well. Throughout the
*  conversation he does a great job of connecting the dots between his students' individual projects,
*  motivating the lab's broader interpretability agenda, and emphasizing key open questions in
*  the field. As always, if you find this work valuable, please do share the episode with
*  your friends. I'd especially suggest this one for anyone who's interested in mechanistic
*  interpretability and considering a PhD in machine learning. And please don't hesitate to
*  share your feedback or suggestions via our website, cognitiverevolution.ai, or by messaging me on your
*  favorite social network. Now, please enjoy this illuminating discussion about the inner workings
*  of large language models with mechanistic interpretability researchers, Koena Paul,
*  Eric Todd, and Professor David Bao. Koena Paul and David Bao from Northeastern University,
*  authors of Future Lens. Welcome to the Cognitive Revolution. Thank you. Really happy to be here,
*  Nathan. I'm excited for this conversation. So Professor Bao leads the group and Koena is part
*  of the research group. And together with your colleagues, you guys have really developed a
*  remarkable interpretability and sort of editability agenda with respect to large
*  language models over the last couple of years. I have covered a couple of your papers previously,
*  although not in the depth that we will get to very shortly with the Future Lens paper,
*  but it's a really cool agenda that is shedding a lot of light on how these new fangled AIs are
*  actually working, what's going on in there, kind of cracking open the black box problem.
*  And certainly regular listeners will know that that's something that I really appreciate and
*  value. For starters, you guys want to just give us a little background on the overall agenda of the
*  group and maybe highlight a couple of your favorite papers that you've published previously. It's a
*  pretty simple agenda. So I think the thing that motivates our group is the fact that machine
*  learning is really a new era for computer scientists. Machine learning has been around
*  for a while, but up until the last decade or so, it's been this dream of having a way of creating
*  self-programming computers that learn from data, that people don't really have to program every
*  line of code. Machine learning worked okay, but it didn't really work in profound ways until the
*  last 10 years or so. But now it's really working. It's really working remarkably well. And so we're
*  facing a new type of software that we cannot use traditional computer science tools and traditional
*  computer science methods for dealing with how to ensure that it's correct, that it does the stuff
*  that we want. All of our tools are very statistical. They're very black box. And so what the theme of
*  the lab is, is to ask how do we confront this new type of software? Are there things that we can do
*  to recover our ability to debug and understand the software that we create? Are there ways that we
*  can take more responsibility for the behavior that emerges from this software? Can we edit the code
*  like the way that you would change a line of code in a traditional program? And so this is actually
*  pretty hard. It would be like asking the question, can you totally control the mechanisms of a tomato
*  or some biological thing that emerged out of a process of evolution? And machine learning is
*  similar. That way it emerges out of a training process. And so just like biologists have to
*  reverse engineer how a tomato works, if they want to really understand what they can do to make it
*  better. We're also trying to develop a science of how to understand the internals of these systems.
*  Now, is that an agenda that you have changed course on relatively recently? I assume it has to be in
*  as much as the understanding of advanced AI systems in this way is predicated on their
*  existence. And I would imagine like at least probably prior to GPT-2, there was almost nothing
*  powerful enough to do this kind of work? Oh, no, I've been at it for a while. So my personal
*  history is I worked at Google for many years and I actually left Google to pursue research. When it
*  started to become clear around 2015 that the field was going to change and the speed at which it's
*  changed has surprised me. It surprised almost everybody in the field, but it was clear that
*  there was a sea change happening. The moment for me was also the same moment for a lot of people
*  when AlexNet came out in 2012 and showed that this really simple, really classical machine
*  learning procedure, something from an idea from the 1950s, right? And an idea from the 1980s,
*  training these neural networks, which really the community at large thought that such a simple
*  procedure probably wouldn't be the thing that solves machine learning in the long run. People
*  thought it would be something trickier or something more complex or something like that.
*  But this idea that all you have to do is scale up neural networks and it works really well was a
*  real eye-opener. So the things that I studied at first, I studied generative vision models a lot
*  like GANs, which were really surprising when they came out. And I thought I'll study these GANs for
*  a long time. Of course, after GANs, we have diffusion models. And of course, we've got these
*  amazing language models and other things going on. So it's been this incredible moving target.
*  It does seem to be a pattern that the earliest to the game started with more
*  vision models. I know that's true for Chris Olaf, for example, as well. So yeah, fascinating kind
*  of shared lineage there. You want to touch briefly on the Rome and Memet papers. This is one that
*  I've covered a little bit in a previous episode. And the way I remember those papers is as a
*  demonstration of the locality of factual knowledge in a language model and also the ability to then
*  edit that language model in ways that preserve a lot of the key properties that you would want to
*  preserve if you were editing a knowledge graph, where, for example, if you were to think that
*  the example in the paper is Michael Jordan played basketball, of course, is the real
*  sentence. But if we wanted to edit that world knowledge to reflect an alternative reality,
*  where Michael Jordan played baseball, then we would want that to be not just for that specific
*  sentence, but robust to different ways you might ask the question, different ways you might set up
*  an auto completion. And in the process of kind of systematically working through the layers to figure
*  out where you're corrupting bits as you go through the layer and figuring out where it starts to fail,
*  and then using that as the place to edit and then achieving that kind of robust editing.
*  It's been a couple of months since I went deep on that one. Tell me how I did.
*  No, no, that's right. And I would back up a little bit, maybe half a step further,
*  which is the fundamental question that we're asking. And it's actually related to FutureLens
*  too, is, is there like a physical reality to the idea of a concept or an idea or a unit of knowledge?
*  Right. We have these things in our head. We think you can go to somebody and you can say,
*  that's something that you know. Like, you know where the Eiffel Tower is, or, oh, you've never
*  heard of the Eiffel Tower. You have no idea where that is. No, it's something that you don't know.
*  So we have this idea that people can know things or they can not know things or they can have an
*  idea or a concept or they can not have one. It just seems so crisp intuitively in our own heads.
*  So the question, is there a physical reality to this? When if an artificial neural network
*  seems to know something or doesn't know something, is there a physical reality
*  to that knowledge or is it just diffuse and spread out in all the neurons and all the
*  computations through the whole network? And I think that there's definitely a school of people
*  who would generally believe that most things are just unimaginably diffuse, that everything's just
*  spread out. There's no reason that there would be any locality, but there's a bunch of neuroscientists
*  in the biological world and some computer scientists in the artificial neural network world
*  who have taken a look over the years and noticed that a lot of times you see locality. I saw that
*  kind of thing in GANs, but our question was, do you see this kind of organization in really large
*  models and do you see any that corresponds to the facts? And so what Rome was about is a bunch of
*  experimental methods for narrowing this down and finding out where facts are localized in a large
*  language model. And it sounds like you had another pie test on it. So maybe you can direct people to
*  listen to that one, but that's the general setting. And of course, there's a bunch of clever
*  methods that you can use to really pin that down. What is the state of that work now? I know that
*  the successor to Rome was the Mehmet paper, right? And that one showed that you could edit up to like
*  10,000 facts at a time. Sure. And then there's another paper that we've written that's actually
*  also coming out this coming year at ICLR. It's called the LRE paper, the linear relational
*  embedding paper. And that paper looks at a different slice of the problem. That paper really
*  asks, if you have a relationship, like something is located in a city or somebody plays a certain
*  instrument or somebody plays a sport or somebody holds a certain position or something like that,
*  there's this general relationship. What's the representation of that general relationship?
*  The Rome paper was asking, what's the representation of like an individual association? But we really
*  wanted to break that down. We can see that there's an individual association. We can see that the
*  representation of the subject and the object seem pretty clear, but we wanted to understand
*  what's the representation of the relation between the subject and the object. And the LRE paper
*  explores that and finds it in a bunch of the cases. The relation can actually be understood
*  as a linear mapping, but it's actually sort of an incomplete story because we found that for a lot
*  of the cases, there's something more complex going on. There's something that looks nonlinear.
*  And so it opens the door to future research, new tech to ask what's going on in the more
*  complicated cases. These relations are sometimes really non-trivial. And I think that there's going
*  to be some interesting, exciting work to do to figure out like, why is it that the models
*  are modeling some relations in a really complex way? What are they getting out of all that complexity?
*  And is it enabling new types of reasoning that we haven't characterized yet?
*  Cool. That's awesome. I look forward to that one in more detail in the future as well.
*  Koena, let's get into the FutureLens paper where you're the lead author. This one really called
*  out to me pretty much immediately because I think you were speaking to it a moment ago as well,
*  where you're saying there's a school of thought out there that's like, this is all stochastic
*  parotry and there's no real understanding and it's just next token prediction. So I'm always
*  interested in things that explore like when mere next token prediction can in fact be a bit more
*  than meets the eye. And this paper is a really good example of that. So you want to start off
*  maybe by just talking about the specific motivation for this particular investigation within the
*  broader agenda of the group? Yeah. So actually the way this problem started was like a little
*  different from how it was before. Initially, I was interested in looking at memorized content
*  in large language models because when you use chat GPT or any other models,
*  some things that I've noticed like license codes, for example, if you just give a couple
*  tokens in, you kind of know the next 11, 20 tokens that tend to be exactly the same
*  from its training data. So initially I was actually first exploring that. And while I
*  was exploring that, I tangentially went to this point where like, okay, well, I can see that it's
*  saying these tokens pretty much like word to word, but like, how about for smaller phrases
*  like New York City and stuff like that, which for us, we consider that as one whole entity.
*  Yeah. That's how it started off in terms of just looking into seeing whether one, a single hidden
*  state, can we actually decode such information from that? And yeah, we were exploring ways
*  that you have seen in the paper in terms of to what extent can we decode that feature information
*  about a particular entity or like just anything in general at this point.
*  So the question as it's a reading directly from the paper in this work, we asked to what extent
*  can we extract information about future that is beyond the currently under consideration token
*  from a single hidden token representation? So let me again, just pitch you how I understand this
*  work and you can correct any misconceptions that I have and think the vocabulary, especially for
*  people that are not in the research can sometimes be a barrier to entry. So if I understand correctly,
*  what you're doing here is looking at activations within the forward pass of a large language model
*  as the numbers are getting crunched. I sometimes like to use the most basic terms I can. The
*  numbers are getting crunched from beginning to end and between the layers where the actual
*  intensive computation occurs, there are these kind of middle states, which are known as activations.
*  You are taking an array of numbers basically that sits there at different places and we can get into
*  more details of the different places that you can look. You can kind of look at every given layer,
*  right? Through the transformer to see a different activation. But the question you're always asking
*  is given this array of numbers, these activations, can I predict not just what the current token is
*  going to be as I'm working through that forward pass, but can I also see what the future tokens
*  are going to be just from the information that's in that one particular vector of numbers? Is that
*  right? That sounds about right. Yeah. Like we just termed those activations hidden states because
*  those are like hidden and they are part of the intermediate computation and stuff. Hey, we'll
*  continue our interview in a moment after a word from our sponsors. AI might be the most important
*  new computer technology ever. It's storming every industry and literally billions of dollars are
*  being invested. So buckle up. The problem is that AI needs a lot of speed and processing power. So
*  how do you compete without costs spiraling out of control? It's time to upgrade to the next
*  generation of the cloud, Oracle Cloud Infrastructure or OCI. OCI is a single platform for your
*  infrastructure, database, application development, and AI needs. OCI has four to eight times the
*  bandwidth of other clouds, offers one consistent price instead of variable regional pricing. And
*  of course, nobody does data better than Oracle. So now you can train your AI models at twice the
*  speed and less than half the cost of other clouds. If you want to do more and spend less like Uber,
*  eight by eight and Databricks Mosaic, take a free test drive of OCI at oracle.com slash cognitive.
*  That's oracle.com slash cognitive, oracle.com slash cognitive.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that actually work,
*  customized across all platforms with a click of a button. I believe in Omniki so much that I invested
*  in it and I recommend you use it too. Use Cogrev to get a 10% discount. Hey everyone, Eric here,
*  the founder of Turpentine, the network that produces the cognitive revolution. This episode
*  is brought to you by ODF, where top founders get their start. ODF has helped over 1,000 companies
*  like Traba, Levels, and Finch. Meet their co-founders and go on to raise over $2 billion.
*  Apply to the next cohort of ODF and go from idea to conviction on what's next. Startups change the
*  world. They can also change your life. Is it your turn? Learn more at beyondec.com slash revolution.
*  The predecessor, I suppose. So, Logit Lens is essentially the tool where it projects these
*  intermediate states into the decoding layer. So, essentially we can just see for that current token
*  prediction, what is the model currently thinking about? Like based on the distribution and when
*  you decode it to the highest probable word, what is the model currently thinking? I recommend anybody
*  who's listening to the podcast who hasn't seen Logit Lens before. This is not our work. This is
*  somebody else's work. So, there's a blogger, a nostalgic person who created this idea of
*  Logit Lens. You should Google it and take a look at what Logit Lens looks like. It's these beautiful
*  grids of words that are overlaid on all the hidden states of the transformer, where every hidden state,
*  every one of these vectors that's inside a transformer, all of these intermediate numbers
*  are all translated into a word. And then at the bottom layers, at the very earliest phase of the
*  transformer, you can see what words the transformer is basically internally thinking. And then as you
*  go through more and more layers, the words evolve until you get to the end. And you can see the
*  predictions of words get more sophisticated as you get to the end. It's always guessing what the next
*  word should be that it should say. And those guesses get better and better the deeper you go
*  into the transformer. It's really interesting to look at the Logit Lens.
*  Yeah, the biggest advantage is you only see what it's currently thinking, which may not
*  be representative of what it might be actually thinking about a couple of tokens ahead. It's
*  not as informative in that sense. And so we are trying to make it more informative and saying,
*  okay, it's currently thinking of the word new. What word is it thinking after new? Is it thinking of
*  New York, New Jersey? These are some examples of things that could follow new, but that's not
*  possible to see with Logit Lens for that particular hidden state, at least.
*  Yeah. So there's two directions that we can consider. Tell me if this intuition
*  jives with your understanding. In the course of the forward pass, basically, this is what the
*  Logit Lens looks at. It's like as we're going layer by layer, we're sort of gradually getting
*  more sophisticated in the way that the model seems to be understanding the input and it's gradually
*  converging to the prediction that it's actually going to make. So you can see at the beginning,
*  it has a low level of confidence and maybe wrong if you just took that hidden state and went
*  directly to decode. And that would be basically like, okay, let's say we do two layers of
*  computation, then we skip all the rest, and then we decode whatever came out of the two layers.
*  Instead of all the layers, what would we get? What we get is not very accurate at two layers. It gets
*  more and more accurate as you go through the layers as it finally reaches its output, which
*  makes sense, right? Because that's presumably why we need all the layers is to be working through
*  the information and gradually getting somewhere. And then there's also the token direction, right?
*  We've got like a sequence of tokens and information can only flow forward because that's the nature of
*  the look back attention mechanism. So it can only flow forward from tokens to future tokens,
*  but that means, or at least it stands to reason, right? And this is what you will then set out to
*  prove that as this information is built up from prior tokens to the current token,
*  it probably means that there's more there than just what would be needed to predict the immediate
*  token. And there's been like lots of interesting intuitions around this with even just articles in
*  English, right? Like if you set up a situation where it's very clear that the actual noun is
*  going to begin with a vowel versus a consonant, then you can see that it predicts the article
*  correctly. And then you're like, huh, that's pretty suggestive that maybe there's more
*  information there. Otherwise, how would it be choosing the article? It seems to be anticipating
*  what's coming beyond this current token as well. So I think of the information processing proceeding
*  like vertically and the token information flow proceeding horizontally. And now we're in this
*  moment where it's okay at each layer through the forward pass through the vertical dimension,
*  we can check to see like, would this be enough already to predict the current token? And again,
*  that's the logic lens kind of based on what you're building. Now we get to, okay, can we also
*  detect that future token information is there, right? Yep. Okay, cool. So tell me how you did
*  it. First of all, I noticed that this was done on GPTJ. That was kind of surprising, but maybe I'm
*  just not sure what I don't know about GPTJ. It seems like these days this is like Lama would be
*  the default for this sort of thing. So how did you choose the model? Again, since this was like a
*  spin-off from the earlier project that I was talking about. So I was using GPTJ and I just
*  continued with it, but it was definitely like one of those models where I could run it on like a
*  single GPTJ. Do we have a picture lens on Lama now? I think people are building it. If it has the same
*  vector size, like 4096, then you can technically do the whole transfer. But yes, generally this
*  method should be workable for other models as well. Yeah. Let's get back to the other models
*  in a little bit because I have some questions around like how you think the different models
*  might behave differently under this sort of examination, but it'll help to establish exactly
*  what it is we're doing. And you said the activation vector, this was actually one of my questions,
*  the vector from which you are predicting, that's a 4096 size vector? And like the number of tokens,
*  but then that would be one for us. So yeah. Okay, cool. So then tell me about the data set. So this
*  is the first, as is so often the case, the first challenge in doing something like this is you've
*  got to collect a data set. This one, it's kind of a subtle one to describe. Yeah. So since I knew that
*  GPTJ was trained on pile, I was like, okay, why don't I take the pile data set and sample
*  a couple of texts from it and just get the hidden state from each of the sentence in there and yeah,
*  I'll run it. So I collected like a hundred thousand of them. One of my initial condition was if it is
*  GPTJ itself, if it is reading this one token, that it's predicting the next token correctly
*  in that sense. And so that's one of the few sample conditions that I had, but otherwise, yeah, once
*  I got like a hundred thousand of them, I stopped and then I was experimenting on that. So it's a
*  hundred thousand samples of texts with what's the filter that you used in that? Oh yeah. The filter
*  that I used was that given the last text of the prompt, that the next one, it predicts correctly.
*  The model predicts correctly. Yeah. Okay. So there's a hundred thousand prompts identified by
*  the condition that the model must get the next token correct per the actual source material.
*  So what are you actually collecting for each of the hundred thousand? It is the activation,
*  right? Or the hidden state for each of the layers throughout the entire transformer? Yeah. That's
*  what eventually happens. But in terms of just storing purposes, I had just the CSV file of these
*  a hundred thousand sentences, but then later during the training process, I would gather the last hidden
*  state of it at that particular layer for whatever like probing or a method that I'm trying. Because
*  all of the analysis downstream of this is going to be at a layer specific level, right? Yes.
*  Ultimately, the actual input itself would be the 4096 vector. But yeah, when I'm collecting all of
*  them, I'm collecting them based on the strings and stuff. So yeah. I always like to get very clear on
*  the inputs and outputs. So now we've got to the point where, okay, we've got the hundred thousand
*  texts and our goal is to say, for a given layer, can we figure out a way to take that 4096 length
*  vector and use that as the input and then predict not just the current token, but the next several
*  tokens from that single input vector? Yeah, almost there. So definitely layer, but also the last
*  token. So if my prompt was 10 tokens, if it was layer wise, it'll be 10 by 4096. But since again,
*  it's just one token and a single hidden state will be the last token of the input prompt. And that
*  would be so that's one by 4096. Yeah. Okay, cool. And then just as validation, there's another
*  thousand that you'll do the testing on once you develop the methods. Okay, cool. So we've got
*  five distinct methods where the first one is the null hypothesis, which is just the
*  bigram, which is, okay, given the total frequency of word pairs in the entire pile data set,
*  to what degree can I just look at the current word and predict the next word solely from that? And
*  if you're guessing at home what that number is, I'll give you a second. It is 20%. Apparently 20%
*  of tokens in the pile. You can guess just from knowing the current word gets you basically to
*  20% accuracy. That was kind of surprising to me. I wouldn't have guessed it would be that high.
*  There you have it. 20%. Yeah. This language modeling is not so hard after all. You just get
*  20% from counting and that's it. The same gram thing was the state of the art method until not
*  too many years ago. Yeah, but it's not state of the art method anymore. So let's talk about the
*  four methods that you developed. And first one is direct vocabulary prediction. So here you take
*  that same 496 vector and just specifically try to jump directly to the logits, right? The final
*  percentage, it's not exactly percentage, but it's within a very short transformation from percentages
*  of the actual tokens to be predicted for the current and then the next few.
*  What is the nature of the thing that you're learning? This is because it's a learned method,
*  right? You're going to optimize and essentially learn a way to make this prediction across the
*  100,000 samples. What is the nature though of the vocabulary prediction thing that is being trained?
*  Yeah. So like the goal with this direct vocabulary prediction is essentially can we like literally
*  decode the token from that hidden state? I imagine the linear models would be the most basic
*  model for probing in terms of just being able to grab that token. And so yeah, that was essentially
*  the goal. We wanted to see whether there was some sort of linearity in like being able to just decode
*  what a future token is. Like is that stored linearly in the hidden state? So that is to be
*  very concrete, a one layer transformation. No, one layer, one token. So in some sense,
*  it's like context free, but yeah, it's one hidden state to one other hidden state. And each of them
*  is like one by four zero nine six. The thing that is being trained, that is doing the transformation
*  from the hidden state to the prediction is just a simple linear transformation. And sorry, just to
*  correct myself earlier, since we were talking about the vocabulary prediction, it's actually
*  one by four zero nine six to five zero four zero zero. So essentially the way this vocabulary
*  prediction is that the GPTJ, if we were to tokenize the words, the size, the vocabulary space of
*  GPTJ is about 50,000 tokens. And we are essentially trying to get that vector of like 50,000 tokens and
*  choose whichever is the highest probability as the token that would be predicted. So that's for the
*  linear direct vocabulary prediction. And so, yeah, that's why for this particular method,
*  we grab in the hidden state, which is again, four zero nine six vector. And then that's two
*  five zero, like that 50,000 size of like one token. You're literally training a decoder,
*  your own decoder head on this problem, right? Yeah. It's like training a little linear classifier.
*  So the number of parameters in that linear classifier would be four oh nine six times the
*  50,000 vocab size. Yep. So essentially each number in the hidden state makes a contribution
*  to each output token. And the intensity of its contribution is determined by the parameters,
*  which are learned in the training of this linear. That sounds right. Yeah. Okay, cool. So that's
*  direct vocabulary prediction. So we got a hundred thousand of these four ninety six vectors. We know
*  what the actual next tokens are. And we're training this mapping of four nine six by the
*  vocab size to do that mapping. Hey, we'll continue our interview in a moment after a word from our
*  sponsors. The tech world turns to the brave browser for its unbeatable privacy protections.
*  But did you know that brave also has a private ad platform? Brave ads offers first party targeting,
*  and it's been cookie lists since day one. So you can relax while third party tracking cookies
*  disappear from the web. Today, millions of people turn to ad blockers to avoid being tracked and
*  pestered online. But brave's new ad model aligns incentives for users and advertisers.
*  Users earn rewards for viewing ads, which they can save, spend or pass along to their favorite
*  creators. And advertisers score points for respecting user privacy, generating ROI without
*  invasive tracking. So whether it's high impact announcements on the new tab page or keyword
*  targeted ads in brave search brave offers diverse, private, future proof ad formats for all your
*  business goals. Join the future of advertising at brave dot com slash ads. Mention M.O.Z. When
*  signing up for a 25 percent discount on your first campaign. Today's podcast is brought to you by
*  Plum. If you're a startup building A.I. features for your customers, you're probably feeling the
*  pain of hallucination, prompt testing, unstructured responses, subpar queries for embeddings. And of
*  course, the mind numbing process of general iteration and refinement. When your engineers
*  have to make every change by hand, that's where Plum comes in. Plum is a no code A.I. app builder
*  designed for product teams who care about quality and speed. Check out useplum.com. That's Plum
*  with a B for early access. Hey all, Eric Torenberg here. I'm hearing more and more that founders want
*  to get profitable and do more with less, especially with engineering. Listen, I love your 30 year old
*  ex-fang senior software engineer as much as the next guy, but honestly, I can't afford them anymore.
*  Founders everywhere are trying to turn to global talent, but boy is it a hassle to do at scale from
*  sourcing to interviewing to on the ground operations and management. That's why I teamed up with Sean
*  Lanahan, who's been building engineering teams in Vietnam at a very high level for over five years
*  to help you access global engineering without the headache. Squad, Sean's new company, takes care of
*  sourcing, legal compliance, and local HR for global talent so you don't have to. With teams across Asia
*  and South America, we can cover you no matter which time zone you operate in. Their engineers
*  follow your process and use your tools. They work with React, Next.js, or your favorite front end
*  frameworks. And on the backend, they're experts at Node, Python, Java, and anything under the sun.
*  Full disclosure, it's going to cost more than the random person you found on Upwork that's doing two
*  hours of work per week, but billing you for 40. But you'll get premium quality at a fraction of
*  the typical cost. Our engineers are vetted top 1% talent and actually working hard for you every day.
*  Increase your velocity without amping up burn. Head to choose squad.com and mention Turpentine
*  to skip the wait list. Then there's kind of two variations of this, right? The first one is the
*  direct vocabulary prediction. The second one is the linear model approximation. And if I understand
*  correctly, the difference is whether you're jumping straight to the output tokens is what you're
*  predicting or keeping the existing decoder and instead trying to predict something that then the
*  decoder would properly decode. Exactly. Yeah. One is to the vocabulary distribution. And then the
*  other one is to the hidden state, which the decoder layer would decode it to that ultimate token. Yeah.
*  And that's pretty interesting. I didn't have too much of an intuition for like why one might be
*  thought to work better than the other. And then it seems like it basically turned out that they
*  roughly work equally well, like almost uncannily similarly. Yeah. Actually for me, that was a
*  little surprising because I would have assumed that because for the vocabulary distribution,
*  like it's also trying to learn how to decode, like it's creating its own decoder thing. I thought it
*  will take probably more number of iterations or basically a lot more data for it to come to that
*  stage, but it works similar to how if you just predict the hidden state and have your decoder
*  layer handle that. Yeah, it works similarly. So that was pretty cool to see. Yeah. Is there something
*  that we can understand about the broader system based on the fact that those two approaches work
*  the same? Like it seems you basically have two linear classifiers and you can't like two is not
*  better than one is kind of an interesting way to see that. Right. I guess one way to interpret that
*  would be that you really are getting toward the max of the information that is there. I guess
*  another thing you might try would be like a bigger, more, you can train a full transformer to do this
*  sort of thing. And maybe you did, but I guess if two linear classifiers aren't better than one,
*  then maybe you'd think we've already maxing out. Is that how you would interpret that?
*  Yeah, that's how it interpreted. We wanted to start with a quote unquote simpler solution,
*  like having some sort of linearity with decoding future tokens. That would have been like a nice
*  final solution, but we realized that no, it's a lot more complex than that, at least at the moment.
*  And so yeah, that's what we tried. We tried our best to max out the linearity aspect of our
*  experiments. Okay, cool. So that's one class of thing, training these linear classifiers.
*  And then the other class of thing is basically an approach where you take the activation out of the
*  context in which it was generated and port it over to and kind of stitch it into a broader
*  forward pass context where that other forward pass context is engineered to be as neutral as
*  possible, or I guess ultimately engineered to allow that activation to shine through and get
*  its content through to the predicted tokens as effectively as possible. So the first way I thought
*  was super intuitive to do that, you just set up the prompt with, hello, could you please tell me
*  more about, and then port in the activation from the other context where however much information
*  has been aggregated at that final token is now being ported in. And the theory there is like,
*  well, because hello, could you please tell me more about is so generic, then in theory, whatever you
*  put there should set it up for a kind of nice, clean continuation. Unfortunately, that one didn't
*  seem to work so well. So I was surprised by that. What do you think is up with that?
*  It's because perhaps it was too generic in that sense. Well, yes, we were targeting generic prompts
*  so that it has the possibility for whatever the intervened hidden state is to like ultimately have
*  that token shine through, but it was probably still too general. The prompt wasn't really optimized
*  for it to be like, Hey, I want the future tokens out from this particular state. And so that's why
*  I feel like it didn't work as well. We tried a few, right? It didn't really work that well.
*  Yeah. Before I gave a couple sentences, I literally started with start of text or just a dot opening
*  bracket. Yeah. I tried a bunch of them, but they didn't seem to work as well either. Yeah. But it
*  was working a bit better than linear models, of course, but still not really as great.
*  Yeah, that's interesting. Okay. So now what comes next though is perhaps even more surprising in
*  view of the fact that you tried multiple actual natural language prompts and none of them worked.
*  The next approach is saying, okay, well, you know, where we're going, we don't need language.
*  It's the soft prompt technique, right? Where this time you're learning what the embeddings
*  should be from a sort of hypothetical abstracted prompt. Like what would the ideal prompt be if we
*  didn't have to represent it in tokens and we could just go straight to the numbers and engineer it
*  at that level so that we could get the tokens out the other end that we want. So in this case,
*  the optimization is tweaking those embeddings across all of the activation to future token
*  prediction pairs. And by optimizing those embeddings, now you can really start to get
*  somewhere. Yeah, that sounds right. That's exactly what we did. That's surprising. What kind of jumps
*  out at me, obviously, now looking to the results, that method works by far the best. And how do you
*  understand why that works so much better? Is there any ability to say what the ultimately learned
*  soft prompt means? Can we translate that back into something that I can understand?
*  We were actually attempting to do that. We were like, okay, we found a soft prompt that works
*  great. Let's try to like get a discrete one, but it was pretty gibberish. So it was like, okay,
*  we'll keep it in like the vector space for now. How gibberish was it? It had like a couple of
*  ads somewhere and it had some like, they looked like words, but then they didn't make sense kind
*  of words. Those were what was there. Yeah, it was pretty gibberish. So we just went on with the
*  vector space soft prompt. But yeah, in terms of the results, it was nice to see that there was a
*  pretty significant increase. And the reason I imagine is because this prompt is trained so that
*  whatever intervened state we have, it enhances whatever the future context is encoded in there.
*  And so because in the manual versions, we were thinking of what the prompts could be, like what
*  we think would make sense. But over here, this is what made sense to the computer. Yeah. It's amazing
*  that basically there's this little capability in the transformer to solve this problem, right? To
*  tell you what the future tokens are. It has some little machine in it that knows how to decode it.
*  And Cohen with her soft prompt training basically came up with a prompt that is like a key. They're
*  like, it's sort of this capability to do it. At least that's the way I see it. But the key
*  didn't seem to correspond to any real piece of text other than this weird gibberish that she saw,
*  right? Yeah. It wouldn't have been something that we could have predicted. It reminds me very much of
*  the universal jailbreak paper, which we did an episode on and there was sort of a similar,
*  now they were operating in token space, but still often found these universal jailbreak prompts to
*  be gibberish sequences. And sometimes they did have some that were like more human readable.
*  Now, this was something that you guys did a lot, right? Like all of these techniques are happening
*  at each layer. So for each of these techniques, you had to train like for the soft prompts,
*  there's what, how many layers in GPTJ is it 28. So you had to train 28 different soft prompts,
*  one for each layer at which you're going to patch in the activation.
*  So that was what the method was initially, but like the actual future lens, the tool,
*  we just use one soft prompt. We use the best model, the best layer that worked. We did that for every
*  state when we actually built the tool. So in the tool it's like one, but then we were using this
*  method to find which was the best soft prompt to use, if you may. Yeah. Gotcha. Okay. So yeah,
*  let's talk a little bit more in detail about the results. I think these are suggestive of many,
*  certainly it's a good graph to just sit and ponder for a little while. Again, folks can refer to the
*  paper to see this is figure four from the paper. Basically what you've got here is four different
*  graphs. Each one corresponds to the token that is being predicted. So N equals zero. The first
*  graph is like predicting the current token, then it's N equals one. The next token, two, the one
*  after that, three, the one after that. And then for each of these predictions, you're able to look
*  at, okay, put the layers across the X axis and the success rate on the Y axis. And you can see that
*  as you proceed through the layers, the prediction success changes. For the first token, the current
*  token, basically you recap the logic lens results, right? Where you can see that as you move through
*  the layers, the predictions get more and more accurate by the time you're at the end by
*  definition-ish or close to definition-ish at the end, you're getting the answer right close to 100%
*  of the time. Yeah, that was our sanity check for N equals zero. We were like, okay, is this method
*  actually working? Let's make sure it's actually decoding the current tokens. Yeah, that was more
*  of a sanity check. So then several things jump out at me about the next three. One is that, again,
*  we've already said that the two linear projection methods basically worked almost exactly the same.
*  Like you can see that those lines for tokens one, two, and three are in almost lockstep through
*  every layer. Those did not work that well. And in fact, and this is kind of surprising too,
*  on the first token, they beat the 20% baseline a bit. But then on the second and third tokens,
*  they're actually worse than the baseline. I guess maybe the baseline is out of domain there at that
*  point anyway, but I wasn't expecting to see things go lower than the baseline really. Yeah, I assume.
*  So we created the bigram baseline. And so for N equals two, N equals three would be trigram and
*  the four-gram models. They were too huge for us to compute at that time. And so, yeah, that's why we
*  didn't include the 20% in there. But yes, it's more to do with the fact that it was trying to predict
*  two tokens ahead, three tokens ahead. So the baseline is not so relevant past just the immediate next
*  token. So you probably don't have a paper with those methods, right? Because they didn't work
*  that great. The next one is the fixed prompt. This one actually does go below the baseline on the first
*  one. So again, I'm like, man, that seems weird. Why would it be lower than the straight baseline?
*  And even to make that more confusing, that method seems to get better for the subsequent tokens. Like
*  it's worse at predicting N equals one, and it gets better at predicting N equals two and N equals three.
*  And that really surprised me. So to provide a bit more context. So when we were checking N equals
*  two, N equals three, we assume that we give like the correct token for the previous ones. So let's
*  say we are talking about New York City, for example. Let's say N equals zero is predicting New York.
*  One is York. Two is city. And so let's say because there are so many possibilities after New York that
*  it doesn't really predict New York. But if we give New York, if not, if we give New York, if we give
*  York, can it actually then predict city? And so that's the idea behind checking for two and three.
*  Because generally, if one is wrong, then it's pretty sure that two and three will be wrong if
*  you check whole phrase wise. So that's why, yeah, we gave one extra token context in that sense. But
*  with that, it's essentially the same thing with one additional token, but nothing else, like whatever
*  the current token was. Can you help me understand that a little bit better when I am imagining
*  porting an activation over two different contexts? How should I understand that mechanistically
*  interacting with the idea that there's another kind of subsequent token included?
*  Yeah. So when you do transplant that hidden state to the fixed context, yes, it's actually completely
*  from a different step at this point. Let's say we did this transplantation at like layer 14.
*  So from layer 14 onwards, it would have the context that is present in that hidden state.
*  But if sometimes that's not enough, as we saw in the fixed prompt result, like n equals one.
*  But let's say if we gave that particular hidden state plus what the next word could have been,
*  so like York in that sense, maybe the reason why it's performing better, it's okay, because it now
*  has like a direction of like where it can predict next. But even then, it's just that hidden single
*  hidden state and that particular one token. So interesting. So with that method, it's getting
*  more information. Does that also help me understand? Because another thing that I was
*  quite surprised by is that the performance of that fixed prompt method seems to be
*  pretty clearly declining as you go through the layers. And whereas the first two, the linear
*  transformation ones are like flatish climbing a little bit, the fixed prompt one is declining.
*  And I was like, hmm, that seems like a very odd reversal from the main logit lens. Do you have an
*  intuition for that? And does that have something to do with the extra tokens that it's given?
*  So yes, in some context, but usually the way I imagine just as the first like last layer is that
*  from beginning, it's kind of build an understanding of what it's going to say. And then in the middle,
*  it has these set of ideas that it wants to say and towards the end, it probably wants to say
*  immediately what it thinks it should be next. And so in that sense, I imagine there could be some
*  information lost along those layers when it's ultimately trying to predict literally the next
*  token in that sense. Yeah. Yeah. And what you just described is definitely my intuition as well,
*  the sort of gradual working up of inputs into higher order concepts through at least half.
*  And my general sense is that in many models even goes deeper than that. Because rough picture in
*  my head is more through like 80% of layers. And then yeah, in the final layers, it's like now we're
*  condensing again, like now it's time to actually cash this out all this sort of high order or high
*  concept work that happened in the middle. Now we've got to cash that out to a concrete prediction.
*  And so you see a collapsing toward the end. And that is very much what we see in the soft prompt
*  one. So a couple of notable facts about the soft prompt results. First of all, they're just a lot
*  better than everything else. And second, they do more follow this pattern that we both each just
*  described of seemingly more and more information buildup that's more useful rising line from the
*  beginning up until the middle layers and then declining. And just the sort of peak here is in
*  the middle. And I've seen later peaks in other models. My guess is that's probably just a
*  function of model size where you'd have to have that end time. And that limits how deep into the
*  model you can continue to build. Does that seem right to you? Yeah, that definitely seems right to
*  me. And the whole idea of like the middle layer importance, it is something that I've seen in other
*  papers as well. And yeah, there's definitely something along in those middle layers,
*  middle, late layers. It is interesting how it declines, right? It definitely suggests
*  that at the late layers, it's erasing some information that is using that space for
*  something else and sort of explains this decline over time. So I feel like the whole phenomenon of
*  a transformer erasing its own information is an interesting one. And we see hints of it here is
*  the cool thing to study. Yeah. What else do you take away from this set of results that I haven't
*  landed on myself? One of the things here is that the information is present, but we weren't able
*  to decode the information directly. Somehow the transformer's own circuits are essential for
*  decoding the information. That's a pretty interesting insight. The mental model I have is like
*  the transformer has its own dictionary in its weight somewhere of how to decode concepts into
*  sequences of words. I love the example that you chose in the final version of your papers,
*  Back to the Future, right? Like the movie title, Back to the Future, this is longer sequences of
*  words. And I imagine that it's not actually directly in the hidden state, the instructions
*  of how to decode Back to the Future, but it's more like a pointer. It's just this compact vector
*  that you have to look up in the model weights somehow. And it's that soft prompt that
*  Quentin and I learned that is triggering some mechanism that causes this lookup to happen
*  that eventually rolls out to the whole phrase, Back to the Future. So I thought this was pretty
*  interesting. If the decoding was simpler, we would have found it through one of these direct
*  decoding methods, but it's something that's the encoding is complex enough that the transformer
*  itself is needed. Yeah. So something I said earlier, maybe I'm now thinking is perhaps wrong
*  because I had said, okay, two linear transformations don't seem better than one.
*  And I jumped to the conclusion that like you could train a whole transformer, but it probably
*  wouldn't work. But now I'm thinking maybe that's exactly what would be needed. What does your
*  intuition say if you were to scale up the direct to go back to those first two methods, but instead
*  of using a linear transformation, what if you used a full transformer to try to do the processing?
*  Do you think that would work? Yeah, I think that should work better. Again, with when you introduce
*  a transformer, that's like the non-linearity thing, which was required for the soft fronting
*  like instances. So ideally it should work better, but that's not something we tried out.
*  I don't feel like we had enough data to try it. Yeah. So, you know, this was a relatively
*  small model training exercise you did, right? Where every layer and every token, all these
*  different settings, you're like training lots and lots of models. If you wanted to make a
*  prediction on a large model like this, you'd probably need to train on millions or hundreds
*  of millions of examples. And at that point, it's a little bit different. It's almost like the task
*  that you're trying to learn, you might be best off just memorizing the whole thing. You could just
*  say this vector corresponds to these tokens a few ahead and just memorize the whole problem.
*  The thing that really surprises me about what Koyyana found was that she didn't need to do that.
*  With a really pretty small amount of data, sort of a hundred thousand samples,
*  she could unlock the dictionaries for all of these phrases. And it wasn't like we're really
*  training the transformer to do something new. That's why it feels like we're unlocking the
*  knowledge that's already in the transformer. Does that make sense? Yeah. That's really interesting.
*  That's super helpful. And I understand exactly what you're saying about a hundred thousand data
*  points would not be enough to retrain a transformer. Maybe it could do the memorizing, but it certainly
*  couldn't possibly relearn all the stuff that the full GPT-J6B knows because there's no way to get
*  there from such a small sample size. So in theory, it could maybe work if you had the full pile and
*  you ran the full pile this way, but obviously that's not feasible on the resources available here. So
*  you can't recreate that magic. When we basically add in another transformer,
*  that kind of ends up becoming like a chicken and egg problem. Like we're trying to understand
*  this transformer, but then we now have to try to understand the method transformer.
*  Yeah. It's a bit absurdist, no doubt. And it becomes almost anti-interpretability at some point
*  as well. Yeah. That's definitely an intuition building exercise more so than a way to create
*  insight into how the things are working. How big is the soft prompt? I assume that individual tokens
*  are embedded in the same 496 space. Yeah. So the soft prompt size was like 10 by 4096,
*  assuming 10 tokens and each of this token having 4096 vector size. Yeah.
*  How's that compared to your linear models? Oh, linear model, like the input was like one by 4096.
*  Yeah. But those models were like 4096 by 4096. Like your soft prompt is way smaller. Yes,
*  that is true. It is much smaller indeed. Yeah. So even though it was the best performing thing,
*  it was like the smallest number of parameters. It'd be like a thousand X difference, right?
*  Because the linear transformation were 4,000 times 50,000 parameters and this is 4,000 times
*  10 parameters. That's true. But I guess like the trade-off is the linear model's trying to
*  understand everything what we technically do have. We have the transformer helping us out,
*  but the weights are frozen. That's true. Yeah. That's right. It's the power of using the
*  transformer to explain itself. Yes. Yeah. Okay. That is really definitely very insightful. Did you
*  try also varying the length of the soft prompt? My mind goes to what if there were no soft prompt
*  at all? Yeah. My co-author, Juning, he definitely tried out a couple of variations of the prompts
*  and found out that the size was like a good enough in that sense for this. And I'm not sure
*  if he tried zero prompt, but I assume that would work similar to a fixed prompt size, just because
*  it is like a fixed prompt. Yeah. It's something we don't know in detail. We didn't see anecdotal
*  evidence that it made a huge difference to make the prompt different sizes. So we just picked a
*  relatively small prompt and tested it. Can we go back to the fixed prompt again for a second? I'm
*  still a little kind of not content with my understanding of why that would actually perform
*  worse than the bigram. I don't know. I would expect it to do better. I'm struggling. That feels
*  like such a natural idea that it seems like it would work better than just such a simple statistic.
*  And yet it's worse. And all of the ones you tried were worse. Like there were none. I assume that
*  you didn't pick the worst of the- No, no. This is the best one. My intuition is this. So we show
*  these various successes. The function vector paper is an example of this, where if you like go and
*  intervene directly in the hidden states or the wrong paper, you go directly intervene in the
*  way to the model and we show, oh, it does something amazing. But actually this isn't generally the
*  case. Imagine sticking random probes into somebody's brain and then saying, hey, I wonder if this will
*  make you smell the scent of bananas. But generally it's not possible to have a success with an
*  experiment like this. So despite our best efforts at prompt engineering, some very clever thing for
*  the model to be set up to do this, just jamming in this hidden state at the end of these engineered
*  prompts, it just didn't work. It's just doing some sort of brain damage. It's really not getting it
*  to predict anything very useful. Obviously, like you say, like a natural thing to try.
*  Yeah. Fascinating. Certainly we can say it's out of domain, right? You're putting it into a state
*  that is clearly very unnatural where all of a sudden, and you still have more computation to
*  go from that particular place of patching. So yeah, that still feels weird, but it's far enough out
*  of domain that it just can't handle it. And it's possible that there is some way to make this work
*  that we weren't able to figure out. So we tried our best with a bunch of different setups for this
*  manual prompts, and this is the best example that you can see. But it's certainly possible
*  that there's some structure that we're missing or some clever way of setting it up that would make
*  it work better. In fact, so we could talk about the function vector's paper also later if you want.
*  There are some other tricks that you can find to get these kinds of interventions to actually work
*  pretty well. I was curious if people like me are still feeling like they want to go try another
*  fixed prompt and see if they can't find the magic words to make it work. What does the tooling look
*  like for all this sort of stuff? What does the coding look like? There are no variations of ways
*  to do about this. But when I was working on the fixed prompt stuff initially, I was using
*  actually David's VowKit tool, which allows me to look into a model, trace it and grab the hidden
*  state and put it in like another run. But then there is a very recent tool called Insight,
*  which also does this. It's basically like a successor of VowKit. And it allows us to do all
*  these like patching interventions and all these just basically a few lines of code.
*  Yeah. You have open source release for this project, right? Yes. We call it future.biolab.info.
*  And yeah, over there we do have the code as well. And yes, basically in the code, I have
*  like notebooks and scripts and yeah, people can refer to that in that sense. So yeah, so definitely
*  check out Karina's repo for trying that people can try their hand at seeing if they can get a
*  clever prompt that works better or some variation on the method. We'd be delighted to see if there's
*  some clever trick that we missed. There's definitely room for creativity in this direction.
*  Absolutely. So you give a pretty good intuition already for what that would look like. You've
*  got the open source code. You've got a library that's specifically designed to facilitate this
*  activation extraction and patching and the loops surrounding that. To actually run a test,
*  I should be able to do this probably in just even like a Google collab notebook, right? I would think.
*  Because of the model and everything, you might need a Google collab pro. I haven't run the
*  training part, but again, the testing part with the future lens, I've tried it on collab pro and
*  it works. Have you used the end of backend? Yes, I know I used it on the server actually,
*  but not necessarily remote equals to because I was like, I'm on the server anyway. You're a little
*  bit of a cheater because you're sitting next to the implementer. But actually a lot of the students
*  who are playing with future lands and these kinds of things, that library was developed by Jaden,
*  his good friend Jaden. And the library supports a remote backend that we're trying to get funding
*  to provide the scalable free backend for people to do interpretability research. We call it the end
*  if backend. It's like a deep inference fabric. And so if you code your interpretability experiments
*  using this idiom, this little library, then, well, if you have the GPUs to run your model,
*  then you can just run them locally. But if you don't, if you need resources to run a model that
*  is too big for your laptop or for your collab environment or something, then you can just flip
*  a flag. You can just say, use a different backend and then the experiment will be run on a shared
*  remote backend for you. So yeah, there's, we have GPDJ running and we've got different llama models.
*  Yeah, I think the 7 billion model as well as, yeah, like llama 70B, which is a pain in the neck
*  to run on your own, but we have that running. Cool. So you have a single library that kind of
*  abstracts away the subtle, I mean, all these things are transformers, of course, but they have
*  differences in terms of their implementations, vector sizes, et cetera. Oh, no, they're not all
*  transformers. Like we have folks using it to study Mamba, for example, the state space models.
*  That's definitely of strong interest to me. Yeah, it's pretty fun stuff. Okay. So people who are
*  interested in this library, it's embryonic, but it's pretty cool. And there's a really nice
*  dynamic community around it. So the library is called nsightnsite.net is the URL to get to it.
*  We haven't really promoted it. So I don't know if you search for it on Google, if it'll come up even,
*  right? It's a little bit of a secret alpha stage project right now. But if you go to nsite.net,
*  there's an icon in the corner to link to a discord channel to join. And there's a bunch of tutorial
*  and documentation on it. But the really valuable thing is to just join the discord and ask around.
*  And there's a really friendly community that's developing it. That's awesome. Is there anything
*  that we can say about the bigger or more intensively trained models as compared to GPTJ? My hypothesis
*  would be that you would probably find higher success rates with bigger models because you
*  would in theory hope that they have more semantically meaningful middle state representations.
*  I would go along in the similar direction as well. It's just that with bigger models,
*  you also need bigger data set for it to potentially train and be more exhaustive in that sense. But
*  in terms of takeaway wise, at least till now, for example, the whole middle layer stuff,
*  I think it should still be something that is pretty transferable like other models as well.
*  As an advisor person here, I'll say this is a gap in our knowledge and we need to run some more
*  experiments. So you're right. I think the intuition that you have, which is that there might be more
*  structure as you get larger models and it actually might become more interpretable in this way,
*  is really interesting. It's a little counterintuitive. Traditionally, people would
*  imagine that as models get bigger, they might become less interpretable and harder to understand.
*  But this intuition that you're sharing here that maybe it becomes more structured, more predictable,
*  easier to understand. That might be true, but it would be quite a claim. So more research is
*  definitely in order to systematically take a look at these kinds of questions.
*  Is there anything interesting that you can share about the probes that have been sent into the
*  Mamba universe so far? I did for reference a two and a half hour monologue about the Mamba paper
*  in December. And I'm counting actually, along with another like-minded state space model fan,
*  I think we're up to very close to if not hitting 20 papers now published downstream of the Mamba
*  paper with different remixes and hybrid versions all over the place. So yeah,
*  have you found anything interesting there? Yeah, all these attention-free architectures,
*  you can basically ask how are they doing it. You can try to lay things like logic lands on
*  top of them or try to build future lands on top of them. And to some extent, they're maybe in
*  surprising ways, they show some similarities to transformers. Now we're sort of halfway through
*  doing some research to try to figure this out. And so I don't want to lead any of your listeners
*  astray by saying something that's not actually true. But yeah, even though they are missing
*  a traditional attention mechanism, they seem to be able to do some of the sophisticated types of
*  computations that transformers use attention for. So exactly how it all works, we're still
*  trying to untangle it. Yeah, cool. All right. I'm looking forward to that. If you don't have a
*  striped hyena in that menagerie already, definitely throw one of those in there at some point as well,
*  because I don't know if you've seen just from the last few days, there was a usage of the
*  striped hyena to do a DNA foundation model, which is starting to show some really interesting
*  properties. First of all, super long context. And striped hyena is a hybrid, so it has attention and
*  also the state space. And my sense definitely is that some sort of mashup is going to be the
*  winner for a lot of scenarios in the future. Certainly in this DNA paper that just came out,
*  they showed that the transformer was the least effective and then Mamba was a bit better, but
*  then the hybrid attention and state space was the best performing. And it is kind of uncanny because
*  it's sort of like, if you believe the theory that the language models are learning some sort of
*  world model representation through next token prediction, by analogy, this seems to be learning
*  some sort of life model or maybe better said, would be cell model at the level of just next
*  base pair prediction. It's a whole other world that's got obviously its own tremendous
*  interpretability challenges, but definitely fascinating space. So plus one for the striped
*  hyena in your next round of experiments. We will be investigating these things carefully.
*  It's a very exciting time. As the world potentially moves on to whatever comes after transformers,
*  it'll be very interesting. Yeah, I always say it's not the end of history. Do you want to talk a
*  little bit about the function vectors paper? So the basic question for function vectors was,
*  Eric was very interested in asking how does in context learning work? It's just this amazing
*  thing. I mean, it was the foundation for all the excitement around GPT-3 was this ability for a
*  model to seemingly learn how to do a task after seeing a half a dozen examples of the task being
*  done. Then you give it another half worked example and it'll work it the rest of the way.
*  It's just amazing that these models are so good at doing that. And so what Eric was looking for is,
*  is there some localization in the in context learning task? What he found was that there is
*  the bottleneck in it between when you give a set of demonstrations and when you ask a model to
*  generalize. Yep. Come and join. Eric Todd. Welcome to the cognitive revolution. So yeah, Eric is the
*  author of the function vector paper. So actually, maybe now that you're here, you can just sort of
*  explain what it is. Yeah. So we found that there are like a small set of attention heads that
*  when you process an ICL prompt that mediate the identification of a task, for example, let's say
*  you give a bunch of examples of like antonyms of big and small, short and tall, and then you
*  give it another query word like a bright and the model you can extract the output of a few attention
*  heads from some other context where they saw a bunch of antonym pairs and take this output and
*  stick it into this new context and it'll give you the antonym of the word that it's processing.
*  So if you take the same attention heads, yeah, and you read out what those same attention heads
*  are saying, if you said Paris, France, Moscow, Russia, Washington, D.C., United States,
*  and then you said Ottawa blank, right? But then you read the attention heads at that moment and
*  then instead you have a totally new context where you have Ottawa or something like that,
*  or you have mediate or something like that. Even though those attention heads were the ones that
*  seem to cause you to say antonyms in one of the experiments in this experiment, if you
*  read out the attention heads for the country capital task and you stick it in to the new
*  context, it seems to encode the new task. It'll actually say Madrid goes to Spain instead of
*  doing antonyms or something like that. And what other types of tasks did you test? You tested the
*  comment. Yeah, we tested like 40 plus different tasks and it seems like they're all mediated by
*  this small set of heads, which is kind of cool that it seems like the model has this sort of
*  path that it communicates this task information or like this bottleneck, I guess that it's
*  communicating what the task is that it's doing, even though in the prompts were never explicitly
*  telling it what the relationship between the demonstration and the label are. It's able to
*  figure that out and communicate it forward. Yeah, this is cool. I'll just resummarize it,
*  make sure I have it right. So you first of all set up a task implicitly with a few shot prompt,
*  which is the original GPTs are few shot learners, right? The original paper title,
*  few shot learners refers to the ability to understand or infer and actually do the task
*  just from a few examples. So pretty fundamental, notable behavior without question. So, okay,
*  set up a couple of these examples, thus creating a few shot prompt. One example is antonyms,
*  another example could be translation. So arrive, depart, small, big, common, rare. And then at that
*  point, as the pattern has been established, you go looking inside the transformer for,
*  is there some, I'd love to hear a little bit how you think about the term bottleneck,
*  but you're going in looking for some sort of relatively small dimensional thing that you
*  could extract and patch over to another context. And now when you find that thing, and obviously
*  that's where all the hard work is, but then the demonstration is that when you have found that
*  thing and you do in fact extract it now in a clean setting without any examples, you can set
*  something up and say the word fast means, and then inject this representation of give me the antonym.
*  And instead of doing what a language model would normally do, which is define what fast means,
*  now says the word fast means slow because you've forced the antonym behavior with the patching from
*  the few shot context now over to the clean context. Yeah. You're right about the bottleneck.
*  So attention seems like a natural place to look just because that's how transformers move
*  information between tokens. And we figured in order to gather information about the task
*  from your context, you'd have to do that via attention. Like if you never explicitly tell it
*  what the task is, you need to go back and look at all the other tokens to figure out what you're
*  doing. And attention is, it's nice because attention heads act on a small subspace.
*  And so they're natural bottlenecks for like sparse activations. So what is it exactly that you are
*  extracting and patching over? Is it the output from an attention head? Yeah, that's right. So
*  you can take the output of these, the small set and just add them all together. And that's the
*  actual thing that we call a function vector is this sum of attention head outputs. And then you
*  can add this vector into some other prompt at a particular layer in the model. So it's one vector
*  that represents the sum of multiple different attention heads, but you're selecting which
*  attention heads to look at. And obviously a big part of the challenge is figuring out which ones
*  to look at. Once you have that sort of thing, does the relationship between tokens need to
*  have some sort of length similarity to the original length relationship or not really because
*  all of the information passing between tokens has already happened by the time the attention
*  head is done, right? It doesn't need to. It doesn't seem like that matters that much.
*  Seems like fairly robust to different settings. So we tried sticking it into like natural text
*  settings, different templated settings. It seems like it works just the same for long or short.
*  Yeah. Isn't that cool? How do you figure out which attention heads to use? And what can we say about
*  the relationship between the different attention heads that together make the vector? It's nice to
*  think of this like single vector, but then it's weird to think of these different heads contributing
*  to like part of this sort of single conceptual vector. Yeah. So we found that a lot of these
*  heads have had a similar attention pattern, which is kind of interesting. Most of them were attending
*  to previous label tokens, which is like you have demonstration label, demonstration label. So they're
*  basically like looking at all of the answers of all the pairs, which kind of suggests that maybe
*  and some other papers have found, like when you do ICL, these label tokens seem to be sort of places
*  where the model stores important information. And so there must be something about the pairs where
*  it's able to figure out the task and it's transporting that task information from those
*  labels onward. The way that we found these heads was we do a process called causal mediation
*  analysis. Also, people sometimes call it activation patching. So basically the setup is you have one
*  sentence with a bunch of pairs of words demonstrating a task, and you have some other sentence where
*  you can set it up where it's maybe demonstrating some other task. We decided to scramble all of the
*  labels so that it wasn't really clear what the task was. And then what you do is you patch the
*  activations from one attention head into this other setting where it's not clear what the task
*  is doing. So you take it from the clean setting into the jumbled setting and measure how much it
*  influences the model's output of the word that you would expect the behavior to induce. So for example,
*  if in your jumbled setting, the query word is like big and you paste in an attention head output
*  from an antonym setting, you'd expect that the model's output for small would go up slightly.
*  And like just doing one attention head isn't enough to flip the prediction. So we started
*  trying multiple attention heads. And it seems once you get to around like 10, you can start having the
*  significant causal effects of getting the model to flip its prediction and start understanding
*  what the task is. So to me, the big surprise was Eric got this working for about 10 attention heads
*  for like antonyms. And then he looked at something else. I think in the paper, we looked at like
*  English to Spanish translation or something. He had a bunch of different tasks and he went and he
*  started looking at the attention heads for these other tasks. And we noticed that they were largely
*  the same attention heads. And so if you just picked up your attention heads from one task and
*  used them on a different task, that whatever information is in those same attention heads
*  would tend to induce the new task too, which was like, it was really surprising. Like I could
*  imagine that there's some antonym attention heads, but it was very interesting to find that there are
*  these attention heads, which are just like general function. Task understanding. Yeah. Yeah. That's
*  really interesting. And it looks like from the figure three in the paper, they're found mostly
*  in the middle layers, but not like all the same layer. They're kind of mixed at different parts
*  of the middle layers. Yeah. Most of them in the middle, maybe there was like one towards the end,
*  but yeah, it matches our intuition. I sort of see transformers as having two processes. One is figure
*  out what I want to from the context and then use that to predict the next token. And so like,
*  you can see maybe the first half of the network doing the figuring out in the second half,
*  using that to predict a token. And like, it's cool that right in the middle, right before it
*  like starts to predict the token is where this process is happening. Yeah, that's fascinating.
*  Obviously recently, mixture of experts has been a huge trend, right? With your GPT-4 allegedly being
*  a mixture of experts model and your mixed role. And of course now Gemini, a 1.5 has been declared
*  to be a big mixture of experts model as well. So I've been looking into what is known, what is
*  understood about mixture of experts. And it's like most of the mixture of experts papers are
*  focused on swapping out of the MLP blocks because that's where like most of the computation is,
*  at least if the context window isn't huge, but now obviously with context windows getting huge,
*  you know, that's starting to even out or maybe even tip the other direction. And so I guess
*  people are also increasingly starting to do a mixture of experts where the attention blocks
*  are also switched out at runtime. So I wonder how this kind of finding should help me think
*  about that. It certainly at first blush to me sounds like, geez, that's a pretty complicated
*  structure. Yeah, there is like, you've got 10 different heads and you could have had more,
*  right? If I understand correctly, you kind of drew a arbitrary line and said like, this gets us most
*  of the 80 Pareto principle type of thing. So it definitely seems like it's a sort of distributed
*  process. The process of identifying the task is a distributed process. It's kind of like
*  mixed throughout layers. Yeah, it is interesting. There's like two in the first
*  layer where they exist, two in the second layer, one in the third, one, one, one, one,
*  and then it goes quiet, at least in your top 10. I wonder maybe one way to think about it is maybe
*  there's like one to two of these per layer. I don't know. It's an interesting just mashup.
*  I wonder if you have any intuition for how this would help us understand mixture of experts.
*  Let me answer in my interpretability professor advisor way. I guess the way I look at it is it's
*  we don't know yet what is the right level of abstraction that we should be looking at
*  to understand these things. So we know the physical things that we made them out of,
*  that we have dimensions, we've got nonlinearities, we've got modules of different types,
*  we've got these NLP's and attention layers and cool state space recurrences and other neat things
*  that people have suggested. And so in the end, it's all just matrix multiplications, right? We
*  know what we're building these things out of, but we're not sure yet exactly the right way of looking
*  at all of these computations and the attention heads. So Roam was a way of looking at the MLPs
*  and say, Hey, there's this interesting association structure in these MLPs. It seems to be pretty
*  informative. Although amendment sort of qualifies that and says, well, you know,
*  might be distributed on a few layers and it's a little bit more subtle. And all of this great
*  mechanistic interpretability work, I think, has been a way of looking at all these attention heads
*  and saying, Oh gosh, these attention heads also reveal a lot of interesting computational structure.
*  And I think that motivated a lot of Eric's work. He says, Oh, is there an attention head? Maybe
*  there's a few. And so there's definitely a structure in the attention heads. To me, it's not
*  a hundred percent clear. That's the end of the story. That it may be like when Eric finds that
*  a dozen attention heads are working in concert with each other, then it leads to the question,
*  is there some abstraction? Is there some way that we should be looking at these attention heads
*  altogether? And I actually see function vectors as one proposal for a way of doing that, right?
*  You can summarize all of these attention heads in a single vector. And even though we've sort of
*  blurred them together and we've lost a bunch of the fine grain distinction, that vector has pretty
*  strong causal effects. It has some interesting properties that Eric investigated in the paper.
*  Like to some extent, these vectors can be composed and do interesting things. And so I don't know if
*  function vectors are going to be one of the abstractions in the end. That's like the right
*  way of looking at what these things are doing. But what it hints at is that there's potentially
*  more structure to be found, maybe at a higher level even than what we've been looking at so far.
*  And to me, the big game, the research game, the chase that we're all on in the interpretability
*  world is to figure out the answer to the question, what is the right level of abstraction?
*  That's great. That might be the perfect note to end on. And you guys are doing
*  admirable and certainly laudable job of chipping away at this massive problem. I'm a big fan of
*  all the work that I see. Anytime I see a Vallab paper, I'm excited to get to the website and you
*  guys do great visualizations as well. So definitely encourage people to go to the individual paper
*  websites and see the visualizations, the animations. For visualizations, let me give a shout out to
*  Nikhil who just archived his paper. That's also going to be at ICLR. We didn't talk about it
*  today, but he has the best circuit visualizations out of anybody. He really has done a really great
*  job at putting those together. So check out his paper. It's called Fine Tuning Enhances
*  Existing Mechanisms. So it's this whole study of the interplay between circuits and fine tuning.
*  And it's also an interesting paper, but really beautifully presented as well.
*  Yeah, we will save that one for next time. This has been a great conversation, guys. Eric Todd,
*  Coenipal and Professor David Bao. Thank you for being part of the cognitive revolution.
*  Thanks, Nathan, for having us.
*  It is both energizing and enlightening to hear why people listen and learn what they value about the
*  show. So please don't hesitate to reach out via email at tcr at turpentine.co or you can
*  DM me on the social media platform of your choice.

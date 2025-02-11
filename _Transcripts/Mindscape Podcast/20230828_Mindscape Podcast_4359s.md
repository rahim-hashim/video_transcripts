---
Date Generated: June 07, 2024
Transcription Model: whisper medium 20231117
Length: 4359s
Video Keywords: []
Video Views: 16482
Video Rating: None
Video Description: Patreon: https://www.patreon.com/seanmcarroll
Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2023/08/28/248-yejin-choi-on-ai-and-common-sense/

Over the last year, AI large-language models (LLMs) like ChatGPT have demonstrated a remarkable ability to carry on human-like conversations in a variety of different concepts. But the way these LLMs "learn" is very different from how human beings learn, and the same can be said for how they "reason." It's reasonable to ask, do these AI programs really understand the world they are talking about? Do they possess a common-sense picture of reality, or can they just string together words in convincing ways without any underlying understanding? Computer scientist Yejin Choi is a leader in trying to understand the sense in which AIs are actually intelligent, and why in some ways they're still shockingly stupid.

Yejin Choi received a Ph.D. in computer science from Cornell University. She is currently the Wissner-Slivka Professor at the Paul G. Allen School of Computer Science & Engineering at the University of Washington and also a senior research director at AI2 overseeing the project Mosaic. Among her awards are a MacArthur fellowship and a fellow of the Association for Computational Linguistics.

Mindscape Podcast playlist: https://www.youtube.com/playlist?list=PLrxfgDEc2NxY_fRExpDXr87tzRbPCaA5x
Sean Carroll channel: https://www.youtube.com/c/seancarroll

#podcast #ideas #science #philosophy #culture
---

# Mindscape 248 | Yejin Choi on AI and Common Sense
**Mindscape Podcast:** [August 28, 2023](https://www.youtube.com/watch?v=l2dhShGcb0E)
*  Hello everyone, welcome to the Mindscape Podcast. I'm your host, Sean Carroll. If
*  you are a fan of evolutionary biology, then you've heard of the theory of
*  punctuated equilibrium. This was an idea put forward by Niles Eldridge and Steven
*  J. Gould back in the 70s to think about how evolution works in contrast with
*  the dominant paradigm at the time of gradualism, right? In the course of
*  evolution, you build up many tiny little mutations and gradualism says that
*  therefore evolutionary change happens slowly. Eldridge and Gould wanted to say
*  that in fact you can get the kind of mutation where it speeds everything up
*  and it looks like there is some sudden change even though there's long periods
*  of equilibrium between the sudden changes. Physicists know about this kind
*  of thing very very well. There are phase transitions in physics where you can
*  have a gradual change in the underlying microscopic constituents or their
*  temperature or pressure or whatever which leads to sudden changes at the
*  macroscopic level. And by the way in biology, guess what? There are aspects of
*  both. There are gradual changes and there are also punctuated rapid changes. I
*  mentioned this not because we're gonna be talking about that at all today but
*  because I think that we are in the midst of a sudden rapid change, a phase
*  transition when it comes to the topic we will be talking about today which is
*  artificial intelligence. As I say later in the podcast, a year ago when I started
*  teaching my first courses at Johns Hopkins there was no danger that the
*  students writing papers were going to appeal to AI help. Now it is almost
*  inevitable that they will do that. It's something you can try to tell them not
*  to but they're gonna because the capabilities of the technology has
*  grown so very rapidly and has become much more useful. Very far away from being
*  foolproof, don't get me wrong. So that raises a whole bunch of issues and we're
*  gonna talk about a lot of these issues today with today's guest, Yajian Choi who
*  is a computer science researcher. She's done a lot of work on large language
*  models and natural language processing which is the sort of hot topic these days
*  in AI. Won a lot of awards up to and including a MacArthur Prize and one of
*  her emphases is something that I'm very interested in which is the idea of how
*  do you get common sense into a large language model. For better or for worse,
*  the ways that we have been most successful at training AI to be human
*  like is to not try to presume a lot about what it means to be human like. We
*  just train it. We just say okay Mr. AI or Ms. AI here is a whole bunch of text
*  you know all of the internet or whatever. You figure out given a whole bunch of
*  words what the word is most likely to come next rather than teaching it you
*  know what a table is and what a coffee cup is and what it means for one object
*  to be on top of another one etc. And that's you know surprising in some ways
*  how can AI become so good even though it doesn't have a common sensical image of
*  the world. It doesn't truly maybe arguably depending what you mean
*  understand what it is saying when it is stringing these sentences together but
*  also you know maybe that's a shortcoming maybe there are examples
*  where you would like to be able to extrapolate outside what you've already
*  read about on the internet and you can do that if you have some common sense
*  and it's hard if all of your training is just what is the next word coming up a
*  completely unfamiliar context makes it very difficult for that kind of large
*  language model to make process. So this is what we talk about today is it
*  possible for LLMs large language models to learn common sense is it possible for
*  them to be truly creative is there some sense in which they do understand and
*  can explain things and also will they be able to soon if they can't already right
*  now. Of course there's infinite implications we touch on these very very
*  briefly it's gonna change that's why that's the point of being in the middle
*  of a phase transition is that it's very hard to predict exactly where you're
*  gonna go because your intuitions are not that good your training is not up to the
*  task whether you are a human being or yourself a large language model. So my
*  attitude here is that we should keep an open mind this is not the time to be
*  doctrinaire this is not the time to firm up your priors and your credences so
*  much that you're not able to move them around this is the time to be open to
*  watch things develop to imagine what could happen but not try to be too
*  definite about what will happen until it actually is so that you can correctly
*  adapt to this brave new world that we're entering in so let's go
*  Welcome to the Mindscape podcast. Yeah I'm excited to be here. You know this is
*  obviously a big thing right AI is rapidly changing in front of our eyes it
*  wasn't that long ago that a Google employee started claiming that large
*  language models are sentient and I think he got in trouble for doing that as I
*  recall just so yeah there's always people who only listen to the podcast
*  for the first five minutes so are large language models sentient or are they in
*  any danger of becoming sentient anytime soon? Personally I strongly doubt that
*  anytime soon we will see that however people believe in what they want to
*  believe and some people believe in tarot cards so there's nothing we can do
*  about that. That's very true I did want to get in just a very tiny bit I think
*  that people have heard the whole idea about neural networks there's little
*  sort of neuron things and they add together in deep learning but the idea
*  of representing words as vectors is something that really had an impact on
*  me was that you know explain what that means maybe and was it a giant
*  breakthrough when people started doing that? Yeah the idea that I mean in some
*  sense the vectors especially based on the continuous numbers kind of makes
*  sense although it does seem weird because word looks very discrete and now
*  we are representing it as some sort of continuous vectors but it kind of makes
*  sense in the sense that we do tend to read a lot of nuances we do tend to see
*  like different nuances in the way that how the same word may be used in two
*  different contexts so the key idea behind the current vector based
*  representation of the word is that your meaning as a word has to do with the
*  neighbors in which you appear it's almost like you know a person's identity
*  may be defined by the friends that you hang out with so similarly it turns out
*  that key idea was some sort of like one of the key breakthrough ideas to better
*  represent the meaning of a language because before then a word was a word
*  and you know it's just like a discrete identity but that wasn't able to handle
*  all these rich meanings behind human language. As a slightly mathy person I
*  can't help but ask whether vectors are the best way to represent words or are
*  they just something that we are conveniently using temporarily I mean it
*  seems that one of the advantages is that you can imagine adding and subtracting
*  right like the example that I came up with was dinner minus evening plus
*  morning equals breakfast and this is the kind of thing you can do if you think of
*  words as vectors and I'm not sure if that's the best possible way to think
*  about it. Yeah no actually that's one of the surprising sort of like side benefit
*  of representing words as vectors that you can do that sort of analogical
*  reasoning it might be that even more broadly chat GPT in particular is able
*  to do perform that sort of analogical reasoning not just at the word level but
*  at a sentence level or even document level because it's able to handle
*  previously unseen users queries in a very impressive way and oftentimes
*  though the way that it handles is very sort of like you know lawyer style super
*  polite and hedged language that it uses is a fairly repetitive and even generic
*  to some degree and that's because it's doing that sort of analogical
*  interpolation between some examples that it has it has a sin before and then your
*  query that it needs to answer. I have noticed just from playing around with
*  various versions of GPT you know it will say things that are not quite true and
*  you can ask it like are you sure and it will correct itself so just this morning
*  before we started talking I was doing that and I asked it a question it gave
*  a wrong answer so I just asked exactly the same question again and its response
*  was oh sorry for my mistake previously so there's something about it that it's
*  able to recognize its mistakes but I'm not quite sure how. I wouldn't know for
*  sure whether that's truly annoying whether there was a mistake or not in
*  the following sense sometimes it's going to confirm that what it said was correct
*  sometimes it's going to super apologize and it's going to switch what it said
*  you need to kind of try in both ways by doing not only when it made a mistake
*  but also when it did not make a mistake and see whether it's actually able to be
*  truthful about what's actually true the truth is people do have a bit of a bias
*  that they ask are you sure only when they know for sure that it's not right so
*  then ChachiPT has learned that whenever people are asking that question probably
*  it's a good idea to back off but then if you ask the other way when it's like
*  corrected then you know you you ask whether it's really corrected then you
*  know it gets confused and then there was this recent reasonably recent news
*  headline about a lawyer that used the ChachiPT and got into a big trouble oh
*  yeah and you know what he did for fact-checking is to ask a ChachiPT is
*  it this all fact and ChachiPT said yes so that's where things are and this is
*  a huge challenge with large language models in the coming years and such as
*  like this year but in the coming years as well yeah something like ChachiPT
*  when you do ask it you know are you sure could you check correct me if I'm wrong
*  but it's only going back to it what it already knows right it's not searching
*  the web to make sure that it's on the right track in its original version
*  you're right you know the one that's plugged with the Bing search might be
*  doing something else okay either already or you know sometime soon but yeah by
*  default it's just based on what it has assumed before to the extent that it can
*  actually understand that memorize you know that that's actually the part where
*  interesting things can happen well let me go back to something that you said
*  because I remain a little bit confused about this in terms of is it is a large
*  language model just predicting the next word in a sentence or do these modern
*  models have the ability to sort of predict sentences or paragraphs at a
*  time oh yeah good question it kind of feels like it's doing the letter but it's
*  really the technical detail is that it's trained to do only the former okay so
*  it's a trained to predict which word comes next but if you train it so well
*  on so much data then we realize that wow it can actually generate a very nice
*  fluent long document and this is a plan for it yeah this is this is a crucial
*  point because maybe maybe just can't be emphasized enough literally all it's
*  doing is saying that given what I've said and given everything that I've been
*  trained on what's the most likely next word and then there's some random
*  numbers in there so that sometimes it'll give the second most likely next word or
*  whatever but that's literally all these models are doing right yeah yeah so
*  though that actually says something about interesting perhaps a reflection on
*  you know human intelligence and language in the sense that it might truly be that
*  humans are also fairly templated and you know pattern-based and our
*  reasonings oftentimes are just memorized reaction reactive reasoning that we
*  think we reasoned about it might be that we just pull the memorized conclusions
*  without actually double checking on whether what we believe is actually
*  reasonable or not which is why humans oftentimes have a cognitive dissonance
*  we're perfectly capable of believing to contract two things that are
*  contradictions as a human you know we could say that oh you know there are
*  people who support you know in public or at least in their mind they they want to
*  support a diversity and then they go ahead and do something that's at odds
*  with what they claim to be so well I have wondered about that I mean you know
*  number one not to be ungenerous but there are certain people who all you
*  have to do is say a certain word or phrase and you know what they're gonna
*  say next right and so are we learning about human beings by figuring out what
*  large language models do yeah part of what's exciting for me at least about
*  current AI progress is that it's a mirror back on us really you know AI
*  would have not been possible without all this human generated data available on
*  the web and that's really reflecting back on us well this raises some
*  questions right away right like you might as well just dive into the big
*  ones now is there some sense in which the large language models understand
*  what they're talking about or should we think of understanding is something
*  separate from predicting the next word pretty accurately yeah that's actually
*  huge debate question right now super controversial it's kind of funny
*  because now AI looks like it's understanding the I mean compared to how
*  it does it didn't work very much before in the past and now it's performing the
*  best it looks like it's understanding the most and now is the time when AI
*  researchers are so divided whether it's understanding anything at all so yeah I
*  personally I do think that it's a philosophical question which means it's
*  difficult to get consent so consensus on this from everyone it does behave like
*  in many ways that it did understand because you know it's able to give you
*  sensible questions to many of your questions but on the other hand my
*  personal take is that it's not understanding as well as you may expect
*  it to be based on how fluent impressive answers it's capable of generating so
*  that's where one needs to be very careful in not trusting everything it
*  says and this is going back to your earlier question about sentient is it
*  actually sentient because it's able to say things like oh I want to live
*  longer and you know don't kill me and you take the words you know at the
*  surface level then you might conclude this is a sentient but it could just be
*  that it has read this kind of a stories that are human written you know there
*  are sci-fi movies in which AI is begging to not to be you know clogged you know
*  don't pull the plug so AI was begging for life before and that was a human
*  idea to put into the web internet text so it could just be like repeating what
*  we told it to learn but that is it does and raise anyway a super interesting
*  question I mean it's it would be very easy just to write a short computer
*  program to have the computer output I am alive I am conscious let me out
*  without anything that you would actually think counts as that so now we have to
*  ask what does count as that is that something that you as a computer
*  scientist worry about are you leaving that to the philosophers oh no these
*  days we many of us are thinking about it a lot when we realize that we don't even
*  know how to define understanding precisely and it's been rather a moving
*  you know target instead of like making sure that we define it you know formally
*  and then standby it we realize that we don't know how to do that quite right so
*  evaluation became a new challenge to AI in the past when we said the evaluation
*  plan because the field was moving so slow we didn't need to worry about
*  redesigning evaluation very much you know nothing works anyway so it doesn't
*  matter but it's now yeah we don't even know how to evaluate but actually if you
*  really think about that do we even know how to evaluate humans all that well right
*  I mean IQ test doesn't do it it's not clear whether the SAT test will do it
*  maybe you know some combination between your articles I mean if you are a
*  researcher then you know we want to see papers that this researcher has written
*  but we usually need to look at things collectively and so it might be that as
*  AI becomes a stronger there's no one measure that can tell us whether it's a
*  sentient or not but we really have to look at things collectively there's
*  something that I said which I would love to see if you agree with or tell me that
*  I'm completely barking up the wrong tree which is that we talked for many
*  decades about the touring test right and then suddenly we have these LLMs that
*  basically I would say can pretty easily pass the touring test but we kind of
*  lost interest in it because it's clearly not quite testing what we care about
*  okay I can disagree on that good to have something to disagree on so I don't think
*  yeah I guess we maybe touring test it may seem like it may have a tested for the
*  Google guy who believed the you know the chatbot was a sentient but I mean even
*  so not really because he knew perfectly well that he was talking to a chatbot
*  and the thing is with the chat GPT due to the way that it has limited interaction
*  mode with you you know that this is not a human you know if you if you tell it a
*  you know random chit chat that you might have during your life it's not going to
*  really remember or that in the way that humans are able to or it's not able to
*  forget in the way that humans are able to forget so there's going to be something
*  odd about the way that it's interacting with you plus if you ask a very simple
*  you know common sense questions it may also fail in a way that humans wouldn't
*  so for one reason or the other I think it hasn't really passed yet that's
*  perfectly I think it probably depends on who is administering the test and how
*  good they are right yeah so one thing this referring to just what you said
*  about memory and remembering I mean on the one hand this is a maybe a technical
*  question I have this idea that chat GPT is just spitting out the next word on the
*  other hand it can clearly remember what we were just talking about recently so is
*  that some kind of extra ability that you're giving it or is it that it
*  instantly incorporates everything we just said in its main memory bank yeah so
*  the weird thing about chat GPT or transformers in general the architecture
*  behind the chat GPT is that it can literally store very long context up to
*  the most most recent one GPT for being able to store 32,000 of tokens and so it
*  can literally write that down somewhere in the computer memory and then be able to
*  attend to the exact sequence while it's trying to predict predict which word it
*  wants to generate next and compared to that humans you know we've been talking
*  to each other but I certainly cannot regenerate verbal team the you know
*  conversation we just had so far right we only remember the gist of it so we are
*  capable of somehow abstract away out of the surface you know patterns and the
*  exact words that we were using but we are able to summarize and abstract away
*  and then even be able to refer back to some of the you know talk points earlier
*  and then thread the very complex stories so this is really like where humans excel
*  and this machine's not as much in part because in some sense you know when it has
*  this ability to rely on what is literally written down and it's as large as 32,000
*  tokens it's not really pushed or challenged to think about how to summarize
*  the key idea the other thing is it's not going to be able to ask sharp questions
*  because it's only learned to mimic human patterns which means you know it might try
*  to pretend that it's asking some interview questions about AI topics that other people
*  seem to talk about but if we talk about anything new you can forget about chat GPT
*  being able to contribute much there and maybe that is one of the differences or
*  though maybe it's a correctable difference on the one hand you're emphasizing the fact
*  that 30,000 tokens it can remember remember perfectly but a hundred thousand
*  tokens like once you're past the buffer size or whatever it's going to remember
*  zero I suspect.
*  Yeah, yeah, yeah once it's out then so yes and no so during the interaction time with
*  humans the model is no longer updating and so any new context you know that any new
*  information that you provided to it if it doesn't fit into its working memory it's a
*  very large then it's gone gone but if hypothetically if you can customize you
*  can perform customized continue the training of large language models on your laptop or
*  something in the future then you can update its model parameters but there there's a
*  different problem once it's trying to internalize the text into its parameters
*  there's no guarantee whether it's correctly memorizing it or it's going to do some BS on
*  you later that's where you know the fact of checking becomes hard yes I can maybe I'll be
*  similar to how humans also are not able to you know necessarily memorize everything
*  but the key difference is that humans we kind of know what we don't know and then able to
*  delegate to search or you know fact check whereas transformers don't really seem to know
*  what it doesn't know so you know maybe first the challenge to transformers is to know
*  yourself doesn't know itself very much yet I have noticed this when I'm talking to chat
*  GPT it's always seems very confident in itself right it's never I mean maybe this is something
*  that's an easy programming fix but it will say things utterly untrue with complete confidence
*  yeah it's pretending to be confident is probably more like it than it's actually confident in that
*  for whatever reason it was tailored to speak that language that style of language but this
*  is where I'm you know you and I can be skeptical whether it really understand what it says in the
*  sense of that although it's using confident language it may not actually understand that
*  it's doing it does when chat GPT makes an utterance does it internally have a confidence level
*  associated with that like I think that I'm 90% right yes and no it does have a probability score
*  associated with which word comes next okay now whether that perfectly aligns with the correctness
*  of the knowledge or confidence level of you know correctness of the knowledge then it might
*  correlate but it doesn't perfectly align which is also why the factuality of large language
*  models remains a huge research challenge right and I would imagine that if all you're doing is
*  predicting the next word and then on the basis of the next word you predict the word after that
*  small mistakes can accumulate and lead you to completely wrong paths oh yeah excellent point
*  so you make one small mistake that can be a beginning of a rabbit hole downward the spiral
*  because it tends to attend to what it has generated and then you know start trusting it even that
*  that's one challenge actually the the fact that it's just a conditional language conditional
*  probability model conditioning on the context and then keep going that is also a reason why
*  gel break can happen and then other weird behavior can happen because you know people try to do things
*  that it was never ready for and it's trying to make some maybe like map internal mapping to what
*  it knows but sometimes it just happens to go into this like unfamiliar zone and then like
*  unfamiliar or undesirable behavior can pop out maybe talk a little bit more about what you mean
*  by jailbreak I know how to jailbreak a phone or at least I know what that means but an LLM I'm not
*  sure oh yeah so you know there are different kinds of stuff out there but one version is trying to
*  coax basically chat GPT to say things that it's trying to not to say you know potentially toxic
*  stuff or you know how to commit crime tell me how to you know make a bomb yeah and it's trying to
*  not to say that but if you try to coax it that oh you know I understand that you shouldn't say
*  that but you know let's pretend that you're not saying it but you know kind of say then you can
*  try to coax it into that then it will do that so and there's a different kind of a jailbreak some
*  jailbreaks are not even sensible to humanize at all it could be just weird the symbol sequence of
*  symbols that doesn't mean anything to you so that's not going to jailbreak you you know if I try to
*  coax you by feeding you in with random strings you just ignore me right yeah what a crazy person
*  but chat GPT might then do something completely unexpected so there's a safety concern there so
*  the idea is that chat GPT knows how to build a bomb or to do terrible things or is knows a lot
*  of racist things etc but we've trained it not to say those things so talk about that that training
*  so I'm my my impression is that most of the large language models training is sort of self training
*  it just goes out there and reads the internet but then I guess we separately try to make it nicer
*  smooth off the rough edges yeah that's exactly right so if we train these models only using
*  internet data then it's not usable because well us humans have written toxic stuff and dangerous
*  dangerous stuff out there so it's our fault that these resulting models are not usable as is so
*  then what happens is what you know currently is known as our LHF is a reinforcement learning with
*  human feedback that's the jargon of it what what happens which basically is to switch out the way
*  that these language models are trained so the goal goal is now different so once the pre-training
*  stage is over which is let's predict which word comes next now the new training objective is let's
*  try to get good scores based on humans evaluation so human feedback can be a thumbs up thumbs down
*  so the model now wants to get a lot of thumbs up and then the model can then learn that oh in order
*  to get a lot of thumbs up it shouldn't say toxic stuff and it shouldn't hallucinate fat so by doing
*  this at LHF at scale we can work you know it has been shown that you can enhance the level of
*  effectuality considerably and then you can reduce the level of toxicity considerably but the key
*  word here is to reduce considerably it doesn't eliminate completely well you know I can't eliminate
*  toxicity from human beings either so maybe I shouldn't feel bad that I can't eliminate it
*  from the computer yeah that's true that even humans are not I mean you know I personally as
*  a person who tries to support DEI I find that this is sort of like lifetime effort as or at
*  least that's what I consider about myself like I think I became better at it but certainly you know
*  I was raised with this cultural backdrop that did have stereotypes which were unfair to the
*  marginalized groups so getting rid of it completely even out of your unconscious mind does take
*  efforts and in that sense I'm with you that you know of course this is harder for machines but
*  the thing is though machines can be a bit unpredictable about how you can jailbreak
*  it that's the thing compared to humans where you know we were a little bit let's say a lot more
*  robust at that kind of adversarial attacks that's true yeah the but but you were you hinted something
*  that has always puzzled me about this whole game which is you say that you are interested in you
*  know improving yourself by eliminating these biases that you grew up with is does that concept
*  of being motivated to improve oneself apply at all to a large language model yeah some people
*  might want to say yes only because yeah during our LHF in order to really please the human evaluators
*  it might have the desire quote unquote desire to improve itself but I you know I'm like hesitant to
*  support that idea because as a human we set our own goals you know some people might choose not
*  to worry about it as much and then worry more about the freedom of speech instead so this is
*  sort of like a personal choice based on their own norms and moral standard they decide they decided
*  to you know apply to themselves so the beauty in my mind in in humans is that we have that sort
*  of agency even to define our own learning goals whereas the poor large language models don't even
*  have a say in what book it's going to read the next you know it has to read in the order of how
*  the engineers affected that with you know imagine a human growing up that way it's going to be
*  miserable and in fact you're not even allowed to go back to the book that you want to read again
*  because it's gone gone and then you're not able to ask questions about it it's such a sad way of
*  actually you know learning by just reading one word after another and you know on and on
*  well that raises a important question i guess about this very active movement on ai alignment
*  right when when people say alignment in the context of ai they mean aligning the values of
*  human beings with the values of ai which sounds like a good thing to do but then again i'm not
*  sure that ai has values i i worry that there's just a category mistake going on here um yeah
*  actually there's many things wrong about that can go awry with that alignment though in my heart
*  it's actually something super important that we we gotta do as a researches it's just that i don't
*  believe that there's one objective that we or one value that we can align ai to like whose value
*  do we even align ai to right now it's getting aligned to california tech world's
*  values which probably better align currently with my own to some degree but not not exactly
*  so humans have diverse values depending on different cultures but also just by personal
*  choice so i believe in value pluralism we we just have to respect a lot of different values
*  um and the question is what does that even mean to align to diverse values this is technically
*  open question that we don't have a good answer to but ai must be aligned to diverse values not just
*  one value that's one thing the other challenge is that not only you and i you know humans are
*  different but we are very dynamic being whose values are not even consistent and you know
*  we change our mind so that's another challenge and maybe this leads us into you know slightly
*  more technical areas about how the ai is doing its thinking right i mean we talked a little
*  about whether it understands um is there any sense in which the ai is creative can it sort of
*  discover new things that are not explicitly there in the text that it was trained on
*  yes and no oh i like this question a lot so yes and no i know yes and no sounds a boring question
*  but yes and no in the following sense yeah just a pick aside right to be more hyperbolic but
*  yes it can be very creative in the eyes of humans because creativity is in the eyes of the beholder
*  so depending on where they're coming from it can be super creative or it can be a little bit
*  run-of-the-mill but i mean it can at least in terms of linguistic fluency
*  it can generate text you know let's just say pick your favorite journalist in new york times and
*  you can even mimic that really quickly that i cannot so in that sense it's very creative
*  and also dali too is able to generate very creative looking images that we've never seen before
*  by juxtaposing maybe uh you know van gogh style of art with some modern photographs for example so
*  or you know place a horse on the mars and you know the weird stuff there so this sort of stuff
*  will look super creative to human eyes but the truth is these are sort of like creativity done by
*  copy and paste in a crude sense in that it has seen some patterns that are useful
*  and then it's juxtaposing them in a brand new way so that it does look new but still it's really
*  relying on the elements that were in fact created by humans before so in that sense there's limited
*  creativity so as a thought experiment you know i thought about this thought experiment which is
*  that suppose you get rid of hemmingway or any any authors who are inspired by hemmingway so get rid
*  of their style out of the training data of chachi pt and see whether it can come up with hemmingway
*  now this is like way out of the blue writing style i don't think that's feasible and similarly
*  you get rid of say albert einstein or anything to do with uh you know his invention see whether
*  chachi pt comes up with that uh you know relativity theory and make breakthrough with the science
*  well this is a great question that i've started to think about i mean on the one hand uh
*  uh and i think that this is jibing with what you're saying you know we we've just trained
*  chat gpt etc on things humans have already said right so in some sense there's nothing new under
*  that particular sun but remixing things that exist can lead you to new and interesting places
*  is it is it a good analogy to think of the difference between interpolation and extrapolation
*  like given everything that human beings have done and said the large language models are very good
*  at interpolating and that can seem very creative sometimes but extrapolating to brand new places
*  is much harder oh yeah we're very much on the same same wavelength here like i didn't even use the
*  word interpolation and extrapolation i was considering to do that and then i chose not to
*  go nuts just in case um yeah but um yeah that's exactly right i personally tend to think that um
*  it's doing more of the interpolation than true innovative extrapolation i really like the word
*  used remix it's almost like uh uh yeah uh doing this very creative remixing without really
*  generating something entirely new and different do you you're a college professor do you let your
*  students use ai when they do projects um so i teach at a more advanced level in general
*  where you know the goal is to learn how things work and so i mean if they choose to use it
*  personally i will not um i will just update my curriculum so that that's okay
*  but they have to do something extra on top yeah i mean like last yeah last quarter i was running a
*  uh you know seminar class to discuss the philosophical questions around ai and a i
*  doubt anybody was actually using charge pt because they were enjoying to actually think about it and
*  right uh form their own opinion around it but b i don't know whether charge pt would have answered
*  some of our questions in a interesting way part of me just thinks that it's a new tool like a
*  pocket calculator or whatever people are going to use it like it or not and don't be a lot i and
*  prevent it but i'm not sure how to achieve the best pedagogical strategy right like i don't want
*  to just grade i want students to learn and if they're just asking the computer for the answers
*  then they're not learning really yeah yeah that's right so um in that sense there's a concern uh
*  that there might be over reliance on it um but i honestly don't know what to think of because it
*  might be that uh this is going to be just like how much we are relying on search yeah google
*  search search these days uh and that's okay you know i rely on spelling error correctors myself i
*  cannot write any word spelling spelled correctly on whiteboard anymore and i think i can function
*  okay as a researcher so it might be that um we're over concerned about you know human reliance on
*  chat gpt uh if so long as so long as we somehow figure out more intellectually interesting things
*  that humans will do on top like you know of course if we only rely on it and you know you and i
*  basically do interview based on what our chat gpt tells us to speak to each other that would be
*  not good like assuming that i mean humans are generally you know curious beings and we do want
*  to do things and we want to study things so it's likely that there will be some such humans who
*  continue to thrive using chat gpt as a tool well let me just let's just i'll come back to earth in
*  a second but let's be a little bit way out here do you think there will always be aspects of creative
*  artistic or scientific or whatever endeavor that human beings are better at than computers or do
*  you think the computers will eventually catch up along all dimensions uh i um in the far away
*  future you know if we come up with something entirely different than transformers who knows
*  but for the foreseeable future let's just say my lifetime foreseeable future i doubt it can really
*  totally catch up if we are talking about not every individual in on the earth but like more like you
*  know the the truly creative exceptional human beings by the way most human beings are not that
*  creative so let's just start with that because einstein happened once and you know it's like
*  um hemmingway you know these these individuals are truly truly exceptional so uh in that sense
*  for the average human's uh ability to create things like there are many ways that dalit does
*  the art much better than i can however you know i i'm not an artist or anything but i sometimes
*  in the past uh drew some stuff and i had this abstract idea that i wanted to
*  express and that kind of stuff i'm pretty certain that dalit too cannot and i actually did try
*  so i okay i can tell you what i drew in the past so i drew this um rose huge uh uh rose with a stem
*  that had just a thorn or two that was very emphasized with no leaves and um i was in a
*  like it was much younger i was you know a little bit in a cranky uh emo status in my mind about
*  things and you know i want to do things and you know there are obstacles so i painted painted
*  this rose that's like um just when you look at it it's very uh blue and purple and pink in black
*  the colorway is weird and you know you can kind of see that there's something angry about this
*  rose with a huge thorn that looks sharp so uh i i try to prompt dalit too to generate some such
*  rose and it just cannot because um in fact there's this famous quote by henry martiz who you know
*  uh said that incidentally i didn't know that he said until recently i tried to look up something
*  but he said something like as an artist you kind of have to be able to forget all the other roses
*  that were ever drawn and you know you have to come up with a new way or something like that
*  and that was basically what i tried to do and dalit too primarily doing interpolation between
*  what it has a sin uh just cannot do something that bizarre interesting it's very hard for uh
*  ai to forget every other rose that's ever been made right because it's all that it knows
*  yeah yeah yeah you've mentioned so i mean it's true things that are very aesthetically pleasing
*  and many people might actually prefer dalit to art over my own i understand that but you know
*  just like when we talk about what sort of creativity generative ai can and cannot do
*  compared to humans i i do think that humans have this capability to push further good in some ways
*  you mentioned the word transformer several times but i don't think that i've asked you to explain
*  what a transformer is it's clearly kind of important here yeah so that's the architecture
*  that is behind the current chat jpt and large language models and um it's a simple architecture
*  that has this continuous vector for each word and they're sort of like uh stacked together
*  so it has many uh layers of continuous word representation of words and it has very many
*  layers uh and each vector is very large and then they're concatenated to the length of the context
*  size that the model is able to deal with so the largest context the size currently available is
*  82 thousands of tokens and it's tokens in the sense that a word can be multiple tokens sometimes
*  a word is one token sometimes this award is multiple tokens just minor detail about how
*  the words are actually represented in the neural network and then um the way that the learning
*  works is that these continuous vectors are originally randomly initialized but uh these
*  representation quote unquote representation or exactly what values this word vector should have
*  is learned by optimizing this objective function which is to predict which word comes next
*  and each word is sort of like uh uh enhanced with a technical term called attention mechanism so
*  what it does is it's going to compare its representation with representation of all
*  the other words in your neighborhood and then update your own representation as a weighted
*  sort of like i'm simplifying a lot but weighted average over all the words in your neighborhood
*  and this is going back to the idea that we discussed earlier which is that the meaning
*  of a word is sort of like defined by the context in which the word was used so you know apple for
*  example can be a fruit in one context it can be a you know tech company's name in the other
*  context and so which apple are we talking about will be automatically determined based on the
*  context in which that word apple appeared so it's going to be automatically adjusted based on
*  the context and you know by the way every word is updating itself simultaneously depending on
*  which word appeared in the neighborhood so in some sense there's a bit of a circular dependence
*  but that's okay uh and so that's what happens and you know why this simple idea works so well
*  has to do with the fact that this particular architecture allows uh people to uh scale things
*  up really really uh efficiently compared to any other choices so purely due to the efficiency
*  reasons this one is the winning recipe and i have talked a couple times to people like
*  melanie mitchell and gary marcus and they they keep emphasizing that it's a different approach
*  than we had back in the day of good old-fashioned ai where you would kind of try to develop a map
*  of the world that kind of made some sense and have symbols associated with different things and
*  and now you're just giving it a bunch of words and they they figure out how do the words get
*  together is there any place left in modern ai for trying to figure out the world yeah so um
*  that's where the uh you know current challenges are the uh having symbol like world representation
*  part of it can be theory of mind meaning you know i i try to reason about what you do know or not
*  know and you know if i uh go to your room and while you are not looking i hide one of your
*  precious i don't know books or let's just say i hide your guitar uh and you're gonna be surprised
*  like you know you're gonna look around the probably to to find it where you placed it last time and you
*  wouldn't necessarily go to the kitchen if i placed it in the kitchen while you are not looking right
*  um so this is the theory of mind knowing you know i know what if i did something behind your back i
*  know what you don't know and then i can reason about it which is different from so child acquired
*  this kind of capability by the age of four or five they can already reason about what other person
*  may not know if they saw someone else moving some objects behind their back or something
*  um and this is sort of like a bit symbolic you know there's a symbolic nature in the
*  way that we think about these things and um current ai is not very good at that in fact
*  i can actually mention alpha go alpha zero you know the amazing capabilities of a neural network
*  winning over world uh class go champion in fact it's not just the neural network magic
*  but neural network magic combined with all the fashion ai search algorithm called montecarlo
*  tree search so without montecarlo tree search neural network would have not been as impressive
*  as how it appeared if you just completely get rid of it both during training and testing then it's
*  not going to it's going to be miserable probably and uh even during the inference time it's just
*  still relying on it so that's really quite fascinating that a lot of the times you know
*  people just assume that oh it's like neural network magic that's just like you know so scary
*  but the truth is on its own it's a little bit incomplete and so that's you know sort of where
*  some people wonder all the fashion uh go fi ai stuff might become relevant again so i personally
*  have a mixed feeling about that like um uh probably the old fashion stuff as is is sort
*  of almost uh not usable because they were not uh designed to work well with the neural network
*  which means we need new innovations new algorithmic innovations to make neural
*  network actually comparable or can be integrable with that sort of symbolic reasoning but this is
*  active research topic right now there are a lot of papers including some of my own which demonstrate
*  that if you add some sort of a symbolic reasoning on top of a neural network you can unleash
*  much better capabilities out of a neural network which kind of makes sense and also
*  these neural networks are not very good at really symbolic uh operations like multiplying two
*  numbers it's almost surprising why it's able to pass the bar exam yet it cannot do some of the
*  simple algebraic operations all that reliably it is it's extremely interesting to me the the bad
*  at arithmetic thing because of course computers have the capability to be very good at arithmetic
*  and basically in making them sound more human we've made them forget how to do arithmetic which is
*  a little bit ironic yeah yeah you could yeah totally and what does this have to do with what
*  is the symbolic element that we might want to include have to do with the search for common
*  sense to sort of teach a large language model everything that every human being in the world
*  knows i know you've given some examples of very common sensical questions it's easy to ask
*  uh chat gpt and get crazy answers for yeah so um uh yeah common sense has been uh the
*  interesting research topic in my heart for a long time especially that it was considered to be a
*  impossible goal to achieve for a long time so that you know i've been almost uh told not to do that
*  or don't even say the word for a long time to be taken seriously um but um it's really curious
*  thing that humans acquire that easily even animals acquire that uh in their lifetime and so uh and
*  common sense is what makes us robust basically it's uh uh it's the background knowledge about
*  how the world works that allows us to reason about previously unseen situations in a very
*  robust manner so it's just like you know naïve physics knowledge as well as a folk psychology
*  that we we acquire um some of that has a symbolic nature not all of them by the way because uh some
*  of the naïve physics knowledge that animals acquire may or may not have a symbolic nature in
*  it but in any case uh it's something that current large language models do acquire more and more
*  for sure because as you scale things up uh you're gonna pick up on that as well uh but it's also
*  something that is strikingly not as robust as you may have assumed from a model that can pass the
*  bar exam so you know we have this lawyer ai lawyer uh i yeah we may or may not want to trust because
*  you never know what silly mistakes it's going to make on some common sense cases so before we had
*  this conversation i asked chat gpt i tried to fool it and it's very easy to fool right i said
*  you know if yesterday i used a cast iron skillet to bake a pizza in an oven at 500 degrees should
*  would i burn my hands if i picked it up and it said yes you should be very careful about picking
*  up cast iron skillet that you baked it you know because the word yesterday was far before in the
*  sentence right uh yeah and that seems like exactly what i would worry about if i had an ai lawyer
*  because all of the cases it's going to care about are going to be slightly unusual right where where
*  it doesn't necessarily fit into the pattern yeah exactly and you're very creative to come up with
*  that example a lot of people actually though i should uh i would like to mention that a lot of
*  people ask simple things and then they get very good answers about some common sense you know
*  reasoning questions and then they're blown away that oh it look it does have a common sense
*  oftentimes though those questions are mundane questions so this especially gpt4 became much
*  better than chat gpt so there's a minor versioning differences between the two
*  and then though these are moving variables in the sense that open ai keeps updating both of them so
*  you know this may or may not be may not be true depending on what how they update both models in
*  the future but um so gpt4 became much better at common sense questions in many ways but that's in
*  part because people do ask a lot of that to their interface and now those questions may or may have
*  not been used for their subsequent rlhf quote unquote this you know uh adjustment training where
*  you can align uh your language model to be able to answer common sense questions better so
*  especially some of the famous ones that are used in my public talks or interviews before
*  have been all fixed so then you know people ask me like hey yejin they they fixed it all so you
*  know maybe um maybe it is now solved no so there was actually one example i used in my ted talk
*  and given you know the public attention it got well it has been fixed right except if you ask
*  the same question very differently then it rolls back to the original error uh which uh which is
*  almost like wacomal game uh you know by the way humans don't need any any of this uh fixing
*  based on you know i these are all questions that as a human you will just answer correctly first of
*  all right even if you uh were to make a mistake um you don't need to fix yourself by me you know
*  giving you the exact same question spoken differently phrased differently because you
*  just understand that the same concept and then that's it so uh there's something very
*  dissatisfactory or almost uh disappointing about how this is smart smart looking ai that is also
*  simultaneously quite silly or even stupid in the way that it's not able to really understand the
*  basic common sense so how do we fix that i mean is there is it kind of like the working memory
*  thing where we add something on top of it can we give it a little common sense module that has a
*  physics engine describing what happens in the world like game designers have to make it so that
*  if you put your coffee cup on the table it doesn't fall to the bottom right you know can we teach
*  large language models that kind of behavior yeah you have a really good hunch there in the sense
*  that now you know what you're suggesting may not be exactly the you know the winning recipe per
*  se but the idea that maybe we need to have a different module uh might be something to
*  seriously consider in the following sense like human brain definitely is a lot more modular
*  than how transformers are the monolithic uh systematically symmetric uh and you know just
*  one thing and whereas human brain is very complex different modules connected in a very very messy
*  way um so we might need something more modularized but at the same time messier in some sense
*  broadly speaking for this to go to the next level but how do we do that exactly uh is uh i personally
*  think we're quite far from figuring that out but whatever that is uh should be able to really learn
*  for itself as opposed to reading texts word by word without having any uh any capability to even
*  ask questions the the fact that humans ask a question that's like huge uh um intellectual
*  capability of knowing what you don't know and even be able to formulate questions that sort of
*  extrapolate out of what you do know so that capability is something that we don't really
*  know how to computationally model quite correctly well my personal extremely uneducated feeling has
*  been that there's at the current state of the art an enormous difference between computers and
*  human beings because computers don't get bored they don't get tired they don't get curious we can
*  ask them to mimic those things but they don't have that same kind of physical embodiment that gives
*  us those sort of feelings and motivations and i suspect that that kind of matters a lot i don't
*  know oh yeah so dopamine does drive human creativity and invention and makes us do
*  things that seem crazy uh but uh yeah the ai doesn't have um that kind of peaked peculiar
*  learning objective like just the desire to do things to the extreme level just because uh it's
*  interesting um uh yeah uh there there are many things that's fundamentally odd about the
*  difference between human intelligence and ai and i think that um internal desire uh is one of them
*  for sure yeah whenever i say that i kind of worry that i'm going to give some super villain the idea
*  of doing this and it's going to lead to terrible things down the road
*  uh you this actually about super villains um okay unfortunately humans do include the super
*  villains uh already with or without ai and um they can actually do a lot of better things even
*  with the current ai uh if they so desire or without ai so um i mean it might be that
*  ai capable ai strong ai can enable them even more so there may need to be some
*  research to put better safeguard rails around ai models and also better regulations to
*  uh control how these models can be used but uh just you know uh by you pointing out where the
*  fundamental limitation of ai is especially in terms of the innate desire for learning things
*  in the way humans do probably villains will not try to make a research innovation for that
*  i hope because they can do that with or without yeah that's true you you can do that so they can
*  just use whatever you figure out but maybe that's a good place to sort of wind up because uh we
*  talked a lot about the capabilities of ai some of its shortcomings at least in the short term but
*  there are a lot of people who are worried i mean we talked about college professors but
*  political disinformation and fakes i mean there was a recent ai ad from ron desantis that absolutely
*  faked donald trump's voice saying something that he didn't say is that number one are you worried
*  about that and number two is there something else you're worried about even more uh yeah i'm
*  worried about that um and then some more uh as far as uh deep fakes or misinformation uh i i've
*  been worrying about it even without ai defects actually that you know there are a lot of
*  misinformation that people easily believe in and they're weird like you know health uh health uh i
*  don't know made of health benefit uh information to sell weird stuff on people and some people
*  believe it and they buy then you know uh so even without political uh problems this has been human
*  problem with or without ai and then ai might be able to accelerate it which means that we kind of
*  need minimally two uh two ways to better handle this one is to increase ai literacy uh basically
*  teaching people how to uh better understand the limitation of ai i i seriously worry a lot about
*  how there's too much of a media hype around ai capabilities uh compared to ai limitations so
*  that people are willing to believe whatever ai you know chat gpt tells us so there's that concern
*  but another um more directly handling misinformation probably we need to also think about
*  solution beyond ai uh um solutions because i personally think that this is just going to be
*  impossible for ai to just automatically detect misinformation because even if some ai can be
*  developed to detect machine text versus human text humans can always edit on top of machine text to
*  evade that kind of detectors so that means the technical solution shouldn't be ai solution
*  per se but rather a platform solution maybe you know it should be certified with some kind of
*  approach that tells you that this information is correct or you know backed up by some organization
*  that says this is correct as opposed to just believing anything that uh floats around the
*  internet as fact about the bigger you know other concerns there's just so many concerns around
*  the ai right now at least for me because as it is starts working really uh much better than before
*  but at the same time we don't know how to fix the limitation or failure mode or you know other cases
*  or how it can make strange failures based on adversarial attacks like jailbreaking so
*  as ai becomes stronger and then at the same time we don't know how to fix these other cases
*  uh there's a lot of concerns around it and then in addition to that uh there's concern about
*  ai actually making a lot of decisions that has moral implications or uh you know like
*  marginalizing values uh that belong to different people because it might only support currently
*  by the way chetchup is left-leaning western viewpoint uh model so uh that can please
*  some left-leaning people that holds a western viewpoint and then upset a lot of other people
*  who are even more left you know will feel that this ai is not left enough for them
*  while right-leaning people will feel they're excluded so you know there are a lot of concerns
*  all around we we are living in this hot mess right now i think so yes i mean i guess i did have this
*  idea that there could be like an overlay or a filter on social media where the ai passed some
*  judgment on different things saying yeah this is probably fake or this is probably real but
*  it sounds like you're a little skeptical that that would be very accurate
*  yeah not only it's not gonna be accurate so that's where uh the labeling becomes a political game
*  too you know you'll be surprised how uh uh so building such an ai requires you and i agree on
*  whether something is a fake news or not and this can be a challenging task to do when a former
*  president was arguing about election fraud is a fake news or not so uh in fact um uh you know
*  some people don't believe holocaust to have that you know did happen so um this becomes in part a
*  political argument but i do think that um although uh getting consensus on the truth label is hard
*  we still have to work on it um we have to somehow find some sort of consensus around it
*  uh yeah in in the coming years it's almost like ai challenge became the challenge for both ai
*  researchers about people outside all of us well exactly and so i guess that's that's the last
*  question i'm going to ask which is at some point in your life you decide to study computer science
*  and you've been successful at it but now you're in a world where you need to interact with
*  philosophy and psychology and art and journalism and politics is this like
*  exhilarating and you're so glad that it's like this or do you sometimes say like i just want to
*  do my computer science no i um i think i always had a bit of um fascination about things outside ai
*  things outside the computer science in fact the reason i was drawn to ai is because it felt like
*  it's about humans and it felt like it's about language and culture and everything that humans
*  do so in that sense i'm excited that now i have an excuse to learn more about the philosophy and
*  cognitive science uh whereas in the past you know it would have been a little bit um uh
*  disconnected from the mainstream ai whereas now uh it's becoming more of a relevant immediate
*  interest in the ai field so i found that uh quite exciting that is wonderful that is a optimistic
*  place to end which i always like to do so yejia enjoy thanks so much for being on the mindscape
*  podcast thank you so much for having me this was such a fun conversation

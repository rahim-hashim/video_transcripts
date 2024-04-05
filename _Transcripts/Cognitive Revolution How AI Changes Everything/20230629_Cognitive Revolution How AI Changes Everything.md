---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 5542s
Video Keywords: []
Video Views: 968
Video Rating: None
---

# Meta's MEGABYTE Revolution with Lili Yu of Meta AI
**Cognitive Revolution "How AI Changes Everything":** [June 29, 2023](https://www.youtube.com/watch?v=8EIqHFFdccA)
*  to model a 600 by 600 image,
*  you have to add the one million tokens,
*  and current architecture just cannot support it.
*  That naturally introduced a different problem,
*  like we need a new architecture to solve this,
*  and that's why we have this very efficient way
*  of modeling involve multi-scale transformer.
*  We are very excited about be able to directly in
*  the future model the format of any file,
*  any input, any modality.
*  I think that's like a really exciting direction for us.
*  Hello, and welcome to the cognitive revolution,
*  where we interview visionary researchers,
*  entrepreneurs and builders working on the frontier
*  of artificial intelligence.
*  Each week we'll explore their revolutionary ideas,
*  and together we'll build a picture of how AI technology
*  will transform work, life and society in the coming years.
*  I'm Nathan Labenz joined by my co-host, Eric Torenberg.
*  Hello, and welcome back to the cognitive revolution.
*  Today, my guest is Lily Yu, research scientist at Meta,
*  and author of the recent hit paper, Megabyte,
*  predicting million byte sequences
*  with multi-scale transformers.
*  I first encountered this paper via a viral tweet
*  from OpenAI's Andre Karpathy,
*  who called it a promising way to potentially move
*  language models beyond tokenization.
*  If you're not familiar with the term tokenization
*  in the context of language models is the process
*  of breaking natural language down into a fixed vocabulary
*  of frequently occurring strings.
*  In the case of GPT-3 and GPT-4,
*  this vocabulary consists of more than 50,000 words,
*  word parts, numbers and symbols.
*  All language model inputs are chopped up into these tokens
*  prior to embedding into numbers,
*  and all next token predictions are selected
*  from this set of tokens as well.
*  In other modalities, there are other conceptions of tokens,
*  image tokens for example, might represent small squares
*  within the larger image.
*  Tokenization is used because existing AI architectures
*  struggle to work with really long sequences of data.
*  With the best performing methods available today,
*  the compute costs ultimately get out of control,
*  and there is a GPU shortage as you may know.
*  So since sequence length is limited,
*  some higher level more semantic compression of the data
*  is necessary and tokenization is the first pass
*  still sort of hacky way that that's currently done.
*  However, it does cause a bunch of problems
*  which Karpathy explains a bit in the tweet
*  and also links to deeper reading on if you're interested.
*  Suffice it to say for our purposes that it gets super weird.
*  So weird in fact, that there is a redditor whose username
*  has been immortalized as part of GPT-3 vocabulary,
*  and there are other super rare tokens
*  that famous models seemingly can't be made to say at all.
*  Karpathy summed it up by saying the list goes on,
*  TLDR everyone should hope that tokenization
*  could be thrown away.
*  TLDR everyone should hope that tokenization
*  could be thrown away.
*  Maybe even more importantly,
*  we may find general purpose strategies
*  for multi-scale training in the process.
*  And that's what we're talking to Lily about today
*  because in her strategy to eliminate the need
*  for tokenization, she just might have made
*  a more fundamental contribution.
*  I'm not an algorithm expert as you'll hear,
*  I ask some pretty simple questions.
*  But recently I have come to believe that given the presence
*  of web scale data and web scale compute,
*  it was really only a matter of time
*  until somebody figured out a workable algorithm.
*  Transformers are just one architecture
*  as the human brain is just one architecture
*  and neither is the end of history.
*  The basic idea of this research
*  is that the megabyte architecture
*  operates at multiple scales.
*  Unlike in a single transformer where all the layers
*  tend to be the same size,
*  in the megabyte architecture information
*  is first encoded in patches,
*  then there is a global model
*  that shuffles all the information around.
*  And then the final byte level predictions
*  are again made by separate local patch models,
*  which can be run in parallel.
*  And it seems like this architecture
*  just might have it all.
*  For starters, yes, the byte level prediction
*  eliminates tokenization.
*  Now the model looks at everything as raw bytes
*  and it's always predicting just the next byte.
*  There are only 256 possible bytes, just two to the eight.
*  So each one is ultimately just a series of eight zeros and ones.
*  It's kind of crazy low level to me at least,
*  if you think about it that way.
*  But because everything is bytes, music, video, text,
*  all of these are bytes on some level.
*  If this does work super well,
*  it will naturally extend across modalities.
*  It also has more attractive scaling laws,
*  sub-quadratic as they say,
*  and again, it's more parallelizable too.
*  These advantages allow it to work
*  up to 1 million byte length sequences,
*  hence the title megabyte.
*  But what is a megabyte?
*  In text, it's a million characters,
*  which does exceed for practical purposes,
*  Claude 100K's 100K token length.
*  In music, it's about one minute of music sound.
*  This architecture, because it's constitutive transformers,
*  will continue to benefit from improvements
*  to transformers more generally.
*  So obviously the key question is how it performs.
*  In their experiments, little you and her teammates
*  show that it does appear to be competitive
*  with the standard transformer methods.
*  So the next step at this point is for MetaAI
*  to take this architecture up to Lama scale
*  and see what happens there.
*  It sounds as you'll hear from Lily's comments
*  that they are very optimistic,
*  but this is such an experimental science
*  that we can't and won't know for sure until they try.
*  Assuming it is successful,
*  we could see mass adoption remarkably quickly.
*  They have open sourced their methods after all,
*  but we still might find performance quirks
*  and behavioral surprises for quite a while to come.
*  And even if they're not successful,
*  I think we should continue to watch
*  this sort of research space closely,
*  as the paradigm could definitely still evolve
*  in unpredictable ways.
*  Now, I hope you enjoy this conversation
*  about some cutting edge architectural research
*  with Lily Yu from MetaAI.
*  Lily Yu, welcome to the cognitive revolution.
*  Yeah, it's a pleasure.
*  Yeah, I'm really excited about this conversation.
*  You've recently published this paper
*  along with colleagues at Meta called Megabyte,
*  predicting million byte sequences
*  with multi-scale transformers.
*  And as soon as I came across it on Twitter
*  and saw the headline figure from the paper,
*  I said, this is one that I definitely want to
*  dig a little bit deeper into.
*  This has been a theme for a couple of recent episodes.
*  Definitely want to encourage listeners to take a second
*  and go look at the figure,
*  just to, obviously pictures worth a thousand words,
*  kind of get that visual in your head
*  of the shape of the architecture
*  that we're gonna be digging into.
*  It should only take like a minute
*  to kind of study it for a second
*  before going on to listen to the rest of the conversation.
*  But I think that will be extremely helpful.
*  We also have all the math and formulas in figure two.
*  For some people who are really curious
*  and want to know exactly the detail.
*  Well, that's what I hope to understand better
*  at the end of this hour than I do coming in.
*  So maybe just for starters,
*  let me kind of bounce off what I took away from the paper
*  and you can tell me if I'm missing anything
*  or how you would frame it differently.
*  The big thing that I saw,
*  and I try to avoid analogies wherever possible
*  to describe AI systems,
*  because I think they so often can confuse and mislead.
*  But when I look at this architecture,
*  it does kind of look like a fork
*  where you've got kind of the main body, the global model,
*  and then you've got these kind of smaller local models
*  that branch off from that.
*  And so it has this kind of general fork shape.
*  And what I was thinking is, okay,
*  this seems like a sort of different take
*  on a somewhat common theme lately,
*  which is like models talking to models
*  in high dimensional space,
*  except you've created a hierarchy
*  that can be trained end to end.
*  So now we have kind of multiple transformers
*  in a single architecture,
*  all operating under one loss function
*  and one optimization function.
*  How'd I do for starters?
*  It's a good start,
*  but first the idea of separating the agents surprised me.
*  Because the interaction is a little bit different
*  when we think about different agent communicating
*  with each other,
*  compared with end to end training
*  of autoregressive language model.
*  So when we say different agents,
*  there's like different type of action
*  coming from different agents.
*  Here in megabytes, we try to do prediction,
*  just everything is bytes.
*  And everything has causal relationship,
*  like different, the local model one follow each other,
*  predicting the bytes, the sequential bytes,
*  even though they are prediction parallel,
*  but it's actually a sequential like uniform bytes.
*  Right, but architecture wise, yes,
*  we have this like, kind of like different patch.
*  We use a simple concat operation,
*  which is the patch embedder, patch embed in the paper,
*  the different patch group, different bytes together,
*  and they go to the global model.
*  And then they separate out, as you said, like fork out.
*  I think that's the correct understanding.
*  So it seems like there's several big advantages to this.
*  And I'd love to hear you kind of describe each one
*  and maybe talk about which ones motivated you
*  and which ones you think are ultimately most powerful.
*  But the big advantages seem to be one
*  that there is the ability just to scale
*  to far larger sequences than a typical transformer can.
*  So you're literally predicting up to a million bytes.
*  In this case, the byte is sort of the unit of prediction.
*  So it takes the place of the token
*  that people are familiar with if they're,
*  you know, API users of open AI or Anthropic or what have you.
*  But going up, you know, anybody would,
*  who's used these sorts of products would recognize that,
*  hey, we have been kind of living at like the 8,000
*  token level for a while.
*  Now that's starting to expand.
*  We've got Claude 100K, but now you're, you know,
*  taking this up to a million bytes.
*  So that's a big deal.
*  There's also the performance or let's say the compute,
*  you know, efficiency advantage
*  because certain things can be run in parallel.
*  They're both smaller.
*  So I guess that's compute efficiency
*  and kind of ready parallelization.
*  And then third, related to the fact
*  that you're predicting bytes,
*  you don't have to worry about tokens.
*  So you can kind of handle everything
*  as like largely sort of raw data.
*  Tell us more about all of those
*  and maybe start with the one
*  that you think is most important.
*  Yeah, so I think for this work,
*  it actually come to hand to hand everything basically.
*  So what we really want to solve is,
*  is get rid of headache of the token either.
*  So we want the token either free language model.
*  However, it's why there must be a reason
*  why people do the token either.
*  One thing is to effectively compress information.
*  So it's easier to do the compute.
*  It's cheaper.
*  So that means, see,
*  but however, the token either indeed
*  introduced lots of problems.
*  So the common problem people may experience right now
*  is, you know, on the text,
*  on the text space, you have this BP token either.
*  The biggest headache is the space.
*  And sometimes you also see people do
*  certain prompt engineer by prefix,
*  some random combination of the letter,
*  and then it's gonna tokenize to certain things
*  and the model gonna continue generation,
*  such a nonsense.
*  That's all drawback of token either.
*  Of course, another difficulty of token either is say,
*  oh, one day you want to use,
*  chat CPT is very powerful.
*  Let's say you want to use a weaker large language model
*  and you want to use in bio,
*  you want to use use in chemistry,
*  you want to use in some foreign codes.
*  And then the token either is out of distribution
*  for your new domain.
*  And then you're gonna get problem with like,
*  fine tuning or something.
*  So that's what people experience with the text.
*  However, it's also a big, big problem for multi-modal.
*  See, you know, right now we are focused on text
*  and then everybody have to use in chat GPT.
*  But we also know like,
*  GPT-4 is already multi-modal.
*  And in the future, multi-modal gonna be a big thing.
*  However, it's a big, big issue
*  when you want to model image
*  or you want to model audio.
*  For example, image,
*  image there are two main architecture to solve it.
*  One is a diffusion model, which take pixel,
*  but diffusion model is very expensive
*  and like it has its own issues.
*  If you want to do auto-regressive image,
*  then you experience even longer sequence.
*  Like for example, in our paper,
*  we do 600 pixel by pixel image,
*  that's already 1 million bytes.
*  And then people use VQGAN as image tokenizer.
*  So text tokenizer give you headache,
*  but the image tokenizer can actually give you light mayor.
*  Hey, we'll continue our interview in a moment
*  after a word from our sponsors.
*  Amnaki uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work,
*  customized across all platforms with a click of a button.
*  I believe in Amnaki so much that I invested in it
*  and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
*  Because it's lossy, it's actually truly lossy.
*  So text tokenizer, the tokenization may not be reasonable,
*  but if you do say input string, tokenize,
*  de-tokenize, you get the original string.
*  But for image, if you do image input,
*  you do tokenization and de-tokenization,
*  you get a slightly different image.
*  So details is off, some color is off,
*  some, yeah, like finger get mixed up.
*  And then if it's original, there's words,
*  you cannot see it clearly.
*  Same thing, same thing for audio.
*  It's also a lossy process.
*  So that's why we really want to get rid of tokenizer,
*  no matter is to enable in the future,
*  the true multi-modal type of modeling
*  or to be able to mix in, easily mix image, text and audio
*  or to be easily adapt to new domain.
*  We really want to get a tokenizer.
*  So that's one of the biggest problem we want to solve.
*  So that come to another question.
*  Nothing is for free, right?
*  I just said the reason people want tokenizer,
*  because you cannot just handle such a long raw input
*  sequence for image, like to model a 600 by 600 image,
*  you have to have the one million tokens
*  and current architecture just cannot support it.
*  So that naturally introduced a different problem.
*  Like we need a new architecture to solve this.
*  And that's why we have this very, very efficient,
*  very, very efficient way of modeling
*  involve multi-scale transformer.
*  So yeah, that's naturally,
*  I think it's a one stone, kill two birds situation here.
*  We remove the tokenizer and we have this very efficient
*  architecture to support it.
*  And we demonstrate that across different modality
*  across text, image and audio,
*  we can both achieve like state of art performance.
*  Okay, so that comes to another question, right?
*  Can you combine the tokenizer and this model architecture
*  to enable very, very long sequence modeling?
*  So I think that's definitely part of our future work.
*  And we are thinking very, very, very carefully.
*  So for the current paper per se,
*  that's not what we're trying to solve.
*  So that's all very helpful.
*  So the big motivation is, and I haven't even mentioned
*  the natural extension to multimodality
*  in my already too long first question.
*  So thank you for bringing that up as well.
*  Cause that's definitely a key part of the result
*  is that you have the same architecture
*  working across different modalities.
*  Let me just try to understand this core figure.
*  So again, listeners, well, look at the figure.
*  This is figure one from the paper.
*  It's, you know, we'll put a link in the show notes,
*  very easy to find and pretty easy to sort of get a general
*  just for, but there are a couple of things
*  I wanna dig into a little bit more.
*  First, the input side, everything is bytes, right?
*  From this is all bytes in and bytes out
*  and the architecture itself doesn't care
*  what these bytes represent, right?
*  So I got that.
*  What is a little less clear to me is
*  what are the patches doing on the input side?
*  Cause if I understood correctly, and maybe I didn't,
*  I understood that the embedding was lossless.
*  So then I was kind of like, well, if it's lossless
*  and it's all just going into this global model
*  that kind of sits at the middle of the whole thing,
*  what is the meaning of those patches
*  or what is the function of those patches
*  as opposed to just saying, you know,
*  here's all the bytes that are inputs,
*  just feed them directly into the global model.
*  Like what's happening in those patch embed modules?
*  So there are a couple of things here.
*  See like in figure one, right?
*  We have this whole string as input
*  and they are actually input as bytes.
*  So we have 16 bytes.
*  So the sequence length is 16
*  and we separate them as patch.
*  So it's four by four.
*  That means each of the, either the local model
*  or the patch embedder.
*  So we have four duplicate of them
*  and each has input of four.
*  And the global model, the global model,
*  they only see the patch input.
*  So each patch take four bytes as input
*  and they're gonna give you back one vector.
*  So the four bytes already merged into one vector.
*  And then now the global can only handle four,
*  can only handle four vector instead of 16.
*  So that's why the global model was able to say
*  like much shorter sequence or equivalently,
*  if it's shorter sequence and you have the same compute,
*  you can make the model bigger.
*  So that's a big difference.
*  If you just put everything into the global model raw,
*  it's say 16 as a sequence length.
*  And now with the help of the patch embedder
*  as a local model, the global model only needs
*  to see sequence of four.
*  So it's much shorter and much efficient.
*  So one thing, another thing which I think is also relevant
*  to your later question is this padding.
*  The padding is actually really, really critical.
*  So in current language model is doing next token prediction.
*  So how they do next token prediction is actually by padding.
*  So if you look at the upper part, the local model,
*  you have this, for example, megabyte,
*  the mega, the mega, the full capture input.
*  So for the local model, you actually need to pad
*  the beginning, this padding token.
*  So the model, how it works is they see the padding token
*  and they predict the M letter.
*  And then they say the M letter, they predict the E letter.
*  So that's make sure they don't see future.
*  They don't see future.
*  Everything to predict, they only see things before it.
*  That's the essence of the next token or here in our paper
*  is next byte prediction.
*  So that's why they need to add this token.
*  So what about the, but however, because our local model
*  can see all the preference patches.
*  So when we, so the input to the global model,
*  you are not only going to patch a single letter,
*  you have to pad a whole patch.
*  Are all the patch embed modules the same?
*  Are they all identical?
*  Like even down to the lookups,
*  the sort of conversion of a byte to,
*  I guess it's even, it's a little different
*  than what I normally think of as embedding, right?
*  Cause I normally think of a token having a sort of long form
*  vector representation, but here, because everything is bytes,
*  there's only 256 bytes, like they're just represented
*  explicitly, literally, right?
*  I see.
*  So actually we still have embedding.
*  Again, as you said, but embedding matrix
*  is much, much smaller.
*  So for example, in a normal large language model,
*  the vocab size is either 32K, 65K, 50K,
*  it depends on the, how the research choose
*  peak for their task.
*  So for that, you have a large vocab map to a embedding space.
*  It's actually the same.
*  It's just the vocab is so much smaller.
*  The vocab is only 256.
*  And for the 256, you map to embedding.
*  Again, as you said, because the vocab is much smaller,
*  so the embedding size we need should be also be smaller.
*  Right?
*  Like otherwise it's such a waste
*  if you have like 4,000 embedding dimension
*  to capture a vocab of 256, that doesn't make sense.
*  So in our paper, actually, the embedding size
*  we pick as 32, which is very, very small.
*  So you are mapped to one hot vector of 256.
*  That's what people to represent a naive vocab
*  is one hot vector.
*  And then you change that to a dense vector of 32,
*  like one dimensional, dense floating point vector
*  with dimensional 32.
*  It's an eighth as big.
*  Yes, yes.
*  So we found that it's not a big,
*  it doesn't really impact that much.
*  We can actually go even smaller,
*  but it's actually a very small module.
*  It didn't optimize that much.
*  So there's still this embedding
*  and you're learning your own embeddings
*  as part of this process.
*  There's not like an off the shelf embedding
*  for this, I suppose, right?
*  Yes, everything's not end to end.
*  So basically you know that matrix, that's more matrix.
*  The patches are the same.
*  So it doesn't matter if I'm in patch one or patch two,
*  patch three, if I have the same bytes
*  that gets converted to the same embeddings
*  and the same data flows into the global model,
*  regardless of which patch that is coming from.
*  Yes, 100%.
*  So there's slight difference.
*  The difference is the position embedding.
*  Yeah, yeah, so position embedding,
*  there's like separate position embedding
*  for the local model and for the global model.
*  You're gonna know which patch you are coming from
*  and which letter inside the patch.
*  So the model actually know your position fully,
*  but the embedding is the same actually.
*  It's exactly the same for Transformer
*  because you know, Transformer has no sequence.
*  Everything's parallel.
*  The matrix has no idea of the sequence
*  and every position information
*  is not from this position embedding.
*  Helpful and clarifying.
*  So I'm up to, I think I understand everything now,
*  up to the global model
*  and the global model, if I understand correctly,
*  is basically a Transformer, right?
*  It is, so it has all the normal features
*  that we would expect from a Transformer,
*  which is to say your residual stream,
*  your attention blocks, your MLP blocks,
*  your non-linear kind of gate
*  and the difference in this case is that
*  its output gets directed to all the,
*  instead of being the final output,
*  its output is the input to each of the local models
*  that are gonna do the final set of predictions.
*  That's perfect, yeah, that's very, very correct.
*  Going back to that panning concept.
*  So, I mean, here's a really naive question.
*  When I'm thinking about predicting text
*  and maybe the answer is gonna be like,
*  don't think about text,
*  maybe think about a different modality for this,
*  but I'm looking at the diagram and it's like,
*  you've got kind of megabyte, tran,
*  are the sort of 12 letters that have been predicted
*  and then as it works its way through,
*  then the output is that the next,
*  the fourth patch is predicted
*  and now at the end you've got four more characters,
*  megabyte, trans, and the last four are S-F-O-R,
*  so you predicted that kind of chunk of four letters.
*  My first question is, why do we even need
*  all of the different local models?
*  What are they doing?
*  Like, what is even happening there?
*  Because my naive, there's gotta be something wrong
*  with my understanding, but what I'm kind of thinking is,
*  okay, you take all this stuff, you do the embeddings,
*  you feed it into the global model,
*  the global model does its thing,
*  but it's really only the last patch
*  that's predicting new content.
*  Ah-ha, I see what you mean.
*  Yes, yes, yes.
*  Okay, so this actually come to,
*  this actually come to how language,
*  so okay, this is a language model,
*  how language model works, even with tokens, right?
*  Even with tokens, you predict every words.
*  So with a sentence, for example, today is sunny.
*  You still predict today with empty input,
*  and you predict is with today, and so on.
*  So you are not only predicting the sunny.
*  So it's the same here.
*  So basically, the model need to know that,
*  see the first ever, the left column, for example,
*  the model need to know that with padded patch,
*  the very red, the most red color,
*  the pad with a padded patch,
*  but it's basically empty patch,
*  it need to predict this mega.
*  That's equivalent with you say empty,
*  and you predict today, and they say the patch plus mega
*  is need to predict the byte, the B-Y-T-E.
*  The one efficient thing about the autoregressive prediction
*  is they predict every words.
*  That's why this learning is efficient.
*  So, and that's done by this,
*  that's done by two things.
*  One is this padding, the other one is triangular masking,
*  the causal mask.
*  Yeah, so basically, we also want to make a prediction
*  on every local patch.
*  It's the same.
*  So we want to predict, so that the loss
*  has rich information about the modeling.
*  We want to, so there are four local model,
*  and every local model's prediction
*  gonna compare with the ground truth and get the loss.
*  So we're gonna have, if we simplify it,
*  we're gonna have 16 loss.
*  So every predict, because there are 16 character,
*  so each character has ground truth to compare into,
*  and then we're gonna get a loss,
*  and in the end, the loss is average.
*  So maybe just starting with vanilla transformer
*  that I'm most familiar with,
*  and everybody in the audience will be more familiar with.
*  I don't know how well understood this is.
*  It's easy to kind of forget
*  and just kind of background this fact,
*  but when you do a forward pass through a transformer,
*  you are not just predicting the final token,
*  but you are actually generating a full set of predictions,
*  which in the case of like a GPT-3 type of model
*  would be full distribution across the entire vocabulary,
*  50,000 tokens at every token position.
*  Now you're not using that at the end,
*  because you already know ground truth there
*  for what all the input tokens were,
*  but you can kind of examine those if you want,
*  assuming you have access to the outputs,
*  which increasingly you have to run your own thing
*  to have that, but you can see along the way that,
*  oh, this token was a surprising token,
*  this token was an expected token, et cetera.
*  So there's lots of kind of interesting things
*  you can clean from that.
*  But then also in the vanilla transformer,
*  there is this kind of look back mechanism
*  that happens through every layer, right?
*  So I guess the kind of,
*  when I think about a traditional transformer,
*  I'm thinking there's two reasons to do that.
*  One is what you said,
*  which is because I'm making a prediction
*  at every single token,
*  I have that many more predictions that I can feedback
*  and use to power my optimization.
*  But then also with the regular transformer,
*  up until the last attention layer,
*  you have some possibility, right?
*  For information from earlier tokens
*  to influence the last token
*  that you're actually here to predict, right?
*  Okay, now flipping over to the megabyte architecture,
*  it seems like maybe if I'm understanding correctly,
*  one of those holds, but maybe not both.
*  So you would still have,
*  you make the prediction for every single byte,
*  which in this case is you're making a 250,
*  because there's 256 possible byte values,
*  you're making a prediction for every possible byte value
*  at every possible byte position.
*  Because you're doing all those predictions,
*  you have all those loss measures
*  that you can then use to power
*  your back propagation optimization.
*  That's presumably particularly important
*  when particularly useful for like informing the global model.
*  But in this case,
*  once the, when you're actually doing inference,
*  once you're past the global model,
*  now there's no more communication, right?
*  Between the local models.
*  So I get kind of one of those two benefits, but not.
*  I see.
*  So I have to comment one on this.
*  This one comment is like, in the autoregressive model,
*  I feel like it's underappreciated
*  that we make prediction every token.
*  So basically if you have 16 token,
*  you make 16 prediction.
*  And that's different with the representation model,
*  which is BERT or Robata.
*  So that's like encoder model.
*  So GPT-2, GPT-3, extra show,
*  they are decoder only model.
*  And we are decoder only model too.
*  So for the encoder only model,
*  the loss is only on the masked tokens.
*  That's only 15% of the tokens.
*  So you do one forward pass,
*  you only get 15% loss on 15% of the tokens.
*  While for decoder only model,
*  you do one forward pass, you get loss on every tokens.
*  I think that's why, personally,
*  I feel that's one of the big reason
*  why decoder only model gradually gets so and so popular
*  and being able to enable very, very big model,
*  very, very, very powerful model, very, very uniform model.
*  That's one of the big reason,
*  because it can learn so efficient
*  and you get rich loss information
*  and you are able to leverage the data really well.
*  So that's a side comment, basically.
*  And of course, that's what we want to leverage
*  to make a prediction on every token.
*  And then that's supported by transformer.
*  So basically think about this.
*  This could be sequential.
*  So what that means, during inference,
*  you have this padded patch as input
*  and that goes to the local model.
*  And the local model gonna see this letter one by one.
*  They gonna see the pad, they predict one letter M,
*  and then they take the M as input,
*  M and padded together as input, they predict E,
*  and they take the pad and the two letter as input
*  and predict G.
*  So theoretically, it's supposed to down sequentially,
*  they predict one by one.
*  But thanks to the parallelism of the transformer,
*  we're able to, during training,
*  during training you can do the feed forward
*  and get every loss
*  and then you can get the loss all together.
*  So that's one advantage of transformer architecture.
*  That's also why everyone is using transformer.
*  Of course, I'm not saying other architecture,
*  people are also making efforts trying to make
*  other architecture scalable and parallelism,
*  but transformer is native for this
*  and it works really, really well.
*  And then as you said, for inference, yes.
*  So basically inference, we decode patch by patch.
*  We decode, see if we want to decode the trends, T-R-A-N.
*  We need to decode the first patch out
*  and take the first patch as input to fit into the global
*  and predict the second patch
*  and take the first two patch output as input
*  to predict the third patch.
*  And then within each patch, of course, byte by byte.
*  Yeah, yeah, yeah.
*  And within each patch, byte by byte.
*  So that's a small difference between, you know,
*  how model works in training
*  and how model works in inference.
*  I'm with you on the training portion.
*  If we are using the megabyte architecture for inference though,
*  is there any reason that I have to run the earlier patches
*  or if I'm just concerned with inference,
*  could I just run the final local patch?
*  So yes, if you know the previous patch,
*  you can run the last patch, right?
*  So that's come to see how
*  you want your language model to work.
*  So this is a question, for example,
*  if you ask your test GPT, I don't know, a coding question,
*  and then the model gonna generate
*  like the coding, like the whole coding answer.
*  So that means your question,
*  they don't need to run one by one,
*  they can run that parallel.
*  But everything the model generates
*  has to run token by token.
*  So it's the same here.
*  If you know the previous patch,
*  you can input that and run that parallel,
*  but everything the model don't know
*  and the model need to continue to generate,
*  it needs to run byte by byte.
*  So, but I'm stuck on this point only because it
*  will either help me confirm or poke a hole
*  in my understanding.
*  But if I am doing new inference
*  with the megabyte architecture,
*  I have to run the whole thing in the loop
*  because I'm predicting one patch at a time
*  and I can only predict one patch at a time
*  because any future patches depend on that patch first,
*  that's basically the meaning of autoregressive.
*  But when I look at figure one and I'm thinking,
*  okay, there's four patches here.
*  Do I in practice, could I just like not run
*  the first three patches at inference time
*  and just embed, you know, do all my local embeddings,
*  do my global model and then just run the final patch.
*  Do you know about the first three patch?
*  Is that given?
*  Yeah, so let's say I'm doing exactly this example.
*  So I've, my first three patches are megabyte, tran
*  and I input those, they get embedded,
*  they get passed into the global model.
*  The global model does its transformer thing.
*  It then produces outputs that would feed
*  into all four patches.
*  But I'm trying to confirm what I think I understand,
*  which is that at that point,
*  there's no further information exchange between the patches.
*  And so if I'm only concerned with the new patch output,
*  then I could just say, okay,
*  I'm gonna ignore those first three patches
*  of output from the global model
*  and only process the fourth patch from the global model
*  because that's all I really need the output for.
*  Yes, that's a hundred percent.
*  Say like after this global model, right?
*  You get four labeled as edge global out
*  in our, the hidden representation of global out.
*  At this point, you can only take the last one.
*  You can only take the last one
*  and then you're gonna use that together with a local model
*  to decode the last bytes you need, yes.
*  Okay, cool.
*  But in training, you do have to do,
*  or you don't, I guess maybe you don't have to,
*  but you do run all of them because they all contribute
*  to the presence of all these loss values
*  that then you can use to optimize the model end to end
*  in the first place.
*  Yes, yes, we want to loss from every, every byte, yes.
*  So that is really interesting.
*  This is not like a strong theory of mine,
*  but increasingly I see kind of a lot of things
*  and I'm like, a lot of these things seem like isomorphic
*  to other things or kind of nearly so.
*  So I was thinking, is there a sort of modified
*  like vanilla transformer that I could kind of imagine
*  that would be akin to this?
*  And what I came up with was like,
*  typically the transformer has like the same width, right,
*  throughout, it has kind of the same dimension at each block.
*  But here you're kind of shrinking the dimensionality
*  of the input in order to have a more efficient global model
*  and then kind of chunking in order
*  for kind of more efficient parallelization.
*  Do you think you could kind of do something similar
*  where if you devise a transformer,
*  you said like the early layers are gonna be wide,
*  but then they'll go through like a bottleneck
*  and then at the end they'll get like particularly narrow.
*  Does that seem like it would potentially
*  have some similar value?
*  Yeah, yes, yes.
*  I think, so there are a couple of things.
*  I think one thing we really want to do is try
*  to take advantage of the powerful transformer.
*  So in some sense, the global model is impact transformer
*  and the local model is also impact transformer.
*  So that's something actually by design
*  because as you said, there are many, many optimization
*  of the transformer architecture
*  and some of them is very memory efficient.
*  Yeah, some of them is flop friendly,
*  but in the end what we really care is how well it scales.
*  So I think there are lots of great work,
*  but they need to test at large scale.
*  So nowadays I think most people do large language models
*  still using the dense transformer
*  because it's most well tested and it's performed well
*  when you have a lot of model,
*  lots of data and a lot of compute.
*  I think that's why we don't want to touch that
*  and in many sense, see one day people found
*  efficient attention mechanism, we can just swap in, right?
*  Because we can swap in the attention in local model
*  and swap in the attention in the global model
*  with this new attention mechanism.
*  So that's by design.
*  Second is this auto-regressive prediction
*  and this masking is actually very, very important.
*  So basically if you want to do also auto-regressive
*  transformer, you have to guarantee that.
*  Otherwise you have information leaking
*  and you have information leaking
*  and then your model will learn nothing.
*  So like the large language model learning,
*  you need to make the task also challenging.
*  If you either know the ground truth,
*  I just copy from my input.
*  When you patch the transformer locally,
*  it's really hard to guarantee that.
*  So basically because we have this triangular masking
*  on the input, if you arbitrarily rescale your inner dimension
*  or as you said, make the model wider or narrower,
*  you have to add very, very complex masking strategy inside
*  and it's really, really hard.
*  So that's the thing.
*  And third thing is there's something quite pretty
*  about how we design this global model.
*  So basically the global model has shorter sequence.
*  So a shorter sequence has not,
*  actually has couple of advantage.
*  One is on the attention.
*  That's what when people can't think about the sequence,
*  that's what people care the most
*  because apparently this quadratic memory scaling
*  give people issue when you have long sequence.
*  But if you make the sequence shorter,
*  it also reduce the feed forward.
*  We also discussed in the paper.
*  So in nowadays feed forward is most compute expensive part
*  of your model.
*  See if a GPT-3, it's only the attention only take
*  two, 3% of your whole compute.
*  Feed forward is a big chunk.
*  And the way we do it for the global model,
*  it's one over P like the normal flop of a transformer,
*  of a naive transformer.
*  So see, we take the passes of eight.
*  Now our global transformer only need to take
*  one, one, one eighth of the compute
*  and we can make it bigger and more powerful.
*  I think that's why we stick to this current design
*  for many reasons.
*  Yeah, that's really interesting.
*  And then I suppose too,
*  it also sort of suggests the potential for modularity.
*  I mean, we see all these projects where certain,
*  a language model is frozen and combined to something else.
*  And I can, as you're talking about this,
*  I can start to easily imagine freezing different parts
*  of the model, having different kinds of local models
*  that could perhaps be swappable depending on,
*  you may only need to fine tune the local models
*  for certain tasks or who knows what, right?
*  But it seems like that would be,
*  this architecture would lend itself quite nicely
*  to modularity downstream.
*  Yeah, yeah, yeah, yeah.
*  I totally agree.
*  I think there's like, there's actually in the VOM,
*  like V language model, there's such architecture
*  to adapt to like say, upper chains.
*  So adding like image understanding
*  and maybe even image generation functionality
*  on top of pre-trained text language model,
*  there's, it's quite, in essence, it's quite similar, yes.
*  Yeah, almost like a different head, so to speak,
*  if you had a similar, maybe even the same concept,
*  but yeah, you have a, if you can train a single global model
*  that can handle different kinds of inputs
*  and represent them in a meaningful way,
*  then you could have different local models
*  that create different sorts of outputs based on that
*  single understanding.
*  Yes, 100%.
*  Yeah, this is really interesting.
*  So, and it's no, the more I learn about it,
*  it makes sense why some of the leading thinkers
*  in this space have been very excited about this paper.
*  You've kind of covered a little bit already the,
*  how you choose the patch size.
*  It seems like that's basically a trade-off.
*  The way I was thinking about it,
*  and you can complicate this,
*  but I was kind of thinking in the limit,
*  if you just had one giant patch,
*  then you basically just have one giant model
*  or two kind of stacked global models,
*  which would have all the normal downsides of that.
*  If you, on the other hand, took the other limit,
*  then you would have kind of an insane number of patches.
*  And I guess I don't know exactly what goes wrong there,
*  but it seems kind of silly.
*  So you're kind of looking for this happy medium
*  in the middle that trades off these two extremes,
*  and that's an experimental process, it seems.
*  Yes, yes, 100%.
*  As you said, either you choose patch size as the whole thing
*  or use two patches as one, that's like both two extremes.
*  We just become a normal transformer, basically.
*  Okay, so the patch size of one, yeah,
*  it doesn't have to do anything.
*  Then it's just the global model,
*  choose those to the output, okay, that makes sense.
*  Either ends, we become the naive transformer,
*  and our model actually also, I mean, in our experiments,
*  we also oblade that.
*  And actually we found out with combination of both two,
*  it's really, really helpful.
*  Then it comes to the question, how to choose a patch size.
*  So theoretically, we should, like,
*  if you want to optimize the memory of your attention,
*  we have a formula to help you how to choose a patch size.
*  But we actually pick the patch size
*  quite heuristically right now.
*  Say for text, we try to stay,
*  don't stay too much away from BPE token.
*  So right now BPE token normally have one BPE token
*  corresponds to do around about four bytes.
*  So we kind of pick a byte,
*  we pick patch size of eight to be not far away from that,
*  but also compute the efficient.
*  And for image, we kind of like,
*  pick patch of eight by eight or 16 by 16.
*  That's what people do with the image token either.
*  So basically how we pick the patch size
*  is kind of like inspired by how people do the tokenization,
*  but we don't want the tokenization at all.
*  So in our paper.
*  So that being said, it's actually a good,
*  in our paper, we also studied how to pick certain patch size,
*  but I will see that's not comprehensive at all.
*  Like we do need more study wide range of that,
*  especially that's going back to the long sequence story.
*  If we make the local embedding local model
*  as strong as a normal transformer,
*  see 2000 tokens, right?
*  The local model, 2000 tokens.
*  And we only have say eight or 16 of those patch,
*  then that means we're training a 16K or 32K,
*  like normal transformer.
*  So I think there's a whole wide spectral,
*  how we can pick the patch size.
*  But interestingly, overall, we find a wide range of patches
*  actually worked quite well for our task.
*  So that's something definitely needs more analysis,
*  which region and how we do the model size to pick to.
*  We do find it's quite stable to the patch size at this point.
*  Yeah, it's interesting.
*  These, I guess the intuition for that would maybe just be
*  that there's some curve and it's kind of relatively flat
*  near the local minimum.
*  And so you have kind of a range there
*  that you won't see too much difference with.
*  Maybe you could just kind of describe
*  the different multimodal experiments.
*  Cause we've talked largely about text,
*  but there's also stuff pertaining to image and even music.
*  Maybe just give like a little rundown of kind of,
*  even just what those data sets are.
*  Cause I don't think people have a great sense,
*  when they see a name of a data set,
*  what even is that task?
*  So give us just a sense of kind of the generality
*  that you've been able to demonstrate.
*  Yes, yes, yes.
*  So basically this auto regressive language model
*  has been very, very popular on text,
*  but people also have been doing that for both image
*  and audio for very, very long time.
*  However, for image, due to the challenge I just described,
*  the image has very, very long sequence.
*  It's not as popular, but even earlier,
*  right after transformer, there's image transformer.
*  However, they have to compress inputs.
*  So it's also a lossy process.
*  The same as audio, like back in, I believe it was 2016,
*  there's like WaveNet that you predict
*  the audio wave one by one.
*  So the task, basically it's a thing.
*  It's predict something, the something's bite,
*  predict bite one by one.
*  And for image, it's normally come with image size,
*  say, you know, 4K image.
*  So the 4K image, when you read the raw image,
*  it's 4K times 4K, so that's like the square,
*  times three, three is normally the RPG channel.
*  That's many of bytes, that's your whole image.
*  And for us, it's like, we just take it,
*  and this is like two, this is a 3D matrix.
*  One image is 3D matrix, and we just flatten it out.
*  And that's your input sequence.
*  That's then become a 1D sequence.
*  And now you can just treat that as text,
*  and you predict one by one, one by one.
*  There's a little bit of a caveat of that.
*  We actually didn't, it's purely flat it out.
*  We take a patch by patch, like eight by eight patch,
*  and eight by eight patch, and then flatten it out.
*  That's illustrated in the image.
*  But for simplicity, it's like, for image,
*  you just take this input pixel value,
*  and you make it 1D, and you predict one by one.
*  It's the same for wave, so when you read,
*  or audio, audio is represented as wave.
*  So you can read the wave input,
*  just that becomes a 1D byte sequence,
*  and you predict one by one.
*  So basically, that's a bigger difference.
*  And for image, you just predict one by one,
*  and compare with ground truth,
*  then that's give you per bit per bit per dimension.
*  There are many way you call the matrix,
*  but it's all the same, basically,
*  how well can you accurately predict
*  one value out of 256.
*  And then we actually achieve state of art
*  for the smaller image, which is actually
*  the same state of our value,
*  matching state of our value on image 64.
*  And of course, we don't want to stop that.
*  The reason we compare image 64 is
*  people rarely do longer sequence of image,
*  it's just because earlier model didn't support that.
*  So, but to illustrate the capability of our model,
*  we did image of 256, as well as image of 640 pixel value,
*  that's equivalent to one million bytes
*  when we flatten it out into 1D.
*  So that's the image experiment.
*  And on the audio experiments, basically,
*  we take some audio book data,
*  where basically audio book data,
*  as well as some speech data,
*  basically think about in the end is just wave,
*  and you want to know how well your model
*  can accurately predict or recover those waves information.
*  So there's actually very, very interesting thing here,
*  is normally the audio is encoded,
*  not by the eight bytes, not by the big bytes of eight,
*  which equivalent to 256 value,
*  is actually 16 bit steps.
*  So that means like you read one value,
*  and that's not pick one out of 256,
*  that's actually pick one out of 65,000.
*  That's actually give people earlier in earlier research,
*  that's actually give people very much headache,
*  because the softmax over one over 65,000
*  is very, very expensive.
*  So what people have been done is either
*  do a classifier based approach
*  to map each of the value into one out of 256,
*  or they do hierarchical decoding.
*  So on the decoding, they do like tree like decoding,
*  decodes into something and smaller bin value,
*  and then further decode.
*  So that has been a big issue.
*  But what we are doing here is like,
*  we just read the file by,
*  so we ignore like, okay, what's the,
*  what, you know, the particular encoding
*  and decoding of audio file, we just ignore those.
*  We take the file and read the bytes and model that.
*  I think that's actually very interesting.
*  And that's the future direction we want to explore.
*  Basically for certain file,
*  forget about its image, its audio, or its video,
*  you just read the bytes.
*  You just read the byte value, and then you model that.
*  I think that's gonna be very, very interesting.
*  I wanna kind of cover results,
*  and then I wonder if there's any, you know,
*  things that you would flag in terms of like,
*  you know, what at a high level, you know,
*  are there trade-offs here?
*  The results you kind of present in two ways,
*  as I understand it.
*  One is basically that you kind of compare a,
*  I believe it's a compute matched experiment
*  where you say, okay, I have a certain compute budget.
*  I'm gonna train a transformer, you know,
*  classic transformer, and also you do the
*  first receiver architecture,
*  and then you've got the, you know,
*  the new megabyte architecture, but same compute budget.
*  I'll train them each as well as I can
*  on this given compute budget,
*  and then I'll compare how they do in the end.
*  And that is done on a byte by byte basis, right?
*  So we're using kind of the same encoding in that experiment
*  and finding that when you're dealing with bytes,
*  like the megabyte architecture just blows away the others.
*  But then the other question is, okay, well,
*  people don't usually do transformers in that way
*  for all the reasons that we've discussed.
*  So then the other approach is,
*  let's take a data set, same data set.
*  And here I was a little bit confused,
*  but it seemed that you're taking the same data set,
*  training transformer, receiver AR,
*  and the megabyte on that same data set.
*  Say it's a text data set.
*  I wasn't quite clear how the compute budget
*  compared across those different architectures,
*  but the key punchline is the results are comparable.
*  Yeah, so it's actually,
*  it's actually experiment hard for us to do,
*  I mean, the latter case.
*  Let me first explain why compute matching is so important
*  because it's actually quite well,
*  quite known to everyone basically
*  for a quite scalable and capable of model architecture,
*  adding more data, as well as adding more compute hours,
*  with the right setup, it normally gets better
*  as you train longer and yeah, train longer
*  and adding parameters to it.
*  So that's why we think compute match
*  is very, very important.
*  It's just like opportunity costs.
*  If I take the local transformer
*  and I just add on top of the global transformer,
*  that's for free, right?
*  It's definitely, like most of the cases gonna get better,
*  but what we want to consider is opportunity cost.
*  If you want to add a global model,
*  you have to make your local model smaller
*  because you only have such compute.
*  So that's the same.
*  So that's a general idea we want to do compute a match.
*  So that's why we implement this Perceiver AR in-house.
*  Of course, we run the experiments to validate.
*  We get comparable experiments from the original paper,
*  but in the compute experiment,
*  we run the baseline, which is Perceiver AR,
*  of course, another baseline, which is naive transformer.
*  We run the three model all ourself
*  and the three model are seeing exactly the same data.
*  They are training for exactly the same hours.
*  So we think that's a fair comparison.
*  And that's what really makes us happy to get a confidence
*  why a megabyte is good.
*  However, as you said, most people don't do this way.
*  When they publish paper,
*  they don't tell you exactly how many hours they train
*  on which GPU was the best size, et cetera, et cetera.
*  So we also want to convince, also let us know,
*  do we comparable with other implementation?
*  We want to compare to more models,
*  but many model we don't know the detail.
*  So in that case, for the benchmark run,
*  we try to run the model longer until the model converge.
*  That means like the validation loss
*  is not going down again.
*  And we take that value to compare
*  with what people has been reporting in their paper.
*  But again, we don't know exactly
*  what's happening in their paper, but that's idea.
*  We want to at least reach a ballpark
*  or at least we know we are not using more compute than them,
*  but we still get comparable performance.
*  So I think that's in high level,
*  two sets of experiments we're running.
*  So this is table three, right in the paper.
*  And so the bottom section,
*  the bottom three lines are all the experience that you ran
*  with the byte level encoding.
*  And you're basically showing there,
*  Megabyte dramatically performing the other architectures
*  with the byte level encoding.
*  And then compared to the top section,
*  it's that validation column where,
*  and I guess also the test column,
*  where you're sort of saying, okay, now,
*  and this is where I'm a little bit unclear
*  as to exactly like, maybe you're also saying,
*  like it's not fully clear.
*  It's not always known exactly what somebody else did.
*  But if I compare the Megabyte row at the bottom
*  to the, let's just take the top one,
*  the transformer Excel from the top,
*  do we know the relative compute budgets of those?
*  Or we just know like the data set it was trained on?
*  Like what is the constant in that comparison?
*  Yeah, the constant in the comparison is only data set.
*  Unfortunately, many of the work,
*  we don't know how much the, how much compute they used.
*  But one thing is like PG-19 is a small data set.
*  So basically that means you run multiple epochs
*  of it for other in-house experiments,
*  for example, say table two,
*  those data sets are much larger than PG-19.
*  But unfortunately, people didn't really report
*  all those data sets.
*  So yeah, we are definitely doing like
*  confined optimization here.
*  So again, the bottom line is,
*  if you use the byte level,
*  byte level encoding, byte level prediction,
*  then the Megabyte architecture
*  is blowing the other side of the water.
*  But if you're kind of comparing on,
*  let's say something like each architecture
*  working in its optimal condition,
*  then you can get kind of comparable performance.
*  And then the punchline is,
*  but you still get all these other advantages
*  of the Megabyte architecture that we've discussed.
*  Actually, that's not a full story.
*  The full story is for bytes.
*  We believe Megabyte is the best.
*  But what people are interested in too is like,
*  see if you have byte input, what's the optimal?
*  We already know Megabyte, we're pretty sure.
*  But another question is like,
*  on byte prediction task, we're the best.
*  But is a byte prediction task as a language model task
*  work as well as when you have tokenizer
*  for the language task?
*  I think that's what we try to get insight from table three.
*  So we didn't really answer that in this paper,
*  but we're working on that right now.
*  It's like, see, byte level has its advantage,
*  but we want to know,
*  can we just replace the tokenizer as a whole in the future
*  and get wide adoption
*  so we don't need to worry about tokenizer
*  with all the troubles I just mentioned
*  at the beginning of our conversation.
*  So that's something we are currently working on.
*  So there's a conversion process there
*  where you're basically saying,
*  we're gonna rescore our byte level prediction output
*  as if it were delivered in token form,
*  and then we can kind of compare
*  on a more apples to apples basis.
*  That's exactly what happened here
*  when you see table three and table two,
*  their value is in totally different range, right?
*  Because table two also have PG-19 results
*  and the BPB is around one.
*  But when you see table three, that's converted.
*  That's converted to token way, like word level publicity,
*  and it's in the range of 42.
*  So there is a conversion between them.
*  So you see table three,
*  that's word level publicity of 42
*  actually is equivalent to 0.8 BPB.
*  So maybe that's a confusion.
*  The reason is because the top session,
*  the top other work, they don't report the BPB value
*  so there's no way we can compare.
*  So we have to convert our results
*  to word level publicity, yes.
*  The upside of this hopefully is pretty well established.
*  You've got these, the avoidance of all the tokenization,
*  you've got the natural flexibility
*  to handle all these different modalities.
*  There's the compute efficiency,
*  the performance is all there.
*  What do you think happens as you scale this up?
*  I mean, there's a couple of interesting little wrinkles
*  in the paper, particularly around the strided inference
*  where there seems to be this,
*  there is some sort of performance penalty
*  associated with the boundaries between the patches.
*  And so you have an interesting strategy for overcoming that.
*  But then I've also seen,
*  most of the commentary on this paper online
*  has been like effusively positive and really hyping it up.
*  But one of the more interesting things I saw,
*  and I really don't have an intuition for this myself,
*  but I wonder if you do,
*  was somebody said, this looks amazing.
*  I do wonder if it will demonstrate the same sort of
*  in context, few shot learning type behavior
*  that the vanilla transformer does.
*  Maybe it wouldn't because of the sort of
*  early localization of information perhaps.
*  So maybe just for starters,
*  tell us about what you kind of observed
*  in the patch boundaries and how you overcame that so far.
*  And then how that may develop and what you expect
*  as you think about scaling this stuff much bigger.
*  Yeah, so basically, again, as you said,
*  see, if we want to answer this question,
*  will people adopt this in a wide range?
*  I think the only way to test that is scale it up.
*  Because nowadays people don't really care about
*  if you train a model that's less than one billion
*  and you only train less than let's say 100 billion tokens.
*  People don't really care about that
*  because we already know there is a region
*  that's model can be more powerful.
*  So that's what we currently working on.
*  See, can we train using similar computer of Lama
*  and get matching performance on Lama?
*  And then we don't need the token either.
*  That's what we currently work on.
*  We think that's ultimate test if that's gonna work well
*  and being able to get adopted and being wisely used.
*  One thing about the boundary is,
*  so that's something really, really interesting.
*  And we have a couple way of thinking like how to solve it.
*  So one thing we explore a little bit
*  is the convolutional layer.
*  The convolutional layer actually improves the model slightly
*  but it didn't improve too much.
*  Ultimately our hope is that's gonna be actually solved
*  with scaling.
*  When the model is seeing enough data,
*  the model should learn the invariance across the boundary.
*  So I think that's exactly the ultimate goal
*  and we're very hopeful to see more data
*  model can learn that.
*  On the other side of in-context learning,
*  I think in-context learning,
*  you shouldn't really to be worried
*  because it's all showing in the publicity, right?
*  Like ultimately if the model can understand
*  and predict the next word well,
*  which is showing in the publicity,
*  then your in-context learning shouldn't be a problem.
*  So I think ultimately, again,
*  I think both question should be answered
*  when we have this large compute
*  and large model size experiments done.
*  There's a lot of surprises in these systems, right?
*  Like in some sense, it's all a giant surprise
*  that transformers have scaled as well as they have
*  and seem to be,
*  even Jan LeCun has recently said some things about like,
*  yeah, they probably do have some nascent world models
*  and he wouldn't go as far as calling it
*  a full world model, whatever.
*  Obviously there's a huge debate around that
*  but it does seem like these things kind of keep surprising us
*  on the upside in general.
*  Do you have any sense for how the surprises
*  with this architecture might be different
*  from the surprises we've seen with kind of,
*  the vanilla transformer or is that just something
*  that we have no way to guess
*  except to go scale it and find out?
*  I will say if it's a surprise,
*  it needs emergent behavior.
*  Like, yeah, most of the time,
*  just let us get surprised.
*  But one thing we hope that it can better at
*  is actually code and math.
*  It's less talk about,
*  but actually coding as well as math problem,
*  that's something like, you know,
*  kind of like big issue with token either.
*  And as well as like sequence length,
*  like the coding when you need to,
*  you always need longer sequence for you
*  to be able to model like the coding problem.
*  Also the way you tokenize is just really, really unnatural.
*  See, we get our part to the proper lessity
*  of a normal language model, cinema.
*  We are also like really looking forward to see
*  how this skilled megabytes work on math and coding problem.
*  Yeah, that's one of the domain
*  we want to really watch closely on.
*  Yeah, the math in particular definitely makes a lot of sense.
*  Some of the explorations of like
*  what a typical language model has to deal with
*  in order to figure out math at all is,
*  it can be pretty crazy sometimes
*  where it's like these long integers,
*  people try to get it to add together
*  are actually being parsed into like two
*  and three digit tokens.
*  And it's like, oh my God, no wonder it can't do the math.
*  You know, when it's looking at it like that,
*  it's definitely coming at it from a, you know,
*  serious deficit for starters.
*  The coding one I have a little less of a intuition for
*  just because it seems like tokenization there,
*  I would guess is usually less weird, but.
*  Yeah, so one thing, one interesting experiment is like,
*  again, token, like at the very beginning,
*  we talk about why people need the tokenization
*  to compress, right?
*  If you take your domain and you compress it's really,
*  and then you run your DPE,
*  you can't get a different tokenizer.
*  And that may give you a different compression rate.
*  So what we do is like in one of the earlier work
*  of my colleague, the encoder,
*  basically it's almost like a codex model
*  developed by Meta too.
*  So that's like code specific language model.
*  If you take the common DPE,
*  which is like DPE to DPE tokenizer,
*  compare with, let's see,
*  which are in-house tokenizer,
*  we can get 30% less of token.
*  That's just tell you like a DPE to tokenizer on code
*  is not efficient.
*  It's like 20, 30% less efficient.
*  So it's very, also very domain specific,
*  also think about in code,
*  sometimes there is like multiple space or something.
*  It's really hard to figure like how BPE token handle that
*  and how that's actually meaningful.
*  Yeah, I think there are issues with current way
*  how people do that.
*  Yeah, this probably also seems like it connects to,
*  I mean, they haven't published a ton about this,
*  but it's kind of gradually come to public light
*  that the latest open AI models have a lot of code
*  early in their training.
*  And presumably this is kind of related
*  where there's like with presumably
*  more code friendly tokenization,
*  it has an easier time learning certain logical structures.
*  And then that can kind of benefit all tasks
*  in a way that is really hard to get,
*  to happen with just traditional natural language
*  and traditional tokenizers.
*  So yeah, that makes me actually start to think that
*  maybe this is going to just be,
*  this might just be strictly better,
*  which I'm sure is what you're hoping too.
*  Yeah, yeah, I think too many sense,
*  even we are happy with the simplicity part.
*  So I don't know if you're familiar with the Galactica work
*  also from Meta.
*  So it's particularly trained on archive and science.
*  There are actually a whole strategy, how you tokenize it.
*  So there's like, oh, it's like in this case, we use BPE,
*  in that case we do byte,
*  in that case we do digit splitting,
*  in that case we do this.
*  So there are three or I believe like three or four rules
*  combined together just to do the tokenization.
*  So that's actually, the users won't really feel the problem
*  because maybe like the only concern as you said,
*  is that you run the tokenizer
*  and then know how many tokens you are,
*  and then that's gonna change your expense.
*  But for developer actually is quite tricky
*  to pick all these rules,
*  how to handle correctly and effectively.
*  And when you decoding,
*  you also have like different way of decoding it.
*  It's actually a hassle.
*  Yeah.
*  So we are hoping this kind of simplify everything.
*  Yeah.
*  Anything else in this work that you wanna highlight
*  that we haven't got to so far?
*  We are very excited about the either,
*  scanning the app or say to be able to directly
*  in the future model the raw format of any file,
*  any input, any modality.
*  I think that's like really exciting direction for us.
*  Yeah.
*  So I'll be looking out for the next paper.
*  I just looked to the,
*  this one was published May 19th.
*  And it's, we're recording here about a month later,
*  knowing the size of the clusters
*  that you guys are working with over there.
*  I feel like I can set my stopwatch
*  and it shouldn't be too much longer
*  before we get some of these questions answered.
*  I think it'll certainly be very interesting to see
*  how that comes out.
*  Maybe just zooming out
*  for a couple of kind of big picture questions.
*  Meta AI has really been on a sort of incredible role lately
*  and has been the subject of quite a bit of speculation.
*  There's like the Google memo that says,
*  and I don't necessarily endorse
*  all the conclusions of that memo,
*  quite the contrary,
*  but the idea is that, you know,
*  Meta is winning because it's got
*  this big open source community.
*  What's it like to be at Meta AI right now
*  with kind of hit after hit?
*  What is the vibe?
*  What is the kind of big vision?
*  It seems like it's probably very different
*  from some of the other places,
*  but I'd love to just kind of hear your reflections
*  on what it's like to be a part of that.
*  I have to tell from my personal angle.
*  On the other hand, I'm also working on like in general,
*  multi-modal, multi-modal language model.
*  So I think, as I said, that's one of the inspiration
*  why we did the megabytes.
*  And in our team, we also believe the future
*  belong to multi-modal or mixed model.
*  We are not think about now we have CHPT,
*  now we have the journey.
*  Why can't we have a unified model
*  that's being able to do everything?
*  That's definitely one big trend we're working on
*  and it's really, really exciting.
*  I cannot ask for more at this stage.
*  You know, it's been striking to see obviously lately,
*  so much focus has shifted toward AI safety
*  and different organizations have kind of come out
*  at the leadership level and signed on to,
*  the extinction risk statement, OpenAI, DeepMind,
*  Anthropic have all leadership
*  that those companies have signed on.
*  Is there like an active dialogue
*  about this within the MetaAI team?
*  I imagine there has to be,
*  but we haven't really heard as much about the kind of,
*  how do we develop all this technology
*  without losing control of it from Meta?
*  Yeah, of course, of course.
*  We formed like couple of like responsible AI team
*  and we are always very, very careful about the data.
*  We are always very, very careful
*  about the bios coming of the model.
*  We have very, very strict,
*  like how we do open source,
*  even though at least right now in my team,
*  like the big org, the Meta Research Lab,
*  we still have open source as our,
*  open science as our major goal,
*  but the process of doing open source is very, very strict.
*  We have to parse all this bios filter.
*  We have to answer all this questions.
*  So that's basically embedded to every project.
*  Of course, like we do hear like every day,
*  like everyone is complaining,
*  why it's so hard to use this model?
*  Why it's so hard to open source,
*  sorry, use this data or open source this model,
*  but it's a word we have to live in right now.
*  We have to do responsible AI.
*  And again, on the other side,
*  there's like particular team forming.
*  So I think in Meta, we are very much following this,
*  but no matter how hard it is,
*  the researcher here are interested.
*  It seems like the leadership is online with open science.
*  We want to do open science.
*  I think, you know, again,
*  we believe that to be able to do responsible AI,
*  we shouldn't let few,
*  that's only represent my own opinion,
*  which we don't necessarily need only a very few number
*  of companies to do that.
*  We should open source it and everybody help debug,
*  help develop more safe model.
*  So yeah, yeah, I think it's definitely hated.
*  I will say everyone has different opinion,
*  but a baseline is like every open source model,
*  it has to have some like internal filter,
*  like it cannot be biased.
*  Yeah.
*  Do you think we're gonna start to see a sorting of
*  researchers across these orgs,
*  because it seems like the,
*  you've obviously published this paper and, you know,
*  along with that comes some fun stuff.
*  Folks at OpenAI, you know,
*  these still still be published some,
*  but like obviously not nearly as much.
*  If they had invented the megabyte architecture,
*  I doubt they would have published it at this point.
*  So it almost seems like there may be,
*  be developing a kind of divergence of like people that,
*  you know, value the open source ethos and,
*  and want to share,
*  go to places like Meta and people that maybe have a more,
*  you know, we want to build a world changing product or,
*  you know, we feel like we have to keep this stuff secret
*  because it ultimately is too dangerous to share.
*  They go to these other labs.
*  Do you see kind of a polarization or a self sorting
*  starting to take place?
*  Yeah. Yeah.
*  100%. I think that, I mean, that's avoidable.
*  When the AI industry is mature enough so that you can quick
*  prototyping or quick productionizing,
*  there's a model or a certain idea.
*  I think it's also understandable for,
*  for certain company to say they don't release their model.
*  It's just unfortunate a little bit to the community.
*  For us, we, we are here, we choose Meta AI.
*  One of the reasons we believe open science
*  and we are sticking to that.
*  But I do see, I agree with you.
*  I do see this polarization.
*  Another thing is it hasn't happened to Meta,
*  but it may happen is when the product team
*  and the research team is doing,
*  like the work is more and more similar,
*  the resources could be pulled into the product team easily,
*  you know, because the ultimate customer facing team,
*  like ultimate like customer experience team,
*  we as a research, as a pure research team,
*  we are doing research that's far ahead.
*  So in such a competitive space,
*  the property like the property has more priority.
*  So one set fact could be the resource shifted to towards
*  that towards the product team and we get less.
*  And you mean by resources there,
*  you mean just compute like access to GP years?
*  100%.
*  Yeah, well, it seems like so far so good on that front.
*  So far so good.
*  I think one of the most sort of unfortunate
*  and problematic dynamics developing in the world today
*  is the US China rivalry,
*  which seems like it's constantly escalating
*  and it seems like nobody can do anything about it.
*  And, you know, that would be bad enough unto itself,
*  but now it seems like it's kind of feeding back
*  into the AI discourse and almost every other conversation
*  I have about big picture AI questions,
*  you know, are we brushing into this?
*  Like is this, you know, do we have a good plan
*  to keep ourselves safe as we build these more
*  and more powerful systems?
*  So often the conversation kind of ends in well,
*  but you know, China will do it if we don't.
*  And so, you know, there's just kind of this low,
*  low trust obviously, and kind of, you know,
*  almost fatalism around like what other choice do we have?
*  So for one thing, I always love to just highlight
*  any positive, you know, connection or collaboration
*  that crosses the US China, you know, divide,
*  and you haven't grown up in China,
*  going to university there,
*  then coming to the United States, working here,
*  you know, in some sense, embody that.
*  What is it like for you right now to be at kind of
*  the center of both of these, you know, super hot topics?
*  Like AI is obviously super hot, US China is super hot,
*  but the, you know, center of that Venn diagram
*  is like maybe the most focal thing in the world.
*  And here you are, you know, publishing research right
*  from the kind of center of all of that.
*  What is that like?
*  And, you know, do you have any feelings about that?
*  It's actually, to me, it's not between US or China.
*  It's like every country can have different policy
*  about how to develop AI model.
*  And that could dramatic impact things.
*  One or two days ago, Israel, as well as Japan,
*  had a loss in like AI model could train on any data.
*  So that's not even in China, right?
*  It's just like in Israel,
*  and Israel nowadays have so many startup.
*  I can imagine a scenario is like now everybody
*  or the startup are gonna be an Israel company
*  so that they can train with any data,
*  they can have more freedom to develop their AI model.
*  Yeah, so again, I think this indeed is a big concern.
*  In the end, the easier way is everybody,
*  of course it's hard, everybody on similar page.
*  So they follow this rule of develop safe AI,
*  but I will say go beyond,
*  definitely go beyond US and China.
*  It's like worldwide.
*  Every country could be, you know,
*  the one who allowed to train the widest AI things there.
*  I just hope that, you know, clearer heads can prevail.
*  And it seems to me that, you know, any, again,
*  any flicker of positive relations between US and China
*  should be celebrated and, you know, elevated
*  and made more visible.
*  And, you know, certainly I've always been a, you know,
*  a big believer that to the degree that the United States
*  can attract people from around the world
*  and including from China, it's like a great thing
*  to bring people to, you know, the same research environments
*  and have this kind of cross-cultural collaboration.
*  So I don't expect you to have all the answers on that.
*  By any means, you've got your hands full, you know,
*  obviously just doing the research itself,
*  but boy, I wanna, you know, I hope we can continue to,
*  you know, to have this, the degree or hopefully even more
*  of the sort of academic and intellectual collaboration
*  that has existed and, you know, continues to exist,
*  but it seems like it's under some threat, you know,
*  and I just really hope that that can be built upon
*  and not, you know, not something we turn our backs on.
*  Okay, I think personally, I haven't felt this threat
*  or I, yeah, I think overall what I have felt
*  is like quite friendly environment.
*  I think this is great, phenomenal conversation.
*  I really learned a lot from it.
*  I'm glad to hear that you have not, you know,
*  felt any of that sort of thing personally.
*  I don't know to what degree people are feeling it personally,
*  but just you look at kind of macro numbers, you know,
*  the number of grad students coming is down,
*  the number of like Americans living in China is way down
*  and, you know, just in general,
*  there's this kind of decoupling phenomenon that,
*  especially as we head into this, you know, AI future,
*  I would like to see more coupling and not less.
*  So that's, you know, just kind of my overall point of view,
*  but I'm very actually heartened to hear that you have,
*  you know, have not found this to be a practical issue
*  in your daily life.
*  So that's good news as I see it.
*  Well, we'll leave it there then for now, again,
*  phenomenal work on the megabyte architecture.
*  I'm looking forward to the next paper
*  and seeing if you've just, you know,
*  changed the AI game, you know, across the board,
*  or if there are any limitations or surprises
*  that are unveiled, I'll certainly be keeping a close eye out
*  and reading your next publications with all that in mind.
*  For now, Lily Yu, thank you for being part
*  of the cognitive revolution.
*  Thanks, thanks for this nice conversation.
*  It's a pleasure.
*  Amnachie uses generative AI
*  to enable you to launch hundreds of thousands
*  of ad iterations that actually work,
*  customized across all platforms with a click of a button.
*  I believe in Amnachie so much that I invested in it,
*  and I recommend you use it too.
*  Use Cogrev to get a 10% discount.

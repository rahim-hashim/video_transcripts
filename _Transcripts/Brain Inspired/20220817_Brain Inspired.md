---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 4365s
Video Keywords: []
Video Views: 1546
Video Rating: None
---

# BI 144 Emily M. Bender and Ev Fedorenko: Large Language Models
**Brain Inspired:** [August 17, 2022](https://www.youtube.com/watch?v=HKRFObw2o5c)
*  Whether we can study the interface between language and actual kind of thinking and reasoning
*  capacities, I am dying to understand how that works.
*  I think that's the most intriguing thing.
*  It's not clear to me that large language models are something that the world needs at all,
*  certainly not larger and larger ones.
*  That's not a phenomenon in the world that, you know, a mountain that we climbed because
*  it was there kind of a thing.
*  We created the mountain as we were climbing it.
*  But if you want to build a system that can think, then it just seems a little bit misguided
*  potentially to just try to think that language will just give you that.
*  And again, I think the idea that it can comes from the fact that a lot of people think that
*  language is what made us smart.
*  Does it matter whether machines are learning language as much as they're learning it differently
*  from humans?
*  I would say yes in two ways.
*  One is to the extent that we're claiming that the machines are a model that we're going
*  to use to study humans, then we need to be very clear about what the similarities and
*  differences are because that gives us the limits of the model.
*  And then secondly, if we're going to be building technology that people are using, the way
*  in which the system was learned might put some limits or tell us something about the
*  resulting system.
*  Hello good people.
*  I'm Paul.
*  Large language models have taken over in the AI world, as you likely know, and their use
*  has extended beyond language, as you also likely know.
*  But in this episode, we're focused on the language versions.
*  So these are the models that are trained on enormous volumes of text, usually online,
*  and can do things like generate human-like language, answer questions, and so on.
*  And the most successful versions of them as of now are based on the transformer mechanism,
*  which I won't detail here, but basically works by learning the statistics of which words
*  appear near other words.
*  So one way they generate text is to look at what text has been produced so far and continuously
*  predict which word might be good to insert next based on the previous words, something
*  called next word prediction.
*  Ev Fedorenko is a neuroscientist who runs the Ev lab at MIT, and she, among others,
*  has been testing how these models compare to how our brains process and generate language.
*  It turns out, next word prediction seems to account for a large part of our language
*  abilities, something we discuss during the episode.
*  Emily Bender is a professor in computational linguistics at the University of Washington.
*  And recently, she has been considering questions like whether the models understand the meaning
*  of the text they produced.
*  The answer is no.
*  Whether we should be scaling up the models, as is the current trend.
*  The answer also is no.
*  So we discuss these topics as well.
*  Another thing that we discuss is the relation between language and thought.
*  Ev has amassed a large volume of data showing that the language network in our brains is
*  distinct from our other cognition-related networks.
*  Ev argues that this and other data indicate that language is not for complex thinking,
*  as people like Noam Chomsky have argued, but instead language is for efficient communication.
*  So I brought Emily and Ev together to discuss these and other topics, and I really enjoyed
*  our discussion.
*  I recommend you dive deeper into their works, which I link to in the show notes at braininspired.co
*  slash podcast slash 144.
*  On the website, you can also learn how to support this podcast through Patreon if you
*  find it of value and or check out a free short video series I made called Open Questions
*  in AI and Neuroscience.
*  Sadly, my video during this recording was so out of sync with my audio that it was beyond
*  So rather than frustrate you like it frustrated me, I've simply removed my video and include
*  only my voice.
*  Apologies for that weirdness.
*  Nonetheless, you still get to hear and see these excellent people, Emily Bender and Ev
*  Fedorenko.
*  Enjoy.
*  Ev, Emily, thanks for being on the podcast and welcome.
*  Emily, have you had a chance to look at my logo for Brain Inspired?
*  No, I haven't.
*  Okay, because I think that you would hate it.
*  Go look it up.
*  Yeah, go look it up.
*  Go to braininspired.co.
*  I think that you would really hate my logo based on previous things that you've discussed.
*  Yeah, so this is a logo that is definitely leaning into the computational metaphors,
*  shall we say.
*  Yes, definitely.
*  Definitely.
*  Okay.
*  Just wanted to get that out of the way.
*  So roughly, where do you guys situate language among our cognitive abilities?
*  Is language the pinnacle of our cognition?
*  As individuals, we can get into social aspects of it later, but just as a cognitive entity,
*  where is language?
*  Maybe we can start with you, Ev.
*  Sure.
*  Well, the thing to keep in mind is that I'm a cognitive scientist and I use neuroscience
*  tools to study cognitive science, so my perspective is tainted by the knowledge I have from that
*  domain.
*  Tainted.
*  And so, well, or the positive version of that.
*  In my work, I've been very interested in the relationship between language and thought
*  or complex reasoning abilities.
*  My initial prior was that language is at the very core of those abilities, and I was very
*  sympathetic to that kind of a view, but it turns out that empirically, the way that humans
*  are built, language rather reflects some of the complexities that we have in our thoughts
*  rather than creating them.
*  So in a sense, I would take the evidence to date as suggesting that language is just kind
*  of one tool in our cognitive toolkit, and a lot of complex thought can happen without
*  access to language.
*  Emily, do you agree with that?
*  Well, so I want to say, you know, on things cognitive science and neuroscience, I definitely
*  defer to Ev.
*  My work is in linguistics and computational linguistics, and so I have no basis on which
*  to compare language to other cognitive abilities.
*  I think that what I can say as a linguist is that language is an interface that allows
*  us to work together with other people and also to work with ourselves across time.
*  And my guess is that that will have lots of really interesting cognitive implications,
*  but that's not really answering the question of how does it fit into some hierarchy of
*  cognitive abilities, because I don't have an answer to that question.
*  But can't you do some armchair philosophy, which is where we got us to the place pre-Ev,
*  where we sort of assume that language is the pinnacle, and according to your prior as well.
*  Is that an area, Ev, where philosophy has led us astray, perhaps?
*  I think so.
*  I think philosophy has led the field astray many, many times, and I think it's because
*  relying on introspection is dangerous.
*  We have intuitions, and intuitions can be helpful for generating hypotheses, but ultimately
*  you can't build stories on that as just a starting point.
*  And because some of the tools for studying the relationship among different cognitive
*  abilities just haven't been around, you know, well, different tools became available at
*  different times, but without those tools we just couldn't empirically ask these questions.
*  And because, I think because some people have this intuition that they talk to themselves
*  when they think, I think that has led to this whole notion of language as being kind of
*  the core essence of thought and the inability to think without language being there.
*  And that just seems to be empirically, just doesn't seem to be true.
*  What about the people who vocally talk to themselves all the time, who vocalize their
*  thoughts, right?
*  And can't seem to think without doing so.
*  That's my daughter and my husband.
*  Well, it depends on what you mean by not able to do, to think without doing so.
*  That's again an empirical question, seemingly, right.
*  I think some of that has to do with humans being highly social, although I think some
*  people like that even do it when they're alone.
*  Again, I'm not saying that language can't be helpful in structuring certain thoughts
*  or maybe extending the kind of window over which we operate in our thought mental space.
*  But like I said, the evidence that we have from both brain imaging and individuals with
*  severe language problems suggest that a lot of stuff can happen.
*  Very complex reasoning can happen without relying on linguistic representations.
*  I think I'm also-
*  Oh, go ahead, go ahead, Emily.
*  I'm detecting in your questions some implicit hierarchy of kinds of thought and kinds of
*  reasoning.
*  So when you say people who can't think without speaking, that suggests that there's certain
*  kinds of the more general thing that we call thinking that you consider sort of real thinking
*  and other stuff that isn't and a value proposition where some of it is the stuff that we tend
*  to do through language.
*  So I'm thinking about the experience of when I go to write something and I'm out for a
*  walk and I have a really great idea and then I sit down to write it and it feels like,
*  oh, I actually had sort of the first, second and sixth parts of this and the stuff in between,
*  I really have to sit down and work out.
*  And as Ev says, if I set it down in language and sort of fix it there, then I can focus
*  on those other connections in between and that can extend what I want to do.
*  But I would not want to call that kind of work real thinking to the exclusion of other
*  things.
*  I mean, do you think that people conflate thinking with language and just that they're
*  the same thing?
*  You know, there's the language of thought, hypothesis of our cognition, et cetera.
*  I mean, do you think that's one of the mistakes that people make is just conflating our thoughts
*  with language?
*  I have a story for you from when I was in college.
*  My mom came to visit once and I was really proud to show her what I was doing and I brought
*  her along to a syntax class I was taking.
*  And my mom's a poet and a personal essayist and a teacher of creative writing, so she's
*  really a language person but in a different way.
*  And she walked out of that class terrified because she said, you are using language to
*  study language, you're going to go crazy.
*  And I think that we're fine, right?
*  Syntacticians actually do manage to hold it together.
*  It's okay.
*  But I do think that there's a danger that because so much of this discourse is done
*  in language and especially in written language that we conflate that with the thing that
*  we're studying and sort of analogously there's all this stuff going on which maybe we'll
*  get into later in the hour about whether or not language models are sentient.
*  Do we have to?
*  Okay.
*  I hope not.
*  The thing that I wanted to bring out of that is people who are taken in by the language
*  models seem to project an inner life onto the language model.
*  And some of that discourse is around, well, see, it's doing language, so therefore it
*  must have an inner life.
*  And my reaction to that is language is one of the key ways in which we become aware of
*  the inner lives of other people.
*  But that doesn't mean that the language itself is the inner life.
*  That's exactly right.
*  I completely agree with this.
*  I think it's not unreasonable.
*  We're a Bayesian reasoning beings, right?
*  And it's not crazy to think that something that produces coherent well-formed language
*  has thoughts because in most of our experiences that's the case.
*  But of course it's a fallacy.
*  Of course we've learned that you can learn a lot of rich statistical patterns of how
*  words go together, including pretty sophisticated aspects of syntax that some syntacticians
*  had argued you just can't learn from experience no matter how much experience you have.
*  That does not imply that there is complex thought there.
*  I mean, one way to also think about it is, for example, humans vary a lot in their reasoning
*  capacities.
*  And oftentimes you have people who speak very eloquently or fluidly and fluently, but it
*  doesn't necessarily mean that there's a lot of kind of rich complex thought behind.
*  We've seen it in politics a lot in the last much years.
*  I meant to ask you this upfront, and this is a total aside, so I apologize.
*  Do you enjoy courting controversy and getting pushback?
*  Because one thing that you kind of share is, so Ev has spent a lot of time collecting evidence
*  for and arguing against the idea that language is necessary for complex thought.
*  So this goes against a lot of intuitions and background philosophy.
*  And of course, Emily, you're writing these critical papers on language models ethically
*  and the fact that they don't understand what they're producing.
*  So I assume that you guys both get a lot of pushback.
*  Is that enjoyable to you?
*  Not particularly.
*  No.
*  I'm not in it for the pushback, that's for sure.
*  Yeah, same.
*  I'm just doing my thing.
*  I want to figure out how things work.
*  I'm an empiricist, and so I'm just trying to understand how the system works.
*  And I'm happy to argue with people, but I think a lot of the pushback comes, it's not
*  incidental that we're females.
*  Like that has...
*  Oh yeah.
*  Really?
*  Yeah, you seem surprised.
*  Yes.
*  I just don't, I don't think I want to believe that, but yeah.
*  Oh, well, you may want to believe, I want to believe all sorts of good things too, but
*  my most salient kind of awareness of these differences came from traveling back when
*  I was like a postdoc or young faculty with my husband, who is also a language researcher.
*  And we would often go and give talks together, you know, sequentially, because if we're both
*  there people would want to hear different anyway.
*  And he was just amazed at how different the tone is of people who talk to me compared
*  to the way that they talk to him.
*  And I just kind of hadn't really given it much thought before.
*  Of course, I'm also raised by a female academic, Nancy Kamwisher, and she was always warning
*  me about this.
*  And yeah, there's definitely a lot of expectation of, you know, like we owe people something
*  to explain to them every little thing without them bothering to even read the papers.
*  And you know, we don't.
*  And you know, I sometimes look wistfully at the other kind of work that I do and wish
*  I had more time for it.
*  So, you know, multilingual grammar engineering and computational semantics.
*  And I find myself putting more and more time into this discourse around what is it that
*  language models can do because I see the hype and the over claims as harmful.
*  And some folks are concerned with sort of the harm to the field of AI.
*  And I frankly couldn't care less.
*  Like AI is not my problem.
*  I'm not trying to build better AI.
*  If I think computer science as a whole and AI in particular is vastly overfunded right
*  now to the detriment of the science in that area and to the detriment of the science in
*  surrounding fields.
*  But I see I see harms to people, right, in terms of when we believe false things about
*  what these systems are doing, then we end up putting too much faith and too much autonomy
*  into automated systems.
*  And so I'm not doing it for the pushback, but I sort of feel like this is a place where
*  my knowledge and expertise in linguistics allows me to do some good in the world.
*  And so that's my motivation.
*  So we could really go off the rails here ethically.
*  And it's not an ethics podcast, but maybe let's get back to what I was going to ask
*  about regarding the meaning and our as humans that we sort of grasp for meaning and
*  anthropomorphize and want to think that we are communicating with something sentient,
*  something that is producing meaning.
*  And is that because we so there's this kind of approach, the computer metaphor of the
*  brain, right, is that we get input signals, we process that input, and then we produce
*  actions.
*  And then there's this alternative viewpoint that really we're producing actions primarily
*  to receive different inputs, right.
*  So instead of a perception to action notion, it's an action to perception notion.
*  And I'm wondering if it's the same if we buy into the action to perception notion,
*  I'm wondering if our grasping for meaning in other humans, our cats and dogs, large
*  language models, if that is the same sort of thing where we're so we yearn for meaning
*  so much and we build meaning out of things so much if that is sort of an analog of the
*  taking action aspect.
*  Does that make sense?
*  I'm just saying like we're like actively filling in the gaps when there are real gaps.
*  I mean, we're certainly very good at filling in cognitively, right, like we have a rich
*  understanding of the world.
*  And if something is not there, we can easily fill it in by assigning mental states and
*  so on.
*  And again, because it's because I think that a big fallacy is that we often can and do
*  what in fact it's necessary to assign mental states to entities that produce coherent
*  language, which is other humans, and to understand what somebody is saying to us, it's
*  really critical to think about their intentions and the whole context in which they're saying
*  something.
*  But it seems and it seems really hard for people to get that you can just learn the
*  regularities of language and produce language and not have all of the stuff that usually
*  comes along with language as part of the human brain.
*  Now, I think there is kind of an interesting flip side of this.
*  Now, I think there is kind of an interesting flip side of that, which is how much of this
*  richness can you infer from patterns in language?
*  Because of course, language reflects this generative process of thinking and we talk
*  about things we think about and feel and so on.
*  And that's an interesting question.
*  Different fields have different kind of takes and approaches to thinking about this.
*  There is obviously a lot of information about the world that's reflected in language.
*  But as a lot of work suggests, some of that knowledge seems quite brittle, not always
*  generalizable in the same ways as what humans have.
*  And presumably it's because along with the linguistic regularities, humans get access
*  to the physical world.
*  They interact with other entities using that same communication code as well as with the
*  objects and engage in the events.
*  And so it's a richer notion of meaning that they get.
*  But I think you can get quite a lot from just the way that words go together.
*  That definitely has a lot of structure.
*  I think to go back to your question of is our looking for meaning analogous to taking
*  an action so that we get a percept back?
*  So this is, I feel out of my depth.
*  Again, I want to defer to Ev when it's questions of what's going on.
*  Come on, you have to.
*  So my sense is that looking at language and how it's used, so linguistic pragmatics and
*  also what we know from the child language aquatists in literature, we are very, very
*  good at taking in linguistic clues together with everything else we have and then using
*  that to make inferences about the communicative intent of the person who uttered the thing.
*  And we do it so quickly and so automatically, including all these processes of, for example,
*  ambiguity resolution.
*  So computers are very, very good at finding multiple different syntactic analyses of a
*  string if you're actually running a parser that's got a grammar in it.
*  My favorite example is have that report on my desk by Friday.
*  Seems like a completely straightforward, unambiguous thing.
*  Any scenario that you can imagine for that sentence, no one's going to say, but wait,
*  what did she mean?
*  32 different parses for that, given a reasonable grammar of English.
*  Because have could be cause to be, or it could be go ahead and take.
*  The report could be about the desk or it could be physically on the desk.
*  By Friday could refer to a time or it could refer to the author of the report.
*  And then all those things can combine together in different ways so that you get 32 different
*  readings.
*  But none of that, like it just, it goes right past us because we are using so much information,
*  sort of general world knowledge, cultural knowledge, what we know about the person who
*  said the thing.
*  And linguists sometimes get tripped up when we are asking speakers for grammaticality
*  judgments because we forget how much of that world building goes into creating that judgment.
*  And so you'll get people saying, oh, no, no, no, nobody would ever say that because we haven't
*  sort of given the time to say, okay, no, in this kind of a situation where these things
*  are going on and you need to emphasize that now is it a natural thing to say?
*  And we sort of work with this false assumption of a null context, which just never exists.
*  So all that to say that our interpretation of language is very fast and very reflexive.
*  And we have the sensation or the intuition that we are getting all that information out of the
*  language when in fact what we're doing is we are pairing a whole bunch of information with
*  the language to make some inferences.
*  But I'm tempted to just go down the road of the of Ev's work comparing large language models with
*  the predictive activity of that with our brains.
*  But maybe before that, what does that say about large language models?
*  Are they not producing language the way we think of language?
*  Because we need a different definition of what they're doing or a different word for
*  what they're doing than language.
*  So I think we often the discourse often does get tripped up because language could be the
*  set of forms or it could be the form meaning pairing or it could be the linguistic system
*  that puts those things together.
*  And so I've started talking about large language models as text synthesizing machines,
*  which still isn't great because a text, especially if you're talking about like,
*  you know, humanistic scholarship, a text also is something that's got a lot of meaning in it.
*  But the point is that what the large language models are doing is coming out with strings.
*  And those strings are conditioned on very carefully modeled understandings and ways that
*  work very carefully constructed models of the patterns of the strings.
*  And embedded in those models is a lot of information about which strings are like each other and which
*  ones tend to co-occur and constraints that look like syntax and constraints that look like lexical
*  semantics. But none of it reflects any communicative intent, nor any connection to
*  the world outside the strings. So no grounding, no social understanding, and so on.
*  And yet, one of the things that Ev has shown with her group is that when you compare the activity
*  of large language models with that of brains, there seems to be this next word prediction
*  that's happening in our brains as well, as it does in the large language models. And this is
*  kind of in the tradition now of the visual system in our brains have been compared to the
*  convolutional neural networks. And we've talked a lot about that on the podcast.
*  But Ev, what does that mean? Are we just missing? Are we just grasping that one
*  tiny aspect of language, next word prediction? And so we need to find the other aspects,
*  the grounding, the context. What does it mean? Yes, that's a great question. So yes, that's
*  exactly how I think about it, except I don't think that prediction is a tiny part. So we have a set of
*  regions in our brain that respond very selectively to language. And my group and other groups have
*  previously shown that these responses are sensitive to how predictable upcoming words are. So there's
*  extra cost if words are unexpected. And that has been shown behaviorally as well in many different
*  paradigms. So there's the system. And as you pointed out, it indeed seems to be the case that
*  if you take representations from modern language models, like the transformer architecture models,
*  and you build a model, a linear mapping model between those representations and the neural
*  representations extracted from that system, this language selective system in the human brain,
*  there is a good relationship. You can learn a relationship so that you can then predict
*  neural responses to some unseen stimuli. And I think it's really intriguing. And it was very
*  surprising to me how well that worked. But it also kind of in my kind of thinking about language and
*  cognition, it came around the time where all of this stuff about separability of language and
*  complex reasoning was becoming clearer and clearer. And then if you think about it through that lens,
*  then perhaps it's not so surprising that we have this system that is a system that has some,
*  that has learned some mappings between forms and some rough approximation of meaning that could then
*  be passed down to systems that actually do complex reasoning on those representations,
*  be it social reasoning or abstract reasoning like in logic and math and whatever else.
*  And so yeah, I think looking at neural responses in this language system is capturing this one
*  aspect of linguistic regularities, which of course, but the reason that I don't think it's a tiny part
*  of language is of course to succeed at predicting the next word, you have to learn to pay attention
*  to all sorts of stuff in the signal, right? To how particular words go together, to some more
*  abstract syntactic patterns and learning all that as a kid is a non-trivial task. Learning that as a
*  model is a non-trivial task. But, and of course, you know, models and kids learn differently.
*  Presumably, I think there's a lot of interesting work to do to try to figure out how those
*  differences may impact resulting representations and so on. But that said, it seems like we have
*  this machine in our brain that does that, stores all of these knowledge representations that we
*  acquire over our lifetime and that uses them to predict upcoming, like how linguistic signals
*  unfold, which is presumably we do because it's facilitates, it basically spreads workload over
*  time better. So we don't have to work as hard when things actually happen. So that's kind of a brief
*  take on that. Emily, does that sit well with you that a huge part of our language faculty is
*  next word prediction or just predicting upcoming words? So I, first of all, again, you know,
*  defer to the empirical work, right? So, you know, my work on language looks at the level of, you know,
*  what can we say about the system? How can we model grammaticality judgments? And I like to think that
*  that kind of work digging into syntax can then help inform the kind of studies
*  that Ev and her team and other researchers are doing. So, but in terms of, you know,
*  what are we finding that the brain is doing? It doesn't matter what I want, right? It matters,
*  you know, is there good empirical work going on? But also, I think that there's a difference between
*  saying, yes, humans have, you know, this facility where we predict what's coming next. And, you know,
*  I appreciate the explanation of that allows us to smooth out the workload by sort of trying to do
*  some of that computation ahead of time, it sounds like. That is very different to saying, and so,
*  therefore, a system trained with the task of doing next word prediction is getting at the heart of
*  language, right? Is getting and therefore, you know, understands what things mean, etc., etc. So
*  it's interesting. And I think it's an interesting way to use the large language models, although with
*  the huge caveat that the nature and scale of the training data is so different between, you know,
*  what something like, you know, even BERT is exposed to and what a human child is exposed to. So like
*  that, the analogy there, I think, breaks down a little bit. But using the language models to sort
*  of model that aspect of what humans do with language is interesting for sure. And I noticed,
*  as Ev was talking, that she was being very careful to reserve the word neural for things happening in
*  actual brains. So while we're talking about, can we have a different word, please? And it would be
*  nice to reserve neural for things that are actually neural rather than metaphorically neural.
*  That idea has flown. It's, I think that there's no going back. Is there? Is there, Ev? There's
*  no going back, right? I don't know. I don't know. I mean, like, as long as people define their terms,
*  yeah, I think terminology is very hard to change. I've fought some of those battles and
*  I usually tend to give up eventually. I'll just keep using them the way that they make sense to me
*  and ask that other people define what they're talking about. But yeah. Yeah. But I think, like,
*  I mean, one other thing to say about this, potentially, like at least some similarity
*  between the representations and the models and the human neural responses is that it's for the
*  first time, and like I always say this, I did not think this would happen in our lifetime. It's for
*  the first time that I think we can go beyond kind of these verbal descriptive hypotheses about how
*  things happen and maybe have like an actual implemented model of at least some aspects of
*  how language might work. It's not, of course, finding a similarity between two sets of
*  representations doesn't mean that they are doing things in the same way, but it's a window, right?
*  It could allow you then to try to manipulate the model architectures, the training objectives,
*  the training, the learning algorithms, and try to see which of these things affect how well those
*  representations, resulting representations can capture human neural responses. And I think we
*  can learn a lot through that kind of careful experimentation on the models now, just because
*  as in of itself, the fact that some big set of parameters provide some fit to human neural data,
*  that's not the end point. Again, I see this as a potential window to actually get beyond saying,
*  like, oh, this bit of the brain does syntax or whatever the field has been doing for the last
*  few decades. Emily was mentioning that the language models learn differently. They learn from different
*  data and presumably different than humans learn. Does it matter how we learn language? So, Ev,
*  I know that you're multilingual from a young age, right? I was multilingual before I came to the US,
*  but yeah, I mean, I'm still kind of bilingual. I guess Russian is my native language, yeah,
*  but I used to speak a few others that I forgot. Here's another aside before we continue, because
*  I want to get this right. Is it true, Ev, that fMRI studies have shown that people who learn
*  multiple languages from a young age, when you, when they're processing and producing those
*  different languages, the representations are more clustered and overlapping than people who learn
*  language at a later age where their native language is like, there's this kind of a central cluster,
*  and then the newly learned languages are more active kind of outside that cluster?
*  We don't see that. Basically, it seems like once you have good proficiency in a language, it all
*  loads on the same set of frontal temporal regions. Now, of course, different languages have to be
*  segregated within that system, otherwise we'll be confused all the time, right? So, it's some fine-grained
*  level of multivariate responses. You can discriminate, you know, French from English or
*  whatever when you're producing it or understanding it, but if you achieve good proficiency in a
*  language, it will all be in that same system for you, even if you learned it later in life.
*  So, thinking about how to, okay, the difference between language and complex thoughts, and there's
*  an interface, right? So, whatever language you're using needs to be passed on to your working memory
*  system or your reasoning abilities and vice versa to produce the language. Is fMRI going to allow us
*  to see that interface, that exchange, because it seems like that interface is perhaps one of the
*  more important things to understand how we utilize language? Yeah, it's a great question. I mean,
*  so, like, one, first the clarification. So, like, when you say there's, like, working memory
*  computations that you need to hold some chunks of language as you're producing whatever, all of that.
*  So, okay, one step back. People used to think that we have a set of language brain areas that do some
*  aspects of language, and then we have some perhaps central hubs, like, for example, working memory,
*  into, like, working memory integration, information integration hub, prediction hub,
*  and then different domains implemented in different parts of the brain all draw on these
*  centralized hubs. Now, it doesn't seem any more like that's how things work. So, the kinds of
*  computations that support language processing, which includes prediction, but also things like
*  integration, as many theories of synthetic complexity have postulated for many years,
*  all the working memory based stories, it's kind of the opposite, the flip side of prediction,
*  right? So, there's a cost in thinking of what might come next, but then there's also a cost
*  in integrating elements into the representation you're building. Anyway, but all of these
*  representations seem to be implemented fokally within this language specialized system,
*  and I think the same is likely true for other domains like music and things like that. But
*  whether we can study the interface between language and actual kind of thinking and reasoning
*  capacities, I am dying to understand how that works. I think that's the most intriguing thing
*  to tackle next, and we're trying to do some of this, like, what are the representations that
*  the language system passes down to these areas that then, for example, reason about, you know,
*  social relationships among people or physical constraints in the world or whatever other,
*  you know, abstract logical kind of connections between things. And we don't have great tools
*  for studying those kinds of questions. For different tools that are available have
*  limitations, but I think we're trying to figure out if we can get really clever with
*  tools like fMRI, which is you kind of need whole brain coverage because you want to be recording
*  from multiple systems at once, and most intracranial recordings, which you can do in humans,
*  have the limit of very, very sparsely sampling the brain. And it's very rare that you would
*  have recordings from the language system and from some downstream, for example, abstract reasoning
*  set of areas. And so we're trying to see how far we can push fMRI to get at this,
*  and I don't know yet. I feel like in the next decade we'll have a better sense.
*  Well, I know one of the things, Ev, that you advocate for is studying animal communication
*  as a proxy for studying language in humans. And, Emily, I don't know how familiar you are with
*  lots of animal cognition and communication, but I guess the question would be, can we really do that?
*  I thought language was something special about humans and that other animals,
*  be they non-human primates down to organisms like bacteria, can communicate, but there's a
*  clear distinction between language and other animal communication. Is language specific to humans?
*  And, you know, is it a viable, do you think, Emily, it's a viable option to study communication
*  in non-human animals to understand something about human language?
*  So I think if we're going to go to communication in non-human animals, we are adding a layer of
*  complexity, but also giving ourselves some distance that might be helpful. So if you look at,
*  say, you know, dolphins or whales, where we don't really know what's going on, there seems to be
*  some interesting complexity there. They certainly, you know, whales. So I'm thinking here in
*  Washington state, we have the Southern Resident Orcas who are severely endangered and every year
*  there's news reports about, you know, the new births in J-Pod and K-Pod. And it's, you know,
*  there's a specific set of individuals and they are in specific groups. And so I think that,
*  you know, someone studying that may well have evidence that there's social structure and
*  communication. And so that gives us some distance. Of course, there's the extra
*  distance of environmental differences. It's like difficult to study marine mammals because
*  they don't share their environment. But we also then are working with something where we don't
*  know the code, right? We don't really know what's in their communication system. And so that's both
*  sort of a further difficulty and some possibly beneficial distance that might help depending on
*  what kind of question you're looking at. As to the question of whether language is special to humans,
*  there's some pretty foundational work by Charles Hockett looking at design features of language to
*  say, what does something have to be before we call it a language? And whenever you're doing that kind
*  of definitional work, I think it's worth keeping an eye on why you're doing the definitional work.
*  So if we're saying, this is what linguistic studies, linguistic studies languages, so things
*  that have these properties are languages and they are in scope, that's just descriptive.
*  If you're saying humans are better than animals because we have language or humans are more
*  sophisticated or more something, then it's a more value-laden different kind of a question.
*  So I think that it's worthwhile to define our terms, as we were saying before, and talk about
*  what is this thing that we're calling language, what are the properties that we care about,
*  and why do we care about them? And if we're looking at it from a neuroscience perspective,
*  it could be, well, we care about how the system works in a human brain. And if we want to look
*  to animal models, then we need to establish that it is analogous enough. And so that's
*  what we're creating the properties. Are you on board with that?
*  Yeah, I just maybe like to add. Yeah, yeah, I think largely very much so. I mean, I think one
*  important thing that I always say is that, you know, there's a lot of continuity in biology,
*  and I just oppose about people making categorical transitions when there's no evidence for such
*  transitions. So I would be very surprised if our system is in some qualitative way different.
*  And I think that desire to postulate a qualitative difference comes from,
*  historically, the focus on syntax, which is a big component of language, but words are also important.
*  And humans, unlike many other animals, can store a vast number of communicative signals.
*  And I think that's not to be underestimated. I think that's similarly important. Once you
*  start thinking about word meanings and the complexity of communicative signals, then it
*  becomes much more likely to be a continuum as opposed to some fundamental new circuit that
*  we have evolved or some new brain region, some new way to process information for which, you know,
*  that may well be true. But so far, evidence for homologies is overwhelming and evidence for,
*  like, fundamentally new kinds of computations that human brains can do that other animals
*  can do is quite sparse. But there's a lot of exciting work both in terms of, like, understanding
*  the actual biology of human neurons compared to other neurons, and there's some interesting
*  differences. So I'm excited about the kinds of things we can learn about those potential differences
*  again in the coming years. So you don't see a qualitative difference between, okay, so someone
*  like Terrence Deacon would argue that there's a qualitative difference between the symbol-like
*  structures that humans use for language and that constitutes language versus what he would call
*  indexical and other kinds of referential signals that are used in the animal kingdom. Whether or
*  not there's different neural architecture underlying it, you don't buy that. There's not a
*  qualitative difference between the ability to use symbols that essentially wear a symbolic species
*  and can pass these things down. I can write the word tangerine and you can understand it in four
*  years, right? And that it's somehow detached from the immediacy of the environment.
*  So you don't buy that there's a qualitative difference? Well, I mean,
*  qualitative difference is called for very strong evidence, and there is a very, very large field
*  of animal communication that has shown that many features of human communication are also present.
*  And yes, they don't have writing systems, okay. So it's harder to pass things down across many
*  generations, but animals communicate about things that are not. If you look at different species,
*  you find evidence of communication about things that are not here and now necessarily. And again,
*  like one thing that I think is important that often gets kind of all locked together is yes,
*  humans are smarter and humans have language. It doesn't mean that humans are smarter because they
*  have language. And in both of these things, kind of the communication system we have and the thinking
*  capacity we have, there may well be continuity as opposed to some fundamentally kind of different
*  processes happening. But I think understanding in which ways we're smarter, setting language aside,
*  can also be a very fruitful thing to try to crystallize some of these differences without
*  bringing language into the bucket, which sometimes just leads to muddled reasoning, because it's very
*  hard for us to think about thought without using language. And then it just all gets lumped together
*  and leads to like a lot of mess in the literature. Okay guys, so let's talk about large language
*  models a little bit more. Okay, so Emily, this is not a knock against linguistics or anything, but
*  one question is do we understand language well enough to build, you know, useful large language
*  models? Do we need to understand language? And I know a lot of what you do is apply your linguistic
*  knowledge to kind of critically evaluate large language models, but do we understand language
*  enough and do we need to understand it enough? So yes, I think that we do need to understand
*  language in order to build good language technology. It's not clear to me that large
*  language models are something that the world needs at all, certainly not larger and larger ones.
*  That's not a phenomenon in the world that, you know, a mountain that we climbed because it was
*  there kind of a thing. We created the mountain as we were climbing it and without, I think,
*  a whole lot of purpose in mind aside from some very fuzzy thinking about AGI, which I think is
*  way off the rails. In terms of building good language technology, yes, I mean we definitely
*  need to look into what we know about language and the more we know about language, the better we can
*  build the language technology. And this includes things like if we want to build language technology
*  that works well across different languages, then looking into linguistic typology, which is the
*  study of how languages are similar and different, can help us do that better. If we want to build
*  language technology that is well situated within its deployment context and not discriminating
*  against people because they speak differently or reproducing the discrimination that's in language,
*  then sociolinguistics is a really rich and useful starting point, right? And I'm not saying that
*  typology or sociolinguistics are, you know, finished areas of study. Is there anything that's a
*  finished area of study? I think the areas of study that we've abandoned are all things where it turned
*  out to be, you know, pseudoscience and anything that had something real at its core, there's
*  always more to do, right? So yes, we could always learn more about language, but what we are not as
*  a field doing in NLP is getting the full advantage of what is known from linguistics. And there's,
*  it's a little bit frustrating to me because sometimes people will write off linguistics
*  because they took one formal syntax class, and by formal I mean formalist, I mean like minimalist
*  program, and said, oh, this isn't useful, and then decided that that was all of linguistics.
*  And that's partially on linguistics because within the field, especially in the US, there's this
*  culture of sort of putting syntax, especially that kind of syntax on the top of the heap, and sort of
*  putting that forward as the pinnacle of linguistics. And so if we do that and people from the outside
*  come and look at what we've done and go, well, not useful, and miss all of the other stuff,
*  we could be doing better on the linguistic side. But I also, you know, will continue telling the
*  language technology people to please keep paying attention to what you can get out of linguistics.
*  And do they? Is there a lot of hesitancy to listen to linguists?
*  Yes. And I think that hesitancy comes from a couple of places. So one is sometimes people do
*  go and they encounter something that is esoteric and not helpful. And I've tried to work against
*  that by writing a couple of books saying, here's 100 quick vignettes about the first one was
*  morphology and syntax, and the second one was semantics and pragmatics. And those came initially
*  out of frustration as a reviewer for NLP conferences around 2010, 2011, going, my God, these people
*  don't know the first thing about how language works. Right. So, okay, well, it's not reasonable
*  to ask people to go do a whole second degree. So what can I do? Well, here's 100 things about how
*  language works. And then I did 100 more. But also, I think that there's something cultural
*  in computer science, which is to say, especially machine learning, the whole point is to build the
*  system that learn the things so you don't have to. And that leads to a direct devaluing of domain
*  knowledge. And linguistics is one important domain for domain knowledge for NLP that gets
*  devalued and ignored. And so I've put a lot of effort into trying to counteract that.
*  What do you think language models need? What would you want to see in, besides scaling up?
*  I mean, I know it's a problem modeling. I don't know. I never said they need to be scaled up.
*  No, no, no, no. I don't think that's necessarily a good strategy. But yeah.
*  No, I mean, that would be the, that's sort of the default program, right, is to scale up.
*  But even, you know, looking at comparing our visual activity to convolutional neural networks,
*  the larger ones don't perform as well because they're not mapped on as well to the structure
*  of our brain. So I'm just saying that, you know, scaling up is not good for neuroscience. Like,
*  it's not going to buy you anything. But is it, you know, is there something that would?
*  You think Emily could help you? I think so. I mean, I think we have a good system, a good
*  general intelligence system that still a lot remains to be understood about, which is the
*  primate brain. And I think when people started seeing some of the successes of the language
*  models, again, conflating all sorts of being able to capture linguistic regularities versus
*  abstract, generalizable world knowledge, then, well, it also depends on the goals, right? Like,
*  if you want to build a system that can solve problems for you, then sure, maybe scaling it
*  up and seeing how far you can push it is a reasonable thing to do, although, of course,
*  it's not environmentally responsible and comes with a lot of its own issues. But if you want to
*  build a system that can think, then it just seems a little bit misguided, potentially, to just try
*  to think that language will just give you that. And again, I think the idea that it can comes
*  from the fact that a lot of people think that language is what made us smart. And we have a
*  very nice, somewhat modular, and I'm not bringing any of like, fedorian baggage where nothing,
*  like some things are encapsulated or anything like that. But it does seem there is division of
*  labor in our brain, and presumably it's because it's metabolic and computationally efficient to
*  build a system like that. And so perhaps instead of trying to make the language models larger and
*  larger and train them on more and more data, you can take existing models, which actually do language
*  really quite well. In many ways, they capture many regularities really pretty well. And you can use
*  linguistic tools like Emma was saying to probe the knowledge that they see, the way they represent
*  language is similar to how humans represent linguistic regularities. But I think we have a
*  working, decent language module-ish, and then we can try to see, okay, how would we build a system
*  that reasons about different aspects of the world? How to build a system that does math,
*  build a system that can interact with computers using computer code, a system that implements
*  social reasoning. So this is kind of going to this notion of having a bunch of distinct capacities.
*  Some of them are relevant to particular domains. Some of them are abstract reasoning capacities,
*  like the kinds of things that are linked to fluid intelligence, just abstract reasoning,
*  novel problem solving, and so on. And then maybe try to combine those different solutions together
*  and try to build interfaces. And maybe that's a better way to try to build a general intelligence
*  system. And maybe it can be much more computationally efficient than trying to get some of this,
*  again, like some of this you may be able to get through language, but it's just not necessarily
*  the best way to design a system, I think, given what we know from human brains.
*  So I think we've maybe found a point of disagreement finally, F, which is I don't think
*  the language models are a nice language module in a system like that, because I think that they
*  capture some things about language, but they don't capture enough. And so that's one point
*  of disagreement. And the other point, maybe this isn't disagreement with you, but disagreement with
*  others that you were sort of modeling as you were speaking, is I don't see the value of building a
*  general intelligence. I think that we would be much better served by building specific tools to
*  help people do things. And there are lots of places where building language processing tools
*  could be extremely useful. Some of my favorite examples are matching patients to clinical trials,
*  helping comb through case law to find precedent. Automatic transcription is wildly useful. Likewise,
*  machine translation. So thinking about it as here are tools rather than running away with,
*  okay, now we've got a language thingy. Let's build a general intelligence around that and then have
*  it be a general purpose tool. I think we're going to have a real hard time creating something that's
*  fit for purpose if we go that direction. That's a great point. Yeah, that's a great point. I mean,
*  again, I'm not an engineer. I don't need to build tools. I see how some tools can be useful. But
*  for me, building something like a generalized intelligence system is another tool for probing
*  the human brain. Like if we can build something taking inspiration from the human brain, then
*  maybe we can ask questions that we just can't ask about how human brains work because we lack the
*  tools. But if we have a model that captures something about human neural responses, then we
*  can try to understand, for example, how the language system passes information down to,
*  say, the abstract logical reasoning engine or social engine. And I have no objections to
*  building scientific models. But most of the people who are talking about building these things are
*  not doing it with that kind of a motivation. That's true. That's true. Well, we at MIT do.
*  Not only at MIT, of course, but a lot of people who interact with are, of course, interested in
*  fundamentally this interaction between the fields with a big goal of understanding how humans work.
*  I want to live in your world.
*  I'm coming over.
*  Yeah, right. Going maybe the other direction, instead of using language models
*  as proxies for brain activity, are large language models teaching us anything about language?
*  So linguistics can inform large language models. But are we getting anything in return, whether
*  it's our limitations or what we're particularly good at that they're not? Are we learning anything
*  about our own cognition through these language models? I'd be very curious to hear what Emily
*  thinks about that. So I think there are linguistic questions around it. And I've mentioned this
*  earlier around what can be learned from, the phrase you used was experience. And there are
*  linguists who want to posit innate knowledge of language and posit it on the basis of saying,
*  see, people know these patterns that they can't possibly have learned just from observing the
*  data. And I guess there's a couple of things I want to say about that. The first is that
*  our experience with language is very, very different from the input that a language model
*  is getting about language. Because our experience with language is always embedded in a physical
*  and social experience. And even if part of what we're doing is learning to predict the next word,
*  it's not that we're just sitting there receiving strings of words,
*  which is roughly what the language model gets to do. So that's sort of one direction.
*  It is interesting, I think, to say, hey, look, these patterns of grammaticality that
*  you were using to posit innate knowledge of language actually are calculable just from data
*  if you have enough data. And then I suppose if you want to get into the degree of that argument,
*  it becomes, okay, well, what's an appropriate amount of data? How much do you need before you
*  say this is something that a child learning a language could reasonably have been expected
*  to be exposed to? So I think that there's questions in that direction that are interesting.
*  I mean, I'm certainly for using computational models to do linguistics. That's what I'm doing
*  with grammar engineering. It's a different approach. It's basically saying, let's actually
*  push the rule-based idea. But instead of having those rules be pen and paper, let's actually write
*  them down on a computer so we can then test them over large data sets and find the phenomena that
*  our rules don't yet account for. And that allows us to move on to the next thing, the next thing.
*  And sort of in that same spirit, I could imagine using a large language model. I wouldn't build it
*  for this purpose. But given that they exist already and it doesn't take very much more
*  electricity to run them a little bit or to probe them, it could be interesting to say, okay,
*  what are the things that can be picked up in this paradigm versus can't? And so I'm thinking of the
*  work of people like Alison Edinger and Ellie Pavlik who do really interesting work on sort of
*  probing and trying to understand what kinds of things can be picked up from this observation of
*  lots and lots of linguistic form versus what seems to require more than that. And so I think
*  that there is interesting studies that can be done. And I'm glad that people are getting some
*  use out of them that way. But like I said, I wouldn't have gone to build a large language
*  model just for that purpose. I think you can probably get at those questions other ways too.
*  Do we need... So Emily, you've famously... We're not going to go down the list of famous papers
*  that you've written, but thinking about the climbing towards NLU on meaning, form, and
*  understanding in the age of data where you argue that large language models don't understand
*  language, don't understand the meaning of what they're saying. Is meaning required for language?
*  And I guess a second question, which is maybe orthogonal, but does it matter how we learn
*  language? Okay. I'm glad you came back to that question because you asked it before and then
*  we didn't get to it. So is meaning required for language? I think, yes. The operational
*  definition of language that I work with, and I'd be interested to hear if this fits in Ev's
*  linguistic or language-related work as well, is that languages are symbolic systems. They are
*  systems that allow us to pair form and meaning in this open-ended way, sort of recombining
*  large but discrete sets of basic symbols into larger symbols. And also from the point of view
*  of why we might build language technology is it's about communication, right? And communication
*  isn't just passing strings back and forth. It's about using the strings as clues that allow the
*  interlocutor to reconstruct communicative intent or a good hypothesis about communicative intent.
*  And so that's where I see meaning being really key to language. Now, does it matter if we learn
*  it the same or learn it differently? So who are we, right? So I think there's probably really
*  interesting questions about what's the range of human variability in how languages are learned?
*  How does that interact with cultural practices about how children are spoken to? How does that
*  interact with modality? And always looking at that with a sort of expansive sense of normal
*  and not there's better or worse ways of doing it. That's sort of one of the pitfalls of that
*  kind of research is it's often the questions can be asked descriptively and inclusively,
*  or they can be asked in a very discriminatory way. Or does we include in that concept machines,
*  right? And does it matter whether machines are learning language as much as they're learning
*  it differently from humans? I would say yes in two ways. One is to the extent that we're
*  claiming that the machines are a model that we're going to use to study humans, then we need to be
*  very clear about what the similarities and differences are because that gives us the
*  limits of the model. And then secondly, if we're going to be building technology that people are
*  using, the way in which the system was learned might put some limits or tell us something about
*  the resulting system. Yeah, I know. Yeah, largely. I think for the most part, I mean, I think,
*  again, I'm really excited. I have this renewed excitement about using these models to try to
*  understand something about how humans learn. And in fact, I just have a postdoc who started
*  yesterday, Cheng Zhezhuang, who comes from Dan Yemens' group, who is interested in exactly this
*  question of how do you need to train a model differently on linguistic input, including
*  cross model data or different learning algorithms, which are more human childlike, or a different
*  nature and amounts of input and seeing whether models trained in these more likely ways, more
*  similar ways to human children, capture something about responses and developing brains to language.
*  And I think that's a really cool and exciting enterprise. And I'm optimistic. I mean, I am a
*  very strong optimist. So I'm optimistic that we can learn something that has been hard to learn
*  with just having access to human neural data and being limited to these kinds of verbal
*  hypotheses about how things happen. In terms of symbolic versus non-symbolic, it's a hard
*  issue. I don't think we have great proposals for how symbols can be instantiated in neurons,
*  which is not to say that that's not how it is, but it would be great to try to
*  move a little bit more in that direction. And I think some of our thinking certainly is
*  symbolic and how much of that characterizes the language system. I think I probably am less
*  strongly on the symbolic side, purely symbolic side than you, Emily, which is fine, right? We can
*  disagree. That's okay. Yeah, absolutely. What about our bodies? I mean, so there's this grounding
*  issue, right? That language needs to be grounded in the real world for meaning to adhere. Thinking
*  about how we learn language, is our biology important? Are our bodies the embodiment that we
*  have? Is that important for language? But so as like, you're going to be training these
*  different models, giving them different kinds of input, but they still don't have bodies. They're
*  not grounded in the world, right? So to speak. It's a very good question. I mean, I think
*  the literatures to pay attention to here are concerned evidence from individuals with very
*  different developmental experiences. There are individuals who are born without limbs,
*  or individuals who are born blind, or individuals who are born deaf, or have other
*  differences in how they experience the world. And one thing that we've learned from some of
*  these studies is that a lot of these perceptual and motor experiences just don't seem to be
*  critically needed to learn really sophisticated models of the world, to acquire sophisticated
*  models of the world. So a striking example, like congenitally blind individuals, knowledge of the
*  color space, or really visual concepts like glance versus glare, and things like that,
*  are very similar to those of individuals who have had access to visual input growing up.
*  And I think what this tells you is that a lot of that information is redundantly represented in the
*  regularities in language. And I think there's interesting questions you can ask given that.
*  But whether a model needs to interact perceptually and in motor ways with its environment, I think
*  it's an empirical question. And people are trying to build embodied language systems.
*  And again, I'm less excited about building it for the goal of building it. Like I'm interested in
*  how will the representations of linguistic meanings, for example, be different for those kinds of
*  models compared to these disembodied text synthesizers, as Emily called them.
*  I think there's a lot to be really careful about here when we talk about the experiences of people
*  with developmental differences and congenitally blind folks and so on. Because there's a move
*  that the people who are interested in promoting the language models as minds rather than as
*  text synthesizing machines make where they draw an analogy between language models and
*  the experiences of deafblind people, for example. And it ends up just always coming across as
*  terribly dehumanizing. Because that analogy is inherently dehumanizing. And I'm in the middle
*  of an ongoing Twitter argument about it again, because people keep doing it. But I think that
*  it's not that any given aspect of our physicality, of our sensory apparatus,
*  is inherently required. But rather, I think, and when you said redundantly encoded, I was actually
*  thinking you were, I was making a prediction about you going a different direction based on
*  my thoughts, which is that our experience of the world is redundantly encoded. We have many
*  different ways of experiencing the world. And we have also many different ways of performing
*  intersubjectivity and sharing experiences of the world. And I think that that's what gives us the
*  toehold in learning the linguistic system. And then once we've acquired a linguistic system,
*  we can use it, like you say, to get information that's redundantly encoded in language. And it's
*  not just distributional. So people will often say the distributional hypothesis is that meaning
*  is use. Wittgenstein says meaning is use. And my retort to that always is, right, but use isn't
*  just distribution. Use is use in some specific communicative context, which is embodied. And
*  that's probably important. But I don't think any particular aspect of the embodiment is,
*  there's facts of embodiment, but there's a lot of redundancy there. And so I think that what's
*  missing is not so much embodiment as experience of the world or what's necessary as experience
*  of the world. And when we talk about the world, it's important to keep in mind that the world is
*  not just the physical and natural world around us, but also the social world that we inhabit.
*  And so there's a lot of richness and complexity there that we are situated in. And that seems to
*  be, is it necessary for learning is maybe the kind of question that building these artificial
*  models would help us answer. But it certainly is a fact of how we learn, because we are all
*  situated in our world, and that's where our learning is taking place.
*  I know that you're both very busy people, so maybe we can just end on sort of an open-ended
*  question. Ev, you were just talking about how foolishly optimistic you are. Put a judgment in
*  there. No, I said foolish. I didn't say foolishly. And Emily, it seems like you have more of a doom
*  and gloom projection toward the future. I have children, and we're in the midst of
*  battling the screen time issue, and my daughter talks to the phone to call a song up. And I'm
*  somewhat terrified for their future interacting with these things because of our proclivity,
*  because of our tendency to anthropomorphize. But I don't know that my terror is well-founded,
*  because we're terrible at predicting the future as humans, as you know. And I think that's
*  the best way to go. So I'm curious, maybe we can start with you, Emily, if
*  am I right in thinking that it's a doom and gloom scenario, or do you see light at the end of the
*  tunnel and that good will come out of large language models and whatever happens next?
*  Because next year, we won't be talking about transformers. We'll be talking about something
*  else, right? Yeah, let's call them exfoliators, just to pick a random one.
*  So I'm laughing at being characterized as not an optimist, because personally, who I am,
*  I'm actually very optimistic. And I think my optimism is rooted in a sense of we collectively
*  make our world. We live in it, we learn in it, and we also create it. And so it's up to us.
*  Not any one of us individually, but all of us collectively can make decisions, and we can
*  make decisions regarding language technology, for example, around, okay, well, what kind of
*  regulation do we want to put in place? What kind of transparency do we want to require? What kind
*  of data production do we want to require? And so on. These aren't going to be easy things to do,
*  but they are things that we can do. And I think when you're talking about the fear that you have
*  as a parent of screen time and how your kids are going to be interacting with things, I feel like
*  we can be empowered through transparency in many ways. And I think that there's a course
*  correction that's needed away from technology that's leaning into our proclivities to
*  anthropomorphize and towards technology that is designed to be helpful tools to assist people in
*  doing what we want to do and not take advantage or, as I say in one of my op-eds, abuse our empathy.
*  But that's not going to happen, because technologists don't care about that, right?
*  In a capitalist society, for example, the regulation whether we could actually do it well
*  is a different question. I tend to think that we're not good at regulating things either, or
*  that that's just a different road that may be unwise. But I just don't see
*  the regulators, the well-intended regulators, catching up with the technologists.
*  So yeah, I mean it's not something that's necessary. Optimism isn't saying,
*  oh, it's all going to be okay, right? Optimism is saying we have the opportunity to try to make it
*  okay. And I know that there's a bunch of work going on right now in Europe around an AI act.
*  And I think that what I'm hearing about is that there's some sensible stuff in there and some
*  stuff that's missing the mark. And a lot of people who are working in the space around
*  technology policy and regulation are engaging. That's also a whole field of study. And yes,
*  you're right that the forces of capitalism have certainly pushed things in a specific direction.
*  But I also think that most people working on technology are actually interested in working
*  on it to make people's lives better. And that there probably is a lot of goodwill that could
*  be leveraged. I'm the most pessimistic person here, I can tell. Do you share, Emily?
*  Yeah, I think that was right on the mark. I mean, I will also say another thing. I was trying to
*  remember the quote, but there's these actually a few quotes from parents worrying about their
*  children from centuries ago, where new technology comes. I'm just saying your kids are going to be
*  okay. I know, I know. Kids come with their, you know, I don't know. I have a five-year-old and
*  she likes her screens and she learns a ton from the screens. And so what's the learning mechanism,
*  ways to learn information have changed, but fundamentally, you know, humans come in with a
*  very good brain with a lot of tissue, much more tissue to do abstract reasoning than animals.
*  That's one difference. Again, it's a qualitative difference rather than a qualitative one.
*  But when you have a lot of space to play with that's not taken up by perception and motor control,
*  you can notice patterns, you can make generalizations, you can connect things
*  that nobody else had connected before. And that makes a, you know, fun and powerful tool that we
*  all have in our heads, much more so than probably any other tool that will ever be created by us.
*  Yeah, okay. I could go on and on about my children and your worries, but I guess we'll
*  leave it here. Thank you both so much for your time and thank you for your work and continued success.
*  Thank you. Thank you. It was very nice to meet you, Emily. Nice to meet you too.
*  Yes, likewise. And a really interesting discussion. Thank you. Yeah, it was fun.
*  I alone produce Brain Inspired. If you value this podcast, consider supporting it through Patreon
*  to access full versions of all the episodes and to join our Discord community. Or if you want to
*  learn more about the intersection of neuroscience and AI, consider signing up for my online course,
*  Neuro AI, The Quest to Explain Intelligence. Go to braininspired.co to learn more. To get in touch
*  with me, email paul at braininspired.co. You're hearing music by the new year. Find them at
*  thenewyear.net. Thank you. Thank you for your support. See you next time.

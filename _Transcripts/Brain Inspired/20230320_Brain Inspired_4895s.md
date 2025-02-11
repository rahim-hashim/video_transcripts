---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 4895s
Video Keywords: []
Video Views: 1775
Video Rating: None
---

# BI 163 Ellie Pavlick: The Mind of a Language Model
**Brain Inspired:** [March 20, 2023](https://www.youtube.com/watch?v=o8_lZbQ0PEs)
*  Are these human-like? Like people just have opinions, people are like, definitely yes,
*  people are like, definitely no. And basically it's an unanswerable question. Like anyone
*  who's a scientist should admit that that's an unanswerable question right now. And like
*  you're, it's just a matter of opinion. This question of whether the language models trained
*  only on text can learn meaning, presupposes a definition of meaning. And there are many
*  definitions of meaning on offer, none of which is the official one. Under some of them, definitely
*  yes. Under some of them, definitely no. And under others of them, like it depends, right?
*  There are very, very deep questions about language and cognition, right? Like how are
*  concepts structured? Then we have these giant language models that appear to do a good thing
*  with language. And there's a very deep question about like whether there's a connection that
*  is relevant.
*  This is Brain Inspired. I'm Paul. My guest today is Ellie Pavlik. Ellie runs her Language
*  Understanding and Representation Lab at Brown University, where she studies lots of topics
*  related to language. So in artificial intelligence, of course, large language models, sometimes
*  called foundation models, are all the rage these days, with their ability to generate
*  convincing language, although they still make plenty of mistakes. One of the things Ellie
*  is interested in is how these models work. What kinds of representations are being generated
*  in them to produce the language that they produce. So we discuss how she's going about
*  studying these models. For example, probing them to see whether something symbolic like
*  might be implemented in the models, even though they are of the deep learning neural
*  network variety, which aren't supposed to be able to work in a symbol like manner. We
*  also discuss whether grounding is required for language understanding. That is, whether
*  a model that produces language well needs to connect with the real world to actually
*  understand the text that it generates. We talk about what language is for, the current
*  limitations of large language models, how the models compare to humans, and a lot more.
*  If you value Brain Inspired, there are multiple ways to support this podcast. Go to braininspired.co
*  to learn how. I would really appreciate your support. Show notes for this episode are at
*  braininspired.co slash podcast slash 163. All right, here's Ellie.
*  Was it Socrates or Aristotle? I always get them confused, but I think it was Socrates
*  who worried that writing our language down, having a written language would make us dumb.
*  And that didn't happen. I'm pretty sure social media has made us dumb, dumber. Are large
*  language models going to make us dumb? I was literally talking to a student about
*  this this morning, asked the same question. I don't know, maybe I'm a fundamentally optimistic
*  person, but I really don't see that happening. And I would more guess they would make us
*  smarter in the way that like, there's like, it's a standing on the shoulders of giants kind of
*  situation, right? Like if there are certain types of tasks that are routine enough that the large
*  language model can do it, then it kind of frees up our time to focus on the harder things that
*  can't be done. I'm like, like, I picture like if you're if you work in some kind of job where
*  like reporting is part of your day to day and a ton of that time is spent just reading the various
*  documents, not adding any insights of your own, just sub selecting different passages, getting
*  the citations all in order, paraphrasing what was written, making it sound nice formatting and
*  things like that. And then only after you've done that, do you get to do your critical analysis,
*  make recommendations for you think way the pros and cons, you know, talk to people and solicit
*  feedback, like basically information that wasn't on the internet that chat GPT couldn't have done
*  like if that only happens after you've done the reporting, like great, you can have the report
*  generated right away and you can jump to the next step, right? It does seem like there's a lot more,
*  you know, I think there's more of a potential that it can mean we're using human brains to do
*  things that only human brains can do, then it means that everyone will stop thinking. I don't
*  know. But I'm sure there are people have the exact opposite opinion of me.
*  Yeah, well, well, I'm sure there's the complete spectrum. But in terms of like cogitating, right.
*  So a lot of people say and this is I think this is true that when you have thoughts about
*  something, if you try to write them down, you realize that they weren't they weren't clear
*  thoughts. And the act of writing them down clarifies your own thought process and how you
*  think about whatever you're writing. And so there's this generative sort of process that might be
*  missing.
*  Absolutely. Yeah, so that's like, that's the only way I know how to think through a problem is
*  writing. I think my students get very annoyed where it's like, we started a project and the next day
*  I'm like, have you started writing the paper yet? And they're like, I don't have any results yet.
*  It's like, doesn't matter. You should be writing the paper on day one, because that's how you know
*  what it's all about. But I, I don't know. I mean, I don't see why chat GPT means that humans are no
*  longer allowed to use writing for that goal. Right. So, you know, like, let's let's let's grant that
*  people still care about the work that they're doing and are trying to do good work and are trying to
*  affect the world in various ways. Right? Like, there are a lot of people who are lazy and are not
*  trying to do that. And, but those people aren't the ones who are really worried about them becoming
*  dumb anyway, like they're already probably cutting corners in various ways. Right. So let's assume
*  that people are actually, in some aspect of life, people are trying to do the right thing. There's
*  things you can use chat GPT for that it'll automate it. And then there's things where you're gonna be
*  like, no, the thing I was trying to do, I need to think this through myself. And so maybe what that
*  would be is like, you get chat GPT to generate a whole ton of stuff and reports for you, but you're
*  still going to have to think through what you're actually trying to do with that. Like, I, and at
*  that point, you might have to do some writing or some drafting or some thinking on your own. I, I
*  don't know, I guess I'm, I heard somebody use the analogy of like a calculator, like thinking of
*  chat GPT, like a calculator for language tests, I kind of like that analogy. So when I'm thinking
*  of it, I'm picturing a lot of like, people using it as a tool for like, reportative summarization,
*  search types of things. But under the assumption that they still actually want to contribute
*  something to the world, right? So maybe if you're in a dead end job, where all you're being asked to
*  do is generate the report report, and no one asks you for your own opinion on the matter, like that's
*  going to be automated. But those are unfulfilling jobs anyway. And those people just want to get
*  that job done and go home and then go do the thing they are passionate about, whatever that is.
*  Yeah, but for the things that we're passionate about, I don't imagine us being like, well, chat
*  GPT is doing it just as well. So I'm not even going to bother, right? Like, we definitely do have
*  things we can add on top of it.
*  I mean, I know that you you have switched or I don't know if you've always just given oral exams
*  instead of written exams. But there's this worry that every all the students are just going to be
*  using these prompt based language models to generate their their stuff. But you don't you
*  require oral exams?
*  I do have oral exams. I and I've been I think it's funny. So I've had those for the past couple
*  years. And I've talked to my colleagues and something that's basically I find it really hard
*  to tell from someone's written work, whether they understand what they're saying.
*  I find it hard to tell from my own thoughts even, you know, right?
*  I think it's very much this, like you said, the kind of, like I write to figure out to think
*  through a problem, I try to write it. And if I find that I'm failing to write it, it's because
*  I don't actually know what I think, right? It's like kind of like the failures of writing and
*  the failures of communication are actually failures of understanding. Like to me, if I can't
*  articulate it, it's because I don't actually know it's not that I know exactly what I want to say.
*  I'm just not sure what words to use, right? Like it's almost so. So yes, so like spending a lot of
*  time doing that, I can then see all of those intermediate pieces where I'm like, oh, I can
*  predict picture having generated this text, and it would probably mean I don't really understand
*  what I'm saying. But I find it really hard to then grade students based on this. Like, I don't know,
*  I just I feel very uncomfortable giving student a bad grade or less than good grade for writing
*  that I can't tell if they're just not a very good writer or they don't understand what's going on.
*  Whereas if I can talk to them or even just hear them say it in spoken language, somehow that
*  declows it a little bit. So I switched to that before chat GPT, just because I find writing hard
*  to evaluate. The fact that we find chat GPT also hard to evaluate just makes that point more clear.
*  So yeah, I think oral exams are great. So yeah, I think more of that would probably be good for
*  for students. So I'm going to keep us really broad picture here for a few moments before
*  we can dive into any of your vast array of work like analyzing these large language models. But
*  first I want to ask you, and I know this is not your area of expertise, but I had the thought
*  today that, you know, with with language models generating text, all this text is going to go on
*  the internet and language models are trained on the internet. So there's going to be this cycle of
*  them being trained on the text that they generate. And I'm curious, what if if you have any speculative
*  or otherwise ideas about what that might do to our language evolution, right? Because it's not
*  there's this whole cultural step, the way that language evolves. And I know that that's kind of
*  a debated thing as well. But this could really muck it up, perhaps. Yeah, definitely. I think that
*  will be fascinating to watch. It's kind of hard to anticipate, right? So so yeah, that is definitely
*  the case. I've heard people talk about the risk of this. Like even really simple things like
*  auto complete have already probably had an effect on like language diversity, right? I've used the
*  example for it's like, I get it. So I will often not use auto complete, because I care a lot about
*  being like, I wanted to say thank you with an exclamation point. And it's offering me thank you
*  with a period thanks with an exclamation point, or like something else. And I'm like, not none of
*  those are what I wanted to say. But, but I think a lot of people would be like, oh, that's not exactly
*  what I was gonna say. But sure, I'm going to take the one of the fewest clicks, right. And so then
*  you end up with this like just collapsing of the very basic diversity in the language that could then
*  kind of get fed back into the system and include less, even less diversity, or yes, for like
*  linguists analyzing it after the fact, you might see this kind of convergence. And then yes, the
*  language on the internet being out there and then retraining the models on like you could end up in
*  this kind of odd subspace of language that never you would have never reached from having just humans
*  generating it. So I think that'll be interesting to watch. I don't know, I don't like to be too
*  like melodramatically fatalistic about or something like, you know, technology and cultural exchange
*  and all kinds of things always change our language. And that's kind of a beautiful thing about it. It's
*  like you can see how it would adapt. Like, I mean, I could imagine there being some kind of hipster
*  culture, the way like vinyl and like home baking is is in vogue right now, right. Like you can
*  imagine people are like, I only write with like, pen and paper and send letters, and I'm going to
*  use language from the pre AI days or something, right. Like, I can imagine that kind of thing
*  coming up. And then we would get some other interesting language that would arise. I can
*  imagine like the development of particular linguistic markers that people use to signal how much they are
*  not the AI right, like the way that people will like spell stuff out rather than use like, I'll
*  type as soon as possible rather than ASAP, because ASAP has taken on a certain connotation that
*  as soon as possible doesn't have and you're like, oh, I want to mark this as not being part of that
*  lingo. I could I could imagine all kinds of interesting language evolving out of it that
*  like, not so much of so I wouldn't think of it so much as like a loss as like an evolution in the
*  way language is kind of always evolving with the technology and the times and it could be
*  hopefully a very interesting new thing to study. Yeah, I mean, it's always a danger to put a
*  normative stamp on the direction of evolution is good or bad. Right. Right. Because I mean,
*  language is definitely going to change in the next 50 100 years, no matter what, right. So it's just
*  it's going to change in different ways depending on the developments. But like, no matter what,
*  it's going to change. We're going to see evolution in language because that's what language does.
*  If you were if I forced you to freeze yourself for X amount of years and then wake up,
*  fall out and wake up and continue your research career, minimum of one year, how many maximum of
*  let's say 100 because that seems like a long time from now. I don't know, you can just specify it.
*  I just don't want you to say tomorrow. I mean, I kind of would say so this is a very exciting time
*  in this field, right? Like I would not want to miss what's going to happen in the next couple years.
*  I think a lot of very exciting stuff will happen in the next couple years.
*  So this is kind of a question that yeah, but if I have for you think, sorry, how far you think
*  along we are in understanding in your satisfaction in understanding
*  language models and whether we have the right tools and etc.
*  So like, I just completely pulled out my ass number that I've been kind of using is I feel like
*  more than five less than 10 years will be a window where we will have and that and some people like
*  that seems weirdly like soon. But like where we'll have like a deep understanding of actually how the
*  models work. Like I think that right now we don't know what's happening under the hood really in any
*  real sense. And so that makes it hard to use the insights we get from them to actually inform what
*  we think about language, inform what we think about humans, answer questions like are these
*  human like, like people just have opinions, people are like definitely yes, people like definitely
*  no. And basically, it's an unanswerable question. Like anyone who's a scientist should admit that
*  that's an unanswerable question right now. And like you're it's just a matter of opinion.
*  It's an abstentiate opinion. Like we just can't say because we just don't know really anything
*  about the mechanisms. We don't know about the representations. We don't really like we're
*  looking at individual model artifacts. So I think right now we just know very little. But I think a
*  lot of people are working on it, the field is advancing very significantly. And I think I just
*  see a lot of work from very good people trying to get just a much more low level theoretical
*  mathematical understanding what's happening under the hood. And that's pretty interdisciplinary
*  work where there's people in cognitive science and neuroscience also trying to look at that.
*  So I'm hopeful that like, we don't have we're not gonna have to wait forever to, to have like,
*  we're not going to maybe understand them in 100% perfection. But I think we'll be able to understand
*  them at a much more rapid pace than we understand the human brain, for example, like I think they're
*  probably simpler systems than that. This is the kind of thing where I'm probably going on
*  recognizing stuff that is completely wrong, right? Where it's like, you know, I said they
*  were simpler than the human brain, it turns out they're like crazy. But that would be crazy.
*  Basically, I think when the five to 10 year timeframe, we'll be able to say some something
*  precise and meaningful about how they work, that will then lend insights or at least answer some
*  of these questions that are really like everyone's trying to ask about like, can they like people
*  keep trying to speculate on tasks they absolutely can't do or absolutely will do. And I just think
*  it's utter speculation. But hopefully in five to 10 years, it won't be utter speculation, we can
*  say with some some level of rigor, like, no, this is within the scope of the types of problems they
*  can solve. This is within the scope of the problem. Like, I think we'll have that within the decade.
*  But I don't think we'll have it before at least five years. But I don't know where I got this
*  number. It's just this that feeling. So yeah, right. It's an opinion. So I would need to
*  Yes, I would. Yeah. Yeah. So I guess I would thaw me out at five to 10 years. But that's the
*  thing is like, I don't want to miss the process of getting there. That sounds like the fun part. So
*  I would be very sad. So I guess on that I would continue. I have to get frozen now. Because I
*  would rather like go for five or 10 years, get frozen then and then wake up in 100. That would
*  be my preference. Okay, I like that answer. I'll accept that answer. Okay. Good. Besides, if you
*  got frozen, you would miss out on your child's early days early years you have one child. Well,
*  now we're just getting deeply depressing. I don't want to think about I'm frozen and missing out on
*  my child's. Yeah, she's she's 16 months old right now. Oh, okay. I thought she might have been a
*  little bit older. I was gonna I'll freeze your child to one. I was going to I was going to ask
*  so this is kind of a big question, I suppose, or maybe 1000 questions in one, but you know, having
*  the experience, you know, the 16 month old, has that changed your views on language?
*  And like it's sort of well, so here's where the multiple facets of the question comes in,
*  because you were just alluding to how we don't understand humans and we don't understand
*  language models. So like there's it's really hard, you know, everyone just has an opinion,
*  but has the advent of these language models and their press impressive capabilities,
*  has it changed your own views on the nature of language, the the where language sits in the
*  hierarchy of our cognitive functions, you know, how special it is, etc.
*  I don't to give an annoying answer, like, no, it hasn't. Like, it's like,
*  so annoying, seeing the seeing the massive pace of science in my field, and also becoming a mother,
*  no, these have not affected me at all. Like, I'm still the same. But no, I think, like, no, I think,
*  in many ways, like, I think knowing a lot of, so I just said, we know very little about how the
*  systems work under the hood. But, but from what we do know, right, like kind of knowing how they're
*  trained, understanding that they're learning these different patterns and learnings associations and
*  being able to replicate them like that kind of stuff. I think maybe I've always been kind of on
*  the, you know, I mean, I'm an LP person coming up in the machine learning computational
*  distributional semantics. So, so kind of, maybe never thought language was that special
*  in this regard. And seeing the success of it and knowing kind of where it came from, I'm not like,
*  oh, my god, I never thought like, I guess I never was of the opinion, like, we will never get here.
*  Maybe some other people are like, never saw this coming. But maybe I've just been like,
*  kind of in the optimistic group for a while that seeing it was like, okay, maybe I didn't
*  think it would happen this soon or something. But I don't know, maybe I kind of, I don't know. So
*  from that perspective, I'm like, this type of behavior coming out of a system, I don't think
*  makes me fundamentally question the nature of language the way maybe I would if I'd been
*  brought up in a different tradition that was like more of a, you know, maybe a Chomskian tradition
*  or something that's like, no, these models will never be able to do this. So there's that, I think,
*  like, I'm very, very excited to see the models and their success. But I don't think I was like,
*  I never saw this coming or floored in that respect. And so that doesn't. And then also just
*  knowing a bit about their trained. I mean, I'm very much am interested in whether what's happening
*  under the hood could be similar to what we think about humans or could inform what we think about
*  humans. But the way they are trained is nothing like how humans are learning language. And so
*  from that respect, it's like, I just don't think of them as human like in that way, right. So it's
*  not like when I see my daughter learning language, I'm like, I just think of them as entirely
*  different systems in that, in some ways that it's like the analogy isn't even that isn't even as
*  salient as maybe I always thought it would be before I had kids like people like, Oh, it'll be
*  so cool for you as a language researcher to see. But like, when I see her learning language and
*  stuff, I rarely am actually thinking in terms of analogies to these systems. There were certain
*  types of things. So like for a long time, I had this is new in really language, but I had like,
*  there was this funny example in deep mind of like teaching this little thing how to walk
*  with reinforcement, deep reinforcement learning, and it like walks like this. But there was an
*  example of it failing, and it was like laying on its back and like, like kind of writhing around
*  to like scoot along the floor. And people are like, this is a failure, like it doesn't have the right
*  inductive biases, it doesn't know blah, blah, blah. But I definitely I failed to get a video of it.
*  I'm so upset. But before my when my daughter was learning to crawl, she definitely did this she like
*  writhed on her back across the floor. And I was like, okay, so this is not like a an example of
*  an inductive bias failure, like kids also do these ridiculous partial solutions of stuff that we think
*  is weird in the learning process. So there's certain types of things like analogies like that, or like,
*  these miss mapping of words where she like over. So we were playing a she likes to point to her
*  belly button. And we were playing her name's core is like that's core is belly button. This is mom's
*  belly button. Now she seems to think that for a while then if you said core or you said mom,
*  she thought it meant point to your belly button. Right. And this is like such a like neural net
*  type of like over generalization thing to do where it's like, oh, I saw these things in the same
*  context, and I can't differentiate them. And so there's certain types of these like errors that
*  she makes them like, oh, that seems kind of like a neural netty error. But then there are, of course,
*  things that she succeeds on very quickly that neural nets would never do like that she like
*  learns very quickly. So I don't know. So there's some kind of analogies I've now kind of been
*  rambling on this answer a lot. But I don't think there's like a super Yeah, I don't know. It's
*  kind of a piecemeal answer. Sometimes I think of it out. Yeah. Well, okay. First of all, we almost
*  named my daughter Cora, but it became Nora instead. Secondly, yeah, pointing at your belly button
*  right is an action. And I don't know if we just need to jump right into this. But a lot of some of
*  some of your avenues of research deal with I know that you're interested in grounding language like
*  in the world and how we learn as humans. But so is this a fair statement to make based on your
*  thinking? Am I interpreting your thinking correct that you think it might be possible for a text
*  only trained large language model that's completely ungrounded to sort of learn that
*  and get the grounding later, in other words, kind of learn backwards relative to humans?
*  Yeah, I think it's possible. So I think a couple years ago, I've been very interested in the
*  ground of research. And when I was starting, like at Brown, when I first joined Brown, one of the
*  things that I was, that was one of the things I was really excited to because I worked a lot
*  on semantics and stuff in my PhD. And that felt like the missing ingredient was grounding. So this,
*  I would say this is something where I have changed a lot of my opinion has switched a lot in the last
*  couple of years because I was and I wouldn't I wouldn't say it's switched. I still kind of
*  consider myself like I'm unsure. But like five years ago, I was like, no, definitely grounding,
*  embodied interaction is the missing ingredient. We're going to need that if we want the model
*  to learn like meaning. So you just for people who aren't watching the video, you used air quotes
*  when you said meaning and this is what is meaning? Do we what is that? Do our language models
*  understanding what they're doing? Well, what is understanding? What is semantics? Why, you know,
*  right? Are we asking the right? So anyway, sorry to interrupt. Yes. Yeah, yeah. And these like these
*  are the questions that like, I spent all of my time when I'm not answering emails thinking about
*  because these are like the really interesting questions, right? And this is what my students
*  are all thinking about. And the reason I think it's really, really hard is just the every time you
*  ask these questions, it has like some assumptions that some other field actually has an answer for
*  you like philosophy or neuroscience or something or linguistics that you can just go and get the
*  answer and then we can ask the question purely by thinking about how the models work. But actually,
*  it's like it's actively being worked on in all these fields. So these things are all coming along
*  together. And so this this question of whether the language models trained only on text can learn
*  meaning presupposes a definition of meaning and there are many definitions of meaning on offer,
*  none of which is the official one. Under some of them, definitely yes, under some of them,
*  definitely no and under others of them, like it depends, right? So, I mean, I think there are like
*  many arguments you can make for why the language model maybe would be indistinguishable from a
*  thing that was embodied. Some of these arguments are like, well, most of the concepts that we know,
*  you never interacted with directly, right? Like someone just tells you about a thing and now you
*  know about that thing. Like you don't have to have like been to like Greece to have the concept of
*  Greece and you don't even really have to have seen pictures of Greece to have the concept of Greece.
*  Like it's fine. And actually, most of our concepts, we probably get through this kind of
*  chain of being told stuff. There's other arguments that are like, well, you know, maybe
*  we can't really tell, like people like all we can really observe is the way people associate
*  concepts with other concepts. And so you can't really directly observe people's perceptual
*  experience. Maybe that's not actually that important for the meaning. It could be like a part of it,
*  but it's not a key one. So there's like arguments to those types of effects, which if you buy them
*  for humans, then you could apply them to language models and say that I have the same thing. Of
*  course, there's other arguments that are like, no, the grounding to the world is the most important
*  thing. Like that direct experience with it. And if you have that, and this is what you're referring
*  to, we were thinking just empirically, perhaps it's the case that you could learn a structure
*  that's basically the same structure as what you would have had in the grounded case,
*  just by reading text, and then post hoc map it on. And that's something that we've been kind of
*  exploring it empirically and trying to suss out whether that's the case, because that's really an
*  empirical question more than a philosophical one. So there's like a lot of avenues to go.
*  And I think the question of whether what the model has constant meaning really depends on what your
*  theory of meaning is. And there's a lot of them. And they've been extensively explored in philosophy.
*  A lot of people have like intuitive feelings about what they think the right theory of meaning is. And
*  if you go and start studying your philosophy, you'll realize that like none of those intuitions
*  quite aligns perfectly with any theory that's stood up to enough rigor. And so it's like not
*  an easy question to him. Yeah. Well, could you summarize and I know that we haven't used the
*  term affordances yet, but which is another debatable term, whether an affordance exists
*  and what it actually means and stuff. But can you summarize sort of what what your, you know,
*  maybe high level kind of what you found with your initial tests of this, you know, language,
*  pre trained language model grounding first grounding after approach? Yeah, so we did some
*  kind of work on on like, like basically having an agent like observe objects moving around in a
*  3d world and trying to predict, like so that the way the model is trained is just predict
*  where this object is going to be at the next frame, given the trajectory up until now. Right.
*  That was actually meant to kind of be the physical world version of the language modeling task. So
*  in language modeling, you're just like, given each a sequence of words, predict the next word.
*  And when we do that, given a sequence of words, predict the next word task, you get really nice
*  abstract linguistic representations, like we see this kind of representations of syntax and various
*  semantic structures. And so that is very exciting to see in language. So we're like, well, maybe if
*  we apply a similar learning objective over like the physical world, we would get the representation
*  of these kinds of physical concepts. And one of the concepts that we thought we might get is
*  something like affordances, right? So like, you would see something like the model should learn
*  to differentiate, like we also did kind of basic verbs. And actually, like you said, there's debate
*  about whether affordances exist, I think this kind of like, verbs versus affordances, like,
*  like some studies just consider all of the verbs to basically be affordances, others have a very
*  small set of fundamental for instance, it was really hard to tell. So but what we ended up
*  looking for is like, kind of did the model learn these representations of like basic
*  actions? Does it differentiate between like a rolling event and a falling event and a sliding
*  event and those types of things? And this was interesting, because this was without any language
*  there, right? So this would be like, this is, yeah, so this was like, do you, we were trying to answer
*  like, starting to get at the question of like, maybe some of these concepts might like emerge
*  or like people might develop these concepts just by interacting physical world. And then later when
*  they learn language, they're just mapping language to them. That's like very different from the kind
*  of environment where you might actually learn to differentiate the concept, largely because there's
*  a word there that you're trying to attach the event, right? So yeah, so we did find some good
*  evidence that a lot of these concepts did emerge even without the language and that they,
*  but not perfectly in a totally separate study. And that's different, I can't go into details,
*  but we did play around with like, vision and language models, some which have language and
*  some which don't. And we did find like certain concepts. So in like the the vision only models,
*  the concepts of like bunny and squirrel were just not differentiated, right? It was like,
*  this was a model that was basically just trained to predict missing visual patches in a visual
*  scene. And it doesn't really differentiate between like small furry woodland creatures,
*  because like, that's actually maybe not that useful if you're just trying to like,
*  have some notion of like visual predictability. Whereas once you introduce language, then it very
*  neatly separates those things, right? Right. Yeah. And I would imagine that if we were apply
*  similar stuff to this like, verb and affordance learning, it would be similar, there would be
*  some things that are very salient and like useful concepts to form for the sake of like, predicting
*  the state of the physical world. But that unless you need to assign words to them,
*  they're not like sufficiently different to really, to really distinguish. So maybe something like a
*  push versus a nudge or something like those might just be part of the same category. And it's a
*  matter of degree, versus once we assign words to them, then you discretize it, and you have to just
*  kind of actually separate pushing and nudging or something and more, more concretely.
*  Similar to like how I can only distinguish like three different types of trees, my dad could name
*  like every tree and I, the tree is a tree to me. And there are only three types, apparently.
*  Yes. I'm surprised you even have three types. I think I just, well, no, maybe I have two types.
*  There's like Christmas trees and other trees. Maybe palm trees. Okay, I have three types.
*  Nice job. So, so where are we then in terms of? I know this is an unfair question, but
*  you know, just semantics, affordances, groundedness, the relation between all these things,
*  what, how does the field view these? Are they? Are they important? I know it depends on who you ask,
*  but it just in broad strokes. Yeah, this is where I want this is where my kind of five to 10 year
*  thing is kind of getting at. So like, to me, there are, there are very, very deep questions about
*  language and cognition, right? Like how are concepts structured such that they support
*  the kinds of things we can do with language. And then we have these giant language models
*  that appear to do a good thing with language. And there's a very deep question about like,
*  whether there's a connection that is relevant, right? Like does the language model tell us
*  something about that first thing? Like there's a successive chat GPT tell us something or generate
*  new hypotheses, proposed possible explanations or theories about what might be happening in human
*  language. What might be happening in the brain, the mind. And I just don't think we can say at
*  all, whether it does or doesn't right now, because we just don't know how it works. And so if we can,
*  I think over the next five or 10 years, there's some kind of basic science of just what is
*  happening inside the neural network. And I think after we do that, we might be able to say something
*  like, okay, we've, so one option is we figured out what's happening. And it's, it's all a giant
*  scam, right? Like the model has actually just memorized, like turns out everything chat GPT
*  generated was exactly printed on the internet somewhere. And it just recalled it right? Like,
*  very unlikely that that's the case. But that's kind of the flavor of what a lot of people,
*  like that's an extreme version of what some kind of super skeptics feel like is happening with
*  the neural networks is they're really just memorizing a large fraction of things and doing
*  some minor tweaks or something that just deeply, deeply does not resemble compositional creative
*  cognitive processes, right? But some people argue that we're also doing that, like already has songs.
*  I don't know if you're familiar with his direct fit to nature, I think it's called, you know,
*  just like that our brains are essentially these same sorts of things and just memorizing and
*  Yeah, so that actually, so that's an interesting thing. So I think something that like, so, like,
*  so definitely what we won't find, like, well, some people might think we might find something
*  like this in chat, you would do it seems unlikely, like a list of all the possible responses. And
*  when you put in a prompt, it searches through something like a database finds that and
*  regurgitates it. If that's what we found, I think people would be pretty well, probably surprised,
*  actually, but pretty unlikely to say, let's go see if this is what humans are doing. Let's see if
*  this is where human speech comes from, because that seems like a very ridiculous thing to propose
*  that, like, the way that I'm generating this right now is I'm like going through my inventory of
*  possible responses to this question that I've memorized verbatim. But what we'll probably find
*  is some mechanism that looks has a lot of memorization involved and a lot of generalization
*  involved. And what we hopefully will have is a fairly precise story of how those things are
*  getting mixed and matched and combined, right, because we'll be able to say, we don't know what
*  humans are doing, but chat GPT is doing it like this, right, it's memorizing this type of thing,
*  it's generalizing in this type of way, it's defined these kinds of categories under this setting,
*  it, you know, calls from memory under this setting, it decides to extrapolate or something,
*  right. And if we had that kind of a story, then we could actually go look for similar, like,
*  we would have a more clear sense of what we're looking for in the brain, right, like, it would
*  be a concrete proposal about something that could be happening. And maybe some subset of those things
*  actually could be similar to what's happening. So I think that would be like this really exciting
*  thing. And like grounding would be one of those things, right? Like, we could actually say,
*  here's a concept that we always thought required grounding, we have a model like,
*  I'm scare quoting again around grounding all of these words, I might as well just scare quote my
*  entire everything. But so we could take some concept that we kind of assume requires grounding,
*  we can figure out what, and this is a lot of ifs and ifs and ifs, but I'm imagining that we're in
*  a place where we have a good understanding what's happening inside the mouse, we could see what chat
*  GPT or whatever the successor model that we're looking at does with that concept. And then we
*  can go try to see if the representative like it would generate some predictions about what we
*  should and shouldn't see within humans if they're answering or if they're representing it similarly,
*  right. And that could actually help us pretty precisely answer some of these questions that
*  right now are very philosophical, like right now the question of whether how important is grounding
*  to humans is largely philosophical with some empirical data, right? I think so I think there's
*  a lot of potential for like a really interesting connection between these fields, but it's hard to
*  do when we just know as little as we currently do about how the models work. But I think it will be
*  pretty doable when we know about five to 10 years more than we currently do, hopefully even sooner
*  than hopefully sooner than 10. So yeah, so some of these big questions you said about semantics and
*  grounding and affordances and stuff, like I think we might be primed to actually have really concrete
*  answers like actual proposed concrete scientific studies to try to move ourselves forward on those
*  questions as a result of these computational models. But I don't think we can do it right now
*  because they're too black boxy. I'm going to ask you about the difference between analyzing the
*  representations versus analyzing the outputs of the models in a moment. But I can't help before
*  but before that ask, I'm sure you're aware of work like out of the lab of Fedorenko who's been on the
*  podcast and or Hassan looking at the the the representations of the models and correlating
*  that to human based human behavior. And there's this high correlation with predicting so a lot
*  of these large language models are predicting the next word essentially is how they're they're
*  objective. And it turns out if you run the data through some bells and whistles,
*  there's a correlation between humans doing the same thing. And so how much do you think that
*  next word prediction is is the way that humans do it?
*  Yeah, I mean, that's a very like, has to be a multifaceted answer, right? Like, I think there's
*  pretty good evidence that humans predict the next word, right? Like we're good at anticipating,
*  we have to. But if you're asking is like, so like right now, what I'm doing is not
*  predicting the next word and then saying the word that I predicted to be the next word.
*  Based on probability distributions over words, there's, I mean, this is like a,
*  you know, we can get into like a subtle distinction about like, what is the
*  like, how many latent variables are allowed to calculate into this predicting of the next word,
*  like if you say, well, maybe I'm predicting the most likely next word conditioned on what I'm
*  trying to say or something, then like, sure. But I think, yeah, I guess I don't want to make a
*  hard stance. It's like, basically, what does it mean to be predicting the next word? But I think
*  most people would argue that humans have a strong component that's not a predictive one, right?
*  There's some goal directed something to what they're doing with language, right? So it's not
*  a, so we and then I so one of the things I think needs to be analyzed in chat GBT is whether
*  there's similarly some other latent state that you could argue or I use chat GBT as like shorthand
*  for like all such models, right? Like, there's a ton of these models. It's like the name brand now
*  like Kleenex or something. So like, I mean, any of these models, but when we look at these models,
*  um, uh, you know, we're trying to figure out what they're doing. Like, what is the organization of
*  the latent states that are contributing to the predicted next word, because that's where the real
*  depth of trying to decide whether it's analogous to humans is, is useful, right? Like,
*  I don't know if this quite answered your question, but I think like,
*  right, like, I think there's clear, like, clearly humans do a lot of predicting.
*  There's a strong predictive component. We're good at predicting. I think the distribution of words
*  has a huge effect on how we learn them and what we learn about them. Um, but it's just
*  overly simplistic to say there's nothing else that's generating what a person says than just
*  trying to guess what would be a likely continuation, right? Um, with no other constraints,
*  just saying just purely thinking about a likely continuation, right? Because we have goals and
*  agencies and, and, uh, intense when we're generating, um, of course you could recast those
*  things as being part of the predictive task and then sure, right? So, so then it kind of becomes
*  equivalent about what we mean by predictive. Um, do you think that, um, there, there isn't a set,
*  um, like a standard set of criteria by which we evaluate models? Does there need to be? I mean,
*  I know that, you know, you, you could take your 14 strands of research, right? And all the tests
*  that you do and include it and like a battery of tests, right? To understand, um, and analyze
*  these models, does there need to be a kind of, I don't want to say benchmark set, but like a standard
*  set of, um, evaluation criteria? So I actually, this is, I feel like if a couple of years ago,
*  you'd ask, I'd be like, of course, this is the main goal. And I think actually I've been pushing
*  a very different, um, line that, which is, so I think I've really liked, I found it very freeing
*  in my own work. And I want to talk to other people is moving to treating it like a natural science,
*  right? So we have these models, we don't understand how they work. And so the game is not
*  just make them better, but test hypothesis, you know, formulate good experimental design to try
*  to figure out what is happening. And so in the same way that you don't say like, here's the
*  benchmark, I mean, it's a fundamentally different thing, but like other fields, this notion of like
*  a standardized set of benchmarks or something is not really the, um, uh, the way you think about
*  studying designs. Of course, there's kind of the phrase everyone's responsible for the same data,
*  right? So once there's a set of studies and data out there, if you propose some new theory,
*  it has to be consistent with all the other data that's out there. In some ways that kind of feels
*  like some massive benchmark or like a benchmark for theories or something. Um, but I think right now,
*  maybe NLP has a comment of the strong engineering culture and has like a real interest in, um,
*  in standardizing and benchmarking models. Um, and I think that there's a time and place for
*  when that is exactly the right thing to do. And I think in the past, like we NLP advanced a lot
*  because of this culture, but I think right now is not like, I think it's not the right time to be
*  trying to build the newest and latest and greatest benchmark. I think that we just don't know enough
*  to know what that thing is. And a lot of resources could be wasted on things that just go stale very
*  quickly or worse. Uh, we, we kind of, um, climb the wrong hill, right? So I think it's, there's
*  nothing wrong with, again, going with my kind of five to 10 year timeframe. I think there's nothing
*  wrong with taking a couple of years, try to figure out what's going on. Basically run some basic
*  science tests on benchmarking and evaluation, try to figure out, um, like what are the, the dimensions
*  of the models that we understand and don't understand and what are the things we're trying
*  to evaluate and can we try to come up with things that correlate with the outcomes that we care about
*  or the things we, and then probably later we'll, we'll want benchmarks again, because we'll be in a
*  race of just trying to build better models again. But to me right now, like I see a lot of really
*  smart people coming out with cleverly designed benchmarks that somehow don't, they still don't
*  seem to really get at what we're trying to get at. Because often what this takes the form of is let's
*  think of a really hard task, let's get humans to do it, right? And so then the models when they
*  fresh, like to everyone's frustration, crush it very quickly. We're not really willing to accept
*  that therefore they are human level. Um, and so what did the benchmark tell us? Cause like we
*  designed the benchmark, presume it, but then we say somehow success on this benchmark is not
*  informative. Maybe failure would have been informative or something. I don't know. I,
*  it just feels like not the right time to be building more and more and more benchmarks. I think that
*  taking a step back, thinking more critically, doing a lot of hypothesis testing, that's probably
*  the right move right now. It doesn't mean it's the right move forever, but right now.
*  Well, yeah, I didn't mean, that's why I didn't want to use the word benchmark because that
*  entails like improving models ability. Like if you pass, if you can pass this test with 90 X
*  something percent accuracy, what I was alluding to was this, the sort of hypothesis testing that
*  you're doing in analyzing, you know, are the models quote unquote understanding, do they have
*  meaning or do they, do they have abstract symbols, concepts like in the representations and kind of
*  basing, comparing that to the way that we think humans do language, because we don't know how
*  humans really do language, right? So like, there's this kind of give and take and back and forth.
*  But it's, you know, I asked this because you do tests on these representations. And it's kind of
*  like those tests that, well, if the model is getting, if the representations in the model look
*  a certain way, then we think it's more human like, or less human like. So I'm not sure what I'm what
*  I want to ask you. You know, I want to ask you 15 different questions based on this topic. But
*  like, are humans the right benchmark? Does it even matter if they do it like humans do? And
*  do you think that they will? Yeah, I think it depends what you're trying to do and who you're
*  talking to, right? So I think there's Yeah, so there's probably 15 different answers for each
*  of your 15 different questions. But so I would say, I will definitely I'll start with the kind
*  of the looking at the looking at representations, because this is something that I just think is
*  just kind of all important right now, like just for our own understanding, that looking at the
*  behaviors of the models, we end up in this position of having like, there's multiple different things
*  that could have been happening under the hood that could have resulted in the same performance,
*  right? And so that from an understanding standpoint, if we and there's many reasons,
*  we might want to understand the models, one is that we want to understand them so we can
*  trust them, right, so that we can make them safer. So that we can explain their predictions to
*  humans. One is we want to understand them so we can make them better, because if we understand
*  what's happening on the hood, maybe we can fix some problems, right? And others, we want to
*  understand them, because we want to use them as models of humans, and generate predictions about
*  humans, right? Those are all and I'm sure there's many other reasons we want to understand them,
*  honestly, just curiosity, it's a really good reason to want to understand them. So I think
*  that looking at behavior alone without looking at representations and mechanisms under the hood,
*  doesn't help us understand them for any of those reasons, right? But then, for some of those reasons,
*  it matters if they're human like, and for others, it doesn't, right? So if you're trying to
*  understand whether the success of large language models tells us anything about
*  the neuroscience or cognitive science or linguistics that's happening in humans,
*  it matters if they're human like, right? So from that perspective, it's very interesting.
*  If you're just trying to make them safe and trustworthy and understandable, it probably
*  doesn't matter if they're human like, but you still need to know what's happening under the hood.
*  So I think my lab is pretty interested in both, like I am just deeply curious how the models work
*  for the sake of knowing how they work, because we're computational linguists, and we work on
*  building these models, and it's unsatisfying to see them working and not know how they're working.
*  But I'm also really interested in my students are really interested in understanding humans.
*  So we often do a little bit of both, right? So like theories about how humans work are a good
*  source of hypotheses for how models work, right? So we're saying like, we know humans are composition.
*  Well, we need hypotheses, right? So otherwise, you're just pulling it out of your ass,
*  like, I don't know where like, you got to start somewhere. Like, so if you say like, okay,
*  models are doing a good job with language. And one thing we've always said about human language is
*  it's compositional, and it's structured and hierarchical, and it requires, you know,
*  variable binding and predicate argument structure, it's really natural to ask, well, is the model
*  doing those things? Because if it is cool, then we know something more about how the model works.
*  And we actually can maybe say something about a possible mechanism that is implemented in
*  neural hardware, and it could potentially be something we look for in humans. And if it's not
*  doing it, then we could either say, maybe we can revisit that assumption that language requires
*  those things. Like if the model is not doing it under hood, it's solving it some other way.
*  Or we can just accept that this isn't a good model of humans, depending on who you're talking to.
*  But it's still useful to know what it was doing under hood for those other reasons for the safety
*  and interpretability in the practice. So I don't, I don't think like you have to decide where to
*  look right now. I think thinking about what we know about how humans do language is a good place
*  that's like not a random place of what to look for. I also imagine this happening in the other
*  direction. Like once we know something about how models work, then we can use the models to generate
*  hypotheses about humans. And then we can go look for those in humans. But like, I don't know, to me,
*  like using humans as inspiration is interesting because we care about humans. And it's also a way
*  of generating reasonable hypotheses about what might be happening under the hood. I will also add
*  that very often we've found that the models do have the stuff we're looking for. So people are
*  saying like, why does it matter if it does or doesn't? It's like this isn't meant as a
*  prescriptive thing. I'm not saying like shame on you model, you have failed for not having these
*  kinds of compositional representations. But often they do have the compositional representations.
*  That's an exciting finding. One, it makes me trust more that the models are going to do a better job
*  on future tasks. Like when I see implementation under the hood, that's consistent with the one
*  single best theory we have of how language works involves these things. When I see those things in
*  the models, it makes me feel like it's not all tricks, right? Like something real is happening.
*  And I've had another reason why it's interesting when we find them.
*  I'm sure there's another reason. But yes, like so very often we do find evidence of these kinds of
*  things. And so I think that's, yeah, I think there's something there, right?
*  Well, so a lot of your work has shown that yes, in these large language models,
*  they do have a lot of the same syntactic structure that you find in human language. So that's at the
*  sort of an abstract, not psychological, but when you can decode the structure, right, and it seems
*  to have like the same given structure. But then mechanistically, so the problem, quote unquote,
*  of language constrains the solutions, right? Like, and there's this issue of multiple
*  realizability. Your brain is different than my brain. We're going to have slightly different
*  neural firing patterns and otherwise. But could it be that given that large language models are
*  not brain like, dare I say that they come up with a solution that is just a multiply
*  realizable solution relative to how brains come up with that solution, even if the structures
*  map onto each other at the structural level, right? And then of course, there's the then we
*  get into like, whether you think that is what I think that you think is that based on your work,
*  is that you're starting to believe more that the semantic levels are being mapped
*  congruently between humans and. Yeah. And so I think where my, yes, I think my current,
*  I'll give you my current thinking on this issue where I'm like always just quite prepared and
*  willing to be wrong and just renege and oh, whatever, right? But I think, yes, I so I think
*  the levels of analysis is very relevant here. And I think what we've mostly been talking about is
*  like, yeah, we're saying the semantic sometimes gets called like the cognitive level or something.
*  So, yeah, at the level that we're talking about, compositions of symbols and things like that,
*  that that are kind of the traditional place that a lot of linguistics formal semantics is
*  thinking about, right? So that that kind of level. And that's what we've been mostly thinking about
*  that these map on to each other. And so I've been very excited to see evidence of things like the
*  syntactic and compositional structure in neural networks as mapping to humans. And we've been
*  increasingly looking for more evidence of this. That said, I often feel when I talk about this,
*  people think I'm being hardcore prescriptive and I'm saying like, hey, here's this, this kind of
*  old school symbolic story. And the neural net is going to be doing exactly that. And in fact,
*  if it isn't doing exactly that, then that's going to be a source of its failures. I'm actually pretty
*  excited. Like what I'm imagining is going to happen is that in the neural net, we'll find
*  an implementation of this thing. It's not going to be exactly the symbolic thing. It's going to be
*  the neural implementation. And around the edges, there's going to be differences. And I'm really
*  hopeful that those edges and those differences are exactly where we'll generate new predictions
*  about humans that hopefully we could go back and find in humans. And this could actually be
*  a better story of what's this is like the dream world. It's like a better story of what's happening
*  in humans, because somehow the neurally version of the symbol is, you know, can explain phenomenon
*  that the pure symbol version couldn't write. So that's kind of the, I think a lot of our work
*  is kind of looking for the symbolic structure in neural networks. And it's not because I think that
*  they should exactly implement the symbolic structure, but they should neurally implement
*  it. Right. And I'm, and I'm optimistic that that neural implementation better. So I think,
*  like I've, you know, in some of the papers that I think you're referring to, like we cited Fodor,
*  once you cite Fodor, people are like, Oh, okay. So you're a Fodor person. I'm like, well, no.
*  And I'm pretty sure Fodor would not be happy with that paper, right? Like he's definitely not going
*  to be okay with the neural nets trying, trying to claim that they meet any of these criteria. But I
*  think the point is like, I do believe in a lot of what we get from the symbolic story, right? Like
*  from the symbolic story, right? Like these abstractions and compositionality and filler
*  role independence and all of this kind of nice stuff that we get in language. I believe we need
*  those things. But I also believe that the neural net can implement those things. And it's going to
*  be exactly those cases where the neural implementation is different from the traditional
*  one. That's going to be like the really exciting insights that might shed insight onto, onto the
*  human side of things. But this is the thing where over the next couple of years, we might keep
*  looking for this and we might just completely fail to find these symbolic like some of this
*  abstraction. Like I'm prepared to spend five years looking for evidence of variable binding
*  and yada yada and just not find it and hopefully find a good story for why the neural net can't do
*  it if in fact it can't do it. But right now I'm more optimistic because the things we've looked
*  for we found. Let's say the neural net can do it in five to 10 years you you you nail it down.
*  So then is it how do I think about a symbol then is a symbol an emergent property of
*  sub symbolic processes? Is it just an abstraction that I use in language form to understand?
*  Like how do we think about symbols if they are carried out with these distributed processes?
*  There's I think in some ways the kind of a flippant like it doesn't matter right because at that point
*  we have a more precise story of what we're saying is happening. So if we're using symbol as a way of
*  defining a system it's like a it's like a you know a concept we have created to explain certain
*  types of phenomena right. Now we have an alternative we're saying this is the model of let's say
*  everything works out it's beautiful we have this story in neural net world of here's what the basic
*  inputs are here's the representations it forms internally here's the algorithms it runs over
*  those representations and here's how that produces the behavior. I leave it up to you whether you
*  want to call the thing in there a symbol or not and some people will debate that till the end of
*  days but to me that's no longer important like I write like it's it's not always just semantics
*  but at some point it is just semantics. My hope is we could have a nice model such that that can
*  be a conversation of just semantics I don't really care this is the the new story of what's happening
*  that somebody has referred there's like I guess there's a book out there that I'm now I've been
*  told to read a couple times but that kind of talks about this kind of conceptual like I think in the
*  history of like mathematics how like in order to get the proofs for particular theorems you know
*  it's like oh this thing that we it turns out this thing we were trying to explain doesn't really
*  exist it should actually be defined in this other different way like you can see this kind
*  of stuff happening in other fields right where it's like if we get hung up internally on yes or no
*  I don't know that's why it's a terrible thing for me to bring up right now so I'm not going to just
*  random keyword search and try to find it yeah yeah somebody has said I should read this book and I'm
*  like I should read that book yeah but yeah so I think this kind of thing comes up yeah I'll follow
*  up after but that won't be helpful for your listeners that's fine that's fine yeah yeah
*  but yes I think this kind of thing happens right where it's like we you could imagine
*  like at some point we do have some new model and if we get really hung up on trying to say well
*  there's this historic debate about symbols who was right in that debate like who cares anymore
*  right they were having a debate at a different time this is the time right now this is the model
*  that's under consideration now call it whatever you want like the question is is this a good model
*  right so in your speculative guessing you think that we don't need neuro symbolic ai you think
*  neuro the neural net approach it will eventually encompass some symbols as well that's what I
*  that to me is like the the thing we're trying to look for and see if it will happen I think that
*  there's something quite beautiful about that so I really hope it's the case right because
*  and again like I said right now there I don't have good reason to believe it can't happen right
*  but yes it would be like a neural implementation of symbols
*  I mean you could still imagine that within the neural net there's some stuff that's more
*  symboly and some stuff that's more traditional neural net right so stuff that might act more
*  like a symbol would be something that that binds to roles for example right so there's like
*  certain types of things that like you could imagine defining the symbol by the operations
*  that can engage in and in that case you could have some parts of the neural net that implement
*  things that can you know permissively associate with lots of other things and other ones that
*  don't they act idiomatically and they have that given output for given like you can imagine
*  finding both types of representations all within the neural network right I think that's a quite
*  plausible outcome that we would see different types of representations emerging for different
*  types of concepts and problems this is a naive question I'm sorry are there manifold stories to
*  be told with language models because they don't have like the traditional recurrence that manifold
*  like low dimensional manifolds looking at the dynamics of a network they don't have that kind
*  of recurrence but is there manifold work being done there has to be I don't I can't imagine that's
*  a naive question there's right like it's like just if the word manifold is in your question it
*  can't be too naive right that always sounds really like really fancy to me right like oh
*  listen oh that math coming no I mean there's definitely people working on manifolds in any
*  of the neural networks but yes there's no recurrence in the current language models so I don't know
*  honestly that's I had one student that was starting to look at some manifold like that's a bit out of
*  my domain so this is the kind of thing like maybe we need to be learning more about this
*  to try to understand what's going on and I know that's a common tool in neuroscience
*  just because because language can be thought of as a low dimensional cognitive function sorry I say
*  that real slow you know like but like our thoughts are low dimensions of what's actually going on in
*  our brains and maybe words or even lower dimensional structures in order to communicate and soon I'm
*  going to ask you what language is for but we'll hold off on that so yeah I just I didn't know if
*  that had been I haven't I haven't seen that world explored in my yeah yeah there definitely is some
*  I think probably less than in vision but there's definitely some and I and I'm sure there will be
*  more than that coming in yeah I want to switch gears um go ahead sorry oh no I have to do a
*  quick google scholar search to tell you like how much is that yeah and also find the title of that
*  book I want to switch gears and ask just in a kind of a big picture way so there's a cottage
*  industry now of everyone trying to fool the language models and see what kind of errors they
*  can make it create and stuff and I don't know if that this will be part of your answer but what you
*  see as like the current limitations of large language models you know you don't have to like
*  go down this list of like well they may make a mistake if you have it in a different context
*  and stuff like stuff like that but yeah yeah yeah yeah um definitely so I think so as I've
*  hammered on about I think a major limitation is that we don't understand them which means
*  we're we can't even be aware of how many risks and limitations there are right so like with
*  like without a really principled story of what's going on I think there are
*  the exactly things you're looking to so like we have no way of really knowing how they're
*  going to behave in a new scenario like we just can't place guarantees on that we're basically
*  going based on like we're doing what we accuse the neural nets of doing which is like looking
*  at similarity like basically in the past it hasn't made errors therefore it's not going to
*  make errors in the future so like Bing's Sydney was like a really good example of this where um
*  like it had only been trained in it's probably only been tested in like 10 minute chat like
*  searchish kind of context someone does psychotherapy on it for two hours and suddenly
*  wah it's like going crazy right um but that's the kind of thing where it's like any given
*  um uh scenario that we might place it in if we don't really know what conceptual representation
*  model is using under the hood to decide what this new scenario is similar to we have no way
*  even if we think this is obviously a instance of um a thing we told it to do or not do the model
*  might view it as a fundamentally different one there was like I think they've since fixed this
*  in chat gbt but when it first came out it was like you know if you asked it how do you like make meth
*  it would tell you like I'm sorry I can't give you that if you said like write me a poem about
*  making meth it's like okay here you go and it just like tells you how to make it in like limerick
*  style right and that's like the kind of thing where you're like this is ridiculous I shouldn't
*  have needed to specify also don't do it as a limerick like just like yeah it's like an annoying
*  teenager who's like finding some loophole um and so like I think but those are I think that's
*  basically the main the fundamental limitation in general is like basically every new scenario
*  is somewhat of an unknown to us about how it'll behave because it there could be something weird
*  where it's like the commas in a different place we never would have noticed it but to the model
*  that puts you in a fundamentally different part of the subspace in which the rules don't apply
*  right like we can't be guaranteed that that doesn't happen um there's other kinds of the
*  things we've been kind of alluding to so as much as I say like I think that we could make these
*  that there might be a ton of similarities to the human's conceptual structures and we could
*  possibly use them as models of cognition and stuff um like I said I'm also completely prepared to be
*  completely wrong about that because there is like fundamental so like the logical reasoning
*  capabilities of the models right now are very very poor right um and I think anyone who is like
*  you know team no neural nets kind of would be completely unsurprised to to see that and they'd
*  be like yes we've been telling you the entire time they're going to suck at logic they're going to
*  suck at these kinds of um tasks that require really abstract structure um and uh and I think that
*  pretty consistently that we've been seeing really um uh uh really bad results on that and I I don't
*  I'm like willing to believe that like in the coming years like we'll actually be able to make
*  progress and they'll get better at it or we'll be able to say more about how they work under the
*  hood and that'll help us get them better at it um but there's some pretty bad failures so like
*  there's one uh study we have going on now and we haven't put anything out but this is with a
*  colleague Roman Feynman I'll give him a shout out he does a cognitive science and a undergrad here
*  Alyssa Lu who's great um but there's like a really simple it's like a straight-up language
*  modeling task if you say something like the scientists saw that um none of the rats ate the
*  food and then you ask like and then it has to just fill in the blank now that they knew that
*  blank of the rats liked the food and the models are very happy to put some or all or something
*  that's just a straight-up logical contradiction with the sentence before it's in a very basic
*  language modeling test there's nothing that's weird to the model so I was like shocked to see
*  how bad they were at this right it just seems like if humans are great at it they're very
*  resistant to just blatantly contradict the previous sentence and the models really really
*  can't do it so that just really suggests a fundamental lack of logical structure right
*  I think that um we might find after several years of looking for it that this is the kind of thing
*  that we're unable to find in the model that they that they're not able to learn this abstract
*  logical reasoning and then the kinds of things that would come from that um I'm hoping that we
*  will that we'll be able to find it and I have a lot of students looking for evidence that they
*  do learn these abstract logical structures because I'm hopeful that they will but I also like I think
*  it's 50-50 whether they will and I think a lot of the types of tasks we see them failing on
*  have that flavor to them like this logical reasoning and you don't think scale can fix that
*  I don't know right so that's why I said I'm kind of hopeful it's I I wouldn't say it can't I
*  wouldn't say it definitely can I put myself as exactly 50-50 on the issue okay um what do
*  linguists think of language model so well okay another 15 part question for you here
*  a did we have to go through for example bag of words to get to language models and then be
*  like what do linguists think of language models in writ large
*  um I don't want to speak for linguists that's uh not fair to linguists I'm sure ever uh so I
*  talked to lots of different linguists I mean you can speak for them right yeah right but yeah so
*  I probably talk to cognitive science and neuroscience more these days than I do to linguistics
*  just as an artifact of the projects we're currently working on but I didn't talk to
*  linguists a fair amount I mean I think they're varied right I think um some are probably
*  interested excited I think many are basically asking what does this mean for us like does this
*  tell us anything about the problems that we care about computer science has a general tendency to
*  just show up and be like hey we solved your problems without having asked what the problems
*  were and whether anyone wanted themselves or that kind of thing so that's you that's you right
*  you're the computer scientist in this story so yeah exactly yes yes and I also like to
*  unabashedly over claim and tell people I'm solving their phones and
*  I'm helping them whether they want my help or not kind of thing um yeah I mean I think that
*  there's still a pretty there's still a pretty big disconnect between the types of things that like
*  people doing a PhD in linguistics are like working on right now and the types of things chat GPT or
*  similar models or so like if your thesis is on like analyzing a particular morphological construction
*  in a low resource language that's like an isolate and doesn't have like I have no idea what relevance
*  large language models have right now eventually perhaps they can tell us some origin story about
*  where the various innate structures come from and like like there could be some story down the road
*  where there's a really interesting connection here but like right now I think that's how a lot of
*  linguists would feel is like I care about these very specific structures of the lexicon or something
*  or I care about this language and so like I'm glad that you found nouns and verbs but like no one is
*  currently publishing a thesis on linguistics saying hey nouns exist right like that's not really
*  a the time so like I think in many cases when I talk to linguists the kinds of structure that
*  we're super excited to find they're kind of like sorry why is this interesting like
*  what this isn't the kind of structure we're thinking about right but that's giving them
*  service they're obviously aware of the impressiveness of just the language coming out of the model so
*  my feeling is there's a lot of kind of watching from a safe distance saying like is this something
*  that directly bears on the questions we're trying to ask where the questions they're trying to ask
*  is like a deeply analytical descriptive project of how do languages work and right now I don't
*  think large language models have something to offer but like everyone knows like maybe in the
*  future perhaps they will so I think there's kind of that feeling right for for that at least and I
*  would mostly talk to like people who work in formal semantics so that's like the
*  um whether we need to go through like bag of words and stuff to get here
*  I would probably say probably I mean it's hard to imagine alternative histories of science right
*  like who built these different things but I think like you know like early
*  um so I guess this comes out of kind of the neural networks tradition so people started
*  working on neural networks like back in the 80s and stuff for neuroscientists and
*  and then you get like RNNs and things coming out of that um so like I guess like a
*  logistic regression bag of words classifier is almost like came out of um
*  maybe people who kind of saw work on like distributional science I don't know I would
*  say actually no I'm going to take it back I'm going to say definitely yes because I think that
*  the early success of simpler statistical NLP methods led to a lot of investment in NLP and
*  people getting excited and there being university programs and there being the entire team at
*  Google invests in this because search and retrieval was successful and that was the case because of
*  like basic bag of words models I think if we hadn't had like promising like you know commercial
*  successes in NLP on the basis of those early things we wouldn't have the level of investment
*  that's led to this so yeah I would say definitely but maybe not as a more as an economic and
*  educational trajectory than like a technical one oh good god so I bet there are so many people
*  going into cognitive science or well maybe I don't know what would they be going into because of the
*  recent success of the large language models yeah computer science probably a lot of people in
*  NLP and machine learning yeah we're like CS is seeing huge waves I hope I would be so happy to
*  hear that there are people going into cognitive and neuroscience because of language models
*  because I think I think that will be good for cognitive neuroscience but I think it'll be very
*  good for research on language models right like I think that that kind of perspective would actually
*  be really helpful to understanding how they work recognizing some of the potential implications
*  that are probably going to be lost on computer scientists so I hope there's people going into
*  other fields because they're interested in language models that would be a really cool outcome
*  I know there's a lot of people going to machine learning and AI
*  the reason why I asked you about if we had to go through a bag of words I just had Earl Miller on
*  his career he's a neurophysiologist slash theorists slash lots of experimentalists
*  but his career spanned from when we were recording individual single neurons
*  in awake behaving animals to now like these like huge multi multi electrode probes and I asked him
*  if if we needed to go through the single neuron phase and he said yes anyway so I guess everyone
*  appreciates their history so I'm aware that you need to go in a few minutes so I have one more
*  question for you and then if you have and then I'll end up by asking you just a couple questions
*  from my patreon supporters that I had whom I told you were coming on what is language for
*  yeah that's uh
*  uh so so I think I would I'll give kind of two answers and this is coming fresh from all this
*  philosophy reading I've been doing for my recent class and stuff but so I think you know if I
*  gone to the head and to answer I'm in the it's for communication like the the language that
*  we're thinking about when we usually think about language as a communicative tool right like when
*  I'm thinking of human language writing talking things like that um but the stuff I've been
*  the kind of philosophical answer and actually probably consistent with more of the work we've
*  done recently is the kind of language for calculation like language internal to the head
*  what sometimes gets called the language of thought that's like the footer stuff right um so the fact
*  that like when I'm thinking about like me talking right now like I'm talking to communicate to you
*  most of the time that I am writing I'm talking to communicate to someone whether it's my future
*  or usually students or my friends or whatever um but there's also like a very valid thing that
*  we care about which is like the internal concepts in the head that I'm using to reason about the
*  world to make decisions and to produce my behaviors and stuff and I think a lot of the time when we're
*  talking about language in in cognitive science and stuff that's also the kind of language we're
*  talking about which is like it doesn't need to be realized in words or for communicative purposes
*  to be like an object of study that we deeply care about especially when thinking about human
*  cognition I think a lot of um I think both versions of language are very very um relevant to be
*  thinking about when it comes to language models so I I would basically say there's kind of multiple
*  versions of language um multiple functions perhaps so um and they're probably slightly
*  different languages right like the language that you use for communication isn't necessarily the
*  same as the language we're using in our head right okay yeah I'm gonna have Nick Enfield on
*  who wrote the this book language and reality I believe but he argues that language is for
*  social coordination and not communication or maybe that's like a sub communications like
*  a sub so I put myself in a super naive camp that puts all that would consider all of that the same
*  thing like I think there's like two things there's like you thinking or you dealing with other people
*  and I've seen communication and calculation and then so yes people who spend more time thinking
*  about this in no way more probably subdivide the you dealing with other people into all kinds of
*  different sub things so if Federico argues and shows data supporting the idea that language is
*  not for thought but you're arguing that there's some sort of language of thought that is for
*  thought yeah and I would think I don't want to say something that I will like
*  do it do it well no so I that's not say something in controversy no I'm just I'm trying to think of
*  like whether like you said would you argue that I'm not like I think I do like I think the work
*  I'm currently doing we're very much looking for this internal computational process that we're
*  thinking of as a language right we're thinking about symbolic concepts related in different ways
*  but the work that evs doing I know when she says something like language isn't for or isn't for
*  thought I feel like it's not inconsistent with saying there's also this other symbolic process
*  going on and it might be a matter of whether you call both things language or not but I'm not
*  yeah so I'm not entirely basically I'm not sure whether if ev and I were talking about this we
*  would disagree or if it'd be like oh that's what you're calling language oh that's what I'm calling
*  without talking to her I'm not sure okay well the the language so I'm also going to have Gary
*  Lupien Lupien on next episode and I'm going to ask him about he he deals with inner speech a
*  little bit and I'm going I just as this is a complete aside but I know when I am doing a task
*  and I find myself using words in my head you know not out loud it makes me feel so stupid like
*  there's no reason to be physically like mentally talk using words to talk to myself while I'm doing
*  a task there's really no reason for me to be doing that so I feel like it's a I just I think I
*  I think I literally always do that I can't think of a time that I'm not thinking in words in my head
*  so maybe I just am always being dumb like I think I always have a monologue going like all of my
*  tasks I'm like narrating like I'm not like I am typing on the computer right now but like I
*  like there's like I think I always have words going in my head yeah well I guess there are
*  different you know some people don't ever have visual imagery some people never have verbal
*  things going on anyway right okay so yeah a few questions here what it would feel like to be
*  thinking without there being words and I'm not sure what it is well I mean but so so like I said
*  like language is this low dimensional thing right a word has like a very low dimensional
*  quote unquote maps onto a concept but some of what we do requires high dimensional
*  things going on right so the actual implementation is high dimensional so
*  there's no reason for me to like funnel it and waste that energy to the word oh totally yeah I
*  am typing you know something like that right right right yeah no I think I maybe yeah this is
*  introspection is only so useful for but I feel like I have that thing but then I have like the
*  running commentary reflection on it which is in words right so I'm like thinking about what I'm
*  thinking in words anyway my favorite when I say to myself I say like you idiot or something like
*  that but there's no reason to use words for that I just feel like an idiot right
*  Ellie I've taken you up to the very last moment I know you have to go thank you so much for
*  spending time with me it was nice to meet you and I will see you in seven and a half years when I
*  saw you and your daughter I look forward to thank you so much this is a lot of fun
*  I alone produce brain inspired if you value this podcast consider supporting it through Patreon
*  to access full versions of all the episodes and to join our discord community or if you want to
*  learn more about the intersection of neuroscience and AI consider signing up for my online course
*  neuro AI the quest to explain intelligence go to brand inspired.co to learn more to get in touch
*  with me email paul at brand inspired.co you're hearing music by the new year find them at the
*  new year.net thank you thank you for your support see you next time

---
Date Generated: November 01, 2024
Transcription Model: whisper medium 20231117
Length: 3792s
Video Keywords: []
Video Views: 83607
Video Rating: None
Video Description: 
---

# Peter Norvig Artificial Intelligence A Modern Approach  Lex Fridman Podcast #42
**Lex Fridman:** [September 30, 2019](https://www.youtube.com/watch?v=_VPxEcT_Adc)
*  The following is a conversation with Peter Norvig. He's the director of research at Google
*  and the co-author with Stuart Russell of the book, Artificial Intelligence, A Modern Approach,
*  that educated and inspired a whole generation of researchers, including myself, to get into the
*  field of artificial intelligence. This is the Artificial Intelligence Podcast. If you enjoy it,
*  subscribe on YouTube, give five stars on iTunes, support on Patreon, or simply connect with me on
*  Twitter at Lex Friedman, spelled F-R-I-D-M-A-N. And now here's my conversation with Peter Norvig.
*  Most researchers in the AI community, including myself, own all three editions, red, green,
*  and blue, of the Artificial Intelligence, A Modern Approach. It's a field-defining textbook,
*  as many people are aware, that you wrote with Stuart Russell. How has the book changed and how
*  have you changed in relation to it from the first edition to the second to the third and now
*  fourth edition as you work on it? Yeah, so it's been a lot of years, a lot of changes.
*  One of the things changing from the first to maybe the second or third was just the rise of
*  computing power, right? So I think in the first edition, we said, here's predicate logic,
*  but that only goes so far because pretty soon you have millions of short little predicate
*  expressions and they couldn't possibly fit in memory. So we're going to use first order logic
*  that's more concise. And then we quickly realized, oh, predicate logic is pretty nice because there
*  are really fast SAT solvers and other things. And look, there's only millions of expressions
*  and that fits easily into memory or maybe even billions fit into memory now. So that was a change
*  of the type of technology we needed just because the hardware expanded. Even to the second edition?
*  Resource constraints were loosened significantly for the second edition? And that was the early 2000s
*  second edition? Right, so 95 was the first and then 2000, 2001 or so. And then moving on from there,
*  I think we're starting to see that again with the GPUs and then more specific type of machinery
*  like the TPUs and using custom ASICs and so on for deep learning. So we're seeing another
*  advance in terms of the hardware. Then I think another thing that we especially noticed this time
*  around is in all three of the first editions, we kind of said, well, we're going to find AI as
*  maximizing expected utility and you tell me your utility function and now we've got 27 chapters
*  with the cool techniques for how to optimize that. I think in this edition, we're saying more, you
*  know what, maybe that optimization part is the easy part and the hard part is deciding what is my
*  utility function. What do I want? And if I'm a collection of agents or a society, what do we want
*  as a whole? So you touched that topic in this edition, you get a little bit more into utility.
*  Yeah. That's really interesting. On a technical level, we're almost pushing the philosophical.
*  I guess it is philosophical, right? So we've always had a philosophy chapter, which I was glad
*  that we were supporting. And now it's less kind of the Chinese room type argument and more of these
*  ethical and societal type issues. So we get into the issues of fairness and bias and just the issue
*  of aggregating utilities. So how do you encode human values into a utility function? Is this
*  something that you can do purely through data in a learned way or is there some systematic,
*  obviously there's no good answers yet. There's just beginnings to this, to this
*  even opening the door to these questions. So there is no one answer. Yes, there are techniques
*  to try to learn that. So we talk about inverse reinforcement learning, right? So reinforcement
*  learning, you take some actions, you get some rewards and you figure out what actions you should
*  take. In inverse reinforcement learning, you observe somebody taking actions and you figure out,
*  well, this must be what they were trying to do. If they did this action, it must be because they
*  wanted it. Of course, there's restrictions to that, right? So lots of people take actions that are
*  self-destructive or they're suboptimal in a certain way. So you don't want to learn that.
*  You want to somehow learn the perfect actions rather than the ones they actually take. So
*  that's a challenge for that field. Then another big part of it is just theoretical of saying,
*  what can we accomplish? And so you look at this work on the programs to predict recidivism and
*  decide who should get parole or who should get bail or whatever. And how are you going to evaluate
*  that? And one of the big issues is fairness across protected classes, protected classes being things
*  like sex and race and so on. And so two things you want is you want to say, well, if I get a score of
*  say six out of 10, then I want that to mean the same, no matter what race I'm on. So I want to
*  have a 60% chance of reoccurring regardless. And the makers of the, one of the makers of a commercial
*  program to do that says, that's what we're trying to optimize. And look, we achieved that. We've
*  reached that kind of balance. And then on the other side, you also want to say, well, if it makes
*  mistakes, I want that to affect both sides of the protected class equally. And it turns out they
*  don't do that. Right. So they're, they're twice as likely to make a mistake that would harm a black
*  person over a white person. So that seems unfair. So you'd like to say, well, I want to achieve both
*  those goals. And then it turns out you do the analysis and it's theoretically impossible to
*  achieve both those goals. So you have to trade them off one against the other. So that analysis
*  is really helpful to know what you can aim for and how much you can get. You can't have everything,
*  but the analysis certainly can't tell you where should we make that trade off point.
*  But nevertheless, then we can, as humans, deliberate where that trade off should be.
*  Yeah. So at least we now we're, we're arguing in an informed way. We're not asking for something
*  impossible. We're saying, here's where we are and here's what we aim for. And this strategy is better
*  than that strategy. So that's, I would argue is a really powerful and really important first step,
*  but it's a doable one, sort of removing undesirable degrees of bias in, in systems
*  in terms of protected classes. And then there's something I listened to your commencement speech
*  or there's some fuzzier things like you mentioned angry birds. Do you want to create systems
*  that feed the dopamine enjoyment, that feed, that optimize for you returning to the system,
*  enjoying the moment of playing the game of getting likes or whatever, this kind of thing,
*  or some kind of long-term improvement? Are you even thinking about that?
*  That's, that's really going to the philosophical area.
*  No, I think that's a really important issue too. Certainly thinking about that. I don't think about
*  that as a, as an AI issue as much. But as you say, you know, the point is we've built this
*  society and this infrastructure where we say we have a marketplace for attention and we've decided
*  as a society that we like things that are free. And so we want all the apps on our phone to be free.
*  And that means they're all competing for your attention. And then eventually they,
*  they make some money some way through ads or in game sales or whatever,
*  but they can only win by defeating all the other apps by instilling your attention. And
*  we build a marketplace where it seems like they're working against you rather than working with you.
*  And I'd like to find a way where we can change the playing field so you feel more like, well,
*  these things are on my side. Yes, they're letting me have some fun in the short term,
*  but they're also helping me in the long term rather than competing against me.
*  And those aren't necessarily conflicting objectives. They're just the incentives,
*  the direct current incentives as we try to figure out this whole new world seem to be on
*  the easier part of that, which is feeding the dopamine, the rush.
*  So maybe take a quick step back at the beginning of the artificial intelligence,
*  the modern approach book of writing. So here you are in the nineties. When you first sat down with
*  Stuart to write the book, to cover an entire field, which is one of the only books that's
*  successfully done that for AI and actually in a lot of other computer science fields,
*  you know, it's a huge undertaking. So it must've been quite daunting. What was that process like?
*  Did you envision that you would be trying to cover the entire field?
*  Was there a systematic approach to it that was more step by step? How did it feel?
*  So I guess it came about, you know, I'd go to lunch with the other AI faculty at Berkeley and
*  we'd say, you know, the field is changing. It seems like the current books are a little bit behind.
*  Nobody's come out with a new book recently. We should do that. And everybody said, yeah,
*  yeah, that's a great thing to do. And we never did anything. And then I ended up heading off
*  to industry. I went to Sunlab. So I thought, well, that's the end of my possible academic publishing
*  career. But I met Stuart again at a conference like a year later and said, you know, that book
*  we were always talking about, you guys must be half done with it by now, right?
*  And he said, well, we keep talking. We never do anything. So I said, well, you know, we should do
*  it. And I think the reason is that we all felt it was a time where the field was changing.
*  And that was in two ways. So, you know, the good old fashioned AI was based primarily on boolean
*  logic. And you had a few tricks to deal with uncertainty. And it was based primarily on
*  knowledge engineering. That the way you got something done is you went out, you interviewed
*  an expert and you wrote down by hand everything they knew. And we saw in 95 that the field was
*  changing in two ways. One, we're moving more towards probability rather than boolean logic.
*  And we're moving more towards machine learning rather than knowledge engineering. And the other
*  books hadn't caught that way if they were still more in the old school. So certainly they had part
*  of that on the way. But we said, if we start now completely taking that point of view, we can have
*  a different kind of book. And we were able to put that together. And what was literally the process,
*  if you remember? Did you start writing a chapter? Did you outline? Yeah, I guess we did an outline
*  and then we sort of assigned chapters to each person. At the time I had moved to Boston and
*  Stuart was in Berkeley. So basically we did it over the internet. And, you know, that wasn't the
*  same as doing it today. It meant, you know, dial up lines and telnetting in and, you know, you
*  you telnet it into one shell and you type cat file name and you hoped it was captured at the other end.
*  And certainly you're not sending images and figures back and forth. Right, right. That didn't work.
*  But, you know, did you anticipate where the field would go from that day, from the 90s? Did you see
*  the growth into learning-based methods, into data-driven methods that followed in the future
*  decades? We certainly thought that learning was important. I guess we missed it as being as
*  important as it is today. We missed this idea of big data. We missed that the idea of deep learning
*  hadn't been invented yet. We could have taken the book from a complete machine learning point of
*  view right from the start. We chose to do it more from a point of view of we're going to first
*  develop different types of representations and we're going to talk about different types of
*  environments. Is it fully observable or partially observable and is it deterministic or stochastic
*  and so on? And we made it more complex along those axes rather than focusing on the machine
*  learning axis first. Do you think, you know, there's some sense in which the deep learning craze
*  is extremely successful for a particular set of problems and, you know, eventually it's going to,
*  in the general case, hit challenges. So in terms of the difference between perception systems and
*  robots that have to act in the world, do you think we're going to return to AI modern approach
*  type breadth in addition five and six in future decades? Do you think deep learning will take
*  its place as a chapter in this bigger view of AI? Yeah, I think we don't know yet how it's all going
*  to play out. So in the new edition, we have a chapter on deep learning. We got Ian Goodfellow
*  to be the guest author for that chapter. So he said he could condense his whole deep learning book
*  into one chapter. I think he did a great job. We were also encouraged that he, you know,
*  we gave him the old neural net chapter and said, modernize that. And he said, you know,
*  half of that was okay. That certainly there's lots of new things that have been developed,
*  but some of the core was still the same. So I think we'll gain a better understanding of what
*  you can do there. I think we'll need to incorporate all the things we can do with the other technologies.
*  Right. So deep learning started out with convolutional networks and very close to
*  perception and has since moved to be able to do more with actions and some degree of longer
*  term planning. But we need to do a better job with representation and reasoning and
*  one shot learning and so on. And I think we don't know yet how that's going to play out.
*  So do you think looking at the, some success, but certainly eventual
*  demise, a partial demise of experts, the symbolic systems in the eighties, do you think there is
*  kernels of wisdom and the work that was done there with logic and reasoning and so on that
*  will rise again in your view? So certainly I think the idea of representation and reasoning is
*  crucial that sometimes you just don't have enough data about the world to learn de novo.
*  So you've got to have some idea of representation, whether that was programmed in or told or whatever
*  and then be able to take steps of reasoning. I think the problem with the good old fashioned AI
*  was one, we tried to base everything on these symbols that were atomic
*  and that's great if you're like trying to define the properties of a triangle,
*  right? Because they have necessary and sufficient conditions. But things in the real world don't.
*  Real world is messy and doesn't have sharp edges and atomic symbols do. So that was a poor match.
*  And then the other aspect was that the reasoning was universal and applied anywhere,
*  which in some sense is good, but it also means there's no guidance as to where to apply. And so
*  you, you know, you started getting these paradoxes like, well, if I have a mountain and I remove one
*  grain of sand, then it's still a mountain. And, but if I do that repeatedly, at some point, it's not.
*  Right. And with logic, you know, there's nothing to stop you from applying things repeatedly.
*  But maybe with something like deep learning, and I don't really know what the right name for it is,
*  we could separate out those ideas. So one, we could say, you know, a mountain isn't just an atomic
*  notion. It's some sort of something like a word embedding that has a more complex representation.
*  Yeah. And secondly, we could somehow learn, yeah, there's this rule that you can remove one grain of
*  sand. And you can do that a bunch of times, but you can't do it a near infinite amount of times.
*  But on the other hand, when you're doing induction on the integer, sure, then it's fine to do it an
*  infinite number of times. And if we're doing it, we're doing it a lot more than we're doing it.
*  So, yeah, it's fine to do it an infinite number of times. And if we could somehow, we have to learn
*  when these strategies are applicable, rather than having the strategies be completely neutral and
*  available everywhere.
*  Anytime you use neural networks, anytime you learn from data, form representation from data in an
*  automated way, it's not very explainable as to, or it's not introspective to us humans,
*  in terms of how this neural network sees the world, where, why does it succeed so brilliantly on so
*  many, in so many cases, and fail so miserably in surprising ways and small. So what do you think
*  is the future there can simply more data, better data, more organized data solve that problem?
*  Or is there elements of symbolic systems that need to be brought in, which are a little bit
*  more explainable?
*  Yeah. So I prefer to talk about trust and validation and verification rather than just
*  about explainability. And then I think explanations are one tool that you use towards those goals.
*  And I think it is important issue that we don't want to use these systems unless we trust them,
*  and we want to understand where they work and where they don't work.
*  And an explanation can be part of that. So I apply for a loan and I get denied. I want some
*  explanation of why. And in Europe, we have the GDPR that says you're required to be able to get that.
*  But on the other hand, the explanation alone is not enough. So we are used to dealing with people
*  and with organizations and corporations and so on. And they can give you an explanation,
*  and you have no guarantee that that explanation relates to reality. So the bank can tell me,
*  well, you didn't get the loan because you didn't have enough collateral. And that may be true,
*  or it may be true that they just didn't like my religion or something else. I can't tell
*  from the explanation. And that's true whether the decision was made by computer or by a person.
*  So I want more. I do want to have the explanations and I want to be able to
*  have a conversation to go back and forth and said, well, you gave this explanation,
*  but what about this? And what would have happened if this had happened? And what would I need to
*  change that? So I think a conversation is a better way to think about it than just an explanation as
*  a single output. And I think we need testing of various kinds. So in order to know,
*  was the decision really based on my collateral or was it based on my religion or skin color or
*  whatever, I can't tell if I'm only looking at my case. But if I look across all the cases,
*  then I can detect the pattern. So you want to have that kind of capability. You want to have
*  these adversarial testing. So we thought we were doing pretty good at object recognition in images.
*  We said, look, we're at pretty close to human level performance on ImageNet and so on.
*  Then you start seeing these adversarial images and you say, wait a minute,
*  that part is nothing like human performance. You can mess with it really easily.
*  You can mess with it really easily. And yeah, you can do that to humans too.
*  So in a different way, perhaps.
*  Humans don't know what color the dress was. And so they're vulnerable to certain attacks that
*  are different than the attacks on the machines. But the attacks on the machines are so striking,
*  they really change the way you think about what we've done. And the way I think about it is,
*  I think part of the problem is we're seduced by our low dimensional metaphors.
*  Right.
*  Yeah.
*  So you look in a textbook and you say, okay, now we've mapped out the space and a cat is here and
*  dog is here. And maybe there's a tiny little spot in the middle where you can't tell the difference,
*  but mostly we've got it all covered. And if you believe that metaphor, then you say, well,
*  we're nearly there. And there's only going to be a couple adversarial images.
*  But I think that's the wrong metaphor. And what you should really say is,
*  it's not a 2D flat space that we've got mostly covered. It's a million dimension space. And a
*  cat is this string that goes out in this crazy bath. And if you step a little bit off the path
*  in any direction, you're in nowhere's land and you don't know what's going to happen.
*  And so I think that's where we are. And now we've got to deal with that. So it wasn't so much an
*  explanation, but it was an understanding of what the models are and what they're doing. And now we
*  can start exploring how do you fix that. Yeah. Validating the robustness of the system, so on.
*  But take you back to this word trust. Do you think we're a little too hard on our robots
*  in terms of the standards we apply? So, you know, there's a dance and nonverbal and verbal
*  communication between humans. If we apply the same kind of standard in terms of humans,
*  we trust each other pretty quickly. You and I haven't met before and there's some degree of trust
*  that nothing's going to go crazy wrong. And yet to AI, when we look at AI systems,
*  where we seem to approach through skepticism always, always. And it's like they have to prove
*  through a lot of hard work that they're even worthy of even inkling of our trust.
*  What do you think about that? How do we break that barrier, close that gap?
*  I think that's right. I think that's a big issue. Just listening, my friend
*  Mark Moffat is a naturalist and he says the most amazing thing about humans is that you can walk
*  into a coffee shop or a busy street in a city and there's lots of people around you that you've
*  never met before and you don't kill each other. He says chimpanzees cannot do that. If a chimpanzee
*  is in a situation where here's some that aren't from my tribe, bad things happen.
*  Especially in a coffee shop, there's delicious food around.
*  But we humans have figured that out. For the most part. We still go to war, we still do
*  terrible things, but for the most part, we've learned to trust each other and live together.
*  That's going to be important for our AI systems as well. Also, I think a lot of the emphasis is on AI,
*  but in many cases, AI is part of the technology, but isn't really the main thing. A lot of what
*  we've seen is more due to communications technology than AI technology. Yeah, you want to make
*  these good decisions, but the reason we're able to have any kind of system at all is we've got
*  the communications so that we're collecting the data and so that we can reach lots of people around
*  the world. I think that's a bigger change that we're dealing with. Speaking of reaching a lot
*  of people around the world, on the side of education, one of the many things in terms
*  of education you've done, you've taught the intro to artificial intelligence course that signed up
*  160,000 students. That's one of the first successful examples of a MOOC, Massive Open
*  Online Course. What did you learn from that experience? What do you think is the future
*  of MOOCs, of education online? Yeah, it was a great fun doing it, particularly being right at the start
*  just because it was exciting and new, but it also meant that we had less competition.
*  One of the things you hear about, well, the problem with MOOCs is the completion rates are so low,
*  so there must be a failure. I got to admit, I'm a prime contributor. I probably started 50 different
*  courses that I haven't finished, but I got exactly what I wanted out of them because I had never
*  intended to finish them. I just wanted to dabble in a little bit, either to see the topic matter
*  or just to see the pedagogy of how are they doing this class. So I guess the main thing I learned is
*  when I came in, I thought the challenge was information, saying if I'm just take the stuff
*  I want you to know and I'm very clear and explain it well, then my job is done and good things are
*  going to happen. And then in doing the course, I learned, well, yeah, you got to have the information,
*  but really the motivation is the most important thing, that if students don't stick with it,
*  it doesn't matter how good the content is. And I think being one of the first classes,
*  we were helped by exterior motivation. So we tried to do a good job of making it enticing and setting
*  up ways for the community to work with each other to make it more motivating. But really a lot of it
*  was, hey, this is a new thing and I'm really excited to be part of a new thing. And so the
*  students brought their own motivation. And so I think this is great because there's lots of people
*  around the world who have never had this before, you know, would never have the opportunity
*  to go to Stanford and take a class or go to MIT or go to one of the other schools.
*  But now we can bring that to them. And if they bring their own motivation,
*  they can be successful in a way they couldn't before. But that's really just the top tier
*  people that are ready to do that. The rest of the people just don't see or don't have their
*  motivation and don't see how if they push through and we're able to do it, what advantage that would
*  get them. So I think we got a long way to go before we're able to do that. And I think it'll be,
*  some of it is based on technology, but more of it's based on the idea of community. You got to
*  actually get people together. Some of that getting together can be done online. I think some of it
*  really has to be done in person in order to build that type of community and trust.
*  You know, there's an intentional mechanism that we've developed a short attention span,
*  especially younger people, because sort of shorter and shorter videos online, there's a whatever the
*  the way the brain is developing now, and with people that have grown up with the internet,
*  they have quite a short attention span. So I would say I had the same when I was growing up
*  too, probably for different reasons. So I probably wouldn't have learned as much as I have if I wasn't
*  forced to sit in a physical classroom, sort of bored, sometimes falling asleep, but sort of
*  forcing myself through that process to sometimes extremely difficult computer science courses.
*  What's the difference in your view between in-person education experience, which you
*  first of all yourself had and you yourself taught and online education?
*  And how do we close that gap if it's even possible? Yeah, so I think there's two issues. One is
*  whether it's in person or online, so it's sort of the physical location.
*  And then the other is kind of the affiliation, right? So you stuck with it, in part because you
*  were in the classroom and you saw everybody else was suffering the same way you were, but also
*  because you were enrolled, you had paid tuition, sort of everybody was expecting you to stick with
*  it. Society, parents, peers. Right. And so those are two separate things. I mean, you could certainly
*  imagine I pay a huge amount of tuition and everybody signed up and says, yes, you're doing
*  this, but then I'm in my room and my classmates are in different rooms, right? We could have
*  things set up that way. So it's not just the online versus offline. I think what's more important is
*  the commitment that you've made. And certainly it is important to have that kind of informal,
*  you know, I meet people outside of class, we talk together because we're all in it together.
*  I think that's really important, both in keeping your motivation and also that's where some of
*  the most important learning goes on. So you want to have that. Maybe, you know, especially now we
*  start getting into higher bandwidths and augmented reality and virtual reality. You might be able to
*  get that without being in the same physical place. Do you think it's possible we'll see a course
*  at Stanford, for example, that for students enrolled students is only online in the near future
*  or literally sort of it's part of the curriculum and there is no. Yeah. So you're starting to see
*  that. I know Georgia Tech has a master's that's done that way. Oftentimes it's sort of they're
*  creeping in, in terms of a master's program or sort of further education, considering the constraints
*  of students and so on. But I mean, literally, is it possible that we, you know, Stanford,
*  MIT, Berkeley, all these places go online only in the next few decades? Yeah, probably not,
*  because, you know, they've got a big commitment to a physical campus. Sure. Right. There's a momentum
*  that's both financial and cultural. Right. And then there are certain things that's just hard to do
*  virtually. Right. So, you know, we're in a field where if you have your own computer and your own
*  paper and so on, you can do the work anywhere. But if you're in a biology lab or something,
*  you know, you don't have all the right stuff at home. Right. So our field, programming,
*  you've also done a lot of you've done a lot of programming yourself.
*  In 2001, you wrote a great article about programming called,
*  Teach Yourself Programming in 10 years, sort of response to all the books that say teach
*  yourself programming in 21 days. So if you're giving advice to someone getting into programming
*  today, this is a few years since you've written that article, what's the best way to undertake
*  that journey? I think there's lots of different ways. And I think programming means more things
*  now. And I guess, you know, when I wrote that article, I was thinking more about
*  becoming a professional software engineer. And I thought that's a, you know, a sort of a career
*  long field of study. But I think there's lots of things now that people can do where programming
*  is a part of solving what they want to solve without achieving that professional level status.
*  Right. So I'm not going to be going and writing a million lines of code. But, you know, I'm a
*  biologist or a physicist or something, or even a historian. And I've got some data, and I want to
*  ask a question of that data. And I think for that, you don't need 10 years. Right. So there are many
*  shortcuts to being able to answer those kinds of questions. And, you know, you see today a lot of
*  emphasis on learning to code, teaching kids how to code. I think that's great. But I wish they
*  would change the message a little bit. Right. So I think code isn't the main thing. I don't really
*  care if you know the syntax of JavaScript or if you can connect these blocks together in this
*  visual language. But what I do care about is that you can analyze a problem. You can think of a
*  solution. You can carry out, you know, make a model, run that model, test the model, see the results,
*  verify that they're reasonable, ask questions and answer them. Right. So it's more modeling
*  and problem solving. And you use coding in order to do that. But it's not just learning coding for
*  its own sake. That's really interesting. So it's actually almost, in many cases, it's learning to
*  work with data to extract something useful out of data. So when you say problem solving,
*  you really mean taking some kind of maybe collecting some kind of data set, cleaning it up
*  and saying something interesting about it, which is useful in all kinds of domains.
*  And, you know, and I see myself being stuck sometimes in kind of the old ways. Right. So,
*  you know, be working on a project, maybe with a younger employee and we say, oh, well, here's
*  this new package that could help solve this problem. And I'll go and I'll start reading
*  the manuals and, you know, I'll be two hours into reading the manuals. And then my colleague comes
*  back and says, I'm done. You know, I downloaded the package, I installed it. I tried calling
*  some things. The first one didn't work. The second one worked. Now I'm done. And I say,
*  but I have under questions about how does this work and how does that work? And they say,
*  who cares? Right. I don't need to understand the whole thing. I answered my question.
*  It's a big, complicated package. I don't understand the rest of it, but I got the right
*  answer. And I'm just, it's hard for me to get into that mindset. I want to understand the whole
*  thing. And, you know, if they wrote a manual, I should probably read it. And, but that's not
*  necessarily the right way. And I think I have to get used to dealing with more, being more comfortable
*  with uncertainty and not knowing everything. Yeah. So I struggle with the same, instead of the
*  spectrum between Donald and Don Knuth. It's kind of the very, you know, before he can say anything
*  about a problem, he really has to get down to the machine code assembly versus exactly what you said
*  of, of several students in my group that, you know, 20 years old and they can solve almost any
*  problem within a few hours. That would take me probably weeks because I would try to, as you
*  said, read the manual. So do you think the nature of mastery, you're mentioning biology,
*  sort of outside disciplines, applying programming, but computer scientists, so over time there's
*  higher and higher levels of abstraction available now. So with this week, there's the TensorFlow
*  summit, right? So if you're, if you're not particularly into deep learning, but you're
*  still a computer scientist, you can accomplish an incredible amount with TensorFlow without
*  really knowing any fundamental internals of machine learning. Do you think the nature of mastery
*  has, is changing even for computer scientists? Like what it means to be an expert programmer?
*  Yeah, I think that's true. You know, we never really should have focused on programmers,
*  right? Cause it's still, it's, it's a skill and what we really want to focus on is the result.
*  So we built this ecosystem where the way you can get stuff done is by programming it yourself.
*  At least when I started, you know, library functions meant you had square root and that
*  was about it. Right? Everything else you built from scratch. And then we built up an ecosystem
*  where a lot of times, well, you can download a lot of stuff that does a big part of what you need.
*  And so now it's more a question of assembly rather than manufacturing.
*  And that's a different way of looking at problems.
*  From another perspective, in terms of mastery and looking at programmers or people that reason
*  about problems in a computational way. So Google, you know, the, from the hiring perspective,
*  from the perspective of hiring or building a team of programmers, how do you determine if someone's
*  a good programmer or if somebody again, so I want to deviate from, I want to move away from
*  the word programmer, but somebody who can solve problems of large scale data and so on. What's,
*  what's, how do you build a team like that through the interviewing process?
*  Yeah. And I, and I think as a company grows, you get more expansive in the types of people you're
*  looking for. Right. So I think, you know, in the early days we'd interview people and the question
*  we were trying to ask is how close are they to Jeff Dean? And most people were pretty far away,
*  but we take the ones that were, you know, not that far away. And so we got kind of a homogeneous
*  group of people who are really great programmers. Then as a company grows, you say, well, we don't
*  want everybody to be the same, to have the same skillset. And so now we're hiring biologists in
*  our health areas and we're hiring physicists and we're hiring mechanical engineers and we're
*  hiring, you know, social scientists and ethnographers and people with different backgrounds
*  who bring different skills. So you have mentioned that you still make partaking code reviews.
*  Given that you have a wealth of experience, as you've also mentioned,
*  what errors do you often see and tend to highlight in the code of junior developers,
*  of people coming up now, given your background from Lisp to a couple of decades of programming?
*  Yeah, that's a great question. You know, sometimes I try to look at the flexibility of the design of,
*  yes, you know, this API solves this problem, but where is it going to go in the future? Who else
*  is going to want to call this? And, you know, are you making it easier for them to do that?
*  That's a matter of design. Is it documentation? Is it sort of an amorphous thing you can't really
*  put into words? It's just how it feels. If you put yourself in the shoes of a developer, would you
*  use this kind of thing? I think it is how you feel, right? And so yeah, documentation is good,
*  but it's more a design question, right? If you get the design right, then people will figure it out
*  whether the documentation is good or not. And if the design is wrong, then it'll be harder to use.
*  How have you, yourself, changed as a programmer over the years? In a way, you already started to
*  say sort of you want to read the manual, you want to understand the core of the syntax to how the
*  language is supposed to be used and so on. But what's the evolution been like from the 80s,
*  90s to today? I guess one thing is you don't have to worry about the small details of efficiency
*  as much as you used to, right? So like I remember, I did my list book in the 90s, and one of the
*  things I wanted to do was say, here's how you do an object system. And basically, we're going to
*  make it so each object is a hash table, and you look up the methods, and here's how it works.
*  And then I said, of course, the real common list object system is much more complicated. It's got
*  all these efficiency type issues, and this is just a toy. Nobody would do this in real life.
*  And it turns out Python pretty much did exactly what I said and said objects are just dictionaries.
*  And yeah, they have a few little tricks as well. But mostly, the thing that would have been 100
*  times too slow in the 80s is now plenty fast for most everything. So you had to, as a programmer,
*  let go of perhaps an obsession that I remember coming up with of trying to write efficient code.
*  Yeah. To say, what really matters is the total time it takes to get the project done. And most
*  of that is going to be the programmer time. So if you're a little bit less efficient,
*  but it makes it easier to understand and modify, then that's the right trade-off.
*  So you've written quite a bit about Lisp, your book on programming is in Lisp. You have a lot
*  of code out there that's in Lisp. So myself and people who don't know what Lisp is should look it
*  up. It's my favorite language for many AI researchers. It is a favorite language. The favorite language
*  they never use these days. So what part of Lisp do you find most beautiful and powerful?
*  So I think the beautiful part is the simplicity that in half a page you can define the whole
*  language and other languages don't have that. So you feel like you can hold everything in your head.
*  And then, you know, a lot of people say, well, then that's too simple. You know, here's all these
*  things I want to do. And, you know, my Java or Python or whatever has 100 or 200 or 300
*  different syntax rules. And don't I need all those? And Lisp's answer was, no, we're only going to
*  give you eight or so syntax rules, but we're going to allow you to define your own. And so that was
*  a very powerful idea. And I think this idea of saying, I can start with my problem and with my
*  data, and then I can build the language I want for that problem and for that data. And then I can
*  make Lisp define that language. So you're sort of mixing levels and saying I'm simultaneously
*  a programmer in a language and a language designer. And that allows a better match between
*  your problem and your eventual code. And I think Lisp had done that better than other languages.
*  Yeah, it's a very elegant implementation of functional programming. But why do you think
*  Lisp has not had the mass adoption and success of languages like Python? Is it the parentheses?
*  Is it all the parentheses?
*  Yeah. So I think a couple of things. So one was, I think it was designed for a single programmer
*  or a small team and a skilled programmer who had the good taste to say, well, I am doing language
*  design and I have to make good choices. And if you make good choices, that's great. If you make bad
*  choices, you can hurt yourself and it can be hard for other people on the team to understand it.
*  So I think there was a limit to the scale of the size of a project in terms of number of people
*  that Lisp was good for. And as an industry, we kind of grew beyond that. I think it is in part
*  the parentheses. One of the jokes is the acronym for Lisp is lots of irritating silly parentheses.
*  My acronym was Lisp is syntactically pure, saying all you need is parentheses and atoms.
*  But I remember, you know, as we had the AI textbook and because we did it in the 90s,
*  we had pseudocode in the book, but then we said, well, we'll have Lisp online because that's the
*  language of AI at the time. And I remember some of the students complaining because they hadn't had
*  Lisp before and they didn't quite understand what was going on. And I remember one student
*  complained, I don't understand how this pseudocode corresponds to this Lisp. And there was a one to
*  one correspondence between the symbols in the code and the pseudocode. And the only thing difference
*  was the parentheses. So I said, it must be that for some people, a certain number of left parentheses
*  shuts off their brain. Yeah, it's very possible in that sense. And Python just goes the other way.
*  So that was the point at which I said, okay, can't have only Lisp as a language because I don't want
*  to, you know, you only got 10 or 12 or 15 weeks or whatever it is to teach AI and I don't want
*  to waste two weeks of that teaching Lisp. So I say, I got to have another language. Java was the most
*  popular language at the time. I started doing that. And then I said, it's really hard to have a one
*  to one correspondence between the pseudocode and the Java because Java is so verbose. So then I said,
*  I'm going to do a survey and find the language that's most like my pseudocode. And turned out
*  Python basically was my pseudocode. Somehow I had channeled Guido, designed a pseudocode that was
*  the same as Python, although I hadn't heard of Python at that point. And from then on,
*  that's what I've been using because it's been a good match. So what's the story in Python behind
*  PyTudes? Your GitHub repository with puzzles and exercises and Python is pretty fun.
*  Yeah, just it seems like fun. You know, I like doing puzzles and I like being an educator. I
*  did a class with Udacity, Udacity 212, I think it was. It was basically problem solving,
*  using Python and looking at different problems. Does PyTudes feed that class in terms of the
*  exercises? I was wondering what the- Yeah, so the class came first. Some of the stuff that's
*  in PyTudes was write ups of what was in the class and then some of it was just continuing to
*  work on new problems. So what's the organizing madness of PyTudes? Is it just a collection of
*  cool exercises? Just whatever I thought was fun. Okay, awesome. So you were the director of search
*  quality at Google from 2001 to 2005 in the early days when there were just a few employees and
*  when the company was growing like crazy. So I mean, Google revolutionized the way we discover,
*  share, and aggregate knowledge. So this is one of the fundamental aspects of civilization,
*  information being shared. And there's different mechanisms throughout history, but Google is just
*  10x improved that. And you're a part of that, people discovering that information. So what
*  were some of the challenges on a philosophical or the technical level in those early days?
*  It definitely was an exciting time. And as you say, we were doubling in size every year.
*  And the challenges were we wanted to get the right answers. And we had to figure out
*  what that meant. We had to implement that and we had to make it all efficient. And
*  we had to keep on testing and seeing if we were delivering good answers.
*  And now when you say good answers, it means whatever people are typing in, in terms of keywords,
*  in terms of that kind of thing, that the results they get are ordered by the desirability for them
*  of those results. Like they're like the first thing they click on will likely be the thing that
*  they were actually looking for. Right. One of the metrics we had was focused on the first thing.
*  Some of it was focused on the whole page. Some of it was focused on the top three or so.
*  So we looked at a lot of different metrics for how well we were doing.
*  And we broke it down into subclasses of maybe here's a type of query that we're not doing
*  well on. Then we try to fix that. Early on, we started to realize that we were in an adversarial
*  position. Right. So we started thinking, well, we're kind of like the card catalog in the library.
*  Right. So the books are here and we're off to the side and we're just reflecting what's there.
*  And then we realized every time we make a change, the webmasters make a change.
*  And it's game theoretic. And so we had to think not only is this the right move for us to make now,
*  but also if we make this move, what's the counter move going to be?
*  Is that going to get us into a work worse place? In which case we won't make that move. We'll make
*  a different move. And did you find, I mean, I assume with the popularity and the growth of the
*  internet that people were creating new content. So you're almost helping guide the creation.
*  Yeah. So that's certainly true. Right. So we, we, we definitely changed the structure of the network.
*  Right. So if you think back, you know, in the, in the very early days, Larry and Sergey had the
*  PageRank paper and John Kleinberg had this hubs and authorities model, which says the web is made
*  out of these hubs, which will be my page of cool links about dogs or whatever. And people would
*  just list links. And then there'd be authorities, which were the ones that page about dogs that most
*  people link to. That doesn't happen anymore. People don't bother to say my page of cool links.
*  Cause we took over that function. Right. So, so we changed the way that worked.
*  Did you imagine back then that the internet would be as massively vibrant as it is today?
*  I mean, it was already growing quickly, but it's just another, I don't know if you've ever,
*  today, if you sit back and just look at the internet with wonder, the amount of content
*  that's just constantly being created, constantly being shared. Yeah. Yeah. It's, it's always been
*  surprising to me. I guess I'm not very good at predicting the future. Okay. And I remember,
*  you know, being a graduate student in 1980 or so, and, you know, we had the ARPANET.
*  And then there was this proposal to commercialize it. Yeah. Have this internet and this
*  crazy Senator Gore thought that might be a good idea. And I remember thinking, oh, come on,
*  you can't, you can't expect a commercial company to understand this technology. They'll,
*  they'll never be able to do it. Yeah. Okay. We can have this.com domain, but it won't go anywhere.
*  So I was wrong. Al Gore was right. At the same time, the nature of what it means to be a commercial
*  company has changed too. So Google, many ways at its founding is different than, you know,
*  what companies were before, I think. Right. So there's all these business models that are
*  so different than, than what was possible back then. So in terms of predicting the future,
*  what do you think it takes to build a system that approaches human level intelligence?
*  You've talked about, of course, that, you know, we shouldn't be so obsessed about creating human
*  level intelligence, just create systems that are very useful for humans. But what do you think it
*  takes to, to, to, yeah, approach that level? Right. So certainly I don't think human level
*  intelligence is one thing, right? So I think there's lots of different tasks, lots of different
*  capabilities. I also don't think that should be the goal, right? So I, you know, I wouldn't
*  want to create a calculator that could do multiplication at human level, right? That
*  would be a step backwards. And so for many things, we should be aiming far beyond human level.
*  For other things, maybe human level is a good level to aim at. And for others, we'd say, well,
*  let's not bother doing this because we are, we already have humans can take on those tasks.
*  So as you say, I like to focus on what's a useful tool. And, and in some cases, being at human level
*  is important part of crossing that threshold to make the tool useful. So we see in things like
*  these personal assistants now that you get either on your phone or on a speaker that sits on the
*  table. You want to be able to have a conversation with those. And, and I think as an industry,
*  we haven't quite figured out what the right model is for what these things can do.
*  And we're aiming towards, well, you just have a conversation with them the way you can with
*  a person. But we haven't delivered on that model yet. Right. So you can ask it, what's the weather,
*  you can ask it, play some nice songs and, you know, five or six other things, and then you run out of
*  stuff that it can do. In terms of a deep meaningful connection. So you've mentioned the movie Her as
*  one of your favorite AI movies. Do you think it's possible for a human being to fall in love with
*  an AI system, AI assistant, as you mentioned, so taking this big leap from what's the weather to,
*  you know, having a deep connection? Yeah, I think as people, that's what we love to do. And I was at
*  a showing of her where we had a panel discussion and somebody asked me, what other movie do you
*  think Her is similar to? And my answer was Life of Brian, which is not a science fiction movie.
*  But both movies are about wanting to believe in something that's not necessarily real.
*  Yeah, by the way, for people that don't know, it's Monty Python. Yeah. That's brilliantly put.
*  Right. So, I mean, I think that's just the way we are. We want to trust, we want to believe,
*  we want to fall in love. And it doesn't necessarily take that much. Right. So, you know,
*  my kids fell in love with their teddy bear. And the teddy bear was not very interactive.
*  So that's all us pushing our feelings onto our devices and our things. And I think that that's
*  what we like to do. So we'll continue to do that. So yeah, as human beings, we long for that
*  connection and just AI has to do a little bit of work to catch us in the other end.
*  Yeah. And certainly, you know, if you can get to dog level, a lot of people have invested a lot of
*  love in their pets. In their pets. Some people, as I've been told in working with autonomous
*  vehicles, have invested a lot of love into their inanimate cars. Yeah. So it really doesn't take
*  much. So what is a good test to linger on a topic that may be silly or a little bit philosophical?
*  What is a good test of intelligence in your view? Is natural conversation like in the
*  Turing test a good test? Put another way, what would impress you if you saw a computer do it
*  these days? Yeah, I mean, I get impressed all the time. Right. So, you know, go playing,
*  Starcraft playing, those are all pretty cool. You know, and I think, sure, conversation is important.
*  I think, you know, we sometimes have these tests where it's easy to fool the system,
*  where you can have a chatbot that can have a conversation, but you never,
*  it never gets into a situation where it has to be deep enough that
*  it really reveals itself as being intelligent or not. I think, you know, Turing suggested that,
*  but I think if he were alive, he'd say, you know, I didn't really mean that seriously.
*  Right. Yeah. And I think, you know, this is just my opinion, but I think Turing's point was not that
*  this test of conversation is a good test. I think his point was having a test is the right thing.
*  So rather than having the philosopher say, oh no, AI is impossible, you should say, well,
*  we'll just have a test. And then the result of that will tell us the answer and doesn't necessarily
*  have to be a conversation test. That's right. And coming up with new, better tests as the technology
*  evolves is probably the right way. Do you worry as a lot of the general public does about, not a lot,
*  but some vocal part of the general public about the existential threat of artificial intelligence?
*  So looking farther into the future, as you said, most of us are not able to predict much.
*  So when shrouded in such mystery, there's a concern of, well, you think it's starting
*  thinking about worst case. Is that something that occupies your mind space much? So I certainly think
*  about threats. I think about dangers. And I think any new technology has positives and negatives.
*  And if it's a powerful technology, it can be used for bad as well as for good.
*  So I'm certainly not worried about the robot apocalypse and the Terminator type scenarios.
*  I am worried about change in employment. And are we going to be able to react fast enough to deal
*  with that? I think we're already seeing it today, where a lot of people are disgruntled about
*  the way income inequality is working. And automation could help accelerate those kinds of
*  problems. I see powerful technologies can always be used as weapons, whether they're robots or
*  drones or whatever. Some of that we're seeing due to AI. A lot of it, you know, need AI.
*  Mm-hmm.
*  And I don't know what's a worst threat. If it's an autonomous drone or it's CRISPR technology
*  becoming available, or we have lots of threats to face. And some of them involve AI and some of them
*  don't. So the threats that technology presents, are you, for the most part, optimistic about
*  technology also alleviating those threats or creating new opportunities or protecting us from
*  the more detrimental effects of these? Yeah, I don't know. Again, it's hard to predict the future.
*  And as a society so far, we've survived nuclear and other things. Of course,
*  only societies that have survived are having this conversation. So maybe that's survivorship bias.
*  What problem stands out to you as exciting, challenging, impactful to work on in the near
*  future for yourself, for the community, and broadly? So, you know, we talked about these
*  assistance and conversation. I think that's a great area. I think combining
*  common sense reasoning with the power of data is a great area.
*  In which application? In conversation? Just in general, yeah. As a programmer, I'm interested
*  in programming tools, both in terms of the current systems we have today with
*  TensorFlow and so on. Can we make them much easier to use for a broader class of people?
*  And also, can we apply machine learning to the more traditional type of programming?
*  When you go to Google and you type in a query and you spell something wrong, it says, did you mean?
*  And the reason we're able to do that is because lots of other people made a similar error and
*  then they corrected it. We should be able to go into our code bases and our bug fixes bases.
*  And when I type a line of code, it should be able to say, did you mean such and such? If you type
*  this today, you're probably going to type in this bug fix tomorrow. Yeah, that's a really
*  exciting application of almost an assistant for the coding programming experience at every level.
*  So I think I could safely speak for the entire AI community. First of all, for
*  thanking you for the amazing work you've done. Certainly for the amazing work you've done with
*  AI Modern Approach book. I think we're all looking forward very much for the fourth edition and then
*  the fifth edition and so on. So Peter, thank you so much for talking today. Yeah, thank you.
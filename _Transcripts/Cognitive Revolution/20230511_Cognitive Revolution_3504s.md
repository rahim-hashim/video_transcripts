---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 3504s
Video Keywords: []
Video Views: 2323
Video Rating: None
---

# The AI Revolution in Medicine with Dr. Isaac Kohane of Harvard Medical School
**Cognitive Revolution "How AI Changes Everything":** [May 11, 2023](https://www.youtube.com/watch?v=pS5Vye671Xg)
*  That's when I frankly became dumbfounded because I gave it very difficult cases.
*  I asked GPT-4 what was the next thing it would do and it went to a molecular diagnosis of
*  something called 11 hydroxylase deficiency.
*  If I ran into 100 random doctors, I'd be surprised if one of them would be able to do that.
*  And so I do think that this is the mechanism to keep doctors up to date with the latest.
*  I think it allows you to remember everything about the patient that you should have remembered.
*  It will allow you to avoid errors.
*  Absolutely.
*  No doctor should be without it.
*  They should have this sidekick that is meticulous, completely up to date, ever vigilant, and
*  sometimes wrong.
*  And that you're there to evaluate that.
*  You can't even compel doctors to Google what is the latest findings for their patients.
*  But if we have this active agent that's listening in and looking at the record, we can really
*  ensure that the patient gets that extra level of scrutiny.
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host, Eric Thornburg.
*  Hello and welcome back to the Cognitive Revolution.
*  Today I'm excited to begin a short series on AI in Medicine.
*  My guest today, Professor Zach Kohani, is chair of the Department of Biomedical Informatics
*  at Harvard Medical School and co-author of the new book, The AI Revolution in Medicine.
*  Professor Kohani was among a select few people to receive early preview and research access
*  to GPT-4 in the fall of 2022.
*  And his approach to exploring, characterizing, and beginning to integrate AI into clinical
*  practice constitutes the single best practical study of modern AI application that I've
*  seen from academia to date.
*  Sam Altman, in a forward to the book, writes that, quote, this book represents the sort
*  of effort that every sphere affected by AI will need to invest in as humanity grapples
*  with this phase change.
*  I totally agree.
*  And I believe that the key insight is the importance of expert hands-on use.
*  To quote the book, to really understand GPT-4, you need to use it and live with it in the
*  same way that no amount of reading and listening to others can tell you what it's like to ride
*  a roller coaster.
*  What it's like to interact with GPT-4 is similarly indescribable.
*  By not just theorizing about the potential of AI, but truly embracing it, Professor Kohani
*  and his co-authors were able to understand GPT-4's strengths, weaknesses, and quirks.
*  Throughout the book and our conversation, he uses concrete examples to demonstrate GPT-4's
*  capabilities and potential impact.
*  Ultimately, he concludes that it is clinically superhuman and will become such a part of
*  the fabric of medicine that to receive medical advice without GPT-4-like support will soon
*  be considered substandard.
*  At the same time, he does understand that it's such an unfamiliar and indeed alien
*  intelligence, somehow both smarter and dumber than any person you've ever met, that human
*  supervision and control remain critical.
*  With a positive vision of human AI symbiosis in medicine and the goal of allowing doctors
*  to quote, re-engage in medicine as an intellectual and emotional process focused on each and
*  every patient, Dr. Kohani and his co-authors issue an urgent call for large-scale testing,
*  as well as public education around AI technology and its limitations.
*  Regardless of the field that you're in, Dr. Kohani's combination of deep immersion,
*  enthusiastic exploration, pragmatic optimism, risk awareness, realism, and forward-thinking
*  vision make this a worthy example for others to study and emulate.
*  The book, which I find myself recommending frequently, is The AI Revolution in Medicine,
*  and I hope you enjoy this conversation with Professor Dr. Zach Kohani.
*  Professor Zach Kohani, welcome to the Cognitive Revolution.
*  Glad to be here.
*  Thanks for inviting me.
*  I'm super excited about this conversation because you have just released or you're in
*  the process of releasing a new book called The AI Revolution in Medicine, which really
*  couldn't be more on the nose for the topic of our podcast and I think is really an exemplary
*  exploration of cutting-edge AI tools and how they can make an impact in our lives and in
*  an area that is obviously so critical and so complicated as medicine.
*  I think it's really a phenomenal artifact that you and your co-authors have created.
*  Before we get into that, I normally don't even do this, but just because there's so much
*  skepticism and doubt and people call me AI hype boy all the time and things like that,
*  could you maybe just give us a quick introduction to who you are, your background in medicine and
*  IT surrounding medicine so that folks have a sense for where you're coming from?
*  Sure.
*  Grew up in Switzerland, came to the United States for college,
*  learned about computers as an undergraduate even though I was a biology major,
*  went to medical school and then was terrified by learning because I didn't have any doctors in my
*  family and learning firsthand that it was a noble profession but not a great science application.
*  And so bailed for a few years to get a PhD in computer science during the heyday of
*  artificial intelligence in the 1980s. And then as we went into AI winter because of the disappointment
*  after some of the overstated promises of that period, I completed my clinical training as a
*  pediatric endocrinologist and started a research group. And so I was a professor at SLAM, a
*  professor at Harvard Medical School, first in pediatrics. Then I created a new department,
*  biomedical informatics. I'm the chair of that department and I have lots of bright young
*  faculty doing lots of great work using computer science and information processing techniques
*  all the way from genomics to clinical AI. I just started a new journal, a spin-off of the new journal
*  of medicine called NeJM AI to focus on how do we actually get clinical grade validation for
*  AI artifacts in clinical care. And along the way, I've been really quite involved with a lot of
*  IT health infrastructure as well, trying to get the data to flow well and most of all for patients
*  rather than for third parties. So I would kind of bottom line that by saying you're about as
*  credentialed as you can possibly get in the world of the intersection of AI and medicine.
*  You've seen a lot. It sounds like you've been through some ups and downs and seen a lot of
*  things that didn't really pan out. Well, let's fast forward then to about six months ago.
*  I'd love to just kind of hear the story of how it came to be that you got this very early access
*  to GPT-4, what that initial experience was like. And then of course, we'll get into all the
*  more conceptual issues. But I think the first person narrative is so powerful. So give me
*  kind of a sense of that. I had met Peter Lee from Microsoft, who's the head of Microsoft Research,
*  several times in different venues. He's very easy to get along with. He understands academia well.
*  He himself was a department chair of computer science at Carnegie Mellon back before DARPA,
*  back before Microsoft. And he calls me up and he tells me that he has to tell me something that
*  on one condition that I can't talk about it with anybody else. He had to get top level company
*  clearance to talk to me about it. And this was before Chad GPT came out. But it was about the
*  next thing, GPT-4. And he showed me what it could do. And that was already pretty exciting. But then
*  he gave me early access to it directly so I could work with it. And that's when I frankly became
*  dumbfounded because I gave it very difficult cases. A case of a child that was called to the nursery
*  where there was a hole in the base of the phallus. You could not palpate testes.
*  I asked GPT-4 what was the next thing it would do. And it went step after step
*  imaging workup, hormonal workup. And I gave it as it went step by step what the results were.
*  And it went to a molecular diagnosis of something called 11 hydroxylase deficiency.
*  If I ran into 100 random doctors, I'd be surprised if one of them would be able to do that.
*  And so I knew that there were a lot of limitations to this. I had seen it, quote, hallucinate. I'd
*  seen it make up stuff. But the fact that it could have this dialogue with me at a very high level
*  of medical sophistication on a large language model that was not particularly tuned for medicine
*  was my mark. And the fact that I could ask it questions literally about
*  Talmudic advice to the same program and get expert commentary was unsettling and exciting
*  at the same time. And in fact, my immediate reaction when Peter told me was my words fail me,
*  which is unusual. I talk at it. But I told him in the end, I was not surprised that this happened,
*  but I could not believe it was happening now. I'd expected this would happen maybe five years after
*  all this. But then as I realized what it could do, within a few days, it occurred to me that it was
*  going to transform the back end business of healthcare, how money is paid, how it's billed,
*  how it's transferred, how procedures are permitted or not. So all the back end stuff,
*  it was going to transform boring administrative stuff that clinicians have to do. But also,
*  since it I knew was going to be released to the public, it was going to change the level of
*  expertise of patients who have been increasingly bereft of primary care support
*  and who out of desperation use whatever data sources and all sorts of they can. I mean,
*  there is a reason why you've heard the term Dr. Google, because even though a lot of the sites
*  it's you get sent to are either bogus or really wrong headed, they're just not getting a good
*  enough alternative to get to expert advice. And in fact, with all its warts,
*  so long as you have a human loop, so long as they eventually talk to a doctor,
*  it's much, much better than what we have today. And that's why even with GPT 3.5 that people were
*  experiencing before GPT 4, you were hearing lots of people using this for their own healthcare.
*  And this is not just an American phenomenon, this is an international phenomenon. And so
*  it's very interesting when you have a transformative technology like this, which takes
*  a fundamentally very conservative, sometimes for the right reasons, discipline like medicine
*  and changes some important power relationships. And so it's going to be fascinating to see how
*  it plays out. I know there's going to be a lot of pushback. Some of it will be because of genuine
*  concern about accuracy, about bias, but also there'll be a lot of secret cows. People
*  are making a lot of money by having a chokehold on how information flows
*  in the medical care system and what kind of advice is given when. You can imagine that
*  if a large language model tells you five reasons why there are alternatives to the surgery that
*  was just proposed, and then you go talk to another doctor and say, that makes sense.
*  The first doctor who proposed surgery is not going to be happy. That's just one example. I'm
*  going to literally millions of such conversations that are going to happen as a result of this
*  democratization of knowledge. Of course, it's going to happen across many verticals, not just
*  medicine, but medicine is such a personal, obviously personal part of our lives that
*  it's going to make those issues quite real all of a sudden.
*  That's a great overview. There's a lot of little areas there that I want to follow up on and dig
*  into in a little bit more detail. Before getting into the medicine specific aspect of this,
*  one thing that Sam Altman said in the foreword to the book, which I think is so true, is that
*  the study that you guys have conducted here is really emblematic of the kind of study
*  that is going to need to be done across a wide range of disciplines.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  I want to tell you about my new interview show, Upstream. Upstream is where I go deeper with some
*  of the world's most interesting thinkers to map the constellation of ideas that matter.
*  On the first season of Upstream, you'll hear from Mark Andreessen, David Sacks,
*  Balaji, Ezra Klein, Joe Lonsdale, and more. Make sure to subscribe and check out the first episode
*  with A16Z's Mark Andreessen. The link is in the description.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omnike so much
*  that I invested in it and I recommend you use it too. Use Cogrev to get a 10% discount.
*  For what it's worth, and listeners have heard me talk about this before, so this is just for you,
*  I had kind of a similar experience. I was an OpenAI customer. They had a customer preview program
*  for GPT-4 as well. So right around the same time, I got essentially, I think the same access and had
*  the same mind-blowing experience where I was kind of dumbfounded, stayed up all night the first night
*  just trying thing after thing. So I can relate. But I want to hear a little bit more about,
*  okay, once that initial shock wore off and you said to yourself, I've got some time here to really
*  get out in front of this thing and try to figure out what's going on, what it can be, what it can
*  do. How did you then approach that? And what advice would you give to others who are thinking about
*  undertaking such a study in their own areas? I think that what you have to do
*  is actually get your hands on it and really put it through its paces in real world examples in what
*  you do. And so, for example, I went through literally hundreds of different scenarios,
*  only a few which have made it to the book, of doctors engaging with it, with different questions,
*  at different points in the diagnostic and management process, all the way from initial
*  screening to management questions to generating billing codes. I came at it and asked friends of
*  mine what questions they had asked their doctors recently and ran it through those questions.
*  And I think it's really important to see how it answers those questions rather than having a
*  theory about it because then you see where it does well and where it doesn't do so well. And
*  right now, I don't see any alternative to having lots of examples like that. I then did the same
*  thing for research. What are the different research tasks? I write down about it on a piece of paper,
*  sadly, all the different parts of both clinical research and basic biomedical research, all the
*  questions that you could ask. And I went through it and there were some areas where it clearly was
*  not ready for prime time and there were other areas where it did really wonderfully. And if you're in,
*  whether as a consumer, a citizen, or if you're running a business, I know of no other way
*  than to actually do that assessment directly. Frankly, that's probably what motivated, even
*  though I decided to do this many years before it was announced, the New England Journal of Medicine,
*  NEJM AI, because we need to have clinical grade validation of these tools. And
*  it's not obvious where in society this is going to happen. So at least I want to create a journal.
*  There'll be one source of clinical grade validation for this. But we need many, many such venues.
*  And we're, of course, going to see this across all verticals. If we don't see them across all
*  verticals, that's where the danger is going to be. And so if you're a decision maker, I see no
*  alternative other than try it out yourself. Don't let other people tell you what it does.
*  Use it in your own hands. And as in many, many things that are exciting like this,
*  on the one hand, it does things better. Some things much better than you could imagine.
*  And some things, it's incredibly limited. You need to learn firsthand. I've tried to point out some
*  of those in the chapters that I wrote in the book. But again, you need to learn firsthand.
*  I think that's truly phenomenal advice. A lot of times people call
*  the AI moment right now pre-paradigmatic. And I think that speaks directly to your point about
*  don't just take some theory and work from that. We don't have really good theories at this point
*  for what these systems can do, even now, let alone what they will be able to do in the future.
*  The book is extremely quotable. And you just kind of alluded to one of the quotes that I loved,
*  which I thought crystallized something that I had felt and tried to articulate, but you guys
*  did it better when you said that it is simultaneously smarter than and stupider than any person you've
*  ever met. I thought that was genius phrasing. Yeah, that's that credit goes to Peter Lee for
*  that one. That was a great quote. I love it. Here's two I think that are yours. And they seem to be in
*  some tension. So I'll give you both. And then, you know, it's kind of like the smarter, stupider
*  thing, but help us unpack this and give us a little more detail. So first quote,
*  how well does the AI perform clinically? My answer is I'm stunned to say better than many
*  doctors I've observed. But then in some tension with that, also quote, for the foreseeable future,
*  GPT-4 cannot be used in medical settings without direct human supervision. So unpack that for us.
*  How impressed should we be that GPT-4 can ace most of the examinations that doctors have to take
*  to get certified doctors? I think it's impressive. And it's impressive how fast it's improved. It's
*  did very poorly on the National Medical Board's GPT-3 a year ago, but since then, it's now
*  top notch. But here's the thing. It's not a human being. And I'm not saying this in some
*  human first bigoted sense. It's just that a lot of the common sense things that we have,
*  that we can share among us, we can't assume are true of GPT. It can engage with you at an expert
*  level about pretty complicated diagnostic and therapeutic problems. At any given point,
*  not often, but the mistakes are huge, it can go off the rails and start arguing with you
*  about a point where it might actually be wrong or about something that is important to you,
*  but it doesn't think it's important. And so on the one hand, there's an old joke. What do you call
*  the person who graduated at the bottom of their medical school class? And the answer is doctor.
*  And that means, of course, that half of doctors on average are worse than the top half.
*  And I'm quite convinced that in the hands of those bottom half, GPT-4 can make them much closer
*  like the top half, which would be a huge improvement in healthcare without even talking about the
*  torchbearer, doctor house kind of things you could do. Just getting us to practice medicine the way
*  it should be done by better practitioners would be a tremendous advance in the future.
*  And healthcare. But because we can't assume that it understands our values or what's important to
*  individual in their decision making, not having a human loop, I guarantee is going to create
*  lots of problems. And I can tell you also, the more you know, the more you can get out of GPT.
*  If you ask it more intelligent questions, it will give you more intelligent answers.
*  And so for a simple future, yes, absolutely. And it'll become a better and better tool.
*  It'll be able to integrate not just text, but vision and sound. It will allow us to
*  see things and catch things that we may have missed because human beings are not always as
*  attentive, as alert, as fastidious as they should be. But you still have just to make it to be a
*  IQ 100 human being means that there's a lot of shared values and performance that you
*  that you can't actually necessarily rely on GPT-4 to have. Now I'm quite willing to believe that
*  when GPT-7 going around as a robot and living among us may be able to acquire those, but we're
*  far of those kind of skills and those kinds of values, maybe, but we're far from that. And so
*  today human in a loop until GPT, these generative models look quite different from what we see today.
*  You kind of alluded to the torchbearer paradigm and you sketch out four paradigms for kind of
*  how an AI system like GPT-4 can be integrated into medicine. I think in a sense, these kind of line
*  up with ways that it could be integrated into all sorts of different areas of society. So I kind of
*  want to go through each one and just interrogate them a little bit. They are the trial, the trainee,
*  the partner, and the torchbearer. So let's start with the trial. The notion here, as I understand
*  it, is that you could think about GPT-4 as sort of like a drug and you could try to evaluate it by
*  kind of having a, you know, some people get it and some people don't and like how does that
*  turn out? You ultimately kind of seem to reject that as a paradigm. I didn't quite follow you
*  all the way there. To me, I kind of thought, well, geez, why not just run that trial? And if it makes
*  people healthier, then that would be pretty meaningful to me. We have in the other
*  pre-generative model flavor of AI and these convolutional neural networks that we use
*  so successfully for image recognition. We have a very focused task, retinopathy,
*  aren't looking at the back of the eye, or pneumonia, looking at chest x-ray.
*  There we can define, here's a patient population. They have a certain characteristic. They come in
*  coughing, let's say, and we're going to accept patients of this kind. We're going to say,
*  here's how we're going to determine success or not success, which is how long are they going to live
*  or did I get the right treatment? And we know how to do that. FDA has done this for drugs.
*  They've even done it for these AI widgets. And the merit there is it's very clear,
*  and especially if you do a randomized controlled trial, whether it is a statistically reproducible
*  kind of phenomenon. That's not going to work for GPT-4 for many, many reasons. One,
*  when you start a conversation with a GPT, you may start because you have a question around that
*  patient coming with cough, but then very quickly, because GPT includes all of medicine, you could
*  end up anywhere in medical diagnosis and therapy space. And that means that if you really want it
*  to do the trial, you'd have to compare it across all diseases. So it's a huge trial. It's not
*  versus a narrow question like the retinopathy. It's like this patient population get healthier
*  when GPT was used. Those trials will happen, but it's going to be a big hall, a big lift. It's
*  going to take thousands or hundreds of thousands of patients. And it's also not going to be
*  reproducible because what you find as how the effect of GPT-assisted doctors in Massachusetts
*  and Boston with a lot of health technology is going to be a different result than what you see
*  in China, which has almost no primary care, or in Africa, or even more practically, I can tell you
*  that predictions, for example, of who is going to most likely to die from COVID. We saw these AI
*  models early in 2020, and hospitals a few hundred miles away had totally different performance with
*  predictive models because the patients were different, different obesity levels, different,
*  and we didn't know, and different race composition. It's going to be very difficult.
*  Furthermore, unlike a small just million parameter model,
*  these large models with a trillion parameters are changing all the time. So I don't even know.
*  In fact, I know for a fact that the GPT-4 I'm working with now in April is not the same GPT
*  I was working with in October of 2022. And so it's very hard to stand up behind and say,
*  oh, it passed some trial test, and now it's going to work. That works for drugs. Drugs are static.
*  And even there, even with drugs, it's a bit of a problem because with different populations,
*  it might have different results. But since this interacts with not just human physiology,
*  but the practice of medicine, how doctors are different in different hospital systems,
*  it's very, very hard to validate it. So the trial model is not going to be particularly
*  useful for GPT as it's being used, which is as a general purpose medical problem solver. You could
*  use it for a very narrow purpose like screening, but in that case, it's not clear that purpose
*  built models might not be able to perform it. It's generality and linguistic supremacy is really
*  where it came most from. I think there's a number of really interesting
*  points there. One thing that, again, I think is representative of a bigger societal wide issue as
*  well is society and individuals and organizations are all going to change in response to AI.
*  And then not too far downstream of that, it will also be like AIs interacting with AIs in ways that
*  become increasingly hard to predict. And so I do think that is way under theorized right now.
*  It's one thing to say, we hold all else equal, we give you GPT-4, how does that go? But then we give
*  everybody this and then we wrap them up as agents. I think we really are stepping into a great unknown.
*  But I still want to challenge maybe just one more time on this question because it does feel like,
*  I'm reminded of an old RAND study that they did. This was probably four years ago now,
*  but they did something where they basically said, we're going to give free unlimited health care
*  to a certain population and we're going to give no health care or whatever they currently have
*  to another population and just step back and observe over a period of a couple of years.
*  And then, I'm not an expert in that study, I think it's probably somewhat debated. It will
*  probably be highly debated with GPT-4 as well. But it does seem at least conceptually possible
*  that you could do something at a very high level like that and then come back and be like,
*  who's living, who's not, who's reporting well-being and who's not. And if there is
*  a significant difference. I want to compliment you on your perfect skepticism, but when it comes up
*  to actually doing that trial, it'll be hard to bank the results because let's say you do it for
*  two or three years. How is it not contaminated? So you get one health care system, GPT, you give
*  another health care system, not GPT, just good doctors. If there's a difference, is it because
*  of the difference of GPT or is it a difference because of the difference in health care system?
*  You do your best to match them up, but it's hard to do that. And people are going to hear about GPT
*  and is it really going to be a pure, and the patients are using it and some of the doctors
*  might be using it. I think it's actually practically very hard to do the experiment that you just
*  described in a way that you would really want to do more than a cocktail party conversation about
*  it and say, oh, it really helped. And this is a percentage of bad outcomes and a percentage of
*  good outcomes. I think that's going to be for the general use, I think that's going to be very,
*  very challenging. Certainly I do think it will be hard to avoid the leakage and it's certainly
*  almost seems impossible to double blind. So it definitely challenges the paradigm.
*  And also just the confounding, the differences in health care systems. It's fortunately or
*  unfortunately, medicine is not right now cookie cutter. There's a lot of bad things that happen
*  because it's not cookie cutter. There's a lot of latitude for doctors to make mistakes and to do
*  things that are frankly remunerative, but not necessarily clinically effective. But because of
*  that, there's so much variation and the economic model, a for-profit hospital, a non-profit hospital,
*  an academic hospital, a community hospital, very different. And again, even different parts of the
*  United States are different. So it's hard to know what the study will be. I'm sure people will try
*  it. My prediction is it's going to be hard. Yeah, that sounds all right to me. So next up is the
*  trainee. The paradigm here is essentially give a battery of tests to an AI, kind of same battery
*  we'd give to a doctor. And if it can pass, then one might think that that's good. But again,
*  I think you do a great job of keeping front and center. The alien, and that's a term that
*  I've also used and you use in the book, the alien nature of the AI and the fact that we supporting
*  those benchmarks or those tests is a fundamental set of assumptions around humanity and just how
*  people will act in all these situations or circumstances that we're not testing explicitly.
*  And we just can't make those same assumptions for the AI. Exactly. I mean, for example, this
*  really happens. God forbid you have a cancer diagnosis. There is a conversation to be had,
*  which is, do you, you know, you have a wedding that you want to make in six months and you might
*  or not prefer to have a better chance of making it healthy to the wedding and having a better
*  chance of living additional year. And those trade-offs are conversation that maybe one day
*  these models can do, but today they can't. They don't have that common sense. They don't have the
*  human grounding yet. So I think that's perfect. And again, this is something that people should
*  develop an intuition for by getting hands on. You find these alien moments in your own explorations
*  and when it hits you, it hits you in a way that is hard to kind of internalize by reading. And I
*  think your book does a great job of bringing that to the fore, but again, go try it people.
*  The partner paradigm. So I think this is kind of where we're landing right now as like your
*  recommendation. You also use this term symbiotic medicine with the doctor and it's really a three
*  party interaction now with the doctor and the patient and the AI. I'd love to hear a little bit
*  of kind of what do you think the right ways and I understand that it's, you know, call this
*  provisional, but what do you think the right ways of using a tool like GPT-4 as a clinician are?
*  Like what should the standard of care be as people have this? You know, could we see ourselves in a
*  scenario where it becomes like a violation of standard of care to not consult GPT-4 in the not
*  too distant future? You know, I remember when I was in training, we had did something that's now
*  disappeared because medicine, the financial pressures of medicine are such that it's not
*  done, which is after clinic, we'd go over together as a group, all the patients and say, and explain
*  what we decided. And then some people would say, hey, did you think about this? Oh, no. Well, I
*  should call the patient and say, we better do that. And that additional reflection
*  absolutely improved our quality of care. And so by analogy,
*  because increasingly it's going to be multimodal, having an AI of this kind, listening in on the
*  conversation, looking at the clinical notes and saying all the time, hey, have you, did you think
*  of that? I think it's a high probability that something you didn't mention, you can say, oh,
*  I already thought of that. Don't be quiet. Or, oh, you might actually think about that. Or did you
*  know Mrs. Jones already had had that test? Don't order another test. Okay. And there's a new drug
*  that's actually twice as effective, lower toxicity level. We try to keep doctors up to date.
*  And it's impossible, even if they're trying and not all of them try. And so I do think that this is
*  the mechanism to keep doctors up to date with the latest and the latest expanding medicine that goes,
*  for example, into genomics that so many doctors don't know about, that some patients know more
*  about than they do. I think it allows you to remember, in quotes, everything about the patient
*  that you should have remembered. It will allow you to avoid errors. It will allow you to identify
*  other patients that perhaps you should be paying more attention to. So the way I think of it is
*  done well, done well. Absolutely. No doctor should be without it. They should have this sidekick that
*  is meticulous, completely up to date, ever vigilant, and sometimes wrong. And that you're
*  there to evaluate that. If I were a patient, I wouldn't want my doctor to have that.
*  In the previous models, we can't compel doctors to keep up to date by the green literature.
*  We can't even compel doctors to Google what is the latest findings for their patients. But if we have
*  this active agent that's listening in and looking at the record, we can really ensure that
*  the patient gets that extra level of scrutiny. And of course, patients are going to have access
*  to the same level of expertise, potentially. And so I think it's going to cause the healthcare system
*  to have to increase the quality of its game. Yeah, I think that's really, again, I appreciate that
*  so much in the book, because I think there really is no putting the two things together.
*  Putting the toothpaste back in the tube, so to speak, on this. And there's really kind of the
*  only way through is through. So I appreciate you confronting that head on. And I actually was
*  thrilled to see a mention of the app Replica in the book. We had the CEO of Replica on the show
*  as one of our guests. And it was such an enlightening conversation around how lonely a lot of people are,
*  how even a pre-... And she's had this app for years. So just how, while even the system was
*  so unsophisticated, it meant a lot to people. And now it's obviously accelerating.
*  So I've actually been slightly terrified about that aspect of it, because what today we would
*  think of the crappiest interactor ever, the ELISA system that Joe Weissenbaum wrote, which was just
*  very simple, very shallow grammatical parser that because a Rogerian therapist basically just plays
*  back to you what you said with a tiny little bit of permutation, people would use this as an actual
*  therapist. And this really, really did not know anything. And Joe Weissenbaum, who created
*  ELISA, his own secretary, would lock herself in her office for a session with that. And so it's both
*  perhaps heartwarming, but also pretty terrifying. And I think it does speak to how much we need
*  that interaction around healthcare. Let's just, let your listeners be deluded about it, especially
*  the younger ones. People with actual health problems have very few people they can talk to.
*  When they run into a primary care provider, if they're lucky enough to have one, it's a 10-foot
*  in the meeting, and most of the questions go unanswered. And when they have another question,
*  it's waiting another six months where things could be done, and then they're not done until
*  things are much worse. So there's a huge need. So let's go then to the kind of possible future
*  that we're not quite in yet, which is the torchbearer model. You might also call this like
*  the Oracle model, or even the sort of scientific or research pioneer, the sort of the sort of
*  research pioneer AI. This was something that I also looked really hard for. One of the first
*  things I tried to figure out is, does this GPT-4 system show anything that seems like it can generate
*  truly new novel scientific insight? And I came to the same conclusion that you did, and you wrote
*  in the book, can GPT-4 independently develop testable hypotheses that entail specific
*  therapeutic interventions with a high likelihood of being supported by clinical trials?
*  Currently, the answer is no. So I think that's definitely true, but I don't have a great sense
*  of exactly why or what the barrier is or how or when that might change. So what do you think is
*  kind of the key thing that it can't do right now that ultimately cashes out to a no on that question?
*  I think that the interest we should have is that it's luring an amazing amount,
*  sometimes in a superhuman way, about the things that we talk about. And so if there's a lot of
*  human beings talking about it, it will know about it. And I don't want to anthropomorphize too much,
*  but it can do some theory formation around those things that human beings talk a lot about.
*  But for a generation of new paradigms where human beings have not talked very much about it,
*  it's a bit at a loss. And what kind of data it would need and how to think about that,
*  there's not a lot for it to learn. And I do think there are ways to approach it. But right now,
*  this current generation of linguistically supreme, but not scientifically supreme,
*  models, I think are limited. At the same time, at the margins, because of this
*  maximum exploitation of what we already know collectively, but not individually,
*  it can surprise us. So for example, doctors are often stumped. And so there's millions of patients
*  in the United States worldwide, hundreds of thousands in the United States who are not
*  diagnosed. And I have the privilege of being the principal investigator of the coordinating center
*  of something called the Undiagnosed Disease Network. And it's across multiple hospitals at Stanford,
*  at Harvard, at Baylor, and Florida, and Duke, and so on. And what we find is if you ask the right
*  questions, if you do the right studies, if you do genomic sequencing, you can sometimes
*  maybe about 34% of cases figure out what was the problem. And that way you make a meaningful
*  change for that patient. And so I've put GPT and this is after seeing a lot of top doctors. So I
*  put GPT for through paces, not only those cases, but even cases that have not been solved. And I
*  said, Hey, we found mutations in the following five genes. Which one of these genes do you think?
*  Is responsible for this case. And it came up with a, with the top ranked one was the one that we had
*  independently through a lot of basic science modeling the disease, the mutation in a fruit fly,
*  all things, validated that it was the cause of the disease of older other genes, which were
*  plausibly causing the disease. So it's not quite theory information, but it's really working at the
*  very head or hairy edge of what's known because of its ability to bring together all this knowledge
*  in a focused way for a question. So we have about 10 minutes left. I think that maybe the final two
*  sections I want to go into a little bit are kind of the next evolution of GPT-4. Sam Altman has
*  recently said that they're not yet training GPT-5, but they plan to do a lot more with GPT-4. Some of
*  it has already been done and we just haven't seen it like the multimodality and ability to understand
*  images. I'd love to hear your thoughts on what you think without just like hyper scaling the model,
*  you know, a hundred X more, what are the kind of incremental enhancements? And that could be like
*  attaching it to systems or it could be, you know, some medical fine tuning, or it could be
*  more multimodality. So it can also like natively understand scans. Like what are the things there
*  that most excite you that you think will be most impactful? My whole life as a science fiction fan,
*  let me try to, at least for the first part of this question, not go there. So here's what I think is
*  going to happen relatively soon. One is using entire healthcare systems as not a fine tuning
*  model because right now it's very hard to fine tune GPT, but to have a certain accessory set of
*  embeddings, like using, for example, the pine cone framework to create a, essentially a knowledge
*  base that GPT can use to customize its advice for that healthcare system. So remember what we were
*  talking about before, how different hospitals are different, different populations. One way to address
*  that is say this, here's your large language model, GPT-4 or perhaps Google's Bard. And here you have
*  a set of embeddings representing essentially the multidimensional co-occurrence of findings
*  in this patient population. And this way you'll be able to give much more customized
*  and deeply reflective of the practice of medicine in that hospital system than generic GPT-4 or other
*  large language models. So I think customizing it to the knowledge base and the practices of a system,
*  of a hospital system, is going to be one important area. The other important area is going to be
*  is going to be specifically in speech. I think that having omnipresent speech recognition,
*  multi-speaker speech recognition is going to address the thing that's been causing,
*  frankly, the most burnout for physicians and most unhappiness, which is they've been turned into
*  documentation clerks. And by having, if you have a combination of the prior record of a patient
*  and you're listening to everything that's going on between the doctor and patient,
*  I'm fairly optimistic that you can come up with a very good first draft of the clinic note that
*  the doctor can just look at, say yeah, or edit, and then have a version of that note sent to the
*  patient, to the referring doctor, and perhaps even to the insurance company appropriately.
*  And so those are, I don't have to stretch my imagination at all to say that's where we're
*  going to go next. Beyond that, I do think the stretch is going to be in discovery, because
*  there's going to be some kinds of theory formations that are going to be very hard for the GPT,
*  for any of the other leading language models. But I think that there can be constrained parts of
*  theory formation where you can say, can you identify in these data
*  the drug that seems to be the most effective based on X, Y, and Z? And although that's not
*  a full de novo theory formation, it's a focused question that with the right data,
*  I think it'll be able to pull off. But I think we need to have the right kind of data. And it's
*  not always obvious which is the right kind of data. It's not clear that the standard
*  transformer model as it is currently implemented will work well for those applications. But we'll
*  see. You allude a little bit to also the integration of, say, an alpha fold type,
*  something that natively grocks protein structures could be integrated with language. Paint that
*  picture a little bit more for us as well. Of course, the best science fiction outcome,
*  which actually I think we will be there in probably 10, 15 years or maybe earlier, is
*  I have a patient with this cancer with the following mutations, both in the germ line and
*  the cancer. What's the right drug for this patient? If we don't have any drugs, what's the right drug
*  to develop? And right now, alpha fold, which is a kind of language model because its language is
*  the language of amino acid sequences, and that and a little bit physics, but mostly the large
*  language model, it's able to solve the proteins of the structure of almost all proteins. It's
*  already being used to understand how small molecules dock. There's already beginnings and
*  deep, deep mind which has been leading in this area has not, understandably, been totally
*  transparent about the next generation, but it's going to be around large protein interactions.
*  And I do think that something like stimulating a cell will, in fact, be possible in a five to 10
*  year time frame. But well before we get to that, it means that in a five year time frame,
*  we're going to be able to do a much better job in saying, here's a drug company. It has a bunch
*  of interesting drug leads to treat this cancer, to treat Alzheimer's. Which of these are going
*  to be most likely to be effective and close at least side effects? And understanding both,
*  bring together the knowledge of structure from something like alpha fold and its descendants,
*  and knowledge about disease progression that you get from large data sets from hospitals.
*  That multimodal linking will allow us, I think, to do a much better job in getting a much better
*  yield. Bring candidates all the way from, this is a possible lead compound to something that will
*  make it through phase one, phase two, and phase three with both efficacy and lack of
*  side effects sufficient to can the project. I think that will be transformative and
*  I think we will see this within the next five years. But it's not just scaling up.
*  I think that's undeniably a super exciting and inspiring vision. The last question I wanted to
*  ask is kind of on the path from here to there. You alluded to, there's going to be all sorts
*  of conflict, there's going to be all sorts of noise. But I was struck by a couple of, again,
*  short quotes from the book. One that kind of surprised me, as you said, you believe in
*  obtaining patient data from patients as opposed to from systems. And so that just got me wondering
*  why is that? And ultimately, who do you think the AI should be working for? Does the hospital system
*  have its AI and the doctor has its and the patient has their own? Or is there one that we all kind of
*  work with together? The dynamics of who the AI is aligned to and whose interests are primary,
*  again, seems just very under theorizable to get your thoughts.
*  No one knows how it's going to settle out in the long term. But I think in the midterm,
*  you're going to have AIs that are aligned for different organizations. And yes, there will be
*  an AI that's aligned for the insurance company and the AI that's aligned for the hospital and
*  an AI that's aligned for patients. And there'll be different markets for those. In the end,
*  as a human being, I hope that and I think there will be the most public support for consumers
*  having the alignment be with them. And so I personally feel that if I am able to donate my
*  data to a large language model or any other kind of AI, if it's aligned with me, I'm much more
*  comfortable giving it my data than with another AI, which is not necessarily aligned with me.
*  I am just as I'm much more likely to tell my doctor it's okay for them to use my data to
*  share, get a second opinion from a colleague. I'm much more likely to want to share my data.
*  And by the way, through work that Apple has done that we were actually quite involved with
*  a few years ago through Apple Health, they have a relationship with 800 hospitals and it's growing
*  by hundreds every month or so. You can actually download all your medications, labs,
*  diagnoses, procedures, demographics, and soon clinical notes, but all those first.
*  And that you can actually just repurpose just as you can repurpose your images from your camera
*  and your iPhone. And so this allows now tens of millions of consumers to potentially contribute
*  their data. And because there are alignment issues, medical alignment issues, not the
*  end of civilization alignment issues, there are different alignments in the way health care is
*  organized. I do think that asking patients for consent for use of their data will give us the
*  biggest buy-in because patients want their data to be used, but for the right reasons. And
*  I think that's a patient and human autonomy question. And that's why we're fortunate to be
*  in this era where more and more of our data has been liberated and is made available to us as
*  consumers. And I think in that mode, our AI assistants should get it from us rather than
*  from entities that may not be as well aligned with us. I regret only that we don't have a lot
*  more time to dig into this in even deeper detail, but the good news is you have written a whole book
*  on this. The book is The AI Revolution in Medicine, GPT-4 and Beyond. I really think it's an exemplary
*  study and applaud you for all your work on it. Professor Zach Kahane, thank you for being part
*  of the cognitive revolution. Nathan, thank you. And now I know which podcast to listen to.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omniki so much
*  that I invested in it and I recommend you use it too. Use CogRev to get a 10% discount.

---
Date Generated: November 01, 2024
Transcription Model: whisper medium 20231117
Length: 4649s
Video Keywords: []
Video Views: 36081
Video Rating: None
Video Description: 
---

# Regina Barzilay Deep Learning for Cancer Diagnosis and Treatment  Lex Fridman Podcast #40
**Lex Fridman:** [September 23, 2019](https://www.youtube.com/watch?v=x0-zGdlpTeg)
*  The following is a conversation with Regina Barzolet. She's a professor at MIT and a world
*  class researcher in natural language processing and applications of deep learning to chemistry
*  and oncology, or the use of deep learning for early diagnosis, prevention, and treatment of cancer.
*  She has also been recognized for teaching of several successful AI-related courses at MIT,
*  including the popular Introduction to Machine Learning course.
*  This is the Artificial Intelligence Podcast. If you enjoy it, subscribe on YouTube, give it five
*  stars on iTunes, support it on Patreon, or simply connect with me on Twitter at Lex Friedman,
*  spelled F-R-I-D-M-A-N. And now, here's my conversation with Regina Barzolet.
*  In an interview, you've mentioned that if there's one course you would take,
*  it would be a literature course with a friend of yours that a friend of yours teaches.
*  Just out of curiosity, because I couldn't find anything on it, are there books or ideas that had
*  profound impact on your life journey? Books and ideas perhaps outside of computer science and
*  the technical fields? I think because I'm spending a lot of my time at MIT, and previously in other
*  institutions where I was a student, I have a limited ability to interact with people. So a lot
*  of what I know about the world actually comes from books. And there were quite a number of books
*  that had profound impact on me and how I view the world. Let me just give you one example of such
*  a book. I've maybe a year ago read a book called The Emperor of All Melodies. It's a book about,
*  it's kind of a history of science book on how the treatments and drugs for cancer were developed.
*  And that book, despite the fact that I am in the business of science, really opened my eyes
*  on how imprecise and imperfect the discovery process is and how imperfect our current solutions
*  and what makes science succeed and be implemented. And sometimes it's actually not the strength of
*  the idea, but devotion of the person who wants to see it implemented. So this is one of the books
*  that, you know, at least for the last year quite changed the way I'm thinking about
*  scientific process just from the historical perspective. And what do I need to do to make my
*  ideas really implemented? Let me give you an example of a book, which is not kind of,
*  which is a fiction book. It's a book called Americana. And this is a book about a young female
*  student who comes from Africa to study in the United States. And it describes her past,
*  within her studies and her life transformation that, you know, in a new country and kind of
*  adaptation to a new culture. And when I read this book, I saw myself in many different points of it,
*  but it also kind of gave me the lens on different events and some of it that I never actually paid
*  attention. One of the funny stories in this book is how she arrives to her new college and she
*  starts speaking in English and she had this beautiful British accent because that's how she
*  was educated in her country. This is not my case. And then she notices that the person who talks to
*  her, you know, talks to her in a very funny way, in a very slow way. And she's thinking that this
*  woman is disabled and she's also trying to kind of accommodate her. And then after a while,
*  when she finishes her discussion with this officer from her college, she sees how she interacts with
*  other students, with American students, and she discovers that actually
*  she talked to her this way because she saw that she doesn't understand English.
*  And he said, wow, this is a funny experience. And literally within a few weeks, I went
*  to LA to a conference and I asked somebody in the airport, you know, how to find like a cab or
*  something. And then I noticed that this person is talking in a very strange way. And my first thought
*  this person has some, you know, pronunciation issues or something. And I'm trying to talk very
*  slowly to him and I was with another professor, Ernst Frankel, and he's like laughing because
*  it's funny that I don't get that the guy is talking in this way because he thinks that I
*  cannot speak. So it was really kind of a mirroring experience. And it let me think a lot about
*  my own experiences moving, you know, from different countries. So I think that books play
*  a big role in my understanding of the world. On the science question, you mentioned that
*  it made you discover that personalities of human beings are more important than perhaps ideas. Is
*  that what I heard? It's not necessarily that they are more important than ideas, but I think that
*  ideas on their own are not sufficient. And many times, at least at the local horizon,
*  it's the personalities and their devotion to their ideas is really that locally changes
*  the landscape. Now, if you're looking at AI, like, let's say 30 years ago, you know, dark ages of AI
*  or whatever, what is symbolic times, you can use any word. You know, there were some people,
*  now we are looking at a lot of that work and we are kind of thinking this is not really
*  maybe a relevant work. But you can see that some people managed to take it and to make it so shiny
*  and dominate the, you know, the academic world and make it to be the standard. If you look at
*  the area of natural language processing, it is well known fact that the reason the statistics
*  in NLP took such a long time to become mainstream because there were quite a number of personalities
*  which didn't believe in this idea and didn't stop research progress in this area. So I do not think
*  that, you know, kind of asymptotically, maybe personalities matters, but I think locally,
*  it does make quite a bit of impact. And it's generally, you know, speed up, speeds up the
*  rate of adoption of the new ideas. Yeah. And the other interesting question is in the early days
*  of particular discipline, I think you mentioned in that book was, is ultimately a book of cancer.
*  It's called the Emperor of All Melodies. Yeah. And those melodies included the trying to,
*  the medicine was the center. So it was actually centered on, you know, how people thought of
*  curing cancer. Like for me, it was really a discovery how people, what was the science of
*  chemistry behind drug development that it actually grew up out of dying, like coloring industry,
*  that people who developed chemistry in 19th century in Germany and Britain to do, you know,
*  the really new dyes, they looked at the molecules and identified that they do certain things to cells.
*  And from there, the process started and, you know, like historically saying, yeah, this is
*  fascinating that they managed to make the connection and look under the microscopes and do all these
*  discovery. But as you continue reading about it and you read about how chemotherapy drugs were
*  developed in Boston, and some of them were developed and Farber, Dr. Farber from Dana Farber,
*  you know, how the experiments were done, that, you know, there was some miscalculation, let's
*  put it this way, and they tried it on the patients and they just, and those were children with
*  leukemia and they died. And then they tried another modification. You look at the process,
*  how imperfect is this process? And, you know, like if we're again looking back like 60 years ago,
*  70 years ago, you can kind of understand it. But some of the stories in this book, which were really
*  shocking to me, were really happening, you know, maybe decades ago. And we still don't have a
*  vehicle to do it much more fast and effective and, you know, scientific the way I'm thinking,
*  computer science scientific. So from the perspective of computer science, you've gotten
*  a chance to work the application to cancer and to medicine in general. From a perspective of an
*  engineer and a computer scientist, how far along are we from understanding the human body biology
*  of being able to manipulate it in a way we can cure some of the maladies, some of the diseases?
*  So this is a very interesting question. And if you're thinking as a computer scientist about
*  this problem, I think one of the reasons that we succeeded in the areas we as a computer scientist
*  succeeded is because we don't have, we're not trying to understand in some ways. Like if you're
*  thinking about like e-commerce, Amazon, Amazon doesn't really understand you. And that's why it
*  recommends you certain books or certain products, correct? And traditionally when people were
*  thinking about marketing, you know, they divided the population to different kind of subgroups,
*  identify the features of this subgroup and come up with a strategy which is specific to that subgroup.
*  If you're looking about recommendations, they're not claiming that they're understanding somebody,
*  they're just managing from the patterns of your behavior to recommend your product.
*  Now, if you look at the traditional biology, and obviously I wouldn't say that I am at any
*  way educated in this field, but what I see is really a lot of emphasis on mechanistic understanding.
*  And it was very surprising to me coming from computer science how much emphasis is on this
*  understanding. And given the complexity of the system, maybe the deterministic full understanding
*  of these processes is beyond our capacity. And the same with computer science when we're doing
*  recognition, when doing recommendation and many other areas, it's just probabilistic matching
*  process. And in some way, maybe in certain cases, we shouldn't even attempt to understand, or we can
*  attempt to understand, but in parallel, we can actually do this kind of matching that would
*  help us to find cure or to do early diagnostics and so on. And I know that in these communities,
*  it's really important to understand, but I'm sometimes wondering, you know, what exactly
*  does it mean to understand here? Well, there's stuff that works, but that can be, like you said,
*  separate from this deep human desire to uncover the mysteries of the universe, of science, of the
*  way the body works, the way the mind works. It's the dream of symbolic AI, of being able to reduce
*  human knowledge into logic and be able to play with that logic in a way that's very explainable
*  and understandable for us humans. I mean, that's a beautiful dream. So I understand it, but it seems
*  that what seems to work today, and we'll talk about it more, is as much as possible reduce
*  stuff into data, reduce whatever problem you're interested in into data and try to apply
*  statistical methods, apply machine learning to that. On a personal note, you were diagnosed
*  with breast cancer in 2014. What did facing your mortality make you think about? How did it change
*  you? You know, this is a great question, and I think that I was interviewed many times, and nobody
*  actually asked me this question. I think I was 43 at the time, and the first time I realized in my
*  life that I may die, and I never thought about it before. And there was a long time since you
*  diagnosed until you actually know what you have and how severe is your disease. For me, it was like
*  maybe two and a half months. And I didn't know where I am during this time because I was getting
*  different tests, and one would say it's bad, and I would say no, it is not. So until I knew where I
*  am, I really was thinking about all these different possible outcomes. Were you imagining the worst,
*  or were you trying to be optimistic? It would be really, I don't remember, you know, what was
*  my thinking. It was really a mixture with many components at the time, speaking, you know,
*  in our terms. And one thing that I remember, and you know, every test comes and then you think,
*  oh, it could be this, or it may not be this, and you're hopeful, and then you're desperate. So it's
*  like there is a whole slew of emotions that go through you. But what I remember is that when I
*  came back to MIT, I was kind of going the whole time through the treatment to MIT,
*  but my brain was not really there. But when I came back, really finished my treatment, and I was here
*  teaching and everything, you know, I looked back at what my group was doing, what other groups were
*  doing, and I saw these trivialities. It's like people are building their careers on improving
*  some parts around two or three percent or whatever. And I was like, seriously, I did a work on how to
*  decipher Ugaritic, like a language that nobody speaks, and whatever. What is significance?
*  When all of a sudden, you know, I walked out of MIT, which is, you know, when people really do care,
*  you know, what happened to your ICLEAR paper, you know, what is your next publication, to ACL,
*  to the world where people, you know, you see a lot of suffering. I'm kind of totally shielded on it
*  on a daily basis. And it's like the first time I've seen like real life and real suffering.
*  And I was thinking, why are we trying to improve the parser or deal with some trivialities when
*  we have capacity to really make a change? And it was really challenging to me because on one hand,
*  you know, I have my graduate students who really want to do their papers and their work,
*  and they want to continue to do what they were doing, which was great. And then it was me who
*  really kind of reevaluated what is the importance. And also at that point, because I had to take some
*  break, I look back into like my years in science and I was thinking, you know, like 10 years ago,
*  this was the biggest thing, I don't know, topic models. We have like millions of papers on topic
*  models and variation of topics models. Now it's totally like irrelevant. And you start looking
*  at this, you know, what do you perceive as important at different point of time and how,
*  you know, it fades over time. And since we have a limited time, all of us have limited time on us,
*  it's really important to prioritize things that really matter to you, maybe matter to you at that
*  particular point, but it's important to take some time and understand what matters to you,
*  which may not necessarily be the same as what matters to the rest of your scientific community
*  and pursue that vision. So that moment, did it make you cognizant? You mentioned suffering of just
*  the general amount of suffering in the world. Is that what you're referring to? So as opposed
*  to topic models and specific detailed problems in NLP, did you start to think about other people
*  who have been diagnosed with cancer? Is that the way you saw the, started to see the world perhaps?
*  Oh, absolutely. And it actually creates because like, for instance, you know, there is parts of
*  the treatment where you need to go to the hospital every day and you see, you know, the community of
*  people that you see, and many of them are much worse than I was at the time. And you all of a
*  sudden see it all. And people who are happier someday just because they feel better. And for
*  people who are in our normal realm, you take it totally for granted that you feel well, that if
*  you decide to go running, you can go running and you can, you know, you're pretty much free to do
*  whatever you want with your body. Like I saw like a community, my community became those people.
*  And I remember one of my friends, Dina Katabi, took me to Prudential to buy me a gift for my
*  birthday. And it was like the first time in months that I went to kind of to see other people. And
*  I was like, wow, first of all, these people, you know, they are happy and they are laughing
*  and they're very different from this other my people. And second thing, I think it's totally
*  crazy. They're like laughing and wasting their money on some stupid gifts. And, you know,
*  they may die. They already may have cancer and they don't understand it. So you can really see
*  how the mind changes, that you can see that, you know, before that you can as didn't, you know,
*  that you're going to die. Of course I knew, but it was kind of a theoretical notion. It wasn't
*  something which was concrete. And at that point, when you really see it and see how little means
*  sometimes the system has to help them, you really feel that we need to take a lot of
*  our brilliance that we have here at MIT and translate it into something useful.
*  Yeah. And you still couldn't have a lot of definitions, but of course, alleviating,
*  suffering, alleviating, trying to cure cancer is a beautiful mission. So I of course know the
*  theoretically the notion of cancer, but just reading more and more about it's 1.7 million
*  new cancer cases in the United States every year, 600,000 cancer related deaths every year.
*  So this has a huge impact United States globally. When broadly, before we talk about how machine
*  learning, how MIT can help, when do you think we as a civilization will cure cancer?
*  How hard of a problem is it from everything you've learned from it recently?
*  I cannot really assess it. What I do believe will happen with the advancement in machine
*  learning is that a lot of types of cancer, we will be able to predict way early and more effectively
*  utilize existing treatments. I think, I hope at least that with all the advancements in AI and
*  drug discovery, we would be able to much faster find relevant molecules. What I'm not sure about
*  is how long it will take the medical establishment and regulatory bodies to kind of catch up and to
*  implement it. And I think this is a very big piece of puzzle that is currently not addressed.
*  That's the really interesting question. So first a small detail that I think the answer is yes, but
*  is cancer one of the diseases that when detected earlier, that significantly improves the outcomes?
*  So like, because we'll talk about there's the cure and then there is detection. And I think
*  where machine learning can really help is earlier detection. So does detection help?
*  Detection is crucial. For instance, the vast majority of pancreatic cancer patients are detected
*  at the stage that they are incurable. That's why they have such a terrible survival rate.
*  It's like just a few percent over five years. It's pretty much today a death sentence. But if you can
*  discover this disease early, there are mechanisms to treat it. And in fact, I know
*  a number of people who were diagnosed and saved just because they had food poisoning. They had
*  terrible food poisoning. They went to ER, they got scan. There were early signs on the scan. And
*  that would save their lives. But this wasn't really an accidental case. So as we become better,
*  we would be able to help too many more people that are likely to develop diseases. And I just
*  want to say that as I got more into this field, I realized that cancer is of course terrible disease.
*  There are really the whole slew of terrible diseases out there, like neurodegenerative diseases and
*  others. So we, of course, a lot of us are fixated on cancer just because it's so prevalent in our
*  society. And you see these people, there are a lot of patients with neurodegenerative diseases and
*  the kind of aging diseases that we still don't have a good solution for. And I felt as a computer
*  scientist, we kind of decided that it's other people's job to treat these diseases. Because
*  traditionally people in biology or in chemistry or MDs are the ones who are thinking about it.
*  And that's the kind of stuff paying attention. I think that it's really a wrong assumption and we
*  all need to join the battle. So how it seems like in cancer specifically, that there's a lot of ways
*  that machine learning can help. So what's the role of machine learning in the diagnosis of cancer?
*  So for many cancers today, we really don't know what is your likelihood to get cancer.
*  And for the vast majority of patients, especially on the younger patients,
*  it really comes as a surprise. Like for instance, for breast cancer, 80% of the patients are first
*  in their families. It's like me. And I never saw that I had any increased risk because nobody had
*  it in my family. And for some reason in my head, it was kind of inherited disease.
*  But even if I would pay attention, the models that currently, these very simplistic statistical
*  models that are currently used in clinical practice, they really don't give you an answer.
*  So you don't know. And the same true for pancreatic cancer, the same true for non-smoking lung cancer
*  and many others. So what machine learning can do here is utilize all this data to tell us
*  any who is likely to be susceptible and using all the information that is already there, be it imaging,
*  be it your other tests, and eventually liquid biopsies and others, where the signal itself
*  is not sufficiently strong for human eye to do good discrimination because the signal may be weak,
*  but by combining many sources, a machine which is trained on large volumes of data can really
*  detect it early. And that's what we've seen with breast cancer and people are reporting it in other
*  diseases as well. That really boils down to data, right? And in the different kinds of sources of
*  data. And you mentioned regulatory challenges. So what are the challenges in gathering large
*  data sets in this space? Again, another great question. So it took me after I decided that I
*  want to work on it two years to get access to data. Any data, like any significant amount.
*  Like right now in this country, there is no publicly available data set of modern mammograms
*  that you can just go on your computer, sign a document and get it. It just doesn't exist.
*  Obviously, every hospital has its own collection of mammograms. There are data that came out of
*  clinical trials. What we're talking about here is a computer scientist who just wants to run
*  his or her model and see how it works. This data, like ImageNet, doesn't exist.
*  There is a set which is called Florida Dataset, which is a film mammogram from the 90s,
*  which is totally not representative of the current developments. Whatever you're landing
*  on them doesn't scale up. This is the only resource that is available. And today there are many
*  agencies that govern access to data. Like the hospital holds your data and the hospital decides
*  whether they would give it to the researcher to work with this data. An individual hospital?
*  Yeah. I mean, the hospital may, assuming that you're doing research collaboration, you can
*  submit, there is a proper approval process guided by IRB. And if you go through all the processes,
*  you can eventually get access to the data. But if you yourself know our OEI community,
*  there are not that many people who actually ever got access to data because it's a very
*  challenging process. And sorry, just a quick comment. MGH or any kind of hospital,
*  are they scanning the data? Are they digitally storing it?
*  Oh, it is already digitally stored. You don't need to do any extra processing steps. It's already
*  there in the right format. Right now there are a lot of issues that govern access to the data
*  because the hospital is legally responsible for the data. And they have a lot to lose if they give
*  the data to the wrong person, but they may not have a lot to gain if they give it as a hospital,
*  as a legal entity, as giving it to you. And the way, what I would imagine happening in the future
*  is the same thing that happens when you're getting your driving license. You can decide whether you
*  want to donate your organs. You can imagine that whenever a person goes to the hospital,
*  it should be easy for them to donate their data for research. And it can be different. Do they
*  only give you a test results or only imaging data or the whole medical record? Because at the end,
*  we all will benefit from all this insights. And it's not like you say, I want to keep my data
*  private, but I would really love to get it from other people because other people are thinking
*  the same way. So if there is a mechanism to do this donation and the patient has an ability to
*  say how they want to use their data for research, it would be really a game changer.
*  People, when they think about this problem, it depends on the population, depends on the demographics,
*  but there's some privacy concerns generally, not just medical data, just any kind of data.
*  It's what you said, my data, it should belong to me. I'm worried how it's going to be misused.
*  How do we alleviate those concerns? Because that seems like a problem that needs to be
*  that problem of trust, of transparency needs to be solved before we build large data sets that help
*  detect cancer, help save those very people in the future.
*  I think there are two things that could be done. There is a technical solutions and there are
*  societal solutions. So on the technical end, we today have the ability to improve disambiguation.
*  For instance, for imaging, you can do it pretty well.
*  What's disambiguation?
*  And disambiguation, sorry, disambiguation, removing the identification, removing the names of the
*  people. There are other data, like if it is a raw text, you cannot really achieve 99.9%,
*  but there are all these techniques that actually some of them are developed at MIT.
*  How you can do learning on the encoded data where you locally encode the image, you train
*  on network, which only works on the encoded images, and then you send the outcome back to
*  the hospital and you can open it up. So those are the technical solutions. There are a lot of people
*  who are working in this space where the learning happens in the encoded form. We are still early,
*  but this is an interesting research area where I think we'll make more progress.
*  There is a lot of work in the natural language processing community, how to do
*  de-identification better. But even today, there is already a lot of data which can be
*  de-identified perfectly, like your test data, for instance, where you can just, you know,
*  the name of the patient, you just want to extract the part with the numbers. The big problem here
*  is again, hospitals don't see much incentive to give this data away on one hand, and then there
*  is general concern. Now, when I'm talking about societal benefits and about the education,
*  the public needs to understand that there are situations, and I still remember myself,
*  when I really needed an answer. I had to make a choice. There was no information to make a
*  choice. You're just guessing, and at that moment you feel that your life is at the stake, but you
*  just don't have information to make the choice. Many times when I give talks, I get emails from
*  women who say, you know, I'm in this situation. Can you please run statistics and see what are
*  the outcomes? We get almost every week a mammogram that comes by mail to my office at MIT. I'm serious
*  that people ask to run because they need to make life-changing decisions.
*  And of course, you know, I'm not planning to open a clinic here, but we do run and give them the
*  results for their doctors. But the point that I'm trying to make that we all at some point,
*  or our loved ones, will be in the situation where you need information to make the best choice.
*  And if this information is not available, you would feel vulnerable and unprotected. And then
*  the question is, you know, would do I care more? Because at the end, everything is a trade-off,
*  correct? Yeah, exactly. Just out of curiosity, it seems like one possible solution. I'd like to see
*  what you think of it based on what you just said, based on wanting to know answers for when you're
*  yourself in that situation. Is it possible for patients to own their data as opposed to hospitals
*  owning their data? Of course, theoretically, I guess patients own their data, but can you walk
*  out there with a USB stick containing everything or upload it to the cloud? Where a company,
*  you know, I remember Microsoft had a service, like I was really excited about, and Google Health was
*  there. I was excited about it. Basically, companies helping you upload your data to the cloud
*  so that you can move from hospital to hospital, from doctor to doctor. Do you see a promise of
*  that kind of possibility? I absolutely think this is, you know, the right way to exchange the data.
*  I don't know now who is the biggest player in this field, but I can clearly see that even for
*  totally selfish health reasons, when you are going to a new facility and many of us are sent to some
*  specialized treatment, they don't easily have access to your data. And today, you know,
*  we want to send this mammogram, need to go to the hospital, find some small office, which gives them
*  the CD and the ship as a CD. So you can imagine we're looking at kind of decades old mechanism
*  of data exchange. So I definitely think this is an area where hopefully all the right regulatory and
*  technical forces will align and we will see it actually implemented. It's sad because
*  unfortunately, and I have to research why that happened, but I'm pretty sure Google Health and
*  Microsoft Health Vault or whatever it's called both closed down, which means that there was either
*  regulatory pressure or there's not a business case or there's challenges from hospitals,
*  which is very disappointing. So when you say you don't know what the biggest players are,
*  the two biggest that I was aware of closed their doors. So I'm hoping I'd love to see why and I'd
*  love to see who else can come up. It seems like one of those Elon Musk style problems that are
*  obvious needs to be solved and somebody needs to step up and actually do this large scale data
*  collection. I know there is an initiative in Massachusetts, I think, actually led by the
*  governor to try to create this kind of health exchange system, at least to help people who
*  kind of when you show up in emergency room and there is no information about what are your
*  allergies and other things. So I don't know how far it will go, but another thing that you said,
*  and I find it very interesting is actually who are the successful players in this space and the
*  whole implementation. How does it go? To me, it is from the anthropological perspective,
*  it's more fascinating that AI that today goes in health care. We've seen so many attempts and so
*  very little successes and it's interesting to understand that I by no means have knowledge to
*  assess it, why we are in the position where we are. Yeah, it's interesting because data is really
*  fuel for a lot of successful applications and when that data requires regulatory approval,
*  like the FDA or any kind of approval, it seems that the computer scientists are not quite there
*  yet in being able to play the regulatory game, understanding the fundamentals of it.
*  I think that in many cases when even people do have data, we still don't know what exactly
*  do you need to demonstrate to change the standard of care. Let me give you an example related to my
*  breast cancer research. In traditional breast cancer risk assessment, there is something called
*  density, which determines the likelihood of a woman to get cancer. This pretty much says
*  how much white do you see on the mammogram? The whiter it is, the more likely the tissue is dense.
*  The idea behind density, it's not a bad idea, in 1967 a radiologist called Wolf decided to look
*  back at women who were diagnosed and see what is special in their images. Can we look back and say
*  that they are likely to develop? So he came up with some patterns. It was the best that his human
*  eye can identify. Then it was kind of formalized and coded into four categories and that's what
*  we are using today. Today, this density assessment is actually a federal law from 2019 approved by
*  President Trump and for the previous FDA commissioner, where women are supposed to be advised by their
*  providers if they have high density, putting them into higher risk category. In some states,
*  you can actually get supplementary screening paid by your insurance because you are in this category.
*  Now you can say how much science do we have behind it, whatever biological science or
*  epidemiological evidence. It turns out that between 40 and 50 percent of women have dense breasts.
*  Above 40 percent of patients are coming out of their screening and somebody tells them,
*  you are in high risk. Now, what exactly does it mean if you as half of the population in high risk,
*  it's from saying, maybe I'm not, or what do I really need to do with it? Because
*  the system doesn't provide me a lot of the solutions because there are so many people like me,
*  we cannot really provide very expensive solutions for them. The reason this whole density became
*  this big deal, it's actually advocated by the patients who felt very unprotected because many
*  women went in the mammograms which were normal and then it turns out that they already had cancer,
*  quite developed cancer, so they didn't have a way to know who is really at risk and what is the
*  likelihood that when the doctor tells you you're okay, you are not okay. So at the time, and it was
*  15 years ago, this maybe was the best piece of science that we had and it took quite 15-16 years
*  to make it federal law, but now this is a standard. Now with the deep learning model, we can so much
*  more accurately predict who is going to develop breast cancer just because you're trained on a
*  logical thing and instead of describing how much white and what kind of white machine can
*  systematically identify the patterns, which was the original idea behind the thought of the
*  cardiologist machine is can do it much more systematically and predict the risk when you're
*  trained the machine to look at the image and to say the risk in one to five years. Now you can ask
*  me how long it will take to substitute this density which is broadly used across the country and
*  really is not helping to bring these new models. And I would say it's not a matter of the algorithm.
*  Algorithms already orders of magnitude better than what is currently in practice. I think it's really
*  the question who do you need to convince? How many hospitals do you need to run the experiment?
*  All this mechanism of adoption and how do you explain to patients and to women across the country
*  that this is really a better measure? And again, I don't think it's an AI question. We can walk more
*  and make the algorithm even better, but I don't think that this is the current, you know, the
*  barrier. The barrier is really this other piece that for some reason is not really explored. It's
*  like anthropological piece. And coming back to your question about books, there is a book that I'm
*  reading. It's called American Sickness by Elizabeth Rosenthal. And I got this book from my
*  clinical collaborator, Dr. Konyi Lehmann. And I said, I know everything that I need to know about
*  American health system, but you know, every page doesn't fail to surprise me. And I think there is
*  a lot of interesting and really deep lessons for people like us from computer science who are coming
*  into this field to really understand how complex is the system of incentives in the system to
*  understand how you really need to play to drive adoption. You just said it's complex, but if we're
*  trying to simplify it, who do you think most likely would be successful if we push on this group of
*  people? Is it the doctors? Is it the hospitals? Is it the governments or policymakers? Is it the
*  individual patients, consumers who needs to be inspired to most likely lead to adoption? Or is
*  there no simple answer? There's no simple answer, but I think there is a lot of good people in
*  medical system who do want to make a change. And I think a lot of power will come from us as consumers
*  because we all are consumers or future consumers of health care services. And
*  I think we can do so much more in explaining the potential and not in the hype terms and not saying
*  that we now cured Alzheimer's and you know, I'm really sick of reading these kind of articles
*  which make these claims, but really to show with some examples what this implementation does and
*  how it changes the care. Because I can't imagine, doesn't matter what kind of politician it is,
*  we all are susceptible to these diseases. There is no one who is free and eventually we all
*  are humans and we are looking for a way to alleviate the suffering. And this is one possible way where
*  we currently are underutilizing, which I think can help. So it sounds like the biggest problems are
*  outside of AI in terms of the biggest impact at this point. But are there any open problems
*  in the application of ML to oncology in general? So improving the detection or any other creative
*  methods, whether it's on the detection segmentations or the vision perception side or some other clever
*  of inference. Yeah, what in general in your view are the open problems in this space?
*  I just want to mention that besides detection, another area where I am kind of quite active
*  and I think it's really an increasingly important area in healthcare is drug design.
*  Because it's fine if you detect something early, but you still need to get drugs and new drugs
*  for these conditions. And today all of the drug design, ML is non-existent there. We don't have
*  any drug that was developed by the ML model or even not developed, but at least even you,
*  that ML model plays some significant role. I think this area with all the new ability to
*  generate molecules with desired properties to do in silica screening is really a big open area.
*  To be totally honest with you, when we are doing diagnostics and imaging, primarily taking the
*  ideas that were developed for other areas and you're applying them with some adaptation,
*  the area of drug design is really technically interesting and exciting area. You need to
*  work a lot with graphs and capture various 3D properties. There are lots and lots of
*  opportunities to be technically creative. And I think there are a lot of open questions in this
*  area. We're already getting a lot of successes even with the first generation of these models,
*  but there are much more new creative things that you can do. And what's very nice to see is that
*  actually the more powerful, the more interesting models actually do do better. So there is a place
*  to innovate in machine learning in this area. And some of these techniques are really unique to,
*  let's say to graph generation and other things. So-
*  What, just to interrupt really quick, I'm sorry. Graph generation or graphs, drug discovery in
*  general, how do you discover a drug? Is this chemistry? Is this trying to predict different
*  chemical reactions or is it some kind of, what do graphs even represent in this space?
*  Oh, sorry. And what's a drug?
*  Okay. So let's say you're thinking there are many different types of drugs, but let's say you're
*  going to talk about small molecules because I think today the majority of drugs are small
*  molecules. So small molecule is a graph. The molecule is just where the node in the graph
*  is an atom and then you have the bond. So it's really a graph representation if you're looking
*  at it in 2D, correct? You can do it 3D, but let's say, well, let's keep it simple and stick in 2D.
*  So pretty much my understanding today how it is done at scale in the companies,
*  without machine learning, you have high throughput screening. So you know that you are interested to
*  get certain biological activity of the compound. So you scan a lot of compounds, like maybe hundreds
*  of thousands, some really big number of compounds. You identify some compounds which have the right
*  activity and then at this point, the chemists come and they're trying now to optimize this
*  original heat to different properties that you want it to be maybe soluble. You want to decrease
*  toxicity. You want it to decrease the side effects. Can that be done in simulation or just by looking
*  at the molecules or do you need to actually run reactions in real labs with lab clothes and stuff?
*  So when you do high throughput screening, you really do screening. It's in the lab. It's really
*  the lab screening. You screen the molecules, correct? I don't know what screening is.
*  The screening is just check them for certain property. Like in the physical space, in the
*  physical world. Like actually there's a machine probably that's doing some, that's actually running
*  the reaction. That's actually running the reactions. Yeah. So there is a process where you can run and
*  this is why it's called high throughput. It becomes cheaper and faster to do it in
*  very big number of molecules. You run the screening. You identify potential good starts.
*  And then where the chemists come in who have done it many times and then they can try to look at it
*  and say, how can you change the molecule to get the desired profile in terms of all other properties?
*  So maybe how do I make it more bioactive and so on? And there the creativity of the chemists
*  really is the one that determines the success of this design because again, they have a lot of
*  domain knowledge of what works, how do you decrease the CCD and so on. And that's what they do.
*  So all the drugs that are currently in the FDA approved drugs, even drugs that are in clinical
*  trials, they are designed using these domain experts, which goes through this combinatorial
*  space of molecules or graphs or whatever and find the right one or adjust it to be the right ones.
*  It sounds like the breast density heuristic from 67, the same echoes.
*  It's not necessarily that. It's really driven by deep understanding. It's not like they just
*  observe it. I mean, they do deeply understand chemistry and they do understand how different
*  groups and how does it change the properties. So there is a lot of science that gets into it
*  and a lot of kind of simulation. How do you want it to behave? It's very, very complex.
*  So they're quite effective at this design, obviously.
*  Now effective, yeah, we have drugs. Depending on how do you measure effective, if you measure
*  it in terms of cost, it's prohibitive. If you measure it in terms of times, we have lots of
*  diseases for which we don't have any drugs and we don't even know how to approach. I don't need to
*  mention few drugs or near degenerative disease drugs that fail. So there are lots of trials that
*  fail in later stages, which is really catastrophic from the financial perspective. So is it the
*  effective, the most effective mechanism? Absolutely no, but this is the only one that currently works.
*  And I would, you know, I was closely interacting with people in pharmaceutical industry. I was
*  really fascinated on how sharp and what a deep understanding of the domain do they have.
*  It's not observation driven. There is really a lot of science behind what they do. But if you ask me,
*  can machine learning change it? I firmly believe yes, because even the most experienced chemists
*  cannot, you know, hold in their memory and understanding everything that you can learn,
*  you know, from millions of molecules and reactions. And this space of graphs is a totally new space.
*  I mean, it's a really interesting space for machine learning to explore, graph generation.
*  Yeah. So there are a lot of things that you can do here. So we do a lot of work. So the first
*  tool that we started with was the tool that can predict properties of the molecules. So you can
*  just give the molecule and the property. It can be bioactivity property or it can be
*  some other property and you train the molecules and you can now take a new molecule and predict
*  this property. Now, when people started working in this area, it is something very simple. They do
*  kind of existing, you know, fingerprints, which is kind of handcrafted features of the molecule.
*  When you break the graph to substructures and then you run it in a feed-forward neural network.
*  And what was interesting to see that clearly, you know, this was not the most effective way to
*  proceed and you need to have much more complex models that can induce a representation, which
*  can translate this graph into the embeddings and do these predictions. So this is one direction.
*  Then another direction, which is kind of related, is not only to store by looking at the embedding
*  itself, but actually modify it to produce better molecules. So you can think about it
*  as the machine translation that you can start with a molecule and then there is an improved
*  version of molecule and you can again, with encoded, translate it into the hidden space
*  and then learn how to modify it to improve the, in some ways, version of the molecules. So that's,
*  it's kind of really exciting. We already have seen that the property prediction works pretty well and
*  now we are generating molecules and there is actually labs which are manufacturing this
*  molecule. So we'll see where it will get us. Okay. That's really exciting. That's a lot of
*  problems. Speaking of machine translation and embeddings, you do, you have done a lot of
*  really great research in NLP, natural language processing. Can you tell me your journey through
*  NLP? What ideas, problems, approaches were you working on? Were you fascinated with? Did you
*  explore before this magic of deep learning re-emerged and after? So when I started my work in
*  NLP, it was in 97. This was a very interesting time. It was exactly the time that I came to ACL
*  and at the time I could barely understand English, but it was exactly like the transition point
*  because half of the papers were really rule-based approaches where people took more kind of heavy
*  linguistic approaches for small domains and tried to build up from there. And then there were the
*  first generation of papers which were corpus-based papers and they were very simple in our terms
*  when you collect some statistics and do prediction based on them. But I found it really fascinating
*  one community can think so very differently about the problem. And I remember my first
*  papers that I wrote, it didn't have a single formula, it didn't have evaluation, it just had
*  examples of outputs. And this was the standard of the field at the time. In some ways, I mean,
*  people maybe just started emphasizing the empirical evaluation, but for many applications like
*  summarization, you just show some examples of outputs. And then increasingly you can see that
*  how the statistical approach has dominated the field and we've seen increased performance across
*  many basic tasks. The third part of the story maybe that if you look again through this journey,
*  we see that the role of linguistics in some ways greatly diminishes. And
*  I think that you really need to look through the whole proceeding to find one or two papers
*  which make some interesting linguistic references. It's really big.
*  You mean today.
*  Today, today. This was definitely not there.
*  So things like Syntactic Trees, just even basically against our conversation about
*  human understanding of language, which I guess what linguistics would be structured
*  hierarchical representing language in a way that's human explainable, understandable is missing.
*  You don't know if it is what is explainable and understandable. In the end, we perform functions
*  and it's okay to have machine which performs a function. Like when you're thinking about
*  your calculator, correct? Your calculator can do calculation very different from you who do
*  the calculation, but it's very effective in it. And this is fine. If we can achieve certain tasks
*  with high accuracy, it doesn't necessarily mean that it has to understand it the same way
*  as we understand it. In some ways, it's even naive to request because you have so many other sources
*  of information that are absent when you are training your system. So it's okay.
*  As it delivers it, and I will tell you one application that's really fascinating. In
*  1997, when I came to ACL, there were some papers on machine translation. They were like
*  primitive, like people were trying really, really simple. And the feeling, my feeling was that, you
*  know, to make real machine translation system, it's like to fly in the moon and build a house
*  and the garden and live happily ever after. I mean, it's like impossible. I never could imagine that
*  within, you know, 10 years, we would already see the system working. And now, you know, nobody is
*  even surprised to utilize the system on a daily basis. So this was like a huge, huge progress,
*  saying that people for a very long time tried to solve using other mechanisms and they were unable
*  to solve it. That's why I'm coming back to a question about biology. In linguistics, people
*  try to go this way and try to write the syntactic trees and try to obstruct it and to find the right
*  representation. And, you know, they couldn't get very far with this understanding while
*  these models using, you know, other sources actually capable to make a lot of progress.
*  Now, I'm not naive to think that we are in this paradise space in NLP. And sure as you know,
*  that when we slightly change the domain and when we decrease the amount of training, it can do like
*  really bizarre and funny thing. But I think it's just a matter of improving generalization capacity,
*  which is just a technical question. Wow. So that's the question. How much of language
*  understanding can be solved with deep neural networks? In your intuition, I mean, it's unknown,
*  I suppose. But as we start to creep towards romantic notions of the spirit of the Turing test
*  and conversation and dialogue and something that maybe to me or to us, so humans, feels like it
*  needs real understanding. How much can that be achieved with these neural networks or statistical
*  methods? So I guess I am very much driven by the outcomes. Can we achieve the performance,
*  which would be satisfactory for us for different tasks? Now, if you again look at machine
*  translation systems, which are trained on large amounts of data, they really can do a remarkable
*  job relatively to where they've been a few years ago. And if you project into the future, if it
*  will be the same speed of improvement, you know, this is great. Now, does it bother me that it's
*  not doing the same translation as we are doing now? If you go to cognitive science, we still don't
*  really understand what we are doing. I mean, there are a lot of theories and there is obviously a lot
*  of progress and studying, but our understanding what exactly goes on in our brains when we process
*  language is still not crystal clear and precise that we can translate it into machines. What does
*  bother me is that, you know, again, that machines can be extremely brittle when you go out of your
*  comfort zone of the, when there is a distributional shift between training and testing. And it has
*  been years and years, every year when a teacher in LP class, you know, I show them some examples
*  of translation from some newspaper in Hebrew, the way it was perfect. And then they have a recipe
*  that Tommy Yakalas' system sent me a while ago and it was written in Finnish of Carilian pies.
*  And it's just a terrible translation. You cannot understand anything what it does. It's like some
*  syntactic mistakes. It's just terrible. And year after year I tried it and will translate it in the
*  end after year. It does this terrible work because I guess, you know, the recipes are not a big part
*  of their training repertoire. So, but in terms of outcomes, that's a really clean, good way to look
*  at it. I guess the question I was asking is, do you think, imagine a future, do you think
*  the current approaches can pass the Turing test in the way, the, in the best possible formulation
*  of the Turing test? Would you want to have a conversation with a neural network for an hour?
*  Oh God, no. No, there are not that many people that I would want to talk for an hour.
*  But there are some people in this world, alive or not, that you would like to talk to for an hour.
*  Could a neural network achieve that outcome? So I think it would be really hard to create
*  a successful training set which would enable it to have a conversation for an hour.
*  Do you think it's a problem of data perhaps? I think in some ways it's a problem both of data
*  and the problem of the way we're training our systems, their ability to truly to generalize,
*  to be very compositional. In some ways it's limited, you know, in the current capacity, at least.
*  You know, we can translate well, we can, you know, find information well, we can extract
*  information. So there are many capacities in which it's doing very well. And you can ask me, would you
*  trust the machine to translate for you and use it as a source? I would say absolutely, especially if
*  we're talking about newspaper data or other data which is in the realm of its own training set,
*  I would say yes. But, you know, having conversations with the machine, it's not something that I would
*  choose to do. But, you know, I would tell you something, talking about Turing tests and about
*  all these kinds of ELISA conversations, I remember visiting Tencent in China and they have this
*  chat board and they claim that it's like really humongous amount of the local population which
*  like for hours talks to the chat board. To me it was, I cannot believe it, but apparently it's like
*  documented that there are some people who enjoy this conversation. And, you know, it brought to me
*  another MIT story about ELISA and Weizenbaum. I don't know if you're familiar with the story.
*  So Weizenbaum was a professor at MIT and when he developed this ELISA, which was just doing string
*  matching, very trivial, like restating of what you said with very few rules, no syntax. Apparently
*  there were secretaries at MIT that would sit for hours and converse with this trivial thing.
*  And at the time there was no beautiful interfaces, so you actually need to go through the pain of
*  communicating. And Weizenbaum himself was so horrified by this phenomena that people can
*  believe enough to the machine, you just need to give them the hint that machine understands you
*  and you can complete the rest. He kind of stopped this research and went into kind of trying to
*  understand what this artificial intelligence can do to our brains. So my point is, you know, how much
*  it's not how good is the technology, it's how ready we are to believe that it delivers the
*  goods that we are trying to get. That's a really beautiful way to put it. I, by the way,
*  I'm not horrified by that possibility, but inspired by it because, I mean, human connection,
*  whether it's through language or through love, it seems like it's very amenable to machine learning
*  and the rest is just challenges of psychology. Like you said, the secretaries who enjoy spending
*  hours. I would say I would describe most of our lives as enjoying spending hours with those we
*  love for very silly reasons. All we're doing is keyword matching as well. So I'm not sure how
*  much intelligence we exhibit to each other with the people we love that we're close with. So it's a
*  very interesting point of what it means to pass the Turing test with language. I think you're right.
*  In terms of conversation, I think machine translation has very clear performance and improvement,
*  what it means to have a fulfilling conversation is very person dependent and context dependent
*  and so on. That's very well put. But in your view, what's a benchmark in natural language,
*  a test that's just out of reach right now, but we might be able to, that's exciting.
*  Isn't perfecting machine translation or is it summarization? What's out there?
*  It goes across specific application. It's more about the ability to learn from few examples for
*  real, what we call fused short learning and all these cases. Because the way we publish these
*  papers today, we say, if we have like naively, we get 55, but now we had a few example and we can
*  move to 65. None of these methods actually realistically doing anything useful. You cannot
*  use them today. And the ability to be able to generalize and to move, or to be autonomous
*  in finding the data that you need to learn, to be able to perfect new task or new language.
*  This is an area where I think we really need to move forward to, and we are not yet there.
*  Are you at all excited, curious by the possibility of creating human level intelligence?
*  Is this, because you've been very in your discussion. So if we're looking at oncology,
*  you're trying to use machine learning to help the world in terms of alleviating suffering. If you
*  look at natural language processing, you're focused on the outcomes of improving practical things like
*  machine translation. But human level intelligence is a thing that our civilization has dreamed
*  about creating super human level intelligence. Do you think about this? Do you think it's at all
*  within our reach? So as you said yourself, Ellie, talking about how do you perceive
*  our communications with each other, that we're matching keywords and certain behaviors and so
*  on. So at the end, whenever one assesses, let's say, relations with another person, you have
*  separate kind of measurements and outcomes inside your head that determine what is the status of
*  the relation. So one way, this is this classical dilemma, what is the intelligence? Is it the fact
*  that now we are going to do the same way as human is doing when we don't even understand what the
*  human is doing? Or we now have an ability to deliver these outcomes, but not in one area,
*  not in an LPL, not just to translate or just to answer questions, but across many, many areas
*  that we can achieve the functionalities that humans can achieve with the ability to learn
*  and do other things. And this we can actually measure how far we are. And that's what makes
*  me excited that we, in my lifetime, at least so far, what we've seen is tremendous progress across
*  these different functionalities. And I think it will be really exciting to see where we will be.
*  And again, one way to think about it is there are machines which are improving their functionality.
*  Another one is to think about us with our brains, which are imperfect, how they can be accelerated
*  by this technology as it becomes stronger and stronger. Coming back to another book that I
*  love, Flowers for Algernon. Have you read this book?
*  Yes.
*  So there is this point that the patient gets this miracle cure, which changes his brain,
*  and all of a sudden they see life in a different way and can do certain things better, but certain
*  things much worse. So you can imagine this kind of computer-augmented cognition where it can bring
*  you that now, in the same way as the cars enable us to get to places where we've never been before,
*  can we think differently, can we think faster? And we already see a lot of it happening
*  in how it impacts us, but I think we have a long way to go there.
*  So that's sort of artificial intelligence and technology affecting our, augmenting our intelligence
*  as humans. Yesterday, a company called Neuralink announced, they did this whole demonstration,
*  I don't know if you saw it, they demonstrated brain-computer brain-machine interface,
*  where there's like a sewing machine for the brain. A lot of that is quite out there
*  in terms of things that some people would say are impossible, but they're dreamers and want
*  to engineer systems like that. Do you see, based on what you just said, a hope for that
*  more direct interaction with the brain?
*  I think there are different ways. One is a direct interaction with the brain, and again,
*  there are lots of companies that work in this space, and I think there will be a lot of
*  developments. But I'm just thinking that many times we are not aware of our feelings,
*  of motivation, what drives us. Let me give you a trivial example, our attention.
*  There are a lot of studies that demonstrate that it takes a while for a person to understand that
*  they are not attentive anymore, and we know that there are people who really have strong
*  capacity to hold attention. There are other end of the spectrum people with ADD and other issues
*  that they have problem to regulate their attention. Imagine to yourself that you have
*  like a cognitive aid that just alerts you based on your gaze, that your attention is now not on
*  what you are doing, and instead of writing a paper, you're now dreaming of what you're going
*  to do in the evening. So even this kind of simple measurement things, how they can change us,
*  and I see it even in simple ways with myself. I have my zone up that I got in MIT gym, it kind
*  of records how much did you run, and you have some points, and you can get some status, whatever.
*  Like I said, what is this ridiculous thing? Who would ever care about some status in some arm?
*  Guess what? So to maintain the status, you have to do set a number of points every month.
*  Not only is it that I do it every single month for the last 18 months, it went to the point that I
*  was running, that I was injured, and when I could run again, in two days, I did some humongous
*  amount of running just to complete the points. It was really not safe. It was like, I'm not going
*  to lose my status because I want to get there. So you can already see that this direct measurement
*  and the feedback is, we're looking at video games and see why the addiction aspect of it,
*  but you can imagine that the same idea can be expanded to many other areas of our life
*  when we really can get feedback. Imagine in your case in relations, when we're doing keyword
*  matching, imagine that the person who is generating the keywords, that person gets direct feedback
*  before the whole thing explodes. Maybe at this happy point, we are going in the wrong direction.
*  Maybe it will be really a behavior-modifying moment.
*  So yeah, it's a relationship management too. So yeah, that's a fascinating whole area of
*  psychology actually as well, of seeing how our behavior has changed with basically all human
*  relations now have other non-human entities helping us out. So you teach a large, a huge
*  machine learning course here at MIT. I could ask you a million questions, but you've seen a
*  lot of students. What ideas do students struggle with the most as they first enter this world of
*  machine learning? Actually, this year was the first time I started teaching a small machine
*  learning class and it came as a result of what I saw in my big machine learning class that Tommy
*  Yackle and I built maybe six years ago. What we've seen that as this area becomes more and more
*  popular, more and more people at MIT want to take this class. And while we designed it for computer
*  science majors, there were a lot of people who really are interested to learn it, but unfortunately
*  their background was not enabling them to do well in the class. And many of them associated
*  machine learning with the word struggle and failure, primarily for non-majors. And that's
*  why we actually started a new class which we call machine learning from algorithms to modeling, which
*  emphasizes more the modeling aspects of it and focuses on it has majors and non-majors. So we
*  kind of try to extract the relevant parts and make it more accessible because the fact that
*  we're teaching 20 classifiers in standard machine learning classes is really a big question we really
*  needed. But it was interesting to see this from first generation of students. When they came back
*  from their internships and from their jobs, what different and exciting things they can do that I
*  would never think that you can even apply machine learning to. Some of them are like matching
*  their relations and other things like variety of different applications. Everything is amenable
*  as the machine learning. That actually brings up an interesting point of computer science in general.
*  It almost seems, maybe I'm crazy, but it almost seems like everybody needs to learn how to program
*  these days. If you're 20 years old or if you're starting school, even if you're an English major,
*  it seems like programming unlocks so much possibility in this world. So when you
*  interacted with those non-majors, is there skills that they were simply
*  lacking at the time that you wish they had and that they learned in high school and so on?
*  How should education change in this computerized world that we live in?
*  The thing is because I knew that there is a Python component in the class.
*  Their Python skills were okay and the class isn't really heavy on programming. They primarily kind of
*  add parts to the programs. I think it was more of the mathematical barriers and the class
*  against wizard design on the majors was using the notation like big O for complexity and others.
*  People who come from different backgrounds just don't have it in the lexical. It's not necessarily
*  a very challenging notion, but they were just not aware. So I think that linear algebra and
*  probability, the basics, the calculus, multivariate calculus are things that can help.
*  What advice would you give to students interested in machine learning, interested, you've talked
*  about detecting, curing cancer, drug design. If they want to get into that field, what should they
*  do? Get into it and succeed as researchers and entrepreneurs. The first good piece of news
*  is that right now there are lots of resources that are created at different levels. You can find
*  online or in your school classes which are more mathematical, more applied and so on. You can find
*  a preacher which preaches your own language where you can enter the field and you can make
*  many different types of contribution depending on what is your strengths. The second point,
*  I think it's really important to find some area which you really care about and it can motivate
*  your learning. It can be for somebody curing cancer or doing self-driving cars or whatever.
*  To find an area where there is data, where you believe there are strong patterns and we should
*  be doing it and we're still not doing it or you can do it better and just start there and see
*  the way it can bring you. You've been very successful in many directions in life.
*  You also mentioned flowers of Argonon. I think I've read or listened to you mention somewhere
*  that researchers often get lost in the details of their work. This is per our original discussion
*  with cancer and so on. Don't look at the bigger picture, bigger questions of meaning and so on.
*  Let me ask you the impossible question. What's the meaning of this thing, of life,
*  of your life, of research? Why do you think we descendant of great apes are here on this spinning
*  ball? I don't think that I have really a global answer. Maybe that's why I didn't go to humanities
*  and I didn't take humanities classes in my undergrad.
*  But the way I'm thinking about it, that each one of us inside of them have their own set of
*  things that we believe are important. It just happens that we are busy with achieving various
*  goals, busy listening to others and to kind of try to conform and to be part of the crowd.
*  That we don't listen to that part. We all should find some time to understand what is our own
*  individual missions. We may have very different missions and to make sure that while we are
*  running 10,000 things, we are not missing out and we're putting all the resources to satisfy
*  our own mission. If I look over my time, when I was younger, most of these missions,
*  I was primarily driven by the external stimulus to achieve this, to be that. Now, a lot of what I do
*  is driven by really thinking what is important for me to achieve independently of the external
*  recognition. I don't mind to be viewed in certain ways. The most important thing for me
*  is to be true to myself, to what I think is right.
*  How long did it take? How hard was it to find the you that you have to be true to?
*  It takes time and even now sometimes the vanity and the triviality can take
*  everywhere. It's just the vanity at MIT is different, the vanity in different places,
*  but we all have our piece of vanity. I think actually for me, many times the place to get back
*  to it is when I'm alone and also when I read. I think by selecting the right people, I can
*  learn from what I read. But again, it's not perfect. Vanity sometimes dominates.
*  Well, that's a beautiful way to end. Thank you so much for talking today.
*  Thank you. That was fun.
*  It was fun.
---
Date Generated: November 01, 2024
Transcription Model: whisper medium 20231117
Length: 6251s
Video Keywords: []
Video Views: 129624
Video Rating: None
Video Description: 
---

# Jeremy Howard fast.ai Deep Learning Courses and Research  Lex Fridman Podcast #35
**Lex Fridman:** [August 27, 2019](https://www.youtube.com/watch?v=J6XcP4JOHmk)
*  The following is a conversation with Jeremy Howard. He's the founder of Fast AI, a research
*  institute dedicated to making deep learning more accessible. He's also a distinguished research
*  scientist at the University of San Francisco, a former president of Kaggle, as well as a top
*  ranking competitor there. And in general, he's a successful entrepreneur, educator, researcher,
*  and an inspiring personality in the AI community. When someone asks me, how do I get started with
*  deep learning? Fast AI is one of the top places I point them to. It's free, it's easy to get
*  started, it's insightful and accessible, and if I may say so, it has very little BS that can
*  sometimes dilute the value of educational content on popular topics like deep learning.
*  Fast AI has a focus on practical application of deep learning and hands-on exploration of the
*  cutting edge that is incredibly both accessible to beginners and useful to experts. This is the
*  Artificial Intelligence Podcast. If you enjoy it, subscribe on YouTube, give it five stars on
*  iTunes, support it on Patreon, or simply connect with me on Twitter at Lex Friedman, spelled F-R-I-D-M-A-N.
*  And now, here's my conversation with Jeremy Howard. What's the first program you ever written?
*  The first program I wrote that I remember would be at high school.
*  I did an assignment where I decided to try to find out if there were some better musical
*  scales than the normal 12-tone, 12-interval scale. So I wrote a program on my Commodore 64 in BASIC
*  that searched through other scale sizes to see if I could find one where there were more accurate
*  harmonies. Like mid-tone? Like you want an actual exactly three to two ratio, whereas with a 12
*  interval scale, it's not exactly three to two, for example. So that's well-tempered, as they say.
*  And BASIC on a Commodore 64. Yeah. Where was the interest in music from? Or is it just...
*  I did music all my life. So I played saxophone and clarinet and piano and guitar and drums and
*  whatever. How does that thread go through your life? Where's music today? It's not where I wish
*  it was. For various reasons, couldn't really keep it going, particularly because I had a lot of
*  problems with RSI with my fingers. And so I had to cut back anything that used hands and fingers.
*  I hope one day I'll be able to get back to it health-wise. So there's a love for music
*  underlying it all. What's your favorite instrument? Saxophone. Baritone saxophone.
*  Well, probably bass saxophone, but they're awkward. Well, I always love it when music is
*  coupled with programming. There's something about a brain that utilizes those that emerges with
*  creative ideas. So you've used and studied quite a few programming languages. Can you give an
*  overview of what you've used? What are the pros and cons of each?
*  My favorite programming environment almost certainly was Microsoft Access back in the
*  earliest days. So that was Visual Basic for applications, which is not a good programming
*  language, but the programming environment was fantastic. It's the ability to create
*  interfaces and tie data and actions to them and create reports and all that. I've never seen
*  anything as good. There's things nowadays like Airtable, which are like small subsets of that,
*  which people love for good reason, but unfortunately nobody's ever achieved anything like that.
*  What is that? If you could pause on that for a second. Access is a database program that
*  Microsoft produced, part of Office, and that kind of withered. But basically it lets you in a totally
*  graphical way, create tables and relationships and queries and tie them to forms and set up
*  event handlers and calculations. It was a very complete, powerful system designed for not massive
*  scalable things, but for useful little applications that I loved. So what's the connection between
*  Excel and Access? Very close. Access was the relational database equivalent, if you like.
*  People still do a lot of that stuff that should be in Access in Excel because they know it.
*  Excel's great as well, but it's just not as rich a programming model as VBA combined with a relational
*  database. I've always loved relational databases, but today programming on top of relational database
*  is just a lot more of a headache. You need something that runs some kind of database server
*  unless you use SQLite, which has its own issues. Then often if you want to get a nice programming
*  model, you only need to add an ORM on top. There's all these pieces to tie together,
*  and it's just a lot more awkward than it should be. There are people that are trying to make it
*  easier. In particular, I think of F-Sharp, Don Syme, who him and his team have done a great job of
*  making something like a database appear in the type system so you actually get tab completion for
*  fields and tables and stuff like that. Anyway, that whole VBA office thing I guess was a
*  starting point, which I still miss. I got into standard visual basic.
*  That's interesting just to pause on that for a second. It's interesting that you're connecting
*  the ease of management of data. In your use of programming languages, you always had a love
*  and a connection with data. I've always been interested in doing useful things for myself
*  and for others, which generally means getting some data and doing something with it and putting it
*  out there again. That's been my interest throughout. I also did a lot of stuff with
*  Apple script back in the early days. It's nice being able to get the computers to talk to each
*  other and to do things for you. Then I think that one of the programming language I most loved then
*  would have been Delphi, which was object Pascal created by Anders Halsberg, who previously did
*  Turbo Pascal and then went on to create .NET and then went on to create TypeScript.
*  Delphi was amazing because it was like a compiled, fast language that was as easy to use as visual
*  basic. Delphi, what is it similar to in more modern languages? Visual basic.
*  It's visual basic. Yeah, but a compiled fast version. I'm not sure there's anything quite
*  like it anymore. If you took C-sharp or Java and got rid of the virtual machine and replaced it
*  with something, you could compile a small type binary. I feel like it's where Swift could get to
*  with the new Swift UI and the cross-platform development going on. That's one of my dreams
*  is that we'll hopefully get back to where Delphi was. There is actually a free Pascal project
*  nowadays called Lazarus, which is also attempting to recreate Delphi. They're making good progress.
*  So okay, Delphi, that's one of your favorite programming languages.
*  Or at least programming environments. Again, Pascal's not a nice language. If you wanted to
*  know specifically about what languages I like, I would definitely pick J as being an amazingly
*  wonderful language. What's J? Are you aware of APL? I am not, except from doing a little research
*  on the work you've done. Okay, so not at all surprising you're not familiar with it because
*  it's not well known, but it's actually one of the main families of programming languages going back
*  to the late 50s, early 60s. So there was a couple of major directions. One was the kind of
*  Lambda Calculus Alonzo Church direction, which I guess kind of Lisp and Scheme and whatever,
*  which has a history going back to the early days of computing. The second was the kind of
*  imperative slash OO, algo, similar going on to C, C++, so forth. There was a third, which are
*  called array oriented languages, which started with a paper by a guy called Ken Iverson,
*  which was actually a math theory paper, not a programming paper. It was called
*  Notation as a Tool for Thought. And it was the development of a new type of math notation.
*  And the idea is that this math notation was much more flexible, expressive, and also well defined
*  than traditional math notation, which is none of those things. Math notation is awful.
*  And so he actually turned that into a programming language because this was the late 50s,
*  all the names were available. So he called his programming language or APL. So APL is an
*  implementation of notation as a tool for thought, by which he means math notation. And Ken and his
*  son went on to do many things, but eventually they actually produced a new language that was
*  built on top of all the learnings of APL, and that was called J. And J is the most expressive,
*  composable language, beautifully designed language I've ever seen.
*  Does it have object oriented components? Does it have that kind of thing?
*  Not really. It's an array oriented language. It's the third path.
*  Are you saying array?
*  Array oriented. What does it mean to be array oriented?
*  So array oriented means that you generally don't use any loops, but the whole thing is done with
*  kind of an extreme version of broadcasting, if you're familiar with that NumPy slash Python
*  concept. So you do a lot with one line of code. It looks a lot like math notation, highly compact.
*  And the idea is that you can kind of, because you can do so much with one line of code,
*  a single screen of code is very unlikely to, you very rarely need more than that to express
*  your program. And so you can kind of keep it all in your head and you can kind of clearly
*  communicate it. It's interesting that APL created two main branches, K and J. J is this kind of like
*  open source niche community of crazy enthusiasts like me. And then the other path, K, is fascinating.
*  It's an astonishingly expensive programming language, which many of the world's most
*  ludicrously rich hedge funds use. So the entire K machine is so small, it sits inside level three
*  cache on your CPU and it easily wins every benchmark I've ever seen in terms of data
*  processing speed. But you don't come across it very much because it's like $100,000 per CPU to
*  run it. But it's like this path of programming languages is just so much,
*  I don't know, so much more powerful in every way than the ones that almost anybody uses every day.
*  So it's all about computation. It's really focused on computation.
*  It's pretty heavily focused on computation. I mean, so much of programming is data processing by
*  definition. And so there's a lot of things you can do with it. But yeah, there's not much work
*  being done on making user interface toolkits or whatever. I mean, there's some, but they're not
*  great. At the same time, you've done a lot of stuff with Perl and Python. So where does that
*  fit into the picture of J and K and APL? Well, it's just much more pragmatic. In the end,
*  you kind of have to end up where the libraries are. Because to me, my focus is on productivity.
*  I just want to get stuff done and solve problems. So Perl was great. I created an email company
*  called FastMail. And Perl was great because back in the late 90s, early 2000s, it just had a lot
*  of stuff it could do. I still had to write my own monitoring system and my own web framework,
*  my own whatever, because none of that stuff existed. But it was a super flexible language
*  to do that in. And you used Perl for FastMail. You used it as a backend. So everything was written
*  in Perl? Yeah. Yeah. Everything. Everything was Perl. Why do you think Perl hasn't
*  succeeded or hasn't dominated the market, where Python really takes over a lot of the tasks?
*  Yeah. Well, I mean, Perl did dominate. It was everything everywhere. But then the guy that
*  ran Perl, Larry Wohl, just didn't put the time in anymore. And no project can be successful if
*  there isn't, you know, particularly one that started with a strong leader that loses that
*  strong leadership. So then Python has kind of replaced it. You know, Python is
*  a lot less elegant language in nearly every way, but it has the data science libraries.
*  And a lot of them are pretty great. So I kind of use it because it's the best we have,
*  but it's definitely not good enough. But what do you think the future of programming looks like?
*  What do you hope the future of programming looks like if we zoom in on the computational fields,
*  on data science, on machine learning? I hope Swift is successful
*  because the goal of Swift, the way Chris Latner describes it, is to be infinitely hackable. And
*  that's what I want. I want something where me and the people I do research with and my students can
*  look at and change everything from top to bottom. There's nothing mysterious and magical and
*  inaccessible. Unfortunately, with Python, it's the opposite of that because Python is so slow.
*  It's extremely unhackable. You get to a point where it's like, okay, from here on down at C.
*  So your debugger doesn't work in the same way. Your profiler doesn't work in the same way.
*  Your build system doesn't work in the same way. It's really not very hackable.
*  What's the part you like to be hackable? Is it for the objective of optimizing training of neural
*  networks, inference of neural networks? Is it performance of the system or is there some
*  non-performance related just creative ideas? It's everything. In the end, I want to be productive
*  as a practitioner. At the moment, our understanding of deep learning is incredibly primitive.
*  There's very little we understand. Most things don't work very well, even though it works better
*  than anything else out there. There's so many opportunities to make it better. You look at any
*  domain area like speech recognition with deep learning or natural language processing
*  classification with deep learning or whatever. Every time I look at an area with deep learning,
*  I always see like, oh, it's terrible. There's lots and lots of obviously stupid ways to do things
*  that need to be fixed. So then I want to be able to jump in there and quickly
*  experiment and make them better. Do you think the programming language
*  has a role in that? Huge role. Yeah. So currently, Python has a big gap in terms of our ability to
*  innovate particularly around recurrent neural networks and natural language processing
*  because it's so slow. The actual loop where we actually loop through words,
*  we have to do that whole thing in CUDA C. So we actually can't innovate with the kernel,
*  the heart of that most important algorithm. It's just a huge problem. This happens
*  all over the place. So we hit research limitations. Another example, convolutional neural
*  networks, which are actually the most popular architecture for lots of things, maybe most things
*  in deep learning. We almost certainly should be using sparse convolutional neural networks,
*  but only like two people are because to do it, you have to rewrite all of that CUDA C level stuff.
*  Yeah, just researchers and practitioners don't. So there's just big gaps in what people actually
*  research on, what people actually implement because of the programming language problem.
*  So you think it's just too difficult to write in CUDA C that a higher level programming language
*  like Swift should enable the easier fooling around creative stuff with RNNs or with sparse convolutional
*  neural networks. Who's at fault? Who's the charge of making it easy for a researcher to play around?
*  I mean, no one's at fault. It's just nobody's got around to it yet. It's just hard. And part of the
*  fault is that we ignored that whole APL kind of direction, most or nearly everybody did for
*  60 years, 50 years. But recently people have been starting to reinvent pieces of that and kind of
*  create some interesting new directions in the compiler technology. So the place where that's
*  particularly happening right now is something called MLIR, which is something that again,
*  Chris Latner, the Swift guy is leading. Because it's actually not going to be Swift on its own
*  that solves this problem because the problem is that currently writing an acceptably fast
*  GPU program is too complicated, regardless of what language you use.
*  And that's just because if you have to deal with the fact that I've got 10,000 threads and I have
*  to synchronize between them all and I have to put my thing into grid blocks and think about
*  whoops and all this stuff, it's just so much boilerplate that to do that well, you have to
*  be a specialist at that and it's going to be a year's work to optimize that algorithm in that way.
*  But with things like tensor comprehensions and tile and MLIR and TVM, there's all these various
*  projects which are all about saying, let's let people create domain specific languages for
*  tensor computations. These are the kinds of things we do generally on the GPU for deep learning.
*  And then have a compiler which can optimize that tensor computation. A lot of this work is actually
*  sitting on top of a project called Halide, which is a mind blowing project where they came up with
*  such a domain specific language. In fact, two, one domain specific language for expressing,
*  this is what my tensor computation is. And another domain specific language for expressing,
*  this is the way I want you to structure the compilation of that, do it block by block and
*  do these bits in parallel. And they were able to show how you can compress the amount of code by
*  10x compared to optimized GPU code and get the same performance. So these other things are
*  sitting on top of that kind of research and MLIR is pulling a lot of those best practices together.
*  And now we're starting to see work done on making all of that directly accessible through Swift
*  so that I could use Swift to kind of write those domain specific
*  languages. And hopefully we'll get then Swift CUDA kernels written in a very expressive and
*  concise way that looks a bit like J and APL and then Swift layers on top of that. And then a Swift
*  UI on top of that. And it'll be so nice if we can get to that point.
*  Now does it all eventually boil down to CUDA and NVIDIA GPUs?
*  Unfortunately at the moment it does, but one of the nice things about MLIR, if AMD ever gets
*  their act together, which they probably won't, is that they or others could write MLIR backends for
*  other GPUs or other tensor computation devices of which today there are increasing number,
*  like Graphcore or Vertex AI or whatever. So yeah, being able to target lots of backends
*  would be another benefit of this and the market really needs competition because at the moment
*  NVIDIA is massively overcharging for their kind of enterprise class cards because there is no
*  serious competition because nobody else is doing the software properly.
*  In the cloud there is some competition, right? But...
*  Not really, other than TPUs perhaps, but TPUs are almost unprogrammable at the moment.
*  You can't, the TPUs has the same problem that you can't.
*  It's even worse. So TPUs, Google actually made an explicit decision to make them
*  almost entirely unprogrammable because they felt that there was too much IP in there and if they
*  gave people direct access to program them, people would learn their secrets. So you can't
*  actually directly program the memory in a TPU. You can't even directly create code that runs on
*  and that you look at on the machine that has the GPU. It all goes through a virtual machine.
*  So all you can really do is this kind of cookie cutter thing of like plug-in high level stuff
*  together, which is just super tedious and annoying and totally unnecessary.
*  So what was the, tell me if you could, the origin story of Fast AI.
*  What is the motivation, its mission, its dream?
*  So I guess the founding story is heavily tied to my previous startup, which is a company called
*  Enlytic, which was the first company to focus on deep learning for medicine. And I created that
*  because I saw there was a huge opportunity to, there's about a 10X shortage of the number of
*  doctors in the world and the developing world that we need. I expected it would take about
*  300 years to train enough doctors to meet that gap. But I guessed that maybe if we used
*  deep learning for some of the analytics, we could maybe make it so you don't need as highly trained
*  doctors for diagnosis and treatment planning. Where's the biggest benefit just before we get
*  to Fast AI? Where's the biggest benefit of AI in medicine that you see today?
*  And not much happening today in terms of like stuff that's actually out there. It's very early,
*  but in terms of the opportunity, it's to take markets like India and China and Indonesia,
*  which have big populations, Africa, small numbers of doctors,
*  and provide diagnostic, particularly treatment planning and triage kind of on device so that
*  if you do a test for malaria or tuberculosis or whatever, you immediately get something that even
*  a healthcare worker that's had a month of training can get a very high quality assessment of whether
*  the patient might be at risk and tell, okay, we'll send them off to a hospital. So for example,
*  in Africa, outside of South Africa, there's only five pediatric radiologists for the entire continent.
*  So most countries don't have any. So if your kid is sick and they need something diagnosed through
*  medical imaging, the person, even if you're able to get medical imaging done, the person that looks
*  at it will be a nurse at best. But actually in India, for example, and China, almost no X-rays
*  are read by anybody, by any trained professional because they don't have enough. So if instead we
*  had an algorithm that could take the most likely high risk 5% and say triage, basically say, okay,
*  someone needs to look at this. It would massively change the kind of way that what's possible with
*  medicine in the developing world. And remember they have, increasingly they have money,
*  they're the developing world, they're not the poor world, they're developing world. So they have the
*  money. So they're building the hospitals, they're getting the diagnostic equipment,
*  but they just, there's no way for a very long time, will they be able to have the expertise.
*  LW Okay. And that's where the deep learning systems can step in and
*  magnify the expertise they do have. So you do see just to linger it a little bit longer,
*  the interaction, do you still see the human experts still at the core of these systems?
*  LW Yeah, absolutely. LW Is there something in medicine that can be automated almost completely?
*  LW I don't see the point of even thinking about that because we have such a shortage of people.
*  Why would we want to find a way not to use them? Like we have people, so the idea of like,
*  even from an economic point of view, if you can make them 10X more productive,
*  getting rid of the person doesn't impact your unit economics at all. And it totally allows the fact
*  that there are things people do better than machines. So it's just to me, that's not a useful
*  way of framing the problem. LW I guess, just to clarify, I guess I meant there may be some
*  problems where you can avoid even going to the expert ever, sort of maybe preventative care,
*  or some basic stuff, low hanging fruit, allowing the expert to focus on the things that are
*  really that- LW Well, that's what the triage would do, right? So the triage would say,
*  okay, 99% sure there's nothing here. So that can be done on device and they can just say, okay,
*  go home. So the experts are being used to look at the stuff which has some chance it's worth
*  looking at, which most things is not, you know, it's fine. LW Why do you think we haven't quite
*  made progress on that yet in terms of the scale of how much AI is applied in the medical field?
*  LW Oh, there's a lot of reasons. I mean, mine is it's pretty new. I only started
*  in Liddick in like 2014 and before that, like, it's hard to express to what degree the medical
*  world was not aware of the opportunities here. So I went to RSNA, which is the world's largest
*  radiology conference. And I told everybody I could, you know, like, I'm doing this thing
*  with deep learning, please come and check it out. And no one had any idea what I was talking about,
*  and no one had any interest in it. So like, we've come from absolute zero, which is hard.
*  And then the whole regulatory framework, education system, everything is just
*  set up to think of doctoring in a very different way. So today, there is a small number of people
*  who are deep learning practitioners and doctors at the same time. And we started to see the first
*  ones come out of their PhD programs. So Zach Kahane over in Boston, Cambridge has a number of
*  students now who are data science experts, deep learning experts and actual medical doctors.
*  Quite a few doctors have completed our fast AI course now and are publishing papers and creating
*  journal reading groups in the American Council of Radiology. And like, it's just starting to happen,
*  but it's going to be a long process. The regulators have to learn how to regulate this. They have to
*  build guidelines. And then the lawyers at hospitals have to develop a new way of understanding that
*  data. Sometimes it makes sense for data to be
*  looked at in raw form in large quantities in order to create well-changing results.
*  Yeah. So regulation around data, all that, it sounds probably the hardest problem,
*  but sounds reminiscent of autonomous vehicles as well. Many of the same regulatory challenges,
*  many of the same data challenges. Yeah. I mean, funnily enough, the problem is
*  less the regulation and more the interpretation of that regulation by lawyers in hospitals. So
*  HIPAA was actually designed to be, and HIPAA does not stand for privacy, it stands for portability.
*  It's actually meant to be a way that data can be used. And it was created with lots of gray areas
*  because the idea is that would be more practical and would help people to use this legislation to
*  actually share data in a more thoughtful way. Unfortunately, it's done the opposite because
*  when a lawyer sees a gray area, they see, oh, if we don't know, we won't get sued, then we can't do
*  it. So HIPAA is not exactly the problem. The problem is more that hospital lawyers are not
*  incented to make bold decisions about data portability. Or even to embrace technology
*  that saves lives. They more want to not get in trouble for embracing that technology.
*  Right. It also saves lives in a very abstract way, which is like, oh, we've been able to release
*  these 100,000 anonymized records. I can't point at the specific person whose life that saved.
*  I can say like, oh, we ended up with this paper, which found this result, which diagnosed a thousand
*  more people than we would have otherwise, but it's like, which ones were helped. It's very abstract.
*  And on the conner side of that, you may be able to point to a life that was taken because of
*  something that was... Yeah. Or a person whose privacy was violated. It's like, oh, this specific
*  person was de-identified. So just a fascinating topic. We're jumping around. We'll get back to
*  Fast AI, but on the question of privacy, data is the fuel for so much innovation in deep learning.
*  What's your sense on privacy, whether we're talking about Twitter, Facebook,
*  YouTube, just the technologies like in the medical field that rely on people's data in order to
*  create impact. How do we get that right? Respecting people's privacy and yet creating
*  technology that is learned from data. One of my areas of focus is on doing more with less data,
*  which... So most vendors, unfortunately, are strongly incented to find ways to require more
*  data and more computation. So Google and IBM being the most obvious... IBM. Yeah. So Watson.
*  Google and IBM both strongly push the idea that they have more data and more computation and more
*  intelligent people than anybody else. And so you have to trust them to do things because nobody
*  else can do it. And Google's very upfront about this. Like, Jeff Dehn has gone out there and given
*  talks and said, our goal is to require a thousand times more computation, but less people. Our goal
*  is to use the people that you have better and the data you have better and the computation you have
*  better. So one of the things that we've discovered is, or at least highlighted, is that you very,
*  very, very often don't need much data at all. And so the data you already have in your organization
*  will be enough to get state of the art results. So like my starting point would be to kind of say
*  around privacy is a lot of people are looking for ways to share data and aggregate data,
*  but I think often that's unnecessary. They assume that they need more data than they do because
*  they're not familiar with the basics of transfer learning, which is this critical technique for
*  needing orders of magnitude less data. Is your sense one reason you might want to
*  collect data from everyone is like in the recommender system context where your individual,
*  Jeremy Howard's individual data is the most useful for providing a product that's impactful
*  for you. So for giving you advertisements, for recommending to you movies, for doing medical
*  diagnosis, is your sense we can build with a small amount of data, general models that will
*  have a huge impact for most people that we don't need to have data from each individual?
*  On the whole, I'd say yes. I mean, there are things like,
*  recommender systems have this cold start problem where Jeremy is a new customer. We haven't seen
*  him before, so we can't recommend him things based on what else he's bought and liked with us.
*  And there's various workarounds to that. A lot of music programs will start out by saying,
*  which of these artists do you like? Which of these albums do you like? Which of these songs
*  do you like? Netflix used to do that. Nowadays, they tend not to. People kind of don't like that
*  because they think, oh, we don't want to bother the user. So you could work around that by having
*  some kind of data sharing where you get my marketing record from Axiom or whatever and
*  try to guess from that. To me, the benefit to me and to society of saving me five minutes on
*  answering some questions versus the negative externalities of the privacy issue doesn't add
*  up. So I think a lot of the time, the places where people are invading our privacy in order
*  to provide convenience is really about just trying to make them more money and they move these
*  negative externalities to places that they don't have to pay for them. So when you actually see
*  regulations appear that actually cause the companies that create these negative
*  externalities to have to pay for it themselves, they say, well, we can't do it anymore. So the
*  cost is actually too high. But for something like medicine, yeah, I mean, the hospital
*  has my medical imaging, my pathology studies, my medical records. And also I own my medical data.
*  So I help a startup called Doc.ai. One of the things Doc.ai does is that it has an app
*  you can connect to, you know, Sutter Health and LabCorp and Walgreens and download your medical
*  data to your phone and then upload it again at your discretion to share it as you wish.
*  So with that kind of approach, we can share our medical information with the people we want to.
*  Yeah. So control, I mean, really being able to control who you share with and so on.
*  So that has a beautiful, interesting tangent, but to return back to the origin story of Fast.ai.
*  Right. So before I started Fast.ai, I spent a year researching where are the biggest opportunities
*  for deep learning because I knew from my time at Kaggle in particular that deep learning had kind
*  of hit this threshold point where it was rapidly becoming the state of the art approach in every
*  area that looked at it. And I'd been working with neural nets for over 20 years. I knew that from a
*  theoretical point of view, once it hit that point, it would do that in kind of just about every domain.
*  And so I kind of spent a year researching what are the domains that's going to have the biggest
*  low-hanging fruit in the shortest time period. I picked medicine, but there were so many I could
*  have picked. And so there was a kind of level of frustration for me of like, okay, I'm really glad
*  we've opened up the medical deep learning world and today it's huge as you know, but we can't do,
*  you know, I can't do everything. I don't even know like, like in medicine, it took me a really long
*  time to even get a sense of like, what kind of problems do medical practitioners solve? What
*  kind of data do they have? Who has that data? So I kind of felt like I need to approach this
*  differently if I want to maximize the positive impact of deep learning. Rather than me picking
*  an area and trying to become good at it and building something, I should let people who
*  are already domain experts in those areas and who already have the data do it themselves.
*  So that was the reason for Fast AI is to basically try and figure out how to get deep learning
*  into the hands of people who could benefit from it and help them to do so in as quick and easy
*  and effective a way as possible. Got it. So sort of empower the domain experts. Yeah. And like,
*  partly it's because like, unlike most people in this field, my background is very applied
*  and industrial. Like my first job was at McKinsey and Company. I spent 10 years in management
*  consulting. I spend a lot of time with domain experts, you know, so I kind of respect them
*  and appreciate them and I know that's where the value generation in society is. And so I also know
*  how most of them can't code and most of them don't have the time to invest, you know,
*  three years in a graduate degree or whatever. So it's like, how do I upskill those domain experts?
*  I think that would be a super powerful thing, you know, biggest societal impact I could have.
*  So yeah, that was the thinking. So much of Fast AI students and researchers and the things you teach
*  are pragmatically minded, practically minded, figuring out ways how to solve real problems and
*  fast. So from your experience, what's the difference between theory and practice of deep learning?
*  Well, most of the research in the deep learning world is a total waste of time. Right. That's
*  what I was getting at. Yeah. It's a problem in science in general. Scientists need to be published,
*  which means they need to work on things that their peers are extremely familiar with and can
*  recognize in advance in that area. So that means that they all need to work on the same thing.
*  And so it really, and the thing they work on, there's nothing to encourage them to work on
*  things that are practically useful. So you get just a whole lot of research, which is minor
*  advances and stuff that's been very highly studied and has no significant practical impact.
*  Whereas the things that really make a difference, like I mentioned transfer learning, like if we
*  can do better at transfer learning, then it's this like world changing thing where suddenly like
*  lots more people can do world-class work with less resources and less data. And
*  but almost nobody works on that or another example, active learning, which is the study
*  of like, how do we get more out of the human beings in the loop? That's my favorite topic.
*  Yeah. So active learning is great, but it's almost nobody working on it because it's just not a
*  trendy thing right now. You know what somebody's sorry, sorry to interrupt.
*  He was saying that nobody is publishing on active learning, but there's people inside companies,
*  anybody who actually has to solve a problem, they're going to innovate on active learning.
*  Yeah. Everybody kind of reinvents active learning when they actually have to work in practice,
*  because they start labeling things and they think, gosh, this is taking a long time and it's very
*  expensive. And then they start thinking, well, why am I labeling everything? I'm only, the machine's
*  only making mistakes on those two classes. They're the hard ones. Maybe I'll just start labeling
*  those two classes. And then you start thinking, well, why did I do that manually? Why can't I
*  just get the system to tell me which things are going to be hardest? It's an obvious thing to do,
*  but yeah, it's just like transfer learning. It's understudied and the academic world just has no
*  reason to care about practical results. The funny thing is, like I've only really ever
*  written one paper. I hate writing papers. I didn't even write it. It was my colleague,
*  Sebastian Rutter, who actually wrote it. I just did the research for it, but it was basically
*  introducing successful transfer learning to NLP for the first time. The algorithm is called ULMFIT.
*  And I actually wrote it for the course, for the first day of the course. I wanted to teach
*  people NLP and I thought I only want to teach people practical stuff. And I think the only
*  practical stuff is transfer learning. And I couldn't find any examples of transfer learning
*  in NLP, so I just did it. And I was shocked to find that as soon as I did it, which, you know,
*  the basic prototype took a couple of days, smashed the state of the art on one of the most important
*  data sets in a field that I knew nothing about. And I just thought, well, this is ridiculous.
*  And so I spoke to Sebastian about it and he kindly offered to write it up, the results. And so it
*  ended up being published in ACL, which is the top computational linguistics conference.
*  So like people do actually care once you do it, but I guess it's difficult for maybe like
*  junior researchers or like, I don't care whether I get citations or papers or whatever. There's
*  nothing in my life that makes that important, which is why I've never actually bothered to
*  write a paper myself. But for people who do, I guess they have to pick the kind of safe
*  option, which is like, yeah, make a slight improvement on something that everybody's
*  already working on. Yeah. Nobody does anything interesting or succeeds in life with the safe
*  option. Although I mean, the nice thing is nowadays everybody is now working on NLP transfer
*  learning. Cause since that time we've had GPT and GPT2 and BERT and you know, it's like, it's so,
*  yeah, once you show that something's possible, everybody jumps in, I guess. So I hope, hope to
*  be a part of, and I hope to see more innovation and active learning in the same way. I think
*  both transfer learning and active learning are fascinating. Public open work. I actually helped
*  start a startup called Platform AI, which is really all about active learning. And yeah,
*  it's been interesting trying to kind of see what research is out there and make the most of it.
*  And there's basically none. So we've had to do all our own research. Once again, and just as you
*  described, can you tell the story of the Stanford competition Dawnbench and Fast AI's achievement
*  on it? Sure. So something which I really enjoy is that I basically teach two courses a year.
*  The practical deep learning for coders, which is kind of the introductory course, and then cutting
*  edge deep learning for coders, which is the kind of research level course. And while I teach those
*  courses, I have a, I basically have a big office at the University of San Francisco, big enough for
*  like 30 people. And I invite anybody, any student who wants to come and hang out with me while I
*  build the course. And so generally it's full. And so we have 20 or 30 people in a big office
*  with nothing to do but study deep learning. So it was during one of these times that somebody in
*  the group said, oh, there's a thing called Dawnbench that looks interesting. And I was like,
*  what the hell is that? And they set out some competition to see how quickly you can train
*  a model. Seems kind of not exactly relevant to what we're doing, but it sounds like the kind
*  of thing which you might be interested in. And I checked it out and I was like, oh crap,
*  there's only 10 days till it's over. It's pretty much too late. And we're kind of busy trying to
*  teach this course. But we're like, oh, it would make an interesting case study for the course.
*  Like it's all the stuff we're already doing. Why don't we just put together our current best
*  practices and ideas? So me and I guess about four students just decided to give it a go. And we
*  focused on this small one called CyPhar 10, which is little 32 by 32 pixel images.
*  Can you say what Dawnbench is? Yeah. So it's a competition to train a model as fast as possible.
*  It was run by Stanford. And it's cheap as possible too. That's also another one for as cheap as
*  possible. And there was a couple of categories, ImageNet and CyPhar 10. So ImageNet is this big
*  1.3 million image thing that took a couple of days to train. I remember a friend of mine,
*  Pete Warden, who's now at Google. I remember he told me how he trained ImageNet a few years ago,
*  and he basically had this little granny flat out the back that he turned into his ImageNet
*  training center. And after a year of work, he figured out how to train it in 10 days or something.
*  It's like that was a big job. Well, CyPhar 10, at that time, you could train in a few hours.
*  It was much smaller and easier. So we thought we'd try CyPhar 10.
*  And yeah, I've really never done that before. Things like using more than one GPU at a time
*  was something I tried to avoid because to me it's very against the whole idea of accessibility is
*  should be to do things with one GPU. I mean, have you asked in the past before,
*  after having accomplished something, how do I do this faster, much faster?
*  Always. But for me, it's always how do I make it much faster on a single GPU that a normal
*  person could afford in their day-to-day life? It's not how could I do it faster by having a
*  huge data center? Because to me, it's all about as many people should be able to use something as
*  possible without fussing around with infrastructure. So anyway, so in this case, it's like, well,
*  we can use eight GPUs just by renting an AWS machine. So we thought we'd try that. And yeah,
*  basically using the stuff we were already doing, we were able to get the speed. Within a few days,
*  we had the speed down to a very small number of minutes. I can't remember exactly how many
*  minutes it was, but it might've been like 10 minutes or something. And so yeah, we found
*  ourselves at the top of the leaderboard easily for both time and money, which really shocked me
*  because the other people competing in this were like Google and Intel and stuff where I like know
*  a lot more about this stuff than I think we do. So then we emboldened, we thought,
*  let's try the ImageNet one too. I mean, it seemed way out of our league, but our goal was to get
*  under 12 hours. And we did, which was really exciting. But we didn't put anything up on the
*  leaderboard, but we were down to like 10 hours. But then Google put in like five hours or something
*  and we're just like, oh, we're so screwed. But we kind of thought, we'll keep trying. If Google can
*  do it in five, I mean, Google did on five hours on like a TPU pod or something, like a lot of hardware.
*  But we kind of had a bunch of ideas to try. A really simple thing was, why are we using
*  these big images? They're like 224, 256 by 256 pixels. Why don't we try smaller ones?
*  And just to elaborate, there's a constraint on the accuracy that your trained model is supposed to
*  achieve. Yeah, you've got to achieve 93%, I think it was for ImageNet. Exactly. Which is very tough.
*  So you have to- Yeah, 93%. Like they picked a good threshold. It was a little bit higher
*  than what the most commonly used ResNet-50 model could achieve at that time. So yeah,
*  so it's quite a difficult problem to solve. But yeah, we realized if we actually just use 64 by 64 images,
*  it trained a pretty good model. And then we could take that same model and just give it a couple of
*  epochs to learn 224 by 224 images. And it was basically already trained. It makes a lot of sense.
*  If you teach somebody, here's what a dog looks like, and you show them low-res versions,
*  and then you say, here's a really clear picture of a dog, they already know what a dog looks like.
*  So that just, we jumped to the front and we ended up winning
*  parts of that competition. We actually ended up doing a distributed version over multiple machines
*  a couple of months later and ended up at the top of the leaderboard. We had 18 minutes.
*  Yeah. And people have just kept on blasting through again and again since then. So what's
*  your view on multi-GPU or multiple machine training in general as a way to speed code up?
*  I think it's largely a waste of time. Both multi-GPU on a single machine and...
*  Yeah, particularly multi-machines because it's just clunky.
*  Multi-GPUs is less clunky than it used to be, but to me, anything that slows down your
*  iteration speed is a waste of time. So you could maybe do your very last
*  perfecting of the model on multi-GPUs if you need to. So for example, I think doing stuff on ImageNet
*  is generally a waste of time. Why test things on 1.3 million images? Most of us don't use 1.3 million
*  images. And we've also done research that shows that doing things on a smaller subset of images
*  gives you the same relative answers anyway. So from a research point of view, why waste that time?
*  So actually I released a couple of new datasets recently. One is called ImageNet, the French
*  ImageNet, which is a small subset of ImageNet, which is designed to be easy to classify.
*  What's... How do you spell ImageNet?
*  It's got an extra T and E at the end because it's very French.
*  And then another one called ImageWolf, which is a subset of ImageNet that only contains dog breeds.
*  That's a hard one, right?
*  That's a hard one. And I've discovered that if you just look at these two subsets,
*  you can train things on a single GPU in 10 minutes. And the results you get are directly
*  transferable to ImageNet nearly all the time. And so now I'm starting to see some researchers
*  start to use these much smaller datasets.
*  I so deeply love the way you think because I think you might've written a blog post saying
*  that sort of going to these big datasets is encouraging people to not think creatively.
*  Absolutely.
*  So you're too... It sort of constrains you to train on large resources. And because you have
*  these resources, you think more research will be better. And then you start... So somehow you kill
*  the creativity.
*  Yeah. And even worse than that, Lex, I keep hearing from people who say,
*  I decided not to get into deep learning because I don't believe it's accessible to people outside
*  of Google to do useful work. So like I see a lot of people make an explicit decision to
*  not learn this incredibly valuable tool because they've drunk the Google Call Aid,
*  which is that only Google's big enough and smart enough to do it. And I just find that
*  so disappointing and it's so wrong.
*  And I think all the major breakthroughs in AI in the next 20 years will be doable on a single GPU.
*  Like I would say, my sense is all the big sort of...
*  Well, let's put it this way. None of the big breakthroughs of the last 20 years have required
*  multiple GPUs. So like batch norm, value, dropout,
*  To demonstrate that there's something to them.
*  every one of them, none of them has required multiple GPUs.
*  GANs, the original GANs didn't require multiple GPUs.
*  Well, and we've actually recently shown that you don't even need GANs. So we've developed
*  GAN level outcomes without needing GANs. And we can now do it with, again, by using transfer
*  learning. We can do it in a couple of hours on a single GPU.
*  Just using a generator model, like without the adversarial part?
*  Yeah. So we've found loss functions that work super well without the adversarial part.
*  And then one of our students, a guy called Jason Antich, has created a system called De-Altify,
*  which uses this technique to colorize old black and white movies. You can do it on a single GPU,
*  colorize a whole movie in a couple of hours. And one of the things that Jason and I did together
*  was we figured out how to add a little bit of GAN at the very end, which it turns out for
*  colorization makes it just a bit brighter and nicer. And then Jason did masses of experiments
*  to figure out exactly how much to do, but it's still all done on his home machine on a single GPU
*  in his lounge room. And if you think about colorizing Hollywood movies, that sounds like
*  something a huge studio would have to do, but he has the world's best results on this.
*  There's this problem of microphones. We're just talking to microphones now.
*  Yeah. It's such a pain in the ass to have these microphones to get good quality audio.
*  And I tried to see if it's possible to plop down a bunch of cheap sensors and reconstruct higher
*  quality audio from multiple sources. Because right now I haven't seen work from, okay,
*  we can say even expensive mics, automatically combining audio from multiple sources to improve
*  the combined audio. People haven't done that and that feels like a learning problem.
*  Hopefully somebody can- Well, I mean, it's eminently doable
*  and it should have been done by now. I felt the same way about computational photography
*  four years ago. Why are we investing in big lenses when three cheap lenses plus actually a little bit
*  of intentional movement, so like take a few frames, gives you enough information to get
*  excellent sub-pixel resolution, which particularly with deep learning,
*  you would know exactly what you meant to be looking at. We can totally do the same thing
*  with audio. I think it's a madness that hasn't been done yet. Is there been progress on photography?
*  Yeah. Photography is basically standard now. So the Google Pixel Nightlight, I don't know if
*  you've ever tried it, but it's astonishing. You take a picture in almost pitch black and you get
*  back a very high quality image and it's not because of the lens. Same stuff with adding
*  the bokeh to the background blurring. It's done computationally.
*  Just the pixel here. Yeah. Basically, everybody now is
*  doing most of the fanciest stuff on their phones with computational photography and also increasingly
*  people are putting more than one lens on the back of the camera. So the same will happen for audio,
*  for sure. And there's applications in the audio side. If you look at an Alexa type device,
*  most people I've seen, especially I worked at Google before, when you look at noise background
*  removal, you don't think of multiple sources of audio. You don't play with that as much as I
*  would hope people would. But I mean, you can still do it even with one. Again, not much work's been
*  done in this area. So we're actually going to be releasing an audio library soon, which hopefully
*  will encourage development of this because it's so underused. The basic approach we used for our
*  super resolution in which Jason uses for De-oldify of generating high quality images,
*  the exact same approach would work for audio. Not one's done it yet, but it would be a couple
*  of months work. Okay. Also learning rate in terms of Dawn bench. There's some magic on learning rate
*  that you played around with. It's interesting. Yeah. So this is all work that came from a guy
*  called Leslie Smith. Leslie's a researcher who like us cares a lot about just the practicalities of
*  training neural networks quickly and accurately, which you would think is what everybody should
*  care about, but almost nobody does. And he discovered something very interesting, which
*  he calls super convergence, which is there are certain networks that with certain settings of
*  high parameters could suddenly be trained 10 times faster by using a 10 times higher learning
*  rate. Now no one published that paper because it's not an area of kind of active research in
*  the academic world. No academics recognize this is important. And also deep learning in academia is
*  not considered a experimental science. So unlike in physics where you could say like,
*  I just saw a subatomic particle do something which the theory doesn't explain. You could publish that
*  without an explanation. And then the next 60 years, people can try to work out how to explain it.
*  We don't allow this in the deep learning world. So it's literally impossible for Leslie to publish
*  a paper that says, I've just seen something amazing happen. This thing trained 10 times faster than it
*  should have. I don't know why. And so the reviewers were like, well, you can't publish that
*  because you don't know why. So anyway, that's important to pause on because there's so many
*  discoveries that would need to start like that. Every other scientific field I know of works
*  that way. I don't know why ours is uniquely disinterested in publishing unexplained experimental
*  results, but there it is. So it wasn't published. Having said that, I read a lot more
*  unpublished papers than published papers because that's where you find the interesting insights.
*  So I absolutely read this paper. And I was just like, this is astonishingly mind-blowing and weird
*  and awesome. And why isn't everybody only talking about this? Because if you can train these things
*  10 times faster, they also generalize better because you're doing less epochs, which means
*  you look at the data less, you get better accuracy. So I've been kind of studying that ever since.
*  And eventually Leslie kind of figured out a lot of how to get this done. And we added minor tweaks.
*  And a big part of the trick is starting at a very low learning rate, very gradually increasing it.
*  So as you're training your model, you would take very small steps at the start,
*  and you gradually make them bigger and bigger until eventually you're taking much bigger steps
*  than anybody thought was possible. There's a few other little tricks to make it work, but
*  if it basically we can reliably get super convergence. And so for the Dawnbench thing,
*  we were using just much higher learning rates than people expected to work.
*  LW What do you think the future of, I mean, it makes so much sense for that to be a critical
*  hyperparameter learning rate that you vary. What do you think the future of learning rate magic
*  looks like?
*  DR Well, there's been a lot of great work in the last 12 months in this area. And people are
*  increasingly realizing that optimize, like we just have no idea really how optimizers work.
*  And the combination of weight decay, which is how we regularise optimizers and the learning rate,
*  and then other things like the epsilon we use in the atom optimizer, they all work together
*  in weird ways. And different parts of the model. This is another thing we've done a lot of work on
*  is research into how different parts of the model should be trained at different rates in different
*  ways. So we do something we call discriminative learning rates, which is really important,
*  particularly for transfer learning. So really, I think in the last 12 months, a lot of people
*  have realised that all this stuff is important. There's been a lot of great work coming out.
*  And we're starting to see algorithms appear, which have very, very few dials, if any, that you have
*  to touch. So like that, I think what's going to happen is the idea of a learning rate will,
*  it almost already has disappeared in the latest research. And instead, it's just like, you know,
*  we know enough about how to interpret the gradients and the change of gradients we see to know how to
*  set every parameter. So you see the future of deep learning, where really, where's the input of a
*  human expert needed? Well, hopefully the input of the human expert will be almost entirely unneeded
*  from the deep learning point of view. So again, like Google's approach to this is to try and use
*  thousands of times more compute to run lots and lots of models at the same time and hope that one
*  of them is good. Auto-ML kind of stuff, which I think is insane. When you better understand the
*  mechanics of how models learn, you don't have to try a thousand different models to find which one
*  happens to work the best. You can just jump straight to the best one, which means that it's
*  more accessible in terms of compute, cheaper, and also with less hyperparameters to set, it means
*  you don't need deep learning experts to train your deep learning model for you, which means that domain
*  experts can do more of the work, which means that now you can focus the human time on the kind of
*  interpretation, data gathering, identifying model errors and stuff like that. Yeah, the data side.
*  How often do you work with data these days in terms of the cleaning, looking at it? Like Darwin
*  looked at different species while traveling about, do you look at data? Have you in your roots in
*  Kaggle? Always, yeah. Look at data. Yeah, I mean, it's a key part of our course. It's like before we
*  train a model in the course, we see how to look at the data. And then after the first thing we do
*  after we train our first model, which we fine tune an ImageNet model for five minutes. And then the
*  thing we immediately do after that is we learn how to analyze the results of the model by looking
*  at examples of misclassified images and looking at a classification matrix and then doing like
*  research on Google to learn about the kinds of things that it's misclassifying.
*  So to me, one of the really cool things about machine learning models in general is that when
*  you interpret them, they tell you about things like what are the most important features,
*  which groups you're misclassifying, and they help you become a domain expert more quickly
*  because you can focus your time on the bits that the model is telling you is important. So it lets
*  you deal with things like data leakage. For example, if it says, oh, the main feature I'm looking at is
*  customer ID. And you're like, oh, customer ID should be predictive. And then you can talk to the
*  people that manage customer IDs and they'll tell you like, oh, yes, as soon as a customer's
*  application is accepted, we add a one on the end of their customer ID or something.
*  So yeah, looking at data, particularly from the lens of which parts of the data the model says is
*  important is super important. Yeah. And using the model to almost debug the data to learn more about
*  the data. Exactly. What are the different cloud options for training your networks? Last question
*  related to Dawnbench. Well, it's part of a lot of the work you do, but from a perspective of
*  performance, I think you've written this in a blog post. There's AWS, there's TPU from Google.
*  What's your sense? What the future holds? What would you recommend now in terms of training?
*  So from a hardware point of view, Google's TPUs and the best Nvidia GPUs are similar. I mean,
*  maybe the TPUs are like 30% faster, but they're also much harder to program.
*  There isn't a clear leader in terms of hardware right now, although much more importantly,
*  the GPU, Nvidia's GPUs are much more programmable. They've got much more written for all them. So
*  like that's the clear leader for me and where I would spend my time as a researcher and practitioner.
*  But then in terms of the platform, I mean, we're super lucky now with stuff like Google,
*  GCP, Google Cloud, and AWS that you can access a GPU pretty quickly and easily.
*  But I mean, for AWS, it's still too hard. Like you have to
*  find an AMI and get the instance running and then install the software you want and blah, blah, blah.
*  GCP is currently the best way to get started on a full server environment because they have a
*  fantastic fast AI in PyTorch ready to go instance, which has all the courses pre-installed. It has
*  Jupyter Notebook pre-running. Jupyter Notebook is this wonderful interactive computing system, which
*  everybody basically should be using for any kind of data-driven research. But then even better than
*  that, there are platforms like Salamander, which we own, and Paperspace, where literally you click
*  a single button and it pops up a Jupyter Notebook straight away without any kind of
*  installation or anything, and all the course notebooks are all pre-installed.
*  So like for me, this is one of the things we spent a lot of time kind of curating and working on,
*  because when we first started our courses, the biggest problem was people dropped out of lesson
*  one because they couldn't get an AWS instance running. So things are so much better now.
*  And like we actually have, if you go to course.fast.ai, the first thing it says is,
*  here's how to get started with your GPU. And it's like, you just click on the link and you click
*  start and you're going. You will go GCP. I have to confess I've never used the Google GCP. Yeah,
*  GCP gives you $300 of compute for free, which is really nice. But as I say, Salamander and
*  Paperspace are even easier still. Okay. So from the perspective of deep learning frameworks,
*  you work with Fast.ai, if you go to this framework, and PyTorch and TensorFlow. What are
*  the strengths of each platform in your perspective? So in terms of what we've done our research on and
*  taught in our course, we started with Theano and Keras, and then we switched to TensorFlow and
*  Keras. And then we switched to PyTorch and then we switched to PyTorch and Fast.ai. And that
*  reflects a growth and development of the ecosystem of deep learning libraries. Theano and TensorFlow
*  were great, but were much harder to teach and to do research and development on because they define
*  what's called a computational graph upfront, a static graph, where you basically have to say,
*  here are all the things that I'm going to eventually do in my model. And then later on,
*  you say, okay, do those things with this data. And you can't debug them, you can't do them step
*  by step, you can't program them interactively in a Jupyter Notebook and so forth. PyTorch was not
*  the first, but PyTorch was certainly the strongest entrant to come along and say, let's not do it
*  that way, let's just use normal Python. And everything you know about in Python is just
*  going to work and we'll figure out how to make that run on the GPU as and when necessary.
*  That turned out to be a huge leap in terms of what we could do with our research and what we
*  could do with our teaching. Because it wasn't limiting.
*  Yeah, I mean, it was critical for us for something like DawnBench to be able to rapidly try
*  things. It's just so much harder to be a researcher and practitioner when you have to do everything
*  upfront and you can't inspect it. Problem with PyTorch is it's not at all accessible to newcomers
*  because you have to write your own training loop and manage the gradients and all this stuff.
*  And it's also not great for researchers because you're spending your time dealing with all this
*  boilerplate and overhead rather than thinking about your algorithm. So we ended up writing this
*  very multi-layered API that at the top level, you can train a state of the art neural network
*  in three lines of code. And which kind of talks to an API, which talks to an API, which talks to an
*  API, which you can dive into at any level and get progressively closer to the machine kind of levels
*  of control. And this is the FastAI library. That's been critical for us and for our students
*  and for lots of people that have won big learning competitions with it and written academic papers
*  with it. It's made a big difference. We're still limited though by Python. And particularly this
*  problem with things like recurrent neural nets, say where you just can't change things unless you
*  accept it going so slowly that it's impractical. So in the latest incarnation of the course and
*  with some of the research we're now starting to do, we're starting to do some stuff in Swift.
*  I think we're three years away from that being super practical, but I'm in no hurry. I'm very
*  happy to invest the time to get there. But with that, we actually already have a nascent version
*  of the FastAI library for vision running on Swift and TensorFlow. Because Python for TensorFlow
*  is not going to cut it. It's just a disaster. What they did was they tried to replicate
*  the bits that people were saying they like about PyTorch, this kind of interactive computation,
*  but they didn't actually change their foundational runtime components. So they kind of added this
*  syntax sugar they call TF. Which makes it look a lot like PyTorch, but it's 10 times slower than
*  PyTorch to actually do a step. So because they didn't invest the time in retooling the foundations
*  because their code base is so horribly complex. Yeah, I think it's probably very difficult to do
*  that kind of rejoin. Yeah. Well, particularly the way TensorFlow was written, it was written by a lot
*  of people very quickly in a very disorganized way. So when you actually look in the code,
*  as I do often, I'm always just like, oh God, what were they thinking? It's pretty awful.
*  So I'm really extremely negative about the potential future for Python.
*  Python for TensorFlow.
*  But Swift for TensorFlow can be a different beast altogether. It can basically be a layer on top of
*  MLIR that takes advantage of all the great compiler stuff that Swift builds on with LLVM
*  and yeah, I think it will be absolutely fantastic.
*  Well, you're inspiring me to try. Evan truly felt the pain of TensorFlow 2.0 Python. It's fine by me.
*  Yeah, it does the job if you're using like predefined things that somebody's already written.
*  But if you actually compare, like I've had to do, because I've been having to do a lot of stuff
*  with TensorFlow recently, you actually compare like, okay, I want to write something from scratch.
*  And you're like, I just keep finding it's like, oh, it's running 10 times slower than
*  PyTorch.
*  So is the biggest cost, let's throw running time out the window. How long it takes you to program.
*  That's not too different now. Thanks to TensorFlow eager, that's not too different.
*  But because so many things take so long to run, you wouldn't run it at 10 times slower.
*  Like you just go like, oh, this is taking too long. And also there's a lot of things which are
*  just less programmable, like tf.data, which is the way data processing works in TensorFlow is just
*  this big mess. It's incredibly inefficient. And they kind of had to write it that way because of
*  the TPU problems I described earlier. So I just feel like they've got this huge technical debt,
*  which they're not going to solve without starting from scratch.
*  So here's an interesting question then. If there's a new student starting today,
*  what would you recommend they use?
*  Well, I mean, we obviously recommend fast AI and PyTorch because we teach new students.
*  And that's what we teach with. So we would very strongly recommend that because
*  it will let you get on top of the concepts much more quickly. So then you'll become an
*  actual and you'll also learn the actual state of the art techniques, you know, so you actually get
*  world-class results. Honestly, it doesn't much matter what library you learn because
*  switching from the chain to MX net to TensorFlow to PyTorch is going to be a couple of days work
*  as long as you understand the foundations well. But you think will Swift creep in there
*  as a thing that people start using? Not for a few years, particularly because like
*  Swift has no data science community, libraries, schooling. And the Swift community has
*  a total lack of appreciation and understanding of numeric computing. So like they keep on making
*  stupid decisions, you know, for years, they've just done dumb things around performance and
*  prioritization. That's clearly changing now because the developer of Swift, Chris Latner,
*  is working at Google on Swift for TensorFlow. So like that's a priority. It'll be interesting
*  to see what happens with Apple because like Apple hasn't shown any sign of caring about numeric
*  programming in Swift. So hopefully they'll get off their ass and start appreciating this
*  because currently all of their low-level libraries are not written in Swift. They're not particularly
*  Swifty at all. Stuff like CoreML, they're really pretty rubbish. So yeah, so there's a long way to
*  go. But at least one nice thing is that Swift for TensorFlow can actually directly use Python code
*  and Python libraries in a literally the entire lesson one notebook of fast AI runs in Swift
*  right now in Python mode. So that's a nice intermediate thing. How long does it take
*  if you look at the two fast AI courses, how long does it take to get from 0.0 to completing both
*  courses? It varies a lot. Somewhere between two months and two years generally.
*  So for two months, how many hours a day? So like somebody who is a very competent coder
*  can do 70 hours per course and- 70, 70, that's it? Okay.
*  Yeah. But a lot of people I know take a year off to study fast AI full time and say at the end of
*  the year, they feel pretty competent because generally there's a lot of other things you do.
*  Like they'll generally they'll be entering Kaggle competitions. They might be reading
*  Ian Goodfellow's book. They might, you know, they'll be doing a bunch of stuff.
*  And often, you know, particularly if they are a domain expert, their coding skills might be
*  a little on the pedestrian side. So part of it's just like doing a lot more writing.
*  What do you find is the bottleneck for people usually except getting started and setting stuff
*  up? I would say coding. Yeah, I would say the best, the people who are strong coders pick it up the
*  best. Although another bottleneck is people who have a lot of experience of classic statistics
*  can really struggle because the intuition is so the opposite of what they're used to. They're
*  very used to like trying to reduce the number of parameters in their model and
*  and looking at individual coefficients and stuff like that. So I find people who have a lot of
*  coding background and know nothing about statistics are generally going to be the best off.
*  So you taught several courses on deep learning and as Feynman says, the best way to understand
*  something is to teach it. What have you learned about deep learning from teaching it?
*  A lot. It's a key reason for me to teach the courses. I mean, obviously it's going to be
*  necessary to achieve our goal of getting domain experts to be familiar with deep learning, but
*  it was also necessary for me to achieve my goal of being really familiar with deep learning.
*  I mean, to see so many domain experts from so many different backgrounds, it's definitely,
*  I wouldn't say taught me, but convinced me something that I like to believe was true,
*  which was anyone can do it. So there's a lot of kind of snobbishness out there about
*  only certain people can learn to code. Only certain people are going to be smart enough to like do AI.
*  That's definitely bullshit. I've seen so many people from so many different backgrounds get
*  state-of-the-art results in their domain areas now. It's definitely taught me that the key
*  differentiator between people that succeed and people that fail is tenacity. That seems to be
*  basically the only thing that matters. A lot of people give up, but if the ones who don't give up,
*  pretty much everybody succeeds. Even if at first I'm just kind of like thinking like,
*  wow, they really aren't quite getting it yet, are they? But eventually people get it and
*  they succeed. So I think that's been, I think they're both things I've liked to believe was
*  true, but I don't feel like I really had strong evidence for them to be true, but now I can say
*  I've seen it again and again. So what advice do you have for someone who wants to get started in
*  deep learning? Train lots of models. That's how you learn it. So I think, it's not just me,
*  I think our course is very good, but also lots of people independently have said it's very good.
*  It recently won the COGX award for AI courses as being the best in the world. So I'd say come to
*  our course, course.fast.ai. And the thing I keep on harping on in my lessons is train models,
*  print out the inputs to the models, print out to the outputs to the models,
*  like study, change the inputs a bit, look at how the outputs vary, just run lots of experiments to
*  get an intuitive understanding of what's going on. To get hooked, do you think,
*  you mentioned training, do you think just running the models in France? Like if we talk about
*  getting started. No, you've got to fine tune the models. So that's the critical thing,
*  because at that point you now have a model that's in your domain area. So there's no point
*  running somebody else's model because it's not your model. So it only takes five minutes to
*  fine tune a model for the data you care about. And in lesson two of the course, we teach you
*  how to create your own data set from scratch by scripting Google image search. And we show you
*  how to actually create a web application running online. So I create one in the course that
*  differentiates between a teddy bear, a grizzly bear, and a brown bear. And it does it with
*  basically 100% accuracy. It took me about four minutes to scrape the images from Google search
*  from the script. There's a little graphical widgets we have in the notebook that help you
*  clean up the data set. There's other widgets that help you study the results to see where the errors
*  are happening. And so now we've got over a thousand replies in our share your work here thread of
*  students saying, here's the thing I built. And so there's people who like, and a lot of them
*  as state of the art, like somebody said, Oh, I tried looking at Devangari characters and I couldn't
*  believe it. The thing that came out was more accurate than the best academic paper after
*  lesson one. And then there's others which are just more kind of fun. Like somebody who's doing
*  Trinidad and Tobago hummingbirds. She said that's kind of their national bird. And she's got
*  something that can now classify Trinidad and Tobago hummingbirds. So yeah, train models,
*  fine tune models with your data set, and then study their inputs and outputs.
*  How much is Fast AI courses?
*  Free. Everything we do is free. We have no revenue sources of any kind. It's just a service to the
*  community. You're a saint. Okay. Once a person understands the basics, trains a bunch of models.
*  If we look at the scale of years, what advice do you have for someone wanting to eventually
*  become an expert? Train lots of models. Specifically train lots of models in your domain area. So an
*  expert what? We don't need more expert like create slightly evolutionary research in areas
*  that everybody's studying. We need experts at using deep learning to diagnose malaria.
*  Or we need experts at using deep learning to analyze language to study media bias. So we need
*  experts in analyzing fisheries to identify problem areas in the ocean. That's what we need. So
*  become the expert in your passion area. And this is a tool which you can use for just about anything,
*  and you'll be able to do that thing better than other people, particularly by combining it with
*  your passion and domain expertise. So that's really interesting. Even if you do want to
*  innovate on transfer learning or active learning, your thought is, I mean, it's one I certainly share,
*  is you also need to find a domain or data set that you actually really care for.
*  Right. If you're not working on a real problem that you understand,
*  how do you know if you're doing it any good? How do you know if your results are good? How do you
*  know if you're getting bad results? Why are you getting bad results? Is it a problem with the data?
*  Is it like, how do you know you're doing anything useful?
*  Yeah, the only, to me, the only really interesting research is not the only, but the vast majority of
*  interesting research is like, try and solve an actual problem and solve it really well.
*  So both understanding sufficient tools on the deep learning side and becoming a domain expert
*  in a particular domain are really things within reach for anybody.
*  Yeah, I mean, to me, I would compare it to like studying self-driving cars, having never
*  looked at a car or been in a car or turned a car on, you know, which is like the way it is
*  for a lot of people, they'll study some academic data set where they literally have no idea about
*  that. By the way, I'm not sure how familiar you are with autonomous vehicles, but that is literally,
*  you describe a large percentage of robotics folks working in self-driving cars, is they actually
*  haven't considered driving. They haven't actually looked at what driving looks like.
*  They haven't driven.
*  It's a problem because you know, when you've actually driven, you know, like these are the
*  things that happened to me when I was driving. There's nothing that beats the real world examples
*  of just experiencing them. You've created many successful startups. What does it take to create
*  a successful startup? Same thing as becoming a successful deep learning practitioner, which is
*  not giving up. So you can run out of money or run out of time or run out of something, you know,
*  but if you keep costs super low and try and save up some money beforehand, so
*  you can afford to have some time, then just sticking with it is one important thing.
*  Doing something you understand and care about is important. By something, I don't mean,
*  the biggest problem I see with deep learning people is they do a PhD in deep learning and
*  then they try and commercialize their PhD. It is a waste of time because that doesn't solve an actual
*  problem. You picked your PhD topic because it was an interesting kind of engineering or math or
*  research exercise. But yeah, if you've actually spent time as a recruiter and you know that most
*  of your time was spent sifting through resumes and you know that most of the time you're just
*  looking for certain kinds of things and you can try doing that with a model for a few minutes and
*  see whether that's something which the model seems to be able to do as well as you could,
*  then you're on the right track to creating a startup. And then I think just, yeah, being
*  just be pragmatic and
*  try and stay away from venture capital money as long as possible, preferably forever.
*  So yeah, on that point, do you venture capital? Were you able to successfully run startups
*  with self-funded? Yeah, so my first two were self-funded and that was the right way to do it.
*  That's scary. No, VCs startups are much more scary because you have these
*  people on your back who do this all the time and who have done it for years telling you
*  grow, grow, grow, grow. They don't care if you fail. They only care if you don't grow fast enough.
*  So that's scary. Whereas doing the ones myself, well, with partners who were friends,
*  it's nice because we just went along at a pace that made sense and we were able to build it
*  to something which was big enough that we never had to work again, but was not big enough that
*  any VC would think it was impressive. And that was enough for us to be excited. So I thought that's
*  a much better way to do things for most people. Generally speaking, not for yourself, but how
*  do you make money during that process? Do you cut into savings? So yeah, so I started Fast Mail and
*  Optimal Decisions at the same time in 1999 with two different friends. And for Fast Mail,
*  I guess I spent $70 a month on the server. And when the server ran out of space, I put a payments
*  button on the front page and said, if you want more than 10 megabytes of space, you have to pay
*  $10 a year. So run low, like keep your costs down. Yeah. So I kept my costs down. And once I needed
*  to spend more money, I asked people to spend the money for me. And that was that basically. From
*  then on, we were making money and I was profitable from then. For Optimal Decisions, it was a bit
*  harder because we were trying to sell something that was more like a $1 million sale. But what we
*  did was we would sell scoping projects. So kind of like prototypey projects, but rather than doing
*  it for free, we would sell them $50,000 to $100,000. So again, we were covering our costs and also
*  making the client feel like we were doing something valuable. So in both cases, we were profitable from
*  six months in. Oh, nevertheless, it's scary. I mean, yeah, sure. I mean, it's scary before you
*  jump in. And I guess I was comparing it to the scarediness of VC. I felt like with VC stuff,
*  it was more scary, kind of much more in somebody else's hands. Will they fund you or not? And what
*  do they think of what you're doing? I also found it very difficult with VC's back startups to
*  actually do the thing which I thought was important for the company rather than doing the thing which
*  I thought would make the VC happy. Now, VCs always tell you not to do the thing that makes them happy.
*  But then if you don't do the thing that makes them happy, they get sad. And do you think optimizing
*  for the whatever they call it, the exit is a good thing to optimize for? I mean, it can be, but not
*  at the VC level because the VC exit needs to be, you know, a thousand X. So where else the
*  lifestyle exit, if you can sell something for $10 million, then you've made it. Right. So
*  it depends. If you want to build something that's going to be kind of happy to do forever,
*  then fine. If you want to build something you want to sell in three years time, that's fine too. I
*  mean, they're both perfectly good outcomes. So you're learning Swift now in a way. I mean,
*  you already, and I read that you use at least in some cases, space repetition as a mechanism for
*  learning new things. I use Enki quite a lot myself. I actually don't never talk to anybody about it.
*  Don't know how many people do it, but it works incredibly well for me. Can you talk to your
*  experience? Like how did you, what do you, first of all, okay, let's back it up. What is space
*  repetition? So space repetition is an idea created by a psychologist named Ebbinghaus.
*  I don't know, must be a couple of hundred years ago or something, 150 years ago. He did something
*  which sounds pretty damn tedious. He wrote down random sequences of letters on cards and tested
*  how well he would remember those random sequences a day later, a week later, whatever.
*  He discovered that there was this kind of curve where his probability of remembering one of them
*  would be dramatically smaller the next day and then a little bit smaller the next day,
*  a little bit smaller the next day. What he discovered is that if he revised those cards
*  after a day, the probabilities would decrease at a smaller rate. And then if you revise them again
*  a week later, they would decrease at a smaller rate again. And so he basically figured out a
*  roughly optimal equation for when you should revise something you want to remember.
*  So space repetition learning is using this simple algorithm, just something like revise something
*  after a day and then three days and then a week and then three weeks and so forth. And so if you
*  use a program like Anki, as you know, it will just do that for you. And if you, and it will say,
*  did you remember this? And if you say no, it will reschedule it back to be up here again,
*  like 10 times faster than it otherwise would have. It's a kind of a way of being guaranteed
*  to learn something because by definition, if you're not learning it, it will be rescheduled to be
*  revised more quickly. Unfortunately, though, it's also like, it doesn't let you fool yourself. If
*  you're not learning something, you know, like your revisions will just get more and more. So
*  you have to find ways to learn things productively and effectively, like treat your brain well. So
*  using like mnemonics and stories and context and stuff like that. So yeah, it's a super great
*  technique. It's like learning how to learn is something which everybody should learn before
*  they actually learn anything. But almost nobody does. So what have you, so it certainly works
*  well for learning new languages for, I mean, for learning like small projects almost. But do you,
*  you know, I started using it for, I forget who wrote a blog post about this inspired me.
*  It might have been you, I'm not sure. I started when I read papers, concepts and ideas, I'll put
*  them. Was it Michael Nielsen? Yeah, it was Michael Nielsen. So Michael started doing this recently
*  and has been writing about it. So the kind of today's Ebbinghaus is a guy called Pieter Wozniak,
*  who developed a system called SuperMemo. And he's been basically trying to become like
*  the world's greatest Renaissance man over the last few decades. He's basically lived his life with
*  space repetition learning for everything. I, and so like, Michael's only very recently got into this,
*  but he started really getting excited about doing it for a lot of different things.
*  For me personally, I actually don't use it for anything except Chinese. And the reason for that
*  is that Chinese is specifically a thing I made a conscious decision that I want to continue to
*  remember. Even if I don't get much of a chance to exercise it, because I'm not often in China,
*  so I don't. Or else something like programming languages or papers, I have a very different
*  approach, which is I try not to learn anything from them, but instead I try to identify the
*  important concepts and actually ingest them. So really understand that concept deeply and study
*  it carefully, and we'll decide if it really is important, if it is like incorporated into
*  our library, you know, incorporated into how I do things, or decide it's not worth it. So I find,
*  I find I then remember the things that I care about because I'm using it all the time. So I've,
*  for the last 25 years, I've committed to spending at least half of every day
*  learning or practicing something new, which is all my colleagues have always hated because it
*  always looks like I'm not working on what I'm meant to be working on, but it always means I do
*  everything faster because I've been practicing a lot of stuff. So I kind of give myself a lot
*  of opportunity to practice new things. And so I find now I don't,
*  yeah, I don't often kind of find myself wishing I could remember
*  something because if it's something that's useful, then I've been using it a lot.
*  It's easy enough to look it up on Google, but speaking Chinese, you can't look it up on Google.
*  So do you have advice for people learning new things? So if you, what have you learned as a
*  process as a, I mean, it all starts with just making the hours in the day available.
*  Yeah, you've got to stick with it, which is again, the number one thing that 99% of people don't do.
*  So the people I started learning Chinese with, none of them were still doing it 12 months later.
*  I'm still doing it 10 years later. I tried to stay in touch with them, but they just, no one did it.
*  For something like Chinese, like study how human learning works. So my, every one of my Chinese
*  flashcards is associated with a story and that story is specifically designed to be memorable.
*  We find things memorable, which are like funny or disgusting or sexy or related to people that we
*  know or care about. So I try to make sure all the stories that are in my head have those characteristics.
*  Yeah. So you have to, you know, you won't remember things well if they don't have some context
*  and yeah, you won't remember them well if you don't regularly practice them, whether it be
*  just part of your day-to-day life or for Chinese for me flashcards. I mean, the other thing is
*  let yourself fail sometimes. So like I've had various medical problems over the last few years
*  and basically my flashcards just stopped for about three years and there've been other times I've
*  stopped for a few months and it's so hard because you get back to it and it's like,
*  you have 18,000 cards due. It's like, and so you just have to go, all right, well, I can either
*  stop and give up everything or just decide to do this every day for the next two years until I get
*  back to it. The amazing thing has been that even after three years, I, you know, the Chinese was
*  still in there. Like it was so much faster to relearn than it was to learn the first time.
*  Yeah, absolutely. It's in there. I have the same with guitar, with music and so on. It's sad
*  because the work sometimes takes away and then you won't play for a year. But really, if you then
*  just get back to it every day, you're right there again. What do you think is the next big breakthrough
*  in artificial intelligence? What are your hopes in deep learning or beyond that people should be
*  working on or you hope there'll be breakthroughs? I don't think it's possible to predict. I think
*  I think what we already have is an incredibly powerful platform to solve lots of
*  societally important problems that are currently unsolved. So I just hope that people will,
*  lots of people will learn this toolkit and try to use it. I don't think we need a lot of
*  new technological breakthroughs to do a lot of great work right now.
*  And when do you think we're going to create a human level intelligence system? Do you think?
*  How hard is it? How far away are we? I don't know. I have no way to know. I don't know.
*  I don't know why people make predictions about this because there's no data and nothing to go on.
*  It's just like, there's so many societally important problems to solve right now. I just
*  don't find it a really interesting question to even answer. So in terms of societally important
*  problems, what's the problem that is within reach? Well, I mean, for example, there are problems that
*  AI creates, right? So most specifically, labor force displacement is going to be huge and people
*  keep making this frivolous econometric argument of being like, oh, there's been other things that
*  aren't AI that have come along before and haven't created massive labor force displacement. Therefore,
*  AI won't. So that's a serious concern for you? Andrew Yang is running on it.
*  Yeah, I'm desperately concerned. And you see already that the changing workplace
*  has led to a hollowing out of the middle class. You're seeing that students coming out of school
*  today have a less rosy financial future ahead of them than their parents did, which has never
*  happened in the last few hundred years. We've always had progress before. And you see this
*  turning into anxiety and despair and even violence. So I very much worry about that.
*  You've written quite a bit about ethics too. I do think that every data scientist working with
*  deep learning needs to recognize they have an incredibly high leverage tool that they're using
*  that can influence society in lots of ways. And if they're doing research, that research is going
*  to be used by people doing this kind of work. And they have a responsibility to consider the
*  consequences and to think about things like how will humans be in the loop here? How do we avoid
*  runaway feedback loops? How do we ensure an appeals process for humans that are impacted by
*  my algorithm? How do I ensure that the constraints of my algorithm are adequately explained to the
*  people that end up using them? There's all kinds of human issues, which only data scientists are
*  actually in the right place to educate people about, but data scientists tend to think of themselves as
*  just engineers and that they don't need to be part of that process, which is wrong.
*  Well, you're in a perfect position to educate them better, to read literature,
*  to read history, to learn from history. Well, Jeremy, thank you so much for everything you do
*  for inspiring huge amount of people, getting them into deep learning and having the ripple effects,
*  the flap of a butterfly's wings, that will probably change the world. So thank you very much.
*  Thank you.

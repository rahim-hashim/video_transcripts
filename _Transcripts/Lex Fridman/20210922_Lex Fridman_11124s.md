---
Date Generated: April 12, 2024
Transcription Model: whisper medium 20231117
Length: 11124s
Video Keywords: ['agi', 'ai', 'ai podcast', 'anaconda', 'artificial intelligence', 'artificial intelligence podcast', 'conda', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'mit ai', 'numba', 'numpy', 'openteams', 'pip', 'python', 'pytorch', 'quansight', 'scipy', 'tensorflow', 'travis oliphant']
Video Views: 586058
Video Rating: None
---

# Travis Oliphant: NumPy, SciPy, Anaconda, Python & Scientific Programming | Lex Fridman Podcast #224
**Lex Fridman:** [September 22, 2021](https://www.youtube.com/watch?v=gFEE3w7F0ww)
*  The following is a conversation with Travis Aliphant, one of the most impactful programmers
*  and data scientists ever. He created NumPy, SciPy, and Anaconda. NumPy formed the foundation of
*  tensor-based machine learning in Python, SciPy formed the foundation of scientific programming
*  in Python, and Anaconda, specifically with Conda, made Python more accessible to a much
*  larger audience. Travis's life work across a large number of programming and entrepreneurial
*  efforts has and will continue to have a measurable impact on millions of lives by empowering
*  scientists and engineers in big companies, small companies, and open source communities
*  to take on difficult problems and solve them with the power of programming. Plus, he's a truly kind
*  human being, which is something that when combined with vision and ambition makes for a great leader
*  and a great person to chat with. To support this podcast, please check out our sponsors in the
*  description. This is the Lex Friedman podcast, and here is my conversation with Travis Aliphant.
*  What was the first computer program you've ever written? Do you remember?
*  Whoa, that's a good question. I think it was in fourth grade. Just a simple loop and basic.
*  Basic, yeah, on an Atari 800, Atari 400, I think, or maybe it was an Atari 800. It was a part of a
*  class, and we just were just basic loops to print things out. Did you use go-to statements?
*  Yes, yes, we use go-to statements. I remember in the early days, that's when I first realized
*  there's like principles to programming, when I was told that don't use go-to statements. Those are bad
*  software engineering principles. It goes against what great, beautiful code is. I was like,
*  oh, okay, there's rules to this game. I didn't see that until high school when I took an AP
*  computer science course. I did a lot of other kinds of just programming in TI. Finally, when I took
*  an AP computer science course in Pascal. Wow. Yeah, it was Pascal. That's when I, oh, there are
*  these principles. Not C or C++? No, I didn't take C until the next year in college. I had a course in
*  C, but I haven't done much in Pascal, just that AP computer science course. Now, sorry for the
*  romanticized question, but when did you first fall in love with programming? Oh, man, good question.
*  I think actually when I was 10, my dad got us a Timex Sinclair, and he was excited about the
*  spreadsheet capability, but I made him get the add-ons so we could actually program in basic.
*  And just being able to write instructions and have the computer do something. Then we got a TI-994A
*  when I was about 12. It had sprites and graphics and music you could actually program to do music.
*  That's when I really fell in love with programming. So this is a full, like a real computer with
*  memory and storage, processors, whatnot. Yeah, the Timex Sinclair was one of the very first. It was a
*  cheap, cheap, like I think it was, well, it was still expensive, but it was 2K of memory. We got
*  the 16K add-on pack, but yeah, it had memory and you could program it. You had the, in order to
*  store your programs, you had to attach a tape drive. Remember the sound that would play when you
*  converted the modem, it would convert digital bits to audio files, set on a tape drive.
*  Still remember that sound, but that was the storage. And what was the programming language?
*  It was basic. And then they had a VisiCalc. And so a little bit of spreadsheet programming,
*  VisiCalc, but mostly just some basic. Do you remember what kind of things drew you to programming?
*  Was it working with data? Was it video games? Math. Math. Mathy stuff. Yeah. I've always loved
*  math. And a lot of people think they don't like math because I think when they're exposed to it
*  early, it's about memory. When you're exposed to math early, you have a good short-term memory,
*  making members time tables. And I do have a reasonably, I mean, not perfect, but a reasonably
*  long little short-term memory buffer. And so I did great at times tables. I said, oh, I get to math.
*  But I started to really like math, just the problem solving aspect. And so computing was
*  problem solving applied. And so that's always kind of been the draw, kind of coupled with the
*  mathematics. Did you ever see the computer as like an extension of your mind, like something
*  able to achieve? Not till later. Okay. Yeah. Not then. It's just like a little set of puzzles
*  that you can play with and you can play with math puzzles. And yeah, it was, it was too rudimentary
*  early on. Like it was sort of, yeah, it was too, it was a lot of work to actually take a thought
*  you'd have and actually get it implemented. And that's still work, but it's getting easier. And
*  so, yeah, I would say that's definitely what's attracted me to Python is that that was more
*  real, right? I could think in Python. Speaking of foreign language, I only speak another language
*  fluently besides English, which is Spanish. And I remember the day when I would dream in Spanish
*  and you start to think in that language. And then you actually, I do definitely believe that language
*  limits or expands your thinking. There are some languages that actually lead you to certain
*  thought processes. Yeah. Like, so I speak Russian fluently and that's certainly a language that
*  leads you down certain thoughts. Well, yeah, I mean, there's a, there's a history of the two world
*  wars of the, of millions of people starving to death or near to death throughout his history
*  of suffering, of injustice, like this promise sold to the people and then the carpet or whatever
*  swept from under them. And it's like broken promises and all of that pain and melancholy is
*  in the language, the sad songs, the sad, hopeful songs, the over romanticized, like, I love you,
*  I hate you. The sort of the swings between the, all the various spectrums of emotion. So that's all
*  within the language. The way it's twisted a poach, there's a, there's a, there's a strong culture of
*  rhyming poetry. So like the bards, like the, the sync, there's a musicality to the language too.
*  Did Dostoevsky write in Russian? Yeah. So like Dostoevsky, Tolstoy, all the,
*  all the ones that I know about, which are translated and I'm curious how the translations.
*  So Dostoevsky did not use the musicality of the language too much. So it actually translates
*  pretty well because it's so philosophically dense that the story does a lot of the work,
*  but there's a bunch of things that are untranslatable. Certainly the poetry is
*  not translatable. I actually have a few conversations coming up offline and also
*  in this podcast with people who've translated Dostoevsky. And that's for people who worked,
*  who work in this field, know how difficult that is. Sometimes you can spend,
*  you know, months thinking about a single sentence, right? In, in the context, like,
*  because there's just a magic captured by that sentence. And how do you translate just in the
*  right way? Because those words can be, can be really powerful. There's, there's a famous line,
*  beauty will save the world from Dostoevsky. You know, there's so many ways to translate that.
*  And you're right. The language gives you the tools with which to tell the story,
*  but it also leads your mind down certain trajectories and paths to where over time,
*  as you think in that language, you become a different human being.
*  Yes. Yeah. Yeah. That's a fascinating reality. I think there's, I know people have explored that,
*  but it's just rediscovered. Well, we don't, we live in our own little pockets. Like this is the sad
*  thing is I feel like, unfortunately, given time and given getting older, I'll never know
*  the China, the Chinese world because I don't truly know the language. Same with Japanese.
*  I don't truly know Japanese and Portuguese and Brazil, that whole South American continent, like,
*  yeah, I'll go to Brazil and Argentina, but will I truly understand the people if I don't understand
*  the language? It's sad because I wonder how much, how many geniuses we're missing because
*  so much of the scientific world, so much of the technical world is in English and so much of it
*  might be lost because they're, it's just, we don't have the common language. I completely agree. I'm
*  very much in that vein of there's a lot of genius out there that we miss and it's sort of fortunate
*  when it bubbles up into something that we can understand or process, there's a lot we miss.
*  So that's why I tend to lean towards really loving democratization or things that empower people or,
*  you know, I very resistant to sort of authoritarian structures. Fundamentally for that
*  reason, I think it's, it, well, several reasons, but it just hurts us. We're worse off.
*  So speaking of languages that empower you, so Python was the first language for me that,
*  that I could, I really enjoyed thinking in, as you said. Sounds like you shared my experience too.
*  So when did you first, do you remember when you first kind of connected with Python, maybe even
*  fell in love with Python? It's a good question. It was a process that took about a year. I first
*  encountered Python in 1997. I was a graduate student studying biomedical engineering at the Mayo
*  Clinic and I had previously, I'd been involved in taking information from satellites. I was an
*  electrical engineering student used to taking information and trying to get something out of
*  it, doing some data processing, get information out of it. And I'd done that in MATLAB. I'd done
*  that in Pearl. I'd done that in, you know, scripting on a VMS. There's actually a Vax VMS system and
*  they had their own little scripting tools around Fortran. Done a lot of that. And then as a graduate
*  student, I was looking for something and encounter Python. And because Python had an array, had two
*  things that made me not filter it away. Because I was filtering a bunch of stuff. I looked at
*  Yorick. I looked at a few other languages that are out there at the time in 1997, but it had arrays.
*  There's a library called Numeric that had just been written in 95. Like not very, not too much
*  earlier. By an MIT alum, Jim Huguenin, you know, and I went back and read the mailing list to see
*  the history of how it grew. And there was a very interesting, fascinating to do that actually,
*  to see how this emergent cooperation, unstructured cooperation happens in the open source world
*  that led to a lot of this collective program, which is something maybe we might get into a
*  little later about what that looks like. What gap did Numeric fill? Numeric filled the gap
*  of having an array object. So instead of- There was no array object. There was no array. There was a
*  one dimensional byte concept, but there was no N dimensional, two, three, four dimensional tensor,
*  they call it now. I'm still in the category that a tensor is another thing and it's just an MD array,
*  we should call it, but kind of lost that battle. There's many battles in this world, some which
*  we'll win, some we lose. That's exactly right. So, and, but it was, it had no math to it. So Numeric
*  had math and a basic way to think in arrays. So I was looking for that and it had complex numbers,
*  a lot of programming languages. And you can see it because, you know, if you're just a computer
*  scientist, you think, ah, complex numbers are just two floats. So you can, people can build that on.
*  But in practice, a complex number as a, as one of the significant algebras that helps connect a lot
*  of physical and mathematical ideas, particularly FFT for an electrical engineer. And, and it's a
*  really important concept and not having it means you have to develop it several times. And those
*  times may not share an approach. One of the common things in programming, one of the things programming
*  enables is abstractions. But when you have shared abstractions, it's even better. It sort of gets to
*  the level of language of actually, we all think of this the same way, which is both powerful and
*  dangerous, right? Because powerful in that we now can quickly make bigger and higher level things
*  on top of those abstractions dangerous because it also limits us as to the things we left, maybe left
*  behind in producing an abstraction, which is at the heart of programming today and actually building
*  around the programming world. I think it's a fascinating philosophical topic.
*  Yeah, they will continue for many years, I think, as we build more and more and more abstractions.
*  Yes, I often think about, you know, we have, we have a world that's built on these abstractions
*  that were they the only ones possible? Certainly not, but they led to, you know, it's very hard to
*  do it differently. Like there's an inertia that's very hard to, you know, push out, push away from.
*  There's, that has implications for things like, you know, the Julia language, which you have heard
*  of, I'm sure. And I've met the creators and I like Julia. It's a really cool language, but they've
*  struggled to kind of against the just the tide of like this inertia of people using Python. And,
*  and, you know, there's strategies to approach that, but nonetheless, it's a, it's a phenomena.
*  And sometimes, so I love complex numbers and I love to race. So I looked at Python and then I
*  had the experience, I did some stuff in Python and I was just doing my PhD. So I was out, my focus was
*  on, I was actually doing a combination of MRI and ultrasound and looking at a phenomena called
*  elastography, which is you push waves into the body and observe those waves. Like you can actually
*  measure them and then you do mathematical inversion to see what the elasticity is. And so that's the
*  problem I was solving is how to do that with both ultrasound and MRI. I needed some tool to do that
*  with. So I was starting to use Python in 97. In 98, I went back, looked at what I'd written and realized
*  I could still understand it, which is not the experience I've had when doing Pearl in 95, right?
*  I'd done the same thing. And then I looked back and I forgot what it was even saying. Now, you know,
*  I'm not saying it. So I, that, that may, Hey, this may work. I like this. This is something I can
*  retain without becoming an expert per se. And so that led me to go, I'm going to push more to this.
*  And then that 98 was kind of the, when I started to fall in love with Python, I would say.
*  A few peculiar things about Python. So maybe compared to Pearl compared to some of the other
*  languages. So there's no braces. Yeah. So you space is used indentation, I should say is used as part
*  of our language. Yeah. Right. So did you, I mean, that's quite a leap. Were you comfortable with
*  that leap or were you just very open-minded? Good question. I was open-minded. So I was
*  cognizant of the concern and it definitely has, it has specific challenges, you know, cut and
*  pasting, for example, your cut and pasting code. And if your editors aren't supportive of that,
*  if you're putting into a terminal and particularly in the past when terminals didn't necessarily have
*  the intelligence to manage it now, now, now IPython and Jupyter notebooks handle that just fine. So
*  there's really no problem. But in the past, it creates some challenges, formatting challenges,
*  also mixed tabs and spaces. If you're, if editors weren't, you weren't clear on what was happening,
*  you would have these issues. So there were really concrete reasons about it that I heard and
*  understood. I never really encountered a problem with it personally. Like it was occasional
*  annoyances, but I really liked the fact that it didn't have all this extra characters, right?
*  That these extra characters didn't show up in my visual field when I was just trying to process
*  understanding a snippet of code. Yeah, there's a cleanness to it. But I mean, the idea is supposed
*  to be that Pearl also has a cleanness to it because of the minimalism of like how many
*  characters it takes to express a certain thing. So it's very compact. But what you realize with
*  that compactness comes, there's a culture that prizes compactness. And so the code gets more
*  and more compact and less and less readable to a point where it's like, like to be a good programmer
*  in Pearl, you write code that's basically unreadable. There's a culture. Correct. And
*  you're proud of it. Yeah, you're proud of it. Right. Exactly. And it's like, feels good. And
*  it's really selective. It means you have to be an expert in Pearl to understand it. Whereas Python
*  allowed you not to have to be an expert. You didn't have to take all this brain energy. You
*  could leverage what I say. You could leverage your English language center, which you're using
*  all the time. I've wondered about other languages, particularly non-Latin based languages.
*  Latin based languages with the characters are really similar. I think people have an easier
*  time, but I don't know what it's like to be a Japanese or a Chinese person trying to
*  learn a different syntax. Like what would computer programming look like in that? I haven't looked
*  at that at all, but it certainly doesn't, you know, leveraging your Chinese language center.
*  I'm not sure Python or any programming does that, but that was a big deal. The fact that it was
*  accessible, I could be a scientist. What I really liked is many programming languages really demand
*  a lot of you and you can get a lot, you know, you do a lot if you learn it. But Python enables
*  you to do a lot without demanding a lot of you. There's nuance to that statement, but it certainly
*  was, it's more accessible. So more people could actually, as a scientist, as somebody who, or an
*  engineer who was trying to solve another problem besides programming, I could still use this
*  language and get things done and be happy about it. And I was also comfortable in C at that time.
*  And Matlab you did a little bit of that.
*  And Matlab I did a lot before that, exactly. So I was comfortable in, those three languages were
*  really the tools I used during my studies and schooling. But to your point about language
*  helping you think, one of the big things about Matlab was it was, and APL before it, I don't
*  know if you remember APL. APL is actually the predecessor of array-based programming,
*  which I think is really an underappreciated, if I talk to people who are just steeped in computer
*  programming, computer science, like most of the people that Microsoft has hired in the past,
*  for example, Microsoft as a company generally did not understand array-based programming.
*  Culturally they didn't understand it. So they kept missing the boat, kept missing the understanding
*  of what this was. They've gotten better, but there's still a whole culture of folks that doesn't
*  programming. That's systems programming or web programming or lists and maps. And what about an
*  n-dimensional array? Oh yeah, that's just an implementation detail. Well, you can think that,
*  but then actually if you have that as a construct, you actually think differently. APL was the first
*  language to understand that and it was in the sixties. The challenge of APL is APL had very
*  dense, not only glyphs, like new characters, new glyphs, but they even had a new keyboard because
*  to produce those glyphs, this is back in the early days in computing when the Quarity keyboard maybe
*  wasn't as established. Like, well, we can have a new keyboard, no big deal. But it was a big deal
*  and it didn't catch on. And the language, APL, very much like Perl, is people would pride themselves
*  on how much could they write the game of life in 30 characters of APL. APL has characters that mean
*  summation and they have adverbs. They would have adjectives and these things called adverbs,
*  which are like methods, like reduction, it would be an adverb on an ad operator.
*  Right. So, but using these tools, you could construct and then you start to think at that
*  level. You think in N dimensions, it's something I like to say, and you start to think differently
*  about data at that point. Now you're, it really helps. Yeah. I mean, outside of programming,
*  if you really internalize linear algebra as a course, I mean, it philosophically allows you to
*  think of the world differently. It's almost like liberating. You don't have to think about the
*  individual numbers in the N dimensional array. You could think of it as an object in itself.
*  And all of a sudden this world can open up. You're saying MATLAB and APL were like the early,
*  see, I don't know if many languages got that right ever. No, no, no, they didn't. Even still,
*  I would say, I mean, NumPy is a, as an inheritor of the traditions that I would say APL J was
*  another version that was, what it did is not have the glyphs, just have short characters,
*  but still a Latin keyboard could type them. And then numeric inherited from that in terms of,
*  let's add arrays plus broadcasting plus methods reduction, even some of the language like rank
*  is a concept that's in, that was in Python is still in Python for the number of dimensions.
*  Right. That's, that's different than say the rank of a matrix, which people think of
*  as well. So it's that it came from that tradition, but NumPy is a very pragmatic, practical tool.
*  NumPy inherited from numeric and we can get to where NumPy came from, which is the current array,
*  at least current as of 2015, 2017. Now there's a ton of them over the past two or three years,
*  but we can get into that too. So if we just sort of linger on the early days of
*  what was your favorite feature of Python? Do you remember like what, it's so interesting to linger
*  on like the, what, what really makes you connect with a language? I'm not sure it's
*  obvious to introspect that. No, it isn't. And I've thought about that. It's some length. I'm not,
*  I think definitely the fact that I could read it later, that I could use it productively without
*  becoming an expert and other language I had to put more effort into. Right. That's like an empirical
*  observation. Like you're not analyzing any one aspect of the language. It just seems time after
*  time and you look back, it's somehow readable. It's somehow readable. Then it was sort of,
*  I could take executable English and translate it to Python more easily. Like I didn't have to go,
*  there was no translation layer. As an engineer or as a scientist, I could think about what I
*  wanted to do. And then the syntax wasn't that far behind it. Yeah. Right. Now there are some,
*  there are some warts there still. It wasn't perfect. Like there's some areas where I'm like,
*  it'd be better if this were different or if this were different. Some of those things got out of
*  the language too. I was really grateful for some of the early pioneers in the Python ecosystem back
*  because Python got written in 91 is when the first version came out. But Guido was very open
*  to users. And one of the sets of users were people like Jim Huguenin and David Asher and Paul Dubois
*  and Conrad Hinson. These were people that were on the main list and they were just asking for
*  things like, Hey, we really should have complex numbers in this language. So let's, you know,
*  there's a J, there's a one J, right? And the fact that they went the engineering route of J is
*  interesting. I don't think that's entirely favoring engineers. I think it's because I
*  is so often used as the index of a for loop. I think that's actually why. Probably. Right. I mean,
*  there's a pragmatic aspect. The fact that complex numbers were there. I love that. The fact that I
*  could write ndarray constructs and that reduction was there. Very simple to write summations and,
*  and, and broadcasting was there. I could do addition of whole arrays. So that was cool.
*  Those are some things I loved about it. I don't know what to start talking to you about because
*  you've been, you've created so many incredible projects that basically change the whole
*  landscape of programming. But okay, let's start with, uh, let's go chronologically with sci-pi.
*  You created sci-pi over two decades ago now. Yes. Right. I love to talk about sci-fi. Sci-fi was
*  really my baby. What is it? Uh, what was its goal? What is its goal? How does it work? Yeah,
*  fantastic. So sci-pi was effectively here. I'm using Python to do stuff that I previously
*  used Matlab to use. And I was using numeric, which is an array library that made a lot of it possible.
*  But I, you know, there's things that were missing. Like I didn't have an ordinary differential
*  equation solver. I could just call, right? I didn't have integration. Yeah. I wanted to
*  integrate this function. Okay. Well, I don't have just a function I can call to do that.
*  These are things I remember being critical things that I was missing. Optimization. I just want to
*  pass a function to an optimizer and have it tell me what the optimal value is. Uh, those are things
*  like, well, why don't we just write a library that adds these tools? And I started to post on the
*  mailing list and there previously been, you know, people have discussed, I remember Conrad Henson
*  saying, wouldn't it be great if we had this optimizer library or David Asch would say this
*  stuff. And, and I'm, you know, I'm a ambitious, ambitious is the wrong word and eager and, uh,
*  probably more time than sense. I was, you know, a poor graduate student. Uh, my wife thinks I'm
*  working on my PhD and I am, but part of the PhD that I loved was the fact that it's exploratory.
*  You're not just, you know, taking orders, fulfilling a list of things to do. You're trying to figure out
*  what to do. And so I thought, well, you know, I'm writing tools for my own use in a PhD. So
*  I'll just start this project. And so in 99, 98 was when I first started to write libraries for
*  Python. But when I fell in love with Python 98, I thought, oh, well, there's just a few things
*  missing. Like, oh, I need a reader to read DICOM files. I was in medical imaging and DICOM was a
*  format that I want to be able to load that into Python. Okay. How do I write a reader for that?
*  So I wrote something called, it was an IO package, right? And that was my very first extension module,
*  which is C. So I wrote C code to extend Python so that the positive in Python, I could write
*  things more easily. That, that combination kind of hooked me. It was the idea that I could,
*  here's this powerful tool. I can use the scripting language and the high level language to think
*  about, but that I can extend easily easily in this, in C that easily for me, because I knew enough C
*  and then Guido had written a link. I mean, the only, the hard part of extending Python was something
*  called the way memory management works and you have to do reference counting. And so there's,
*  there's a tracking of reference counting you have to do manually. And if you don't, you have,
*  you have memory leaks. And so that's hard. Plus then C, you know, it's just much more,
*  you have to put more effort into it. It's not just, I have to now think about pointers and
*  have to think about stuff that is different. I have to kind of, you're like putting a new
*  cartridge in your brain. Like you're, okay, I'm thinking about MRI. Now I'm thinking about
*  programming and, and they're distinct modules. You end up having to think about, so it's harder.
*  And when I was just in Python, I could just think about MRI and high level writing. But I could do
*  that and that kind of, I liked it. I found that to be enjoyable and fun. And so I ended up, oh,
*  well, let me just add a bunch of stuff to Python to do integration. Well, and the cool thing is,
*  is that the power of the internet, I just looking around and I found, oh, there's this net live,
*  which has hundreds of four-channel routines that people have written in the sixties and the
*  seventies and the eighties and four-channel 77. Fortunately, it wasn't four-channel 60s.
*  I've been imported to four-channel 77 and four-channel 77 is actually a really great
*  language. Four-channel 90 probably is my favorite four-channel because it's also,
*  it's got complex numbers, got arrays and it's pretty high level. Now the problem with it
*  is you'd never want to write a program in four-channel 90 or four-channel 77,
*  but it's totally fine to write a subroutine in. Right. And so, and then four-channel kind of got
*  a little off course when they tried to compete with C++, but at the time I just want libraries
*  that do something like, oh, here's an order of equation. Here's integration. Here's run,
*  cut it integration already done. I don't have to think about that algorithm and you could,
*  but it's nice to have somebody who's already done one and tested it. And so I sort of started this
*  journey in 98 really, if you look back at the main list, there's sort of this, this productive
*  era of me writing an extension module to connect run, cut integration to Python and making an
*  ordinary additional equation solver. And then releasing that as a package. So we could call ODE
*  pack. I think I called it then quad pack. And then I just made these packages. Eventually that became
*  multi-pack because they're originally modular. You can install them separately, but a massive
*  problem in Python was actually just getting your stuff installed at the time, releasing software
*  for me. Like today it's people think, what does that mean? Well, then it meant some poorly written
*  webpage. I had some bad webpage up and I put a tarball, just a GZip tarball of source code.
*  That was the release. But okay, can we just stand that because
*  that the community aspect of creating the package and sharing that, that's rare. That to have to
*  both have at that time. So like the raw, it was pretty early. Yeah. So, oh, well, not, not rare.
*  Maybe, maybe you can correct me on this, but it seems like in the scientific community, so many
*  people, you were basically solving the problems you needed to solve to process the particular
*  application, the data that you need and to also have the mind that I'm going to make this usable
*  for others. That's, I would say I was inspired. I'd been inspired by Linux, been inspired by
*  you know, Linus, Linus and him making his code available. And I was starting to use Linux at the
*  time. And I went, this is cool. So I'd kind of been previously primed that way. And generally I
*  was, I was into science because I liked the sharing notion. I liked the idea of, Hey, let's,
*  if collectively we build knowledge and share it, we can all be better off. Okay. So you want to
*  energize by that. So it's energized by the already. Yeah. Right. And I can't deny that. I was,
*  I'm sort of a, had this very, I liked that part of science, that part of sharing. And then all of
*  a sudden, oh, wait, here's something. And here's something I could do. And then I slowly over years
*  learned how to share better so that you could actually engage more people faster. One of the
*  key things was actually giving people a binary they could install. Right. So that wasn't just
*  your source code. Good luck. Compile this and then it's compiled, ready to install. You just, you know,
*  so in fact, a lot of the journey from 98, even through 2012, when we started Anaconda was about
*  that. Like it's why, you know, it's really the key as to why a scientist with dreams of doing MRI
*  research ended up starting a software company that installs software. I work with a few folks now
*  that don't program like on the creative side, the video side, the audio side. And because my whole
*  life is running on scripts, I have to try to get them, I'm having all the task of teaching them
*  how to do Python enough to run the scripts. And so I've been actually facing this, whether it's
*  on the condoms, some with the task of how do I minimally explain basically to my mom, how to
*  write a Python script. And it's an interesting challenge. It's a to do item for me to figure out
*  like what is the minimal amount of information I have to teach? What are the tools you use?
*  That one, you enjoy it to your effect of it. They're related. Those are two related questions.
*  And then the debugging, like the iterative process of running the script to figure out what the error
*  is, maybe even for some people to do the fix yourself. So do you compile it? Do you
*  distribute, like how do you distribute that code to them? And it's interesting because I think
*  it's exactly what you're talking about. If you increase the circle of empathy, the circle of
*  people that are able to use your programs, you increase it. It's like effectiveness and it's power.
*  And so you have to think, you know, can I write scripts? Can I write programs that can be used by
*  biomedical engineers, by all kinds of people that don't know programming and actually maybe
*  plant a seed, have them catch the bug of programming so that they start on the journey.
*  That's a huge responsibility. And ultimately it has to do with the Amazon one click buy,
*  like how, how frictionless can you make the early steps?
*  Frictionless is actually really key to go in any community is every, any friction point,
*  you're going to lose some people. Now, sometimes you may want to intentionally do that. If you're
*  early enough on, you need a lot of help. You need people who have the skills. You might actually,
*  it's helpful. You don't necessarily have too many users as opposed to contributors if you're early
*  on. Anyway, there's a sci-fi started in 98, but it really emerged as this collection of modules
*  that I was just putting on the net, people were downloading. And you know, I think I got a hundred
*  users by the end of that year, but there, but the fact that I got a hundred users and more than that
*  people started to email me with fixes. Like, and that was actually intoxicating, right? That was the,
*  that was the, you know, here I'm writing papers and I'm giving conferences and I get people
*  would say, hello, but yeah, good job. But mostly it was, you're reviewed with, it's competitive.
*  You publish a paper and people are like, Oh, it wasn't my paper. You know, I was starting to see
*  that sense of academic life where it was so much, I thought there was a cooperative effort,
*  but it sounds like we're here just to one up each other. And you know, it's not, it's not true across
*  the board, but a lot of that's there. But here in this world, I was getting responses from people
*  all over the world. You know, I remember Piero Peterson in Estonia, right? Was one of the first
*  people. And he sent me back this make file because the first thing it is, yeah, your build thing
*  stinks. And here's a better make file. Now it is a complex make file. I don't think I never
*  understood that make file actually, but it worked and it did a lot more. And so I was like, thanks,
*  this is cool. And that was my first kind of engagement with community development. But you
*  know, the process was he sent me a patch file. I had to upload a new tar ball and I just found,
*  I really love that. And the style back then was here's a mailing list is very, it wasn't as,
*  there's certainly weren't the tools that are available today. It was very early on,
*  but I really started to, that's the whole year. I think I did about seven packages that year,
*  right? And then by the end of the year, I collected them into a thing called multi-pack.
*  So 99, there was this thing called multi-pack and that's when a high school student,
*  no, he was a high school student at the time, a guy named Robert Kern, took that package and made
*  a windows installer, right? And then of course, a massive increase of usage.
*  So by the way, most of this development was under Linux.
*  Yes. Yes, it was on Linux. I was a Linux developer doing it on the Unix box. I mean,
*  at the time I was actually getting into, I had a new hard drive, did some kernel programming to
*  make the hard drive work. I mean, not programming, but modification to the kernel so I could actually
*  get a hard drive working. I love that aspect of it. I was also in, at school, I was building a
*  cluster. I took Mac computers and you put yellow dog Linux on them. At the Mayo Clinic, they were
*  just, they had all these Macs that were older, they were just getting rid of. And so I kind of
*  got permission to go grab them together. I put about 24 of them together in a cluster in a cabinet
*  and put yellow dog Linux on them all. And I wrote a C++ program to do MRI simulation. That was what
*  I was doing at the same time for my day job, so to speak. So I was loving the whole process.
*  And the same time I was, oh, I need a ordinary differential equation. That's why ordinary
*  differential equations were key was because that's the heart of a block equation for simulating MRI
*  is an ODE solver. And so that's, but I actually did that, those happened at the same time. That's
*  why it was kind of what you're working on and what you're interested in, they're coinciding.
*  I was definitely scratching my own itch in terms of building stuff. And which helped in the sense
*  that I was using it for me. So at least I had one user. I had one person who was like, well,
*  no, this is better. I like this interface better. And I had the experience of Matlab to guide some
*  of what those APIs might look like. But you're just doing yourself, you're building all this stuff.
*  But with the Windows installer, it was the first time I realized, oh yeah, the binary installer
*  really helps people. And so that led to spending more time on that side of things. So around 2000,
*  so I graduated my PhD in 2000, end of year, end of 2000. So 99 doing a lot of work there, 98 do a lot
*  of work there, 99 kind of spending more time on my PhD, you know, helping people use the tools,
*  thinking about what do I want to go from here? There was a company, there was a guy actually,
*  Eric Jones and Travis Vought. They were two friends who founded a company called Enthought.
*  It's here in Austin, still here. And Eric contacted me at the time when I was a
*  graduate student still. And he said, hey, why don't you come down? We want to build a company.
*  We're thinking of a scientific company and we want to take what you're doing and kind of add it to
*  some stuff that he'd done. He'd written some tools. And then Piero Peterson had done F2Py.
*  Let's come together and build, pull this all together and call it SciPy. So that's the origin
*  of the SciPy brand. It came from, you know, multi-pack and a whole bunch of modules I'd written,
*  plus a few things from some other folks and then pull together in a single installer.
*  SciPy was really a distribution of Python, masquerading as a library.
*  How did you think about SciPy in context of Python, in context of Numeric?
*  So we saw SciPy as a way to make an R&D environment for Python, like use Python,
*  dependent on Numeric. So Numeric was the array library we depended on. And then from there,
*  extend it with a bunch of modules that allowed for, and at the time the original vision of SciPy was
*  to have plotting, was to have, you know, the REPL environment and kind of a whole, really a whole
*  data environment that you could then install and get going with. And that was kind of the thinking.
*  It didn't really evolve that way, right? It sort of had a, but one, it's really hard to do
*  massive scale projects with open source collectives. They actually, there's sort of
*  an intrinsic cooperation limit as to which, you know, too many cooks in the kitchen, you know,
*  you can do amazing infrastructure work. When it comes down to bringing it all together into a
*  single deliverable, that actually requires a little more product management that is not,
*  that doesn't really emerge from the same dynamic. So it struggled, you know, struggled to get
*  almost too many voices. It's hard to have everybody agree, you know, consensus doesn't really work at
*  that scale. You end up with politics, you know, with the same kind of things that's happening in
*  large organizations trying to decide on what to do together. So consensus building was still,
*  was challenging at scale as more people came in, right? Early on it's fine because there's nobody
*  there. And so it works, but then as you get more successful and more people use it, all of a sudden,
*  oh, there's this scale at which this doesn't work anymore and we have to come up with different
*  approaches. So SciPy came out officially in 2001, was the first release. Most of the time,
*  I remember the days of getting that release ready. It was a Windows installer and there were bugs on
*  how, you know, the Windows compiler handled complex numbers and you were chasing segmentation
*  faults. It's a lot of work. There was a lot of effort, had nothing to do with my area of study.
*  And at the same time, I had just gotten an offer. So he wondered if I wanted to come down and help
*  him start that company with his friend. And at the time I was like, I was intrigued, but I was
*  square in a path, an academic path. And I had just got an offer to go and teach at my alma mater.
*  So I took that tenure track position. And SciPy, and kind of then I started working on SciPy as a
*  professor too. So I left, I got to Mayo Clinic, graduated, wrote my thesis using SciPy, wrote,
*  you know, there's images that were created. Now the plotting tool I used was something
*  from Yorick actually. It was a plotting PLT, kind of a plotting language that I used.
*  Yorick is a programming language?
*  It was a programming language. It had a plotting tool, Dislin. It had integration to Dislin. I
*  ended up using Dislin plus some of the plotting from Yorick linked to from Python. Anyway, it was
*  people don't plot that way now, but this is before, and SciPy was trying to add plotting,
*  right? It didn't have much success. Really the success of plotting came from John Hunter,
*  who had a similar experience to my experience, my kind of maverick experience as a person just
*  trying to get stuff done and kind of having more time than money maybe, right?
*  And John Hunter created what?
*  Matplotlib.
*  He's the creator of Matplotlib.
*  Yeah. So John Hunter was, you know, he wasn't a student at the time, but he was working in
*  Quant Field and he said, we need better plotting. So he just went out and said, cool, I'll make a
*  new project and we'll call it Matplotlib. And he released in 2001, about the same time that SciPy
*  came out. And it was separate library, separate install, use numeric, SciPy use numeric. And so
*  SciPy, you know, 2001 we released SciPy and then Enthoq created a conference called SciPy,
*  which brought people together to talk about the space. And that conference is still ongoing.
*  It's one of the favorite conferences of a lot of people because it's changed over the years,
*  but early on it was a collection of 50 people who care about scientists mostly,
*  practicing scientists who want to care about coding and doing it well and not using Matlab.
*  And I remember being driven by, you know, I like Matlab, but I didn't like the fact that
*  so I'm not opposed to proprietary software. I'm actually not an open source zealot. I love open
*  source for the, what it brings, but I also see the role for proprietary software. But what I didn't
*  like was the fact that I would develop code and publish it and then effectively telling somebody
*  here to run my code, you have to have this proprietary software. Right. And there's also
*  culture around Matlab as much, because I've talked to a few folks, MathWorks grades, yeah.
*  I mean, there's just a culture they try really hard, but it just, there's this corporate
*  IBM style culture that's like, or whatever. I don't want to say negative things about IBM,
*  whatever, but there's a- No, it's really that connection. It's something I'm in the middle
*  of right now is the business of open source and how do you connect the ethos of cooperative
*  development with the necessity of creating profits, right? And like right now today,
*  I'm still in the middle of that. That's actually the early days of me exploring this question.
*  So I was writing SciPy. I mean, as an aside, I also had, so I had three kids at the time. I have
*  six kids now. I got married early, wanted a family. I had three kids and I remember reading,
*  I read Richard Stallman's post and I was a fan of Stallman. I would read his work. I liked this
*  collective ideas he would have. Certainly the ideas on IP law, I read a lot of stuff. But then
*  he said, okay, well, how do I make money with this? How do I make a living? How do I pay for my kids?
*  All this stuff was in my mind. Young graduate student making no money thinking I got to get a
*  job. And he said, well, I think just be like me and don't have kids. That's just don't-
*  That's his take on it. That was what he said in that moment. That's the thing I read and I went,
*  okay, this is a train I can't get on. There has to be a way to preserve the culture of open source
*  and still be able to make sufficient money to feed your kids. Yes, exactly. There's got to be.
*  That actually led me to a study of economics because at the time I was ignorant and I really
*  was. I'm actually embarrassed for educational system that they could let me and I was valedictorian
*  in my high school class and I did super well in college. Academically, I did great. But the
*  fact that I could do that and then be clueless about this key part of life, it led me to go,
*  there's a problem. I should have learned this in fifth grade. I should have learned this in
*  eighth grade. Everybody should come out with a basic knowledge of economics.
*  You're an interesting example because you've created tools that change the lives of
*  probably millions of people and the fact that you don't understand at the time of the creation of
*  those tools, the basics economics of how to build up a giant system is a problem.
*  Yeah, it's a problem. And so during my PhD at the same time, this is back in 98, 99 at the same time,
*  I was in a library. I was reading books on capitalism. I was reading books on Marxism.
*  I was reading books on what is this thing? What does it mean? And I encountered a... Basically,
*  what I encountered a set of writings from people that said they were the inheritors of Adam Smith.
*  Read Adam Smith for the first time, which is the wealth of nations and this notion of emergent
*  societies and realized, oh, there's this whole world out here of people.
*  And the challenge of economics is also political. Because economics, people, different parties
*  running for office, they want their economic friends. They want their economists to back them
*  up or to be their magicians, the magicians in Pharaoh's court, the people that are going to say,
*  hey, you should listen to me because I've got the expert who says this. And so it gets really muddled.
*  But I was looking at it as a scientist going, what is this space? What does this mean? How does
*  Paris get fed? What is money? How does it work? And I found a lot of writings I really loved. I
*  found some things that I really loved and I learned from that. It was writings from people
*  like Von Missess. He wrote a paper in 1920 that still should be read more than it is. It was the
*  economic calculation problem of the socialist Commonwealth. It was basically in response to
*  the Bolshevik revolution in 1917. And his basic argument was, it's not going to work to not have
*  private property. You're not going to be able to come up with prices. The bureaucrats aren't going
*  to be able to determine how to allocate resources without a price system. And a price system emerges
*  from people making trades. And they can only make trades if they have authority over the thing
*  they're trading. And that creates information flow that you just don't have if you try to top down
*  it. And it's like, huh, that's a really good point. Yeah. The price is to have a signal that's used.
*  And it's important to have that signal when you're trying to build a community of productive people
*  like you would in the software engineering space. Yeah. The prices are actually an important
*  signaling mechanism. Right. And that money is just a bartering tool. Right. So this is the first time
*  I've encountered any of this concept. Right. And the fact that, oh, this is actually really critical.
*  Like it's so critical to our prosperity and that we're dangerously not learning about this,
*  not teaching our children about this. So you had the three kids and you had to make some hard
*  decisions. Had to make some money. Right. Had to figure it out. But I didn't really care. I mean,
*  I've never been driven by money. Just need it. Right. To eat. So how did that resolve itself in
*  terms of side by? So I would say it didn't really resolve itself. It sort of started a journey that
*  I'm continuing on. I'm still on, I would say. I don't think it resolved itself. But I will say,
*  I went in eyes wide open. Like I knew that there were problems with giving stuff away and creating
*  market externalities. That the fact that, yeah, people might use it and I might not get paid for
*  it and I'll have to figure something else out to get paid. Like at least I can say I'm not bitter
*  that a lot of people have used stuff that I've written and I haven't necessarily benefited
*  economically from it. Like I've heard other people be bitter about that when they write or they talk
*  like, oh, I should have got more value out of this. And I'm also, I want to create systems that let
*  people like me who might have these desires to do things, let them benefit. So it actually creates
*  more of the same. Not to turn on your bitterness module, but there's some aspects. I wish there
*  mechanisms for me to reward whoever created SciPy and NumPy because it brought so much joy to my
*  life. I appreciate that. And I think the tip jar notion was there. I appreciate that. And I think
*  but there should be a very frictionless mechanism. I totally agree. I would love to talk about some
*  of the ideas I have because I actually came across, I think I've come up with some interesting notions
*  that could work, but they'll require anything that will work takes time to emerge. Like things don't
*  just turn overnight. That's definitely one thing I've also understood and learned is any fixes.
*  That's why it's kind of funny. We often give credit to, you know, oh, this president gets elected
*  and oh, look how great things have done. And I saw that when I had a transition in a condo,
*  when a new CEO came in, right? And it's like the success that's happening, there's an inertia there.
*  Yeah. And sometimes the decision you made like 10 years before is the reason why the success is
*  the- Right, exactly. So we're sort of just going around taking credit for stuff.
*  The credit assignment has like a delay to it that makes the credit assignment basically wrong.
*  Wrong more than right. Exactly. And so I'm like, oh, this is, you know, that's the stuff I would
*  read a ton about, you know, early on. So I don't, I feel like I'm with you. Like I want the same
*  thing. I want to be able to, and honestly, not for personally, I've been happy. I've been happy. I
*  feel like I don't have any, I mean, we've been done reasonably okay, but I've had to pursue it.
*  Like that's really what started my trajectory from academia is reading that stuff led me to say, oh,
*  entrepreneurship matters. I love software, but we need more entrepreneurs and I want to understand
*  that better. So once I kind of had that virus infect my brain, even though I was on a trajectory
*  to go to a tenure track position at a university and I was there for six years, I was kind of
*  already out the door when I started. And we can get into that, but-
*  Can I just ask you a quick question on, is there some design principles that were in your mind
*  around SciPy? Like, is there some key ideas that were just like sticking to you that this is the
*  fundamental ideas? Yeah, I would say so. I would think it's basically accessibility to scientists,
*  like give them, give scientists and engineers tools that they don't have to think a lot about
*  programming. So give them really good building blocks, give them functions that they want to
*  call and sort of just the right length of spelling. There's one tradition in programming where it's
*  like, make very, very long names. And you can see it in some programming languages where the names
*  take half the screen. And in the 4chan world, characters had to be six letters early on.
*  And that's way too much, too little. But I was like, I liked to have names that were informative,
*  but short. So even though Python, well, this is a different conversation, but
*  documentation is doing some work there. So when you look at great scientific
*  libraries and functions, there's a richness of documentation that helps you get into the details.
*  The first glance at a function gives you the intuition of all it needs to do by looking at
*  the headers and so on. But to get the depths of all the complexities involved, all the options
*  involved, documentation does some work. Documentation is essential. So we thought
*  about several things. One is we wanted plotting. We wanted interactive environment. We wanted good
*  documentation. These are things we knew we wanted. The reality is those took about 10 years to evolve,
*  given the fact that we didn't have a big budget. It was all volunteer labor.
*  When Enthot got created and they started to try to find projects people would pay for pieces,
*  and they were able to fund some of it. Not nearly enough to keep up with what was necessary.
*  And no criticism, just simply the reality. I mean, it's hard to start a business and then
*  do consulting and then also promote an open source project that's still fairly new.
*  Cypho is fairly niche. We stayed connected all while I was a student, sorry, a professor. I went
*  to BYU and started to teach electrical engineering, all the applied math courses. I loved teaching
*  signal processing, probability theory, electromagnetism. If you look at rate my
*  professor, which my kids love to do, I got some bad reviews because people-
*  What was the criticism?
*  I would speak too high of a level. I definitely had a calibration problem coming out of graduate
*  work where I hate to be condescending to people. I really have a ton of respect for people,
*  fundamentally. My fundamental thing is I respect people. Sometimes that can lead to a... I was
*  thinking they had more knowledge than they did. And so I would just speak at a very high level,
*  assume they got it.
*  But they need to rise to the standard that you set. I mean, that's one of the-
*  It is.
*  Some of the greatest teachers do that.
*  And I agree. And that was kind of what was inspiring me. But you also have to... I cannot
*  say I was articulate to some of the greatest teachers. One classic example, when I first
*  taught at BYU, my very first class, it was overheads, transparencies, overheads.
*  The four projectors were really that common. I took transparencies, I'm writing my notes out.
*  I go in, room's half dark. I just blaring through these transparencies. Here it is,
*  here it is, here it is. And I gave a quiz after two weeks. No one knew anything.
*  Nothing I had taught had gotten anywhere. And I realized, okay, this is not working. And so I
*  put away the transparencies and I turned around and just started using the chalkboard.
*  And what it did is it slowed me down. The chalkboard just slowed me down and gave
*  people time to process and to think. And then that made me focus. My writing wasn't great on
*  their chalkboard, but I really loved that part of the teaching. So that entered SciPy's world in
*  terms of we always understood that there's a didactic aspect of SciPy. How do you take the
*  knowledge and then produce it? The challenge we had was the scope. Ultimately, SciPy was everything.
*  So 2001, when it first came out, people were starting to use it. No, this is cool. This
*  tool we actually use. At the same time, 2001 timeframe, there was a little bit of
*  like the Hubble Space Telescope, the folks at Hubble. And started saying, hey, Python,
*  we're going to use Python for processing images from Hubble. And so Perry Greenfield was a good
*  friend and running that program. And he had called me before I left to BYU and said, you know,
*  we want to do this, but numeric actually has some challenges in terms of, you know, it's not the
*  array doesn't have enough types. We need more operations, you know, broadcast needs to be a
*  little more settled. They wanted record arrays. They want to, you know, record arrays are like
*  a data frame, but a little bit different, but they want a more structured data. So he had called me
*  even early on then and he said, yeah, what do you want to work on something to make this work? I
*  said, yeah, I'm interested, but I'm going here and we'll see if I have time. So in the meantime,
*  while I was teaching and SciPy was emerging and I had a student, I was constantly while I was
*  teaching, trying to figure out a way to fund this stuff. So I had a graduate student, my only graduate
*  student, a Chinese fellow, Liu Hongze is his name, great guy. He wrote a bunch of stuff for
*  iterative linear algebra, like got into writing some of the iterative linear algebra tools that
*  are currently there in SciPy and they've gotten better since, but this is in 2005, kept working
*  on SciPy. But Perry had started working on a replacement to numeric called Numere. And in 2004,
*  a package called ND image. It was an image processing library that was written for Numere
*  and it had in it a morphology tool. I don't know if you know what morphology is. It's open,
*  dilations, there was sort of this, as a medical imaging student, I knew what it was because it
*  was used in segmentation a lot. And in fact, I'd wanted to do something like that in Python and
*  SciPy, but just had never gotten around to it. So when it came out, but it worked only on Numere
*  and SciPy needed numeric. And so we effectively had the beginning of this
*  split and numeric and Numere didn't share data. They were just two. So you could have a gigabyte
*  of numeric number data and gigabyte of numeric data and they wouldn't share it. And so you have
*  these, then you have these scientific libraries written on top. I got really bugged by that.
*  I got really like, oh man, this is not good. We're not cooperating now. We're not, we're sort of
*  redoing each other's work and we're just this young community. So that's what led me, even though
*  I knew it was risky because my, you know, I was on a tenure track position, 2004 I got reviewed.
*  They said, Hey, things are going okay. You're doing well. Paper's coming out, but you're kind
*  of spending a lot of time in this open source stuff. Maybe you do a little less of that and
*  a little more of the paper writing and grant writing, which was naive, but it was definitely
*  the time, you know, the thinking that still goes on. You're basically creating a thing,
*  which enables science in the 21st century. Right. Maybe don't emphasize that so much in your free
*  or tenure. It illustrates some of the challenges. It does. It's, and it's people mean well,
*  but we've gotten broken in a bunch of ways. Certain things, programming, understanding the role of
*  software engineering, programming society is a little bit like, exactly. Now I was in an
*  electrical engineering position. Right. That's even worse. Yeah. It was very, they were very
*  focused. And so, you know, good people and I had a great time. I love my time. I love my teaching.
*  I loved all the things I did there. The problem was the split was happening in this community
*  that I loved. I saw people and I went, oh my gosh, this is going to be, this is not great.
*  And so I happened, you know, fate, I had a class I had signed up for. I was trying to build an MRI
*  system. So I had a kind of a radio, a set of a radio, a digital radio class, a digital MRI class.
*  And I had people sign up, two people signed up, then they dropped. And so I had nobody in this
*  class. So, and I didn't have any other courses to teach. And I thought, oh, I've got some time
*  and I'll just write, I'll just write a, a merger of numeric and number A. Like I'll basically take
*  the numeric code base at the features number A was adding and then kind of come up with a single
*  array library that everybody can use. So that's where NumPy came from was my thinking, hey,
*  I can do this. And who else is going to, because at that point I'd been around the community long
*  enough and I'd written enough C code. I knew, I knew the structures. And I, in fact, my first
*  contribution to numeric had been writing the C API documentation that went in the first
*  documentation for NumPy for numeric. Sorry, this is Paul Dubois, David Asher, Conrad Hinson,
*  and myself. I got credit because I wrote this chapter, which is all the C API of, of numeric,
*  all the C stuff. So I said, ah, I probably the one to do it. You know, nobody else is going to do
*  this. So it was sort of out of a, out of a sense of duty and passion, knowing that I don't think
*  my academic, I don't think the department here is going to appreciate this, but I,
*  it's the right thing to do. It was like,
*  Can we just link on that moment? Because the importance of the way you thought and the action
*  you took, I feel is, is understated and is rare. And I would love to see so much more of it because
*  what happens as the tools become more popular, there's a split that happens and it's a truly
*  heroic and impactful action to in those early, in that early split, to step up and you, it's like
*  great leaders throughout history, like get, what is the Braveheart, like get on a horse
*  and, and rally the troops. Because I think that can have, make a big difference. We have
*  TensorFlow versus PyTorch in the machine learning community. We have the same problem today. Yeah.
*  I wonder, it's actually bigger. I wonder if it's possible to, in the early days, to rally the troops.
*  It is possible, especially in the early days. The longer it goes, the harder, right? And the more
*  energy in the factions, the harder. But in the early days it is possible and it's extremely
*  helpful. And there's a willingness there, but the challenge is there's usually not a willingness to
*  fund it. There's not a willingness to, you know, like I was literally walking into a field saying
*  I'm going to do this and here I am, like, you know, I have five kids at home now.
*  Pressure builds.
*  Sometimes my wife hears these stories and she's like, you did what? I thought we were going to,
*  I thought you were actually on a path to make sure we had resources and money. But,
*  but again, there's a, there's an aspect. I'm a very hopeful person. I'm an optimistic person,
*  my nature. I love people. I learned that about myself later on. Part of my, my religious beliefs
*  actually lead to that. And it's why I hold them dear because it's actually how I feel about,
*  that's what, it's what leads me to this, to these attitudes, sort of this hopefulness and this
*  sense of, yeah, it may not, it may not work out for me financially or maybe, but that's not the
*  ultimate gain. Like that's a thing, but it's not, you know, that's not the scorecard for me. And so
*  I just wanted to be helpful. And I knew, and partly because of these sci-pi conferences,
*  because of the mailing list conversations, I knew there was a lot of need for this.
*  Right. And so I had this, it wasn't like I was alone in terms of no feedback. I had these people
*  who knew, but it was crazy. Like people who at the time said, yeah, we didn't think you'd be able
*  to do it. We thought it was crazy. And also instructive, like practically speaking,
*  that you had a cool feature that you were chasing in the morphology. Like the, like it's, it's not,
*  there's an end result. It's not some visionary thing. I'm going to unite the community. You're
*  like, you were actually practically, this is what one person actually could do and actually build.
*  Cause that is important. Cause you can get over your skis. You can definitely get over your skis.
*  And I had, in fact, this almost got me over my skis. Right. I would say, well, in retrospect,
*  I hate looking back. We, I can tell you all the flaws with numpy, right? When I go into it,
*  there's lots of stuff that I'm like, oh man, that's embarrassing. That was wrong. I wish I had
*  somebody slap me with a wet fish there. Like I needed, like what I'd wished I'd had was somebody
*  with more experience and certainly library writing and array library. There's like,
*  I wish I had me, I could go back in time and go do this, do that. There's a Morton Vien.
*  Cause there's things we did that are still there that are problematic,
*  that created challenges for later. And I didn't know it at the time. I didn't understand how
*  important that was. And in many cases didn't know what to do. Like there was pieces of the design of
*  numpy. I didn't know what to do until five years ago. Now I know what they should have been done,
*  Ben, but I didn't know at the time and nobody, and I couldn't get the help. Anyway, so I wrote it.
*  It took about, it took four months to write the first version, then about 14 months to make it
*  usable. But it was, it wasn't, it was that first four months of intense writing, coding, getting
*  something out the door that worked. That was, it was, it was definitely challenging. And then the
*  big thing I did was create a new type object called D type. That was probably the sync, the
*  contribution. And then the fact that I added a broad, not just broadcasting, but advanced indexing
*  so that you could do, um, masks indexing and indirect indexing instead of just slicing.
*  And so for people who don't know, and maybe you can elaborate numpy, I guess the vision
*  in the narrowest sense is to have this object that represents and dimensional arrays. And like at any
*  level of abstraction you want, but basically it could be a black box that you can investigate
*  in ways that you would naturally want to investigate such objects. Yes, exactly. So you
*  could do math on it easily math on it. So it had, so it had an associated library of math operations
*  and effectively SciPy became an even larger operate set of live math operations. So the key for me was
*  I was going to write numpy and then move SciPy to depend on numpy. In fact, early on, one of the
*  initial proposals was that we would just write SciPy and it would have the numeric object inside
*  of it and it'd be SciPy dot array or something that turned out to be problematic because numeric
*  already had a little mini library of linear algebra and some functions and it had enough momentum,
*  enough users that nobody wanted to, they wanted backward compatibility. One of the big challenges
*  of numpy was I had to be backward compatible with both numeric and number in order to allow both of
*  those communities to come together. There was a ton of work in creating that backward compatibility
*  that also created echoes in today's object. Like some of the complexity in today's object is actually
*  from that goal of backward compatibility in these other communities, which if you didn't have that,
*  you'd do something different, which is instructive because a lot of things are there. You know,
*  what is that there for? It's like, well, it was, it's a remnant. It's an artifact of its historical
*  existence. By the way, I love the empathy and the lack of ego behind that because I feel,
*  you see that in the split in the JavaScript frameworks, for example, the arbitrary branching
*  is, I think in order to unite people, you have to kind of put your ego aside and truly listen to
*  others. Like what do you love about number rate? What do you love about numeric? Like actually get
*  a sense. We're talking about languages earlier, sort of empathize to the culture of the people
*  that love something about this particular API, some, the naming style or the use,
*  the actual usage patterns and like truly understand them. And so that you can like
*  create that same draw in the United. I completely agree. And you have to also have enough passion
*  that you'll do it. It can't be just like a perfunctory, oh yeah, so I'll listen to you.
*  And then I'm not really that excited about it. So it really is an aspect. It's a philosophical,
*  there's a philia, there's a love of a steaming of others. That's actually at the heart of what
*  it's sort of a life philosophy for me, right? That I'm constantly pursuing and that helped,
*  absolutely helped. It makes me wonder in a philosophical, like looking at human civilization
*  as one object, it makes me wonder how we can copy and paste Travis's in this.
*  Some aspects, maybe. Some aspects, right, right. Exactly. Well, it's a good question. How do we
*  teach this? How do we encourage it? How we lift it? Because so much of the software world,
*  it's giant communities, right? But it seems like so much is moved by like little individuals. You
*  talk about like Linus Torvald. It's like, can you, could you have not, could you have had Linux
*  without him? Could you, it's like, Gido and Python, Gido and Python. I mean, the SciPy community
*  particularly, it's like I said, we wanted to build this big thing, but ultimately we didn't. What
*  happened is we had Mavericks and champions like John Hunter who created Matplotlib. We had Fernando
*  Perez who created IPython. And so we sort of inspired each other, but then there's sort of
*  a culture of this selfless, the stewardship mentality as opposed to ownership mentality,
*  the stewardship and community focused, community focused, but intentional work. Like not waiting
*  for everybody else to do the work, but you're doing it for the benefit of others and not worried
*  about what you're going to get. You're not worried about the credit. You're not worried
*  about what you're going to get. You're worried about, I later realized that I have to worry a
*  little about credit, not because I want the credit, because I want people to understand what led to
*  the results. Like I don't, it's not, it's not about me is I want to understand this is what led to the
*  result. So let's like, I think doing, and this is what had no impact on the result. Like let's,
*  let's promote this. Just like you said, I want to promote the attributes that led, that helped make
*  us better off. How do we make more of West, West McKinney? Like West McKinney was critical to the
*  success of Python because of his creation of pandas, which was the roots of that were in,
*  were all the way back in numeric and num array and numpy where numpy created an array of records.
*  West started to use that almost like a data frame, except it's an array of records and data frame.
*  The challenge is, okay, if you want to augment it at another column, you have to insert, you have to
*  do all this memory movement to insert a column, whereas data frames became, oh, I'm going to have
*  a loose collection of arrays. So it's a record of arrays that is the heart of a data frame.
*  And we thought about that back in the memory days, but West ended up doing the work to build it. And
*  then, then also the operations that were relevant for data processing. What I noticed is just that
*  each of these little things creates just another tick, another up. So numpy ultimately took a
*  little while, about six months in people started joining me, you know, Francesc, Alt-head, Robert
*  Kern, Charles Harris. And these people are many of the unsung heroes, I would say, people who are,
*  you know, they don't, they sometimes don't get the credit they deserve because they were critical
*  both to support, like, you know, it's, it's hard and you want, you need some support, people need
*  support and I needed just encouragement and they were helping encourage by contributing. And, and
*  once the big thing for me was when John Hunter, he had previously done kind of a simple thing called
*  numerics to kind of, you know, between numeric and num array, he had a little high level tool that
*  would just select each one for Matplotlib. In 2006, he finally said, we're going to just make numpy
*  the dependency of Matplotlib. As soon as he did that, and I remember specifically when he did that,
*  I said this, okay, we've done it. Like that was when I knew we had seen success. Before then it
*  was still, you know, doing sure, but that kind of started a roller coaster and then 2006 to 2009.
*  And then I've been floored by the, by what it's done. Like I hadn't, I knew it would help. I didn't
*  have no idea how much it would help. Right. So, and it has to do with again, the language thing,
*  it just, people started to think in terms of numpy. Like, and that opened up a whole new way
*  of thinking. And part of the story that you kind of mentioned, but maybe you can elaborate is it
*  seems like at some point in the story, Python took over science and data science and not bigger
*  than that. The scientific community started to think like programmers or started to utilize the
*  tools of computers to do like at a scale that wasn't done with Fortran, like at this gigantic
*  scale, they started to opening their heart and then Python was the thing. I mean, there's a few
*  other competitors, I guess, but Python, I think really, really took over. I agree. There's a lot
*  of stories here that are kind of during this journey because this is sort of the start of this
*  journey in 2005, six. So my tenure committee, I applied for tenure in 2006, 2007, it came back.
*  I split the department. I was very polarizing. I had some huge fans and then some people said,
*  no way. Right. So it was very, I was a polarizing figure in the department. It went all the way up
*  to the university president. Ultimately, my department chair had the sway and they didn't
*  say no. They said, come back in two years and do it again. And I went, at that point, I was like,
*  I had this interest in entrepreneurship, this interest in not the academic circles, not the,
*  like, how do we make industry work? So I do have to give credit to that exploration of economics
*  because that led me, oh, I had a lot of opinions. I was actually very libertarian at the time.
*  And I still have some libertarian trends, but I'm more of a collectivist libertarian.
*  So you value broadly, philosophically freedom.
*  I value broadly, philosophically freedom, but I also understand the power of communities,
*  like the power of collective behavior. And so what's that balance, right? That makes sense.
*  So by the time I was just, I got to go out and explore this entrepreneur world. So I left
*  academia. I said, no thanks. Called my friend Eric here, who had, his company was going. I said,
*  hey, could I join you and start this trend? And he, at that time they were using SciPy a lot.
*  They were trying to get clients. And so I came down to Texas and in Texas is where I sort of,
*  it's my entrepreneur world, right? I left academia and went to entrepreneur world in 2007. So I moved
*  here in 2007, kind of took a leap, knew nothing really about business, knew nothing about a lot
*  of stuff there. There's, you know, for a long time, I've kept some connections to a lot of academics
*  because I still value it. I still love the scientific tradition. I still value the
*  essence and the soul and the heart of what is possible. Don't like a lot of the administration
*  and the kind of, we can go into detail about why and where and how this happens. What are
*  the challenges? I mean, I don't know, but I'm with you. So I'm still affiliated with MIT.
*  I still love MIT because there's magic there. Yeah. There's people I talk to, like researchers,
*  faculty, in those conversations and the whiteboard and the, and just the conversation,
*  that's magic there. All the other stuff, the administration, all that kind of stuff
*  seems to, you don't want to say too harshly criticize sort of bureaucracies,
*  but there's a lag that seems to get in the way of the magic. And I don't, I still have a lot of hope
*  that that can change because I don't often see that particular type of magic elsewhere in the
*  industry. So like, we need that and we need that flame going. And it's the same thing as exactly as
*  you said, it has the same kind of elements like the open source community does. And, but then if
*  you, like the reason I stepped away, the reason I'm here, just like you did in Austin is like,
*  if I want to build one robot, I'll stay at MIT. But if I want to build millions and make money
*  enough to where I can explore the magic of that, then you can't. And I think that dance is,
*  that translational dances has been lost a bit. Right. And there's a lot of reasons for that.
*  I'm certainly not an expert on this stuff. I can opine like anybody else, but I,
*  I realized that I wanted to explore entrepreneurship, which I, and really figure out,
*  and it's been a driving passion for 20 years, 20, 25 years. How do we connect capital markets
*  and company? Cause again, I fell in love with the notion of, oh, profit seeking on its own is not a
*  bad thing. It's actually a coordination mechanism for allocating resources that,
*  you know, non, in an emergent way, right. That respects everybody's opinions. Right. So this is
*  actually powerful. So, so I say all the time when I make a company and we do something that makes a
*  profit, what we're saying is, Hey, we're collecting of the world's resources and voluntarily people
*  are asking us to do something that they like. And that's a huge deal. And so I really liked that
*  energy. So that's what I came to do and to learn and to try to figure out. And that's what I've
*  been kind of stumbling through since for the past 14 years. 2007. So you were still.
*  So NUPI was just emerging, right? One of the things I've done, it's worth mentioning because
*  it's emphasized the exploratory nature of my thinking at the time. I said, well, I don't know
*  how to fund this thing. I've got a graduate student I'm paying for, and I've got no funding for him.
*  And I had done some fundraising from the public to try to get public fundraisers for my lab.
*  I didn't really want to go out and just do the fundraising circuit the way it's traditionally
*  done. So I wrote a book and I said, I'm going to write a book and I'm going to charge for it.
*  It was called Guide to NUPI. And so ultimately NUPI became documentation driven development
*  because I basically wrote the book and made sure the stuff worked to the book would work.
*  So it really helped actually make NUPI become a thing. So writing that book, and it was not a,
*  it's not a page turner. Guide to NUPI is not a book you pick up and go, Oh, this is great,
*  over the fire. But it's where you could find the details. Like how'd all this work?
*  And a lot of people loved that book.
*  And so a lot of people ended up, so I, but I said, look, I need it. So I'm going to charge for it.
*  And I got some flack for that. Not that much, just probably five angry messages, people yelling at
*  me saying I was a bad guy for charging for this book.
*  Was one of them Richest Alman?
*  No.
*  Just kidding.
*  No, I haven't really had any interaction with him personally, like I said. But there were a few,
*  but actually surprisingly not. There was actually a lot of people like, no, it's fine. You can charge
*  for a book. That's no big deal. We know that's a way you can, you can try to make money around
*  open source. So, so what I did, I did an interesting way. I said, well, you know, kind of my ideas
*  around, around IP law and stuff. I love the idea. You can share something, you can spread it. Like
*  once it's the fact that you have a thing and copying is free, but the creation is not free.
*  So how do we, how do you fund the creation and allow the copying, right? And then software
*  is a little more complicated than that because creation is actually a continuous thing. That's
*  not like you build a widget and it's done. It's sort of a process of emerging and continuing to
*  create. But I wrote the book and had this market determined price thing. I said, look, I need,
*  I think I said 250,000. If I make 250,000 from this book, it's, I'll make it free. So as soon
*  as I get that much money, or I said five years, right? So there's a time limit.
*  That's really cool. I didn't know this story.
*  Yeah. So I released it on this and it's actually interesting because one of the people who also
*  thought that was interesting ended up being Chris White, who was the director of DARPA project that
*  we got funding through at Anaconda. And the reason he even called us back is because he remembered
*  my name from this book and he thought that was interesting. And so even though we hadn't gone
*  to the demo days, we applied and the people said, yeah, nobody ever gets this without coming to the
*  demo day first. This is the first time I've seen it, but it's because I knew Chris had done this,
*  had this interaction. So it did have impact. I was actually really, really pleased by the result.
*  I ended up in three years, I made 90,000. So I sold 30,000 copies by myself. I just put it up on,
*  use PayPal and sold it. And those are my first taste of kind of, okay, this can work to some degree.
*  All over the world, right? From Germany to Japan, it was actually, it did work. And so I appreciated
*  the fact that PayPal existed and I had a way to get the money. The distribution was simple.
*  This is pre-Amazon book stuff. So it was just publishing a website. It was the popularity of
*  SciPy emerging and getting company usage. I ended up not letting it go to five years and not trying
*  to make the full amount because a year and a half later I was at Entho. I had left academia
*  at Entho and I kind of had a full-time job. And then actually what happened is the documentation
*  people, there's a group that said, hey, we want to do the documentation for SciPy as a collective.
*  They were essentially needing the stuff in the book. And so they kind of asked, hey,
*  could we just use the stuff in your book? And at that point I said, yeah, I'll just open it up.
*  So that's, but it has served its purpose. And the money that I made actually funded my grad student.
*  Like it was actually, I paid him 25,000 a year out of that money.
*  So the funny thing is if you do a very similar kind of experiment now with NumPy or something
*  like it, you could probably make a lot more. It's probably true.
*  Because of the tooling and the community building.
*  Yeah, I agree.
*  And social media, there's just a virality to that kind of idea.
*  I agree. There'd be things to do. I've thought about that. And really I thought about a couple
*  of books or a couple of things that could be done there. And I just haven't, right? Even
*  I tried to hire a ghostwriter this year or two to see if that could help, but it didn't.
*  Part of my problem is I've been so excited by a number of things that stemmed in from that.
*  So I came here, worked at Enthot for four years. Graciously, Eric made me president,
*  then we started to work closely together. We actually helped him buy out his partner.
*  It didn't end great. Unfortunately, Eric and I aren't friends now. I still respect him. I wish
*  we were, but he didn't like the fact that Peter and I started Anaconda. That was not, I mean,
*  so there's two sides to that story, so I'm not going to go into it.
*  But you, as human beings, and you wish you still could be friends.
*  I do. I do. It saddens me.
*  That's a story of great minds building great companies. Somehow it's sad that
*  when there's that kind of... And I hold him in esteem. I'm grateful for him. I think they're
*  doing, you know, Enthot still exists. They're doing great work. Helping scientists. They still
*  run the SciPy conference. They have an R&D platform they're selling now that's a tool
*  that you can go get today, right? So Enthot has played a role in the SciPy in supporting the
*  community around SciPy, I would say. They ended up building a tool suite to write GUI applications.
*  That's where they could actually make that the business could work. And so supporting SciPy and
*  NumPy itself wasn't as possible. They tried. I mean, it was not just because it was just
*  because of the business aspect. And I wanted to build a company that could get venture funding,
*  right? Better for worse. I mean, that's a longer story. We could talk a lot about that, but...
*  And that's where Anaconda came to be.
*  That's where Anaconda came to be.
*  So let me ask you, it's a little bit for fun because you built this amazing thing. And so
*  let's talk about like an old warrior looking over old battles. There's a sad letter in 2012
*  that you wrote to the NumPy mailing list announcing that you're leaving NumPy. And some of the things
*  you've listed, some of the things you regret, or not regret necessarily, but some things to think
*  about. If you could go back and you could fix stuff about NumPy or both sort of in a personal
*  level, but also like looking forward, what kind of things would you like to see changed?
*  Good question. So I think there's technical questions and social questions right there.
*  First of all, I wrote NumPy as a service and I spent a lot of time doing it. And then other
*  people came help make it happen. NumPy succeeded because the work of a lot of people. So it's
*  important to understand that. I'm grateful for the opportunity, the role I had, I could play,
*  and I'm grateful that things I did had an impact, but they only had the impact they had because the
*  other people that came to the story. And so they were essential. But the way data types were
*  handled, the way data types, we had array scalars, for example, that are really just a substitute for
*  a type concept. So we had array scalars or actual Python objects so that there's for a 32-bit float
*  or a 16-bit float or a 16-bit integer, Python doesn't have a natural, it's just one integer,
*  there's one float. Well, what about these lower precision types, these larger precision types?
*  So we had them in NumPy so that you could have a collection of them, but then have an object in
*  Python that was one of them. And there's questions about like in retrospect, I wouldn't have created
*  those up and improved the type system. Like made the type system actually a Python type system,
*  as opposed to currently it's a Python one level type system. I don't know if you know the
*  difference between Python one, Python two, it's kind of technical, kind of depth, but Python two,
*  one of its big things that Guido did, it was really brilliant. It was he actually,
*  Python one, all classes, new objects were one. So he was a user, wrote a class. It was an instance
*  of a single Python type called the class type. In Python two, he used a meta typing hook to
*  actually go, oh, we can extend this and have users write classes that are new types.
*  So he was able to have your user classes be actual types and the Python type system got a lot more
*  rich. I barely understood that at the time that NumPy was written. And so I essentially in Python,
*  in NumPy created a type system that was Python one era. It was every D type is an instance of
*  the same type, as opposed to having new D types be really just Python types with additional metadata.
*  What's the cost of that? Is it efficiency? Is it usability?
*  It's usability primarily. The cost isn't really efficiency. It's the fact that it's clumsy
*  to create new types. It's hard. And then one of the challenges you want to create new types,
*  you want a quaternion type, or you want to add a new posit type, or you want to, so it's hard.
*  And now if we'd have done that well, when Numba came on the scene where we could actually compile
*  Python code, it would integrate with that type system much cleaner. And now all of a sudden you
*  could do gradual typing more easily. You could actually have Python when you add Numba plus
*  better typing could actually be a, you'd smooth out a lot of rough edges.
*  But there's already, there's like, but are you talking about from the perspective of
*  developers within NumPy or users of NumPy? Because developers have new, not really users
*  of NumPy so much. It's the development of NumPy. So you're thinking about like,
*  how to design NumPy so that it's contributors.
*  Yeah, the contributors are, it's easier. It's easier. It's less work to make it better and to
*  keep it maintained. And where that's impacted things, for example, is the GPU. Like all of a
*  sudden GPUs start getting added and we don't have them in NumPy. Like NumPy should just work on
*  GPUs. The fact that we have to download a whole other object called Kupai to have arrays on GPUs
*  is just an artifact of history. Like there's no fundamental reason for it.
*  Well, that's really interesting. If we could sort of go on that tangent briefly is
*  you have PyTorch and other library like TensorFlow that basically tried to mimic
*  NumPy. Like you've created a sort of platonic form of multi-dimensional.
*  Yeah, exactly. Well, and the problem was they didn't realize that.
*  Yeah.
*  The platonic form has a lot of edges. They're like, well, we should cut those out before we present it.
*  So I wonder if you can comment, is there like a difference between their implementations? Do you
*  wish that they were all using NumPy or like in this abstraction on GPU? And sorry to interrupt,
*  there's GPUs, ASICs, there might be other neuromorphic computing. There might be other kind of,
*  or the aliens will come with a new kind of computer. Like an abstraction that NumPy should
*  just operate nicely over the things that are more and more and smarter and smarter with
*  this multi-dimensional arrays.
*  Yeah. Yeah. I have several comments there. We are working on something now called data-api.org.
*  Data-api.org. You can go there today. And it's our answer. It's my answer. It's not just me. It's me
*  and Rolf and Athen and Aaron and a lot of companies are helping us at QuantSite Labs.
*  It's not unifying all the arrays, it's creating an API that is unified. So we do care about this and
*  trying to work through it. I actually had the chance to go and meet with the TensorFlow team
*  and the PyTorch team and talk to them after exiting Anaconda. Just talking about it because
*  the first year after leaving Anaconda in 2018, I became deeply aware of this and realized that,
*  oh, this split in the array community that exists today makes what I was concerned about in 2005
*  pretty parochial. It's a lot worse. Now there's a lot more people, so perhaps the industry can
*  sustain more stacks. There's a lot of money, but it makes it a lot less efficient. I mean,
*  but I've also learned to appreciate, it's okay to have some competition. It's okay to have different
*  implementations, but it's better if you can at least refactor some parts. I mean,
*  you're going to be more efficient if you can refactor parts.
*  It's nice to have competition over things over what is nice to have competition.
*  Yeah, innovative. And then maybe on the infrastructure, however you define
*  infrastructure, maybe it's nice to have come together.
*  Cooperation, exactly. I agree. But it was interesting to hear the stories. I mean,
*  TensorFlow came out of the C++ library. Jeff Dean wrote, I think, there was basically how they were
*  doing inference. And then they realized, oh, we could do this TensorFlow thing. That C++ library,
*  then what was interesting to me was the fact that both Google and Facebook, it's not like
*  they supported Python or NumPy initially. They just realized they had to. They came to this world
*  and then all these were like, hey, where's the NumPy interface? Oh, then they kind of came late
*  to it and then they had these bolt-ons. TensorFlow's bolt-on, I don't mean to offend, but it was so bad.
*  It's the first time that I'm usually, I mean, one of the challenges I have is I don't criticize
*  enough in the sense that I don't give people input enough. I think it's universally agreed upon that
*  the bolt-ons on TensorFlow work. But I went to a talk given at Majorca in Spain and a great guy,
*  he came and gave a talk. I said, you should never show that API again at a PyData conference.
*  That's terrible. You're taking this beautiful system we've created and you're corrupting all
*  these poor Python people, forcing them to write code like that or thinking they should.
*  Fortunately, they adopted Keras and now Keras is better. And so Keras, TensorFlow is fine,
*  it's reasonable. But they bolted it on. Facebook did too. Facebook had their own C++ library for
*  doing inference and they also had the same reaction. They had to do this. One big difference is
*  Facebook, maybe because of the way it's situated in part of FAIR, part of the research library,
*  TensorFlow is definitely used and they couldn't just open it up and let the community
*  change what that is because I guess they were worried about disrupting their operations.
*  Facebook's been much more open to having community input on the structure itself. Whereas Google and
*  TensorFlow, they're really eager to have user community users. People use it and build the
*  infrastructure, but it's much more walled. It's harder to become a contributor to TensorFlow itself.
*  And it's also, this is a very difficult question to answer and don't mean to be throwing shade
*  at anybody, but you have to wonder, it's the Microsoft question of when you have a tool like
*  PyTorch or TensorFlow, how much are you tending to the hackers and how much are you tending to
*  the big corporate clients? Do you tend to the millions of people that are giving you almost
*  no money or do you tend to the few that are giving you a ton of money? I tend to
*  stand with the people because I feel like if you nurture the hackers, you will make the
*  right decisions in the long term that will make the companies happy. I lean that way too.
*  I totally agree. But then you have to find the right data. But it's a balance
*  because you can lean to the hackers and run out of money. Yeah, exactly. Which has been some of
*  the challenge I've faced in the sense that I would look at some of the experiments like NumPy,
*  the fact that we have this split is a factor of I wasn't able to collect more money towards NumPy
*  development. I didn't succeed in the early days of getting enough financial contribution to NumPy
*  so they could work on it. I couldn't work on it full time. I had to just catch an hour here,
*  an hour there. And I basically not like that. I've wanted to be able to do something about that for
*  a long time and try to figure out how. Well, there's lots of ways. Possibly one could say,
*  we had an offer from Microsoft early days of Anaconda. 2014, they offered to come buy us.
*  Right? The problem was the right people at Microsoft didn't offer to buy us. And they were
*  still, it was really, we were like a second, they had really bought, they just bought R, the R
*  company called, it was not R studio, but it was another R company that was emergent. And it was
*  kind of a, well, we should also get a Python play. But they were really doubling down on R.
*  It was where you would go to die. So it was before Sacha was there.
*  Sacha had just started. And the offer was coming from someone two levels down from him.
*  And if it had come from Scott Guthrie, so I got a chance to meet Scott Guthrie, great guy, I like him.
*  If it had offered to come from him, probably would be at Microsoft right now.
*  That'd be fascinating. That would be really nice actually, especially given what Microsoft has
*  since done for the open source community. Yes. I think they're doing well. I really like some of
*  the stuff they've been doing. They're still working on it. They've hired Guido now and they've hired
*  a lot of Python developers. Wait, Guido's not at Microsoft? Yeah, he works at Microsoft.
*  Which he retired, then he came out of retirement and he's working on it.
*  I was just talking to him and he didn't mention this part.
*  Well. I should investigate this further.
*  Well. Because I know he loved Dropbox, but I wasn't sure what he was doing, who he was up to.
*  Well, he was kind of saying he'd retire, but it's literally been five years since I last sat out and
*  really talked to Guido. Guido's a technology expert. I was excited because I'd finally figured
*  out the type system for NumPy. I wanted to talk about that with him and I kind of overwhelmed him.
*  Could you stay on that just for a brief moment because you're a fascinating person in the history
*  of programming. He is a fascinating person. What have you learned from Guido about programming,
*  about life? Yeah, yeah. A lot, actually. I've been a fan of Guido's. We have a chance to talk.
*  Some, I wouldn't say we talk all the time, not really at all. But we talked enough to,
*  I respect his... In fact, when I first started NumPy, one of the first things I did was I asked
*  Guido for a meeting with him and Paul Dubois in San Mateo. I went and met him for lunch and basically
*  to say maybe we can actually, part of the strategy for NumPy was to get it into Python 3
*  and maybe be part of Python. So we talked about that and about that approach. I would have loved
*  to be a fly in the water. That was good. Over the years for Guido, I learned... So he was open. He
*  was willing to listen to people's ideas over the years. Now, generally, I'm not saying universally
*  that's been true, but generally that's been true. So he's willing to listen. He's willing to defer.
*  On the scientific side, he would just kind of defer. He didn't really always understand what
*  we were doing. And he'd defer. One place where he didn't enough was we missed a matrix multiply
*  operator that finally got added to Python, but about 10 years later than it should have.
*  But the reason was because nobody... It takes a lot of effort. And I learned this while I was
*  writing NumPy. I also wrote tools to Python. I became a Python dev and I added some pieces to
*  Python, like the memory view object. I wanted the structure of NumPy into Python. So we didn't get
*  NumPy into Python, but we got the basic structure of it into Python so you could build on it.
*  Nobody did for a while, but eventually he database authors started to. And it's a lot better. They
*  did. And also Antoine Petrou and Stefan Kra actually fixed the memory view object because
*  I wrote the underlying infrastructure in C, but the Python exposure was terrible until they came
*  in and fixed it, partly because I was writing NumPy and NumPy was the Python exposure. I didn't
*  really care about if you didn't have NumPy installed. Anyway, Guido opened up ideas,
*  technologically brilliant. I really got a lot of respect for him when I saw what he did with
*  this type class merger thing. It was actually tricky. And then willing to share his ideas.
*  So the other thing early on in 1998, I said I wrote my first extension module. The reason I
*  could is because he'd written this blog post on how to do reference counting. And without it,
*  I would have been lost. But he was willing to at least try to write this post. And so he's been
*  motivated early on with Python. There's a computer science for everybody. You can have this early on
*  desire to, oh, maybe we should be pushing programming to more people. So he had this
*  populist notion, I guess, or populist sense. So learn that there's a certain skill. I've seen it
*  in other people too, of engaging with contributors sufficiently to, because when somebody engaged
*  with you and wants to contribute to you, if you ignore them, they go away. So building that early
*  contributor base requires real engagement with other people. And he would do that.
*  RG Can you also comment on this tragic
*  stepping down from his position as the benevolent dictator for life over the wars?
*  JS The walrus operator?
*  RG The walrus operator was the last battle. I don't know if that's the cause of it, but
*  there's this for people who don't know, you can look up. There's the walrus operator, which looks
*  like a colon and equal sign. And it actually does maybe the thing that an equal sign should be doing.
*  But historically, equal sign means something else. It just means assignment.
*  So he stepped down over this. What do you think about the pressure of leadership?
*  JS You mentioned the letter I wrote in NumPy at the time. That was a hard time, actually.
*  There's been really hard times. You get criticized, and you get pushed, and you get...
*  Not everybody loves what you do. Anytime you do anything that has impact at all,
*  you're not universally loved. You get some real critics. And that's an important energy,
*  because it's impossible if you did everything right. You need people to be pushing. But sometimes
*  people can get mean. I prefer to give people the benefit of the doubt. I don't immediately assume
*  they have bad intentions. And maybe that doesn't happen for everybody. For whatever reason,
*  their past, their experience with people, they sometimes have bad intentions. So they immediately
*  attribute to you bad intentions. You're like, where did this come from? I'm definitely open
*  to criticism, but I think you're misinterpreting the whole point. Because I would get that. Certainly
*  when I started Anaconda, sometimes I say to people, I care enough about entrepreneurship to make some
*  open source people uncomfortable. And I care enough about open source to make investors
*  uncomfortable. So you create doubters on both sides. And this is just a plea to the listener
*  and the public. I've noticed this too, that there's a tendency, and social media makes this worse,
*  when you don't have perfect information about the situation, you tend to fill the gaps with the
*  worst possible, or at least a bad story that fills those gaps. And I think it's good to live life,
*  maybe not fully naively, but filling in the gaps with the good, with the best, with the positive,
*  with the hopeful explanation of why you see this. So if you see somebody like you trying to make
*  money on a book about NumPy, there's a million stories around that that are positive. And those
*  are good to think about, to project positive intent on other people. Because for many reasons,
*  usually because people are good and they do have good intent. And also when you project that
*  positive intent, people will step up to that too. So it has this kind of viral nature to it. And of
*  course, what Twitter early on figured out on Facebook is that they can make a lot of money
*  in engagement from the negative. And so we're fighting this mechanism, which is challenging.
*  It's easier.
*  It's just easier to be negative. And then for some reason, something in our minds really enjoys
*  sharing that and getting all excited about the negativity.
*  We do. Yeah. But-
*  But some protective mechanism perhaps that we're worried we're going to eat and if we don't.
*  Exactly. For us to be effective as a group of people in the software engineering project,
*  you have to project positive intent, I think.
*  I totally agree. Totally agree. And I think that's very... And so that happens in this space. But
*  Python has done a reasonable job in the past. But here is a situation where I think it's started
*  to get this pressure where it didn't. I really didn't know enough about what happened. I've
*  talked to several people about it. And I know most of the steering committee members today,
*  one person nominated me for that role, but it's the wrong role for me right now.
*  I have a lot of respect for the Python developer space and the Python developers.
*  I also understand the gap between computer science Python developers and array programming
*  developers or science developers. And in fact, Python succeeds in the array space, the more it
*  has people in that boundary. And there's often very few. I was playing a role in that boundary
*  and working like everything to try to keep up with even what Gita was saying. I'm a C programmer,
*  but not a computer scientist. I was an engineer and physicist and mathematician. And I didn't always
*  understand what they were talking about and why they would have opinions the way they did.
*  So you have to listen and try to understand. Then you also have to explain your point of
*  view in a way they can understand. And that takes a lot of work. And that communication
*  is always the challenge. And it's just what we're describing here about the negativity is just
*  another form of that. How do we come together? And it does appear we're wired anyway to at least
*  there's a part of us that will enemy, friend, enemy. And we see, yeah, it's like, why are we
*  wiring on the enemy front? So why are we pushing that? Why are we promoting that so deeply?
*  Let's assume friend until proven otherwise. Yes.
*  So because you have such a fascinating mind and all of this, let me just ask you these questions.
*  So one interesting side on the Python history is the move from Python 2 to Python 3. You mentioned
*  move from Python 1 to Python 2, but the move from Python 2 to Python 3 is a little bit interesting
*  because it took a very long time. It broke in quite a small way backward compatibility,
*  but even that small way seemed to have been very painful for people. Is there a lessons you draw
*  tons of lessons from from how long it took and how painful it seemed to be?
*  Yeah, tons of lessons. Well, I mentioned here earlier that num numpy was written in 2005.
*  It was in 2005 that I actually went to Guido to talk about getting numpy into Python 3. Like my
*  strategy was to, oh, we were moving to Python 3. Let's have that be. And it seems funny in retrospect
*  because like, wait, Python 3, that was in 2020, right? When we finally ended support for Python 2
*  or at least 2017. The reason it took a long time, a lot of time, I think it was because one of the
*  things is there wasn't much to like about Python 3. 3.0, 3.1. It really wasn't until 3.3. Like I
*  consider Python 3.3 to be Python 3.0. It wasn't until Python 3.3 that I felt there was enough
*  stuff in it to make it worth anybody using it. And then 3.4 started to be, oh, yeah, I want that.
*  And then 3.5 as the matrix will play operator. And now it's like, okay, we got to use that.
*  Plus the libraries that started leveraging some of the features of Python 3.
*  Exactly. So it really, the challenge was it was, but it also illustrated a truism that,
*  when you have inertia, when you have a group of people using something,
*  it's really hard to move them away from it. You can't just change the world on them.
*  And Python 3, it made some, I think it fixed some things Guido had always hated. I think he didn't
*  like the fact that print was a statement. He wanted to make it a function. But in some sense,
*  that's a bit of gratuitous change to the language. And you could argue, and there are people who have,
*  but one of the challenges was there wasn't enough features and too many just changes
*  without features. And so that empathy for the end user as to why they would switch wasn't there.
*  I think also it illustrated just the funding realities. Python wasn't funded. It was also
*  a project with a bunch of volunteer labor. It had more people, so more volunteer labor,
*  but it was still, it was funded in the sense that at least Guido had a job. And I've learned some of
*  the behind the scenes on that now since, since talking to people who lived through it and
*  maybe not on air, we can talk about some of that. But it's interesting to see, but Guido had a job,
*  but his full-time job wasn't just work on Python. He had other things to do.
*  It's wild.
*  It is wild, isn't it?
*  It's wild how few people are funded.
*  Yes.
*  And how much impact they have.
*  Maybe that's a feature in our book. I don't know.
*  Maybe, yes, exactly. At least early on. I know.
*  Yeah.
*  It's like Olympic athletes are often severely underfunded, but maybe that's what brings out the
*  greatness.
*  Yes, correct. No, exactly. Maybe this is the essential part of it. Because I do think about
*  that in terms of I currently have an incubator for open source startups. What I'm trying to do right
*  now is create the environment I wished had existed when I was leaving academia with Numpy
*  and trying to figure out what to do. I'm trying to create those opportunities and environments.
*  And that's what drives me still is how do I make the world easier for the open source entrepreneur?
*  Let me say, I mean, I could probably stand Numpy for a long time, but this is a fun question.
*  So, Andrei Kapotty leads the Tesla Autopilot team. And he's also one of the most legit
*  programmers I know. He builds stuff from scratch a lot. And that's how he builds intuition about
*  how a problem works. He just builds it from scratch. And I always love that. And the primary
*  language he uses is Python for the intuition building. But he posted something on Twitter
*  saying that they got a significant improvement on some aspect of their data loading, I think,
*  by switching away from NP dot square root. So the numpy's implementation of square root to math
*  dot square root. And then somebody else commented that you can get even a much greater improvement
*  by using the vanilla Python square root, which is like- Power 0.5.
*  Power 0.5. And it's fascinating to me. I just wanted to-
*  So that was- Absolutely.
*  That was some shade throwing at some- No, no.
*  But also- Yes, we're talking about-
*  It's a good way to ask the trade-off between usability and efficiency broadly in Numpy,
*  but also on these specific weird quirks of a single function.
*  Yep. So on that point, if you use a numpy math function on a scalar, it's going to be slower
*  than using a Python function on that scalar. Because the math object in Numpy is more
*  complicated. Because you can also call that math object on an array. And so effectively,
*  it goes through a similar machine. There aren't enough of the- Which you would do and you could
*  do like checks and fast paths. So yeah, if you're basically doing a list, if you run over a list,
*  in fact, for problems that are less than a thousand, even maybe 10,000 is probably the-
*  If you're going more than 10,000, that's where you definitely need to be using arrays.
*  But if you're less than that, and for reading, if you're doing a reading process and essentially
*  it's not compute bound, it's IO bound. And so you're really taking lists of thousand at a time
*  than doing work on it. Yeah, you could be faster just using Python, straight up Python.
*  See, but also- And then-
*  This is the- Sorry to interrupt, but there's the fundamental questions.
*  When you look at the long arc of history, it's very possible that np.square is much faster.
*  It could be.
*  So in terms of like, don't worry about it. It's the evils of overoptimization or whatever,
*  all the different quotes around that is sometimes obsessing about this particular little
*  quark is not- For somebody like, if you're trying to optimize your path, I mean, I agree,
*  premature optimization creates all kinds of challenges, right? Because now, but you may
*  have to do it. I believe the quote is the root of all evil.
*  It's the root of all evil, right? Let's give Donald Newt, I think, or somebody else.
*  Well, Doc Newt is kind of like Mark Twain. He would just attribute stuff to him.
*  And it's fine because he's brilliant. So no, I was a LaTeX user myself. And so I have a lot of
*  respect and he did more than that, of course. But yeah, someone I really appreciate in the computer
*  science space. Yeah, I think that's appropriate. There's a lot of little things like that where
*  people actually, if you understood it, you go, yeah, of course that's the case. And the other
*  part I didn't mention, and Numba was a thing we wrote early on. And I was really excited by
*  Numba because it's something we wanted. It was a compiler for Python syntax. And I wanted it
*  from the beginning of writing NumPy because of this function question. The power of arrays is
*  really that you can write functions using all of it. It has implicit looping. So you don't worry
*  about, I write this n-dimensional for loop with four loops, four, four statements. You just say,
*  oh, big four-dimensional array. I'm going to do this operation, this plus, this minus, this reduction.
*  And you get this, it's called vectorization in other areas, but you can basically think at a high
*  level and get massive amounts of computation done with the added benefit of, oh, it can be
*  paralyzed easily. It can be put in parallel. You don't have to think about that. In fact,
*  it's worse to go decompose your, you write the four loops and then try to infer parallelism from
*  four loops. So it's actually a harder problem than to take the array problem and just automatically
*  paralyze that problem. That's what, and so functions in NumPy are called universal functions,
*  Ufuncs. So square root is an example of a Ufunc. There are others, sine, cosine, add, subtract.
*  In fact, one of those first libraries to SciPy was something called special, where I added Bessel
*  functions and all these special functions that come up in physics. And I added them as Ufuncs
*  so they could work on arrays. So I understood Ufuncs very, very well from day one inside of
*  numeric. That was one of the things we tried to make better in NumPy was how do they work?
*  Can they do broadcasting? What does broadcasting mean? But one of the problems is, okay, what do
*  I do with a Python scalar? So what happens? The Python scalar gets broadcast to a zero-dimensional
*  array, and then it goes through the whole same machinery as if it were a 10,000-dimensional array.
*  And then it kind of unpacks the element and then does the addition. That's not to mention the
*  function it calls in the case of square root is just the Clib square root. In some cases,
*  Python's power, there's some optimizations they're doing that can be faster than just calling the
*  Clib square root. In the interpreter or in the... No, in the C code, in the Python runtime.
*  In the Python runtime. So they've really optimized it, and they have the freedom to do that because
*  they don't have to worry about... It's just a scalar.
*  It's just a scalar. Right. They don't have to worry about the fact that, oh, this could be an object
*  with many pieces. The Ufunc machine is also generic in the sense that typecasting and
*  broadcasting. Broadcasting's idea of I'm going to go, I have a zero-dimensional array, I have a
*  scalar with a four-dimensional array, and I add them. Oh, I have to kind of coerce the shape of
*  this guy to make it work against the whole four-dimensional array. So it's the idea of I can
*  do a one-dimensional array against a two-dimensional array and have it make sense.
*  Well, that's what NumPy does is it challenges you to reformulate, rethink your problem
*  as a multi-dimensional array problem versus move away from scalars completely.
*  Right. Exactly. Exactly. In fact, that's where some of the edge cases boundaries are is that,
*  well, they're still there, and this is where array scalars are particular. So array scalars
*  are particularly bad in the sense that they were written so that you could optimize the math on
*  them, but that hasn't happened. And so their default is to coerce the array scalar to a
*  zero-dimensional array and then use the NumPy machinery. That's what you could specialize,
*  but it doesn't happen all the time. So in fact, when we first wrote Numba, we'd do comparisons
*  and say, look, it's a thousand X speed up. We were lying a little bit in the sense that, well,
*  first do the 40 X slowdown of using array scalars inside of a loop. Because if you just use Python
*  scalars, you'd already be 10 times faster. But then we would get a hundred times faster over that
*  using just compilation. But what we do is compile the loop from out of the interpreter to machine
*  code. And then that's always been the power of Python is this extensibility so that you can,
*  because people say, oh, Python's so slow. Well, sure, if you do all your logic in the runtime of
*  the Python interpreter, yeah. But the power is that you don't have to. You write all the logic,
*  what you do at the high level is just high level logic. And the actual calls you're making could be
*  on gigabyte arrays of data. And that's all done at compiled speeds. And the fact that integration is,
*  one, can happen, but two, is separable. That's one of the, the language like Julia says,
*  we're going to be all in one. You can do all of it together. And then there's, the jury's out. Is
*  that possible? I tend to think that you're going to, there's separate concerns there. You want to
*  precompile. In fact, generally you will want to precompile some of your loops. Like SciPy is a
*  compilation step. To install SciPy, it takes about two hours. If you have many machines, maybe you
*  can get it down to one hour. But to compile all those libraries takes a while. You don't want to
*  do that at runtime. You don't want to do that all the time. You want to have this precompiled
*  binary available that you're then just linking into. So there's real questions about the whole,
*  you know, source code. Code is, running binary code is more than source code. It's creating object
*  code. It's the linker. It's the loader. It's the, how does that interpret it inside of the virtual
*  memory space? There's a lot of details there that actually I didn't understand for a long time until
*  I, you know, read books on the topic. And it, and it led to, the more you know, the better off you
*  are. And you can do more details, but sometimes it helps with abstractions too. Well, the problem,
*  as we mentioned earlier with abstractions is you kind of sometimes assume that whoever
*  implemented this thing had your case in mind and found the optimal solution. Yes. Or like you assume
*  certain things. I mean, there's a lot of, one of the really powerful things to me early on,
*  I mean, it sounds silly to say, but with Python, probably one of the reasons I fell in love with it
*  is dictionaries. Yes. So obviously probably most languages have some mapping concept, but
*  it felt like it was a first-class citizen and it was just my brain was able to think in dictionaries.
*  But then there is the thing that I guess I still use to this day is order dictionaries,
*  because that seems like a more natural way to construct dictionaries. Yeah. And from a
*  computer science perspective, the running time cost is not that significant, but there's a lot of
*  things to understand about dictionaries that the abstraction kind of doesn't necessarily incentivize
*  you to understand. Right. Do you really understand the notion of a hash map and how the dictionary
*  is implemented? But you're right. Dictionaries are a good example of an abstraction that's powerful.
*  And I agree with you. I agree. I love dictionaries too. It took me a while to understand that once
*  you do, you realize, oh, they're everywhere. And Python uses them everywhere too. Like it's
*  actually constructed that one of the foundational things is dictionaries and it does everything
*  with dictionaries. So it is, it's powerful. Order dictionaries came later, but it is very,
*  very powerful. It took me a little while coming from just the array programming entirely to
*  understand these other objects like dictionaries and lists and tuples and binary trees. Like I
*  said, I wasn't a computer scientist, but I studied arrays first. And so I was very array
*  centric and you realize, oh, these others don't have purposes and value actually. I agree.
*  There's a friendliness about like one way to think about arrays is arrays are just
*  like full of numbers, but to make them accessible to humans and make them less error prone
*  to human users. Sometimes you want to attach names, human interpretable names that are sticky
*  to those arrays. So that's how you start to think about dictionaries is you start to convert
*  numbers into something that's human interpretable. And that's actually the tension I've had with
*  NumPy because I've built so much tooling around human interpretability and also protecting me
*  from a year later, not making the mistakes by being, I wanted to force myself to use English
*  versus numbers. Yes. So there's a, there's a project called label the race, like very early
*  it was recognized that, Oh, we need, we were indexing NumPy, which is numbers, all the columns and
*  particularly the dimensions. I mean, if you have an image, you don't necessarily need to label each
*  column or row, but if you have a lot of images or you have another dimension, you at least like to
*  label the dimension as this is X, this is Y, this is Z, or this is give us some human meaning or
*  some domains of meaning. That was one of the impetuses for pandas actually was just, Oh,
*  we do need to label these things and label label array was an attempt to add that like a lighter
*  weight version of that. And there's been like, that's an example of something I think NumPy could add
*  could be added to NumPy. But one of the challenges again, how do you fund this? Like, like I said,
*  one of the tragedies I think is that I never had the chance to, I was never paid to work on NumPy.
*  Right. So I've always just done in my spare time, always taken from one thing, taken from another
*  thing to do it. And at the time, I mean, today it would be the wrong day. And today, like paying me
*  to work on NumPy now would not be a good use of effort, but, but we are finally at QuantSite labs.
*  I'm actually paying people to work on NumPy and SciPy, which is I'm thrilled with them excited by,
*  I've wanted to do that. That's why I was wanting to do from day one. It just took me a while.
*  To figure out a mechanism to do that. Even like in the university setting, respecting that from
*  like pushing students, young minds, the young graduate students to contribute and then figuring
*  out financial mechanisms that enable them to contribute and then sort of reward them for their
*  innovative scientific journey. That that would be nice. But then also just the better allocation
*  of resources. Well, you know, it's 20 year anniversary since 9-11 and I was just looking,
*  we spent over $6 trillion in the, in the middle East after 9-11 in the various efforts there.
*  And sort of to put politics and all that aside, it's just, you think about the education system,
*  all the other ways we could have possibly allocated that money. To me, to take it back,
*  the amount of impact you would have by allocating a little bit of money to the programmers,
*  that build the tools that run the world is fascinating. I mean, it is, I don't know. I think
*  again, there is some aspect to being broke as somewhat of a feature, not a bug that you make
*  sure that your value. So manage that. Right. No, I know. So, but I don't think that's the
*  big part. So it's like, I think you can, you can have enough money and actually be wealthy
*  while maintaining your values. Agreed. I think agreed. There's an old adage that, you know,
*  nations that trade together, don't go to war together. Yeah. Right. I've often thought about,
*  you know, nations that code together. Yeah. Because one thing I love about open source is it's,
*  it's global. It's multinational. Like there aren't national boundaries. One of the challenge with
*  business and open source is the fact that well, business is national, like businesses or entities
*  that are recognized in legal jurisdictions, right. And have laws that are respected in those
*  jurisdictions and hiring. And yet the open source ecosystem is not, it's not, it's not there. Like
*  currently, one of the problems we're solving is hiring people all over the world, right. Because
*  we, it's a global effort and I've had the chance to work and I've loved the chance. I've never been
*  to like Iran, but I once had a conference where I was able to talk to people there, right. And talk
*  to folks in Pakistan. Never been there, but we had a call where there, and there are people there,
*  like just scientists and normal people. And, you know, and, and it's, there's a, there's a certain
*  amount of humanizing, right. That gets away from the, like we often get the memes of society that
*  bubble up and then get, get discussed, but the memes are not even an accurate reflection of the
*  reality of what people are. Well, if you look at the major power centers that are leading to something
*  like cyber war in the next few decades, it's the United States, it's Russia and China. And those
*  three countries in particular have incredible developers. So if they work together, I think
*  that's one way the politicians can do their stupid bickering, but like the, there's a layer of
*  infrastructure of humanity. If they collaborate together, that, that I think can prevent major,
*  major military conflict, which would, I think most likely happen at the cyber level versus the
*  actual hot war level. You're right. No, I think that's good. That's good prediction. Nations that
*  code together, don't go to war together. That's, that's a hope, right? That's one of the
*  philosophical hopes, but yeah. So you mentioned the project of Numba, which is fascinating. So
*  from the early days, there was kind of a pushback on Python that it's not fast. You know, you see C
*  plus, if you want to write something that's fast, you use C C plus plus. If you want to write
*  something that's usable and friendly, but slow, you use Python. And so what is a number? What is
*  its goal? How does it work? Great. Yeah. Yes. That's what the argument and the reality was people
*  would write high level coding and use compiled code, but there's still user story use cases where
*  you want to write Python, but then have it still be fast. You still need to write a for loop.
*  Like before Numba, it was always don't write a for loop, you know, write it in a vectorized way,
*  you know, put it in an array and often though that can make a memory trade off. Like quite often you
*  can do it, but then you make maybe use more memory because you have to build this array of data.
*  That's you don't necessarily need all the time. So Numba was, it started from a desire to have
*  kind of a vectorized that worked. A vectorized was a tool in NumPy. It was released. You give
*  it a Python function and it gave you a universal function, a U func that would work on arrays.
*  So get a function that just worked on a scalar. Like you could make a, like the classic case was
*  a simple function that an if then statement in it. So sine X over X function, sync function,
*  if X equals zero, return one, otherwise do sine X over X. The challenge is you don't want that loop
*  had one in Python. So you want a compiled version of that. But the U func, the vectorized in NumPy
*  would just give you a Python function. So it would take the array of numbers and at every call do a
*  loop back into Python. So it was very slow. It gave you the appearance of a U func, but it was
*  very slow. So I always wanted a vectorized that would take that Python scalar function and produce
*  a U func working on binary native code. So in fact, I had somebody work on that with PyPy
*  see if PyPy could be used to produce a U func like that early on in 2009 or something like that,
*  2010. They didn't work that well. It was kind of pretty bulky, but in 2012, Peter and I had just
*  started Anaconda. We had, I had just, I had learned to raise money. That's a different topic,
*  but I'd learned to raise money from friends, family and fools, as they say.
*  That's a good line.
*  Oh, that's a good line.
*  But so we're trying to do something. We were trying to change the world. Peter and I are
*  super ambitious. We want to make array computing and we had ideas for really what's still the
*  energy right now. How do you do at scale data science? And we had a bunch of ideas there,
*  but one of them, I had just talked to people about LLVM and I was like, there's a way to do this.
*  I just, I went, I heard about my friend Dave Beasley at a compiler course. So I was looking
*  at compilers like, and I realized, oh, this is what you do. And so I wrote a version
*  of Numba that just basically mapped Python bytecode to LLVM.
*  Nice.
*  Right? So, and the first version is like, this works and it produces code. That's fast. This is
*  cool for, you know, obviously a reduced subset of Python. I didn't support all the Python language.
*  There had been efforts to speed up Python in the past, but those efforts were, I would say,
*  not from the array computing perspective, not from the perspective of wanting to produce a
*  vectorize improvement. They were from a perspective of speeding up the runtime of Python,
*  which is fundamentally hard because Python allows for some constructs that aren't,
*  you can't speed up. Like it's this generic, you know, when it does this variable.
*  So I, from the start did not try to replicate Python's semantics entirely. I said, I'm going
*  to take a subset of the Python syntax and let people write syntax in Python, but it's kind of
*  a new language really.
*  So it's almost like four loops, like focusing on four loops.
*  Four loops, scalar arithmetic, you know, typed, you know, really typed language, a type subset.
*  That was the key. So, but we wanted to add inference of types. So you didn't have to spell
*  all the types out because when you call a function, so Python is typed, it's just dynamically typed.
*  So you don't tell it what the types are, but when it runs, every time an object runs,
*  there's a type for the variables. You know what it is. And so that was the design goals of Numba
*  were to make it possible to write functions that could be compiled and have them use for
*  NumPy arrays, like the need to support NumPy arrays.
*  And so how does it work? Do you add a comment within Python that tells it to do, like how do
*  you help out the compiler?
*  Yeah. So there isn't much actually. You don't, it's kind of magical in the sense that it just
*  looks at the type of the objects and then does type inference to determine any other
*  variables it needs. And then it was also because we had a use case that could work early,
*  like one of the challenges of any kind of new development is if you have something that to make
*  it work, it was going to take you a long time. It's really hard to get out off the ground.
*  If you have a project where there's some incremental story, it can start working today
*  and solve a problem. Then you can start getting it out there, getting feedback because Numba today,
*  Numba is nine years old today. The first two, three versions were not great, but they solved
*  a problem and so people could try it and we could get some feedback on it.
*  Not great. And it was very focused.
*  Very fragile, very subset. The subset it would actually compile was small. And so if you wrote
*  Python code and said, so the way it worked is you write a function and you say at JIT,
*  use decorators. So decorators, just these little constructs, let you decorate code with an app and
*  then the name. The app JIT would take your Python function and actually just compile it and replace
*  the Python function with another function that interacts with this compiled function.
*  And it would just do that. And we went from Python byte code, then we went to AST. I mean,
*  writing compilers actually, I learned a lot about why computer science is taught the way it is
*  because compilers can be hard to write. They use tree structures, they use all the concepts of
*  computer science that are needed. And it's actually hard to, it's easy to write a compiler
*  and then have it be spaghetti code. Like the passes become challenging and we ended up with
*  three versions of Numba, right? Numba got written three times.
*  What programming language is Numba written in?
*  Python.
*  Wait, okay.
*  Yeah, Python. So.
*  Really?
*  Yeah.
*  That's fascinating.
*  Yeah. So Python, but then the whole goal of Numba is to translate Python byte code
*  to LLVM. And so LLVM actually does the code generation. In fact, a lot of times they'd say,
*  yeah, it's super easy to write a compiler if you're not writing the parser nor the code generator.
*  Right.
*  So for people who don't know, LLVM is a compiler itself. So you're compiling.
*  Yeah. It's really badly named low level virtual machine, which that part of it is not used. It's
*  really low level.
*  Chris, he doesn't mean that.
*  Yeah. Love Chris. But the name makes you imply that the virtual machine is what it's all about.
*  It's actually the IR and the library that the code generation is. That's the real beauty of it.
*  The fact that what I love about LLVM was the fact that it was a plateau you could collaborate on,
*  right? Instead of the internals of GCC or the internals of the Intel compiler,
*  like how do I extend that? And here's a place we could collaborate. And we were early. I mean,
*  people had started before. It's a slow compiler. Like it's not a fast compiler. So for some kind
*  of JITs, like JITs are common in the language because one, every browser has a JavaScript JIT.
*  It does real time compilation of the JavaScript to machine code.
*  For people who don't know, JIT is just in time compilation.
*  Thank you. Yeah. Just in time compilation. They're actually really sophisticated. In fact,
*  I got jealous of how much effort was put into the JavaScript JITs.
*  Yes. Well, it's kind of incredible what they've done with JavaScript JITs.
*  I completely agree. I'm very impressed. But, you know, number one, it was an effort to make
*  that happen with Python. And so we used some of the money raised from Anaconda to do it.
*  And then we also applied for this DARPA grant and used some of that money to continue the development.
*  And then we used proceeds from service projects we would do. We get consulting projects that we
*  would then use some of the profits to invest in Numba. So we ended up with a team of two or three
*  people working on Numba. It was a fits and starts, right? And ultimately the fact that we had a
*  commercial version of it also we were writing. So part of the way I was trying to fund Numba is say,
*  well, let's do the free Numba and then we'll have a commercial version of Numba called Numba Pro.
*  And what Numba Pro did is it targeted GPUs. So we had the very first CUDA JIT and the very first
*  At-JIT compiler that in 2012 for 2013, you could run not just a U-FUNC on CPU, but a U-FUNC on GPUs.
*  And it would automatically paralyze it and get 1000x speed ups.
*  That's an interesting funding mechanism because large companies or larger companies care about
*  speed in just this way. So it's exactly a really good way.
*  Yeah. There's been a couple of things you know people will pay for. One, they'll pay for really
*  good user interfaces. And so I'm always looking for what are the things people will pay for that
*  you could actually adapt to the open source infrastructure. One is definitely user interfaces.
*  The second is speed. Like a better runtime, faster runtime.
*  And then when you say people, you mean like a small number of people pay a lot of money,
*  but then there's also this other mechanism that a ton of people pay a little bit.
*  First, we mentioned Anaconda, we mentioned friends, family and fools.
*  So Anaconda is yet another. So there's a company, but there's also a project
*  that is exceptionally impactful in terms of for many reasons, but one of which is bringing
*  a lot more people into the community of folks who use Python. So what is Anaconda?
*  What is its goals? Maybe what is Conda versus Anaconda?
*  Yeah, I'll tell you a little bit of the history of that because Anaconda, we wanted to do,
*  we wanted to scale Python because we, you know, that was the goal. Peter and I had the goal of
*  when we started Anaconda, we actually started as Continuum Analytics was the name of the company
*  that started. It got renamed Anaconda in 2015. But we said we want to scale analytics. NumPy is great,
*  Pandas is emerging, but these need to run at scale with lots of machines. The other thing we wanted
*  to do was make user interfaces that were web. We wanted to make sure the web did not pass by the
*  Python community, that we had ways to translate your data science to the web. So those are the
*  two kind of technical areas. We thought, oh, we'll build products in this space. And that was the
*  idea. Very quickly in, but of course, the thing I knew how to do was to do consulting to make money
*  and to make sure my family and friends and fools that had invested didn't lose their money.
*  So it's a little different than if you take money from a venture fund. If you take money
*  from a venture fund, the venture fund, they want you to go big or go home. They're kind of like
*  expecting 9 out of 10 to fail or 99 out of 100 to fail. It's different. I was at a barbell strategy.
*  I was like, I can't fail. I mean, I may not do super well, but I cannot lose their money.
*  So I'm going to do something I know can return a profit, but I want to have exposure to an upside.
*  So that's what happened in Anaconda. There was lots of things we did not well in terms of that
*  structure and I've learned from since to have it better. But we did a really good job of kind
*  of attracting the interest around the area to get good people working and then get funnel some
*  money on some interesting projects. Super excited about what came out of our energy there, like a lot
*  did. So what are some of the interesting projects? So Dask, Numba, Bokeh, Conda. There was a data
*  shader, panel, HoloViz. These are all tools that are extremely relevant in terms of helping you
*  build applications, build tools, build faster code. There's a couple I'm forgetting. So Bokeh is a plotting.
*  Jupiter Lab. Jupiter Lab came out of this too. Fascinating. Okay. So Bokeh does plotting.
*  Bokeh does plotting. So Bokeh was one of the foundational things to say, I want to do plot
*  in Python, but have the things show up in a web. Right. That's right. That's right. That's right.
*  Plotting to me still, with all due respect to Matplotlib and Bokeh, it feels like still an unsolved
*  problem. Oh, it is. It's a big problem. Right. Because you're, I mean, I don't know.
*  Visualization broadly. Yes. I think we've got a pretty good API story around certain use cases
*  of plotting. But there's a difference between static plots versus interactive plots versus
*  I'm an end user. I just want to write a simple, Panda started the idea of here's a data frame.
*  I'm going to adopt plot. I'm just going to attach plot as a method to my object, which was a little
*  bit controversial, right? But works pretty well actually, because there's a lot less you have to
*  pass in, right? You can just say, here's my object. You know what you are. You tell the
*  visualization what to do. So that, and there's things like that that have not been, you know,
*  super well developed entirely, but Bokeh was focused on interactive plotting. So you could,
*  it's a short path between interactive plotting and application, dashboard application. And there's
*  some incredible work that got done there. Right. And it was a hard project because then you're
*  basically doing JavaScript and Python. So we wanted to tackle some of these hard problems and
*  just go after them. We got some DARPA funding to help and it was super helpful. It's a funny story
*  there. We actually did two DARPA proposals, but one we were five minutes late for, and DARPA has
*  a very strict cutoff window. And so we had two proposals, one for the Bokeh and one for actually
*  Numba and the other work. Which one were you late for? The foundation on the miracle work.
*  So Bokeh got funded. Fortunately, Chris let us use some of the money to fund still some of the
*  other foundational work, but it wasn't as, yeah, he, his hands were tired. He couldn't do anything
*  about it. That was a whole interesting story. So one of the incredible projects that you worked on
*  is Conda. Yes. So what is Conda? Yeah, Conda, it was early on, like I said, with SciPy. SciPy was
*  a distribution, masquerade, and library. And you heard me talking about compiler issues and trying
*  to get the stuff shipped and the fact that people can use your libraries if they have it.
*  So for a long time, we'd understood the packaging problem in Python. And one of the first things you
*  did at Continental Analytics became Anaconda was organize the Pi data ecosystem in conjunction
*  with NumFocus. We actually started NumFocus with some other folks in the community the same year
*  we started Anaconda. I said, we're going to build a corporation, but we're also going to reify the
*  community aspect and build a nonprofit. So we did both of those. Can we pause real quick and
*  can you say what is PyPy, the Python package index, like this whole story of packaging in Python?
*  Yeah, that's what I'm going to get to, actually. This is exactly the journey I'm on. It's to sort
*  of explain packaging in Python. I think it's best expressed through the conversation I had with Gito
*  at a conference where I said, so, you know, packaging is kind of a problem. And Gito said,
*  I don't ever care about packaging. I don't use it. I don't install new libraries. I'm like,
*  I guess if you're the language creator and if you need something, you just put it in the distribution.
*  Maybe you don't worry about packaging. But Gito has never really cared about packaging,
*  right? And never really cared about the problem of distribution, somebody else's problem. And
*  that's a fair position to take, I think, as a language creator. In fact, there's a philosophical
*  question about should you have different development packaging managers? Should you have a package
*  manager per language? Is that really the right approach? I think there are some answers of,
*  it is appropriate to have development tools. And there's an aspect of development tool that is
*  related to packaging. And every language should have some story there to help their developers
*  create. So you should have language specific development tools that relate to package
*  managers. But then there's a very specific user story around package management that those
*  language specific package managers have to interact with and currently aren't doing a good job of that.
*  That was one of the challenges that not seeing that difference and still exists in the difference
*  today. Conda always was a user. I'm going to use Python to do data science. I'm going to use
*  Python to do something. How do I get this installed? It was always focused on that.
*  So it didn't have like a develop, you know, classic example is pip has a pip develop. It's
*  like, I want to install this into my current development environment today. Now,
*  Conda doesn't have that concept because it's not part of the story.
*  For people who don't know pip is a Python specific packaging manager. That's exceptionally popular.
*  That's probably like the default thing you learn. It's the default user. Yeah. And so the story
*  there emerged because what happened is in 2012, we had this meeting at the Google Googleplex and
*  Guido was there to come talk about what we're going to do, how we're going to make things work
*  better. And Wes McKinney, me, Peter, Peter has a great photo of me talking to Guido and he
*  pretends we're talking about this story. Maybe we were, maybe we weren't, but we did at that
*  meeting talk about it and ask Guido, Guido, what we need to fix packaging in Python. Like people
*  can't get the stuff. And he said, go fix it yourself. I don't think we're going to do it.
*  All right. The origin story right there. All right. You said, okay, you said to do this ourselves. So
*  at the same time, people did start to work on the packaging story in Python. It just took a little
*  longer. So in 2012, kind of motivated by our training courses we were teaching, like how do
*  very similar to what you just mentioned about your mother. Like it was motivated by the same
*  purpose. Like, how do we get this into people's hands? And it's this big, long process. It takes
*  too expensive. It was actually hurting NumPy development because I would hear people were
*  saying, don't make that change to NumPy because I just spent a week getting my Python environment.
*  And if you change, if you change NumPy, I have to reinstall everything and reinstalling such a pain.
*  Don't do it. I'm like, wait, okay. So now we're not making changes to a library because of the
*  installation problem that it'll cause for end users. Okay. There's a problem with pack. There's
*  a problem with installation. We've got to fix this. So we said, we're going to make a distribution
*  of Python. And we'd previously done that at M thought. I wanted to make one that would give
*  away for free. Everyone could just get it. Like that was critical that we could just get it.
*  It wasn't tied to a product. It was just, you could get it. And then we had constantly thought
*  about, well, do we just leverage RPM? But the challenge had always been we want a package
*  manager that works on Windows, Mac OS 10 and Linux the same. Right. And it wasn't there. Like you
*  don't have anything like that. You have for people who don't know RPM is red hats.
*  Operating system specific package. Correct. It's an operating specific. Yes. So do you create the
*  design? Question is, do you create an umbrella package manager that cross operating system?
*  Yes, that was the decision. And a neighboring design question is, do you also create a package
*  manager that spans multiple programming languages? Exactly. That was the world we faced. And we
*  decided to go multiple operating systems, multiple and programming language independent,
*  because even Python and particularly what was important was SciPy has a bunch of 4chan in it.
*  Right. And scikit-learn has links to a bunch of C++. There's a lot of compiled code and the
*  Python package managers, especially early on, didn't even support that. So in 2000, so we
*  released Anaconda, which was just a distribution of libraries, but we started to work on Conda in
*  2012. First version of Conda came out in early 2013, summer of 2013. And it was a package
*  manager. So you could say Conda install scikit-learn. In fact, scikit-learn was a fantastic project
*  that emerged. It was the classic example of the scikits. I talked to you earlier about SciPy being
*  too big to be a single library. Well, what the community had done is said, let's make scikits.
*  And there's scikit-image, there's scikit-learn, there's a lot of scikits. And it was a fantastic
*  move that the community did. I didn't do it. I was like, okay, that's a good idea. I didn't like
*  the name. I didn't like the fact you type scikit-image. I was like, that's gotta be simpler.
*  Sklearn, we gotta make that smaller. I like typing all this stuff from imports. So I was kind of a
*  pressure that way, but I love the energy and love the fact that they went out and they did it and
*  DOS people, Jared Millman, and then of course, Gaelle, and there's people I'm not even naming.
*  Scikit-learn really emerged as fantastic project. And the documentation around that is also
*  incredible. And the fact that it was incredible. Exactly. I don't know who did that, but they did
*  a great job. A lot of people in INRIA, a lot of people, a lot of European contributors.
*  There's some Andreas in the US. There's a lot of just people I just adore. I think they're amazing
*  people. Awesome use of SciPy. I love the fact that they were using SciPy. Effectively,
*  they do something I love, which is machine learning. But couldn't install it.
*  Because there's so many pieces involved. So many dependencies. So our use case of Conda was Conda
*  install Scikit-learn. And it was the best way to install Scikit-learn in 2013 to really 2018,
*  17, 18. PIP finally caught up. I still think it's you should Conda install Scikit-learn,
*  before the PIP install Scikit-learn, but you can PIP install Scikit-learn. The issue is the package
*  they created was wheels and PIP does not handle the multi-vendor approach. They don't handle the
*  fact that you have C++ libraries you're depending on. They just stop at the Python boundary. And so
*  what you have to do in the wheel world is you have to vendor. You have to take all the binary
*  and vendor it. Now if your change happens in underlying dependency, you have to redo the whole
*  wheel. So TensorFlow is a good example of a, you should not PIP install TensorFlow. It's a terrible
*  idea. People do it because the popularity of PIP, many people think, oh, of course that's how I
*  install everything in Python. Yeah, this is one of the big challenges. You take a GitHub repository,
*  or just a basic blog post. The number of times PIP is mentioned over Conda is like 100 X to one.
*  Correct. So it just has to do with the- That was increasing. It wasn't true early because PIP
*  didn't exist. Conda came first. But that's like the long tail of the internet documentation
*  user generated. So that you think, how do I install, you Google, how do I install TensorFlow?
*  You're just not going to see Conda in that first page. You won't. That's not correct. Exactly.
*  Not today. You would have in 2016, 2017. And it's sad because you saw the,
*  Conda solves a lot of usability issues. Correct. Especially super challenging things. I don't know.
*  One of the big pain points for me was just on the computer vision side, OpenCV installation.
*  Perfect example. I think Conda, I don't know if Conda has solved that one. Conda has an OpenCV
*  package. I don't know. I certainly know PIP has not solved. I mean, there's complexities there
*  because- Right. I actually don't know. I should probably know a good answer for this. But if you
*  compile OpenCV with certain dependencies, you'll be able to do certain things. So there's this
*  flexibility of what options you compile with. And I don't think it's trivial to do that
*  with Conda or- So Conda has a notion of variance of a package. You can actually have different
*  compilation versions of a package. So not just the version is different, but, oh, this is compiled
*  with these optimizations on it. So Conda does have an answer. As with flavors? As flavors, basically.
*  Well, PIP, as far as I know, does not have flavors. No. PIP generally hasn't thought deeply about the
*  binary dependency problem. And that's why fundamentally it doesn't work for the SciPy ecosystem.
*  It barely- You can sort of paper over it and duct tape it and it kind of works until it doesn't and
*  it falls apart entirely. So it's been a mixed bag. And I've been having lots of conversations
*  with people over the years because, again, it's an area where if you understand some things,
*  but not all the things, but they've done a great job of community appeal. This is an area where
*  I think Anaconda as a company needed to do some things in order to make Conda more community
*  centric. And I talk about this all the time. There's a balance between every project starts
*  with what I call company backed open source. Even if the company is yourself, it's just one person
*  doing business as. But ultimately for projects to succeed virally and become massive influencers,
*  they have to get community people on board. They have to get other people on board.
*  So it has to become community driven. And a big part of that is engagement with those people,
*  empowering people, governance around it. And what happened with Conda in the early days,
*  PIP emerged and we did do some good things. Conda Forge, the Conda Forge community is sort of the
*  community recipe creation community. But Conda itself, I still believe, and Peter is CEO of
*  Anaconda, he's my co-founder. I ran Anaconda until 2017, 2018. Peter's still Anaconda. And we're
*  still great friends. We talk all the time. I love him to death. There's a long story there about
*  why and how we can cover in some other podcasts perhaps. Maybe a more business focused one. But
*  there's one area where I think Conda should be more community driven. He should be pushing
*  more to get more community contributors to Conda and let the... Anaconda shouldn't be fighting this
*  battle. It's really a developers. Like you said, help the developers and then they'll actually
*  move us the right direction. That was the problem I have is many of the cool kids I know don't use
*  Conda. And that to me is confusing. It is confusing. It's really a matter of... Conda has some
*  challenges. First of all, Conda still needs to be improved. There's lots of improvements to be made.
*  And it's that aspect of wait, who's doing this? And the fact that then the PIPA really stepped up.
*  They were not solving the problem at all. And now they kind of got to where they're solving it
*  for the most part. And then effectively you could get... Conda solved a problem that was there and
*  it still does. And there's still great things it can do. And we still use it all the time at
*  QuantSight and with other clients. But you can kind of do similar things with PIP and Docker.
*  Especially with the web development community, that part of it again is there's a lot of
*  different kind of developers in the Python ecosystem. And there's still a lack of some
*  clear understanding. I go to the Python conference all the time and there's only a few people in the
*  PIPA who get it. And then others who are just massively trumpeting the power of PIP,
*  but just do not understand the problem. Yeah. So one of the obvious things to me from a mom,
*  from a non-programmer perspective is the across operating system usability. That's much more
*  natural. So they use Windows and it seems much easier to recommend Conda there. But then you
*  should also recommend it across the board. So I'll definitely sort of... But what I recommend now is
*  a hybrid. I do. I mean, I have no problem with PIP. Is it possible to use... Oh, it is. It is.
*  What I... Build the environment with PIP with Conda. Build an environment with Conda. And then PIP
*  install on top of that. That's fine. Be careful about PIP installing OpenCV or TensorFlow or...
*  Because if somebody's allowed that, it's going to be most surely done in a way that can't be
*  updated that easily. So install the big packages, the infrastructure with Conda, and then the weirdos,
*  that like the weird like implementation for some... I had a... There's a cool library I used
*  that based on your location and time of day and date tells you the exact position of the sun
*  relative to the earth. And it's just like a simple library, but it's very precise. And I was like,
*  all right. But that was... And it's PIP. Well, the thing they did really well is
*  Python developers who want to get their stuff published, you have to have a PIP recipe.
*  Right? I mean, even if it's... The challenge is... And there's a key thing that needs to be added
*  to PIP. Just simply add to PIP the ability to defer to a system package manager. Because
*  recognize you're not going to solve all the dependency problem. So give up and allow a
*  system package to work. That way, and a conda is installed and it has PIP, it would default to
*  conda to install this stuff. But Red Hat RPM would default to RPM to install some more things.
*  Like that's a key, not difficult, but somewhat work. Some work feature needs to be added. That's
*  an example of something like... I've known we need to do it. I mean, it's where I wish I had more
*  money. I wish I was more successful in the business side. Trying to get there, but I wish my family,
*  friends and fool community that I know- Was larger.
*  Was larger and had more money. Because I know tons of things to do effectively with more resources.
*  But I have not yet been successful at channel. Tons of it. Some. I'm happy with what we've done.
*  We've created again at QuantSite what we created to get Anaconda started. We created community
*  analytics to get Anaconda started. Done it again with QuantSite. Super excited by that.
*  By the way- It took three years to do it.
*  What is QuantSite? What is its mission? We've talked a few times about different fascinating
*  aspects of it, but it's like big picture. What is QuantSite?
*  Big picture QuantSite. QuantSite is its mission is to connect data to an open economy. So it's
*  basically consulting of the Pydata ecosystem. It's a consulting company. And what I've said
*  when I started it was we're trying to create products, people and technology. So it's divided
*  into two groups. And a third one as well, the two groups are a consulting services company that just
*  helps people do data science and data engineering and data management better and more efficiently.
*  Like full stack, full thing. Full stack, full thing.
*  We'll help you build a infrastructure if you're using Jupiter. We do staff orientation,
*  need more programmers, help you use DAS more effectively, help you use GPUs more effectively.
*  Just basically a lot of people need help. So we do training as well to help people
*  both immediate help and then get learned from somebody. We've added a bunch of stuff too. We
*  kind of separated some of these other things into another company called OpenTeams that we
*  currently started. One of the things I loved about what we did at Anaconda was creating a
*  community innovation team. And so I wanted to replicate that. This time we did a lot of
*  innovation at Anaconda. I wanted to do innovation, but also contribute to the projects that existed.
*  Like create a place where maintainers, so the SciPy and NumPy and all these projects we already
*  started can pay people to work on them and keep them going. So that's Labs. QuantSight Labs is a
*  separate organization. It's a nonprofit mission. The profits of QuantSight help fund it. In fact,
*  every project that we have at QuantSight, a portion of the money goes directly to QuantSight
*  Labs to help keep it funded. So we've gotten several mechanisms to keep QuantSight Labs funded.
*  I'm really excited about Labs because it's been a mission for a long time.
*  What kind of projects are within Labs?
*  So Labs is working to make the software better, like make NumPy better, make SciPy better. It
*  only works on open source. So companies do, we have a thing called a community work order,
*  we call it. If a company says, I want to make Spyder better. Okay, cool. You can pay for a month
*  of a developer of Spyder or a developer of NumPy or a developer of SciPy. You can't tell them what
*  you want them to do. You can give them your priorities and things you wish existed and they'll
*  work on those priorities with the community to get what the community wants and what emerges
*  is what the community wants.
*  Is there some aspect on the consulting side that is helping as we were talking about morphology
*  and so on. Is there specific applications that are particularly like driving, sort of inspiring
*  the need for updates to SciPy?
*  Correct. Absolutely. Absolutely. GPUs are absolutely one of them. A new hardware beyond GPUs. I mean,
*  Tesla's Dojo chip. I'm hoping we'll have a chance to work on that perhaps. Things like that are
*  definitely driving it. The other thing is driving is scalable, like speed and scale. How do I write
*  NumPy code or NumPy Lite code if I want it to run across a cluster? You know, that's Dask or maybe
*  it's Ray. I mean, there's sort of ways to do that now or there's Moden and there's so Pandas code,
*  NumPy code, SciPy code, Scikit-learn code that I want to scale. So that's one big area.
*  Have you gotten a chance to chat with Andre and Elon about because like-
*  No, I would love to by the way. I have not, but I'd love to. I just saw their Tesla AI days video.
*  Super exciting.
*  So this one of the, you know, I love great engineering, software engineering teams and
*  engineering teams in general, and they're doing a lot of incredible stuff with Python. They're like
*  revolutionizing so many aspects of the machine learning pipeline that's operating in the real
*  world. And so much of that is Python. Like you said, the guy running, you know, Andre Kapathi,
*  running Autopilot is tweeting about optimization of NumPy versus-
*  I would love to talk to them. In fact, we have at QuantSight, we've been fortunate enough to work
*  with Facebook on PyTorch directly. So we have about 13 developers at QuantSight. Some of them are in
*  labs working directly on PyTorch. So basically when we started QuantSight, I went to both
*  TensorFlow and PyTorch and said, hey, I want to help connect what you're doing to the broader
*  sci-fi ecosystem because I see what you're doing. We have this bigger mission. We want to make sure
*  we don't lose energy here. And Facebook responded really positively and I didn't get the same
*  reaction. Not yet. I love the folks at TensorFlow. I really love the folks at TensorFlow too. They're
*  fantastic. I think it's just how it integrates with their business. I mean, like I said, there's
*  a lot of reasons. Just the timing, the integration with their business, what they're looking for.
*  They're probably looking for more users and I was looking to kind of
*  cut some development effort and they couldn't receive that as easily, I think.
*  So I'm hoping, I'm really hopeful and love the people there.
*  What's the idea behind OpenTeams?
*  So OpenTeams, I'm super excited about OpenTeams because it's one of the-
*  I mentioned my idea for investing directly in open source. So that's a concept called
*  FeroSS. But one of the things when we started QuantSight, we knew we would do
*  is we develop products and ideas and new companies might come out.
*  At Anaconda, this was clear. At Anaconda, we did so much innovation that like five or six companies
*  could have come out of that. And we just didn't structure it so they could. But in fact, they
*  have. You look at Dask, there's two companies coming out of Dask. Bokeh could be a company.
*  There's like lots of companies that could exist off the work we did there.
*  And so I thought, oh, here's a recipe for an incubation, a concept that we could actually
*  spawn new companies and new innovations. And then the idea has always been, well,
*  money they earn should come back to fund the open source project. So labs is, I think there
*  should be a lot of things like QuantSight labs. I think this concept is one that scales. You can
*  have a lot of open source research labs. Along the way, so in 2018, when the bigger idea came,
*  how to make open source investable, I said, oh, I need to create a venture fund. So we created a
*  venture fund called QuantSight Initiate at the same time. It's an angel fund, really. We started
*  to learn that process. How do we actually do this? How do we get LPs? How do we actually go in this
*  direction and build a fund? And I'm like, every venture fund should have an associated open
*  source research lab, which is no reason. Like our venture fund, the carried interest, a portion of
*  it goes to the lab. It directly will fund the lab. That's fascinating, brother. So you use the power
*  of the organic formation of teams in the open source community and then naturally that leads
*  to a business that can make money. It always maintains and loops back to the open source.
*  Loops back to open source. Exactly. And to me, it's a natural fit. There's something, there's
*  absolutely a repeatable pattern there. And it's also beneficial because, oh, I have natural
*  connections to the open source. If I have an open source research lab, they'll all be out there
*  talking to people. And so we've had a chance to talk to a lot of early stage companies and
*  our fund focused on the early stage. So QuantSight has the services, the lab, the fund. In that
*  process, a lot of stuff started to happen. We started to do recruiting and support and training.
*  And I was starting to build a bigger sales team and marketing team and people besides just
*  developers. And one of the challenges with that is you end up with different cultural aspects.
*  Developers, in any company you go to, you can kind of go, look, is this a business led company,
*  a developer led company? Do they kind of coexist? What's the interface between them? There's always
*  a bit of a tension there, like we were talking about before. What is the tension there? With
*  OpenTeams, I thought, wait a minute, we can actually just create this concept of QuantSight
*  plus labs. While it's specific to the Pi data ecosystem, the concept is general for all open
*  source. So OpenTeams emerges as, oh, we can create a business development company for
*  many, many QuantSights, like thousands of QuantSights. And it can be a marketplace to connect,
*  essentially be the enterprise software company of the future. If you look at what enterprise software
*  wants from the customer side, and during this journey, I've had the chance to work and
*  sell to lots of companies, Exxon and Shell and JV Morgan Bank of America, like the Fortune 100,
*  and talk to a lot of people in procurement and see what are they buying and why are they buying.
*  So I don't know everything, but I've learned a lot about, oh, what are they really looking for?
*  And they're looking for solutions. They're constantly given products from enterprise
*  software. Here's open source, lead enterprise software, now I buy it. And then they have to
*  stitch it together into a solution. Open source is fantastic for gluing those solutions together.
*  So whereas they keep getting new platforms they're trying to buy, what most enterprises want is
*  tools that they can customize that are as inexpensive as they can.
*  Yeah. And so you always want to maintain the connection to the open source because that's
*  Yeah. So open teams is about solving enterprise software problems.
*  Brilliant. Brilliant idea, by the way.
*  With a connect, but we do it honoring the topology. We don't hire all the people. We are a
*  network connecting the sales energy and the procurement energy. And we were on the business
*  side, get the deals closed, and then have a network of partners like QuantSight and others
*  who we hand the deals to, to actually do the work. And then we have to maintain, I feel like
*  we have to maintain some level of quality control so that the client can rely on open teams to
*  ensure their delivery. It's not just, here's a lead, go figure that out. But no, we're going
*  to make sure you get what you need. Yeah. By the way, it's such a skill and I don't know if I have
*  the patience. Does everyone have the patience to talk to the business people or more specific?
*  I mean, there's all kinds of flavors of business people or like marketing people.
*  There's a challenge. I hear what you're saying because I've had the same challenge.
*  Yeah. And it's true. There's sometimes you think, okay, this is way overwrought.
*  Yeah. So you have to become an adult. You have to, because the companies have needs. They have
*  ways to make money and they also want to learn and grow. And yet it's your job to kind of educate
*  them in the best way, like the value of open source, for example. Right. And I'm really grateful
*  for all my experiences over the past 14 years, understanding that side of it and still learning,
*  for sure. But not just understanding from companies, but also dealing with marketing
*  professionals and sales professionals and people that make a career out of that and understanding
*  what they're thinking about and also understanding, well, let's make this better. We can really make
*  a place, open teams I see as the transmission layer between companies and open source communities
*  producing enterprise software solutions. Eventually we want to, today we're taking on SAS and MATLAB
*  and tools that we know we can replace for folks. Really, anytime you have a software tool at
*  organization where you have to do a lot of customization and make it work for you,
*  it's not, you're just buying this thing off the shelf and it works. It's like, okay, you buy this
*  system and you customize a lot, usually with expensive consultants to actually make it work
*  for you. All of those should be replaced by open source foundations with the same.
*  You're doing such important work, such important work in these giant organizations. They're doing
*  exactly that. Taking some proprietary software and hiring a huge team of consultants that
*  customize it and then that whole thing gets outdated quick. That's brilliant. One solution
*  to that is kind of what Tesla is doing a little bit of, which is basically build up a software
*  engineering team. Build a team from scratch. Build a team from scratch. If companies are doing it
*  well, that's what they're doing right now. Exactly. That's okay. You're creating a topology
*  for some of that. You just don't have to do it. That's not the only answer. Other companies can
*  access this, maybe more accessible. Let's really, really say Open Team is the future of enterprise
*  software. We're still early. This idea just percolated over the past year as we've grown
*  quonsight and realized the extensibility of it. We just finished in our seed round to help get
*  more salespeople and then push the messaging correctly. There's lots of tools we're building
*  to make this easier. We want to automate the processes. We feel like a lot of the power is
*  the efficiency of the sales process. There's a lot of wasted energy in small teams and the sales
*  energy to get into large companies and make a deal. There's a lot of money spent on that.
*  Creating the tools and processes for that sales. Make that super seamless so a single company can
*  go, oh, I've got my contract with Open Teams. We've got a subscription they can get. They can
*  make that procurement seamless. Then the fact they have access to the entire open source ecosystem.
*  We have a part of our work that's embracing open source ecosystems and making sure we're
*  doing things useful for them. We're serving them. Then companies making sure they're getting
*  solutions they care about. Then figuring out which targets we have. We're not taking on
*  all of enterprise software yet. But we're definitely set.
*  This feels like the future. The idea and the vision is brilliant. Can I ask you,
*  why do you think Microsoft bought GitHub and what do you think is the future of GitHub?
*  I thought it was a brilliant move. I think they did because Microsoft has always had a
*  developer-centric culture. They always have. One of the things Microsoft's always done well is
*  understand their power as developers. Ballmer didn't necessarily make a good meme about how
*  he approached that. They're broadening that. I think that's why. Because they recognize GitHub
*  is where developers are at. Do they have a vision like Open Teams type of situation?
*  I don't think so yet.
*  Are they just basically throwing money at developers to show their support?
*  I think so.
*  Without a topology like you put it. A way to leverage that. To give developers actual money.
*  I don't think so. I think they're still an enterprise software company. They make a bunch
*  of money. They make a bunch of games. They're a big company. They sell products. I think part of
*  it is they know there's opportunity to make money from GitHub. There's definitely a business there
*  to sell to developers or to sell to people using development. I think there's part of that. I think
*  part of it is also they had definitely wanted to recognize that you need to value open source to
*  get great developers. Which is an important concept that was emerging over the past 10 years.
*  We were able to convince JP Morgan to support PyData because of that fact. That was where the
*  money for them putting a couple hundred thousand into supporting PyData for several conferences
*  was they want developers. They realized that developers want to participate in open source.
*  Enterprise software folks don't always understand how their software gets used.
*  Having spent a lot of time on the floors at JP Morgan at InShell, at ExxonMobil, you see,
*  oh, these companies have large development teams. Then they're dealing with what's being
*  delivered to them. I really feel a privilege that I had a chance to learn some of these people and
*  see what they're doing and even work alongside them as a consultant using open source and
*  trying to figure out how do we make this work instead of our large organization.
*  Well, some of it is actually for a large organization, some of it is messaging to
*  the world that you care about developers and you're the cool, you care. For example,
*  if Ford, because I talked to them, the car companies, they want to attract, you want to
*  take on Tesla and autopilot. You want to take that, right? What do you do there? You show that
*  you're cool. You try to show off that you care about developers and they have a lot of trouble
*  doing that. One way, I think Ford should have bought GitHub. Just to show off these old school
*  companies and it's in a lot of different industries, there's probably different ways.
*  It's probably an art to show that you care to developers and the developers,
*  for example, just spitballing here, but Ford or somebody like that could give
*  $100 million to the development of NumPy and literally look at the top most popular projects
*  in Python and just say, we're just going to give money. That's going to immediately make you cool.
*  They could actually. In fact, we set up NumFocus to make it easy.
*  The challenge was also you have to have some business development. It's a bit of a seeding
*  problem. I've talked to the folks at Linux Foundation, I know how they're doing it. I know
*  how in starting NumFocus because we had two babies in 2012. One was Anaconda, one was NumFocus. They
*  were both important efforts. They had distinct journeys and super grateful that both existed
*  and still grateful both exist. There's different energies in getting donations as there is getting
*  this is important to my business. I'm going to make money this way. If you can tie the
*  message to an ROI for the company, it becomes a more effective. It's much more effective.
*  There are rational arguments to make. I've tried to have conversations with marketing,
*  especially marketing departments. Very early on, it was clear to me that, oh, you could just take
*  a fraction of your marketing budget and just spend it on open source development and you get better
*  results from your marketing. Sorry, I'm going to try not to go on grants here. What have you learned
*  from the interaction with the marketing folks on that kind of? You gave a great example of something
*  that will obviously be much better investment in terms of marketing is supporting open source
*  projects. The challenge is not dissimilar from the challenge you have in academia,
*  the different colleges. Knowledge gets very specific and very channeled. People get a lot
*  of learning in the thing they know about. It's hard then to bridge that and to get them to think
*  differently enough to have a sense that you might have something to offer because it's different.
*  How do I implement that? What do I do with that? Which budget do I take from? Do I slow down my
*  spend on Google Ads or my spend on Facebook Ads or do I not hire a content creator? There's an
*  operational aspect to that. You have to be the CMO or the CEO. You have to get the right level.
*  You have to hire at a high position level. People that care about this and they specialize.
*  They won't know how. You can also do it very clumsily. You absolutely have to honor and
*  recognize the people you're going to and the fact that if you just throw money at them,
*  it could actually create more problems. Can I just say, this is not you saying,
*  because I just need to say this. I've been very surprised how often marketing people are terrible
*  at marketing. I feel like the best marketing is doing something novel and unique that anticipates
*  the future. It feels like so much of the marketing practice is like what they took in school or maybe
*  they're studying from what was the best thing that was done in the past decade and they're
*  just repeating that over and over as opposed to innovating. Taking the risk. To me, marketing
*  is taking the big risk and being the first one to risk. There's an aspect of data observation
*  from that risk that's I think is shared what they're doing already. I think it's content.
*  There's this whole world on content marketing that you could almost say, well, yeah, it can get over.
*  You can get inundated with stuff that's not relevant to you. Whereas what you're saying
*  would be highly relevant and highly useful and highly beneficial.
*  Yeah, but it's risky. That's why there's a lot of innovative ways of doing that. Tesla is an
*  example of people that basically don't do marketing. They do marketing in a very,
*  let's say, Elon hired a person who's just good at Twitter for running Tesla's Twitter account.
*  That's exactly what you want to be doing. You want to be constantly innovating in the-
*  There's an aspect of telling. I've definitely seen people doing great work where you're not
*  talking about it. I would say that's actually a problem I have right now with QuantSight Labs.
*  QuantSight Labs has been doing amazing work. Really excited about it, but we have not been
*  talking about it enough. We haven't been- There's different ways to talk about it.
*  There's different ways to, there's different channels through which to communicate. There's
*  also, I'll just throw some shade at companies I love. For example, iRobot, I just had a
*  conversation with them. They make Roombas. I think I love the incredible robots, but every time they
*  do like marketing type stuff, it just looks so corporate. To me, the incredible, maybe wrong
*  in the case of iRobot, I don't know, but to me, when you're talking about engineering systems,
*  it's really nice to show off the magic of the engineering and the software and all the
*  geniuses behind this product and the tinkering and the raw authenticity of what it takes to
*  build that system versus the marketing people who want to have pretty people standing there,
*  all pretty with the robots moving perfectly. To me, there's some aspect, it's like speaking
*  to the hackers. You have to throw some bones, some care towards the engineers, the developers,
*  because there's some aspect, one, for the hiring, but two, there's an authenticity to that kind of
*  communication that's really inspiring to the end user as well. If they know that brilliant people,
*  the best in the world are working at your company, they start to believe that that product that
*  you're creating is really good. It's interesting, because your initial reaction would be, wait,
*  there's different users here, why would you do that? My wife bought a Roomba, and she loves
*  developers, she loves me, but she doesn't care about that. It's interesting what you said is,
*  actually, the authenticity, because everyone has a friend, everyone knows people, there's word of
*  mouth. Word of mouth is so, so powerful. Yeah, exactly. That's interesting. I think it's the
*  lack of that realization, there's this halo effect that influences your general marketing.
*  Interesting. For some stupid reason, I do have a platform, and it seems that the reason I have a
*  platform, many others like me, millions of others, is the authenticity, and we get excited naturally
*  about stuff. I don't want to get excited about that iRobot video, because it's boring, it's
*  marketing, it's corporate, as opposed to, I wanted to do some fun, this is me, like a shout out to
*  iRobot, is they're not letting me get into the robot. Yeah, well, there's an aspect of,
*  that could be benefiting from a culture of modularity, like add-ons, and that could
*  actually dramatically help. You've seen that over history, Apple is an example of a company like
*  that, or the, I can see what your point is, is that you have something that needs to be,
*  it needs to be adopted broadly, the concept needs to be adopted broadly, and if you want to go
*  beyond this one device, you need to engage this community. Yeah, and connecting to the open
*  sources, you said, I gotta ask you, you're a programmer, one of the most impactful programmers
*  ever, you've led many programmers, you lead many programmers, what are some from a programmer
*  perspective, what makes a good programmer, what makes a productive programmer, is there a device
*  you can give to be a great programmer? That's a great, great question, and there are times in my
*  life I'd probably answer this even better than I hope maybe give an answer today, because I thought
*  about this numerous times, like right now I've spent on so much time recently hiring salespeople
*  that- That your mind is a little bit-
*  My mind is a little bit- On something else.
*  On something else, but I reflected on the past, and also, I have some really, the only way I can
*  do this is I have some really great programmers that I work with, who lead the teams that they
*  lead, and my goal is to inspire them and hopefully help them, encourage them, and be, help them
*  encourage with their teams. I would say there's a number of things, a couple of things. One is
*  curiosity. I think a programmer without curiosity is mundane, like you'll lose interest, you won't
*  do your best work, so it's sort of, it's an affect, it's sort of, are you, have some curiosity about
*  things. I think two, don't try to do everything at once, recognize that you're, you know, we're
*  limited as humans, you're limited as a human, and each one of us are limited in different ways,
*  you know, we all have our different strengths and skills, so it's adapting the art of programming
*  to your skills. One of the things that always works is to limit what you're trying to solve,
*  right? So, if you're part of a team, usually maybe somebody else has put the architecture
*  together and they've gotten, given a portion for you if you're young. If you're not part of a team,
*  it's sort of breaking down the problem into smaller parts, is essential for you to make progress.
*  It's very easy to take on a big project and try to do it all at once, and you get lost,
*  and then you do it badly. And so, thinking about, you know, very concretely what you're doing,
*  defining the inputs and outputs, defining what you want to get done, even just talking about that,
*  and like writing down before you write code, just what are you trying to accomplish? I mean,
*  very specific about it really, really helps. I think using other people's work,
*  right? Don't be afraid that somehow you're, like you should do it all. Like, nobody does.
*  Stand on the shoulders of giants. And copy and paste some stack overflow.
*  Copy and paste some stack overflow. But don't just copy and paste, it's particularly relevant
*  in the era of codecs and the auto-generated code, which is essentially I see as an indexing of
*  stack overflow. Right, exactly.
*  Exactly. It's like- It's the search engine.
*  It's the search engine over stack overflow basically. So, it's not, I mean, we've had this
*  for a while, but really you want to cut and paste, but not blindly. Like, absolutely have cut and
*  paste to understand, but then you understand, oh, this is what this means. Oh, this is what it's
*  doing. And understand as much as you can. So, it's critical. That's where the curiosity comes in.
*  If you're just blindly cutting and pasting, you're not going to understand. And so, understand.
*  And then, you know, be sensitive to hype cycles, right? Every few often, there's always a, oh,
*  test-driven development is the answer. Oh, object-oriented is the answer. Oh,
*  there's always an answer. You know, agile is the answer. Be cautious of jumping onto a hype cycle.
*  Likely, there's signal. Like, there's a thing there that's actually valuable you can learn from,
*  but it's almost certainly not the answer to everything you need.
*  What lessons do you draw from you having created NumPy and SciPy, like, in service of sort of
*  answering the question of what it takes to be a great programmer and giving advice to people?
*  How can you be the next person to create a SciPy?
*  Yeah. So, one is listen.
*  To?
*  Listen.
*  To who?
*  To people that have a problem, right? Which is everybody, right? But listen and listen to many.
*  And try to then do. Like, you're going to have to do an experiment. You know, do, fall down. Don't
*  be afraid to fall down. Don't be afraid. The first thing you do is probably going to suck,
*  and that's okay. Right? It's honestly, I think iteration is the key to innovation.
*  And it's almost that psychological hesitation we have to just iterate. Like, yeah, we know
*  you, we know it's not great, but next time it'll be better. I mean, just keep learning and keep
*  improving and keep improving. So, it's an attitude. And then it doesn't take intense concentration.
*  Right? Good things don't happen. Just, it's not quite like TikTok or like Facebook. You know,
*  you can't scroll your way to good programming. Right? There are, you know, sincere, like hours
*  of deep, don't be afraid of the deep problem. Like often people will run away from something
*  because, oh, I can't solve this. And you might be right, but give it an hour. Give it a couple
*  of hours and see. And, you know, just five minutes, not going to give you that.
*  Was it lonely when you were building SciPy and Numpy?
*  Hugely. Yeah. Absolutely lonely in the sense of you had to have an inner drive. And that
*  inner drive for me always comes from, I have to see that this is right in some angle. I have to
*  believe it, that this is the right approach, the right thing to do. With SciPy, it was like, oh,
*  yeah, the world needs libraries in Python. Clearly Python is popular enough with enough
*  influential people to start and it needs more libraries. So that is a good in and of itself.
*  So I'm going to go do that good. So find a good, find a thing that you know is good and just work
*  on it. So that has to happen. And it is, and you kind of have to have enough realization of your
*  mission to be okay with the naysayer or the fact that not everybody joins you up front. In fact,
*  one thing I've talked to people a lot, I've seen a lot of projects come and some fail. Like not
*  everything I've done has actually worked perfectly. I've tried a bunch of stuff that, okay, that didn't
*  really work or this isn't working and why, but you see the patterns. And one of the key things is
*  you can't even know for six months, I say 18 months right now, if you're just starting a new project,
*  you got to give it a good 18 month run before you even know if the feedback's there. Like it's,
*  you're not going to know in six months. You might have the perfect thing, but six months from now,
*  it's still kind of still emerging. So give it time because you're dealing with humans and humans have
*  an inertial energy that just doesn't change that quickly. So.
*  Let me ask a silly question, but like you said, you're focused on the sales side of things
*  currently, but back when you were actively programming, maybe in the nineties, you talked
*  about IDEs. What's your, a setup that you have that brings you joy, keyboard, number of screens,
*  Yeah, I will.
*  Linux.
*  I do still like to program some, it's not as much as I used to. I have two projects I'm super
*  interested in trying to find funding for them, trying to figure out some good teams for them,
*  but I could talk about those. But what I, yeah, what I get, I'm an EMAX guy.
*  Great. Thank the superior editor. Everybody I've got, I've, I don't often delete tweets,
*  but one of the tweets I deleted when I said EMAX was better than them. And then the hate I got,
*  it is, I was like, I'm walking away from this.
*  I do too. I don't push it. I mean, I'm not, I'm just joking. Of course.
*  Yeah, exactly. It's kind of like, but people do take the editor.
*  They take it seriously. I did as a joke.
*  But it's your life.
*  It is, but there's something, there's something beautiful to me about EMAX,
*  but there's for people that love him, there's something beautiful to them about that.
*  I mean, I do use them for quick editing, like command line. If I said quick editing,
*  I will still sometimes use it, but not much. Like it's simple, corrective,
*  corrective single editor character.
*  So when you were developing SciPy, you were using EMAX.
*  Yep. SciPy and NumPy are all in an EMAX on that Linux box and CVS and then SVN,
*  version control. Git came later. Like Git has, I love distributed branch stuff.
*  I think Git is pretty complicated, but I love the concept. And also of course, GitHub is,
*  and then GitLab make Git definitely consumable. But that came later.
*  Did you ever touch Lisp at all? Like were your emotional feelings about all the parentheses?
*  Great question. So I find myself appreciating Lisp today much more than I did early.
*  Because when I came to programming, I knew programming, but I was a domain expert.
*  And to me, the parentheses were in the way. It's like, wow, it's just all this,
*  it just gets in the way of my thinking about what I'm doing. So why would I have all these?
*  That was my initial reaction to it. Now as I appreciate kind of the structure that kind
*  of naturally maps to a logical thinking about a program, I can appreciate them.
*  And why it's actually, you could create editors that make it not so problematic,
*  right? Honestly. So I actually have a much more appreciation of Lisp and things like
*  Clojure and there's Hy-Vee, which is a Python, a list that compiles the Python bytecode.
*  I think it's challenging. Like typically these languages are, I even saw the whole data science
*  programming system in Lisp that somebody created, which is cool. But again, I think it's the lack
*  of recognition of the fact that there exists what I call occasional programmers. People are never
*  going to be programmers for a living. They don't want to have all this cuteness in their head.
*  They want just, it's why basic, you know, Microsoft had the right idea with basic in
*  terms of having that be the language of visual basic, the language of Excel and SQL SQL server.
*  They should have converted that to Python 10 years ago, but probably a better place that they had.
*  But there's also, there's a beauty and a magic to the history behind a language in Lisp. You know,
*  some of the most interesting people in the history of computer science and artificial
*  intelligence have used Lisp. So yes, you feel well, it's back to that language. When you,
*  when you have a language, you can think in it. Yeah. And it helps you think about it.
*  It attracts a certain kinds of people that think in a certain kind of way. And then that's,
*  that's there. Okay. So what about like small laptop with a tiny keyboard or is there like,
*  three screens, you know, good question. I've never gotten into the big, the many screens,
*  to be honest. I mean, and maybe it's because in my head, I kind of just, I just swap between windows,
*  like partly because I guess I really can't process three screens at once. Anyway, like
*  I just, I'm looking at one and I just flip, you know, I flip an application open.
*  So where it's really helpful is actually when I'm trying to do, you know, here's data and I want to
*  input it from here. That's the only time I really need another screen. So now because you're both
*  developer lead developers, but then there's also these businesses and there's sales people, you're
*  working with large companies, operations people, hiring people. Yeah. The whole thing.
*  Which operating system is your favorite at this, at this point? So Linux was the early
*  Linux. So yeah, I love, love Linux as a, as a server side and was early days. I was,
*  I had my own Linux desktop. I've been on Mac laptops for 10 years now. Yeah.
*  This is what leadership looks like. Switch to Mac. Okay. Great. Pretty much. I mean,
*  just the fact that I had to do PowerPoints, I had to do presentations and, you know, plug in,
*  I just couldn't mess with plugging in laptops. It wouldn't project and yeah. So you mentioned
*  also Quantset Labs and things like that. Can you give advice on how to hire great programmers
*  and great people? Yeah. I would say produce an open source project.
*  Get people contributing to it and hire those people. Yeah. I mean, you're doing it sort of
*  you might, maybe perhaps a little biased, but that's probably a hundred percent really good advice.
*  I find it hard to hire. I still find it hard to hire. Like in terms of, I don't think that
*  it's not hard to hire if I've worked with somebody for a couple of weeks,
*  but a cup, an hour or two of interviews, I have no idea. So that instinct, that radar of knowing
*  if you're good or not, that you've, you found that you're still not able to really. It's really hard.
*  I mean, the resume can help, but again, the resume is like a presentation of the things
*  they want you to see, not the reality of, and there's also, you know, you have to understand
*  what you're hiring for. There are different stages and different kinds of skills. And so
*  it isn't just a, one of the things I talk a lot about internally at my company is that
*  the whole idea of measuring ourselves against a single axis is flawed because we're not,
*  it's a multidimensional space and how do you order a multidimensional space? There isn't one
*  ordering. So this whole idea, you immediately have projected into a thing when you're talking
*  about hiring or best or worst or better or not better. So what is the thing you're actually
*  needing? And you can even hire for that. There is such a thing, generally I really value people
*  who have the affect, the care about open source. Like, so in some cases they're thinning open
*  source is simply a kind of a filter of an affect. However, I have found this interesting dichotomy
*  between open source contributors and product creation. I don't know if it's fully true,
*  but there does seem to be the more experience, the more affect somebody has in open source
*  community, the less ability to actually produce product that they have. And the opposite is kind
*  of true too. The more product focused are, I find a lot of people, I've talked to a lot of people
*  who produce really great products and they have a, they're looking over the open source communities,
*  kind of wanting to participate and play, but they played here and they do a great job here.
*  And then they don't necessarily have some of the same. Now I don't think that's entirely
*  necessary. I think part of it is cultural, how that's, how they've emerged. Because one of the
*  things that open source communities often lack is great product management, like some product
*  management energy. That's brilliant. But you want both of those energies in a place together.
*  Yes, you really do. And so it's a lot of it's creating these teams of people that have these
*  needed skills and attributes that are hard. And so, so one of the big things I look for is somebody
*  that fundamentally recognize their need to learn, to learn, like one of the values that we have in
*  all of the things we do is learning. Like if somebody thinks they know it all, they're going
*  to struggle. And some of that is just, there's more basic things like humility, just being humble
*  in the face of all the things you don't know. And that's like step one of learning. That's step one
*  of learning. Right. And, and you know, I've spent a lot of time learning, right. Other people spend
*  a lot more time, but I've spent a lot of time learning. I went, you know, my whole goal was
*  get a PhD because I love school and I wanted to be a scientist. And then what I found is what's been
*  written about elsewhere as well as the more I learned, the more I didn't know, the more I
*  realized, man, I, I know about this, but this is such a tiny thing in the global scope of what I
*  might want to know about. So I need to be listening a whole lot better than, than I am just talking.
*  That's changed a little bit. Actually, my wife says that I used to be a better listener. Now that
*  I have, I'm so full of all these ideas I want to do, she kind of says, you got to give people
*  time to talk. So you've succeeded on multiple dimensions. So one is the, the 10 year track
*  faculty. The other is just creating all these products and building up the businesses, then
*  working with businesses. Do you have advice for young people today in high school, in college of
*  how to live a life as a nonlinear and as successful as yours, a life that could be, they could be proud
*  of? Well, that's, that's a super compliment. I'm humbled by that. Actually, I, I would say
*  a life that can be proud of, honestly, one thing that I've said to people is first, find people you
*  love and care about them. Like family matters to me a lot and family means people you love and have
*  committed to. Right. So it's, it could be whatever you, you mean by that, but it's, it, you need to
*  have a foundation. So find people you love and want to commit to and do that. Cause it anchors
*  you in a way that nothing else can. Right. And then, and then you find other things and then kind
*  of from out there, you find other kinds of things you can commit to, whether it's ideas or, or people
*  or groups of people. So, you know, especially in high school, I would say, don't settle on what you
*  think, you know, right? Give yourself 10 years to think about the world. Like there's, I see a lot
*  of high school students who seem to know everything already. I think I did too. I think it's maybe
*  natural, but, but recognize that the things you care about, you might change your perspective
*  over time. I certainly have over time is that, you know, I was really passionate about one specific
*  thing and I was kind of softened. You know, I was a big, I didn't like the federal reserve, right?
*  And there's still, we can have a longer conversation about monetary policy and finances, but,
*  but I'm a little more nuanced in my, in my perspective at this point. But you know, that's,
*  that's one area where you learn about something and go, ah, I want to attack it, you know, build,
*  don't destroy, like build, like so much, so often the tendency is to not like something,
*  they want to go attack it, build something, build something to replace it, build up, you know,
*  attract people to your new thing. You'll get far, you'll be far more, far better, right? You don't
*  need to destroy something to build something else. So that's, I guess, generally. And then,
*  you know, definitely, like curiosity, you know, follow your curiosity and, and let it,
*  don't just follow the money. And all of that, like you said, is grounded in family friendship and
*  ultimately love. Yes. Which is a great way to end it. Travis, you're one of the most impactful
*  people in the engineering, the computer science, in the human world. So I truly appreciate everything
*  you've done. And I really appreciate that you would spend your valuable time with me. It was
*  an honor. It was a real pleasure for me. I appreciate that. Thanks for listening to this
*  conversation with Travis Oliphant. To support this podcast, please check out our sponsors in
*  the description. And now let me leave you with something that in the programming world is called
*  Hodgson's law. Every sufficiently advanced Lisp application will eventually be re-implemented
*  in Python. Thank you for listening and hope to see you next time.

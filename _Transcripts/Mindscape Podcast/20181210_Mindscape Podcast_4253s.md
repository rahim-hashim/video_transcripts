---
Date Generated: June 10, 2024
Transcription Model: whisper medium 20231117
Length: 4253s
Video Keywords: ['comics', 'computer', 'design', 'electronic', 'music']
Video Views: 6698
Video Rating: None
Video Description: Blog post (with audio player, show notes, and transcript): https://www.preposterousuniverse.com/podcast/2018/12/10/episode-26-ge-wang-on-artful-design-computers-and-music/

Patreon: https://www.patreon.com/seanmcarroll

Everywhere around us are things that serve functions. We live in houses, sit on chairs, drive in cars. But these things don't only serve functions, they also come in particular forms, which may be emotionally or aesthetically pleasing as well as functional. The study of how form and function come together in things is what we call "Design." Today's guest, Ge Wang, is a computer scientist and electronic musician with a new book called Artful Design: Technology in Search of the Sublime. It's incredibly creative in both substance and style, featuring a unique photo-comic layout and many thoughtful ideas about the nature of design, both practical and idealistic.

 Ge Wang received his Ph.D. in computer science from Princeton University, and is currently Associate Professor at the Center for Computer Research in Music and Acoustics at Stanford University. He is the author of the ChucK programming language for musical applications, and co-founder of the mobile-app developer Smule. He has given a well-known TED talk where he demonstrates Ocarina, an app for turning an iPhone into a wind instrument.
---

# Episode 26: Ge Wang on Artful Design, Computers, and Music
**Mindscape Podcast:** [December 10, 2018](https://www.youtube.com/watch?v=pCe2mGDmsfk)
*  Hello everyone and welcome to the Mindscape Podcast. I'm your host Sean
*  Carroll and as I've said before one of the major motivations for me personally
*  in doing a podcast project is to be able to explore things other than what I do
*  for a living, mostly physics, a little bit of philosophy. So the podcast lets me
*  talk to other scientists, neuroscientists, biologists, chemists and it also lets me
*  go beyond science. We've talked to poker players and movie directors and
*  musicians and so forth. So today's podcast is definitely one of those
*  examples of going well beyond my comfort zone. Go Wang, today's guest, is
*  actually a computer scientist, officially, a computer programmer at
*  Stanford University and that's my comfort zone, okay, but his specialty is
*  computer programming of music. So he builds instruments that make computers
*  into musical instruments. He puts on performances with laptop orchestras,
*  things like that. Go Wang has a famous TED talk where he demonstrates an iPhone
*  ocarina. You can actually, if you have an iPhone, go to the app store, download an
*  app called ocarina which will turn your iPhone into a musical instrument. You
*  don't need any extra hardware, you blow into the microphone and make beautiful
*  music. We'll actually have a demonstration on the podcast today.
*  However, Go wrote a book that was not about computer programming or musical
*  instruments but about the general idea of design, artful design, designing
*  anything, whether it's computers or musical instruments but cups of coffee
*  or pencil boxes or anything like that. The general principles that relate form
*  and function, the human needs and the possibilities of the technology or the
*  shapes you're doing, whether it's music or art or industrial design. I know
*  nothing about this. I think it's a cool and important topic, so we had a great
*  conversation. But this is definitely an example where we're learning new things.
*  I bring no special predilections or pre-existing notions to this
*  conversation and therefore we had a lot of fun. Design is everywhere in our lives
*  and thinking about it with someone who is also an expert in computer science
*  and music was a great experience. So let's go.
*  Go Wong, thanks for coming on the Mindscape podcast. Thanks, John. Thanks
*  for having me. Now I'm gonna admit right away that this is going to be one of the
*  more adventurous podcasts that I've done. You've written a book about design,
*  which is something I know nothing about. Not like even when I know nothing about
*  things like neuroscience or whatever, I still have opinions about them. And here's
*  something I don't even have opinions about. So hopefully we'll have a wide
*  ranging conversation and you'll be able to guide me through the rough spots and
*  so forth. But let's start with the fact that in some sense you're a computer
*  programmer. You're a computer scientist. Is that a fair thing to say? That is a
*  fair thing to say. My PhD and undergrad were both in computer science even though
*  now I'm an associate professor in the music department. Actually in the Center
*  for Computer Research and Music and Acoustics, CCRMA or CARMA at Stanford.
*  But that's within the music department. Within the music department. I have a
*  courtesy appointment in computer science. So I'm kind of really ever kind of in
*  both places and neither places. I don't actually don't know what I am exactly,
*  but I think it's fair to say I'm a computer scientist. It's the best place
*  to be, not knowing where you are. But you have to get to not knowing where you are.
*  I mean did the computer interest come first or the music interest? You know at
*  some point those were both interesting because I love building things and I
*  think the computer science eventually spoke directly to that. I could really
*  realize things that I wanted to see how this works. And then I always
*  loved music. Did you grow up playing instruments? I grew up
*  playing the accordion at age seven. Wow, that's hardcore. And then my
*  grandparents got me that and then my parents got me an electric
*  guitar for my 13th birthday. That changed my world. Are you one of these people?
*  Because I know some people like they're handed an instrument they never played
*  it before and like within minutes beautiful music is coming out and I am
*  completely opposite of that. I don't know. I don't know about beautiful music but I
*  love just playing instruments figuring out how they actually interact and how
*  they work. And yeah something some sounds will likely come out if you hand me an
*  instrument. It might not be beautiful. And at some point, I mean when did you
*  realize that the computer side of things could have a musical
*  component? Really towards the end of undergrad. I was taking music
*  classes, taking computer science classes and then I took a class at Duke
*  because we're a dem undergrad from Professor Scott Lindroth who's actually
*  now the vice provost of the arts at Duke and he's a you know he's I think he's
*  been a lifelong mentor and I took this computer music class and I heard music
*  that was just like I didn't hear anywhere else and felt and realized I
*  couldn't really hear anywhere else except in the medium of the computer and
*  that fascinated me. Were you already a computer science major at that point? Yeah I was
*  already a computer science major. Okay cool and so then you go to your PhD and like help
*  write programming languages and things like that. Yeah so I think having had
*  that experience with like electronic music, computer music, undergrad, applied
*  to grad school in computer science but really kind of looking for programs that
*  did computer music and I was very fortunate to find well my advisor Perry
*  Cook at Princeton using computer science but he also was jointly appointed at
*  Princeton in music so he's actually was Princeton's first joint hire across
*  engineering in arts and humanities. That's very difficult to do I know yeah.
*  Yeah and so I ended up working on things like yeah programming language for
*  generating music it's called Chuck we're working and I'm working on laptop
*  orchestras. But writing a programming language that just sounds very hardcore
*  like are you in there is it a assembly language? How do you write a programming
*  language or do you write it in a different language and then compile? So
*  Chuck was written in C++ and the way I wrote it was well I took a compiler
*  class and then I basically well it's I followed basically chapter by chapter
*  this textbook on how to basically how to make a compiler in programming languages
*  by Andrew Appel who happened to be another professor at Princeton at the
*  time and and and I literally knew nothing about making a programming
*  language so I literally just followed the textbook but then I deviated when I
*  when I needed to and I think I designed it really backwards. I designed it
*  backwards I think and I mean that in a good way in that I kind of wrote down on
*  paper the kind of code I wanted to write and I wanted and to get the kind of
*  music I want so I kind of said you know what I want this thing to look like and
*  now I went back and see if I can actually do it by writing code to kind of
*  implement these. Are you telling me that form follows function? Sometimes yes form
*  often follows function sometimes function follows form in a weird way. Who
*  was the guy who said that for the first time? It was an American architect Lewis
*  Sullivan. Lewis Sullivan okay yes yeah and of course it's you know he's trying
*  to make a point but in reality like you say there are two things form and
*  function that go back and forth and so this is is it is it safe to say that
*  designing this computer programming language is one of the first ways you
*  came into contact with that principle? Yeah I mean I didn't really think too
*  too intentionally consciously about design at the time I just wanted to build
*  things. It was actually my advisor Perry Cook who said this cryptic thing to me
*  and said you know go whatever you whatever you make you know whatever you
*  do do it with aesthetics and I was like I have no idea what that means. No one ever told me that before. I'm a computer science
*  major. Right no one and yeah but it oddly made sense and Perry still denies that
*  he's ever said this he doesn't remember he actually said this to me but like I
*  was like this completely changed the way I I do things is things are not just
*  pure functional things we are not purely functional creatures but we we actually
*  you know you say that you don't you don't know anything about design but I
*  would beg to differ and I think we all we all have and cannot help them make
*  aesthetic judgments on things you know what's not just what's pleasing but
*  what's beautiful what's truthful what's just and what's just plain awesome these
*  are all I think aesthetic judgments. Well that's good I mean it's what I wanted to
*  get into that at some point but let me just back up a little bit because
*  despite being a computer scientist but despite having a appointment in a music
*  department yes you didn't write a book about computer music there's computer
*  music in there but you wrote you took a grander palette right you aim for bigger
*  fish. Yes I think it's artful design I well I took me three years to write it
*  and I still don't know exactly what it's about or any more I thought I did it has
*  a lot of computer music in there but I think it tries to address you know three
*  questions and you know I would say they are you know what is the nature of
*  design and the meaning it holds in human life what does it mean to design well
*  and to design ethically and how can this shaping of technology reflect our
*  values as human beings so those are kind of these broader questions I tried to
*  tackle. Yeah these are pretty big questions. Very interdisciplinary and also you know very grand but like you say
*  everyone has some kind of design sense right I mean like I say for scientists
*  sometimes degrading philosophy I always tell them look you can't not do
*  philosophy you can do it well or you could do it badly right and if you're
*  not educated then maybe you do it badly then maybe design is the same way. I love
*  that I think that's I personally think that's absolutely right is that you just
*  you know whatever I think design is really you have an outcome or something
*  in mind and you go about very intentionally shaping or changing
*  things to kind of achieve that outcome you put you're kind of putting the
*  pieces together making them fit to actually you know get at some result or
*  for a certain purpose and when you do that you're designing. And at what point
*  did you go from you know you have been designing of course computer programming
*  languages and we'll get into actual musical instruments and orchestras and
*  so forth but what is it that made you think that the book you should write
*  should be about the idea of design rather than about these more specific
*  examples of it? That's a good question I think a couple of things for one I
*  think I was realizing what I was doing was like engineering it's like art but
*  it's also not like engineering exactly not like art exactly right it embodies
*  engineering precision you do need to really get to the nuts and bolts of you
*  know how you program or how you do software engineering or how a certain
*  technique or technology actually works. And you build hardware things as well
*  right? From time to time I'm mostly a software guy but sometimes I dabble in
*  hardware as well. And in like art it's there's a certain artfulness you can
*  definitely bring into the things you engineer not just in how it looks but
*  kind of you know how it actually works and does the way of working actually
*  reflect something you wanted to reflect. These more I think tacit and intangible
*  qualities of something that we clearly care about you know if you just look at
*  buildings right people design buildings and if we just cared about the function
*  we'd all be content living in warehouses and clearly we're not. So I think that we
*  know to do think about buildings in that way but you know I think when it comes
*  to things like software, tools, games, social experiences these are I think
*  we're just learning to think about more aesthetically yeah about these things
*  and it reminds me a little bit I interviewed Scott Derrickson movie
*  director for the podcast and I was remarking to him that you know I I'm
*  very happy with books and words and pages and also equations and figures and
*  other physics-y things. So I could imagine in an alternate life being like
*  a movie screenwriter or a novelist or something like that. I couldn't imagine
*  being a director because there's a million other things have to worry about
*  like that personalities of the actors but also the design of the sets and the
*  costumes and everything and he and he said which sort of the obvious answer
*  but you know that's what he likes he likes the fact that there's a little bit
*  of everything involved and it sounds like you were drawn to the fact that you
*  were computer programming but in a way that you know given that it was music
*  and instruments and so forth design just became a necessary element pretty
*  obviously. Yeah and I think that's right and I felt like design is really this
*  universal thing that we all do but only more you know recent times that we do we
*  think about design and as kind of a discipline or a thing onto itself but I
*  think we've always designed we can't help but design but I think it well like
*  anything else it's it's also possible to do well or do poorly right and I'm
*  really interested in how we can think about doing it well or doing it better. I
*  mean obviously Archimedes or Leonardo were designers even though they wouldn't
*  have called themselves that. Right. So it's it I mean is is it true or are we
*  just fooling ourselves to think that there is a separate discipline called
*  design right? Yeah we design so many different things from music to you know
*  teapots right and are there common principles there? I that's a wonderful
*  question I think I like to think that the design shouldn't be its own actually
*  separate discipline actually I think it's just something that all of us do and
*  there's a certain universality I think that actually does pervade design really
*  everywhere. In artful design I think I try to offer a few of them one is this
*  idea that I you know in looking at the motivation you know design is all about
*  purpose it's like what are you trying to do and and then how are you gonna go
*  about doing it and I would also add why would you want to do that so there's all
*  these different dimensions I think that's common to any design and and then
*  part of this why you know I break it down into this into means versus ends and
*  what I mean by that means as in means to an end like I do this because I want to
*  achieve some of the purpose you know I'm hey I'm gonna make this thing to open a
*  can for me right I so that's that's a means to an end but it and in itself
*  it's the other side are kind of the more intrinsically interesting or valuable or
*  beautiful things about a design. Form would fit into that. This is the idea we
*  don't want all live in warehouses exactly live in an aesthetically pleasing
*  space. Yeah aesthetically pleasing but also place things to with meaning you
*  know buildings aren't just pleasing it's great when they are right but also you
*  know buildings can serve as kind of symbols can serve as meaning for the
*  for the people or this even the city that it's in and and also I think
*  there's a certain well for lack of better word truth that we can get at when
*  we actually design things you know okay it's something that reflects who we are
*  in kind of our values and I think that all from that for me is all kind of in
*  these this aesthetic dimension of design so there is certainly this this idea
*  that let's make things look really look and feel good but I think it actually
*  goes much deeper than that and that we can you know that is a tool even if
*  you're building a tool you know it's a tool making people's lives better does it
*  speak to your well-being and and what are the values that actually that's
*  actually a play here yeah I think that this is I mean like I said since I'm not
*  an expert and I have no prior experience to the formal aspects of this way of
*  thinking I was trying to you know struggle with how to even grasp what the
*  essence of design is supposed to be there is an aesthetic component
*  obviously but it's not just hanging art on your wall it is this functional
*  aspect of things right and so at the trivial level there's this marriage
*  between doing things or having things done for purpose and having them
*  aesthetically pleasing but what you're pointing at is that there's like I'm not
*  sure if it's another dimension or an extra movement in the same direction of
*  meaningfulness and you know some connection with what it means to be
*  human is reflective in the best design I think that's exactly right I think it's
*  this meaning you know it can there's actually a principle in the book that
*  actually was talking about AI and automation and I think the principles a
*  two-part one it says you know that which can be automated should be automated
*  except where in cases where you know if something is cannot be meaningfully
*  automated it should not be automated so I'll give you an example the other day
*  yeah what's an example well for example this act of playing to play like I like
*  well like playing hopefully right and to play like I don't it doesn't matter how
*  well I play I just want to play and I don't ever want that automated because
*  the whole point of playing is to do it yourself right right you don't want to
*  build a computer program to play your video games for you exactly and and all
*  these you know a lot of things that are well experiential for example it's
*  meaningful for us to do and it's and certainly I can have like a program or
*  robot kind of play in my place but what's the point of that you know it's
*  possible but not meaningful and at some level I think this you know for all the
*  automation that that's coming into our world with technology I think humans at
*  some level still have to be the arbiters of meaning you know we have to determine
*  what is meaningful to do and you know what do we want to what do we want to
*  do and that gets back to this question of you know what's intrinsically
*  interesting about you know certain activities well good so we have time
*  here so let's let's unpack this a little bit because I've had philosophers on the
*  podcast and will and you know one of them Alex Rosenberg I recently talked to
*  you know kind of is skeptical about the idea of meaning at all and but I think
*  he's an extremist on one side so let's go to the other side like what would he
*  mean meaning what is it what is that is it just I care about that or is there
*  something deeper do you personally delve into the philosophical literature when
*  thinking about these things not meaning per se but I do delve into some
*  philosophical literature I think meaning is really like for me it's actually
*  simpleness and not in the not simplistic but simple in the sense I think it is
*  what we value okay it's the meaning is you know if it's meaningful to you that
*  means you find some value that mmm and I would say a more inwardly rewarding kind
*  that's the meaning more bling more more money or whatever right it's not the
*  not enough exactly it's more like your soul and in a play for example I think
*  is a is a good example of like this is it matters to me may not matter anybody
*  else but that value of play is so fundamental to it's it's a so something
*  that speaks to this value of play is meaningful to me in that sense so I think
*  it's interesting to think about why play exists right why through the process of
*  natural selection this came to be I mean I have cats I grew up with dogs
*  certainly other animals are very playful in their own right it doesn't serve some
*  function or is that is that is it just an offspring of other things are useful
*  well it's it I've thought about that a lot I have no no clear answers on that
*  but it leaves me think about other things like food and eating right I think
*  it's a related thing to play like eating and one hand it's very functional
*  right we eat so we sustain ourselves so we don't die but clearly we've were at a
*  point where we also eat for its sheer enjoyment and I think there's in this
*  one thing we find we actually have this dual purpose if you know one is very
*  functional one is very aesthetic and we clearly spent a lot of time and energy
*  thinking about and going about like making food making sure there is food
*  and you know really cooking is an art right so I sometimes I wonder if like you
*  know where our aesthetics actually come from the aesthetic of play the aesthetic
*  food the aesthetic of really if finding things beautiful or truthful and did it
*  do they arise from kind of traditional evolutionarily more functional things I
*  don't have I'm not an expert in this so I don't know if I can offer a good answer
*  on this but I think about this all the time is that like word is it's remarkable
*  to remarkable to me that that we can experience things period you know like
*  and it's remarkable that we find things beautiful and even if we knew the answer
*  to the question of where it came from was it wouldn't change the fact that's
*  meaningful and beautiful right I often end some of my talks when I talk about
*  the big picture the book that I wrote there's a lot of sort of deflationary
*  messages you know we're bags of atoms we live for a very short period of time
*  we're small compared to the universe but then you show a picture of the universe
*  the Hubble Ultra Deep Field with all these galaxies and the point is we took
*  that picture right like we decided to spend millions and millions of dollars
*  to take that picture and it's not helping us feed ourselves or anything
*  like that we just wanted we had the curiosity and the interest in the beauty
*  that was brought out by that that's exactly right and you know fundamental
*  research like you know theoretical physics it's for me it's I think of a
*  more less like science and engineering but more as really it's like the
*  humanities in a way right it's really getting at some fundamental truth of
*  about the world it's in like with a capital W or what is there yeah and also
*  our place in it and it's so human to want to to want to understand like that
*  you know I don't tell my colleagues I'm saying this but it does have a lot to do
*  with you know the humanities it's driven by curiosity not by immediate practical
*  interests but as you point out you know even the areas of disciplinary study
*  that are driven by immediately practical interests engineering biology medicine
*  they still have this aesthetic component so maybe let's come back ground ourselves
*  a little bit you you got here through this journey of music and computers and
*  so forth so tell us about some of the design you've done in that arena
*  yourself you know the making of different kinds of musical instruments
*  orchestras and so on sure I've I make tools toys games and social experiences
*  with technology for musical purposes and I could give you a demo of one if you
*  like so this is a this is an app I designed ten years ago I started a
*  company called Smule as Smule is still around and it's a way to make music
*  socially together with people I I stepped down five years ago but Smule is
*  still going strong but designed this as part of Smule Smule ten years gonna it's
*  Ocarina and it's a it's an app for your for your phone you play by blowing into
*  it so much okay before you play is it coming out of that speaker yes okay so
*  we should put that in front of the microphone okay so how directional is
*  it's pretty darn directional so okay so let's try that
*  you may have to edit you may edit part of this out now we're gonna leave this
*  in we're gonna all the messiness is here we did get brought more paraphernalia
*  than any other podcast guest I've had so far so this is awesome so I'm holding
*  my phone but not in the usual way I'm kind of holding it like a sandwich and
*  I'm blowing into the microphone the bottom
*  and I'm using my fingers on the screen to there these four circles that expanse
*  can track when I when I press down on them and those control pitch
*  accelerometer in the iPhone controls vibrato so if I hold the phone flat
*  versus tilting it downward that's vibrato
*  you can play all kinds of little ditty with this and it's a very physical use
*  of the phone and you haven't there's no hardware enhancement to the phone you
*  didn't put a you know pickup or anything like that it how does your
*  blowing on the phone get registered so I'm blowing to the microphone in there
*  there's actually a soft little software program that's tracking the strength of
*  how hard I'm blowing into the microphone you know I'm gonna blow the mic from
*  not gonna do it here but you know we get the and from there you can just
*  basically do an envelope follower and see how much roughly how much energy is
*  in there and then you map that to sound that's being generated on on the device
*  okay and and that's that's pretty much it and then you're mapping the
*  interaction from the multitouch and the accelerometer to different parameters in
*  the sound synthesis and this is called ocarina because it is very much like an
*  existing instrument called the ocarina right this is an instrument that's been
*  around in various forms for thousands of years actually and it's one of the more
*  I would say the one the simpler instruments to start playing because the
*  interaction really is you know you blow into and there's a few holes you can
*  hold down you can to control pitch and to answer your earlier question yeah this
*  is no no no add-ons to the phone the part of the design was and say can we
*  design something that required those little constraints that require no
*  additional components and in a way and I talked about this in our full design
*  this is inside out design this is actually function following a bit of
*  form and a form in this case being your phone yeah you have a phone what are you
*  gonna do with it we didn't do with it what are all the things that's on the
*  phone and and what makes sense and if you go to this exercise like well a
*  piano is like a little too big and interaction you know however keys you
*  have a keys and or guitar or drums these are all but but a four hole English
*  pendant ocarina is about the same size as the as the iPhone and also the
*  complexity of interaction is comparable yeah so that was kind of a match is a
*  perfect match and so it's this backwards like you know I say we design backwards
*  from really the end users experience and we design backwards from the medium in
*  this case the medium was the iPhone and all the things that it's available but
*  you had in mind you number one you wanted to make a musical instrument yes
*  number two you had an iPhone available and so it and our listeners can go
*  download this on the App Store yeah ocarina is available look for smule
*  ocarina and in actually there's another component to Ocarina as well okay
*  this is a social component there's a global visualization and here I'm
*  actually seeing this double helix graphics coming out of actually possibly
*  Southern California to joy someone that calls themselves a belted biscuit
*  belted biscuits this person I know I have no idea classic and undiscovered
*  genius out there and we cross the street we wouldn't know right doesn't matter
*  yeah but you know roughly where they're coming from here's amazing grace from
*  London Adam and that's all you know about you know who these people are you
*  know the app is designed for you not to what's a weird social network so it's
*  basically all that's doing is other people are playing and we can listen to
*  whatever they're playing yeah that's all it all it is and when I play it that
*  means they can listen to me when you're playing feel bad well the app is kind of
*  taking in these little snippets and then a few interaction and sending those up
*  to basically a server and then that's when someone's listening they kind of
*  randomly gets served something in the recent past okay so it's not quite in
*  real time and not quite in real time no so this morning when I was just trying
*  to make it work at all and not really completely succeeding that is not
*  probably sent to anyone that likely was not but you can you can turn this feature
*  on and off but it's kind of an anonymous like listening you know it's it's to say
*  in this in this social system identity doesn't matter it's about like you know
*  physicality because you're blowing to the phone and make music and it's about
*  you know this little sense of connection you have with someone you know if you're
*  like final countdown coming from Korea you'd be like who is that person and the
*  app gives you know gives you no answers on that but it does want you to ask that
*  question yeah that's cool and is there some this probably not a fair question
*  is there follow-up like do you do people make orchestras do they join out in this
*  no follow-up and I think this is a I think of as a logical end here this is
*  not a tool to study kind of how people make music for me it's not a social
*  network it's not a social network it's it's a place where to feel a little
*  connected with the you know and that's that's the end and so that's in that
*  sense you know it goes back to this like that's an end in itself I just want
*  people to feel connected it's not here to serve another purpose beyond that you
*  make what I thought was a really good point about the fact that let's say 200
*  years ago but maybe even more recently than that what families would do in
*  their leisure time is create music together that's right we almost never do
*  that anymore we listen to music and maybe because it's just so easy to put
*  it on a record or you know play Spotify or whatever or Pandora I should mention
*  Pandora because they're my blog my podcast appears on Pandora now maybe
*  it's too easy or maybe there's a skill or are we just exposed to really really
*  good musicians so far that we're embarrassed about our own skills but you
*  want to kind of bring it back the ability to get around you know late at
*  night instead of watching TV we can play music together yeah I think it goes back
*  to this question of meaning and I in values I think music making to me is a
*  value and that's something that I think is does a person good and and I don't
*  know why I think is a lot of different factors that that's changed kind of our
*  relationship with music making technology really is the thing that's
*  changed it over the last really last hundred years you know before household
*  electricity you know to get music there's no broadcast there's no internet
*  there's no recording you had to be where music was you had to listen to music
*  where it was made and and if you look throughout human history there's never
*  been a civilization or a culture that's been without either music or dance so
*  music has been with us and of course we find like flutes made out of like bear
*  femur and and human bones even like kind of dating tens of thousands of years so
*  you know music is has really been with us but only really in the last hundred
*  two hundred years it has you know kind of music is you know for better for
*  better and you know can be recorded it can be disseminated over long
*  distances and and then we can capture like you know kind of like the musicians
*  that really speak to us and we always have their sound and I think that's a
*  good part of it perhaps possible side effect and possible downside is that we
*  might be making less music than ever before and maybe it's because I don't
*  know I don't I don't I refuse to believe it's because we've here we hear people
*  that are like so amazing that we are intimidated I think sometimes they even
*  inspire us but I think it's really just now we have so much that we could do
*  that that can you know it's so much easier just to fire up like a video game
*  which I do and I love playing or to just watch streaming video or whatnot and
*  some all things that I love to do yeah so they could see these out there with a
*  lot of music and I don't know I'm not I get your desire to not think that it's
*  because we're intimidated by people who are better than us but I bet that
*  there's a lot of people who used to think they could sing and now we can
*  listen to Aretha Franklin and Freddie Mercury and go well maybe I'm not as good
*  as them or playing the piano or whatever well I think that's it gets back to well
*  to this idea I think of the intrinsic value of making music again I think play
*  comes back you know you're not making music to be good you're making music
*  because it like enriches you and it's just you know to learn and you know
*  amateur musicianship was like a good thing you know I hope it still is to
*  learn instrument for this just because you like one you want to know you want
*  to learn you know and I think the for this year intrinsic worth of knowing how
*  to play the piano play the guitar and you know if you have a favorite song you
*  want to know to play that song are you doing this so you can you know be on
*  stage performing for thousands of people not necessarily I think that could be
*  that that that that's good too but I think if you take everything else away
*  just making music for yourself I think there's some something really awesome
*  about that I would say the same thing about making art right doing anything
*  this is something that most people don't do but it's not that hard I mean you can
*  paint you know you could well you'll paint badly compared to an expert but
*  that's okay you know the activity itself can be rewarding exactly so do you think
*  the kinds of things you're designing will help bring back the actual personal
*  creation of music to people I hope is to help people realize that there's this
*  intrinsic value to doing this and I think what they do I don't know for
*  example I don't think the apps that things I do are well certainly kind of
*  these the apps on mobile phones they're not I don't think of them as educational
*  tools at all I think of them more as like personal expression windows like
*  for people to feel you want to lower the sense of inhibition right and for people
*  to to feel this joy of making music to play like in all sense of the word play
*  an instrument but also just play the more things like laptop orchestra and
*  things like Chuck the programming language for music those are I think for
*  perhaps a different audience even though they overlap somewhat and those are more
*  I think on the on a different side of research like what kind of tools can we
*  build and what kind of instruments can we build for like laptops for orchestras
*  of laptops and humans it tell us a little bit about the laptop project it
*  was there more than one or was there yes there now they're more than I think I
*  would say probably more than 70 worldwide and most women academic
*  institutions the first one of its kind really started at Princeton and while
*  I was a grad student this is started by my advisor Perry Cook and Dan Truman
*  who's still a music professor at Princeton and they been exploring kind of
*  a really kind of how we can design instruments but also design instruments
*  that preserve some of the things we love about traditional instruments one how
*  they how they emanate sound you know if you were to play like a violin like in a
*  room the sound doesn't naturally come from a PA system it comes from the
*  artifact itself and that it's a certain sense of presence and intimacy that
*  comes with that kind of sound different concert halls have different feelings
*  right it's a feeling exactly and so they've been looking at kind of like
*  different ways to build speakers that capture the sonic intimacy and this
*  eventually led to the laptop orchestra and this started at Princeton is the
*  Princeton laptop or short work in 2005 I graduated in 2008 and started
*  Stanford and then started the Stanford laptop or or slur and the idea is that
*  for in the laptop or we have computers of course we have humans and also we
*  have these hemispherical speaker arrays now they look like the you know the dome
*  of r2d2 and they're they actually they they're made out of 11 inch diameter
*  wooden salad bowls with holes drilled into them and we put speaker drivers in
*  them and the whole idea is that we sit we pair each salad bowl with a computer
*  so that the sound that the computer is making comes out locally to where it's
*  being played and then you have that multiplied by 20 and you can really have
*  a you'll have an orchestra that can build a wall of sound but the physical
*  playing is tapping on the keyboard of the laptops it varies we to date we've
*  designed more than probably 200 different instruments and some of them
*  are tapping on the keyboard uses the mouse some of them are using things like
*  we know it's game controllers we've used this thing called the game track which
*  is like a basically it's it was made to track your hand in 3d space it was made
*  for golf games and so it's tethered to this base that's on the ground and you
*  have to wear gloves that the ends of the tethers are attached to and that
*  basically just gives you the six to your freedoms of freedom before your your two
*  hands are a little bit theremin like you can make theremins out of it yeah so you
*  can you can basically have like you can move your your arms around your hands
*  around and you can translate this gesture into sonic gestures so we anything we
*  can get our hands on we basically can can become a potential interface for
*  music making in the laptop orchestra now can I ask another unfair question is the
*  music good sometimes we'd be trying to make good music sometimes it's like we
*  always try to make music that's interesting you know that kind of
*  challenges or ask some questions about how we make music or you know this is
*  bring about kind of a different way you think about creating an instrument or
*  performing music and certainly we you know to the best of our ability we try
*  to make music that's good but the music is it that might be a matter of taste as
*  well well or is it just you know first it's remarkable you can do it at all
*  and down the road people will start putting it to more artistic uses I I
*  think it's definitely exploratory yeah we're definitely in the early stages
*  and but part of that I think has to do with the medium of the computer itself
*  you know as a thing you make instruments out of and Perry had this principles like
*  when you're designing computer music instruments often you're making the
*  piece not the instrument first and foremost okay you're kind of figuring
*  out what you want the piece that sounds exhausting every time you want to make a
*  new musical piece you have to make new instruments actually that's exactly
*  that's exactly what we end up doing is that you know we have like 200 something
*  like 200 instruments now in the laptop orchestra we have just about that many
*  that many pieces and we generally don't create general-purpose instruments that
*  can be used for a number of pieces but we were thinking about what is the
*  specific piece and what is exactly the right instrument that we can craft to
*  play that piece and so have these very specialized instruments and I think that
*  speaks to the medium of the computer it's possible in a matter of days
*  sometimes to actually have an idea and actually prototype an instrument and you
*  have a piece of music that we've never heard before and this is not supposed to
*  bring music making into people's living rooms this is just exploring a new kind
*  of music that you could imagine playing in a concert hall and people coming and
*  listening to I think that's right yeah this is a different way of thinking about
*  how to make music it's this one's left less about kind of self-expression as
*  something like Ocarina is trying to do this one's more like researching kind of
*  how we make music together with this new medium of the computer have you had to
*  bring collaborations with professional composers or musicians yeah Plork has
*  done quite a few of these and I mean Plork's played with Sakir Hussein who is
*  the amazing top of player and so percussion and they've done some amazing
*  things do they travel their tour I don't know there's a tour there was
*  definitely a few concerts a few years ago that featured them and it's it's
*  really kind of I think it's born out of curiosity it's like how do we what kind
*  of instruments are possible you know the medium is very different so you
*  probably get different instruments out of the medium and because the instrument
*  is different the music is going to be different and the way you perform so
*  it's this cascading like cause and effect you know it's designed at every
*  stage right you design one you know it's attributed to Mark Marshall McLuhan
*  that you know the we shape our tools and thereafter they shape us so the laptop
*  orchestra is it by the shaping things in every stage the end result is going
*  to be really really different well I was going to ask about the the
*  technological aspect here the role of technology it you know it seems very
*  technological if you're making a laptop orchestra or an ocarina out of an iPhone
*  but in some sense every musical instrument is technology right like
*  they've been technology all along where it I mean in what sense are we exploring
*  new music spaces because the technology is allowing us to do that well the
*  medium that first of all that's that's exactly right I every instrument is a
*  technology whether it's vibrating strings or vibrating columns of air I
*  think for computer music we're exploring the very medium of the computer itself
*  and the thing that you know sets that apart perhaps from other mediums is that
*  well one is programmable and two in some ways I think of traditional
*  you know it's really like form follows physics yes exactly and but the computer
*  you you kind of for better fours have this completely compartmentalized way of
*  thinking about instruments like what's the input what do you want it to sound
*  like those can be very different and then there's a mapping layer in the
*  middle that you map the input to the output and you can change the input
*  without changing the output vice versa in practice this doesn't always work
*  well and you want to really design everything in a more we call it a more
*  embodied kind of a way but that's kind of the difference is that this medium is
*  something that you know for better fours frees you from kind of the physics the
*  physical kind of nature of things and into kind of rules that are more
*  governed and you know more virtual realm I suppose yeah I'm interested also you
*  know how how much we can formalize this right I mean there's things you can do
*  like so now that you have a laptop when I was a kid kid I was in an
*  undergraduate this is the first laptop era right the mid 1980s IBM PCs and Macs
*  were everywhere and I definitely you know programmed our little IBM PCs to
*  make I would call them noises more than musical sounds but it's a very natural
*  thing to do so then how much once you're after you've done that can you step back
*  and say oh here are the principles I know you've mentioned Cronkberg's
*  levels laws of technology right I mean how intellectualized is this versus just
*  kind of playing around and learning things well that's a great question it
*  goes actually goes broader to this whole idea of like what design prints what
*  principles can we capture about designing things and you know in general
*  more specifically and this is where design and really computer music design
*  is is well it's it's not entirely formalizable but I think it's more
*  formalizable than like it is if you say it is right I think there's some middle
*  ground and if I were to go back to Aristotle he said something like the
*  following you know we should not expect more precision than a topic naturally
*  affords right I love that quote in your book because I was exactly thinking
*  that like you know should be is there the right answer to design but
*  Aristotle saying like no that's not the kind of thing you should be looking for
*  I think sometimes there it's valuable to say things you know generally or you
*  know in the broad sense and so design is really in this tacit dimension in
*  between like you know engineering precision and really like full
*  formalizability to kind of like there's no I think there are things we can say
*  but there are more like lenses to think with and then like recipes to follow
*  right and so you know Perry for example in computer music design had these
*  principles you know first one is like instant music subtlety later is a way to
*  think about a particular way to think about how you design instrument and you
*  know he had a coffee mug that makes music and you and you really pick it up
*  and the sensors on it enable you to start making sound and music immediately
*  but over time you can learn kind of kind of its personality the artful way to
*  drink your coffee exactly so it's so it's you know I think the principles in
*  artful design really was was inspired by kind of Perry's principle which to me
*  said that there is a level of specificity and precision but only to the
*  extent it makes it you know make sense and if we expect too much if we try to
*  formalize it too much it actually loses something of its essence I should
*  mention that there are a lot of principles in your book it's not like
*  three principles yeah at the end of the book it closes with one two three four
*  five six seven eight nine ten pages of principles with like 15 principles per
*  page so there's a lot of principles in the heart remember you remember all
*  these no but I think when a situation arises I it's sometimes it's a way to
*  think about it doesn't tell you what to do but it gives you kind of like you
*  know kind of the principle of automation you know it says that there isn't kind
*  of this membrane we can look for beyond which makes sense to automate and on the
*  other side we should really be confident about what we don't need to automate and
*  what we should we ought not automate and I think so design is as much of how to
*  automate or how not automate as it is figuring out where that little boundary
*  is and that's I think you know really a responsibility of the designer as well
*  have you worked on the automation of the composing of the music do we have
*  artificial intelligence writing scores for the laptop orchestra occasionally we
*  have had algorithmic components and generative components I think it's still
*  a pretty open problem and but also goes back to the question of meanings like why
*  do we why do we want to do that right and and if I may I remember this
*  conversation had heading to grad school and you know this this is before I went
*  to it was on my way to Princeton and and someone asked me what are you doing grad
*  school like I'm going to computer science but I'm really doing computer
*  music and say okay what do you want to do is like I want to write like the I
*  want to I want to write a program for the computer to generate to make music
*  yeah right and and that person asked me what's the point and terrible question
*  and I was like yeah that's I don't know have an answer for that and so instead of
*  actually it is actually very good question but it's a terrible question
*  it's a terrible it's a it but I think there's a it really changed the way I
*  think about things and I am really glad that person asked it because I could not
*  answer that because I think the meaning I realized that you know so instead of
*  actually building trying to build like this like the world's most like amazing
*  algorithmic composition system I went to make a tool with which others can
*  actually get their hands dirty and and build things themselves and if they want
*  to make an algorithmic composition system they can use Chuck the programming
*  language to do it so I've kind of taken one step back and designed something
*  like framed it completely or face it's a framing issue it reminds me a little bit
*  of you know in chess and go artificial intelligence not only is better than the
*  best humans but comes up with new strategies I wonder if you know Sunday
*  it's a much harder problem whether artificial intelligences won't be
*  playing music in ways that humans never thought of or you know kinds of
*  compositions we hadn't yet hit on I think I think I think it was some
*  somewhere in chapter 8 I think a fellow colleague at Stanford actually I captured
*  this moment she asked me you know what we have robot musicians you know really
*  AI that play music and I seen you mean I said you mean as well as humans it's
*  like yes and she's a philosopher so I I gave her kind of a tongue-in-cheek answer
*  which happened to believe you so I think you know the day we have robot
*  musicians is we'll have that day when we have robot philosophers right and I think
*  and she's like oh you know okay so then that means that maybe on that day the
*  AI will have understood something more subtly human and I think I think that's
*  right it's like I don't know what that really means but I think robots need to
*  Yeah. It again comes back to the question of meaning right? Well even in the very
*  most basic kind of pattern recognition tasks which computers are getting very
*  good at it's still really easy to fool them just by putting things you know
*  outside of their normal contexts right you know if you I just saw this morning
*  for some reason someone was showing a photograph of a bus on a road and you
*  ask the computer what it is and it says it's a bus but then you just like in
*  Photoshop rotate the bus 90 degrees and says oh now it's a snowplow it doesn't
*  say it's a bus of 90 degrees because it has no background framing for that. Yeah
*  and some things are hmm I mean for things like you know go or chess and
*  image recognition there are you know kind of what might be considered correct
*  answers and there are a lot of things I think in life that we value that have no
*  correct answers you know like art yeah music you know there are things that
*  are well that just aren't problems to be solved so much but things that we
*  clearly care about. Yeah. So this I mean maybe this is not a perfect segue but
*  you wrote a book and number one it's a book it's you didn't write an opera you
*  didn't write a musical piece so you chose to write a book that's a conscious
*  decision and secondly it's a graphic book right it's a but not mostly hand
*  drawn but photographs and overlay text and so forth and I notice on the cover
*  page on the title page it says that you go on are the author and designer of
*  the book so what what what made you think that a book was the right way to
*  do this after all there's so much sound in your work and there's no sound in the
*  book and then what made you think that this graphic way of doing it was the
*  right thing. That's a great question I'm still wondering that sometimes myself
*  but I'm really glad I did it this way as a photocomic book and well I think it's a
*  book about design so I felt like I kind of I really wanted to very clearly and
*  intentionally designed it and you know the medium I think you know design is
*  really how you connect the medium to the message and this and it absolutely
*  changes how you write the book so it's actually I started writing like what I
*  thought would be a more conventional book about 300 pages of words in text
*  yeah I was like it's gonna be great with some figures and I thought I
*  actually have a lot of photos I was like you know maybe just have more photos and
*  figures than than normal and then I was like you know what if there's some
*  things it's easier to talk about if it's talked about not so formally but also
*  with visual guides and also more of like kind of a you know conversation what if
*  like I don't know the pencil bag could talk you know these things suddenly you
*  know I think about comic books that I grew up with including the adventures of
*  Tintin and Chinese by the way I was born in Beijing and I was I grew up a really
*  reading Tintin and then you know it was like what if half the book was was a
*  comic book and at that point I was like you know what so and then the whole
*  thing then was this commitment to just it's like what what is this book really
*  about and now that it's and it seems to fit the idea that what you're offering
*  is not the single grand unified answers to what design is but more of a
*  invitation and a conversation and a set of ideas that work together in
*  interesting ways right that's the hope yes and the aim yeah I mean having
*  pictures of you in the book talking to us using you know thought bubbles and
*  speech balloons invites a conversational kind of response to the book yes I think
*  I wanted to make it feel like a kind of a face-to-face conversation and and now
*  I also want to feel like I'm I'm I'm there for you you know through this
*  through this like a some furnough of design and you know kind of and also I
*  think it's a way to kind of offer certain you know truths more like in a
*  more informal way and we'll have a more accessible more accessible yeah I mean
*  anyone anyone who sees a and it's not a graphic novel it's not a novel a graphic
*  text what does comic book I think I'm a person called a comic book yeah
*  comic book it's kind of an interesting genre these days I interviewed Clifford
*  Johnson who is a physicist a string theorist who did a graphic novel based
*  on physics and string theory and there's the been these famous examples of you
*  know graphic novels about philosophy history and so forth it's a growing
*  genre it sounds like I think so I mean I love comic books and one thing more I
*  can say about the foot the fact that this is a photo comic book rather than
*  like a drawn comic book is that for me like you know I want design is design
*  may reach for the sublime the subtitles like technology in search of the sublime
*  may try to reach for the transcendent but I think its feet must be grounded in
*  everyday life you know and I think the photo aspect is to say this is you don't
*  have to parse in this extra aesthetic layer of how stylistically it's drawn
*  but rather to say this is I mean it has its own aesthetic of course but these
*  moments happened and it's it's you know I think it's very different like for like
*  a comic book of spider-man probably like I prefer it to be drawn right because
*  it's it's fictional it's not and that gives me like my mind a different place
*  to go but aesthetically if it's not drawn photographs it'd be very strange
*  of like spider-man comics were photo comics because then you'd be wondering
*  who's acting as spider-man under the mask and what's the you kind of start
*  thinking about these like but here it's nonfiction right and you want to be
*  grounded you want to be real so like every thing you're describing is a thing
*  you can take a picture right right and how I mean since I'm an author I'm very
*  I'm kind of tempted now to write you know a more graphic comic booky physics book
*  but is you are the designer of the book like how does it work what is the actual
*  process are you what program are you using to make these pages I think I
*  horrified like pretty much everyone that discovered how I actually did this I did
*  this in in an old version of Omni Graffle which is an outlining program I
*  was using since grad school to make figures for my papers and I got really
*  there's nothing like familiarity with nothing like minority yeah and so every
*  page in the book and of which there are 488 and many many pages that never made
*  it into the final book right and each one of those is a separate file in in
*  Omni Graffle and I've learned to you know have like a lot of these little
*  tools of like commonly used speech bubbles and other things if I can
*  incorporate images into this kind of and I pull up those pages when I need to
*  make a page and and I've got I think I got pretty at least after a year or two
*  I got pretty fast at doing this and it really felt like this is yeah it feels
*  good I mean maybe this is an impolite to question but what does Stanford think
*  about this the university not the press that's I I think Stanford I don't know I
*  hope they like it yeah so far people have really supported me actually this
*  book was supported by both the School of Engineering and the School of Humanities
*  and Sciences which to me is like I feel like symbolically that's awesome it's
*  like this is actually this is a book that is at these intersections you know
*  it's not it's not one or the other but like another right right and was it very
*  different you know sort of in your personal experience in the sense that
*  you've been doing so much music and now you are being a visual artist in some
*  sense I've always been drawn to the visual arts and also really the
*  combination of like the audio and visual and interactive so and I've always taken
*  photographs so just kind of a hobbyist amateur photographer I guess and I mean
*  just because the audience is this is an audio podcast you can't see it but it's
*  way beyond just a set of pictures of you talking with some graphs I mean you
*  really obviously put a tremendous amount of effort into the design in terms of
*  background images and fonts and angles and things like that so it must been a
*  lot of fun it was a ton of fun it was a ton of work and there are over 1,600
*  photos in the book 1,300 of which I either took or a few of them I generated
*  and there like few drawings in there and the other came from public domain
*  Creative Commons you know and that's a shout out I rely on Wikimedia when I
*  write my books it's so good and it helps you know you in your other design work
*  even for the audio stuff you also care about the visual presentation right it's
*  all a part of you emphasize the human aspect of design and we're visual
*  creatures as much as anything else yeah I think we're trying to I think it's
*  trying for design to speak to all as much you know kind of all that we are
*  we're visual creatures we are creatures that care about aesthetics that have a
*  sense of goodness and justice and all of these things and so whatever those
*  things are that that make us who we are I think design has this you know
*  potential to address at least something you know in the aggregate hopefully all
*  of that and even an ethical dimension where do where do ethics and morality
*  come in to this so for me I think of design is like what is the function of
*  the thing and then what is everything else beyond the function of a thing in
*  an ethics fall into for me into well strange to say it's falls into kind of
*  the more of the aesthetic dimension of design if we think of design is simply
*  like what are the pragmatics and what are the aesthetics and beam as in
*  aesthetics as in everything beyond the sheer functionality and for me like I
*  think you know the ethical dimension of design is that well I think the argument
*  from the book goes you know design is all about choices you're really just
*  making like this cascading series of decisions about you know what to build
*  how you build it and who it's for and all of these things and if it's all about
*  choices then you know and these decisions you know they have implications for
*  people that use them the users and if and if that's the case then yeah making
*  decisions as engineers as designers well that's tantamount to actually taking
*  action you know anywhere else in life you know if we believe that then
*  shouldn't we as designers and engineers be held to the same moral ethical
*  framework as as we would anywhere else and so that's that's the argument and
*  then the next part of the argument is to say but that's it just is like there's
*  no recipe to be moral or ethical and in fact at least we don't agree on what the
*  right one is exactly and I think that's actually that that we don't agree is
*  why we have ethics is that we you know values come into conflict and we got to
*  try our best to apply different lenses to this to see how we can best what does
*  that even mean to resolve it right so in some sense is it like we said about
*  philosophy earlier you can't not do it you can do it badly or you can do it
*  well and likewise you can't fail to have ethical dimensions of your work when
*  you're designing things you can just pay attention to them or not that's exactly
*  right in first law of Kranzberg's law of technology technology technology is
*  neither good or bad nor is it neutral right and it has an effect and has an
*  effect and you cannot pay attention to it but it doesn't mean it doesn't you
*  know you doesn't mean it doesn't have in fact nor does that mean you're free from
*  responsibility you can't a company can't say hey we've built this platform
*  however people use it is not our problem you're not thinking many specific no
*  not in specific companies I mean certainly physicists historically have
*  done that you know we did the atomic bomb right you know and chemists chemists
*  and doctors these days are facing up against the same thing that we were
*  recording this only a week or two after it was announced that someone claims to
*  have genetically engineered a baby right and there's science there obviously but
*  there's clearly an ethical dimension as well right so I think you know for
*  engineers I think to really be not just capable engineers but actually human
*  engineers that you've got you have to consider all of these dimensions and you
*  know if you build something that's like useful makes money but you've exploited
*  people or you've done harm in the process I don't think the thing is
*  aesthetic it's not beautiful it's not truthful right and and the other thing
*  I would say is I think ethics and the world right now currently thinks of
*  ethics largely as this kind of like leash on technology but I think I would
*  I want to offer an additional way to look at I agree that there should be
*  constraints you know but what if ethics is really like values and what if those
*  values are not the leash but the foundation of what you make in the first
*  place like that should inform what you build how you build it and it's much
*  more proactive than to say we've built this thing how can we make sure it does
*  no evil right because you know the other day you know do no evil is it well that's a
*  rather low bar I mean it's a terrible thought to think like oh I can do all
*  this cool stuff if it weren't for those pesky ethics right right it's but it's
*  like but if you think about it in the other direction it's like what are my
*  values what are things I find awesome and why do I find them awesome and then
*  you you can get so excited about building something and you know you've
*  you've kind of like and the ethical considerations are kind of built in from
*  the get-go and not as this like you know checkpoint that you have to just like
*  aesthetics you can't add isn't aesthetics is not something you kind of
*  slap on at the end nor is ethics some like module you install into your system
*  just to make it ethical suddenly and it's more like that do these do these
*  different aspects do they come into your teaching at Stanford when you talk to
*  your students is this part of a course on design absolutely so I've started
*  using our full design as a textbook and in fact at some level I think was
*  written as a textbook as a very strange textbook no exercises I didn't see any
*  problem sets there are no problem sets and there there are what I called a
*  toots kind of like that people could try to do they're not yeah they're not you
* 're right they're not problem sets but they do try to put some of the ideas
*  into into motion and I'm I've designed a new course in this coming winter quarter
*  in 2019 called design that understands us and in this course we're actually
*  going to look at the shaping of technology but really in this full
*  broad spectrum per broad perspective way and in here we're going to bring to bear
*  really the aesthetic dimension the ethical dimension we're going to look at
*  everything from social network to artificial intelligence to instruments
*  to toys to games to really anything that that we find in in in our everyday
*  lives you say one of the things I mean maybe to close this up me this is a good
*  final topic the title is artful design the title of the book but then that
*  there's a subtitle technology in search of the sublime and sublime is in a
*  different color and underlined in that since you're designing it this is not
*  random choices right why is sublime the word you chose there I think I think it
*  reflects a certain optimism you know that as builders as engineers and
*  engineering itself is something that can be more than quote-unquote simply a
*  problem solver that it can be something that is beautiful truthful can be just
*  can be ethical and and I think when you talk about those things we're really
*  talking about kind of these something closer to the transcendent and for me
*  the sublime is kind of this window into looking at the transcendent you know I
*  think it's you were talking earlier about how you know at the end of your
*  books you know we are just kind of we are worth we're basically these these
*  like molecules and we're this insignificant things in this rather
*  unremarkable like in the grand scheme of things like rock and space part of a
*  solar system in this you know arm of this you know one of hundreds of
*  billions of galaxies and and beyond that who knows like what's out there and I
*  think you do you know more than I do but we we're none of us knows very much none
*  of us none of us know very much but yet we're non-zero we exist and if you think
*  about how small we are but also that we're actually here and we are
*  experiencing things I find that to be like miraculous and that gives me and
*  when I think about that that's you know it's it's sublime because it reflects
*  a certain truth but a truth that I also find incredibly beautiful well I wouldn't
*  I mean how careful should we be because you're using words like sublime and
*  transcendent and miraculous that are often associated with something beyond
*  the natural world are you you mean to imply that or is you just taking it as
*  part of the human condition that you know the human condition inner feeling
*  that is you know it's hard to articulate but we feel it right I think what's a
*  blind for me is that the natural world is is that is that this is this not is
*  just like it's insane it's like why do we why are we there's a there's a truth
*  out there that we clearly do not fully understand do you know we don't even
*  know how to frame it perhaps I mean like why are we we do not understand how we
*  come into being or if there's a purpose and that's you know and I think the
*  universe is preposterous to quote you know this is it's it's but in a really
*  horrifying terrifying but also in a just an exquisitely amazing and beautiful way
*  and I think actually you know the natural sublime is you're standing in
*  front of like this huge Canyon and you feel this both a sense of awe and this
*  twinge of fear right and well I think if you think about the universe for
*  example yeah I think I get both of those feelings it's just but it's not the kind
*  of fear that makes you run it's the kind that makes you still you know and then
*  you makes you reflect and I think technology you know back to technology in
*  the search of the sublime is getting at that same thing that I think I don't know
*  I think for me like the arts humanities fundamental you know research and
*  science it is all trying to get at in different ways is get at this like truth
*  the truth of things and both out there and also kind of in ourselves like who
*  are we and it's so human to want to understand ourselves just a little bit
*  more than before and that was actually my question for you and I don't know if
*  there's an answer for this is that I I don't really see a difference between
*  like what's out there what's in here but it both seem really hard to do and I was
*  gonna ask you like what's what's harder or is there like even that I'm I'm very
*  very quick to say that physics cosmology things like that are easier than anything
*  involving human beings because precisely the success mode of physics and cosmology
*  is that we reach for the simplest manifestations of the natural world right
*  doesn't mean they're easy in any objective sense they're still hard they
*  seem even harder than they are because we can make so much progress so quickly
*  that we're led into these abstruse realms of you know equations and
*  phenomena that our everyday life does not equip us to deal with but we can
*  still figure it out you know we figured out about physics is amazing even give
*  and how much we haven't whereas email we figure out human beings is still a
*  little bit sketchy right complex systems are the hard systems to understand and
*  as far as we know we human beings are the most complex systems in the universe
*  to date I love that you are you are a physicist philosopher humanist all of
*  that in one well go on thank you so much for this conversation this was great and
*  I was wondering if maybe we could end by you playing us out on the ocarina if
*  you have a tune ready oh yeah we don't usually have musical accompaniment but
*  yeah

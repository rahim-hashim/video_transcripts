---
Date Generated: April 09, 2024
Transcription Model: whisper medium 20231117
Length: 7153s
Video Keywords: ['TED talk', 'agi', 'ai', 'ai podcast', 'artificial intelligence', 'artificial intelligence podcast', 'consciousness', 'engineering', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'mit ai', 'robotics', 'robots', 'simone giertz']
Video Views: 346191
Video Rating: None
---

# Simone Giertz: Queen of Sh*tty Robots, Innovative Engineering, and Design | Lex Fridman Podcast #372
**Lex Fridman:** [April 16, 2023](https://www.youtube.com/watch?v=OgIo36F6Fsg)
*  It's a machine. It was my friend, Daniel Beauchamp, and we had this long-running joke
*  about a proud parent machine that you could give a quarter and it pats you on the shoulder.
*  It says, proud of you. So yeah, I still have that hanging on my wall in my workshop. So that one,
*  I'm really happy with. I just think it's a really funny concept and also I executed the build well.
*  So it's an arm? Like what's the build?
*  Yeah, I built it off of an old lamp arm. Yeah, basically it's just a motorized arm
*  and this kind of torso of a person. So it's actually a hand, right?
*  It's just laser cut plywood and it kind of has like, it looks creepy. And yeah, it says,
*  proud of you son. Because I just thought that sounded more funny than proud of you daughter
*  and also proud of you son just, it immediately communicates that it's a parent. It's not just
*  like a colleague or something. It's like proud of you. I'm trying to do a quarter for it.
*  Yeah, but he added like chat GPT on top of that and fine tune it on conversations you've had with
*  your parents and all of a sudden you have a thing that can fundamentally transform your psyche.
*  Yeah. The following is a conversation with Simone Yetch, an inventor, designer, engineer,
*  and roboticist, famous for a combination of humor and brilliant creative design in the
*  systems and products she creates, including as part of her new product design company called
*  Yetch. She has a popular YouTube channel where she has demonstrated a lot of her incredible and fun
*  designs and inventions from quote shitty robots to a Tesla Model 3 converted into a truck,
*  but where she also revealed her personal journey after having been diagnosed with a brain tumor.
*  Simone is a brilliant, fun, and inspiring human being. It was truly an honor for me to get to
*  meet her and to have this chat. This is the Lex Friedman podcast. To support it, please check
*  out our sponsors in the description. And now dear friends, here's Simone Yetch. What was the first
*  cool thing you built where you fell in love with the process of making stuff? You know, I think
*  in the beginning of building stuff, you run into the limitations of your skills so much. So I feel
*  like honestly building gets less and less frustrating or like I love it more and more,
*  the more I know. So the limitations aren't fun? Like when it's really frustrating? The limitations
*  are fun, but it's like when you have an idea of something and you want to make it a certain level
*  and then you just have to compromise with the materials and the tools and the skills you have.
*  So I can't remember first time where I felt like... I'm proud of this. Wow, this was so
*  smooth. I'm so proud of it. Like I feel like a lot of people, I watch them build stuff and it's
*  just like watching water pour down. You know, it's just like so easy. And for me, it's just like
*  trying to shove a toy car into a wall. So you're not able to step back and
*  marvel like at the early creations, even like, even like, we're not even talking
*  the Arduino stuff even before then. I'm from Sweden and you have to choose either sewing
*  or woodworking and I chose like woodworking in middle school. And I remember the sense of
*  pride when I got to bring something home and that thing of like, oh my God, I get to show my parents
*  this. And I think that is kind of the feeling that I've built my job around. It's like the sense of
*  pride and wanting to show people something that I made. And back then it was like a little wooden
*  spoon, you know, and now it's a slightly larger wooden wooden spoon. It's dynamic and moves and
*  has a mind of its own. You first started doing more engineering type stuff with Arduino boards at
*  Punch2Design, which is an SF engineering firm. What are just from your memory there, what are
*  some cool things you built there? So the thing is I went to advertising school and I just like
*  vocational studies a year. And I realized there that I didn't care much for advertising,
*  but I thought it was really fun to build stuff and program. So like, I just completely focus on
*  that. And there I built my first hardware project or like electronics project, which was this iPhone
*  case with retractable guitar strings. So basically I imagined that you could like pull out guitar
*  strings from the bottom of your iPhone and you could pluck it to your belt and then you could hold
*  a chord on the screen. And I built that together with my friend Jonathan and I was like, oh, this
*  is dope. I thought it was so much fun. And I considered like, oh, should I go to school for
*  this? But then I thought, maybe I can get a job and I could get paid to learn about electronics.
*  So just based off of that one project, I got the job at Punch2Design, which actually was
*  one year internship. Can you explain what we're talking about here? So it's a case
*  with guitar strings attached to it. Does it actually work at all?
*  It does. These are not on the screen guitar strings. No. So they're actual strings that you
*  pull out. So there's a mechanism that's almost like a seatbelt mechanism. And yeah, you pull them out
*  from the bottom of your phone and you can attach them to your belt. I mean, it's terrible. There's
*  a few different ways to decide if somebody is touching a guitar string. And what you do in a
*  real guitar is you have the little, it's like measuring the vibration or the change in the,
*  as the, yeah, you're measuring how the guitar is vibrating and you can't really do that because
*  I can't have a receiving sensor because the guitar strings are going to move in relationship
*  to that because you don't have like a rigid neck. And this is like, yeah, this was my first
*  electronics project. I was a little fledging baby maker, but what I decided was to use capacitive
*  touch because that is independent on if the guitar strings are moving in relationship to something
*  or in relation to something. So basically there was just this little Bluetooth Arduino board
*  that this company Punch Thru Design made. So that was how I found them. And I measured the capacitive
*  touch. So like whenever the guitar string was measured, there was this little microcontroller
*  that was like, oh my God, a guitar string got measured or touched. And then that sent a signal
*  over Bluetooth to my phone. And I'd built a little iPhone app that interpreted those Bluetooth
*  signals and then checked what type of chord I was holding on the screen and then played the
*  coherence. So you're holding the chords on the screen. So you're doing the multi-touch
*  sensing there. That's incredible. I honestly cannot believe that I pulled it off because I
*  think I was, I was, ignorance was definitely bliss because that was like, yeah, the first hardware
*  project I'd ever built the first iPhone app I'd ever programmed. And like now if somebody was
*  like, Hey, I want this to be my first project. I would probably be like, Oh, that's a lot, but
*  I pulled it off.
*  Because that's such an interesting thing for people to hear because it's your first project.
*  And a lot of people stop because of the difficulty of their first project. They never truly discovered
*  their own genius because they stopped at the first and you didn't stop. So it'd be interesting to
*  kind of psychoanalyze you on the couch of why you didn't stop because you have to build an app.
*  Yeah.
*  To figure out how to, did you know how to program much or no?
*  No.
*  Okay.
*  I mean a little bit, but I never programmed or done any iOS apps.
*  Okay. So you have to figure out how to get, forget like what the app does,
*  just get the app running and working. And then you have to figure out how to get the sensors
*  in like real time, the finger touching, and you have to connect how to get the capacitors touch
*  working with the microcontrollers. Do you know anything about the capacitor touch sensors
*  at that time?
*  I mean, it's pretty easy. Now it's basically-
*  Everything is easy.
*  Rockets are pretty easy.
*  You sound like my grandma. She's, I have an Italian grandma and I always trying to get her,
*  we're like trying to get her to tell her recipes and every recipe starts with,
*  it's very simple. And then there's like 45 minutes of her explaining it.
*  It's like with gymnastics at the Olympics, they make it look easy. The best people in the world
*  always make the impossible seem easy.
*  I pride myself with making buildings look really hard because I feel like I'm always
*  struggling so much.
*  You make the easy seem impossible. So how many strings was it?
*  Gosh, I mean, this is such a long time ago. No, it was six.
*  Oh, six strings and you can touch it and then there's, wow. And then the phone itself makes
*  the sound?
*  Uh-huh. And I still think it's such a cool concept to have this like mobile. I'm not even a guitar
*  player. I don't know. I was, I mean, I got the idea because I was kind of strumming on my charge
*  cord of my phone.
*  Oh, like an air guitar, but on a cord?
*  Yeah. But I've been thinking about it because I'm like, oh man, it would be really fun to
*  go back to that project with what I know now. But the problem with it is that when you're
*  producing the tension in your string just with your arm, like you can't make it taut enough to
*  actually play. Like it kind of becomes playing these like saggy strings. So as you're not really
*  getting that experience. And I think that's why, I mean, I, yeah, I haven't really pursued it.
*  I wonder if there's a way to generate the tightness from the case itself.
*  Like a device that unfolds and then with some kind of tightening mechanisms.
*  Yeah. But then it kind of becomes this like whole thing in a guitar. Then it just becomes
*  a really shitty guitar. Like, which this is a really shitty guitar, but it's also not a guitar.
*  But it's so shitty. It's awesome.
*  Yeah. I don't know.
*  But it's a cool, it's cool that you have an interface between a device that's capable of
*  incredible computational power and an actual hardware thing. Is there something that you can
*  psychoanalyze that made you finish that others could hear in their own struggle to do their
*  first project like that? Because you were not, you were in a non-engineering person, technically.
*  And you did a pretty cool renegade out there, wild, no instructions, engineering project.
*  No, it's definitely, it was an off-road build where it's like, if you're building a Lego kit,
*  it's very much on the road and you're following instructions and this is like,
*  you have no idea if you're headed for a cliff or a dead end or you're going to get stuck.
*  I think it had a natural pressure to it because it was a school project.
*  So it did have deadlines built into it and stuff like that. So that definitely helped.
*  But I think also it was just so incredibly motivating when I realized that I might be
*  able to pull it off. I felt like a bloodhound, you know? You're just like,
*  oh my God, I can actually make this happen. And I think if I hadn't seen that at the horizon,
*  it would have been harder to stick through. Were you able to see the end of the tunnel
*  pretty early on? No, not really. So there's something just suffering for a while. I don't
*  know how your brain works, but it's like, if I have a problem, I can't stop thinking about it.
*  It's so fun to think about it. I spent two and a half years designing a coat hanger
*  and I just can't stop thinking about it. I get so into it because I think it's so much fun.
*  Take me to this two-year journey of the coat hanger.
*  The coat hanger. How did it begin?
*  How did it begin? It began with a corner in my home where I couldn't fit a coat rack. The thing
*  is I shouldn't have brought this up because I'm going to release it as a product probably in a
*  year. Or an actual product. Okay. Well, that's a mystery. It's a mystery. Yeah.
*  It solves a fundamental problem in the human condition.
*  And I am so excited about it. I get so pumped about it because I see it's just this issue or
*  this problem that I want to solve and I can't put it to rest until I have.
*  Speaking of coat hangers, door knobs have always been interesting to me.
*  It's cool how there's things that everybody uses that somebody designed.
*  Lex. Yeah.
*  Oh my God. So, okay. So, I have two big... So, basically I started on YouTube and I've
*  been doing that for the last seven or eight years and I've been thinking of,
*  okay, what's next for me? Because I want to keep on trying out new things.
*  And I'm going into two different avenues. One is the product business that I started,
*  I started Coat Hangers TBD. And then I am working on a pilot episode of a show
*  where each episode is about an everyday object and why they look the way that they do. So,
*  we've written a pilot episode about forks and it's all about like, why do they look the way
*  that they do? Why did this became the eating implement of the West? Why are we ruled by an
*  iron fork? How did that happen? And every everyday object that you have and that you just take for
*  granted, somebody just made it up. Yeah. We're all sheep. We all keep using it.
*  Yeah. Even if it's not optimal. I mean,
*  presumably most objects are optimal, you hope? Or at least a local optimal.
*  Yeah. And that's what I think is so like the world around us. And this is why I love building
*  things is because it just opens up this idea that the world around us is so malleable and
*  you can make objects work for you better. Like I spent, I made this fruit bowl. I had a fruit
*  bowl and I was always annoyed that I had either too little or too much fruit for it. So I made a
*  fruit bowl where I can change the diameter of it. It has a mechanism so you can like make it bigger
*  or smaller. And that's just like the thing of being like bowls. Why are they the way that they are?
*  I can make them different. And I think like, I want to make an episode about doorknobs. I think
*  it's so interesting. Why are they the way they are? Why are they placed the way where they are?
*  I think that's going to be a rabbit hole from which you will never return.
*  I would happily live in that rabbit hole forever. Like if I could dig out a little niche for myself
*  there because I think it's like, you know, they go so deep. They're also on different sides of
*  doors. You never, like the push pull situation on doors in general, like that's one of the main
*  problems of humanity is figuring out the push pull. It is embarrassing.
*  Okay. How many? There's 8 billion people on earth. Every single second there is millions of people
*  being embarrassed by the confusion of what the push is. Real life stats. Right now there's somebody,
*  some guy first time in college is trying to be impressive to everybody who pushes on a
*  and he plays it off like it's cool. Oh shit, I knew that. No, but that's the thing. And it
*  affects our behaviors. That was why I think it's so interesting with forks is that forks actually
*  affect our eating behaviors and they can get you to eat faster or slower, take bigger bites or
*  smaller bites. And there are all these ways or like the social, I mean, the reason that chopsticks
*  work is because they do the food chopping in kitchen rather than on the plate. And also you
*  have a bowl that you bring to your mouth with, whereas a plate you keep on the, like there are
*  all these ways in these objects affect our behavior, opening and closing doors. And I think it's
*  such an interesting take on culture through and like human behavior through these objects that
*  we use every day and we never question them really. Yeah. And then there's institutions that are
*  controlling our mind that don't want us to know the truth. Why are forks not more popular? Have
*  you asked yourself that question? Yeah. No, it's all big utensil is behind all of it.
*  All right. So I mean, in those early days, did you suffer from imposter syndrome?
*  Like that leap to being an engineer was there, especially when you started working on points
*  through design on a team of engineers, was there insecurity? Both yes and no. I think I've,
*  um, I always try to flip my flaws into selling points. And for that, so getting that job, I,
*  I was like, oh, you're a team of engineers. Everybody working here is an engineer. Your
*  customers are not all engineers. You need somebody who can be your filter and tell you when something's
*  going to be too hard for your customers to understand. So it was more me being like,
*  oh no, it might seem that me not having skills is a bad thing, but actually it's a great thing.
*  I represent the everyday person. I understand deeply what everybody needs and wants.
*  Yes, that is me. The representation of the, of the average human. Um, but I mean, I, I remember
*  that. So I studied physics for a year in college and then I dropped out and I had this rule for
*  myself that whenever I did not understand any something, I would ask a question. So I was always
*  raising my hand in class and it's this room entirely like auditorium filled with incredibly
*  intelligent people who are mortified of seeming stupid. And I think that was really like, and I
*  remember people at the end of the year coming up to me and being like, thank you so much for all
*  the questions you asked, because whenever there was something that I was too scared to ask, you
*  always raised your hand. So I think it is a bit of a skill. And I think that is kind of how I channel
*  my imposter syndrome is I'm just like, no, let's lay it all out there.
*  So you're okay being almost like self-deprecating, just coming off. I mean, I'm definitely that. I
*  kind of lean into, I call myself an idiot. I lean into being stupid. I think not all heroes wear
*  capes and the guy and girl who asks the stupid question is everybody's hero, including the
*  teachers. Yeah, I think it's both. It's a double-edged sword. I started out on the internet,
*  I kind of got the moniker, the queen of shitty robots, because I posted a lot of stuff on
*  shitty robots on Reddit and people started calling me the queen of shitty robots. And then the kind
*  of dropped. So what I'm trying to say is I did not come up with that myself, but I did happily
*  adopt it. So I definitely came from a place of building things that didn't work and kind of,
*  yeah, everything going wrong every time, happily failing. And I think that was amazing. It was a
*  really powerful tool for me to not get my perfectionism in the way, because if I set out
*  to do something that's great, then I'm never going to start. And I was like, no, I just need
*  something that looks funny. But what I've realized now is there's also a defense mechanism.
*  Being self-deprecating is like always beating people to the punch. It kind of was a survival
*  tactic on the internet of being like never daring to set out as an expert. And I still do that.
*  I'm terrified to tell people how to do something, even if I know, because it kind of opens you up
*  for being shot down. So I think I definitely have a conflicted relationship with it. And now,
*  especially as I'm getting older, I am more skilled than I was before. I'm a CEO of three businesses,
*  and I'm like, I don't need to keep on talking myself down all the time. So yeah, I think it's
*  definitely something that has served me really, really well. And that is still a thing that I have
*  in my work life and in my relationships, but I'm also trying to only do it when it's beneficial
*  to me and not when it's harmful. Yeah, but when you're as successful as you are, I feel like people
*  like it when you're self-deprecating and you don't take yourself seriously, you have that humility.
*  I think it's probably the hardest when you're starting out. Yeah. I think it was easier then,
*  almost. I don't know. But nobody takes you seriously, right? When you're starting out,
*  when you're young. I just realized that I played a lot more stupid than I was. And
*  I think it's also, oh gosh, I can't believe I'm the one bringing this up. But being a woman in
*  a male-dominated field, and I was just trying to make myself the least amount threatening,
*  or really unthreatening, because people are threatened by you in different ways. And it's
*  you have such a thin line that you can walk where you're like, okay, I need to be just attractive
*  enough for people to not be offended by my appearance, but just unattractive enough for
*  people to not sexualize me. I have to be just smart and witty enough for people to be like,
*  oh my God, that's really cool. But also shoot myself down enough for other people not to be
*  able to do it or be like, oh yeah, watch this woman try to thinking that she knows how to
*  build electronics.
*  That's an interesting skill to build, especially when you put yourself out there on the internet.
*  Unfortunately, that's the reality of the internet. And it's a skill you have to kind of develop.
*  It's actually why a lot of really brilliant people avoid the internet. There's not many people,
*  like at MIT, for example, there's not many brilliant professors or PhD students and so on,
*  just putting their stuff out there. Because if they really put their heart and soul into a thing,
*  first of all, that's really hard. And nobody sees it. And everyone's like, this is boring.
*  So there's so many failure modes, like this is boring. Or like you said, you're coming off as
*  too much of an expert, you're not self-deprecating enough. Well, there's just so many failure modes
*  and it's terrifying for people. But I feel like that's a skill you should learn. Because
*  most people, like at MIT, at university and so on, are doing a lot of awesome stuff.
*  And you should show it off. But I feel like
*  you figured out a really good process of showing it off. When you fail, when you succeed, all of it,
*  not taking yourself too seriously, but also revealing through the humor and the self-deprecation,
*  a kind of genius, a kind of intelligence and curiosity.
*  I just want to snapshot that quote and put it on my LinkedIn profile.
*  On the back of your book. When is your autobiography coming out?
*  Never. You don't want to say that because like a year from now.
*  Oh, gosh. I don't want to shit on autobiographies. No.
*  No. But even just by saying that, I'm shitting on autobiographies.
*  Me being interested enough in somebody to want to read 600 pages about them talking about themselves,
*  No. Well, that's exactly the kind of person that should write one.
*  But also I'm fucking 32 years old. What do I have to write about? Like I went through puberty,
*  I lost my virginity, and here we are. Like, I don't know. It's like such a...
*  Three chapters. It's a coloring book.
*  Chapter seven. I learned to tie my own shoelaces.
*  I feel like it would be awesome. Anyway, what's the queen? So how did you achieve the status of
*  royalty? The queen of shitty robots. What's the origin story there?
*  I mean, I have officially renounced my title now.
*  Can you still speak of the time when you led? I can still speak of the time.
*  Your kingdom? Yes. No, I mean, it started on...
*  Did you rule by love or fear? By fear of rejection.
*  From me. That people would reject me. So I started making these little gifts.
*  Like the early projects that I did were very gift-forward. It was always like I only did it
*  because it could be translated into a gif. Gift-forward? I like it.
*  Yeah. But honestly, it's a really good mental exercise to vet if your project is easy enough
*  to be explained by a seven-second looping video without audio. Because nobody's going to care
*  that it also has Bluetooth. It's self-explanatory enough to be explained through a gif.
*  Just pause. I'm sorry to interrupt, but I feel like all scientific papers and projects
*  should go through that exercise. Can you explain this again?
*  Yeah. Actually, DeepMind does a good job of this. We've saw protein folding. Here's a gif.
*  That's literally what they do. Because who is going to read the nature paper?
*  So you have to ... How do we communicate this visually in a sexy, clean way where people can
*  intuitively understand even if you don't know what a protein is, even if you don't know what
*  protein folding is? Yeah. It's a cool exercise. No, it's very like, yeah, if somebody comes out
*  of context, and that's been really interesting also building this product business and trying to
*  do the marketing around that. And I'm like, if somebody comes in and they have no idea
*  about what this product is, will they get it explained to them in this ad? And I don't know.
*  But it's definitely a worthwhile exercise to do. So I started making these projects that got
*  translated into gifs, and I posted them on slash r slash shitty robots on Reddit.
*  So that's how Reddit existed? Yeah. And I loved it. I thought it was
*  really fun. And I was like, I want to contribute with content here.
*  Conquered it. I don't. I mean, I don't know.
*  I was I think I was voted top user 2015. So yeah, that's an old merit.
*  Once you win a Nobel Prize, you always have the Nobel Prize.
*  So what was the first thing? Remember the early gifts that you created?
*  So this is when I was at Punch Through Design in San Francisco. I was kind of building a lot
*  of hardware projects for them. But I also felt and they were so supportive of me. But I also
*  it's such a different way representing a brand versus representing yourself. So there were some
*  projects that I just like ruled out because I was like, it feels too weird for this brand.
*  And I started building them on the side. One of them was a toothbrush helmet. And yeah,
*  so it's like a skateboard helmet with a robot arm on the forehead, kind of like a unicorn horn.
*  And it brushes your teeth for you. Was that the first YouTube video you uploaded?
*  It was the first gif that I uploaded. So actually, I wanted to I wanted to do a kids show about
*  electronics in Sweden because I was like, I love electronics. I think it's fucking dope.
*  I could do a kids show about it. So I filmed this terrible, terrible pilot episode in my bedroom in
*  San Francisco. And that's when I built the toothbrush helmet and I emailed it to them.
*  I mean, just cold email, like I know in or anything. I was like, Hey, I want to do this.
*  And they didn't get back to me. Nobody surprised. And I was like, well, I have this
*  thing I built, I might as well post it on the internet. So that's what I made the little
*  gif and I posted it on slash r slash shitty robots. And I think it got like 50,000 views.
*  And I was like, wow. And from there, I just kept on building things. And I think within
*  six months, it was my full time job. Can you go through the detailed design of this
*  toothbrush helmet? There's a motor, like a server, like what's the motor? What's the,
*  is an Arduino involved? Yeah. So I built it off of this robot arm called me arm. So it's just this
*  acrylic robot arm and I think it has three server motors. It's all controlled by an Arduino,
*  all the electronics. It was a kit. So I assembled it. How do you make sure the,
*  the length of the arm is the proper? I mean, the arm came down. So it's like,
*  I just programmed it to come down to my mouth and then poorly brush my front teeth.
*  Yeah. Yeah. It was just swung back and forth. I mean, trial and error. What was the challenges
*  of that? Do you remember or is that one not much of a challenge? No, it was definitely a struggle.
*  So how do you loop it with a nice gift? I mean, it loops fine. Yeah. That's not that hard. No,
*  I mean, it doesn't have to be perfect. It's the gift. It's the internet. Things are shitty all
*  the time. I think, I mean, I think the biggest struggle of that was that I had this intention
*  for it to be this show and then them not giving, yeah, giving back. And I was like, well, if they
*  don't want it, then maybe YouTube will have me. They don't notice my genius yet. What was,
*  what was so bad about the pilot? Do you remember what's like the worst, most embarrassing?
*  Yeah. I mean, it's thankfully not on the internet so nobody can find it,
*  but it's very much me being in what I called host mode, which is where I'm like,
*  okay, so what we're going to learn today is that we're going to look at this. This is something
*  called a servo motor and it's like the intonation and everything is really different. And I'm
*  actually, I mean, thinking back of that, I'm so happy that they didn't get back to me because
*  it's such a different thing to kind of start your career in your living room, running back and forth
*  to the camera and like filming something and then looking at it. And like I got to really
*  find my own voice in different way. And then like a year later, they offered me a show,
*  but then I was so off and running. I was like, no, I don't want to do this.
*  You didn't fall into that place of being like a actor, like a YouTuber where you're presenting
*  a kind of personality. You're more focused on the product you're creating.
*  I mean, I think it's a combination of it. I mean, I think of it as acting sometimes,
*  but I only play the role of myself. But of course it's like when you're shooting something for the
*  seventh time, like you have to be able to muster that enthusiasm. But no, it's not a kind of,
*  think of everyday life me as a watered down version of the YouTube version. It's like,
*  that's a cheap knockoff. Yes. No, it's just like add two parts water.
*  But like on YouTube is just so condensed because you have jump cuts and you know, like
*  I'll scrape jokes and make sure that everything lands and there's music and stuff. And then like
*  in real life, you don't have any of that, but it's still me. What are some other cool robots
*  in the early days that stand out to you? I mean, there's a million we can go through, but like what
*  maybe what, what was like a challenging one, like a really challenging one in the early days?
*  I mean, I remember the breakfast robot, which was my second project was a challenging one.
*  So eating cereal. Yeah. It's a robot that like pours milk and cereal and feeds me
*  with a spoon. I was mostly challenging because it was so like everything had to be in the right
*  location. And there were so many takes before I got everything right. And by right, I mean,
*  it makes an absolute mess. Yeah. That one was challenging. How many takes was that one?
*  I don't know. Probably 12, 10 something. It's just a mess everywhere.
*  It's a mess. And also I use like Cheerios for the cereals and my, it's shot in my old bedroom in
*  San Francisco and the floors were sticky for weeks afterwards. Dude, this goes into your autobiography.
*  Yeah. It's nice. I'm just hoping we can just type out this podcast and I'll release it as a,
*  my manager would be stoked. We'll fix it in post. Yeah. The feed, cause you have like a couple of
*  feeding ones, right? The soup. Isn't there a soup one? Yeah. There's a soup robot.
*  There's a beer pouring robot. I mean, that's, that's awesome. That's a difficult robotics problem
*  in the shitty and the, in the perfect version of having an arm that interacts intimately with a
*  human being. And one of the most intimate things you could do with a human being that's PG is
*  to feed it. Where is he going with this? Oh my God. He's a YouTube comment. Come live. Damn it.
*  So like to me there's a, like feeding is tricky or even like getting a beer, even pouring a beer
*  is tough. Into a glass. Yeah. It's trickier than anyone who hasn't tried it. Thanks. And even
*  making it, I think what I realized is that like making things really shitty or like failing in a
*  spectacular way is also its own sort of skill because like the shittiest robot is the one that
*  doesn't turn on, but like that isn't much to watch. So it was always like wanting for it to fail in
*  these kinds of spectacular ways. No, there's a lot of stuff to be said about engineering in it.
*  Is there something to be said on a philosophical level about the value of a flawed robot?
*  So like the kind of robots you want is to be partially flawed. Like do you think the kind
*  of robots we'll have in the home that are friends and, you know, almost like pets, wouldn't they
*  need to be kind of shitty because we can love the, somehow we humans love the shitty. I mean,
*  it is kind of endearing and cause I think it, it kind of, I'm going to mess up this world word.
*  Anthropomorphizes them. I think it's, I mean, I never feel as deeply connected to my Roomba
*  as when it's like, I'm on a cliff. Have you had Roomba's talk? No. I really, yeah, I've done that
*  a lot when they talk to you. Yeah. And it immediately anthropomorphize them. And then you
*  have, if they have a name, which is why most roboticists don't give names or gender to robots
*  because you become connected to them. I'm of the opposite mind. You should have like an intimate
*  relationship sounds weird, but you should have a close connection to robots. I mean, there's power
*  in that. There's a social element to robotics, even an arm. I don't know. There's something about us
*  humans that gains so much value from our interaction with dynamic objects. And we should like lean into
*  that as opposed to run away from it. That was always the confusing thing to me about robotics
*  is that most roboticists run away from that. Yeah. Weird. Cause it's obviously going to be,
*  robots are obviously going to be everywhere. Yeah. Obviously. But it's also humans are sensitive and
*  squishy and there's so much liability. Oh, yeah. Yeah. But the humans are sensitive and squishy
*  when they interact with each other and they hurt each other all the time.
*  Like sometimes they get together and they're like, Oh, you're the best. You know, you're the best.
*  And then they leave each other and then they break each other's hearts. Sorry about your breakup.
*  I'm excited. I'm just trying to get over this. I'm actually drunk for this interview.
*  Haven't been able to sleep for nights. But from a safety protocol perspective,
*  people think about like physical damage, not emotional damage. I know this sounds ridiculous.
*  I know it sounds ridiculous, but it won't be. It's already happening. There's an app called
*  replica where people have an intimate relationship with an AI chat bot and they hurt themselves.
*  I was thinking about this. Yeah. Okay. In dating, what if you, cause you can train
*  like a chat bot to kind of mimic the way that you talk to people and interact with people.
*  Go on. Yeah. But then I'm like, okay, but what if we could all make AI versions of ourselves
*  and have them date like thousands and thousands of other AI people and have that as a way to turn
*  out potential candidates? Like, I feel like that's going to be, what's the, what's the, yeah.
*  What's the, what?
*  No, but what's the point of like meeting 20 people if you're like, Oh, but if we just had our AI
*  versions of ourselves interact, they'd be like, Oh, your, your method of conflict is not going to
*  match or what if the AI version of you like sleeps around with all the other AIs and it becomes
*  famous for that. And it starts this on only fans. And then it becomes, and you're like,
*  what did you do? You come back home, you'd realize like, I don't, I didn't want to create a monster,
*  create a monster. I mean, do I get it cut? Exactly. That's the question I'd be asking.
*  But I think it's definitely like, yeah, the, the human technology interaction is really interesting
*  because I feel like I don't love any of the machines that I have in my life. You haven't,
*  you haven't. I mean, I don't love my phone. I touch it all the time and it's there and it's
*  like constantly, it's a constant presence, but there's nothing in the meat that it feels like,
*  Oh, I love this object. Like I kind of despise it.
*  Well, that might be the way you show love. I don't know. That's a deeper,
*  that's another psychoanalysis thing. So you don't, there's not robots
*  whom you've taken apart that you miss?
*  No, they're all terrible. I mean, I have objects that I built that I love. None of the robots,
*  I think, but that's also because it was a different, that was a different era where I wasn't really
*  putting a lot of care into the projects I built. So the more care you put into,
*  into the design to actually make it look, to make it functional, look good. That's where
*  you put the love in. Yeah. I mean, it is, it's like, I feel like any technology company that
*  figures out a way to get you to actually genuinely love your Roomba or like love it in the way that
*  you would love a pet, there's a lot to be gained. Yeah. And I think it's scary depending on who the
*  company is because then they can manipulate you. If you love your Roomba and all of a sudden your
*  Roomba starts telling you to buy stuff or it's leaving. To put lotion on Jeff Bezos' head.
*  I don't know where the lotion came in, but yes, maybe by certain. I just imagine my Amazon Echo
*  being like, Hey, Jeff Bezos is really a great guy. But even though you haven't, do you think it's
*  possible to fall in love with a robot? Yeah. I mean, people fall in love with things all the time.
*  Well, people have fallen in love with your shitty robots, probably. I guarantee you there's people
*  listening to this that are a little bit heartbroken saying that you've never fallen
*  in love with your shitty robots. They're like, but I had a really emotional connection to that
*  robot. Like the one with it with a parent, Patsy on the back. Oh, that one. That one I do like,
*  I like that one a lot. That's probably my favorite, like shitty robot. Can you explain it?
*  So it's a machine. It was my friend, Daniel Beauchamp and I, we had this long running joke
*  about a proud parent machine that you could give a quarter and a Patsy on the shoulder. It says,
*  proud of you. So yeah, I still have that hanging on my wall in my workshop. So that one I'm really
*  happy with. I just think it's a really funny concept. And also I executed the build wall.
*  So that was, so it's an arm. Like what's the build? Yeah. Built it off of an old lamp arm.
*  Yeah. Basically it's just a motorized arm and this kind of torso of a person.
*  Well, so it's actually a hand, right? I don't remember it correctly.
*  It's like a laser cut. It's just laser cut plywood and it kind of has like,
*  it looks creepy. Yeah. Which I like. Yeah. The creepy helps with the...
*  Yeah. And yeah, it says proud of you son. Because I just thought that sounded more funny than proud
*  of you daughter. And also proud of you son just, it immediately communicates that it's a parent.
*  It's not just like a colleague or something. It's like proud of you.
*  Yeah. And it charges you a quarter for it.
*  Yeah. But he added like chat GPT on top of that and fine tune it on conversations you've had with
*  your parents. And all of a sudden you have a thing that can fundamentally transform your psyche.
*  Yeah. That's all it takes. That's a beautiful creation. How'd you come up with that creation?
*  That was my friend, Daniel and I, who had a long running joke about it.
*  High level. Can you speak to your creative process?
*  I think a lot of it, I mean, it's changed. For the shitty robot.
*  For the shitty robot. Yeah. I mean, it has a lot of overlap. So it's identifying everyday problems.
*  And in the shitty robot era, I would kind of take an everyday problem like, oh, I have a hard time
*  getting up in the morning and I would solve it in the most ridiculous, spectacular way I could think
*  of. So for waking up in the morning, it was having an alarm clock that slaps me in the face with a
*  rubber hand. And what I'm doing now is still identifying everyday problems, but I'm actually
*  trying to like product design my way out of it. What in your experience was the funniest thing?
*  Is it violence? Like the hand slapping you? Food eating? Is there, or is it just cased about it?
*  I think the funniest is, no, I think it's more like the proud parent machine. It's not violent.
*  It doesn't, there's no, nothing is just emotional and it's kind of
*  a commentary on this fraught relationship that we sometimes have with our parents and their pride of
*  us. Sometimes, every time. Sometimes. My dad visited like last week and he was like,
*  I just want to say I'm so proud of you and for the life you've built for yourself. And that was
*  really sweet. I'll put that on the back of my autobiography too. Yeah. It's not your fault,
*  Simone. It's not your fault. Some stuff is my fault. What was the longest one to complete
*  for the Shady Robots that you remember? Because you spent, on a few of them, you spent quite a long
*  time. Which is also inspiring when you take so long on a project. Yeah. I think kind of in the
*  more like fun whimsical department rather than Shady Robots, I built recently this music box
*  small music box that kind of has a barrel with little spikes and it plays a song. But I did a
*  large version of that that pops a sheet of bubble wrap and then like plays tones into a pan flute.
*  So yeah, you can actually program it to play different songs. That won't kick my butt in so
*  many creative ways and it was such a pain. I think that is probably the like weird, funny project
*  that's taken me the longest and like the biggest engineering effort. Where's the sound coming from?
*  So if you, it all came from me realizing that if you pop bubble wrap and you pop it right in front
*  of the opening of a pan flute or like one of the pipes, you can have it play different tones.
*  So that's what it does. So I built this music instrument off of that. Okay. If it's okay,
*  can you describe some, something like how it works? Some of the technical details here? Yeah. So
*  basically, I mean, one of the big issues that I had, so I worked with as of a year and a half back,
*  I hired an engineer Stu. So we were collaborating on it. But a big issue that we had was feeding in
*  the bubble wrap sheet and like making sure that it feeds in straight and doesn't get skewed because
*  you need to make like the popping feet, which is where you program this barrel to pop different
*  bubbles need to be so perfectly aligned on the bubble of the bubble wrap for it to pop in the
*  right location. So there's a feeder for the bubble wrap. That's a challenge. And then you have to
*  have a barrel with the little baby feet on it that pops the bubble wrap. Why is it so exciting?
*  That barrel was a pain as well. I had to get like this rotary setup for my CNC and yeah, it was a
*  lot of work. But that was really fun. And it's just like, this is probably my favorite privilege
*  of my job is that I can go down any rabbit hole I think find interesting. Did you have a lot of
*  joy from popping the bubbles? Yeah, that's a lot of self-soothing. And like I got to spend,
*  I think I spent a week trying to figure out the best material to pop bubble wrap with. Because
*  if you have two, if you kind of put them to through or through, if you put a sheet of bubble wrap
*  through two rigid tubes, the air kind of just escapes from one side of the bubble into the other.
*  So what I realized was that if you have a squishy material, like kind of a yoga mat material
*  in between it, it actually, it prevents that and pops it a lot more reliably.
*  So like increasing the pop reliability was a huge effort as well. You have to pop a squishy
*  thing with another squishy thing. Because you don't need a lot of force. Yeah. Like you just
*  need it to not the air to not be able to escape anywhere. Wow. But then also we had, there was
*  different qualities of bubble wrap where there was a lot of transference between different bubbles.
*  So instead of the bubble popping, it would just seep the air into a neighboring bubble and that
*  membrane would kind of, so, you know, I just like getting to spend weeks on weeks of just
*  studying bubble wrap. Did you ever think about like publishing academic work on bubble wrap?
*  No. Wouldn't that be epic? Because nobody's done this. I bet you nobody's done
*  squishing material on squishy versus squishy for popping. I bet somebody has, but you know,
*  I always, I thought I was going to go into academia. Like I was such an ambitious student
*  I loved school. I actually applied to MIT, but then I pulled out because I was like, no,
*  I don't want to do it. But now I realize it's really good that I didn't because I'm too much
*  of a spaz. Too much of a spaz. Now I'm distracted. I'm thinking there must be papers about when you
*  have two bubbles. Yeah. You need to know the physics of two bubbles. When you have two bubbles
*  colliding, one will pop first and there has to be good models of that. But that's very,
*  that has to do with chemistry and whatever the material the ball was made from. But then, no,
*  there's materials in here. There's got, somebody must understand bubble wrap deeply, like deeply.
*  So I'm just going to take a quick restroom break because Lex is on his own train now
*  and I'm just going to leave you to talk about bubble. Actually don't need to go to the restroom.
*  I'm going to insert like a two hour instructional here with like a blackboard.
*  It's the skill of a podcaster. I feel like I could throw you any topic and you could just
*  go on about it. I don't know if I have that skill. I just love bubble wrap.
*  Yeah. Okay. Bubble on bubble interaction. Go. So you did mention MIT, you went to college
*  physics for one year and you dropped out. What do you learn from that? Who do you think should
*  and shouldn't go to college? I think first of all, you shouldn't listen to me.
*  That should be the name of your autobiography. First of all, you shouldn't listen to me.
*  I, you know, I realized that I was there for the wrong reasons. I had this deep, I got completely
*  like starting to get grades in school, which in Sweden at that time we started getting it at eighth
*  grade. So when I was 14, it just kind of hijacked my brain because I realized that I could put a
*  number on how smart I was and I got obsessed with it. And I wanted to study mechanical engineering
*  because I was like, I like machines, but then physics was kind of the hardest thing you could
*  do. And I had this like deep need to prove to myself that I was smart. So I started studying
*  physics, realized I wasn't that smart. I realized, or I mean, just mostly that I like, I love math,
*  but I don't love math 10 hours a day. And also I think I am a generalist through and through,
*  like I'm decent at a fair amount of things, but definitely not a specialist in any ways. And this,
*  it was such a specialist type of area that I felt like the other parts of my brain kind of just
*  dwindled and died. So I think most of all, if people are thinking about going to college,
*  and especially if you're here in the States and it's so fucking expensive, really, okay, there's
*  two things I want to do. One is like actually go to a workplace where people are doing the job
*  that you think you want to do. If you want to become a doctor, like be at a hospital and like
*  try to see how doctors work and if you actually like it, because I feel like people have a lot
*  of ideas of what it's going to be like, and it just doesn't match with reality. And then I think
*  when people figure out what they want to do, there's kind of, that's two separate questions,
*  or there's two questions that you can split out of that. One is like, what do you actually want to do?
*  That for me, for the last 10 years is building stuff. But then there's a second part to that
*  question, which is what context do you want to do that? Do you want to build stuff at a startup or
*  a big corporation? Do you want to build stuff for an art gallery or for the movies or for YouTube?
*  And I think that's often like people only learn how to answer the first question, but then it's
*  like the context means as much. Because I was building stuff at Punch Through Design and I
*  wasn't getting that like deep fulfillment. Like I felt like I wasn't fully using myself and like
*  hitting all of my gears because I just wasn't that motivated about building stuff for other people.
*  And I changed the context and everything changed. And so sometimes you do need to consider a resume
*  and stuff like that for depending on the, but I think people consider that way too much,
*  especially in modern times. I feel like you don't need to go to college just for the resume.
*  I feel like the biggest benefit of college, I mean, there's a bunch, but one is just to do
*  hard things. But you could do hard things anywhere. But some people need to be, I was
*  probably one of those people, to be forced to do hard things. And the other is to meet fascinating
*  humans from all walks of life that have all kinds of different passions. And it allows you to learn,
*  depending on the major, you can learn generally. And you can search if you're doing it efficiently
*  about what actually inspires you. And the other thing is the resume thing. But ultimately,
*  you don't need college to find your passion to run with it.
*  I mean, I have so much college FOMO though. Like I think it's, I chose a different set of experiences.
*  And when I applied to MIT, I was, I think I was 24, because I was like, oh, maybe I should become
*  an electrical engineer, because I really liked electronics. But then I remember seeing that the
*  average age was 18. And I was like, oh, fuck, no, I can't hang out or like be in a room filled
*  with 18 year olds who are smarter than me. So I think I definitely like missed the train on having
*  that experience. But at the same time, I did so many other things and I chose other experiences
*  and I wouldn't trade them. But I still like, I mean, I'll go to on a campus and I'll be like,
*  but I think it's also because I have a dreamy idea of what it is because I never had to do
*  it and practice fully. Exactly. It's the FOMO. Yeah. Yeah. A lot of people really struggle with
*  that burden. They'll, they'll go, it doesn't matter how long you go through. If you don't go all the
*  way to the PhD, you, a lot of people have the FOMO. It doesn't, it's a silly, silly, silly little
*  notion, I think, because I think you should be doing college or school until you find something
*  that lights your heart aflame. Where you're like, fuck yes, I want to do this. Yeah. And run with
*  it. I mean, you can, you can find that in other contexts as well. I've, I found it. Yeah. But,
*  it is a buffet of experiences that you can have. What about, what was the most fun robot to make?
*  Or a musical artistic creation where the process was the most fun. Oh, they're all painful in
*  different ways. So pain. Yeah. Do you find pain fun? No, but it's definitely the pride of getting
*  to pull something off or like managing to pull something off even when it was really difficult.
*  It's very satisfying. What was the difficult thing that you pulled off? You were like, yeah,
*  this is cool. I like working on jigsaw puzzles, but I don't like how much table space they take
*  up because I like just have one big table where I can do it. And that's also my dining table.
*  So I made this mechanical table where you can switch between two tabletops. And that was an
*  incredibly painful project. And I'm really happy with the outcome and like so proud that I managed
*  to pull it off. How does it switch tabletops? It's tambor mechanism. So like tambor, like you'll
*  have on like old record player, like it's these like thin slats of wood with fabric on the back
*  and you can kind of get them to go around curves. So basically one of the tabletops or table surfaces
*  is tambor. And then there's a little crank and you can kind of roll it off to the side and it
*  reveals another tabletop under it that you can then lift up because it's on cams. So you can
*  switch between the two. I think that one was both really difficult to pull off and it's also one of
*  few projects that I use in my everyday life. Like I use it almost every day. You know what a really
*  cool one was that that was part of your Ted talk where this rotating thing that you wear on your
*  shoulders was that hard to make? So for people who haven't seen your Ted talk, they should, of course,
*  but it's a, how would you describe that? How would you call that device? Sorry,
*  I don't even know. I never used it beyond the Ted talk really. Yeah, but basically it's the
*  shoulder rig and it has this like almost like Saturn ring looking platform that goes around.
*  I can't even remember what the problem proposition was that I was trying to solve.
*  Variety probably introducing variety to your life. And this, and an element of surprise because
*  you can put popcorn as you did on it and it goes around as a little hand. Why is like a tiny hand
*  funny? I don't know, but it just slams whatever is on that thing into your face. Yeah. I don't know.
*  Was that easy to make? Yeah, that one's fine. I can't. There was, I mean, my Ted talk was so,
*  yeah, for one, once again, they cut out my best joke. What was the best joke? My best joke. They
*  didn't even ask me about it. It was, so there's this whole lead up where I built a chopping
*  machine. So it's a machine that chops vegetables and has two giant knives and it goes, and it's
*  kind of terrifying. And I show a video of it and then it ends on this gif of it chopping up a banana
*  and I'm kind of scrunching up my face being like, and the whole reason I show that project is
*  because I'm leading it up to the punchline of, oh, and as a bonus, this gif right here is the
*  perfect response if anyone ever sends you dick pics you don't want, which brought down the house.
*  It does it every time. And they cut it out without asking me because they were like, oh, but we wanted
*  people to be able to show it in classrooms. And I was like, I have abandoned the hope of being
*  shown in classrooms for years ago. That's a good joke. Thank you. That's a really good one.
*  You're okay going sometimes a little bit edgy.
*  I mean, I say that I'm crude and wholesome because I can be very crude, but I also try really,
*  really hard to be a good person and to like, I'll say shit and fucking all that stuff,
*  which I don't even think is crude. But yeah, but I really, really try to wield the power that I have
*  in a thoughtful way. So no, I wouldn't call me edgy because I'm not, I don't think it's edgy.
*  It's all like- Chopping a banana with knives
*  and saying it's a good gif response to anyone that sends you dick pics is definitely not edgy.
*  You're correct. Yeah. I think it's pretty, it's a funny joke.
*  I feel bad that they cut that. I mean, it's fine. It's like, it's a decision that I made really early
*  on where I was like, what I'm, I think often people misinterpret what I'm doing as being for
*  children, which I think is part because like my projects were always really colorful and fun.
*  I think it also has some sprinkles of sexism of being like, oh, it's a woman doing something.
*  She must be doing it for the children. And I'm like, fuck the children. I'm doing it for myself.
*  So I think I would just really early on decided of like, oh no, I'm not going to try to cater to
*  that. Which like still, I mean, I get a lot of messages from parents being like, can you please
*  stop cussing in your videos? And I'm also like, I get it. But also that is not what's going to
*  mess up your kids. I really try to be thoughtful and a decent enough role model, but I'll also
*  acknowledge that humans fuck. Yeah. It's okay. Somehow that you being able to say the F you
*  to the system. What word? Word? What? Do it. I can't. I'm scared.
*  It sounds better when you say a few. It's a dance. I should. Oh boy. Have you ever made a robot that
*  dances with you? No. Okay. You need a dance partner. I get lonely sometimes. Yeah. I feel like
*  that's the theme of this whole podcast. Yeah. What's the most embarrassed you've ever been on
*  your podcast? So I don't know if you've experienced this, but I generally embarrassed by most things
*  I say inside my head. Yeah. So like when I say something like now it's just, there's a voice
*  inside my head that goes, like what? Your disappointment. Like that the parent patting
*  in the back, the hand stops working. Yeah. Just slows down. Yeah. And then there's an awkward
*  silence. You don't know what to say next. That's really embarrassing usually. I used to work as a
*  journalist, so I know how to sit with the silence and try to drag it out of you.
*  See what I did there? You gave up. You pulled out. I quit. I was sweating. I was literally sweating.
*  Also, because you're in a full fucking suit. What is that? Like how did that come about?
*  It actually was probably MIT is because everybody was dressing in like sweatpants,
*  very chill wear. And I was like, I like taking everything seriously. It just felt like it was
*  my way of saying F you to the way things are. Cause I like, I always admire Richard Feynman.
*  I like it how there's like a classiness to it. So I don't know if it's for visual purposes,
*  but it's just how I feel when I put on a suit. It makes me feel like I'm going to take this really,
*  really seriously. And if I embarrass myself, it's all my fault. Cause I tried, there's no excuse.
*  I tried a hundred percent. The interesting thing about your Ted talk to go to a dark topic.
*  Is what happened when I walked off stage? No, what happened when you walked off stage?
*  Found out that I had a brain tumor.
*  Was that not where you're going? There's something else dark about my, yeah.
*  Well, yes. I thought you knew through the Ted talk. You found out right after.
*  I mean, the reason that I found out was partly because of the Ted talk. Cause my mom came into
*  town to be there for it. And my right eyelid was swollen and it had kind of been swelling over
*  a while. And I even got in comments about it on my YouTube channel. And I thought it was allergies
*  cause I was like, oh, it's just pollen allergies. It's just affecting my one eye. Cause maybe I
*  sleep mostly on that side. I don't know. And my mom came into the States and then Vancouver for
*  my Ted talk. And she's like, Simone, you have to like have a scan or see what's up. Well, like we
*  have to go to the doctor. And she really pushed me to do it. Cause I was like, I'm fine.
*  And I had an MRI scan on like 5 PM on a Friday night. My boyfriend at the time was there. And
*  I remember like halfway through an MRI scan, they kind of pull you out and they inject contrast
*  fluid or this like thing that yeah, just gives them another type of scan. And the nurse looked
*  at me in this way and was like, how long have you had symptoms for? And that's what I knew that
*  they'd found something. And then they like shove you back into the machine for another 20 minutes.
*  And my ex was just seeing like them like zooming in and out of my scans. And there was like this,
*  obviously something that just looked wrong in there. And they sent me to the ER and I found out
*  that I had a brain tumor the size of a golf ball that probably been grown since I was a teenager.
*  So it had been growing over like 10, 15 years. And yeah, I had surgery to remove it. And then
*  it kept on growing the parts that they couldn't remove. And I went through radiation treatment.
*  So that was like two years that just was kind of dedicated to just getting better and getting back
*  to where I am now. And I remember like, I was so stoked about 2020 because I was like, this is the
*  first year that I'm not held back by my health. And I'm like, finally going to be able to do
*  everything I've feathered. And then the pandemic happens and you're kind of like, okay,
*  just in the backseat of what's happening and things that are out of my control again.
*  In your public, you made a couple of videos about it. I have a brain tumor, my brain tumor is back.
*  You kind of, you know, you name your tumor Brian, you kind of make it a lighthearted thing.
*  But you don't reveal much of the darkness. But were you scared or some low points?
*  Of course I was scared. I mean, it's terrifying. It's like, and also when it's in your brain,
*  you know, I was like, take any other part of me, but don't take my brain.
*  No, it's this unfathomable thing that happens. And you're like, I'm healthy. How can this possibly
*  be a brain tumor? Like my eye is swollen. Like there's nothing there. I haven't had any seizures.
*  I haven't had any cognitive issues. I haven't had any headaches even. Like how is that even possible?
*  So you go through a lot of different stages of just trying to understand what it is. And I think
*  I remember being hit like right as I found out when we're in like an Uber, port Uber driver,
*  from where I had my MRI scan to the ER where they sent me. And I was really both really grateful
*  that I've gotten so much more out of life than I ever thought I would. Like I've had a hell of a
*  life. And even if it would have ended really early, I would have done so much more than I ever thought.
*  But I was also really, really sad that I hadn't had kids yet. Like that was my big grief of like,
*  fuck, I haven't had had time to have kids yet. But no, it's terrifying. I mean, the prospect of
*  somebody cutting up your head, like that's terrifying, but it honestly wasn't as bad as
*  I thought it was going to be. What about the radiation treatment? What are some things that
*  you know, people should, you learned about it, about the process and about yourself through that,
*  that people might be interested about? I think surgery was both harder and easier than radiation
*  treatment because it was harder because it was so much more intense. And it's such a dramatic thing,
*  like going to the hospital that morning and being like, I don't know, and you feel so awful when
*  you wake up. But then the recovery from it was pretty linear. Like almost every week I would get
*  a little bit better. The thing about radiation is that it was not linear at all. And it kind of
*  drained me in this weird, like it was so hard to predict. And also they put me on these,
*  I spent months feeling like I was high out of my mind and I couldn't process reality in a way that
*  I normally would. Like everything just felt off. Like I felt, yeah, I felt like I was high on drugs.
*  And I kept on asking my doctors what was going on. And they're like, no, I don't know. I don't
*  think it's anything related. And I was on this Alzheimer's medicine that they put you on to
*  prevent dementia from radiation treatment, like kind of as a preventative. And I found all these
*  subreddits of people using that Alzheimer's medicine to get high. And people be like, oh my
*  God, bro, I had like 20 milligrams yesterday and I was high out of my mind. And I'm like,
*  I'm on 30 milligrams a day. Like, of course it feels weird. And that was honestly one of the
*  scariest parts of it because that was the first time where I felt like it genuinely affected my
*  way of processing reality. And yeah, I was so relieved when I found out that that was what was
*  causing it. Cause I felt like I was going crazy. But even after surgery, like I woke up and I felt
*  like myself, like everything was, I got no brain injury. So obviously this is like my experience
*  from somebody who came out of it pretty unscathed, who didn't get any brain injuries and didn't have
*  to do any of that recovery. It's more just the recovery from like the physical act of somebody
*  cutting your skull open and taking a large chunk out. Did you research all the things that can go
*  wrong? No, no. Honestly, I'm a bit surprised by how I acted.
*  Just pausing for you to pour. You're welcome editors.
*  It's like a commercial. This is like work injury from being a YouTuber. It's all like freeze if
*  there's audio that comes in. Yeah. Sponsored by Tapwater. I was surprised by how little I was
*  willing to think critically about what my doctors told me to do. Like I very early on, the neurologist
*  that I worked with, he was the one who was on call at the ER the day where I came in. And he was the
*  one who ended up doing my surgery and he kind of became like my rock in this. And I just 100%
*  trusted him. And he turned out to be an amazing doctor and like did a great job and was just like,
*  I got so, so lucky. But I remember my mom being like, oh, but we should like talk about second
*  opinions and like we should try to do more research. And I was like so unwilling to do that
*  because opening up to the idea that there are multiple ways or multiple things that might be
*  right or wrong was so terrifying. Like I wanted there to just be like, no, this is the only option.
*  This is what we need to do. And if I started questioning that, then I don't know if I would
*  have been able to go through with it. So yeah, it was a strange, I just really wanted to trust the
*  doctors that I worked with and I was very scared to question them in any way.
*  Pete How did that process change your relationship with death? Are you afraid of death?
*  Do you ponder your mortality?
*  Beth Yeah, I think it took away a part of youth
*  for me.
*  Pete Like the innocence?
*  Beth Yeah. I mean, you kind of think of terrible things as something that happens to other people
*  and death and illness. So, I think it kind of fast tracked that for me.
*  But it mostly changed my relationship to life. It changed, it's made me so much more gentle with
*  myself. Like going through illness, it forces you to redefine what it means to be good. And before,
*  being good had been pushing myself really hard. It had been working and, I don't know,
*  just being really hard with myself and disciplined. And when you're healing from something,
*  being good is listening to your body. It's resting. It's like really being in tune with
*  what your health, where your health is at. And I think that is something that's kind of stuck
*  with me since then. I'm like so much more gentle and delicate with myself.
*  Pete And with others?
*  Beth Ah, fuck that. I think it definitely, it's like when you're young and healthy, it's really
*  hard to know what it feels like to be ill. And I remember, you know, you like go to yoga class and
*  you'd be like, oh my god, this is too slow. Like I want it to be, I have so much more energy. Like I
*  need to. And when I was recovering from my brain surgery, there was this yoga studio nearby my
*  house and they had a yoga for seniors. And I was so stoked because I was like, oh, this is the yoga
*  class I'll be able to take. And I think that was really eye opening of just like, there's no,
*  you kind of imagine that it's just like, oh, just push yourself harder. But no, that's not it.
*  With age or sickness or it's just, you got to be so gentle with yourself and you have to
*  cater to people where they're at.
*  Pete Yeah. And just appreciation of this like biological vehicle you get and you should take
*  care of it.
*  Beth Being sick sucks. It's awful. And I really, I'm really motivated to
*  postpone that for as much as I can. And also I was so tremendously grateful when I got ill
*  that I felt like I had so much to take from. Like I had so many energy reservoirs. I'd spent my life
*  taking pretty decent care of my body and like exercising and eating well and like not wrecking
*  my body in any way. And I felt like this was the first time where that was so critical. And I felt
*  like my body was ready for it, you know?
*  Pete I thought you were going to go the other way. Like you can take care of your body all you want
*  and it's, bad stuff happens. So you should go on drug binges and go wild and do crazy things.
*  Beth I mean, I also had that thought where I was like, I fucking floss every day. How do I have a
*  brain tumor? I've been good. Like, why does this happen to me? But more so it was like my body was
*  so resilient and ready for it. And I was really, really proud of it.
*  Pete It's amazing that the human body is able to recover from even the harshest things.
*  Beth Yeah, it's wild. And my brain, so after surgery, because yeah, I had a brain tumor the
*  size of a golf ball, kind of behind my right eye. And after brain surgery, you kind of just have this
*  big hole in your head, like this void. And usually your brain stays that way, like it retains the
*  shape even after the brain tumor is gone. But for some reason, my brain was feeling really ambitious
*  and it has completely flopped back. And I have almost like a normal looking brain now,
*  where doctors are like, oh, we would almost not be able to tell that you had one.
*  So yeah, that just blew my mind. I was like, when did it? Was that why I had all those headaches
*  after surgery? It was just my brain being like, ugh.
*  Pete Try, working. Yeah. Oh, pretty cool thing I want to ask you about is the everyday calendar
*  that you worked on. That was a long time. That took a long time.
*  Beth Yeah. So basically, I designed this calendar, like I wanted to start meditating every day.
*  But it's really hard to meditate every day and to like kind of build that habit. And what I would
*  do is I would make these grids in my notebooks where I could like check a box for every day.
*  Like I just wanted like a little ding, I did it. And like this thing of accountability.
*  But then I was like, I don't want to have a notebook that I do this in. Like I want an art
*  piece that I can hang on my wall, like accountability art. And I made this thing
*  called the everyday calendar, which has an entire year on it. So it's 365 days. And if you tap any
*  of the days, you light it up. And we turn it into a Kickstarter campaign. And it's now a product
*  that I'm selling through my product business, the Yacht Store.
*  Pete What's it called?
*  Beth The Yacht Store.
*  Pete Yeah. And that for people who are confused is the right way to pronounce your last name.
*  Beth Which does it. It's right, but it's so wrong. It makes my last name is spelled G-I-E-R-T-Z.
*  Pete Who does that song? If loving you is wrong, I don't want to be right.
*  Beth Yeah. I'm not pronouncing my last name yet.
*  Pete That's what makes me think. Because what's his name?
*  From the office, he covers it from the British office, which is the better office.
*  Okay. Tangent upon a tangent upon a tangent. So you said you created the everyday calendar
*  to make a more beautiful, in quotes, and more sacred gold star system on a wall.
*  Not a notebook that gets thrown into a drawer.
*  Beth Yeah. Wow. Well said past me.
*  Pete You said that making this calendar taught you a lot in quotes. I feel like a real investigative
*  journalist. You've said in 2018- Beth Yeah, I'm waiting for the gotcha.
*  Pete Can you share some of the lessons you've learned? Like what do you mean you've learned
*  a lot from making this calendar? What are we talking about?
*  Beth As somebody who builds things, manufacturing something is such an unrelated process. Like
*  making one of something and making 10,000s of something. Like they're not even distant cousins.
*  It's completely different beasts to tackle. And yeah, so that was one of it. Everything
*  takes so much longer than you think it's going to. I did a Kickstarter campaign that we launched in
*  2018 after my surgery. And yeah, it's just, you know, you think you're so generous with the
*  timelines. We still ended up being a year late, but we shipped. We're good. But yeah, I mean,
*  I'm trying to get my product business off the ground. We launched in May. And it's just, yeah,
*  it's just a pain. As somebody who's terrified of disappointing people, I'm like, why have I chosen
*  some of the jobs where it's the easiest to disappoint people?
*  You can disappoint people at scale now.
*  Yeah, I can disappoint people at scale. And also them actually haven't paid me money
*  to deliver on something, which is a terrible transaction. But it's, I'm just stoked to realize
*  that I love the job still. Like I love the product development aspect of it. I love trying to design
*  stuff for manufacturing and figure it out and like anticipate how people are going to use your
*  products. And like the everyday calendar, I mean, we've sold thousands of them now. They're all
*  over the world. And it's like people actually finding something useful that I made and
*  implementing them into their lives. It's just mind boggling.
*  Especially because this is tracking habits, good habits.
*  Or bad ones. You can do it.
*  You can use it however you want.
*  I went in a drinking binge again today.
*  Kicked another kid.
*  What does it take to mass manufacture something? What did you learn about that? Like what are,
*  can you like elucidate the gap between the one, the prototype versus the product development for
*  mass manufacture?
*  I mean, for one of it is like, yeah, the manufacturing, the tooling that they use in
*  manufacturing and to do things in a cost effective way is really different. Like I
*  can make a one off, then it's going to take me 17 hours. But obviously you can't spend 17 hours
*  for calendar when you're doing something in factory. I think it's that like quality control
*  is such a beast. You cannot trust anybody telling you that things are going to be okay. Like you're,
*  you have to have such trust issues. And it's also terrifying. I mean, as somebody who's doing
*  everything independently, I haven't raised any capital for it. Like it's all self-invested and
*  we're doing it all in house. It's just, you know, yeah, I could buy 10,000 calendars, but then what
*  if all of them are, have a manufacturing issue or, you know, it's just, it's just terrifying
*  because the risks are so high. But also I got to this point where for one, this is something that
*  I wanted to do for a long time, but something that going through health problems taught me
*  is how fragile my business model is. Because I mean, I'm basically running an influencer business
*  where I make videos on YouTube and then I have an ad spot and I talk about a brand. So like I'm a
*  human billboard, which is fine. It grants me a lot of freedom to play around. But if I am not
*  well enough to be on a stage giving talks or be in front of a camera, everything stops. Like it's
*  such a pillar of a business and it can topple over at any given moment or like YouTube could change
*  the algorithm, like legislation could catch up and change how you're able to advertise on the
*  internet. Like it's so frail and I really felt like I need to diversify what I'm doing and also
*  just to keep it interesting for myself. So what I decided was to start a product business because
*  also it's kind of this perfect combination of businesses where I can turn my YouTube channel
*  into an R and D department because I have a reason to constantly be exploring things and turning out
*  new products. I can also do that as early audience testing and see what people are actually excited
*  about. And if there's something that I think would make an interesting product, I can pass
*  that over to the product business. And then once I'm ready to market that and sell it, I can pass
*  it over to the YouTube channel. So it's like, I can kind of, once I realized that YouTube didn't
*  feel like an end goal for me, I was like, okay, then I can use it as a tool to accomplish these
*  other things that I want to do. And this was one of them. So yeah, it's a lot that went into it.
*  And one of the tools, like you said, is R and D, but it's also kind of advertisement for the
*  cool stuff that you're doing. I think Mr. Beast is one of the creators that's also
*  starting to understand this power of this reputation that you've built of like people
*  trust you, like they love you to do cool stuff. They trust that you put your heart and soul into
*  a thing. And they feel your pain and the struggle too. For example, say the everyday calendar,
*  there was issues in manufacturing or something like this. They would feel the pain of that and
*  there was still support. I mean, that's the beauty of it when you have the actual person
*  right there struggling with their lows and highs. That's a decision that I made really early on
*  where I was like, the yet store is supported by me, but it's separate from me. It's not merchandise.
*  You don't have to know who I am or care about who I am to be interested in this product.
*  And if you go on the website, yet.store, plug. I'm on the about page, yet.store. You have to go to
*  the about page to find anything about me. It's definitely not like the system of brand. And I
*  think anybody who's followed me for a long time will see that my personality is sprinkled into it,
*  but it's still clean off of me. And I think that's also because I wanted something that
*  was separate from me because I am also running out of narcissism, believe it or not. I don't
*  feel like I want to, I don't want it to be about me. And I want it to be something that can also
*  run independently of me. I want to be able to retire my face and still do the other stuff
*  because I think it's fun, but I don't want that to be the core of it. What other kind of stuff
*  have you worked on for the product design for yet?
*  So, I mean, a lot of the products, I decided to launch the store with a really small roster
*  of products because developing products is such upfront heavy, like cost-wise and just investment.
*  It's such a very big upfront investment. And I know that it would take a while,
*  or I knew it would take a while for me to kind of find the right tonality and visual language
*  for the brand. So I just wanted to launch it, have it be out there, start working on it,
*  start learning more about what it entails, even if we just had a small roster of products.
*  So we've released it with, we have a puzzle. This is just a whim, but I wanted to release a puzzle
*  that has one piece missing. So it's actually, as far as I can tell, it's the world's first
*  officially incomplete puzzle. You get 499 out of 500 pieces. I keep the 500th piece.
*  So I have a box in my workshop with everybody's missing pieces.
*  Yeah.
*  And I don't know what to do with it yet, but someday it will come to me.
*  Profound artistic statement.
*  It is something. It's definitely something. And I'm surprised by how many of them we've sold,
*  which I'm also like, I kind of wanted to have that product out there because I was like,
*  can you imagine having a pitch deck if I do ever raise money of being like,
*  you know how good I am at selling things? I sold people 5,000 incomplete puzzles.
*  Incomplete puzzles.
*  Yeah. Also have, it's like a lot of the products, I call them basket fillers. They're kind of just
*  stuff where I'm like, yeah, this is easy to throw into your basket. I mean, we have these rings,
*  I'm wearing them. So there's a screwdriver ring, which is a Phillips head screwdriver,
*  and then a screw ring that kind of has a recess, like a Phillips head screw.
*  I have these sawdust socks that make you look like your feet are covered in sawdust,
*  like you spent all day in the shop without having to put any of the actual effort in.
*  But then we have four more products in the pipeline that we're working on and that are
*  kind of the more, the big ambitious products that are more in line with what I want the brand to be.
*  The tagline is unique solutions to everyday problems. And it's just a lot of trying to
*  develop novel takes on existing products.
*  So something where the function becomes a bigger, bigger part of the design.
*  Yeah.
*  And so what's the process of creating something like that, like even the everyday calendar?
*  So like, what are some challenges that are interesting along the way? So you have to sketch
*  it out, you have to like brainstorm, draw things out, and then create a schematic and see like how,
*  how do you know what it's going to look like visually?
*  Don't. And it's, I mean, I, so the everyday content,
*  everyday calendar, the first, so I just built it for myself first. Like that did not come as a,
*  as a product idea first. And that's kind of been the process that I've had for a lot of things.
*  Like I make it for myself and then I'm like, oh, maybe other people would find this useful too.
*  So the everyday calendar, the first prototype I made, it had actually physical mechanical toggle
*  switches. So 365 toggle switches that you could flip. So if you worked out that day or meditated
*  for me was meditating, you can just flip that switch. And that was great. But when I started
*  evaluating it as a product, it's, if you have 365 of something in a product, like the runaway cost
*  is crazy. So the cheapest option, most reliable option we could find was capacitive touch.
*  So basically it's a touch interface and the front plate is a circuit board itself. So it's this like
*  the circuit board that's designed in this really fancy way. So it looks like a beautiful piece of
*  art, not to do my own work too much. But it's actually a circuit board, which I also thought
*  was really interesting of like using this, that people usually hide away in products. And it felt
*  like a nod to my career in electronics as well, being like, no, let's make it pretty. Let's make
*  it pretty. Let's make it put it front and forward. But yeah, I mean, what I'm realizing now more and
*  more is like, there's so many of like, I would love to turn the puzzle table into a product,
*  but then it's like, that would be a $7,000 table and I don't want to sell a table for $7,000. So
*  you're kind of limited to the price bracket you're in. And it's like, your margins are tough,
*  like maintaining your margins are really, really tough. And as somebody who's like,
*  I would love to sell the stuff that we're doing cheaper, but you just, it's just not feasible.
*  Like you need those margins to survive. And well, one of the genius things in the conversations
*  I've had with Elon is the ability through sort of systematic questioning of how things have been
*  done in the past to discuss what is the lowest cost way to solve a problem. And so he's very good at
*  getting to like with Optimus robot, for example, the humanoid robot, how do you get the cost down?
*  And that seems to be like one of the essential things to do. And in any product that you have
*  to mass manufacture is constantly discussed, like how do we simplify, simplify?
*  It's definitely a design limitation. It's interesting. It's both hard and interesting
*  to work within. And that's such a different thing as well. It's like, as I talked about before,
*  like what is the context and what you're creating things, like I'm still building things. I'm still
*  inventing things, but I changed the context and it has a very different set of limitations
*  and constantly trying to simplify your product to make it cheaper. And yeah, it's a really
*  interesting and different type of design process. You can lose some of the magic though, right? Like
*  people can do that a little bit too much. I think Apple is famous, like Johnny Ive is famous for
*  sort of focusing on design first and not worrying about the cost later because you don't want to
*  sacrifice. There's some stuff that's going to cost more, but it keeps some of the magic.
*  I think it's for some of the products that we're working on. It's like, I'm like, let's just make
*  it the best we think it can be. And then we can scale back from there. Like, let's not impose
*  these limitations on ourselves upfront. Like, let's just make it the most beautiful version of
*  itself. And then we can decide what we want to compromise with or compromise on. Yeah.
*  That's what I say every day when I look in the mirror.
*  And then we can compromise. Yeah.
*  And then see how shit goes wrong later. All right. Back a little bit to the robots.
*  Actually to one of your more epic projects. I mean, they're all epic, but truck. Yeah.
*  You cutting into a Tesla and turning into an epic truck. What was that like? Where did the idea
*  come from? The idea came from that I really wanted an electric pickup truck. Like I'm only
*  really driven electric because I got my driver's license pretty late and I'm like one of that
*  first generation drivers. It's like probably never going to have a gas vehicle.
*  But yeah, this was in 2018 as well. 2018 was a big year. Yeah. Or 2019. I can't remember. And I
*  I figured that we could just make our own. So you took a Tesla? Tesla Model 3. Model 3? Mm hmm.
*  And you cut off a piece of it and you turn it into a pickup truck. What's the
*  it looks pretty badass. So what are some of the challenges of doing that? It's unlike other
*  projects you've done. Yeah. It's very much outside of my realm. Like I'm not a car person. I haven't
*  worked on cars before. So we brought in a big team and had another project manager for it and
*  stuff. Because also like cars, you definitely don't want things to go wrong. Like there's no
*  part of me that wants to fuck around and make something that's going to be really unsafe for
*  me or for other people who are driving with me. So yeah, I mean, it was about a year of planning
*  and then we got the car and then we spent a month just tearing it apart and trying to make it. I
*  was so set. Like I really wanted the car just for its function. And I was like, I'm so fine with it
*  if it's really ugly. But then we managed to make it actually look really good. So that wasn't part
*  of the discussion, like how the final thing looks? I wasn't so, I wasn't that fussed about it. I was
*  like, I just want it for its function. Like I really want this car. I don't want it because
*  it looks cool. But then it ended up looking pretty cool as well. And I'm really, I mean, even now,
*  a couple of years later, when there are some more options of electric pickup trucks,
*  I still stan Trucla. Like Rivian, Ford F-150, like they're all great, but they're giant.
*  You're sitting there on a porch in your cowboy hat drinking whiskey and saying...
*  With my cattle dog.
*  I wanted like a small 90s pickup truck.
*  Back to shitty robots. You reuse parts of previous robots a lot. What's like a memorable example
*  of that? It's just the graveyard of parts in your workshop?
*  I've gotten better at keeping projects intact. In the beginning, I used to disassemble every
*  project because I was also a much more stringent budget. So if I needed a motor,
*  then I would like seal it off of an existing robot or a previous robot. But I've gotten really good
*  at not doing that now because I'm like, maybe one day I want to have a museum exhibit. And then
*  it would be nice to have all of those machines intact and not having to rebuild them.
*  Centuries from now, you can look at Benjamin Franklin's house.
*  Oh yeah, no, we're just going to look at my house.
*  Yeah, just house. Just some weird shit.
*  Yeah, that goes great with my idea of myself.
*  With the autobiography, yeah. You said that people keep requesting in the comments.
*  Did I put a dildo on it?
*  Yeah. Wait, was that actually what you were going to ask?
*  Yeah, I have dildo written in my notes.
*  I thought I just made it into a raunchy punch line. You were actually going to get there.
*  Yeah, that was in the early days in the city robot days, but now I have
*  a filter on my YouTube channel for every possible spelling of dildo.
*  I mean, people want to probably sexualize robots, right? Or they put...
*  They want to sexualize my relationship with them.
*  Oh.
*  You know, because I have majority male followers and they're so sweet and so respectful, 99%.
*  But I realize there is a lot of...
*  I realize that society hasn't taught men how to have female role models.
*  And the way that people channel it is through being like,
*  oh, it's because I want to fuck her or I want to date her or I want to marry her.
*  And I'm like, I don't think you want any of those things. I think you actually just admire my work.
*  But you don't know how to look up to a woman.
*  Yeah. That's beautifully put. What about weapons? Do you get requests to put weapons on a thing?
*  Yeah. It's interesting. I kind of started in robotics as just like a happy camper who is
*  really into tinkering. And now I'm kind of seeing some of the darker parts of it.
*  I remember first time I went to a proper factory and I saw big industrial robot arms at work.
*  And I was like, oh, wow, this is what it is about. And it was almost scary where I was like,
*  oh, I've just been playing around with these tiny versions of this. And I'm like, oh my God,
*  everybody, robotics is cool and fun. And then you get in there and you're like,
*  this is kind of terrifying.
*  You were platforming the very things that will destroy human civilization.
*  You're making it fun and entertaining.
*  I'm the mouthpiece. And I'm like getting people into robotics and engineering and we're all just
*  building our demise and accelerating speed. No, but I mean, I had that and also with
*  companies who are saying that they're never going to put weapons on their robots and then
*  have military contracts and stuff like that. And you're like, this is dark and scary.
*  Fortunately, I haven't gotten a lot of requests for it.
*  Yeah, drones are terrifying, especially.
*  Drones are fucking terrifying. And it's really everything. I mean, we're humans are so good at
*  creative ways of killing and fucking each other. It's like almost everything goes.
*  And it's, yeah, I'm terrified of the future where we are going to use more robots to kill each other.
*  And come up with new and new creative ways to kill and hurt each other.
*  Emotionally, psychologically, physically.
*  Speaking of which, what are your thoughts about, I don't know if you've been paying attention,
*  but Chad GPT, the advancement in language models and artificial intelligence.
*  Have you added speaking capabilities to any of your devices?
*  I have. I have Siri on. Yeah. I used to have an Amazon Echo in my house, but then I removed it.
*  It just freaked me out that I could whisper from my bed and it hurt me.
*  I'd be like, Alexa, please, Spotify. I'd be like, playing Spotify.
*  Yeah.
*  Fuck. I think it is a powerful tool that we are not fully ready for.
*  And I don't know. I think the internet is kind of a parade of us using
*  powerful things in harmful ways. And I think chatbots are really, really exciting. I'm
*  stoked to have a personal assistant that's like, or a virtual assistant that actually
*  does a good job and can solve problems for me. But yeah, it also feels like it can get dark really,
*  really quickly. Yeah, because you can form close connections like we're talking about with it,
*  and then it can be used to manipulate you. Manipulate you in terms of what is true
*  and manipulate you in terms of getting you to buy stuff.
*  Or maybe because at least for now, it's centralized getting everybody to think the same way.
*  It's the same in like, algorithms being used to radicalize people or kind of having that as a
*  consequence of the way that they work and combine that with a really advanced language
*  model. And you can control people's worldview in a way that you could. I mean, it's just,
*  it's wild. And I think we're not ready for it. And I don't know if we ever would be because we're
*  very impressionable little squishy flesh bags.
*  Which takes us back to when the squishy flesh bags interact, which one pops first?
*  Still on the bubble. Bubble on bubble. New paper coming out of it.
*  What were we talking about? Oh, what about consciousness? So you never anthropomorphize
*  the robots? Did they ever come to life for you? Where you kind of thought, no, because they built
*  them and I know how they work. So that prevents you from being able to see the magic. I don't know.
*  But I think it's like, I definitely, when I did a lot of the shitty robot stuff, I wanted them to
*  move like a human or like in a more organic way and not just like point A to point B,
*  just use this way to program stuff. So I wanted other people to anthropomorphize them, but I
*  don't think I did necessarily. I'm trying to think of a piece of technology that I've kind of
*  projected feelings upon, but no, I can't. So sometimes what makes me anthropomorphize
*  something, even though I built it, is there's elements of surprise. So especially with machine
*  learning, you're surprised by the kind of things it does. Have you ever been surprised by a robot?
*  No, because they're all pretty dumb. Like also the robots I built, it's like,
*  like they're all just servos moving from, I mean, they're, I don't think I've built anything with
*  a huge amount of sensors or like they're just moving in a pattern that I programmed them to move.
*  What's the most complex thing you've built? I mean, probably Trucla.
*  Trucla. Yeah, was complex just for the sheer scale of it. And like the, I mean, I think that
*  was my biggest project, both in terms of build scope, but also in terms of impact that it had.
*  Like that project just went wild. But then, yeah, then I don't know. The bubble wrap music box,
*  I don't know. They're all complicated in different ways. That one is epic. How does the bubble wrap
*  connect to the flute, by the way? How does that work? The flute is just right where, like mounted
*  right where it pops it. Okay. Yeah. That's so fascinating. I'm going to watch that video.
*  Funny enough, in my in deep investigative journalistic research of you,
*  says you're used to being an MMA reporter. How, how, how did that happen? How did you get into it?
*  I was really into martial arts. I was like a huge UFC buff. I mean, this is
*  2010 maybe. You practiced martial arts yourself?
*  I did. Yeah. I was mostly standup. I did. I did a lot of Muay Thai and then some Brazilian Jiu-Jitsu
*  and just, yeah. I was really, the thing is I get really intense about my hobbies and I was so into it.
*  I was all in and I had worked a little bit as a journalist and I was like, oh, I should like
*  do MMA reporting and I emailed this MMA website in Sweden. I was like, hey, can I come and write for
*  you? And they were like, oh, actually we're going to an event in Gothenburg tomorrow. Do you want to
*  come? Yeah. And I was like, wow, this is a lot. It's like 11 PM at night, but sure I'll come.
*  And I went there to their office. I'd never really met them. And I'm like, this is kind of scary.
*  I'm a 20 year old girl and going there in a group of men, with a group of men and they were so rude.
*  They'd like, I went there and I was like, hey, what's up? And they were all kind of ignoring me
*  and just like not looking at me or interacting with me until they realized that Simon was a girl
*  because we'd only talked over email and they're like, oh, this guy named Simon is going to come.
*  And then they were like, oh, fuck Simon. It's actually Simone and it's a girl. So I kind of
*  like slid into that in a very, very strange way. And I did that for a year, but then I got kicked
*  out of an interview with Alexander Gustafsson. And I was like-
*  Your pronunciation is so good.
*  And then I just kind of never went back and I was done with it. And now I'm not allowed to do
*  martial arts because of brain stuff. So I've kind of put all of that behind me. And it's
*  interesting. It's like, I definitely see the athleticism in it and the skill that goes into it.
*  I think as the older I get, the more concerned I am about the health impacts of the sport and
*  of the people who are practicing it on an elite level. And I'm just not as,
*  I cannot as 100% just cheer as somebody beats somebody else up into a pulp.
*  Yeah. Especially considering the effects it might have on the brain. May I ask why you got
*  kicked out? Is it because of the Gustafson interview? Is anything fun? Is it embarrassing?
*  So it was- No, it wasn't. I didn't intend to get kicked out. I didn't realize I was going to get
*  kicked out. So it was Alexander Gustafson was going to fight John Jones. And he was kind of
*  like this golden boy in Sweden. And he had just come out to the press that he had actually been
*  to jail for violent crimes. And all I wanted to ask, all I asked was what was the reason that you
*  wanted to bring that forward now? And apparently that was completely blacklisted, but I hadn't
*  gotten briefed about it at all. And the PR man, head of PR of the UFC was just yelling at me.
*  And they kicked me out of Grand Hotel in Stockholm. And I immediately called my mom and I was like,
*  mom, you will not believe what just happened. I got kicked out of an interview at Grand Hotel
*  because in the nineties, she got kicked out of an interview with Mel Gibson from the Grand Hotel.
*  So that's like Ren's in the family. So I was just like, so yeah, no, it was just this weird
*  generational skip where we both got kicked out of interviews at the same hotel.
*  You spent quite a bit of time in China as a student. Is that something you can speak to,
*  the differences and culturally, maybe even from like a student in engineering perspective between
*  China and US, maybe even Sweden, those are like technologically speaking, just such fundamentally
*  different places. I mean, I moved to China when I was 16 and I went there as an exchange student.
*  So that is before I had ever touched upon those things. And it was, and then I went back when I
*  was 19 to work as an English teacher for a little bit. It was incredibly challenging to be there.
*  The language barrier, the language, the culture. All of it. I mean, I was like,
*  now when I look at 16 year olds, I'm like, you're a baby. And I moved, sorry, 10 to 16 year olds,
*  listening to this, but like, I just can't believe I did that. And yeah, I didn't speak the language.
*  I got placed in like a small city with almost no foreigners. It was just a constant audience of
*  people staring at you because they haven't interacted with a lot of foreigners before.
*  And yeah, it definitely, and then after that I moved to Kenya.
*  And I think that was one of the reasons why it was so interesting to move to the States,
*  because people were like, oh, isn't it like hard with the language barrier or the cultural
*  difference? And I was like, dude, this is nothing. And I could speak the language,
*  or like I could speak English well, and I could kind of pass as an American, even just as I moved
*  here. And it was such a relief where I was like, wow, I'm like an undercover foreigner,
*  because I got to a point where I realized like, it doesn't matter how good my Mandarin is. I'm
*  never, people are never going to fully accept me here. So yeah.
*  And you moved, you went to Kenya, you've spoken about this after your parents got divorced.
*  Yeah. When did I talk about that? I didn't realize I told that story.
*  I know. I know so many things. What do you think this is?
*  Is it from when I have my Amazon Echo installed?
*  Yeah. I made a few context.
*  I came home from China, first time. I was there for a year.
*  It's one of the most turned upside down days of my life. I spent a year there, and I was so excited.
*  I had a really rough year. And I was so excited just to come home and like be a child again.
*  I remember thinking and just like feeling like I belonged. And then I came home and I found out
*  that my parents had separated when I was gone and they hadn't told me because they wanted to
*  like not affect my stay there, which I think was 100% the right decision of them to make.
*  But I kind of came home to a house that was starting to get picked apart.
*  And it was a big shock to your world.
*  It was both yes and no. I think I remember I just sat down on my bed and I was like,
*  well, this isn't what I expected, but I guess I'll move to Kenya because I was one of the few,
*  there were a few Swedish boarding schools in the world. There was one in Brussels, Paris, London,
*  and then one in Nairobi. And I didn't want to miss more school because I'd taken a gap
*  here when I went to China. So I was like, I guess I'll go to Nairobi. And I'm thinking now,
*  I think if my parents had stayed together, granted it was amazing that they made the
*  right decision in every way, but my roots kind of never grew back after that.
*  And I think I just kept on moving abroad and moving around and being really restless.
*  Have you ever been able to find a home spiritually?
*  I have a home. Yeah. I mean, I have a home
*  in the people around me and I have a lot of different homes. I think what I'm realizing
*  more and more is you cannot live without consequence and compromise. And sometimes I
*  can envy people who have that same friend group that they had their entire life or that just really
*  belong in a place. And I realized that would be amazing, but I've chosen different experiences.
*  And one of the upsides of that is I can feel home almost anywhere. One of the downsides of that is
*  that I cannot feel fully at home anywhere. Wow, that's deeply and darkly poetic.
*  Do you feel at home?
*  Ah.
*  Probably the way you put it is really beautifully put. Yeah. No. I have to find a home in the people
*  I love. Yeah. What advice would you give to young people?
*  That look at your stellar life, the trajectory of your career as a human being, as a creator,
*  as an engineer, as a designer, as an incredibly interesting personality
*  who's working on an autobiography. What advice would you give them? How to make their way in this
*  life? Maybe high school students, maybe college students on how to make their way in this life.
*  They can have a career they can be proud of or a life they can be proud of.
*  Oh my God, Lex. You know, this is not the advice, but there are very few moments in a career that
*  feel as good as you think they are going to. And there are very few moments of feeling really proud
*  of yourself. I feel like I often just feel like I'm not doing it well enough or big enough or,
*  I know I just had one of those moments like hearing you say that. I'm like, oh, I'm actually doing okay.
*  I think my main advice is enthusiasm is a much more potent fuel in life than duty.
*  And just because something is boring doesn't mean that it's important. I kind of realized
*  for myself that I'm so much better at the things I enjoy. But school doesn't really teach us
*  how to stay excited about something and how to stay enthusiastic about something. And if you can
*  find that, then you've got a goldmine of potential. So I kind of had to reprogram myself to be like,
*  just because this is fun doesn't mean that it's not important. Because I had so much guilt about it
*  in this weird way or where I'm like, no, this is too fun. This can't be work. And I'm like,
*  no, it's still work. The boring stuff isn't more important. And vice versa, as you said,
*  just because it's boring and hard doesn't mean it's the right thing to do. That's interesting.
*  I'm going to have to take that advice and think through it. Because genetically I'm built a little
*  bit like if this is really unpleasant, it's probably good for me. And it's a dangerous thing
*  to think. Sometimes it's true, sometimes it's not.
*  No, and it's like, what comes really easy? And where do you have that
*  effortless momentum and enthusiasm? And that is kind of the sweet spot.
*  I think that I'm also really happy that I spent time trying out so many different jobs. I've had
*  so many different jobs before I did it. And I would do things for a year and then I quit.
*  And it feels like I tried on a bunch of different pants. And you're like, okay,
*  I can kind of wear this, but they're not super comfortable or I don't love the look of them or
*  whatever. And now I feel like I found this pair of pants that just fits me perfectly. And that
*  perfectly caters to my strengths and my weaknesses. I used to work as an editor for the Swedish
*  government. And I remember thinking like, oh, I need to be okay that not a lot of things are
*  happening and that things are moving slowly and that the work is kind of like monotonous.
*  And then I realized like, or maybe I should be in a workplace where it's a benefit or strength that
*  I want a lot of things to happen and that I can handle a high speed. And I think that is really
*  such a good question to ask as well. What are my strengths? What are my weaknesses? And then what
*  context are most of these things strengths? And if you know the measurements, you can find the
*  right fitting pants. Yeah. Or the right suit, as Lex will tell you. What do you think is the meaning
*  of life? Oh, I don't think there's any meaning. It's a meaningless void? No, just that it doesn't
*  have any meaning doesn't mean that it's meaningless. I don't think that there's this big grand meaning.
*  I think a more important question is what brings you substantial joy in your life. To me,
*  it's the relationships with people that I have. Love? Yeah. I mean, love in all different kinds
*  of form. I'm really working on figuring out how to build more community, especially in a society
*  that isn't really made for it. I want more passive hangouts with people where I just want
*  people who are there. Together? To get high? No, together. To get high? Maybe together. Yeah.
*  Seeing somebody for lunch and shooting the shit and what's the latest with you is great, but what
*  I want is somebody to just roll up in sweatpants and open my fridge and be like, what are you
*  going to do? I don't know. Maybe I'll read a book. Sharing silence. Sharing silence, being alone
*  together, and just that type of community, I think, is what I'm really seeking out now.
*  I think, yeah, and also working on a goal, on a joint goal together with other people.
*  I think being a YouTuber can be really lonely. I mean, as much as I'm working with a team,
*  I just want to work in a bigger project and have that sense of, wow, we're doing this together.
*  I think that accesses my pride a lot better than just being proud of myself. It's so much easier
*  for me to be proud of a team than for me to be proud of myself. That's probably good advice for
*  people who are doing creative work on YouTube, too, to work on a team. Yeah, and just try to do
*  things. Take it from the queen of shitty robots, but try to do things with integrity, former queen
*  of shitty robots. Do things with integrity. Anything you do on the internet is kind of,
*  I think of things as tattoos on my internet and on my internet self. I'm really happy that I said
*  no to some things early in my career that I know that I would have regretted now. Just think of it
*  in the long term. Going viral is overwhelming and so stressful and so fun, but so intense.
*  I'm really happy that I managed to build that into a more long-term career than just have it
*  be something that passed. And come down from the viral moment and maintain your humanity.
*  Yeah. And also, really deliberately defining what success means to you. Because there are so many
*  reasons or so many definitions that other people will give you. Especially when you're working on
*  the internet, there are just numbers upon numbers that are like, you're doing well,
*  you're not doing well. And something I'm really happy that I did was early on, I really tried to
*  think of what does success look like for me? And I realized that it's not having the world's biggest
*  YouTube channel. It's being proud of the projects that I put out and having full say in how I spend
*  my time. That is the most important thing to me. And if I had a huge YouTube channel and I was
*  making so much money, but I kind of had this machine run me rather than the other way around,
*  to me it's so important to be able to wake up in the morning and be like,
*  I don't want to do this anymore. And for that to be okay. And I think I defined that for myself
*  early on and I've really tried to live by it and made decisions after that. And I'm really happy
*  that I did that. And also with the store, with the design you're doing now, you're putting
*  a little bit of love in the products that create a scale. I mean, that's what Johnny Ive did.
*  That's the cool thing. So you can create something beautiful and then people can share that love at
*  scale. It's terrifying and beautiful and I'm so here for it. I'm here for it too. I'm a big fan.
*  I'm a big fan of who you are. I'm a big fan of everything you do, of putting yourself out there,
*  putting your love out there in terms of the designs you create. Also just because I'm a fan
*  of robotics, I think you inspire a lot of people. I think the shitty robots are actually incredible
*  robots and it's incredible engineering. That's the best combination of design and engineering
*  and fun, all of it together. So thank you for doing that. I'm a big fan. You're an inspiration
*  and thank you for sitting down with me. This is awesome. Thank you so much for having me.
*  Thanks for listening to this conversation with Simone yetch to support this podcast. Please
*  check out our sponsors in the description. And now let me leave you with some words from Kurt
*  Vonnegut. We have to continually be jumping off cliffs and developing our wings on the way down.
*  Thank you for listening and hope to see you next time.

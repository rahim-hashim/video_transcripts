---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 6992s
Video Keywords: ['michael littman', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 94942
Video Rating: None
Video Description: Michael Littman is a computer scientist at Brown University. Please support this podcast by checking out our sponsors:
- SimpliSafe: https://simplisafe.com/lex and use code LEX to get a free security camera
- ExpressVPN: https://expressvpn.com/lexpod and use code LexPod to get 3 months free
- MasterClass: https://masterclass.com/lex to get 2 for price of 1
- BetterHelp: https://betterhelp.com/lex to get 10% off

EPISODE LINKS:
Michael's Twitter: https://twitter.com/mlittmancs
Michael's Website: https://www.littmania.com/
Michael's YouTube: https://www.youtube.com/user/mlittman

PODCAST INFO:
Podcast website: https://lexfridman.com/podcast
Apple Podcasts: https://apple.co/2lwqZIr
Spotify: https://spoti.fi/2nEwCF8
RSS: https://lexfridman.com/feed/podcast/
Full episodes playlist: https://www.youtube.com/playlist?list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4
Clips playlist: https://www.youtube.com/playlist?list=PLrAXtmErZgOeciFP3CBCIEElOJeitOr41

OUTLINE:
0:00 - Introduction
2:30 - Robot and Frank
4:50 - Music
8:01 - Starring in a TurboTax commercial
18:14 - Existential risks of AI
36:36 - Reinforcement learning
1:02:24 - AlphaGo and David Silver
1:12:03 - Will neural networks achieve AGI?
1:24:30 - Bitter Lesson
1:37:20 - Does driving require a theory of mind?
1:46:46 - Book Recommendations
1:52:08 - Meaning of life

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# Michael Littman Reinforcement Learning and the Future of AI  Lex Fridman Podcast #144
**Lex Fridman:** [December 12, 2020](https://www.youtube.com/watch?v=c9AbECvRt20)
*  The following is a conversation with Michael Litman, a computer science professor at Brown University,
*  doing research on and teaching machine learning, reinforcement learning, and artificial intelligence.
*  He enjoys being silly and lighthearted in conversation, so this was definitely a fun one.
*  Quick mention of each sponsor, followed by some thoughts related to the episode.
*  Thank you to Simply Safe, a home security company I use to monitor and protect my apartment.
*  ExpressVPN, the VPN I've used for many years to protect my privacy and the internet.
*  Masterclass, online courses that I enjoy from some of the most amazing humans in history.
*  And BetterHelp, online therapy with a licensed professional.
*  Please check out these sponsors in the description to get a discount and to support this podcast.
*  As a side note, let me say that I may experiment with doing some solo episodes in the coming month
*  or two. The three ideas I have floating in my head currently is to use one, a particular moment
*  in history, two, a particular movie, or three, a book to drive a conversation about a set of
*  related concepts. For example, I could use 2001, a space Odyssey or X Machina to talk about AGI
*  for one, two, three hours. Or I could do an episode on the, yes, rise and fall of Hitler
*  and Stalin, each in a separate episode, using relevant books and historical moments for reference.
*  I find the format of a solo episode very uncomfortable and challenging, but that just
*  tells me that it's something I definitely need to do and learn from the experience. Of course,
*  I hope you come along for the ride. Also, since we have all this momentum built up
*  on announcements, I'm giving a few lectures on machine learning at MIT this January.
*  In general, if you have ideas for the episodes, for the lectures, or for just short videos on
*  YouTube, let me know in the comments that I still definitely read, despite my better judgment,
*  and the wise sage device of the great Joe Rogan. If you enjoy this thing, subscribe on YouTube,
*  review it with five stars on our podcast, follow on Spotify, support on Patreon, or connect with me
*  on Twitter, Lex Friedman. And now here's my conversation with Michael Littman. I saw a
*  video of you talking to Charles Isbell about Westworld, the TV series. You guys were doing
*  a kind of thing where you're watching new things together, but let's rewind back. Is there a sci-fi
*  movie or book or shows that was profound, that had an impact on you philosophically,
*  or just specifically something you enjoyed nerding out about?
*  Yeah, interesting. I think a lot of us have been inspired by robots in movies. One that I really
*  like is there's a movie called Robot and Frank, which I think is really interesting because it's
*  very near-term future where robots are being deployed as helpers in people's homes. And we
*  don't know how to make robots like that at this point, but it seemed very plausible. It seemed very
*  realistic or imaginable. I thought that was really cool because they're awkward, they do funny things,
*  it raised some interesting issues, but it seemed like something that would ultimately be helpful
*  and good if we could do it right. Yeah, he was an older cranky gentleman. He was an older cranky
*  jewel thief. It's kind of a funny little thing, which is he's a jewel thief and so he pulls
*  the robot into his life, which is something you could imagine taking a home robotics thing
*  and pulling into whatever quirky thing that's involved in your existence. It's meaningful to
*  you. Exactly so. Yeah, and I think from that perspective, I mean, not all of us are jewel
*  thieves and so when we bring our robots into our lives, it explains a lot about this apartment,
*  but no, the idea that people should have the ability to make this technology their own,
*  that it becomes part of their lives. And I think it's hard for us as technologists to make that
*  kind of technology. It's easier to mold people into what we need them to be. And just that opposite
*  vision, I think, is really inspiring. And then there's an anthropomorphization where we project
*  certain things on them because I think the robot was kind of dumb, but I have a bunch of
*  Roombas that play with and you immediately project stuff onto them, much greater level
*  of intelligence. We'll probably do that with each other too. Much greater degree of compassion.
*  One of the things we're learning from AI is where we are smart and where we are not smart.
*  Yeah. You also enjoy, as people can see, and I enjoyed myself watching you sing and even dance
*  a little bit, a little bit of dancing. A little bit of dancing. That's not quite my thing.
*  As a method of education or just in life, in general. So easy question. What's the
*  definitive, objectively speaking, top three songs of all time? Maybe something that,
*  to walk that back a little bit, maybe something that others might be surprised by,
*  the three songs that you kind of enjoy. That is a great question that I cannot answer,
*  but instead let me tell you a story. Pick a question you do want to answer.
*  That's right. I've been watching the presidential debates and vice presidential debates and it turns
*  out, yeah, you can just answer any question you want. Let me interrupt you.
*  It's a related question. No, I'm sorry.
*  Yeah, well said. I really like pop music. I've enjoyed pop music ever since I was very young.
*  So 60s music, 70s music, 80s music, this is all awesome. And then I had kids and I think I stopped
*  listening to music and I was starting to realize that my musical taste had sort of frozen out.
*  And so I decided in 2011, I think, to start listening to the top 10 Billboard songs each
*  week. So I'd be on the treadmill and I would listen to that week's top 10 songs so I could
*  find out what was popular now. And what I discovered is that I have no musical taste
*  whatsoever. I like what I'm familiar with. And so the first time I'd hear a song is the first
*  week that was on the charts. I'd be like, and then the second week I was into it a little bit. And
*  the third week I was loving it. And by the fourth week is like just part of me. And so
*  I'm afraid that I can't tell you the most, my favorite song of all time,
*  because it's whatever I heard most recently. Yeah, that's interesting. People have told me
*  that there's an art to listening to music as well. And you can start to, if you listen to a song,
*  just carefully, explicitly just force yourself to really listen. You start to, I did this when I was
*  part of jazz band and fusion band in college. You start to hear the layers of the instruments. You
*  start to hear the individual instruments. You can listen to classical music or to orchestra this
*  way. You can listen to jazz this way. I mean, it's funny to imagine you now to walk in that forward
*  to listening to pop hits now as like a scholar, listening to like Cardi B or something like that,
*  or Justin Timberlake. Is he, no, not Timberlake, Bieber. They've both been in the top 10 since I've
*  been listening. They're still, they're still up there. Oh my God. I'm so cool. If you haven't
*  heard Justin Timberlake's top 10 in the last few years, there was one song that he did where the
*  music video was set at essentially NURR-IPS. Oh, wow. Oh, the one with the robotics. Yeah. Yeah.
*  Yeah. Yeah. It's like at an academic conference and he, and he's doing a demo. It was sort of
*  a cross between the Apple, like Steve Jobs kind of talk and NURR-IPS. So I, you know, it's, it's
*  always fun when AI shows up in pop culture. I wonder if he consulted somebody for that. That's
*  really interesting. So maybe on that topic, I've seen your, your, your celebrity multiple
*  dimensions, but one of them is you've done cameos in different places. I've seen you in a TurboTax
*  commercial as like, I guess the, the brilliant Einstein character. And the point is that
*  TurboTax doesn't need somebody like you. It doesn't need a brilliant person. Very few things need
*  someone like me, but yes, they were specifically emphasizing the idea that you don't need to be a
*  computer expert to be able to use their software. How'd you end up in that world?
*  I think it's an interesting story. So I was teaching my class. It was an intro computer science
*  class for non-concentrators, non-majors. And sometimes when people would visit campus,
*  they would check in to say, Hey, we want to see what a class is like. Can we sit on your class?
*  So a person came to my class who was the daughter of the brother of the husband of the best friend
*  of my wife. Anyway, basically a family friend came to campus to, to check out Brown and asked to come
*  to my class and came with her dad. Her dad is who I've known from various kinds of family events
*  and so forth. But he also does advertising. And he said that he was recruiting scientists for this,
*  this, this ad, this, this TurboTax set of ads. And he said, we wrote the ad with the idea that we get
*  like the most brilliant researchers. But they all said, no. So can you help us find the like B level
*  scientists? I'm like, sure. That's, that's who I hang out with. So that should be fine. So I put
*  together a list and I did what some people call the Dick Cheney. So I included myself on the list
*  of possible candidates, you know, with a little blurb about each one and why I thought that would
*  make sense for them to do it. And they reached out to a handful of them. But then they ultimately,
*  they YouTube stalked me a little bit and they thought, Oh, I think he could do this. And they
*  said, okay, we're going to offer you the commercial. I'm like, what? So it was, it was such an
*  interesting experience because it's, it's, they have another world, the people who do
*  like nationwide kind of ad campaigns and television shows and movies and so forth.
*  It's quite a, a remarkable system that they have going because they have a set. Yeah. So I went to,
*  it was just somebody's house that they rented in New Jersey. But in the commercial, it's just me
*  and this other woman. In reality, there were 50 people in that room and another, I don't know,
*  half a dozen kind of spread out around the house in various ways. There were people whose job it
*  was to control the sun. They were in the backyard on ladders, putting filters up to try to make sure
*  that the sun didn't glare off the window in a way that would wreck the shot. So there was like six
*  people out there doing that. There was three people out there giving snacks, the craft table.
*  There was another three people giving healthy snacks because that was a separate craft table.
*  There was one person whose job it was to keep me from getting lost. And the, I think the reason for
*  all this is because so many people are in one place at one time. They have to be time efficient. They
*  have to get it done. The morning they were going to do my commercial in the afternoon, they were
*  going to do a commercial of a mathematics professor from Princeton. They had to get it done. No,
*  you know, no wasted time or energy. And so there's just a fleet of people all working as an organism.
*  And it was fascinating. I was just the whole time just looking around like, this is so neat.
*  Like one person whose job it was to take the camera off of the cameraman so that someone else
*  whose job it was to remove the film canister. Cause every couple's takes, they had to replace
*  the film because you know, film gets used up. It was just, I don't know. I was geeking out the whole
*  time. It was so fun. How many takes did it take? It looked the opposite. Like there was more than
*  two people there. It was very relaxed. Right. Yeah. I mean, the person who I was in the scene with
*  is a professional. She's a, you know, improv comedian from New York city. And when I got there,
*  they had given me a script as such as it was. And then I got there and they said,
*  we're going to do this as improv. I'm like, I don't know how to improv. Like this is not,
*  I don't know what this, I don't know what you're telling me to do here. Don't worry. She knows.
*  Okay. Okay. We'll see how this goes. I guess, I got pulled into the story because like,
*  where the heck did you come from? I guess in the scene, like how did you show up in this
*  random person's house? I don't know. Yeah. Well, I mean, the reality of it is I stood outside in
*  the blazing sun. There was someone whose job it was to keep an umbrella over me because I started to
*  shits. I started to sweat. And so I would wreck the shot because my face was all shiny with sweat.
*  So there was one person who would dab me off at an umbrella. But yeah, like the reality of it,
*  why is this strange stalkery person hanging around outside somebody's house?
*  We're not sure when you have to look in what to wait for the book, but are you, so you make,
*  you make, like you said, YouTube, you make videos yourself, you make awesome parody sort of parody
*  songs that kind of focus in a particular aspect of computer science. How much those seem really
*  natural. How much production value goes into that? Do you also have a team of 50 people?
*  Videos, almost all the videos, except for the ones that people would have actually seen
*  were just, are just me. I write the lyrics, I sing the song. I generally find a,
*  like a backing track online because I'm, I'm like you can't really play an instrument.
*  And then I do, in some cases I'll do visuals using just like PowerPoint,
*  lots and lots of PowerPoint to make it sort of like an animation. The, the most produced one is
*  the one that people might've seen, which is the overfitting video that I did with Charles Isbell.
*  And that was produced by the Georgia Tech and Udacity people. Cause we were doing a class
*  together. It was kind of, I usually do parody songs kind of to cap off a class at the end of a class.
*  So that one you're wearing, so it was just a thriller. You're wearing the Michael Jackson,
*  the red leather jacket. The interesting thing with, with podcasting that you're also into is
*  uh, that I really enjoy is that there is not a team of people. It's kind of more, cause you know,
*  there's something that happens when there's more people involved than just one person,
*  that just the way you start acting, I don't know, there's a censorship you're not given,
*  especially for like slow thinkers like me, you're not, and I think most of us are,
*  if we're trying to actually think we're a little bit slow and careful, it kind of large teams get
*  in the way of that. And I don't know what to do with that. Like that's the, to me, like if, you
*  know, there's, it's very popular to criticize, quote unquote, mainstream media. I, but there is
*  legitimacy to criticizing them the same. I love listening to NPR for example, but every, it's
*  clear that there's a team behind it. There's a commerce, there's constant commercial breaks.
*  There's this kind of like rush of like, uh, okay, I have to interrupt you now because we have to go
*  to commercial. Just this whole, it creates, it destroys the possibility of nuanced conversation.
*  Yeah, exactly. Which Charles, uh, is both what I talked to yesterday told me that
*  Evian is naive backwards, which the fact that his mind thinks this way is just, uh,
*  it's quite brilliant. Anyway, there's a freedom to this podcast. He's Dr. Awkward, which by the way,
*  is a palindrome. That's a palindrome that I happen to know from other parts of my life. And I just,
*  you just threw it out. Well, you know, stick, use it against Charles. Dr. Awkward.
*  So what, uh, what was the most challenging parody song to make? Was it the thriller one?
*  No, that was really fun. I wrote the lyrics really quickly. Um, and then I gave it over to
*  the production team. They recruited a acapella group to sing that one. It went really smoothly.
*  It's great having a team because then you can just focus on the part that you really love,
*  which in my case is writing the lyrics. Uh, for me, the most challenging one, not challenging in a
*  bad way, but challenging in a really fun way was I did one of the, one of the parody songs I did is,
*  is about the halting problem in computer science. The, the, the fact that you can't create a program
*  that can tell for any other arbitrary program, whether it actually going to get stuck in an
*  infinite loop or whether it's going to eventually stop. And so I, I did it to an 80 song because
*  that's, I hadn't started my, my new thing of learning current songs. And it was Billy Joles,
*  the piano man, which is a great song. Yeah. And sing me a song. You get the piano man. Yeah.
*  Yeah. So the lyrics are great because first of all, it rhymes, uh, not all songs rhyme. I did,
*  I've done Rolling Stone songs, which turn out to have no rhyme scheme whatsoever. They're just
*  sort of yelling and having a good time, which it makes it not fun from a parody perspective.
*  Cause like you can say anything, but this, you know, the lines rhyme and there was a lot of
*  internal rhymes as well. And so figuring out how to sing with internal rhymes, a proof of the
*  halting problem was really challenging. And, uh, it was, I really enjoyed that process.
*  What about, uh, last question on this topic, what about the dancing in the thriller video? How many
*  takes that take? So I wasn't planning to dance. They, they had me in the studio and they gave me
*  the jacket and it's like, well, you can't, if you have the jacket and the glove, like there's not
*  much you can do. So I, um, I think I just danced around and then they said, why don't you dance a
*  little bit? We, we, there was a scene with me and Charles dancing together. They did not use it in
*  the video, but we recorded it. Um, yeah, yeah, no, it was, it was pretty funny. And Charles, who has
*  this beautiful, wonderful voice, doesn't really sing. He's not really a singer. And so that was
*  why I designed the song with him doing a spoken section and me doing the singing. It's very like
*  Barry White. Yeah. It was awesome. So one of the other things Charles said is that, you know,
*  everyone knows you as like a super nice guy, super passionate about teaching and so on. Uh,
*  what he said, don't know if it's true that despite the fact that you're, you are,
*  okay, I will admit this finally for the first time that was, that was me. It's the Johnny Cash song.
*  It was a man, Reno, just to watch him die, uh, that you actually do have some strong opinions
*  and some topics. So if this in fact is true, what, uh, strong opinions would you say you have?
*  Is there ideas you think maybe an artificial intelligence and machine learning, maybe in life
*  that you believe is true that others might, you know, some number of people might disagree with
*  you on? So I try very hard to see things from multiple perspectives. There's, there's this
*  great Calvin and Hobbes, Calvin and Hobbes cartoon where Cal, do you know? Okay. So Calvin's dad is
*  always kind of a bit of a foil and he, he, he talked Calvin into, Calvin had done something
*  wrong. The dad talks him into like seeing it from another perspective and Calvin, like this breaks
*  Calvin because he's like, Oh my gosh, now I can see the opposite sides of things. And so the,
*  it's, it becomes like a Cubist cartoon where there is no front and back, everything's just exposed.
*  And it really freaks him out. And finally he settles back down. It's like, Oh good, no,
*  I can make that go away. But like, I'm that, I'm that, I live in that world where I try,
*  I'm trying to see everything from every perspective all the time. So there are some
*  things that I've formed opinions about that I would be harder, I think, to disavow me of.
*  One is, um, the super intelligence argument and the existential threat of AI is one where I feel
*  pretty confident in my feeling about that one. Like I'm willing to hear other arguments, but like
*  I am not particularly moved by the idea that if we're not careful, we will accidentally create
*  a super intelligence that will destroy human life. Let's talk about that. Let's get you in
*  trouble and record your video. It's like, it's like, it's like Bill Gates, uh, I think he said
*  like some quote about the internet, that that's just gonna be a small thing. It's not gonna really
*  go anywhere. And then I think Steve Ballmer said, uh, I don't know why I'm sticking on Microsoft.
*  Uh, that's something that like smartphones are useless. There's no reason why Microsoft should
*  get into smartphones that kind of, so let's get, let's talk about a GI as a GI is destroying the
*  world. We'll look back at this video and see. No, uh, I think it's really interesting to actually
*  talk about it because nobody really knows the future. So you have to use your best intuition.
*  It's very difficult to predict it, but you have spoken about a GI and the existential risks
*  around it and sort of based on your intuition that we're quite far away from that being a serious
*  concern relative to the other concerns we have. Can you maybe unpack that a little bit? Yeah,
*  sure, sure, sure. So, so as, as I understand it, the, uh, for example, I read Boston's book
*  and a bunch of other reading material about this sort of general way of thinking about the world.
*  And I think the story goes something like this, that we will at some point create computers that
*  are smart enough that they can help design the next version of themselves,
*  which itself will be smarter than the previous version of themselves. And eventually bootstrapped
*  up to being smarter than us, at which point we are essentially at the mercy of this sort of
*  more powerful intellect, which in principle, uh, we don't have any control over what its goals are.
*  And so if its goals are at all out of sync with our goals, like the, for example, the continued
*  existence of humanity, we won't be able to stop it. It'll be way more powerful than us and we will
*  be toast. So there's some, I don't know, very smart people who have signed on to that story.
*  And it's a, it's a compelling story. I, I want to, now I can really get myself in trouble. I once
*  wrote an op-ed about this specifically responding to some quotes from Elon Musk, who has been,
*  you know, on this very podcast, uh, more than once and AI summoning the demon.
*  I forget. But then he came to Providence, Rhode Island, which is where I live and said, uh,
*  to the governors of all the states, uh, you know, you're worried about entirely the wrong thing.
*  You need to be worried about AI. You need to be very, very worried about AI. So, uh, and
*  journalists kind of reacted to that and they wanted to get people's, people's take. And I was
*  like, okay, my, my, my belief is that one of the things that makes Elon Musk so successful and so
*  remarkable as an individual is that he believes in the power of ideas. He believes that you can have,
*  you can, if you know, if you have a really good idea for getting into space, you can get into
*  space. If you have a really good idea for a company or for how to change the way that people
*  drive, you just have to do it and it can happen. It's really natural to apply that same idea to AI.
*  You see these systems that are doing some pretty remarkable computational
*  tricks, uh, demonstrations, and then to take that idea and just push it all the way to the
*  limit and think, okay, where does this go? Where is this going to take us next? And if you're a
*  deep believer in the power of ideas, then it's really natural to believe that those ideas could
*  be taken to the extreme and kill us. So I think, you know, his strength is also his
*  undoing because that doesn't mean it's true. Like it doesn't mean that that has to happen,
*  but it's natural for him to think that. So another way to phrase the way he thinks, and
*  I find it very difficult to argue with that line of thinking. Uh, so Sam Harris is another person
*  from a neuroscience perspective that things like that is saying, well, is there something fundamental
*  in the physics of the universe that prevents this from eventually happening? And that's the Nick
*  Bostrom thinks in the same way that kind of zooming out. Yeah. Okay. We humans now, uh,
*  are existing in this like time scale of minutes and days. And so our intuition is in this time
*  scale of minutes, hours and days. But if you look at the span of human history, is there any reason
*  we, you can't see this in a hundred years and like, is there, is there something fundamental
*  about the laws of physics that prevent this? And if it doesn't, then it eventually will happen
*  or we'll, we will destroy ourselves in some other way. And it's very difficult. I find to actually
*  argue against that. Yeah. Uh, and not sound like, not sound like you're just like rolling your ass.
*  Uh, like I have like science fiction, we don't have to think about it, but even, even worse than that,
*  which is like, I don't know if kids, but like, I got to pick up my kids now. Like this, okay.
*  I see more pressing short. Yeah. There's more pressing short term things that like, uh, stop
*  over this existential crisis. We have much, much shorter things like now, especially this year,
*  there's COVID. So like any kind of discussion like that is like, there's, there's, you know,
*  there's pressing things today. It's, it's, and then sort of the Sam Harris argument. Well, like any day
*  the exponential singularity can, can occur is very difficult to argue against. I mean, I don't know.
*  But part of his story is also, he's, he's not going to put a date on it. It could be in a thousand
*  years. It could be in a hundred years. It could be in two years. It's just that as long as we keep
*  making this kind of progress, it's ultimately has to become a concern. I kind of, I'm on board with
*  that, but the thing that the piece that I feel like is missing from that, that way of extrapolating
*  from the moment that we're in is that I believe that in the process of actually developing
*  technology that can really get around in the world and really process and, and, and, and do
*  things in the world in a sophisticated way, we're going to learn a lot about what that means,
*  that we don't know now, because we don't know how to do this right now. If you believe that you can
*  just turn on a deep learning network and eventually give it enough compute and it'll eventually get
*  there. Well, sure. That seems really scary because we won't, we won't be in the loop at all. We
*  won't, we won't be helping to design or, or target these kinds of systems, but I don't, I don't see
*  that, that feels like it is against the laws of physics because these systems need help, right?
*  They need to surpass the, the difficulty, the wall of complexity that happens in arranging
*  something in the form that that will happen. Yeah. Like I believe in evolution. Like I believe that
*  the, that, that there's an argument, right? So there's another argument, just to look at it from
*  a different perspective, that people say, well, I don't believe in evolution. How could evolution,
*  it's, it's sort of like a random set of parts, assemble themselves into a 747 and that could just
*  never happen. So it was like, okay, that's maybe hard to argue against, but clearly 747s do get
*  assembled. They get assembled by us. Basically the idea being that there's a process by which we will
*  get to the point of making technology that has that kind of awareness. And in that process,
*  we're going to learn a lot about that process and we'll have more ability to control it or to shape
*  it or to build it in our own image. It's not something that is going to spring into existence
*  like that 747 and we're just going to have to contend with it completely unprepared.
*  That's very possible that in the context of the long arc of human history, it will in fact spring
*  into existence, but that's, that's springing might take, like, if you look at nuclear weapons,
*  like even 20 years is a springing in the context of human history. And it's very possible, just
*  like with nuclear weapons that we could have, I don't know what percentage you want to put at it,
*  but the possibility of could have knocked ourselves out. Yeah. The possibility of human
*  beings destroying themselves in the 20th century with nuclear weapons. I don't know. You can,
*  if you really think through it, you could really put it close to like, I don't know, 30, 40%
*  given like the certain moments of crisis that happened. So like, I think one,
*  like fear in the shadows that's not being acknowledged is this not so much the AI will
*  run away is, is that as it's running away, we won't have enough time to think through
*  how to stop it. Right. Fast takeoff or foom. Yeah. I mean, my much bigger concern,
*  I wonder what you think about it, which is we won't know it's happening. So I kind of
*  heard that argument. Yeah. I think that there's an AGI situation already happening with social media
*  that our minds, our collective intelligence of human civilization is already being controlled
*  by an algorithm. And like we're, we're already super like the level of a collective intelligence
*  thanks to Wikipedia, people should donate to Wikipedia to feed the AGI. Man, if we had a
*  super intelligence that, that was in line with Wikipedia's values, that it's a lot better than a
*  lot of other things I can imagine. I trust Wikipedia more than I trust Facebook or YouTube as far as
*  trying to do the right thing from a rational perspective. Yeah. Now that's not where you were
*  going. I understand that, but it does strike me that there's sort of smarter and less smart ways of
*  exposing ourselves to each other on the internet. Yeah. The interesting thing is that Wikipedia
*  and social media have very different forces. You're right. I mean, Wikipedia, if AGI was
*  Wikipedia, it'd be just like this cranky overly competent editor of articles. You know, there's
*  something to that, but the social media aspect is, is, is not. So the vision of AGI is, is as a
*  separate system that's super intelligent, that's super intelligent. That's one key little thing.
*  I mean, there's the paperclip argument that's super dumb, but super powerful systems. But with
*  social media, you have a relatively like algorithms we may talk about today, very simple algorithms
*  that when, uh, so something Charles talks a lot about, which is interactive AI, when they start
*  like having at scale, like tiny little interactions with human beings, they can start controlling
*  these human beings. So a single algorithm can control the minds of human beings slowly to what
*  we might not realize. It could start wars. It could start, it could change the way we think about
*  things. It feels like in the long arc of history, if I were to sort of zoom out from all the outrage
*  and all the tension on social media, that it's progressing us towards, uh, better and better
*  things. It feels like chaos and toxic and all that kind of stuff, but it's chaos and toxic. Yeah. But
*  it feels like actually the chaos and toxic is similar to the kind of debates we had from the
*  founding of this country. You know, there was a civil war that happened over that, over that
*  period. And ultimately it was all about this tension of like, something doesn't feel right
*  about our implementation of the core values we hold as human beings. And they're constantly
*  struggling with this. And that results in people calling each other, uh, like just, just being
*  shitty to each other on Twitter. But I, ultimately the algorithm is managing all that. And it feels
*  like there's a possible future in which that algorithm controls us to, into the direction of
*  self-destruction and whatever that looks like. Yeah. So, so, all right. I do believe in the power
*  of social media to screw us up royally. I do believe in the power of social media to benefit
*  us too. I do think that we're in a, yeah, it's sort of almost got dropped on top of us and now
*  we're trying to, as a culture, figure out how to cope with it. There's a sense in which,
*  I don't know, there's, there's some arguments that say that, for example, uh, I guess college
*  age students now, late college age students now, people who were in middle school when,
*  when social media started to really take off, maybe, maybe really damaged. Like this may have
*  really hurt their development in a way that we don't have all the implications of quite yet.
*  That's the generation who, if, and I hate to make it somebody else's responsibility,
*  but like they're the ones who can fix it. They're the ones who can, who can figure out
*  how do we keep the good of this kind of technology without letting it eat us alive? And if they're
*  successful, we move on to the next phase, the next level of the game. If they're not successful, then,
*  yeah, then we're, we're going to wreck each other. We're going to destroy society.
*  So you're going to, in your old age, sit on a porch and watch the world burn
*  because of the tick tock generation that, uh, I believe, well, so like this, my kid's age,
*  right? And that's certainly my daughter's age and she's very tapped in to social stuff, but she's
*  also, she's trying to find that balance, right? Of participating in it and in getting the positives
*  of it, but without letting it eat her alive. Um, and I think sometimes she ventures, I hope she
*  doesn't watch this. Sometimes I think she ventures a little too far and is in, and is consumed by it.
*  And other times she gets a little distance. Um, and if, you know, if there's enough people like
*  her out there, they're gonna, they're gonna navigate this, this choppy waters. That's,
*  that's an interesting, uh, skill actually to develop. I talked to my dad about it.
*  You know, I've, uh, now somehow this podcast in particular, but other reasons
*  has received a little bit of attention. And with that, apparently in this world, even though I
*  don't shut up about love and I'm just all about kindness, I have now a little mini army of trolls.
*  It's kind of hilarious actually, but it also doesn't feel good, but it's a skill to learn
*  to not look at that, like to moderate actually, how much you look at that. The discussion I have
*  with my dad, it's similar to, uh, it doesn't have to be about trolls. It could be about checking
*  email, which is like, if you're anticipating, you know, there's, uh, my dad runs a large institute
*  at Drexel university and there could be stressful like emails you're waiting, like there's drama
*  of some kinds. And so like there's a temptation to check the email. If you send an email and you kind
*  of, and that pulls you in into, it doesn't feel good. And it's a skill that he actually complains
*  that he hasn't learned. I mean, he grew up without it, so he hasn't learned the skill of how to
*  shut off the internet and walk away. And I think young people, while they're also being quote unquote
*  damaged by like, uh, you know, being bullied online, all of those stories, which are very
*  like horrific, you basically can't escape your bullies these days when you're growing up. But
*  at the same time, they're also learning that skill of how to be able to shut off, uh, the like
*  disconnect with it, be able to laugh at it and not take it too seriously. It's fascinating.
*  Like we're all trying to figure this out. Just like you said, it's been dropped on us and we're
*  trying to figure it out. Yeah, I think that's really interesting. And I, I guess I've become a
*  believer in the human design, which I feel like I don't completely understand. Like how do you make
*  something as robust as us? Like we're so flawed in so many ways and yet, and yet, you know, we
*  dominate the planet and we do seem to manage to get ourselves out of scrapes eventually,
*  not necessarily the most elegant possible way, but somehow we get, we get to the next step.
*  And I don't know how I'd make a machine do that. I, I, I generally speaking, like if I train one
*  of my reinforcement learning agents to play a video game and it works really hard on that first
*  stage over and over and over again, and it makes it through it succeeds on that first level.
*  And then the new level comes and it's just like, okay, I'm back to the drawing board.
*  And somehow humanity, we keep leveling up and then somehow managing to put together the skills
*  necessary to achieve success, some semblance of success in that next level too. And you know,
*  I hope we can keep doing that. You mentioned reinforcement learning. So you've have a couple
*  years in the field. No, quite, you know, quite a few, quite a long career in artificial intelligence
*  broadly, but reinforcement learning specifically. Can you maybe give a hint about your sense of the
*  history of the field? And in some ways it's changed with the advent of deep learning, but as a long
*  roots, like how is it weaved in and out of your own life? How have you seen the community change
*  or maybe the ideas that it's playing with change? I've had the privilege, the pleasure of being,
*  of having almost a front row seat to a lot of this stuff. And it's been really,
*  really fun and interesting. So when I was in college in the eighties, early eighties,
*  the neural net thing was starting to happen. And I was taking a lot of psychology classes,
*  a lot of computer science classes as a college student. And I thought, you know, something that
*  can play tic-tac-toe and just like learn to get better at it. That ought to be a really easy thing.
*  So I spent almost all of my, what would have been vacations during college, like hacking on my home
*  computer, trying to teach it how to play tic-tac-toe and programming language, basic. Oh yeah. That's,
*  that's, that's, I was, I, that's my first language. That's my native language. Is that when you first
*  fell in love with computer science, just like programming basic on that? What was, what was
*  the computer? Do you remember? I had, I had a TRS 80 model one before they were called model ones,
*  because there was nothing else. I got my computer in 1979. Instead, so I was, it was, I would have
*  been bar mitzvahed, but instead of having a big party that my parents threw on my behalf, they just
*  got me a computer. Cause that's what I really, really, really wanted. I saw them in the, in the,
*  in the mall in Riyushak. And I thought, what, how are they doing that? I would try to stump them.
*  I would give them math problems like one plus, and then in parentheses, two plus one. And it would
*  always get it right. I'm like, how do you know so much? Like I've had to go to algebra class for the
*  last few years to learn this stuff. And you just seem to know. So I was, I was, I was smitten and
*  I got a computer and I think ages 13 to 15, I have no memory of those years. I think I just was in my
*  room with the computer, listening to Billy Joel communing, possibly listening to the radio, listening
*  to Billy Joel. That was the one album I had on vinyl at that time. And, and then I got it on
*  cassette tape and that was really helpful because then I could play it. I didn't have to go down to
*  my parents' wifi or hi-fi, sorry. And at age 15, I remember kind of walking out and like, okay,
*  I'm ready to talk to people again. Like I've learned what I need to learn here.
*  And so, yeah, so, so that was, that was my home computer. And so I went to college and I was like,
*  oh, I'm totally going to study computer science. And I opted the college I chose specifically had
*  a computer science major. The one that I really want the college I really wanted to go to didn't.
*  So bye bye to them. Which college did you go to? So I went to Yale. Princeton would have been way
*  more convenient and it was just beautiful campus and it was close enough to home. And I was really
*  excited about Princeton and I visited, I said, so computer science major, like, well, we have
*  computer engineering. I'm like, oh, I don't like that word engineering. I like computer science. I
*  want to do like, you're saying hardware and software. They're like, yeah. I'm like, I just
*  want to do software. I couldn't care less about hardware. And you grew up in Philadelphia? I grew
*  up outside Philly. Yeah. Yeah. Okay. So the local schools were like Penn and Drexel and
*  Temple. Like everyone in my family went to Temple at least at one point in their lives, except for
*  me. So yeah, Philly, Philly family. Yale had a computer science department and that's when you,
*  it's kind of interesting. You said eighties in your own networks. That's when you know,
*  hot new thing or a hot thing period. So what is that in college? When you first learned about
*  neural networks? Or when she learned like, how did you, it was in a psychology class, not in a CS
*  class. Yeah. Was it psychology or cognitive science or like, do you remember like what context?
*  It was, yeah, yeah. Yeah. So, so I was a, I've always been a bit of a cognitive psychology groupie.
*  So like I, I study computer science, but I like, I like to hang around where the cognitive
*  scientists are. Cause I don't know, brains, man, they're like, they're wacky. Cool.
*  And they have a bigger picture view of things. They're a little less engineering. I would say
*  they're more, they're more interested in the nature of cognition and intelligence and perception and
*  how like the vision system work. They're asking always bigger questions. Now with the deep learning
*  community, they're, I think more, there's a lot of intersections, but I do find that the, the
*  neuroscience folks actually, and a cognitive psychology, cognitive science folks are starting
*  to learn how to program, how to use neural artificial neural networks. And they are actually
*  approaching problems in like totally new, interesting ways. It's fun to watch that grad
*  students from those departments, like approach a problem of machine learning. Right. They come in
*  with a different perspective. Yeah. They don't care about like your image net data set or whatever.
*  They, they want like to understand the, the, the, like the basic mechanisms at the, at the
*  neuronal level and the functional level of intelligence. It's kind of, it's kind of
*  cool to see them work. But yeah. Okay. So you always love, you're always a groupie of cognitive
*  psychology. Yeah. Yeah. And so, uh, so it was in a class by Richard Garrick. He was kind of my,
*  my favorite, uh, psych professor in college. And I took, uh, like three different classes with him.
*  And yeah, so they were talking specifically the class, I think was kind of a,
*  there was a big paper that was written by Steven Pinker and Prince. I don't, I'm blanking on Prince's
*  first name, but Prince and Pinker and Prince, they wrote kind of a, uh, they were at that time,
*  kind of like, ah, I'm blanking on the names of the current people. Um, the cognitive scientists
*  who are complaining a lot about deep networks. Oh, uh, Gary, uh, Gary Marcus, sorry Marcus. Yeah.
*  And who else? I mean, there's a few, but Gary, Gary's the most feisty. Sure. Gary's very feisty.
*  And with this, with his co-author, they, they, you know, they're kind of doing these kinds of
*  takedowns where they say, okay, well, yeah, it does all these amazing things, but here's a shortcoming,
*  here's a shortcoming, here's a shortcoming. And so the Pinker Prince paper is kind of like the,
*  that generation's version of Marcus and Davis, right? Where they're, they're trained as cognitive
*  scientists, but they're looking skeptically at the results in the, in the artificial intelligence
*  neural net kind of world and saying, yeah, it can do this and this and this, but like it can't do
*  that and it can't do that and it can't do that. Maybe in principle or maybe just in practice at
*  this point. But, but the fact of the matter is you're, you've narrowed your focus too far
*  to be impressed. You know, you're impressed with the things within that circle, but you need to
*  broaden that circle a little bit. You need to look at a wider set of problems. And so, so we had,
*  so I was in this seminar in college that was basically a close reading of the Pinker Prince
*  paper, which was like really thick, there was a lot going on in there. And, and it, and it talked
*  about the reinforcement learning idea a little bit. I'm like, oh, that sounds really cool because
*  behavior is what is really interesting to me about psychology anyway. So making programs that,
*  I mean, programs are things that behave, people are things that behave like I want to make
*  learning that learns to behave. And which way was reinforcement learning presented? Is this
*  talking about human and animal behavior or are we talking about actual mathematical constructs?
*  Ah, that's a great, so that's a good question. Right. So this is, I think it wasn't actually
*  talked about as behavior in the paper that I was reading. I think that it just talked about
*  learning. And to me, learning is about learning to behave, but really neural nets at that point
*  were about learning, like supervised learning. So learning to produce outputs from inputs.
*  So I kind of tried to invent reinforcement learning. I, when I graduated, I joined a
*  research group at Bellcore, which had spun out of Bell Labs recently at that time because of the
*  divestiture of the long distance and local phone service in the 1980s, 1984. And I was in a group
*  with Dave Ackley, who was the first author of the Boltzmann machine paper. So the very first
*  neural net paper that could handle XOR, right? So XOR sort of killed neural nets. The very first,
*  the zero width order. The first winter. Yeah. The perceptron's paper and Hinton, along with his
*  student, Dave Ackley, and I think there was other authors as well, showed that, no, no, no, with
*  Boltzmann machines, we can actually learn nonlinear concepts. And so everything's back on the table
*  again. And that kind of started that second wave of neural networks. So Dave Ackley was, he became
*  my mentor at Bellcore. And we talked a lot about learning and life and computation and how all
*  these things fit together. Now Dave and I have a podcast together. So I get to kind of enjoy that
*  sort of his perspective once again, even all these years later. And so I said, I was really
*  interested in learning, but in the concept of behavior. And he's like, oh, well, that's
*  reinforcement learning here. And he gave me Rich Sutton's 1984 TD paper. So I read that paper. I
*  honestly didn't get all of it, but I got the idea. I got that they were using, that he was using ideas
*  that I was familiar with in the context of neural nets and like sort of back prop.
*  But with this idea of making predictions over time, I'm like, this is so interesting,
*  but I don't really get all the details I said to Dave. And Dave said, oh, well, why don't we have
*  him come and give a talk? And I was like, wait, what, you can do that? Like, these are real people.
*  I thought they were just words. I thought it was just like ideas that somehow magically seeped into
*  paper. He's like, no, I know Rich, like, we'll just have him come down and he'll give a talk.
*  And so I was, you know, my mind was blown. And so Rich came and he gave a talk at Belcor.
*  And he talked about what he was super excited, which was they had just figured out at the time,
*  Q learning. So Watkins had visited the Rich Sutton's lab at UMass or Andy Bartow's lab
*  that Rich was a part of. And he was really excited about this because it resolved a whole
*  bunch of problems that he didn't know how to resolve in the earlier paper. And so-
*  And for people who don't know, TD, temporal difference, these are all just algorithms
*  for reinforcement learning. Right. And TD, temporal difference in particular,
*  is about making predictions over time. And you can try to use it for making decisions,
*  right? Because if you can predict how good an action outcomes will be in the future,
*  you can choose one that has better and, but the theory didn't really support
*  changing your behavior. Like the predictions had to be of a consistent process if you really
*  wanted it to work. And one of the things that was really cool about Q learning, another algorithm
*  for reinforcement learning, is it was off policy, which meant that you could actually be learning
*  about the environment and what the value of different actions would be while actually
*  figuring out how to behave optimally. So that was a revelation. Yeah. And the proof of that is kind
*  of interesting. I mean, that's really surprising to me when I first read that and then enrich
*  Sutton's book on the matter. It's kind of beautiful that a single equation can capture-
*  One equation, one line of code, and you can learn anything.
*  Yeah. So equation and code, you're right. The code that you can arguably, at least,
*  if you squint your eyes, can say, this is all of intelligence,
*  that you can implement that in a single, I think I started with Lisp, which is a shout out to Lisp,
*  like a single line of code, key piece of code, maybe a couple, that you could do that. It's kind
*  of magical. It feels so good to be true. Well, and it sort of is. Yeah. It seems to require
*  an awful lot of extra stuff supporting it. But nonetheless, the idea is really good. And as far
*  as we know, it is a very reasonable way of trying to create adaptive behavior, behavior that gets
*  better at something over time. Did you find the idea of optimal at all compelling?
*  You could prove that it's optimal. So one part of computer science that it makes people feel
*  warm and fuzzy inside is when you can prove something like that assorting algorithm worst
*  case runs and N log N and it makes everybody feel so good. Even though in reality it doesn't
*  really matter what the worst case is, what matters is like, does this thing actually work
*  in practice on this particular actual set of data that I enjoy? Did you?
*  So here's a place where I have maybe a strong opinion, which is like, you're right, of course,
*  but no, no, like, so, so what makes worst case so great, right? If you have a worst case analysis,
*  so great is that you get modularity. You can take that thing and plug it into another thing and
*  still have some understanding of what's going to happen when you click them together, right?
*  If it just works well in practice, in other words, with respect to some distribution that you care
*  about, when you go plug it into another thing, that distribution can shift and can change and
*  your thing may not work well anymore and you want it to and you wish it does and you hope that it
*  will, but it might not and then, ah. So you're saying you don't like machine learning?
*  But we have some positive theoretical results for these things. You know, you can come back at me
*  with, yeah, but they're really weak and yeah, they're really weak and you can even say that,
*  you know, sorting algorithms, like if you do the optimal sorting algorithm, it's not really the
*  one that you want and that might be true as well, but. But it is the modularity is a really
*  powerful statement. I really like as an engineer, you can then assemble different things. You can
*  count on them to be, I mean, it's interesting. It's a balance like with everything else in life.
*  You don't want to get too obsessed. I mean, this is what computer scientists do, which they
*  tend to get obsessed. They over optimize things that where they start by optimizing them,
*  they over optimize. So it's easy to like get really granular about this thing, but like the
*  step from an N squared to an N log N sorting algorithm is a big leap for most real world
*  systems. No matter what the actual behavior of the system is, that's a big leap and the same
*  can probably be said for other kinds of first leaps that you would take on a particular problem.
*  It's the picking the low hanging fruit or whatever the equivalent of doing the not the dumbest thing,
*  but the next to the dumbest thing is picking the most delicious reachable fruit. Yeah.
*  Most delicious reachable fruit. I don't know why that's not a saying.
*  Yeah. Okay. So, so you then this is the eighties and this kind of idea starts to percolate of
*  learning. At that point I got to meet, I got to meet Rich Sutton. So everything was sort of
*  downhill from there. And that was, that was really the pinnacle of everything. But then I,
*  you know, then I felt like I was kind of on the inside. So then as interesting results were
*  happening, I could like check in with, with Rich or with Jerry Tesaro, who had a huge impact on
*  kind of early thinking in, in temporal difference learning and reinforcement learning and showed
*  that you could do, you could solve problems that we didn't know how to solve any other way.
*  And so that was really cool. So it was good things were happening. I would hear about it from either
*  the people who were doing it or the people who were talking to the people who were doing it.
*  And so I was able to track things pretty well through, through the nineties.
*  So what, wasn't most of the excitement on reinforcement learning in the nineties era with,
*  what is it? TD gamma? Like what's the role of these kind of little like fun game playing things and
*  breakthroughs about, you know, exciting the community. Was that like, what were your,
*  cause you've also built a crossword or part of building a crossword puzzle, a solver,
*  solving program called proverb. So, so you were interested in this as a problem, like in forming,
*  using games to understand how to build intelligence systems. So like, what did you think about TD
*  gamma? Like, what did you think about that whole thing in the nineties?
*  Yeah. I mean, I found the TD gammon result really just remarkable. So I had known about some of
*  Jerry's stuff before he did TD gammon. He did a system, just more vanilla, well, not entirely
*  vanilla, but a more classical back, propy kind of a network for playing backgammon where he was
*  training it on expert moves. So it was kind of supervised, but the way that it worked was not to
*  mimic the actions, but to learn internally and evaluation function. So to learn, well,
*  if the expert chose this over this, that must mean that the expert values this more than this.
*  And so let me adjust my weights to make it so that the network evaluates this as being better than
*  this. So it could learn from, from human preferences. It could learn its own preferences. And then when
*  he took the step from that to actually doing it as a full-on reinforcement learning problem, where
*  you didn't need a trainer, you could just let it play. That was, that was remarkable. Right. And so
*  I think as, as humans often do, as we've done in the recent past as well, people extrapolate,
*  it's like, oh, well, if you can do that, which is obviously very hard, then obviously you could do
*  all these other problems that we, that we want to solve that we know are also really hard.
*  And it turned out very few of them ended up being practical, partly because I think neural nets,
*  certainly at the time we're struggling to be consistent and reliable. And so training them
*  in a reinforcement learning setting was a bit of a mess. I had, I don't know, generation after
*  generation of like master students who wanted to do value function approximation, basically
*  reinforcement learning with neural nets. And over and over and over again, we were failing. We
*  couldn't get the good results that Jerry Tesaro got. I now believe that Jerry is a neural net
*  whisperer. He has a particular ability to get neural networks to do things that other people
*  would find impossible. And it's not the technology, it's the technology and Jerry together.
*  At which I think speaks to the role of the human expert in the process of machine learning.
*  Right. It's so easy. We were so drawn to the idea that, that it's the technology that is,
*  that is, is where the power is coming from. That I think we lose sight of the, of the fact that
*  sometimes you need a really good, just like, I mean, no one would think, Hey, here's this great
*  piece of software. Here's like, I don't know, GNU, EMAX or whatever. And it doesn't, that prove that
*  computers are super powerful and basically going to take over the world. It's like, no, Stalman is
*  a hell of a hacker. Right. So he was able to make the code do these amazing things. He couldn't have
*  done it without the computer, but the computer couldn't have done it without him. And so I think
*  people discount the role of people like Jerry, who, who, who have just a particular, particular
*  set of skills on that topic, by the way, as a small side note, I tweeted EMAX is greater than
*  Vim yesterday and deleted, deleted the tweet 10 minutes later when I realized you're, you were on
*  fire. It started a war. I was like, Oh, I was just kidding. I was just being, and I'm going to walk,
*  walk, walk back and I, so people still feel passionately about that particular piece of,
*  I don't get that because EMAX is clearly so much better. I don't understand, but you know, why do
*  I say that? Because I, cause like I spent a block of time in the eighties, um, making my fingers
*  know the EMAX keys. And now like that's part of the thought process for me. Like I need to express.
*  And if you take that, if you take my EMAX key bindings away, I become,
*  I can't express myself. I'm the same way with the, I don't know if you know what it is, but
*  a Kinesis keyboard, which is a butt shaped keyboard. Yes, I've seen them. Yeah. And they're very,
*  uh, I don't know, sexy, elegant, beautiful. Yeah. They're, they're gorgeous. Uh, way too expensive.
*  But, uh, the, the problem with them, similar with EMAX is when you, once you learn to use it,
*  it's hard to use other things. There's this absurd thing where I have like small, elegant,
*  lightweight, beautiful little laptops and I'm sitting there in a coffee shop with a giant
*  Kinesis keyboard and a sexy little laptop. It's absurd, but it, you know, like I used to feel bad
*  about it, but at the same time you just kind of have to, sometimes it's back to the Billy Joel
*  thing. You just have to throw that Billy Joel record and throw Taylor Swift and Justin Bieber
*  to the wind. So see, but I like them now because I, cause again, I have no musical taste. Like,
*  now that I've heard Justin Bieber enough, I was like, I really like his songs and Taylor Swift,
*  not only do I like her songs, but my daughter's convinced that she's a genius. And so now I
*  basically have, I'm signed onto that. So that speaks to the back to the robustness of the human
*  brain. That speaks to the neuroplasticity that you can just, you can just like a mouse teach yourself
*  to a dog, teach yourself to enjoy Taylor Swift. I'll try it out. I don't know. I tried, you know
*  what it has to do with just like acclimation, right? Just like you said, a couple of weeks.
*  Yeah. That's an interesting experiment. I'll actually try that. Like I'll listen. That wasn't
*  the intent of the experiment, just like social media. It wasn't intended as an experiment to see
*  what we can take as a society, but it turned out that way. I don't think I'll be the same person
*  on the other side of the week listening to Taylor Swift, but let's try. It's more compartmental.
*  Don't be so worried. Like it's like, I get that you can be worried, but don't be so worried
*  because we compartmentalize really well. And so it won't bleed into other parts of your life.
*  You won't start, I don't know, wearing red lipstick or whatever. Like it's fine. It's fine.
*  Change fashion and everything.
*  It's fine. But you know what? The thing you have to watch out for is you'll walk into a coffee shop
*  once we can do that again.
*  And recognize the song.
*  And you'll be, no, you won't know that you're singing along until everybody in the coffee shop
*  is looking at you. And then you're like, that wasn't me.
*  Yeah. That's the, you know, people are afraid of AGI. I'm afraid of the Taylor, the Taylor
*  Swift takeover.
*  Yeah. And I mean, people should know that TD Gammon was, I get, would you call it,
*  do you like the terminology of self play by any chance? So like systems that learn
*  by playing themselves, just, I don't know if it's the best word, but.
*  What's the problem with that term?
*  Okay. So it's like the big bang, like it's, it's like talking to serious physicists.
*  Do you like the term big bang? And when, when it was early, I feel like it's the early days
*  of self play. I don't know. Maybe it was used previously, but I think it's been used by only
*  a small group of people. And so like, I think we're still deciding is this ridiculously silly name,
*  a good name for the cons potentially one of the most important concepts in artificial intelligence.
*  Okay. It depends how broadly you apply the term. So I used the term in my 1996 PhD dissertation.
*  Oh, wow. The actual terms of.
*  Yeah. Because, because Tassaro's paper was something like training up an expert
*  backgammon player through self play. So I think it was in the title of his paper. If not in the
*  title, it was definitely a term that he used. There's another term that we got from that work
*  is rollout. So I don't know if you, do you ever hear the term rollout? That's a backgammon term
*  that has now applied generally in computers. Well, at least in AI, because of TD gammon.
*  Yeah. That's fascinating.
*  So how is self play being used now? And like, why is it, does it, does it feel like a more general,
*  powerful concept? It's sort of the idea of, well, the machine just going to teach itself to be smart.
*  Yeah. So that's, that's where maybe you can correct me, but that's where, you know, the continuation
*  of the spirit and actually like literally the exact algorithms of TD gammon are applied by deep mind
*  and open AI to learn games that are a little bit more complex that when I was learning artificial
*  intelligence, go was presented to me with artificial intelligence, the modern approach.
*  I don't know if they explicitly pointed to go in those books as like unsolvable kind of thing,
*  like implying that these approaches hit their limit in this, with these particular kind of games.
*  So something, I don't remember if the book said it or not, but something in my head,
*  or if it was the professors instilled in me the idea, like this is the limits of artificial
*  intelligence of the field. Like it instilled in me the idea that if we can create a system
*  that can solve the game of go, we've achieved a GI. That was kind of, I didn't explicitly like
*  say this, but it, that was the feeling. And so from, I was one of the people that it seemed magical
*  when a learning system was able to, to beat a, a human world champion at the game of go.
*  And even more so from that, that was alpha go even more so with alpha go zero than kind of renamed
*  and advanced into alpha zero, beating a world champion or world-class player
*  without any supervised learning on expert games. We're doing only through by playing itself.
*  So that is, I don't know what to make of it. I think it would be interesting to hear
*  what your opinions are on just how exciting, surprising, profound, interesting, or boring
*  the breakthrough performance of alpha zero was. Okay. So alpha go knocked my socks off. That was,
*  that was so remarkable. Which aspect of it?
*  That, that, that they, they got it to work, that they actually were able to leverage a whole bunch
*  of different ideas, integrate them into one giant system. Just the software engineering aspect of it
*  is mind blowing. I don't, I, I've never been a part of a program as complicated as the program
*  that they built for that. And, and just the, you know, like, like Jerry Tesaro is a neural net
*  whisperer, like, you know, David Silver is a kind of neural net whisperer too. He was able to coax
*  these networks and these new way out there architectures to do these, you know, solve these
*  problems that, as you said, you know, when we were learning from AI, no one had an idea how to make
*  it work. It was, it was remarkable that these, you know, these, these techniques that were so good at
*  playing chess and that could beat the world champion in chess couldn't beat, you know, your typical
*  go playing teenager in go. So the fact that, that, you know, in a very short number of years,
*  we kind of ramped up to trouncing people in go just blew me away.
*  So you, you're kind of focusing on the engineering aspect, which is also very surprising. I mean,
*  there's something different about large, well-funded companies. I mean, there's a compute aspect to it
*  too. Like that's of course, I mean, that's similar to deep blue, right? With, with IBM, like there's
*  something important to be learned and remembered about a large company taking the ideas that are
*  already out there and investing a few million dollars into it or, or more. And so you're kind
*  of saying the engineering is kind of fascinating both on the, the, without for go is probably just
*  gathering all the data, right? Of the expert games, like organizing everything, actually doing
*  distributed, supervised learning. And to me, see the engineering I kind of took for granted
*  to me, philosophically being able to persist in the, in the face of like long odds, because it
*  feels like for me, I'll be one of the skeptical people in the room thinking that you can learn
*  your way to, to beat go. Like it sounded like, especially with David Silver, it sounded like
*  David was not confident at all. So like it was like not, it's funny how confidence works.
*  Yeah. It's like, you're not like cocky about it. Like, but- Right. Cause if you're cocky about it,
*  you kind of stop and stall and don't get anywhere. Yeah. But there's like a hope that's unbreakable.
*  Maybe that's better than confidence. It's a kind of wishful hope in a little dream. And you almost
*  don't want to do anything else. You kind of keep doing it. That's, that seems to be the story.
*  And- But with enough skepticism that you're looking for where the problems are and fighting
*  through them. Yeah. Cause you know, there's gotta be a way out of this thing. Yeah. And for him,
*  it was probably there's, there's a bunch of little factors that come into play. It's funny how these
*  stories just all come together. Like everything he did in his life came into play, which is like a
*  love for video games and also a connection to, so the, the nineties had to happen with TD Gammon
*  and so on. Yeah. And in some ways it's surprising, maybe you can provide some intuition to it that
*  not much more than TD Gammon was done for quite a long time on the reinforcement learning front.
*  Yeah. Is that weird to you? I mean, like I said, the, the students who I worked with, we tried to
*  get, basically apply that architecture to other problems and we consistently failed. There were
*  a couple, a couple of really nice demonstrations that ended up being in the literature. There was
*  a paper about controlling elevators, right? Where it's, it's like, okay, can we modify the heuristic
*  that elevators use for deciding, like a bank of elevators for deciding which floors we should be
*  stopping on to maximize throughput essentially. And you can set that up as a reinforcement learning
*  problem and you can, you know, have a neural net represent the value function so that it's taking
*  where are all the elevators, where are the button pushes, you know, this high dimensional,
*  well, at the time, high dimensional input, you know, a couple dozen dimensions and turn that
*  into a prediction as to, oh, is it going to be better if I stop at this floor or not?
*  And ultimately it appeared as though for the standard simulation distribution for people
*  trying to leave the building at the end of the day, that the neural net learned a better strategy
*  than the standard one that's implemented in elevator controllers. So that, that was nice.
*  There was some work that Satyendra Singh et al did on handoffs with cell phones,
*  you know, deciding when, when should you hand off from this cell tower to this cell tower?
*  Oh, okay. Communication networks, yeah.
*  Yeah. And so a couple things seemed like they were really promising. None of them made it
*  into production that I'm aware of. And neural nets as a whole started to kind of implode around then.
*  And so there just wasn't a lot of air in the room for people to try to figure out,
*  okay, how do we get this to work in the RL setting?
*  And then they, they found their way back in 10, in 10 plus years. So you said Alpha Go was
*  impressive. Like it's a big spectacle. Is there... Right. So then Alpha Zero. So I think I may have
*  a slightly different opinion on this than some people. So I talked to Satyendra Singh in
*  particular about this. So Satyendra was a like Rich Sutton, a student of anti-barto. So they
*  came out of the same lab, very influential machine learning, reinforcement learning researcher.
*  Now at DeepMind as is Rich, though different sites, the two of them.
*  He's in Alberta.
*  Rich is in Alberta and Satyendra would be in England, but I think he's in England from Michigan
*  at the moment. But the, but he was, yes, he was much more impressed with Alpha Go Zero, which is
*  didn't, didn't get a kind of a bootstrap in the beginning with human trained games.
*  And it's just was purely self-play. Though the first one, Alpha Go was also a tremendous amount
*  of self-play, right? They started off, they kick-started the, the action network that was
*  making decisions, but then they trained it for a really long time using more traditional
*  temporal difference methods. So, so as a result, I didn't, it didn't seem that different to me.
*  It seems like, yeah, why wouldn't that work? Like once, once it works, it works. So what,
*  but he, he found that, that removal of that extra information to be breathtaking. Like that,
*  that's a game changer. To me, the first thing was more of a game changer.
*  But the open question, I mean, I guess that's the assumption is the expert games might contain
*  with them, within them, a humongous amount of information.
*  But we know that it went beyond that, right? We know that it somehow got away from that
*  information because it was learning strategies. I don't think it's, I don't think Alpha Go is just
*  better at implementing human strategies. I think it actually developed its own strategies that were,
*  that were more effective. And so from that perspective, okay, well, so it, it made at least
*  one quantum leap in terms of strategic knowledge. Okay. So now maybe it makes three, like, okay.
*  But that first one is the doozy, right? Getting it to, to, to work reliably and, and for the
*  networks to, to hold onto the value well enough. Like that was, that was a big step.
*  Well, isn't, maybe you could speak to this on the reinforcement learning front. So the
*  starting from scratch and learning to do something like the first, like,
*  like random behavior to like crappy behavior to like somewhat okay behavior.
*  It's not obvious to me that that's not like impossible to take those steps. Like if you
*  just think about the intuition, like how the heck does random behavior become somewhat basic
*  intelligent behavior? Not, not human level, not superhuman level, but just basic. But you're
*  saying to you kind of the intuition is like, if, if you can go from human to superhuman level
*  intelligence on the, on this particular task of game playing, then you're good at taking leaps.
*  So you can take many of them. That the system, I believe that the system can take
*  that kind of leap. Yeah. No. And also I think that the beginner knowledge in go, like you can start
*  to get a feel really quickly for the idea that, you know, certain parts of the being in certain
*  parts of the board seems to be more associated with winning, right? Cause it's not, it's not
*  stumbling upon the concept of winning. It's told that it wins or that it loses. Well, it's self play.
*  So it both wins and loses. It's told which, which side won. And the information is kind of there to
*  start percolating around to make a difference as to, well, these things have a better chance of
*  helping you win. And these things have a worse chance of helping you win. And so, you know,
*  it can get to basic play, I think pretty quickly. Then once it has basic play, well, now it's kind
*  of forced to do some search to actually experiment with, okay, well, what gets me that next
*  increment of improvement? How far do you think, okay, this is where you kind of bring up the,
*  the Elon Musk and the Sam Harris is right. How far is your intuition about these kinds of
*  self-playing mechanisms being able to take us? Cause it feels one of the ominous,
*  but stated calmly things that when I talked to David Silver, he said,
*  is that they have not yet discovered a ceiling for alpha zero, for example, on the game of go or
*  chess. Like it's, it keeps, no matter how much they compute, they throw at it, it keeps improving.
*  So it's possible. It's very possible that you, if you throw, you know, some like 10 X compute that
*  it will improve by five X or something like that. And when stated calmly, it's so like,
*  oh yeah, I guess so. But, but like, and then you think like, well, can we potentially have like,
*  continuations of Moore's law in totally different ways, like broadly defined Moore's law,
*  right? Not the constant exponential improvement. Like, are we going to have an alpha zero that
*  swallows the world? But notice it's not getting better at other things. It's getting better at
*  go. And I think it's a, that's a big leap to say, okay, well, therefore it's better at other things.
*  Well, I mean, the question is how much of the game of life can be turned into.
*  Right. So that's, that I think is a really good question. And I think that we don't,
*  I don't think we as a, I don't know, community really know that the answer to this, but,
*  so, okay. So, so I went, I went to a talk by some experts on computer chess. So in particular,
*  computer chess is really interesting because for, you know, for, of course, for a thousand years,
*  humans were the best chess playing things on the planet. And then computers like edge to head of
*  the best person. And they've been ahead ever since. It's not like people have, have overtaken
*  computers, but, but computers and people together have overtaken computers. Right. So at least last
*  time I checked, I don't know what the very latest is, but last time I checked that there were teams
*  of people who could work with computer programs to defeat the best computer programs.
*  In the game of go.
*  In the game of chess.
*  In the game of chess.
*  Right. And so using the information about how these things called ELO scores, this sort of notion of
*  how strong a player are you, there's a, there's kind of a range of possible scores and the,
*  you increment in score. Basically, if you can beat another player of that lower score,
*  62% of the time or something like that, like there's some threshold of,
*  if you can somewhat consistently beat someone, then you are of a higher score than that person.
*  And there's a question as to how many times can you do that in chess? Right. And so we know that
*  there's a range of human ability levels that cap out with the best playing humans. And the computers
*  went a step beyond that and computers and people together have not gone, I think a full step beyond
*  that. It feels the estimates that they have is that it's starting to asymptote that we've reached
*  kind of the maximum, the best possible chess playing. And so that means that there's kind of a
*  finite strategic depth, right? At some point, you just can't get any better at this game.
*  Yeah. I mean, I don't, so I like to check that. I think it's interesting because if you have
*  somebody like Magnus Carlsen, who's using these chess programs to train his mind, like to learn
*  a better chess player. Yeah. And so like, that's a very interesting thing because we're not static
*  creatures. We're learning together. I mean, just like we're talking about social networks,
*  those algorithms are teaching us just like we're teaching those algorithms. So that's a fascinating
*  thing. But I think the best chess playing programs are now better than the pairs. Like they have
*  competition between pairs, but it's still, even if they weren't, it's an interesting question.
*  Where's the ceiling? So the David, the ominous David Silver kind of statement is like, we have
*  not found the ceiling. Right. But so the question is, okay, so I don't know his analysis on that.
*  From talking to Go experts, the depth, the strategic depth of Go seems to be substantially
*  greater than that of chess, that there's more kind of steps of improvement that you can make
*  getting better and better and better. But there's no reason to think that it's infinite.
*  Infinite, yeah. And so it could be that it's that what David is seeing is a kind of asymptoting,
*  that you can keep getting better, but with diminishing returns. And at some point,
*  you hit optimal play. Like in theory, all these finite games, they're finite. They have an optimal
*  strategy. There's a strategy that is the mini max optimal strategy. And so at that point,
*  you can't get any better. You can't beat that that strategy. Now that strategy may be
*  from an information processing perspective, intractable, right? You need
*  all the situations are sufficiently different that you can't compress it at all. It's this
*  giant mess of hard coded rules. And we can never achieve that. But that still puts a cap on how
*  many levels of improvement that we can actually make. But the thing about self play is if you
*  put it, although I don't like doing that in the broader category of self supervised learning,
*  is that it doesn't require too much or any human. Human labeling. Yeah. Yeah. Human label or just
*  human effort, the human involvement past a certain point. And the same thing you could argue is true
*  for the recent breakthroughs in natural language processing with language models. Oh, this is how
*  you get to GPT three. Yeah. See how that did the, uh, that was a good, good transition. Yeah.
*  You're a pro. Practice that for days, uh, leading up to this guy now. Uh, but like that's one of the
*  questions is can we find ways to formulate problems in this world that are important to us humans,
*  like more important than the game of chess that, uh, to which self supervised kinds of approaches
*  could be applied, whether it's self play, for example, for like, maybe you could think of like
*  autonomous vehicles in simulation, that kind of stuff, or just robotics applications and simulation
*  or, uh, in the self supervised learning where on, uh, unannotated data or data that's generated by
*  humans naturally without extra costs like the Wikipedia or like all of the internet can be used
*  to learn something about, to create intelligence systems that do something, uh, really powerful
*  that pass the touring test or that do some kind of superhuman level performance. So what's your
*  intuition? They trying to stitch all of it together about our discussion of AGI, the limits of
*  self play and your thoughts about maybe the limits of neural networks in the context of
*  language models. Is there some intuition in there that might be useful to think about?
*  Yeah, yeah. Yeah. So, so first of all, the, the whole transformer network family of things, um,
*  is really cool. It's really, really cool. I mean, for, you know, if you've ever,
*  back in the day you played with, I don't know, Markov models for generating texts and you've
*  seen the kind of texts that they spit out and you compare it to what's happening now, it's,
*  it's amazing. It's so amazing. Now it doesn't take very long interacting with one of these
*  systems before you find the holes, right? It's, it's not smart in any kind of general way.
*  It's really good at a bunch of things and it does seem to understand a lot of the statistics of
*  language extremely well. And that turns out to be very powerful. You can answer many questions with
*  that, but it doesn't make it a good conversationalist, right? And it doesn't make it a good storyteller.
*  It just makes it good at imitating of things that is seen in the past. The exact same thing
*  could be said by people who voting for Donald Trump about Joe Biden supporters and people voting
*  for Joe Biden about Donald Trump supporters is, uh, you know, that they're not intelligent. They're
*  just following the, yeah, they're following things they've seen in the past. And, uh, so it's very,
*  it doesn't take long to find the flaws in their, uh, in, in their like natural language generation
*  abilities. So we're being very critical of AI systems. Right. So, so I've had a similar thought,
*  which was that the stories that GPT three spits out are amazing and very human-like.
*  And it doesn't mean that computers are smarter than we realize necessarily. It partly means
*  that people are dumber than we realize, or that much of what we do day to day is not that deep.
*  Like we're just, we're just kind of going with the flow. We're saying whatever feels like the
*  natural thing to say next. Not a lot of it is, is, is creative or meaningful or intentional,
*  but enough is that we actually get, we get by, right? We do come up with new ideas sometimes,
*  and we do manage to talk each other into things sometimes. And we do sometimes vote for reasonable
*  people sometimes, but, um, but it's really hard to see in the statistics because so much of what
*  we're saying is kind of rote. Um, and so our metrics that we use to measure how these systems
*  are doing don't reveal that because it's, it's, it's in the interstices that, that is very hard
*  to detect. But is your, do you have an intuition that with these language models, if they grow in
*  size, it's already surprising that when you go from GPT two to GPT three, that there is a noticeable
*  improvement. So the question now goes back to the ominous David Silver and the ceiling.
*  Right. So maybe there's just no ceiling. We just need more compute now.
*  I mean, okay. So now I'm speculating as opposed to before when I was completely on firm ground.
*  Yeah. All right. Um, I don't believe that you can get something that really
*  can do language and use language as a thing that doesn't interact with people. Like I think that
*  it's not enough to just take everything that we've said, written down and just say, that's enough.
*  You can just learn from that and you can be intelligent. I think you really need to be pushed
*  back at, I think that conversations, even people who are pretty smart, maybe the smartest thing
*  that we know, not maybe not the smartest thing we can imagine, but we get so much benefit out of
*  talking to each other and interacting. Um, that's presumably why you have conversations live with
*  guests is that, that there's something in that interaction that would not be exposed by, oh,
*  I'll just write you a story and then you can read it later. And I think, I think because these
*  systems are just learning from our stories, they're not learning from being pushed back at by us,
*  that they're fundamentally limited into what they could actually become on this route. They have to,
*  they have to get, you know, shut down. Like we, like we, we have to have an argument that they have
*  to have an argument with us and lose a couple of times before they start to realize, oh, okay, wait,
*  there's some nuance here that actually matters. Yeah. That's actually subtle sounding, but quite
*  profound that the interaction with humans is essential. And the limitation within that is
*  profound as well, because the time scale, like the bandwidth at which you can really interact
*  with humans is very low. So it's costly. So you can't, one of the underlying things about self
*  plays, it has to do, you know, a very large number of interactions. And so you can't really deploy
*  reinforcement learning systems into the real world to interact. Like you couldn't deploy a language
*  model into the real world to interact with humans because it was just not getting enough data
*  relative to the cost it takes to interact. Like the time of humans is, is expensive,
*  which is really interesting. That's the goal that takes us back to reinforcement learning and trying
*  to figure out if there's ways to make algorithms that are more efficient at learning, keep the
*  spirit and reinforcement learning and become more efficient. In some sense, this seems to be the
*  goal. Let's hear what your thoughts are. I don't know if you got a chance to see a blog post called
*  Bitter Lesson. Oh yes. By Rich Sutton that makes an argument. Hopefully I can summarize it. Perhaps,
*  perhaps you can. Yeah, but do you want to? Okay. So I mean, I could try and you can correct me,
*  which is, he makes an argument that it seems if we look at the long arc of the history of the
*  artificial intelligence field, he calls, you know, 70 years that the algorithms from which we've seen
*  the biggest improvements in practice are the very simple, like dumb algorithms that are able to
*  leverage computation. And you just wait for the computation to improve. Like all of the academics
*  and so on have fun by finding little tricks and, and congratulate themselves on those tricks. And
*  sometimes those tricks can be like big, that feel in the moment, like big spikes and breakthroughs,
*  but in reality over the decades, it's still the same dumb algorithm that just waits for the compute
*  to get faster and faster. Do you find that to be an interesting argument against the entirety of
*  the field of machine learning as an academic discipline? That we're really just a subfield
*  of computer architecture. We're just kind of waiting around for them to do their next thing.
*  Who really don't want to do hardware work. So like-
*  That's right. I really don't want to think about hardware.
*  We're procrastinating.
*  Yes, that's right. Just waiting for them to do their jobs so that we can pretend to have done ours.
*  So yeah, I mean, the argument reminds me a lot of, I think it was a Fred Jelinek quote,
*  early computational linguist who said, you know, we're building these computational linguistic
*  systems and every time we fire a linguist, performance goes up by 10%, something like that.
*  And so the idea of us building the knowledge in, in that, in that case was much less, he was finding
*  to be much less successful than get rid of the people who know about language as a, you know,
*  from a kind of scholastic academic kind of perspective and replace them with more compute.
*  And so I think this is kind of a modern version of that story, which is okay, we want to do better on
*  machine vision. You could build in all these, you know,
*  motivated part-based models that, you know, that just feel like obviously the right thing that you
*  have to have, or we can throw a lot of data at it and guess what we're doing better with it,
*  with a lot of data. So I hadn't thought about it until this moment in this way, but what I believe,
*  well, I've thought about what I believe. What I believe is that, you know,
*  compositionality and what's the right way to say it, the complexity grows rapidly as you consider
*  more and more possibilities, like explosively. And so far Moore's law has also been growing
*  explosively, exponentially. And so, so it really does seem like, well, we don't have to think
*  really hard about the algorithm design or the way that we build the systems, because the best benefit
*  we could get is exponential and the best benefit that we can get from waiting is exponential.
*  So we can just wait. It's got, that's gotta end, right? And there's hints now that, that Moore's
*  law is, is starting to feel some friction, starting to, the world is pushing back a little bit.
*  One thing that I, I don't know, do lots of people know this? I didn't know this. I was, I was trying
*  to write an essay and yeah, Moore's law has been amazing and it's been, it's enabled all sorts of
*  things, but there's a, there's also a kind of counter Moore's law, which is that the development
*  cost for each successive generation of chips also is doubling. So it's costing twice as much money.
*  So the amount of development money per cycle or whatever is actually sort of constant. And at some
*  point we run out of money. So, or we have to come up with an entirely different way of, of doing the
*  development process. So like, I guess I always, always a bit skeptical of the look, it's an
*  exponential curve. Therefore it has no end. Soon the number of people going to NURBS will be greater
*  than the population of the earth. That means we're going to discover life on other planets.
*  No, it doesn't. It means that we're in a, in a sigmoid curve on the front half,
*  which looks a lot like an exponential. The second half is going to look a lot like diminishing
*  returns. Yeah. The, I mean, but the interesting thing about Moore's law, if you actually like
*  look at the technologies involved, it's hundreds, if not thousands of S curve stacked on top of
*  each other. It's not actually an exponential curve. It's constant breakthroughs. And then what
*  becomes useful to think about, which is exactly what you're saying, the cost of development,
*  like the size of teams, the amount of resources that are invested in continuing to find new S
*  curves, new breakthroughs. And yeah, it's a, it's an interesting idea. You know, if we live in the
*  moment, if we sit here today, it seems to be the reasonable thing to say that exponentials end.
*  And yet in the software realm, they just keep appearing to be happening. And it's so,
*  I mean, it's so hard to disagree with Elon Musk on this because it, like I've,
*  you know, I used to be one of those folks. I'm still one of those folks. I've studied
*  autonomous vehicles. This is what I worked on. And, and it's, it's like,
*  you look at what Elon Musk is saying about autonomous vehicles. Well, obviously in a couple
*  of years or in a year or, or next month, we'll have fully autonomous vehicles. Like there's
*  no reason why we can't driving is pretty simple. Like it's just a learning problem and you just
*  need to convert, uh, all the driving that we're doing it to data and just having, you know,
*  know, with the trains and that data and, uh, like we use only our eyes, so you can use cameras and
*  you can train on it. And it's like, yeah, that's that what that should work. And then you put that
*  hat on, like the philosophical hat. And, but then you put the pragmatic hat and it's like,
*  this is what the flaws of computer vision are. Like this is what it means to trans scale. And
*  then you, you put the human factors, the psychology hat on, which is like, it's actually driving us a
*  lot, the cognitive science or cognitive, whatever the heck you call it is, it's really hard. It's
*  much harder to drive than, than we realize there's much larger number of edge cases.
*  So building up an intuition around this is, um, is around exponential is really difficult. And on
*  top of that, the pandemic is making us think about exponentials, making us realize that like,
*  we don't understand anything about it. We were not able to intuit exponentials were either
*  ultra terrified, some part of the population and some part is like, uh,
*  the opposite of whatever the different carefree and we're not managing it. Blase.
*  Well, wow. That's the French. Uh, it's got an accent. So it's, uh, it's fascinating to think
*  what, what the limits of this exponential growth of technology, not just Moore's law,
*  it's technology, how that rubs up against the bitter lesson and GPT three and self play mechanisms.
*  That is not obvious. I used to be much more skeptical about neural networks. Now at least
*  give us slither possibility that will be all, that will be very much surprised and also, you know,
*  uh, caught in a way that like, we, uh, are not prepared for, like in applications of, um,
*  social networks, for example, because it feels like really good transformer models that are
*  able to do some kind of like very good, uh, natural language generation of the same kind of models
*  that can be used to learn human behavior and then manipulate that human behavior to gain
*  advertisers dollars and all those kinds of things. Uh, feed the capitalist system and, and they
*  arguably already are manipulating human behavior. Yeah. Yeah. So, but not for self preservation,
*  which I think is a big, that would be a big step. Like if they were trying to manipulate us to
*  convince us not to shut them off, I would be very freaked out, but I don't see a path to that from
*  where we are now. They, they, they don't have any of those abilities. That's not what they're
*  trying to do. They're trying to keep people on, on the site, but see, the thing is this, this is
*  the thing about life on earth is they might be borrowing our consciousness and sentience.
*  Like, so like in a sense they do because the creators of the algorithms have like, they're not,
*  you know, if you look at our body, we're not a single organism. We're a huge number of
*  organisms with like tiny little motivations were built on top of each other. In the same sense,
*  the AI algorithms that are, they're not like system that includes companies and corporations,
*  right? Cause corporations are funny organisms in and of themselves that really do seem to have
*  self preservation built in. And I think that's at the, at the design level, I think the design to
*  have self preservation be a focus. So you're right in that, in that broader system that we're also a
*  part of and can have some influence on, it's, it's, it is much more complicated, much more powerful.
*  Yeah, I agree with that. So people really love it when I ask what three books, technical,
*  philosophical fiction had a big impact in your life. Maybe you can recommend we went with movies.
*  We went with Billy Joe and I forgot what you, what music you recommended, but I didn't. I just said,
*  I have no taste in music. I just like pop music. That was actually really a skillful the way you
*  have. Thank you. Thanks. I was, I'm going to try to do the same with the books.
*  So do you have a skillful way to avoid answering the question about three books you would recommend?
*  I'd like to tell you a story. So my first job out of college was at Belcourt. I mentioned that before
*  where I worked with Dave Ackley, the head of the group was a guy named Tom Landauer. And I don't
*  know how well known he's known now, but arguably he's the, he's the inventor and the first
*  proselytizer of word embeddings. So they, they developed a system shortly before I got to the
*  group. Yeah. That, that called latent semantic analysis that would take words of English and
*  embed them in a multi-hundred dimensional space and then use that as a way of, you know, assessing
*  similarity and basically doing reinforcement learning and not sorry, not reinforcing information
*  retrieval, you know, sort of pre-Google information retrieval. And he was trained as an
*  anthropologist, but then became a cognitive scientist. So I was in the cognitive science
*  research group. It's, you know, like I said, I'm a cognitive science groupie. At the time, I thought
*  I'd become a cognitive scientist, but then I realized in that group, no, I'm a computer scientist,
*  but I'm a computer scientist who really loves to hang out with cognitive scientists. And he said,
*  he studied language acquisition in particular. He said, you know, humans have about this number
*  of words of vocabulary and most of that is learned from reading. And I said, that can't be true
*  because I have a really big vocabulary and I don't read. He's like, you must. I'm like,
*  I don't think I do. I mean, like stop signs. I definitely read stop signs, but like reading
*  books is not, it's not a thing that I do. Really though. It might be just visual, maybe the red
*  color. Do I read stop signs? No, it's just pattern recognition at this point. I don't sound it out.
*  So now I do. I wonder what that, oh yeah. Stop the guns. So that's fascinating. So you don't,
*  so I don't read very, I mean, obviously I read and I've read, I've read plenty of books,
*  but like some people like Charles, my friend Charles and others, like a lot of people in
*  my field, a lot of academics, like reading was really a central topic to them in development.
*  And I'm not that guy. In fact, I used to joke that when I got into college, that it was on kind of a
*  help out the illiterate kind of program because I got to, like I, in my house, I wasn't a
*  particularly bad or good reader, but when I got to college, I was surrounded by these people that
*  were just voracious in their reading appetite. And they would like, have you read this? Have you read
*  this? And I'd be like, no, I'm clearly not qualified to be at this school. Like there's no way I should
*  be here. Now I've discovered books on tape, like audio books. And so I'm much better. I'm more
*  caught up. I read a lot of books. There's a small tangent on that. It is a fascinating open question
*  to me on the topic of driving, whether, you know, supervised learning people, machine learning
*  people think you have to like drive to learn how to drive. To me, it's very possible that just by
*  us humans, by first of all, walking, but also by watching other people drive, not even being inside
*  cars as a passenger, but let's say being inside the car as a passenger, but even just like being a
*  pedestrian and crossing the road, you learn so much about driving from that. It's very possible
*  that you can, without ever being inside of a car, be okay at driving once you get in it
*  or like watching a movie, for example, I don't know something like that.
*  Have you taught anyone to drive? No, so I have two children and I learned a lot about car driving
*  because my wife doesn't want to be the one in the car while they're learning. So that's my job.
*  So I sit in the passenger seat and it's really scary. I have wishes to live and they're, you
*  know, they're figuring things out. Now they start off very much better than I imagine like a neural
*  network would, right? They get that they're seeing the world. They get that there's a road that they're
*  trying to be on. They get that there's a relationship between the angle of the steering, but it takes a
*  while to not be very jerky. And so that happens pretty quickly. Like the ability to stay in lane
*  at speed, that happens relatively fast. It's not zero-shot learning, but it's pretty fast.
*  The thing that's remarkably hard, and this is I think partly why self-driving cars are really hard,
*  is the degree to which driving is a social interaction activity. And that blew me away.
*  I was completely unaware of it until I watched my son learning to drive and I was realizing that he
*  was sending signals to all the cars around him. And those in his case, he's always had social
*  communication challenges. He was sending very mixed, confusing signals to the other cars.
*  And that was causing the other cars to drive weirdly and erratically. And there was no question
*  in my mind that he would have an accident because they didn't know how to read him.
*  There's things you do with the speed that you drive, the positioning of your car,
*  that you're constantly in the head of the other drivers. And seeing him not knowing how to do that
*  and having to be taught explicitly, okay, you have to be thinking about what the other driver is
*  thinking, was a revelation to me. I was stunned. It's quite brilliant. So creating theories of
*  mind of the other. Theories of mind of the other cars. Yeah. Yeah. Which I just hadn't heard
*  discussed in the self-driving car talks that I've been to. Since then, there's some people who do
*  do consider those kinds of issues, but it's way more subtle than I think there's a little bit of
*  work involved with that when you realize, like when you especially focus not on other cars,
*  but on pedestrians, for example, it's literally staring you in the face. Yeah. Yeah. Yeah. So
*  that when you're just like, how do I interact with pedestrians? Yeah. Pedestrians, you're practically
*  talking to an octopus at that point. They've got all these weird degrees of freedom. You don't know
*  what they're going to do. They can turn around any second. But the point is we humans know what
*  they're going to do. Like we have a good theory of mind. We have a good mental model of what they're
*  doing. And we have a good model of the model that have a view and the model of the model of the
*  model. Like we're able to kind of reason about this kind of the social game of it.
*  The hope is that it's quite simple actually, that it could be learned. That's what I just talked to
*  the Waymo. I don't know if you know that company. It's Google South Africa. I talked to
*  their CTO about this podcast and they like I rode in their car and it's quite aggressive and it's
*  quite fast and it's good and it feels great. It also just like Tesla, Waymo made me change my mind
*  about like maybe driving is easier than I thought. Maybe I'm just being speciesist, human centered.
*  Maybe. It's a speciesist argument. Yes. I don't know. But it's fascinating to think about like the
*  same as with reading, which I think you just said you avoided the question. I still hope you
*  answered it somewhat. We avoided it brilliantly. It is there's blind spots as artificial intelligence
*  that artificial intelligence researchers have about what it actually takes to learn to solve
*  a problem. That's fascinating. Have you had Anka Dragan on? Yeah. Okay. She's one of my favorites.
*  So much energy. She's right. Oh, she's amazing. Fantastic. And in particular, she thinks a lot
*  about this kind of I know that you know that I know kind of planning. And the last time I spoke
*  with her, she was very articulate about the ways in which self-driving cars are not solved. Like
*  what's still really, really hard. But even her intuition is limited. Like we're all like new to
*  this. So in some sense, the Elon Musk approach of being ultra confident and just like plow it out
*  there, putting it out there, like some people say it's reckless and dangerous and so on. But
*  partly it seems to be one of the only ways to make progress in artificial intelligence. So
*  it's you know, these are difficult things. You know, democracy is messy. Implementation of
*  artificial intelligence systems in the real world is messy. So many years ago before self-driving
*  cars were an actual thing you could have a discussion about, somebody asked me like what
*  if we could use that robotic technology and use it to drive cars around? Like isn't that aren't
*  people going to be killed and then it's you know, blah, blah, blah. I'm like that's not what's going
*  to happen. I said with confidence, incorrectly obviously. What I think is going to happen is
*  we're going to have a lot more like a very gradual kind of rollout where people have these cars in
*  like closed communities, right? Where it's somewhat realistic, but it's still in a box,
*  right? So that we can really get a sense of what are the weird things that can happen? How do we
*  how do we have to change the way we behave around these vehicles? Like it's obviously requires a
*  kind of coevolution that you can't just plop them in and see what happens. But of course,
*  we're basically popping them in and see what happens. So I was wrong, but I do think that
*  would have been a better plan. So that's but your intuition is funny. Just zooming out and looking
*  at the forces of capitalism. And it seems that capitalism rewards risk takers and rewards and
*  punishes risk takers like it and like, try it out. The academic approach to let's try a small thing
*  and try to understand slowly the fundamentals of the problem. And let's start with one and do two
*  and then see that and then do the three. You know, the capitalist like startup entrepreneurial dream
*  is let's build 1000 and let's right and 500 of them fail. But whatever the other 500 we learned
*  from them. But if you're good enough, I mean, one thing is like your intuition would say like,
*  that's going to be hugely destructive to everything. But actually, it's kind of the the
*  forces of capitalism, like people are quite easy to be critical. But if you actually look at the
*  data at the at the way our world has progressed in terms of the quality of life, it seems like
*  the competent good people rise to the top. This is coming from me from the Soviet Union and
*  so on. It's like, it's interesting that somebody like Elon Musk is the way you you push progress
*  and artificial intelligence like it's forcing way more to step this, their stuff up and way most
*  forcing Elon Musk to step up. It's fascinating, because I have this tension in my heart and just
*  being upset by the lack of progress in autonomous vehicles and within academia. So there's a huge
*  progress in the early days of the DARPA challenges. And then it just kind of stopped like at MIT,
*  but it's true everywhere else with with an exception of a few sponsors here and there.
*  It's like, it's not seen as a sexy problem. At times, like the moment artificial intelligence
*  starts approaching the problems of the real world, like academics kind of like, all right,
*  let let the company get really hard in a different way in a different way. And that's right. I think
*  yeah, right. Some of us are not excited about that other way. But I still think there's fundamental
*  problems to be solved in those difficult things. It's not, it's still publishable, I think like
*  we just need to, it's the same criticism you could have of all these conferences in Europe,
*  to see if you PR or application papers are often as powerful and as important as like,
*  theory paper, even like theory just seems much more respectable and so on. I mean,
*  in machine learning communities changing that a little bit, I mean, at least in statements,
*  but it's still not seen as the sexiest of pursuits, which is like, how do I actually
*  make this thing work in practice as opposed to on this toy data set? All that to say,
*  are you still avoiding the three books question? Is there something on audiobook that you can
*  recommend? Oh, yeah, I mean, I've, yeah, I've read a lot of really fun stuff. In terms of books that
*  I find myself thinking back on that I read a while ago, like the test of time to some degree,
*  I find myself thinking of program or be programmed a lot by Douglas Rochkop,
*  which was, it basically put out the premise that we all need to become programmers in one form or
*  another. And it was an analogy to once upon a time, we all had to become readers, we had to become
*  literate. And there was a time before that when not everybody was literate, but once literacy was
*  possible, the people who were literate had more of a say in society than the people who weren't.
*  And so we made a big effort to get everybody up to speed. And now it's, it's not 100% universal,
*  but it's quite widespread. Like the assumption is generally that people can read. The analogy that
*  he makes is that programming is a similar kind of thing that, that we need to have a say in
*  right. So being a reader, being literate, being a reader means you can receive all this information,
*  but you don't get to put it out there. And programming is the way that we get to put it
*  out there. And that was the argument they made. I think he specifically has now backed away from
*  this idea. He doesn't think it's happening quite this way. And that might be true that it didn't,
*  society didn't sort of play forward quite that way. I still believe in the premise. I still believe
*  that at some point we have the relationship that we have to these machines and these networks has
*  to be one of each individual can, has the wherewithal to make the machines help them do the things that
*  that person wants done. And as you know, as software people, we know how to do that. And
*  we have a problem. We're like, okay, I'll just, I'll hack up a pro script or something and make it.
*  So if we lived in a world where everybody could do that, that would be a better world. And computers
*  would be have, I think less sway over us. And other people's software would have less sway over
*  us as a group. Yeah. In some sense, software engineering, programming is power. Programming
*  is power, right? It's yeah, it's like magic. It's like magic spells and, and it's not out of reach
*  of everyone. But at the moment, it's just a sliver of the population who can, who can commune with
*  machines in this way. So I don't know. So that book had a big, big impact on me. Currently, I'm
*  reading the alignment problem actually by Brian Christian. So I don't know if you've seen this out
*  there yet. Is this similar to just your Russell's work with the control problem? It's in that same
*  general neighborhood. I mean, they take, they have different emphases that they're, they're
*  concentrating on. I think, I think Stuart's book did a remarkably good job, like a, like just a
*  celebratory good job at describing AI technology and sort of how it works. I thought that was great.
*  It was really cool to see that in a book. Yeah. I think he has some experience writing some books.
*  You know, that's probably a possible thing. He's maybe thought a thing or two about how to explain
*  AI to people. Yeah. Yeah. That's a really good point. This book so far has been remarkably good
*  at telling the story of the sort of the history, the recent history of some of the things that
*  have happened. This, I'm in the first third. He said this book is in three thirds. The first
*  third is essentially AI fairness and implications of AI on society that we're seeing right now.
*  And that's been great. I mean, he's telling those stories really well. He's, he went out and talked
*  to the frontline people who, whose names are associated with some of these ideas and it's
*  been terrific. He says the second half of the book is on reinforcement learning. So maybe that'll be
*  fun. And then the third half, third third is on the super intelligence alignment problem. And I,
*  I suspect that that part will be less fun for me to read.
*  Yeah. Yeah, it's, it's an interesting problem to talk about. I find it to be the most interesting,
*  just like thinking about whether we live in a simulation or not as a, as a thought experiment
*  to think about our own existence. So in the same way, talking about alignment problem with AGI
*  is a good way to think similar to like the trolley problem with autonomous vehicles.
*  It's a useless thing for engineering, but it's a, it's a nice little thought experiment for
*  actually thinking about what are like our own human ethical systems, our moral systems to,
*  to, to, uh, by thinking how we engineer these things, you start to understand yourself.
*  So sci-fi can be good at that too. So one sci-fi book to recommend is, um, Exhalations by Ted
*  Chang, a bunch of short stories. Um, this Ted Chang is the guy who wrote the short story that
*  became the movie Arrival. Um, and all of his stories just from a, he's, he was a computer
*  scientist, actually studied at Brown. Um, they all have this sort of really insightful bit of
*  science or computer science that drives them. And so it's just a romp, right? To just like,
*  he creates these artificial worlds with these, by extrapolating on these ideas that,
*  that we know about, but hadn't really thought through to this kind of conclusion. And so his
*  stuff is, it's really fun to read. It's mind warping. So I'm not sure if you're familiar.
*  I seem to mention this every other word, uh, is I'm from the Soviet Union and I'm Russian,
*  uh, read way too much. My roots are Russian too, but a couple of generations back.
*  Well, it's probably in there somewhere. So maybe you can, uh,
*  we can pull at that thread a little bit of the existential dread that we all feel. You mentioned
*  that you, I think somewhere in the conversation, you mentioned that you don't really pretty much
*  like dying. I forget in which context it might've been a reinforcement learning perspective. I don't
*  know. I know. You know what it was? It was in teaching my kids to drive. That's how you face
*  your mortality. Yes. Uh, from a human beings perspective or from a reinforcement learning
*  researchers perspective, let me ask you the most absurd question. What's, uh, what do you think is
*  the meaning of this whole thing? The meaning of life on this spinning rock?
*  I mean, I think reinforcement learning researchers maybe think about this from a science perspective
*  more often than a lot of other people, right? As a supervised learning person, you're probably not
*  thinking about the sweep of a lifetime, but reinforcement learning agents are having little
*  lifetimes, little weird little lifetimes. And it's, it's hard not to project yourself into their world
*  sometimes. But you know, as far as the meaning of life, so I, when I turned 42, you may know from,
*  that's a, that is a book I read. Um, the, the Hitchhiker's Guide to the Galaxy, that that is the
*  meaning of life. So when I turned 42, I had a meaning of life party where I invited people over
*  and, um, everyone shared their meaning of life. We, they, we, they, we had slides made up and so we
*  had, we all sat down and did a slide presentation to each other about the meaning of life.
*  And mine, mine was balance. I think that life is balance. And, um, so the activity at the party
*  for 42 year old, maybe this is a little bit non-standard, but I, I found all the little
*  toys and devices that I had that where you had to balance on them. You had to like stand on it and
*  balance or a pogo stick I brought a rip stick, which is like a weird two-wheeled skateboard.
*  I got a unicycle, but I didn't know how to do it. I didn't know how to do it.
*  I now can do it. I love watching you try. Yeah. I'll send you a video. I'm not great, but I, but,
*  but I managed. Um, and so, uh, so balanced. Yeah. So, so my, my wife has a really good one that she
*  sticks to and is probably pretty accurate. And it has to do with healthy relationships with people
*  that you love and working hard for good causes. But to me, yeah, balance balance in a word. That's
*  that that works for me. Not too much of anything. Cause too much of anything is iffy. That feels
*  like a Rolling Stones song. I feel like they must be. You can't always get what you want, but if you
*  try sometimes you can strike a balance. Yeah, I think that's how it goes. Uh, Michael,
*  I'll write your parody. It's a huge honor to talk to you. This is really, I've been a big fan of
*  yours. So, um, uh, can't, uh, can't wait to see what you do next in the world of, uh, education,
*  the world of parody in the world of reinforcement learning. Thanks for talking to me. My pleasure.
*  Thank you for listening to this conversation with Michael Littman and thank you to our sponsors.
*  Simply Safe, a home security company I use to monitor and protect my apartment Express VPN,
*  the VPN I've used for many years to protect my privacy on the internet, masterclass,
*  online courses that I enjoy from some of the most amazing humans in history and better help
*  online therapy with a licensed professional. Please check out these sponsors in the description
*  to get a discount and to support this podcast. If you enjoy this thing, subscribe on YouTube,
*  review fast stars and Apple podcast, follow on Spotify, support on Patreon,
*  or connect with me on Twitter at Lex Friedman. And now let me leave you some words from Groucho
*  Marx. If you're not having fun, you're doing something wrong. Thank you for listening and
*  hope to see you next time.
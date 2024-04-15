---
Date Generated: April 14, 2024
Transcription Model: whisper medium 20231117
Length: 4809s
Video Keywords: []
Video Views: 56241
Video Rating: None
---

# Jeff Atwood: Stack Overflow and Coding Horror | Lex Fridman Podcast #7
**Lex Fridman:** [November 29, 2018](https://www.youtube.com/watch?v=KZkYSSE8HHI)
*  The following is a conversation with Jeff Atwood. He is the co-founder of Stack Overflow and Stack
*  Exchange, websites that are visited by millions of people every single day. Much like with Wikipedia,
*  it is difficult to understate the impact on global knowledge and productivity that these networks of
*  sites have created. Jeff is also the author of the famed blog Coding Horror and the founder of
*  Discourse, an open source software project that seeks to improve the quality of our online community
*  discussions. This conversation is part of the MIT course on Artificial General Intelligence and the
*  Artificial Intelligence podcast. If you enjoy it, subscribe on YouTube, iTunes, or your podcast
*  provider of choice, or simply connect with me on Twitter at Lex Friedman, spelled F-R-I-D.
*  And now here's my conversation with Jeff Atwood. Having co-created and managed for a few years the
*  world's largest community of programmers in Stack Overflow 10 years ago, what do you think
*  motivates most programmers? Is it fame, fortune, glory, process of programming itself, or is it
*  the sense of belonging to a community? I think it's puzzles really. I think it's
*  this idea of working on puzzles independently of other people and just solving a problem sort of
*  on your own almost. Although nobody really works alone in programming anymore. But I will say
*  there's an aspect of sort of hiding yourself away and just sort of beating on a problem until you
*  solve it. Like brute force basically to me is what a lot of programming is. It's like the computer
*  is so fast, right? You can do things that would take forever for a human, but you can just do them
*  so many times and so often that you get the answer, right? You're saying just the pure act of tinkering
*  with the code is the thing that drives most problems. The joy, the struggle balanced within
*  the joy of overcoming the brute force process of pain and suffering that eventually leads to
*  something that actually works. Well, data is fun too. Like there's this thing called the shuffling
*  problem. Like the naive shuffle that most programmers write has a huge flaw. And there's
*  a lot of articles online about this because it can be really bad if you're like a casino and
*  you have an unsophisticated programmer writing your shuffle algorithm. There's surprising ways
*  to get this wrong. But the neat thing is the way to figure that out is just to run your shuffle a
*  bunch of times and see like how many orientations of cards you get. You should get an equal
*  distribution of all the cards. And with the naive method of shuffling, if you just look at the data,
*  if you just brute force and say, okay, I don't know what's going to happen. You just write a program
*  that does it a billion times and then see what the buckets look like of the data. And the money hall
*  problem is another example of that, where you have three doors and somebody gives you information
*  about another door. So the correct answer is you should always switch in the money hall problem,
*  which is not intuitive and it freaks people out all the time, right? But you can solve it with data.
*  If you write a program that does the money hall game and then never switches and always switches,
*  just compare, you would immediately see that you don't have to be smart, right? You don't have to
*  figure out the answer algorithmically. You can just brute force it out with data and say, well,
*  I know the answer is this because I ran the program a billion times and these are the data
*  buckets that I got from it, right? So empirically, fine data. But what's the joy of that? So for you,
*  personally, outside of family, what motivates you in this process?
*  Well, to be honest, I don't really write a lot of code anymore. What I do at Discourse is
*  manager stuff, which I always despised, right? As a programmer, you think of managers as people who
*  don't really do anything themselves. But the weird thing about code is you realize that language is
*  code. The ability to direct other people lets you get more stuff done than you could by yourself
*  anyway. You said language is code? Language is code. Meaning communication with other humans? Yes,
*  it is. You can think of it as systematic. So what is it like to be, what makes, before we get into
*  programming, what makes a good manager? What makes a good leader? Well, I think a leader, it's all
*  about leading by example, first of all, like sort of doing and being the things that you want to be.
*  Now, this can be kind of exhausting, particularly when you have kids, because you realize that
*  your kids are watching you like all the time, like even in ways that you've stopped seeing
*  yourself. Like the hardest person to see on the planet is really yourself, right? It's a lot easier
*  to see other people and make judgments about them, but yourself, like you're super biased.
*  You don't actually see yourself the way other people see you. Often you're very, very hard on
*  yourself in a way that other people really aren't going to be. So, you know, that's one of the
*  insights is, you know, you've got to be really diligent about thinking like, am I behaving in
*  a way that represents how I want other people to behave, right? Like leading through example.
*  There's a lot of examples of leaders that really mess this up, right? Like they make decisions
*  that are like, wow, that's why would, you know, it's just, it's, it's, it's a bad example for other
*  people. So I think leading by example is one. The other one I believe is working really hard.
*  Now I don't mean like working exhaustively, but like showing a real passion for the problem,
*  like, you know, not necessarily your solution to the problem, but the problem itself is just
*  one that you really believe in. Like with discourse, for example, the problem that we're
*  looking at, which is my current project is how do you get people in groups to communicate in a way
*  that doesn't like break down into the howling of wolves, right? Like how do you deal with trolling
*  not like technical problems of how do I get people to post paragraphs? How do I get people to use
*  bold? How do you get people to use complete sentences? Although those are problems as well,
*  but like, how do I get people to get along with each other, right? Like, and then solve whatever
*  problem it is they set out to solve or, you know, reach some consensus on discussion or just like
*  not hurt each other even, right? Like maybe it's a discussion that doesn't really matter, but are
*  people like yelling at each other, right? And why, right? Like that's not the purpose of this kind
*  of communication. So I would say, you know, leadership is about, you know, setting an example,
*  you know, doing the things that represent what you want to be and making sure that you're actually
*  doing those things. And there's a trick to that too, because the things you don't do also say a
*  lot about what you are. Yeah. So let's pause on that one. So those two things are fascinating. So
*  how do you have as a leader, that self-awareness? So you just said it's really hard to be self-aware.
*  So for you personally, or maybe for other leaders you've seen or look up to, how do you know
*  both that the things you're doing are the wrong things to be doing, the way you speak to others,
*  the way you behave and the things you're not doing? How do you get that signal?
*  There's two aspects to that. One is like processing feedback that you're getting.
*  So how do you get feedback? Well, right. So are you getting feedback? Right. Like, so one way we do
*  it, for example, at Discourse, we have three co-founders and we periodically talk about
*  decisions before we make them. So it's not like one person can make a mistake or like, wow,
*  there can be misunderstandings, things like that. So it's part of like group consensus of leadership
*  is like, it's good to have, I think systems where there's one leader and that leader has the rule
*  of absolute law are just really dangerous in my experience. For communities, for example,
*  like if you have a community that's run by one person, that one person makes all the decisions,
*  that person's going to have a bad day. Something could happen to that person, something,
*  there's a lot of variables. So like at first, when you think about leadership,
*  have multiple people doing leadership and have them talk amongst each other. So they're giving
*  each other feedback about the decisions that they're making. And then when you do get feedback,
*  I think there's that little voice in your head, right? Like, or your gut or wherever you want to
*  put it in your body. I think that voice is really important. Like I think most people who have any
*  kind of moral compass or like want to do, most people want to do the right thing. I do believe
*  that. I mean, there might be a handful of sociopaths out there that don't, but most people,
*  they want other people to think of them as a good person. And why wouldn't you, right? Like,
*  do you want people to despise you? I mean, that's just weird, right? So you have that little voice
*  that sort of the angel and devil on your shoulder sort of talking to you about like what you're
*  doing, how you're doing, how does it make you feel to make these decisions? Right. And I think
*  having some attunement to that voice is important. But you said that voice also for, I think there's
*  a programmer situation too, where sometimes the devil on the shoulders a little, a little too loud.
*  So you're a little too self-critical for a lot of developers, especially when you have
*  introverted personality. How do you struggle with the self-criticism or the criticism
*  others? So one of the things of leadership is to do something that's potentially unpopular or
*  where people doubt you and you still go through with the decision. So what's that balance like?
*  I think you have to walk people through your decision-making, right? Like you have to,
*  this is where blogging is really important and communication is so important. Again, code,
*  language is just another kind of code is like, here is the program by which I arrived at the
*  conclusion that I'm going to reach. Right. It's one thing to say, like, this is a decision, it's final,
*  deal with it. Right. That's not usually satisfying to people. But if you say, look,
*  you know, we've been thinking of this problem for a while, here's some stuff that's happened.
*  Here's what we think is right. Here's our goals. Here's what we want to achieve. And we've looked
*  at these options and we think this of the available options is the best option. People will be like,
*  oh, okay. All right. Maybe I don't totally agree with you, but I can kind of see where you're
*  coming from. And like, I see it's not just arbitrary decision delivered from a cloud of
*  flames in the sky, right? It's like a human trying to reach some kind of consensus about,
*  you know, goals and their goals might be different than yours. That's completely legit. Right. But
*  if you're making that clear, it's like, oh, well, the reason we don't agree is because we have
*  totally different goals, right? Like, how could we agree? It's not that you're a bad person. It's
*  that we have radically different goals in mind when we started looking at this problem.
*  And the other one you said is passion. So, or hard work, sorry.
*  Well, those are tied together to me in my mind. I didn't say hard work and passion. Like for me,
*  like, I just really love the problem discourse is sending out to solve because in a way it's like,
*  there's a, there's a vision of the world where it all devolves into Facebook, basically owning
*  everything and every aspect of human communication. Right. And this has always been kind of a scary
*  world for me. First, cause I don't, I think Facebook is really good at execution. I got to
*  compliment them. They're very competent in terms of what they're doing, but Facebook has not much
*  of a moral compass in terms of Facebook cares about Facebook. Really. They don't really care
*  about you and your problems. What they care about is how big they can make Facebook. Right.
*  Is that you talking about the company or just the mechanism of how Facebook works?
*  Kind of both really. Right. Like, and the idea with discourse, the reason I'm so passionate about
*  is cause I believe every community should have the right to own themselves, right? Like they should
*  have their own software that they can run that belongs to them. That's their space where they
*  can set the rules. And if they don't like it, they can move to different hosting or, you know,
*  whatever they need, they need to happen can happen. But like this, this idea of a company town
*  where all human communication is implicitly owned by WhatsApp, Instagram and Facebook.
*  And it's really disturbing too, cause Facebook is really smart. Like I said, they're great at
*  execution buying and WhatsApp and buying Instagram were incredibly smart decisions.
*  And they also do this thing on, if you know, but they, they have this VPN software that
*  they give away for free on smartphones and it indirectly feeds all the data about the traffic
*  back to Facebook. So they can see what's actually getting popular through the VPNs, right? They have
*  low level access to the network data because users have let them have that. So.
*  Let's take a small pause here. First of all, discourse. Can you talk about,
*  can you lay out the land of all the different ways you can have communities? So there's
*  stack overflow that you've built. There's discourse. So stack overflow is kind of like a
*  wiki Wikipedia you talk about. And it's a very specific scalpel, very focused. So what is the
*  purpose of discourse and maybe contrast that with Facebook? First of all, say what is discourse?
*  Start from the beginning. Well, let me start from the very beginning. So stack overflow is very
*  structured wiki cell Q and a for programmers, right? And that was the problem we first worked
*  on it. When we started, we thought it was discussions because we looked at like programming
*  forums and other things, but we quickly realized we were doing Q and a, which is a very narrow
*  subset of human communication. So when you started stack overflow, you thought you didn't
*  even know the Q and a. Not really. Well, we didn't know. We had an idea of like, okay, these are
*  things that we see working online. We had a goal, right? Our goal was there was this site, Experts
*  Exchange with a very unfortunate name. Thank you for killing that site. Yeah, I know, right? Like
*  a lot of people don't remember it anymore, which is great. Like that's the measure of success. When
*  people don't remember the thing that you were trying to replace, then you've totally won.
*  So it was a place to get answers to programming questions, but it wasn't clear if it was like
*  focused Q and a, if it was a discussion, there were plenty of programming forums. So we weren't
*  really sure we were like, okay, we'll take aspects of dig and Reddit, like voting were very important,
*  reordering answers based on votes, wiki style stuff of like being able to edit posts, not just
*  your post, but other people's posts to make them better and keep them more up to date.
*  Ownership of blogging of like, okay, this is me. I'm saying this in my voice, you know,
*  this is the stuff that I know. And you know, you get your reputation accrues to you.
*  And it's pure recognition. So you asked earlier, like what motivates programmers,
*  I think pure recognition motivates them a lot. That was one of the key insights of Stack Overflow
*  was like recognition from your peers is why things get done. Initially money, not so your boss,
*  but like your peers saying, wow, this person really knows their stuff has a lot of value. So
*  the reputation system came from that. So we were sort of Frankensteining a bunch of stuff together
*  in Stack Overflow, like stuff we had seen working and we knew worked. And that became Stack Overflow.
*  Over time, we realized it wasn't really discussion. It was very focused questions
*  and answers. There wasn't a lot of room on the page for, let me talk about this tangential thing.
*  It was more like, okay, is it answering the question? Is it clarifying the question? Or
*  could it be an alternative answer to the same question? Because there's usually more than one
*  way to do it in programming. There's like, say, five to 10 ways. And one of the patterns we got
*  into early on with Stack Overflow was there were questions where there would be like hundreds of
*  answers. And we're like, wow, how can there be a programming question with 500, 200, 500 answers?
*  And we looked at those and we realized those were not really questions in the traditional sense.
*  They were discussions. It was stuff that we allowed early on that we eventually decided wasn't
*  allowed, such as what's your favorite programming food? What's the funniest programming cartoon
*  you've seen? And we had to sort of backfill a bunch of rules about like, why isn't this allowed?
*  Such as is this a real problem you're facing? Like nobody goes to work and says, wow, I can't
*  work because I don't know what the funniest programming cartoon is. So sorry, can't compile
*  this code now. Right? It's not a real problem you're facing in your job. So that was one rule.
*  And the second, like, what can you really learn from that? It's like what I call accidental
*  learning or Reddit style learning, where you're just like, oh, just browse some things and oh,
*  wow, you know, did you know tree frogs only live three years? I mean, I just made that up. I don't
*  know if that's true. But I didn't really set out to learn that. I don't need to know that. Right.
*  Accidental learning. It was more intentional learning. We're like, okay, I have a problem.
*  And I want to learn about stuff around this problem having. Right. And it could be theory,
*  it could be compiler theory, it could be other stuff. But I'm having a compiler problem. Hence,
*  I need to know the compiler theory, that aspect of it that gives me the gets me to my answer.
*  Right. So kind of a directed learning. So we had to backfill all these rules as we sort of figured
*  out what the heck it was we were doing. And the system came very strict over time. And a lot of
*  people still complain about that. And I wrote my latest blog entry, what does Stack Overflow want
*  to be? I want to be when it grows up celebrating the 10 year anniversary. Yeah, yeah. So 10 years,
*  and the system is trended towards strictness. There's a variety of reasons for this. One is,
*  people don't like to see other people get reputation for stuff as they view they view as
*  frivolous, which I can actually understand. Because if you saw a programmer got like 500 upvotes for
*  funniest programming cartoon or funniest comment they had seen in code, it's like, well, why do
*  they have that reputation is because they wrote the joke? Probably not. I mean, they did maybe or
*  the cartoon, right? They're getting a bunch of reputation based on someone else's work. It's not
*  even like programming. It's just a joke, right? It's a related program. So you begin to resent
*  that you're like, well, that's not fair. And it isn't at some level. They're correct. I mean,
*  I empathize because like, it's not correct to get reputation for that versus here's a really gnarly
*  regular expression problem. And here's a really, you know, clever, insightful, you know, detailed
*  answer laying out. Oh, here's why you're seeing the behavior that you're seeing here. Let me teach
*  you some things about how to avoid that in the future. That's, that's great. Like that's gold,
*  right? You want people to get reputation for that. Not so much for, wow, look at this funny thing I
*  saw. Right? Great. So there's this very specific Q and A format and then take me through the
*  journey towards discourse and Facebook and Twitter. So you started at the beginning that stack overflow
*  evolved to have a purpose. So what is discourse? This passion you have for creating community for
*  discussion. What, where does that, when was that born and how well part of it is based on the
*  realization the stack overflow is only good for very specific subjects where there's sort of,
*  it's based on data facts and science where answers can be kind of verified to be true.
*  Another form of that is there's the book of knowledge, like the tome of knowledge that defines
*  like whatever it is, you can refer to that book and I'll give you the answer. There has to be,
*  it only works on subjects where there's like semi clear answers to things that can be verified in
*  some form. Now, again, there's always more than one way to do it. There's complete flexibility
*  and system around that. But where it falls down is stuff like poker and Lego. Like we had,
*  if you go to stack exchange.com, we have an engine that tries to launch different Q and A topics,
*  right? And people can propose Q and A topics, sample questions, and if it gets enough support
*  within the network, we launched that Q and A site. So some of the ones we launched were poker
*  and Lego and they did horribly, right? Because I mean, they might still be there lingering on in
*  some form, but it was an experiment. This is like a test, right? And some subjects work super well
*  in the stack engine and some don't. But the reason Lego and poker don't work is because they're so
*  social, really. It's not about, you know, what's the rule here in poker. It's like, well, you know,
*  what kind of cigars do we like to smoke while playing poker or, you know, what's a cool set
*  of cards to use when I'm playing poker or, you know, what's some strategies? Like say I have this
*  hand come up, put some strategies I could use. It's more of a discussion around like what's
*  happening. Like with Lego, you know, same thing like here's this cool Lego set I found. Look how
*  awesome this is. And like, yeah, that's freaking awesome, right? It's not a question, right? There's
*  all these social components, discussions that don't fit at all. Like we literally have to disallow
*  those in Stack Overflow because it's not about being social. It's about problems that you're
*  facing in your work that you need concrete answers for, right? Like you have a real demonstrated
*  problem that's sort of blocking you and something. Nobody's blocked by, you know, what should I do
*  when I have a straight flush, right? Like it's not a blocking problem in the world. It's just an
*  opportunity to hang out and discuss. So discourse was a way to address that and say, look, you know,
*  discussion forum software was very, very bad. And when I came out of Stack Overflow in late,
*  early 20, early 2013, early, early 2012, it was still very, very bad. I expected it improved in
*  the four years since I last looked, but it had not improved at all. And I was like, well, that's kind
*  of terrible because I love these communities of people talking about things that they love,
*  you know, that there's just communities of interest, right? And there's no good software
*  for them. Like startups would come to me and say, Hey, Jeff, I want to, you know, I have this
*  startup. Here's my idea. And the first thing I would say to them is like, well, first, why are
*  you asking me? Like, I don't really know your field, right? Not necessarily. Like, why aren't
*  you asking like the community, like the people that are interested in this problem, the people
*  that are using your product, why aren't you talking to them? And then they say, oh, great idea. Like,
*  how do I do that? And then that's when I started playing sad trombone, because I realized all the
*  software involving talking to your users, customers, audience, patrons, whatever it is,
*  it was all really bad. You know, it was like stuff that I would be embarrassed to recommend
*  to other people. And yet that's where I felt they could get the biggest and strongest, most
*  effective input for what they should be doing with their product, right? It's from their users,
*  from their community, right? That's what we did on Stack Overflow. So what we're talking about with
*  forums, the, what is it, the dark matter of the internet, it's still, I don't know if it's still,
*  but for the longest time, it has some of the most passionate and fascinating discussions. And what's
*  the usual structure? There's usually what it's a, it's linear, so sequential. So you're posting one
*  after the other and there's pagination. So it's every, there's a 10 posts and you go to the next
*  page. And that format still is used by like, I'm, we're doing a lot of research with Tesla vehicles,
*  and there's a Tesla Motors Club forum, which is extremely fun. We really wanted to run that,
*  actually. They pinged us about it. I don't think we got it, but I really would have liked to
*  gotten that one. But they've started before even 2012, I believe. I mean, they've been running for
*  a long time. It's still an extremely rich source of information. So what's broken about that system
*  and how are you trying to fix it? I think there's a lot of power in, in connecting people that love
*  the same stuff around that specific topic, meaning Facebook's idea of connection is
*  just any human that's related to another human, right? Like through friendship or any other
*  reason. Facebook's idea of the world is sort of the status update, right? Like a friend of yours
*  did something, ate at a restaurant, right? Whereas discussion forums were traditionally around the
*  interest graph. Like I love electric cars, specifically I love Tesla, right? Like I love
*  the way they approach the problem. I love the style of the founder. I just love the design ethic.
*  There's a lot to like about Tesla. I don't know if you saw the oatmeal. He did a whole love comic
*  to Tesla and it was actually kind of cool because I learned some stuff. He was talking about how
*  great Tesla cars were specifically, like how they were built differently. And he went into a lot of
*  great detail. That was really interesting. And to me, that oatmeal post, if you read it, is the
*  genesis of pretty much all interest communities. I just really love this stuff. So for me, for
*  example, there's yo-yos, right? Like I'm into the yo-yo communities and there's these interest
*  communities are just really fascinating to me. And I feel more connected to the yo-yo communities
*  than I do to friends that I don't see that often, right? Like to me, the powerful thing is the
*  interest graph and Facebook kind of dabbles in the interest graph. I mean, they have groups,
*  you can sign up for groups and stuff, but it's really about the relationship graph. Like this
*  is my coworker, this is my relative, this is my friend, but not so much about the interest. So I
*  think that's the linchpin of which forums and communities are built on that I personally love.
*  Like I said, leadership is about passion, right? And being passionate about stuff is
*  a really valid way to look at the world. And I think it's a way a lot of stuff in the world gets
*  done. Like I once had someone describe me as, he's like, Jeff, you're a guy who you just get super
*  passionate about a few things at a time and you just go super deep in those things. And I was like,
*  that's kind of right. That's kind of what I do. I'll get into something and just be super into
*  that for a couple of years or whatever and just learn all I can about it and go super deep in it.
*  And that's how I enjoy experiencing the world, right? Like not being shallow in a bunch of
*  things, but being really deep on a few things that I'm interested in. So forums kind of unlock that,
*  right? And you don't want a world where everything belongs to Facebook. At least I don't. I want a
*  world where communities can kind of own themselves, set their own norms, set their own rules,
*  control the experience. Because community is also about ownership, right? Like if you're meeting at
*  the Barnes and Noble every Thursday and Barnes and Noble says, get out of here, you guys don't buy
*  enough books. Well, you know, you're kind of hosed, right? Barnes and Noble owns you, right?
*  Like you can't, but if you have your own meeting space, you know, your own clubhouse, you can set
*  your own rules, decide what you want to talk about there and just really generate a lot better
*  information than you could like hanging out at Barnes and Noble every Thursday at 3pm, right?
*  So that's kind of the vision of discourse is a place where it's fully open source.
*  You can take the software, you can sell it anywhere. And you know, you and a group of people
*  can go deep on whatever it is that you're into. And this works for startups, right? Startups are
*  a group of people who go super deep on a specific problem, right? And they want to talk to their
*  community. It's like, well, install discourse, right? That's what we do at discourse. That's
*  what I did at Stack Overflow. I spent a lot of time on Meta Stack Overflow, which is our internal,
*  well, public community feedback site and just experiencing what the users were experiencing,
*  right? Because they're the ones doing all the work in the system and they had a lot of interesting
*  feedback. And there's that 90 10 rule of like 90% of the feedback you get is not really actionable
*  for a variety of reasons. It might be bad feedback. It might be crazy feedback. It might be feedback
*  you just can't act on right now. But there's 10% of it that's like gold. It's like literally
*  gold and diamonds where it's like feedback of really good improvements to your core product
*  that are not super hard to get to and actually make a lot of sense. And my favorite is about
*  5% of those stuff. I didn't even see coming. It's like, oh my God, I never even thought of that. But
*  that's a brilliant idea, right? And I can point to so many features of Stack Overflow that we
*  drive from Meta Stack Overflow feedback and Meta discourse, right? Same exact principle of discourse.
*  You know, we're getting ideas from the community. I was like, oh my God, I never thought of that,
*  but that's fantastic, right? Like I love that relationship with the community.
*  LWK From having built these communities, what have you,
*  what have you learned about? What's the process of getting a critical mass of members in a community?
*  Is it luck, skill, timing, persistence? What is, is it the tools like discourse that empower that
*  community? What's the key aspect of starting for one guy or gal and then building it to two,
*  one and 10 and a hundred and a thousand and so on?
*  JG I think we're starting with an N of one. I mean, I think it's persistence and also you have to be
*  interesting. Like somebody I really admire once said something that I always liked about blogging.
*  He's like, here's how you blog. You have to have something interesting to say and have an interesting
*  way of saying it, right? And then do that for like 10 years. So that's the genesis is like,
*  you have to have sort of something interesting to say. That's not exactly what everybody else
*  is saying and an interesting way of saying it, which is another way of saying kind of entertaining
*  way of saying it. And then as far as growing it, it's like ritual, you know, like you have to like,
*  say you're starting a blog, you have to say, look, I'm going to blog every week, three times a week,
*  and you have to stick to that schedule, right? Because until you do that for like several years,
*  you're never going to get anywhere. Like it just takes years to get to where you need to get to.
*  And part of that is having the discipline to stick with the schedule. And it helps again,
*  if it's something you're passionate about, this won't feel like work. Like I love this. I could
*  talk about this all day every day, right? You just have to do it in a way that's interesting
*  to other people. And then as you're growing the community, that pattern of participation
*  within the community of like generating these artifacts and inviting other people to help you
*  like collaborate on these artifacts, like even in the case of blogging, like I felt in the early
*  days of my blog, which I started in 2004, which is really the genesis of Stack Overflow. If you look
*  at all my blog, it leads up to Stack Overflow, which was I have all this energy in my blog,
*  but I don't like 40,000 people were subscribing to me. And I was like, I want to do something.
*  And then then I met Joel and said, Hey, Joel, I want to do something. Take this ball of energy
*  for my blog and do something. And all the people read my blog saw that. Oh, cool. You're involving
*  us. You're saying, look, you're part of this community. Let's build this thing together.
*  Like they pick the name. Like we voted on the name for Stack Overflow on my blog. Like we came up
*  and naming is super hard. First of all, I the hardest problem in computer science is coming
*  with a good name for stuff, right? But there you can go back to my blog. There's the poll where we
*  voted and Stack Overflow became the name of the site and all the early beta users of Stack Overflow
*  were audience of my blog plus Joel's blog. Right? So we started from like, if you look at the
*  genesis of it, I was just a programmer who said, Hey, I love programming, but I have no outlet to
*  talk about it. So I'm just going to blog about it because I don't have enough people to work to talk
*  to about it. Because at the time I worked place where, you know, programming wasn't the core
*  output of the company. It was a pharmaceutical company. And I just love this stuff, you know,
*  to an absurd degree. So I was like, I'll just blog about it and then I'll find an audience.
*  Eventually found an audience, eventually found Joel and eventually built Stack Overflow from that
*  one core of activity. Right. But it was that repetition of feeding back in feedback from my
*  blog comments, feedback from Joel feedback from the early Stack Overflow community. When people
*  see that you're doing that, they will follow along with you. Right. They say, Oh, cool. You're here
*  in good faith. You're actually, you know, not listening to everything because that's impossible.
*  That's impossible. But you're actually, you know, waiting our feedback and what you're doing because
*  why wouldn't I? Because who does all the work on Stack Overflow? Me, Joel? No, it's the other
*  programmers that are doing all the work. So you've got to have some respect for that. And then,
*  you know, discipline around, look, you know, we're trying to do a very specific thing here on Stack
*  Overflow. We're not trying to solve all the world's problems. We're trying to solve this very specific
*  Q&A problem in a very specific way. Not because we're jerks about it, but because these strict
*  set of rules help us get really good results. Right. And programmers, that's an easy sell for
*  the most part because programmers are used to dealing with ridiculous systems of rules,
*  like constantly. That's basically their job. So they're very, oh yeah, super strict system
*  of rules that lets me get what I want. That's programming, right? That's what Stack Overflow is.
*  So you're making it sound easy, but in 2004, let's go back there. In 2004, you started the blog,
*  Coding Horror. What was it called that at the beginning? It was one of the smart things I did.
*  It's from a book by Steve McConnell, Code Complete, which is one of my favorite programming
*  books, still probably my number one programming book for anyone to read.
*  One of the smart things I did back then, I don't always do smart things when I start stuff,
*  I contacted Steven and said, hey, I really like this. It was a sidebar illustration indicating
*  danger in code, right? Coding Horror was like, watch out. And I love that illustration because
*  it spoke to me because I saw that illustration go, oh my God, that's me. I'm always my own worst
*  enemy. That's the key insight in programming is every time you write something, think, how am I
*  going to screw myself? Because you will constantly, right? So that icon was like, oh yeah,
*  I need to constantly hold that mirror up and look and say, look, you're very fallible. You're going
*  to screw this up. How can you build this in such a way that you're not going to screw it up later?
*  How can you get that discipline around making sure at every step I'm thinking through all the
*  things that I could do wrong or that other people could do wrong? Because that is actually how you
*  get to be a better programmer a lot of times, right? So that sidebar illustration, I loved it
*  so much. And I wrote Steve before I started my blog and say, hey, can I have permission to use
*  this? Because I just really like this illustration. And Steve was kind enough to give me permission
*  to do that and just continues to give me permission. So yeah, really, that's awesome. But in 2004,
*  you started this blog, you know, you look at Stephen King, his book on writing or Steven
*  Pressfield, War of Art book. I mean, it seems like writers suffer. I mean, it's a hard process of
*  writing, right? There's a lot of there's gonna be suffering. I mean, I won't kid you like, well,
*  the work is suffering, right? Like doing the work, like even when you're every week, you're like,
*  okay, that blog post wasn't very good. Or, you know, people didn't like it. Or people said
*  disparaging things about it. You have to like, have the attitude is like, you know, no matter
*  what happens, I want to do this for me, right? It's not about you. It's about me. I mean, in the end,
*  it is about everyone, because this is how good work gets out into the world. But you have to be
*  pretty strict about saying like, you know, I'm selfish in the sense that I have to do this for
*  me. You know, you mentioned Stephen King, like his book on writing, but like one of the things I do,
*  for example, when writing is like, I read it out loud, one of the best pieces of advice for writing
*  anything is read it out loud, like multiple times and make it sound like you're talking, because
*  that is the goal of good writing. It should sound like you said it with with slightly better phrasing,
*  because you have more time to think about what you're saying. But like, it should sound natural
*  when you say it. And I think that's probably the single best writing advice I can give anyone.
*  Just just read it over and over out loud, make sure it sounds like something you would normally
*  say. And it sounds good. And what's your process of writing? So there's usually a pretty good idea
*  behind the blog post. So ideas, right. So I think you got to have the concept that there's so many
*  interesting things in the world. Like, I mean, my god, the world is amazing, right? Like, it's you
*  could never write about everything that's going on, because it's so incredible. But if you can't
*  come up with, like, let's say, one interesting thing per day to talk about, then you're not
*  trying hard enough, because the world is full of just super interesting stuff. And one great way to
*  to like mine stuff is go back to old books, because they bring up old stuff that's still super
*  relevant. And I did that a lot, because I was like reading classic programming books. And a lot of
*  the early blog posts were like, Oh, I was reading this programming book, and they brought this really
*  cool concept. And I want to talk about it some more. And you get the I mean, you're not claiming
*  credit for that idea, but it gives you something interesting to talk about. That's kind of evergreen,
*  right? Like, you don't have to go, what should I talk about? So we'll just go dig up some old
*  classic programming books and find something that Oh, wow, that's interesting. Or how does that
*  apply today? Or what about x and y or compare these two concepts? So pull a couple of sentences
*  in that book, and then sort of play off of it, almost agree or disagree that so in 2007,
*  you wrote that you were offered a significant amount of money to sell the blog, you chose not
*  to. What were all the elements you were thinking about? Because I'd like to take you back,
*  it seems like there's a lot of nonlinear decisions you made through life. So what was that decision
*  like? Right. So I one of the things I love is the choose your own adventure books, which I loved as
*  a kid. And I feel like the early programmer books, because they're, they're all about if then
*  statements, right? If this then this, and they're also very, very unforgiving, like there's all these
*  sites that map the classic to your adventure books, and how many outcomes are bad, a lot of
*  bad outcomes. So part of the game is like, Oh, I got a bad outcome, go back one step, go back one
*  further steps. Like, how did I get here? Right? Like, it's a sequence of decisions. And this is
*  true of life, right? Like every decision is a sequence, right? individually, any individual
*  decisions, not necessarily right or wrong, but they lead you down a path, right? So I do think
*  there's some truth that so this particular decision, the blog had gotten fairly popular,
*  there's a lot of RSS readers that I discovered. And this guy contacted me out of the blue from
*  this like bug tracking companies, like, Oh, I really want to buy your blog for like, I think
*  it was around $100,000. Maybe like 80,000. But it was it was a lot, right? Like, and that's, you know,
*  at the time, like, I would have a year's worth of salary all at once. So I didn't really think about
*  like, well, you know, and I remember talking to people at the time, it's like, wow, that's a lot
*  of money. But then I really like my blog, right? Like, do I want to sell my blog, because it
*  wouldn't really belong to me anymore at that point. And one of the guidelines that I like to I don't
*  like to give advice to people a lot. But one of the pieces of advice I do give because I do think
*  it's really true, and it's generally helpful is whenever you're looking at a set of decisions,
*  like, oh, gosh, I do a B or C, you got to pick the thing that's a little scarier in that list,
*  because not, you know, not like jump off a cliff scary, but the thing that makes you nervous,
*  because if you pick the safe choice, it's usually you're not really pushing, you're not pushing
*  yourself, you're not choosing the thing that's going to help you grow. So for me, the scarier
*  choice was to say no, I was like, well, no, let's just see where this is going, right, because then
*  I own it. I mean, it belongs to me, it's my thing. And I can just take it and some other logical
*  conclusion, right? Because imagine how different the world would have been had I said yes,
*  and sold the blog. It's like there probably wouldn't be stack overflow. Yeah, you know,
*  a lot of other stuff would have changed. So for that particular decision, I think it was that same
*  rule, like what scares me a little bit more do the thing that scares you. Yeah. So speaking of which
*  startups, I think there's a specific some more general questions that a lot of people would be
*  interested in. You've started stack overflow, you started discourse. So what's the is one,
*  two, three guys, whatever it is in the beginning, what was that process like?
*  Do you start talking about it? Do you start programming? Do you start like where's the
*  birth and the catalyst that actually I can talk about it in context of a stack overflow and
*  discourse. So I think the key thing initially is there is a problem something that some state of
*  the world that's unsatisfactory to the point that like you're upset about it, right? Like in that
*  case, it was experts exchange. I mean, Joel's original idea because I approached Joel's like,
*  look, Joel, I have all this energy behind my blog. I want to do something. I want to build something,
*  but I don't know what it is because I'm not I'm honestly not a good idea person. I'm really not.
*  I'm like the execution guy. I'm really good at execution, but I'm not good at like blue
*  sky ideas. Not my forte, which is another reason why I like the community feedback because they
*  blue sky all day long for you. Right. So when I can just go in and cherry pick a blue sky idea from
*  community, even if I have to spend three hours reading to get one good idea, it's worth it, man.
*  But anyway, so the idea from Joel was, hey, experts exchange. It's got great data, but the
*  experience is hideous, right? It's trying to trick you. It feels like you use car salesmen. It's just
*  bad. So I was like, oh, that's awesome. It feeds into community. It feeds into like, you know,
*  we can make creative commons. So I think the core is to have a really good idea that you feel very
*  strongly about in the beginning that like there's a wrong in the world that we will an injustice
*  that we will write through the process of building this thing for discourse. It was like, look,
*  there's no good software for communities to just hang out and like do stuff, right? Like whether
*  it's problem solving, startup, whatever forms are such a great building block of online community.
*  And they're hideous. They were so bad, right? It was embarrassing. Like I literally was embarrassed
*  to be associated with this software, right? I was like, we have to have software that you'd be proud
*  of. It's like, this is competitive with Reddit. This is competitive with Twitter. This is competitive
*  with Facebook, right? I would be proud to have the software on my site. So that was the genesis of
*  discourse was feeling very strongly about there needs to be a good solution for communities.
*  So that's step one, Genesis. You feel super strongly about right. And then people galvanize
*  around the idea. Like Joel was already super excited about that idea. I was excited about the
*  idea. So with the forum software, I was posting on Twitter, I had researched as part of my research,
*  I start researching the problem, right? I found a game called forum wars, which was a parody of
*  forum. It's still very, very funny of like forum behavior circle, like I would say 2003.
*  It's age some right? Like the behavior is a little different in there of Twitter, but it was awesome.
*  It was very funny. And it was like a game is like an RPG and it had a forum attached to it. So it
*  was like a game about forums with a forum attached. It was like, this is awesome, right? This is so
*  cool. And the founder of that company or that project, it wasn't really a company contacted
*  me. This guy, Robin Ward from Toronto is, Hey, you know, I saw you've been talking about forums.
*  And like, I really love that problem space. It's like, I'd still love to build really good
*  forum software because I don't think anything else there's any good. And I was like, awesome.
*  At that point, I was like, we're starting a company because like, I couldn't have wished for a
*  better person to walk through the door and say, I'm excited about this too. Same thing with Joel,
*  right? I mean, Joel is a legend in the industry, right? So when he walked through, I'm excited
*  about this problem. It's like me too, man, we can do this. Right? So that to me is the most important
*  step. It's like having it, you're super excited about and another person, a co-founder, right?
*  Because again, you get that dual leadership, right? Of like, am I making a bad decision?
*  Sometimes it's nice to have checks of like, is this a good idea? I don't know. Right.
*  So those are the crucial seeds, but then starting to build stuff, whether it's you programming,
*  there is prototyping. So there's tons of research. There's tons of research. Like what's out there
*  that failed? Because a lot of people look at successes. Oh, look at how successful X is.
*  Everybody looks at the successes. Those are boring. Show me the failures. Because that is
*  what's interesting. That's where people were experimenting. That's where people were pushing.
*  But they failed, but they probably failed for reasons that weren't directly about the quality
*  of their idea. Right? So look at all the failures. Don't just look what everybody looks at, which is
*  like, oh gosh, look at all these successful people. Look at the failures. Look at the things that
*  didn't work. Research the entire field. And so that's the research that I was doing that led me to
*  Robin, right? Was that. And then when we, for example, we did a Stack Overflow, we're like,
*  okay, well, I really like elements of voting and digging Reddit. I like the Wikipedia. Everything's
*  up to date. Nothing is like an old tombstone that has horrible out of date information.
*  We know that works. Wikipedia is an amazing resource. Blogging, the idea of ownership is
*  so powerful. Right? Like, oh, I, I, Joe wrote this and look how good Joe's answer is. Right? Like
*  all these concepts were rolling together, researching all the things that were out there
*  that were working and why they were working and trying to like fold them into that. Again,
*  that Frankenstein's monster of what Stack Overflow is. And by the way, that wasn't a free decision
*  because there's still a ton of tension in the Stack Overflow system. There's reasons people
*  complain about Stack Overflow because it's so strict, right? Why is it so strict? Why
*  you guys always closing my questions? It's because there's so much tension that we built into the
*  system around like trying to get good, good results out of the system. And, you know, it,
*  it's not a free, that stuff doesn't come for free, right? It's not like we, we're all have
*  perfect answers and nobody will have to get their feelings hurt or nobody will have to get down
*  voted. Like that. It doesn't work that way. Right? Like, so this is an interesting point on a small
*  tangent. You write about anxiety. So I've posted a lot of questions and written answers on Stack
*  Overflow and the questions I usually go to something very specific to something I'm working on.
*  This is something you talk about that really the goal of Stack Overflow isn't about, is to write a
*  question not, that's not about you. It's about the question that will help the community in the future.
*  Right. But that's a tough sell, right? Because people are like, well, you know, I don't really
*  care about the community. What I care about is my problem. My problem. And that's fair, right? It's
*  sort of that again, that tension, that balancing active, we want to help you, but we also want to
*  help everybody that comes behind you, right? The long line of people are going to come up and say,
*  Oh, I kind of have that problem too. Right. And if nobody's ever going to come up and say, I have
*  this problem too, then that question shouldn't exist on Stack Overflow because the question is
*  too specific. And then even that's tension, right? How do you judge that? How do you know
*  that nobody's ever going to have this particular question again? So there's a lot of tension in the
*  system. Do you think that anxiety of asking the question, the anxiety of answering that tension
*  is inherent to programmers, is inherent to this kind of process? Or, or can it be improved? Can it
*  be happy land where the, that tension is not quite so harsh? I don't think Stack Overflow can
*  totally change the way it works. One thing they are working on finally is the Ask page had not
*  changed since 2011. I'm still kind of bitter about this because I feel like you have a Q&A system
*  and what are the core pages in a Q&A system? Well, first of all, the question, all the answers and
*  all the, also the Ask page, particularly when you're a new user or someone trying to ask a
*  question, that's the point at which you need the most help. And we just didn't adapt with the times,
*  but the good news is they're working on this from what I understand, and it's going to be a more
*  wizard based format. And you could envision a world where as part of this wizard based program,
*  when you're asking questions, okay, come up with a good title, what are good words to put in the
*  title? One word that's not good to put in the title is problem. For example, I have a problem.
*  Oh, you have a problem. Okay. A problem. That's great. Right? Like you need specifics, right?
*  Like, so it's trying to help you make a good question title. For example, that step will be
*  broken out, all that stuff. But one of those steps in that wizard of asking could say, Hey,
*  I'm a little nervous. You know, I've never done this before. Can you put me in a queue for like
*  special mentoring? Right? You could opt in to a special mentor. I think that would be fantastic.
*  Like I don't have any objection to that at all in terms of being an opt in system. Because there
*  are people that are like, you know, I just want to help them. I want to help a person no matter
*  what I want to go above and beyond. I want to spend like hours with this person. It depends
*  what their goals are. Right? Like a great idea. Who am I to judge? Right? So that's fine. It's
*  not precluded from happening, but there's a certain big city ethos that we started with, like, look,
*  we're New York City. You don't come to New York City and expect them to be, Oh, welcome to the
*  city. Joe, how's it going? Come on in. Let me show you around. That's not how New York City works.
*  Right? I mean, and you know, again, New York City is a reputation for being rude, which I actually
*  don't think it is having been there fairly recently. It's not rude. People are just like
*  going about their business. Right? Look, look, I have things to do. I'm busy. I'm a busy professional,
*  as are you. And since you're a busy professional, certainly when you ask a question, you're gonna
*  ask the best possible question, right? Because you're a busy professional and you would not
*  accept anything less than a very well-witted question with a lot of detail about why you're
*  doing it, what you're doing, what you researched, what you found. Right? Because you're a professional
*  like me. Right. And this rubs people sometimes the wrong way. And I don't think it's wrong to say,
*  look, I don't want that experience. I want just a more chill place for beginners. And I still think
*  sacrifice is not was never designed for beginners. Right? There's this misconception that, you know,
*  even Joel says something, Oh yeah, stack overflow for beginners. And I think if you're a prodigy,
*  it can be right. But that's not really representative. Right. Like I think as a
*  beginner, you want a totally different set of tools. You want like live screen sharing,
*  live chat. You want access to resources. You want a playground, like a playground you can
*  experiment in and like test and all this stuff that we just don't give people because that was
*  never really the audience that we were designing stack overflow for. That doesn't mean it's wrong.
*  And I think it would be awesome if there was a site like that on the internet or if stack
*  overlays and Hey, you know, we're going to start doing this. That's fine too. You know, I'm not
*  there. I'm not making those decisions, but I do think the pressure, the tension that you described
*  is there for people to be. Look, I'm a little nervous because I know I gotta do my best work.
*  Right. The other one is something you talk about, which is also really interesting to me is duplicate
*  questions or do it's a, it's a really difficult problem that you highlight super pro super hard.
*  Like you could take one little topic and you could probably write 10, 20, 30 ways of asking
*  about that topic and there will be all different. I don't know if there should be one page that
*  answers all of it. Is there a way that stack overflow can help disambiguate, like separate
*  these duplicate questions or connect them together or is it a totally hopeless, difficult, impossible
*  task? I think it's a very, very hard computer science problem. And partly because people are
*  very good at using completely different words. It always amazed me on second overflow. You'd have
*  two questions that were functionally identical and one question had like zero words in common
*  with the other question. Like, Oh my God, from a computer science perspective, how do you even
*  begin to solve that? And it happens all the time. People are super good at this, right?
*  Accidentally at asking the same thing in like 10, 20 different ways. And the other complexity
*  is we want some of those duplicates to exist because if there's five versions with different
*  words, have those five versions point to the one centralized answer, right? It's like, okay,
*  this is duplicate. No worries. This here's, here's the answer that you wanted over here on this,
*  this, you know, the prime example that we want to have rather than having 10 copies of the question
*  and the answer, because if you have 10 copies of the question answer, this also devalues the
*  reputation system, which programmers hate. As I previously mentioned, you're getting reputation
*  for an answer that somebody else already gave. It's like, well, it's an answer, but somebody
*  else already gave that answer. So why are you getting a reputation for the same answer as the
*  other guy gave it four years ago? People get offended by that, right? So the reputation system
*  itself adds tension to the system in that the people who have a lot of reputation become very
*  incentivized to enforce the reputation system. And for the most part, this good, I know it sounds
*  weird, but for most parts, like look, strict systems, I think to use deck overflow, you have
*  to have the idea that, okay, strict systems ultimately work better. And I do think in programming,
*  you're familiar with loose typing versus strict typing, right? The idea that you can declare a
*  variable, not declare a variable rather, just start using a variable and okay, I see it's
*  implicitly an integer. Bam, awesome. Duck equals five. Well, duck is now an integer five, right?
*  And you're like, cool, awesome, simpler, right? Why would I want to worry about typing? And for
*  a long time, like in the Ruby community, they're like, yeah, this is awesome. Like you just do a
*  bunch of unit testing, which is testing your program's validity after the fact to catch any
*  bugs that, that, that strict typing of variables would have caught. And now you have this thing
*  called TypeScript from Microsoft, from the guy who built C sharp Anders, who's one of the greatest
*  minds in software development, right? Like in terms of language design and says, no, no, no,
*  we want to bolt on a strict type system to JavaScript because it makes things better.
*  And now everybody's like, oh my God, we, we deployed TypeScript and found 50 lane bugs
*  that we didn't know about, right? Like this is super common. So I think there is a truth
*  in programming that strictness, it's not the goal. We're not saying be super strict. The
*  strictness is correct. No, it's no, no strictness produces better results. That's what I'm saying.
*  Right? So strict typing of variables, I would say you almost universally have consensus now is
*  basically correct. Should be that way in every language, right? Duck equals five should generate
*  an error because you know, you didn't declare, you didn't tell me that duck was an integer,
*  right? That's a bug, right? Or maybe you mistype, you type deck, right? Instead of duck, right?
*  You never know this happens all the time. Right? So with that in mind, I will say that the strictness
*  of the system is correct. Now that doesn't mean cruel. That doesn't mean mean that doesn't mean
*  angry. It just means strict. Okay. So I think where there's misunderstanding is and people get
*  cranky, right? Like another question you asked is like, why are programmers kind of mean sometimes?
*  Well, who do programmers work with all day long? So I have a theory that if you're at a job
*  and you work with assholes all day long, what do you eventually become an asshole, an asshole?
*  And what is the computer except the world's biggest asshole? Because the computer has no time for your
*  bullshit. The computer, the minute you make a mistake, everything else crashing down, right?
*  One semi-colon has crashed space missions, right? So that's normal. So you begin to internalize that
*  you begin to think, oh, my coworker, the computer is super strict and kind of a jerk about everything.
*  So that's kind of how I'm going to be because I work with this computer and I have to exceed
*  to its terms on everything. So therefore you start to absorb that and you start to think,
*  oh, well being really strict arbitrarily is really good. An error of error code 56249 is a completely
*  good error message because that's what the computer gave me. Right? So you kind of forget
*  to be a person at some level. And you know how they say great detectives, internalized criminals
*  and kind of are criminals themselves. Like this trope of the master detective is good because
*  you can think like the criminal. Well, I do think that's true of programmers. Really good programmers
*  think like the computer because that's their job. But if you internalize it too much, you become
*  the computer, you kind of become a jerk to everybody because that's what you've internalized.
*  You're almost not a jerk, but you have no patience for a lack of strictness.
*  Yes. As you said, it's not out of a sense of meanness. It's accidental, but I do believe it's
*  an occupational hazard or being a programmer is you start to behave like the computer.
*  You're very unforgiving. You're very terse. You're very, oh, wrong. Incorrect. Move on. It's like,
*  well, can you help me? Like, what could I do to fix? No, wrong. Next question. Right? Like that's
*  normal for the computer, right? Just fail next. Right? Like I don't know if you remember in
*  Saturday Night Live, like in the nineties, they had this character was an IT guy. Yeah. The move
*  guy move. Move. Was that Jimmy Fallon? No, no. Who played him? Okay. Yeah. I remember move. Right.
*  He had no patience for it might have been mad TV actually. Or not. TV might have been might have
*  been. But anyway, that was the that's always been the perception, right? You start to behave like
*  the computer. It's like, oh, you're wrong out of the way. You know, you've written so many
*  blog posts about programming about programs, programming, programmers. What do you think makes
*  a good, let's start with what makes a good solo programmer? Well, I don't think you should be a
*  solo programmer. I think to be a good solo programmer, it's kind of like what I talked about.
*  Well, not on Mike, but one of the things John Carmack, one of the best points he makes in the
*  book, Masters of Doom, which is a fantastic book, and anybody listening to this who hasn't read it,
*  please read it. It's such a great book is that at the time they were working on stuff like
*  Wolfenstein and doom, like they didn't have the resources that we have today. They didn't have
*  Stack Overflow. They didn't have Wikipedia. They didn't have like discourse forums. They didn't have
*  places to go to get people to help them, right? They had to work on their own. And that's why it
*  took a genius like Carmack to do this stuff, because you had to be a genius to invent from
*  first principles. A lot of stuff he was he was like the hacks he was coming up with were genius,
*  right? Genius level stuff, but you don't need to be a genius anymore. And that means not working
*  by yourself. You have to be good at researching stuff online. You have to be good at asking
*  questions, really good questions that are really well researched, which implies, oh, I went out
*  and researched for three hours before I wrote this questions. Like that's what you should be doing,
*  because that's what's going to make you good, right? To me, this is the big difference between
*  programming in like the 80s versus programming today is like you kind of had to be by yourself
*  back then. Like where would you go for answers? I remember in the early days when I was learning
*  visual basic for Windows, like I would call the Microsoft helpline on the phone when I had like
*  program because I was like, I don't know what to do. So I would like go and call and they had these
*  huge phone banks and like, can you imagine how alien that is now? Like who would do that? Right?
*  Like that's crazy. So there was just nowhere else to go when you got stuck, right? Like I had the
*  books that came with it. I read those study those religiously. I just saw a post from Steve
*  Sanofsky that said this C++ version seven came with like 10,000 pages of written material
*  because where else were you going to figure that stuff out? Go to the library?
*  I mean, you didn't have Wikipedia. You didn't have, you know, read it. You know, where to go to
*  answer these questions. So you've talked about through the years, basically not having an ego
*  and not thinking that you're the best programmer in the world. And so it was kind of
*  just looking to improve to become a better programmer than you were yesterday. So how
*  have you changed as a programmer and as a, as a thinker designer around programming over the past,
*  what is it 15 years really of being a public figure?
*  I would say the big insight that I had is eventually as a programmer, you have to kind of
*  stop writing code to be effective, which is kind of disturbing. Um, cause you really love it. And
*  but you realize like being effective at programming, at programming in the general sense,
*  doesn't mean writing code. And a lot of times you can be much more successful by not writing code
*  and writing code in terms of just solving the problems you have, essentially hiring people
*  that are really good and like setting them free and like giving them basic direction, right? Like
*  on strategy and stuff. Cause a lot of the problems you encounter aren't necessarily solved to like
*  really gnarly code. They're solved by conceptual solutions, which can then be turned into code.
*  But are you even solving the right problem? I mean, so I would say for me, the main insight
*  I have is, is, is to succeed as a programmer. You eventually kind of stop writing code. That's
*  going to sound discouraging probably to people hearing, but I don't mean it that way. What I mean
*  is that you're coding at a higher level language eventually like, okay, so we're coding an assembly
*  language, right? That's the beginning, right? You're hard coded to the architecture. Then you have
*  stuff like C where it's like, wow, we can abstract across the architecture, the right code. I can
*  then compile that code for arm or, you know, you know, whatever, you know, X86 or whatever else is
*  out there. And then even higher level net, right? Like you're looking at like Python, Ruby,
*  interpreting languages. And then to me as a programmer, like, okay, I want to go even higher.
*  I want to go higher than that. How do I abstract higher than language? It's like, well, you abstract
*  in spoken language and written language, right? Like you're sort of inspiring people to get things
*  done, giving them guidance. Like, what if we did this? What if we did this? Um, you're writing in
*  the highest level language that there is, which is for me, English, right? Whatever your spoken
*  language is. So it's all about being effective, right? And I think, uh, uh, uh, Patrick McKenzie,
*  patio 11 on, on hacker news and works at Stripe has a great post about this, of how calling
*  yourself a programmer is a career limiting move at some level. Once you get far enough from your
*  current, I really believe that. And again, I apologize. This is sound discouraging. I don't
*  mean it to be, but he's so right because all the stuff that goes on around the code, like the people,
*  like that's another thing. If you look at my early blog, it was about, wow, programming is about
*  people more than it's about code, which doesn't really make sense, right? But it's about, can these
*  people even get along together? Can they understand each other? Can you even explain to me what it is
*  you're working on? Are you solving the right problem? People were right. Another classic
*  program book, which again, up there with code complete, please read people where it's that
*  software is people, right? People are the software first and foremost. So a lot of the skills that I
*  was working on early in the blog were about figuring out the people parts of programming,
*  which were the harder parts. The hard part of programming, once you get to a certain skill
*  level in programming, you can pretty much solve any reasonable problem that's put in front of you.
*  You're not writing algorithms from scratch, right? That just doesn't happen. So any sort of
*  reasonable problem put in front of you, you're going to be able to solve. But what you can't solve is
*  our manager is a total jerk. You cannot solve that with code. That is not a code solvable problem.
*  And yet that will cripple you way more than, oh, we had to use this stupid framework I don't like,
*  or Sam keeps writing bad code that I hate, or Dave is off there in the wilderness writing God
*  knows what, right? These are not your problems. Your problem is your manager or a coworker is so
*  toxic to everybody else in your team that nobody can get anything done because everybody's so
*  stressed out and freaked out, right? These are the problems that you have to attack.
*  Absolutely. And so as you go to these higher level abstractions, as you've developed as a programmer
*  to higher, higher level abstractions and go into natural language, you're also the guy who
*  kind of preached building it, diving in and doing it and learn by doing.
*  Do you worry that as you get to higher, higher level abstractions, you lose track
*  of the lower level of just building? Do you worry about that? Even not maybe now,
*  but 10 years from now, 20 years from now? Well, no, I mean, there is always that paranoia and,
*  oh gosh, I don't feel as valuable since I'm not writing code. But for me, like when we started
*  the discourse project, it was Ruby, which I didn't really know Ruby. I mean, as you pointed out,
*  and this is another valuable observation in Stack Overflow, you can be super proficient,
*  for example, C sharp, which I was working in, that's what we built Stack Overflow and still
*  is written in and then switch to Ruby and you're a newbie again, right? Like I'm but you have the
*  framework. I know what a for loop is. I know what recursion is. I know, you know, what a, what a
*  stack traces, right? Like I have all the fundamental concepts to be a programmer. I just don't know
*  Ruby. So I'm still on a higher level. I'm not like a beginner beginner. Like you're saying,
*  I'm just like, I need to apply my programming concepts already know to Ruby. Well, so there's
*  a question that's really interesting. So looking at Ruby, how do you go about learning enough that
*  your intuition can be applied? Well, that's the thing that's what I was trying to get to is like,
*  what I realized when I started with just me and Robin, I realized if I bother Robin, I am now
*  costing us productivity, right? Every time I go to Robin, rather than building the the our first
*  alpha version of discourse, he's now answering my stupid questions about Ruby. Is that a good
*  use of his time? Is that a good use of my time? And the answer to both of those was resoundingly
*  no. Right? Like we were getting to an alpha and it was pretty much just, okay, we'll hire more
*  programmers, right? Like we eventually hired Neil and then eventually Sam, who came in as a co
*  founder. I actually was Sam first, then Neil later. But the answer to the problem is just hire other
*  competent programmers, not like teach. Now I shall pull myself up by my bootstraps and and
*  learn Ruby. But at some point, writing code becomes a liability to you in terms of getting
*  things done. There's so many other things that go on in the project, like building the prototype.
*  Like you mentioned, like, well, how do you, if you're not writing code, how does everybody keep
*  focus on like, what, what, what are we building? Well, first, basic mockups and research, right?
*  What do we even want to build? There's a little bit of that that goes on. But then very quickly,
*  you get to the prototype stage, like build a prototype. Let's iterate on the prototype really,
*  really rapidly. And that's what we do with discourse. And that's what we demoed to get our
*  seed funding for discourse was the the alpha version of discourse that we had running and ready
*  to go. And it was very, it was bad. I mean, it was, I'll just tell you, it was bad. I have, we have
*  screenshots of it. I'm just like embarrassed to look at it now. But it was the prototype. We were
*  figuring out like what's working, what's not working, because there's such a broad gap between
*  between the way you think things will work in your mind or even on paper, and the way they work once
*  you sit and live in the software, like actually spend time living and breathing on software,
*  so different. So my philosophy is get to a prototype. And then what you're really optimizing
*  for speed of iteration, like how you can turn the crank, how quickly can we iterate, that's the
*  absolutely critical metric of any software project. And I had a tweet recently that people liked,
*  and I totally this is so fundamental to what I do is like, if you want to measure the core
*  competency of any software tech company, it's the speed at which somebody can say, Hey, we really
*  need this word in the product change this word, right, because it will be more clear to the users
*  like what like instead of respond, it's reply or something. But there's some from the conception
*  of that idea to how quickly that single word can be changed in your software rolled out to users,
*  that is your lifecycle. That's your health, your heartbeat. If your heartbeat is like super slow,
*  you're basically dead. No, seriously, like if it takes two weeks, or even a month to get that
*  single word change, there was Oh, my God, this great idea. That word is so much clearer. I'm
*  talking about like a super like everybody's on board for this change. It's not like let's just
*  change the word because we're bored. Like this is an awesome change. And then it takes a month to
*  roll out. It's like, well, you're dead. Like you can't iterate, you can't have how you can do
*  anything, right? Like, so anyway, about the heartbeat, it's like get the prototype and then
*  iterate on it. That's that's what I view is like the central tenet of modern software development.
*  That's fascinating. You put it that way. It's actually so I work in a build autonomous
*  vehicles. And when you look at what maybe compare Tesla to most other automakers,
*  the psych, the whatever the heartbeat for Tesla is literally days now in terms of they can
*  over the air deploy software updates to all their vehicles, which is markedly different than every
*  other automaker, which takes years to update a piece of software. And so and that's reflected
*  in everything that's the final product that's reflected in really how slowly they adapt to the
*  times. And to be clear, I'm not saying being a hummingbird is the goal either. It's like you
*  don't want to heartbeat. That's like so fast. It's like you're you're you're just freaking out. But
*  like it is a measure of health. You should have a healthy heartbeat. It's up to for people listening
*  to decide what that means. But it has to be healthy. It has to be reasonable because otherwise you're
*  just going to be frustrated because like that's how you build software. You make mistakes. You
*  roll it out. You live with it. You see what it feels like and say, oh, God, that was a terrible
*  idea. Oh, my gosh, this could be even better if we did. Why? Right. You turn the crank and then
*  the more you do that, the faster you get ahead of your competitors ultimately, because you're
*  it's rate of change. Right. Delta V. Right. How fast are you moving? Well, within a year,
*  you're going to be miles away by the time they catch up with you. Right. Like that's the way it
*  works. And plus users like as a software developer, I love software that's constantly changing
*  because I don't understand people get super pissed off when like, oh, they change the software on
*  me. How dare they? I'm like, yes, change the software, change it all the time, man. That's
*  that's what makes this stuff great is that it can be changed so rapidly and become something that
*  that is greater than it is now. Now, granted, there's some changes that suck. I admit I've
*  seen it many times. But in general, it's like that's what makes software cool. Right. Is that it is so
*  malleable. Like fighting that is like weird to me because it's like, well, you're fighting the
*  essence of the thing that you're building. Like that doesn't make sense. You want to really embrace
*  that not not to be a hummingbird, but like embrace it to a healthy cycle of your heartbeat. Right.
*  So you talk about that people really don't change. It's true. That's why probably a lot of the stuff
*  you write about in your blog probably will remain true. There's a flip side of the coin. People
*  don't change. So investing and understanding people is like learning Unix in 1970, because
*  nothing has changed. Right. Like all those things you've learned about people will still be valid
*  34 years from now. Whereas if you learn the latest JavaScript framework, that's going to be good for
*  like two years. Right. Exactly. So but if you look at the future of programming, so there's a people
*  component, but there's also the technology itself. Do you what do you see as the future of programming?
*  Will it change significantly? Or as far as you can tell, people are ultimately programming and so it
*  it's not something that you foresee changing in any fundamental way. Well, you got to go look back
*  on sort of the basics of programming. And one of the things that always shocked me is like
*  source control. Like I didn't learn anything about source control. I graduated from college in 1992,
*  but I remember hearing from people like in as late as like 1998, 1999, like even maybe today,
*  they're not learning source control. And to me, it's like, well, how can you not learn
*  source control that is so fundamental to working with other programmers,
*  working in a way that you don't lose your work, like just just basic soft, the bed literal bedrock
*  software development is source control. Now you compare today like GitHub, right, like Microsoft
*  bought GitHub, which I think was incredibly smart acquisition move on their part. Now they have
*  anybody who wants like reasonable source controls and go sign up on GitHub, it's all set up for you.
*  Right. There's tons of walkthroughs, tons of tutorials. So from the concept of like,
*  has programming advanced from say 1999? It's like, well, hell we have GitHub. I mean, my God,
*  yes, right. Like it's massively advanced over over what it was. Now as to whether programming
*  is significantly different, I'm going to say no, but I think the baseline of like what we view is
*  like fundamentals will continue to go up and actually get better. Like source control, for
*  example, that's one of the fundamentals that has gotten I mean, hundreds of orders of magnitude
*  better than it was 10, 20 years ago. So those are the fundamentals. Let me introduce two things
*  that maybe you can comment on. So one is mobile phones. So that could fundamentally transform what
*  what programming is, or maybe not. Maybe you can comment on that. And the other one is artificial
*  intelligence, which promises to in some ways to do some of the programming for you is one way to
*  think about it. So it's really what a programmer is, is using the intelligence that's inside your
*  skull to do something useful. The hope with artificial intelligence is that it does some of
*  the useful parts for you the way you don't have to think about it. So do you do you see smartphones
*  the fact that everybody has one, and they're getting more and more powerful as potentially
*  changing programming? And do you see AI is potentially changing? Okay, so that's good. So
*  smartphones have definitely changed. I mean, since you know, I guess 2010 is when they really
*  started getting super popular. I mean, in the last eight years, the world has literally changed,
*  right? Like everybody carries a computer around. And that's normal. I mean, that is such a huge
*  change in society. I think we're still dealing with a lot of the positive negative ramifications of
*  that, right? Like everybody's connected all the time. Everybody's on the computer all the time.
*  That was my dream world as a geek, right? But it's like, be careful what you ask for, right? Like,
*  wow, now everybody has a computer. It's not quite the utopia that we thought it would be, right?
*  Computers can be used for a lot of stuff that's not necessarily great. So to me, that's the central
*  focus of the smartphone is just that it puts a computer in front of everyone granted a small
*  touchscreen, smallish touchscreen computer. But as for programming, like, I don't know, I don't think
*  that I've kind of over time come to subscribe to the Unix view of the world when it comes to
*  programming. It's like, you want to teach these basic command line things. And that is just what
*  programming is going to be for, I think, a long, long time. I don't think there's any magical,
*  like, visual programming that's going to happen. I just, I don't know, I've over time have become
*  a believer in that Unix philosophy of just, you know, they kind of had a right with Unix.
*  That's going to be the way it is for a long, long time. And we'll continue to, like I said,
*  raise the baseline, the tools will get better, it'll get simpler, but it's still fundamentally
*  gonna be command line tools, you know, make fancy IDs. That's kind of it for the foreseeable future.
*  I'm not seeing any visual programming stuff on the horizon, because you kind of think, like,
*  what do you do on a smartphone that will be directly analogous to programming?
*  Like, I'm trying to think, right? Like, and there's really not much.
*  So, not necessarily analogous to programming, but the kind of things that, the kind of programs you
*  need to write might need to be very different. And the kind of languages, I mean, but I probably
*  also subscribe to the same, just because everything in this world might be written in JavaScript.
*  Oh, yeah, that's definitely, that's already happening. I mean, discourse is a bet on,
*  discourse is itself JavaScript is another bet on that side of the table. And I still
*  try to believe in that. So I would say smartphones have mostly a cultural shift more than a programming
*  shift. Now, your other question was about artificial intelligence and like,
*  sort of devices predicting what you're going to do. And I do think there's some strength to that.
*  I think artificial intelligence kind of overselling it in terms of what it's doing. It's more like
*  people are predictable, right? People do the same things. Like, let me give you an example.
*  One, one check we put into discourse that's in a lot of big commercial websites is, say you log in
*  from New York City now, and then an hour later, you log in from San Francisco. It's like, well,
*  that's interesting. How did you get from New York to San Francisco in one hour? So at that point,
*  you're like, okay, this is a suspicious login at that point. So we would alert you. It's like,
*  okay, but that's not AI, right? That's just a heuristic of like, how did you in one hour
*  get 2000 miles, right? That doesn't mean you grant maybe you're on a VPN, there's other ways to
*  happen. But that's just a basic prediction based on the idea that people pretty much don't move
*  around that much. Like they may travel occasionally, but like nobody, I mean, unless you're a
*  traveling salesman that's literally traveling the world every day, like there's so much repetition
*  and predictability in terms of things you're going to do. And I think good software anticipates your
*  needs. Like, for example, Google, I think it's called Google now, or whatever that Google thing
*  is that predicts your commute and predicts based on your phone location, like where are you every
*  day? Well, that's probably where you work. That kind of stuff. I do think computers can get a lot
*  better at that, but I hesitate to call it like full blown AI. It's just computers getting better
*  at like, first of all, they have a ton of data because everybody has a smartphone. Now all of
*  a sudden we have all this data that we didn't have before about location, about like, you know,
*  communication and feeding that into some basic heuristics and maybe some fancy algorithms that
*  turn it into predictions of anticipating your needs like a friend would, right? Like, oh, hey,
*  I see your home. Would you like some dinner? Right? Like, let's go get some food because that's
*  usually what we do at this time of day. Right. In the context of actually the act of programming,
*  do you see IDEs improving and making the life of programming is better? I do think that is possible
*  because there's a lot of repetition in programming. Clippy would be the bad example of,
*  oh, I see it. It looks like you're writing a for loop. But there are patterns in code, right?
*  And actually libraries are kind of like that, right? Rather than go code up your own HTTP request
*  library, it's like, well, you'd use one of the existing ones that we have. That's already a
*  trouble shot, right? It's not AI per se. It's just building better Lego bricks, bigger Lego bricks
*  that have more functionality in them. So people don't have to worry about the low level stuff as
*  much anymore. Like WordPress, for example, to me is like a tool for somebody who isn't a programmer
*  to do something. I mean, you can turn WordPress into anything. It's kind of crazy actually through
*  plugins, right? And that's not programming per se. It's just Lego bricks stacking WordPress
*  elements, right? And a little bit of configuration glue. So I would say maybe in a broader sense,
*  what I'm seeing like there'll be more gluing and less like actual programming. And that's a good
*  thing, right? Because most of the stuff you need is kind of out there already.
*  You said 1970s Unix. Do you see PHP and these kind of old remnants of the early birth of programming
*  remaining with us for a long time? Like you said, Unix in itself, do you see ultimately,
*  you know, this stuff just being there out of momentum?
*  I kind of do. I mean, I was a big believer in Windows early on and I was a big, you know,
*  I was like, Unix, what a waste of time. But over time, I've completely flipped on that where I was
*  like, okay, the Unix guys were right. And pretty much Microsoft and Windows were kind of wrong,
*  at least on the server side. And on the desktop, right, you need a GUI, you know, that stuff. And
*  you have the two philosophies like Apple built on Unix, effectively Darwin. And on the desktop,
*  it's a slightly different story. But on the server side, where you're going to be programming.
*  Now it's a question of where the programming is going to be. There's going to be a lot more like
*  client side programming, because technically, discourse is client side programming. The way
*  you get discourse, we deliver a big ball of JavaScript, which is then execute locally.
*  So we're really using a lot more local computing power. We'll still retrieve the data. Obviously,
*  we have to display the posts on the screen and so forth. But in terms of like sorting and
*  a lot of the basic stuff, we're using the host processor. But to the extent that a lot of
*  programming is still going to be server side, I would say, yeah, the Unix philosophy definitely
*  won. And there'll be different veneers over Unix. But it's still if you if you peel away
*  one or two layers, it's going to be Unixy for a long time. I think Unix won. I mean, so definitively.
*  It's interesting to hear you say that because you've done so much excellent work on the
*  Microsoft side in terms of back end development. Cool. So what's the future hold for Jeff Atwood?
*  I mean, the discourse continuing the discourse in trying to improve conversation on the web.
*  Well, this course is what I mean is originally called a five year project,
*  then really quickly revise that to a 10 year project. So where we started in early to the
*  2013, that's when we launched the first version. So we're still, you know, five years in this is
*  the part where it starts getting good. Like we have a good product now discourse. There's any
*  any project you build in software, it takes three years to build what you wanted to build anyway,
*  like v1 is going to be terrible, which it was. But you ship it anyway, because that's how you
*  get better at stuff. It's about turning the crank. It's not about v1 being perfect, because that's
*  ridiculous. It's about v1, then let's get really good at v1.1, 1.2, 1.3, like how fast can we
*  iterate? And I think we're iterating like crazy on discourse, the point that like, it's a really
*  good product. Now we have serious momentum. And my original vision was, I want to be the WordPress
*  of discussion, meaning someone came to you and said, I want to start a blog, although the very
*  question is kind of archaic. Now it's like, who actually blogs anymore, but I wanted the answer
*  to that to be it would be WordPress normally, because that's the obvious choice for blogging
*  most of the time. But if someone said, hey, I want to I need a group of people to get together
*  and do something, the answer should be discourse, right? That should be the default answer for
*  people because it's open source, it's free, doesn't cost you anything, you control it, you can run it.
*  Your minimum server cost for discourse is five bucks a month at this point. They actually got
*  the VPS prices down, it used to be $10 a month for one gigabyte of RAM, which we were our dependent,
*  we have a heavy stack, there's a lot of stuff in discourse, you need Postgres, you need Redis,
*  you need Ruby, and Rails, you need a sidekick for scheduling. It's not a trivial amount of stuff,
*  because we were architected for like, look, we're building for the next 10 years, I don't care about
*  shared PHP hosting, that's not my model. My idea is like, hey, eventually, this is going to be very
*  cheap for everybody. And I want to build it right, using again, higher, bigger building block levels
*  right that have more requirements. And there's a WordPress model of WordPress.org,
*  WordPress.com. Is there a central hosting for discourse or no? There is, we're not strictly
*  segmenting into the open source versus the commercial side. We have a hosting business,
*  that's how discourse makes money is we host discourse instances, and we have really close
*  relationship with our customers of the symbiosis of them giving us feedback on the product.
*  We definitely wait feedback from customers a lot heavier than feedback from somebody who just
*  wanders by and gives feedback. But that's where we make all our money. But we don't have a strict
*  division. We encourage people to use discourse, like the whole point is that it's free, right?
*  You're anybody can set it up. I don't want to be the only person that hosts discourse. That's
*  absolutely not the goal. But it is a primary way for us to build a business. And it's actually kind
*  of a great business. I mean, the business is going really, really well, in terms of hosting.
*  So I used to work at Google Research is a company that's basically funded on advertisement. So it's
*  Facebook. Let me ask if you can comment on it. I think advertisement is best. So you'd be extremely
*  critical on what ads are. But at its best, it's actually serving you in a sense is giving you
*  it's connecting you to what you would want to explore. So it's like related posts or related
*  content is the same. That's the best of advertisement. So discourse is connecting people
*  based on their interests. It seems like a place where advertisement at its best
*  could actually serve the users. Is that something that you're considering thinking about as a way to
*  bring to financially support the platform? That's interesting, because I actually have
*  a contrarian view of advertising, which I kind of agree with you. I recently installed that blocker
*  like reluctantly because I don't like to do that. But like the performance of the ads, man, like
*  they're so heavy now and like it's just crazy. So like it's almost like a performance argument
*  more than like I actually am pro ads. And I contrary, I have a contrarian viewpoint. I agree
*  with you. If you do ads, right, it's serving you stuff you would be interested in anyway. Like I
*  don't mind that that actually is kind of a good thing. So plus I think it's it's rational to want
*  to support the people that are doing this work through seeing their ads. And but that said,
*  I run ad block now, which I didn't want to do. But I was convinced by all these articles, like 30,
*  40 megabytes of stuff just to serve you ads. Yeah, it feels like as now or like the experts
*  exchange of whenever you start to stack overflows, it's a little bit. It's all there's so many
*  companies in ad tech, though. It's embarrassing. Like you can do that. Have you seen those logo
*  charts of like just the whole page is like you can't even see them. They're so small. There's
*  so many companies in the space. But since you brought it up, I do want to point out that very,
*  very few discourse sites actually run using an ad support model. It's not effective. Like it's
*  too diluted. It's too weird. It doesn't pay well. And like users hate it. So it's a combination of
*  like users hate it. It doesn't actually work that well in practice. Like in theory. Yes, I agree with
*  you. If you had clean, fast ads that were exactly the stuff you would be interested in. Awesome.
*  We're so far from that, though. Right. Like Google does an OK job retargeting and stuff like that.
*  But in the in the real world, discourse sites rarely can make ads work. It just doesn't work
*  for so many reasons. But you know, it does work is subscriptions, Patreon, affiliate codes for like
*  Amazon of like just, oh, here, here's a cool yo yo click. And then you click and go to Amazon and
*  they get a small percentage of that, which is fair, I think, because you saw the yo yo on that site
*  and you click through and you bought it. Right. That's fair for them to get five percent of that
*  or two percent of that, whatever it is. Those things definitely work. In fact, a site that I
*  used to participate in a lot, I helped the owner. One of the things I got them switched to discourse,
*  I basically paid them to switch to discourse because I was like, look, you guys going to switch.
*  I can't come here anymore on this terrible software. But I was like, look, and on top of that,
*  like you're serving people ads that they hate. Like you should just go full on Patreon because
*  he had a little bit of Patreon. Go full on Patreon. Do the Amazon affiliates thing for any Amazon links
*  that get posted and just do that and just triple down on that stuff. And that's worked really well
*  for them and this creator in particular. So that stuff works. But traditional ads, I mean,
*  definitely not working, at least on discourse. So last question. You've created the code keyboard.
*  I've programmed most of my adult life in a Kinesis keyboard. I have one upstairs now.
*  Can you describe what a mechanical keyboard is and why is it something that makes you happy?
*  Well, you know, this is another fetish item, really. Like it's not required. You can do
*  programming on any kind of keyboard, right? Even like an on screen keyboard. Oh God,
*  that's terrifying. But you could touch. I mean, if you look back to the early days,
*  competing there were chiclet keyboards, which are I mean, those are awful. Right. But what's
*  a chiclet keyboard? Oh God. Okay. Well, it's just like thin rubber membranes. Oh, the rubber ones.
*  Oh no. Super bad. Right. Yeah. So it's a fetish item. All that really says is, look,
*  I care really about keyboards because keyboard is the primary method of communication with computer.
*  Right. So it's just like having a nice mic for this podcast. You want a nice keyboard,
*  right? Because it has very tactile feel. I can tell exactly when I press the key. I get that
*  little click. So, oh, and it feels good. And it's also kind of a fetish item. It's like, wow,
*  I care enough about programming that I care about the tool, the primary tool that I use to
*  communicate with the computer, make sure it's as good as it feels good to use for me. And like,
*  I can be very productive with it. So to be honest, it's a little bit of a fetish item,
*  but a good one. It indicates that you're serious in the case you're interested. It indicates that
*  you care about the fundamentals because you know what makes you a good programmer? Being able to
*  type really fast, right? Like this is true, right? So a core skill is just being able to type fast
*  enough to get your ideas out of your head into the code base. So just practicing your typing can make
*  you a better programmer. It is also something that makes you, well, makes you enjoy typing,
*  correct? The actual act, something about the process. Like I play piano, it's tactile.
*  There's a tactile feel that ultimately feeds the passion, makes you happy.
*  Right? No, totally. That's it. I mean, and it's funny because artisanal keyboards have exploded.
*  Like Massdrop has gone ballistic with this stuff. There's probably like 500 keyboard projects on
*  Massdrop alone. And there's some other guy I follow on Twitter, I used to write for this site,
*  The Tech Report, way back in the day. And he's like every week, he's just posting like what I call
*  keyboard porn of like, just cool keyboards. Oh my God, those look really cool. Right? Like,
*  that's like how many keyboards this guy has. It's got me with yo-yos. How many yo-yos do you have?
*  How many do you need? Well, technically one, but I like a lot. I don't know why. So same thing with
*  keyboards. So yeah, they're awesome. Like I highly recommend anybody who doesn't have a mechanical to
*  research it, look into it and see what you like. And you know, it's ultimately a fetish item,
*  but I think these sort of items, these religious artifacts that we have are part of what makes us
*  human. Like that part's important, right? It's kind of what makes life worth living.
*  Yeah. It's not necessary in the strictest sense, but ain't nothing necessary if you think about it.
*  Right? Like, so yeah, why not? So sure. Jeff, thank you so much for talking today.
*  Yeah, you're welcome. Thanks for having me.

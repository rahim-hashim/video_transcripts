---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 5396s
Video Keywords: ['Science & Medicine', 'Technology', 'episodes']
Video Views: 501
Video Rating: None
---

# BI 037 Nathaniel Daw: Thinking the Right Thoughts
**Brain Inspired:** [June 09, 2019](https://www.youtube.com/watch?v=ffDl6XdAbQw)
*  This problem, how do you manage your computations?
*  How do you decide what to think about and what not to think about,
*  and when to think about it and when to act?
*  How does the brain do that?
*  Offers a really nice insights into all these weird phenomena like habits,
*  compulsion, and people say racism and stuff,
*  is a different way of thinking about these really deep problems.
*  We're going to look back on this and be embarrassed?
*  I think there's a hassle.
*  I'm embarrassed now.
*  I am too, yeah.
*  We don't know anything.
*  I mean, it's just so hopeless.
*  Like, it's just so complicated.
*  It's such a mess.
*  This reminds me of this joke that Daniel Wolpert used to start his talks with.
*  When should we think and when should we act?
*  And when it's appropriate to think, what should we think about?
*  That is the crux of what we talk about today,
*  part of what Nathaniel Daw is working on these days.
*  Hello, everyone.
*  This is Paul Middlebrooks from Bend, Oregon today.
*  On a little trip with my family.
*  It's lovely here.
*  I've already gone on a few runs along the Deschutes River Trail.
*  I highly recommend it.
*  All right.
*  Nathaniel Daw is a professor at the Princeton Neuroscience Institute.
*  And man, he has done some stuff.
*  His main focus is building computational models
*  to account for how our brains learn and make decisions.
*  And as you'll hear, he's also interested in tying in these models
*  to neuropsychiatric disorders.
*  So he's done a lot of work using reinforcement learning as a starting point,
*  but that's really underselling the breadth and depth of his work,
*  both past and present.
*  And I encourage you to visit his lab website to enter the rabbit hole,
*  which you will then go down.
*  Today, we talk about things like the difference between model-based
*  and model-free reinforcement learning
*  and how the brain controls which of these to use in different situations.
*  We review the phenomenon of replay in brains and machines.
*  And in brains, this is where sequences of brain activity
*  are replayed in neural circuits at different times
*  and in different ways relative to when an experience actually occurs.
*  We talk about some of his most recent work
*  on how replay in the hippocampus could help us figure out
*  which memories are appropriate to conjure up
*  and prioritize in given circumstances to make appropriate decisions
*  and how this potential role of replay can explain many different flavors
*  of replay that have been observed over the years.
*  As usual, we perambulate many other topics,
*  including his upcoming keynote address
*  at the Cognitive Computational Neuroscience Conference.
*  I'll be speaking to a few more of the keynote speakers for CCN.
*  This is a conference you will want to attend in the years moving forward.
*  It's in Berlin this year, Germany,
*  and I think it'll be somewhere in the USA next year.
*  Find the show notes at braininspired.co.
*  slash podcast slash 37.
*  I'm so grateful to all of my guests, Nathaniel included, of course,
*  who take the time out of their very busy schedules
*  to share their science and stories with little old me.
*  So I hope that you guys are grateful to them as well.
*  And of course, I am grateful to you for listening.
*  So thanks. All right.
*  I'm going to take my kids to an old volcano now.
*  And hopefully for my sake and theirs, it is not too active.
*  Enjoy Nathaniel Daw.
*  Welcome, Nathaniel. Thanks for joining me on the show.
*  I'm happy to be here.
*  So I got stood up last night by your wife.
*  No kidding.
*  Yael Niv.
*  I was actually supposed to interview her just last night.
*  And, you know, as these things happen, it didn't work out
*  because of internet connection and scheduling and things like that.
*  I also did not know that you were married to Yael Niv.
*  And as a complete coincidence that I would have been interviewing you guys back to back.
*  I guess I'm not up on my celebrity neuroscience couples.
*  There are a lot of them, actually.
*  How do you meet people in neuroscience?
*  Well, I mean, I'm going to start off with a really hard hitting question here.
*  How do you make a marriage between two neuroscientists in very overlapping fields?
*  How do you make that work out?
*  I know that you're in the throngs of childcare right now while she travels, for instance.
*  Yeah, but, you know, I think there's a sense in which it works very well
*  that we can help each other out and have all the same constraints
*  and professional challenges and so on.
*  And that so I think, you know, academic marriages work well.
*  There's it's something we have to go to the same conference
*  and that often poses a child care issue.
*  And I think if I probably if I had like ordered a wife out of a catalog,
*  I probably wouldn't end up choosing have chosen one that does exactly the same thing I do.
*  But, you know, life is what it is.
*  Life is what it is.
*  She's she's fantastic.
*  So as you'll no doubt find out if you ever get the chance to actually talk to her.
*  Well, geez, that's I mean, that's what I keep hearing.
*  She's every every time I tell someone, yeah, I'm going to be interviewing Guile pretty soon.
*  Everyone's so excited about it.
*  No one no one was that excited about you, Nathaniel, but I'm going to interview you.
*  Well, I'm the yeah, I'm the substitute, right?
*  Yeah. Yeah.
*  OK. Well, you're going to be giving a keynote address
*  at the Cognitive Computational Neuroscience Conference in a few months.
*  And that conference is all about bringing together neuroscience,
*  cognitive science and artificial intelligence.
*  I'm wondering if you have a take on how these fields, which are overlapping,
*  but but, you know, have their own communities and stuff, how they can best work together.
*  Yeah, I mean, that's something I thought about a lot
*  because I did my PhD in computer science and I, you know,
*  I had a lot of professional advantages and a lot of professional challenges.
*  I think related to that related to what do you mean?
*  Well, to being a I mean, being a computer science, knowing computer science
*  in neuroscience psychology has been just an incredible secret weapon.
*  Yeah. Made a whole career off it. Right.
*  Would you say that you're like had the right knowledge base at the right time?
*  Or is that is this a recurring theme, you think, in like in neuroscience?
*  Because the computer science backgrounds really seems to be flourishing right now.
*  Yeah. I mean, I think there's a there's just so many opportunities there.
*  And partly maybe from my and there have been for a while.
*  And I think there will continue to be.
*  And partly this reflects, of course, my own weird perspective and bias.
*  But I just think, you know, computer science, you know, neuroscience,
*  especially in psychology, just have such a need for for theory, really. Right.
*  For for some kind of high level understanding.
*  And there's just so, you know, computer scientists know so much about
*  how to think about problems, how to formalize them,
*  what are the sort of families of ways you can approach them
*  in so many different areas.
*  And in, you know, neuroscience is basically no offense to all of us,
*  you know, nothing about these things. Right.
*  There's just so much, you know, the parts of neuroscience
*  that have been the most successful, like vision or the parts where that,
*  you know, we don't even we forget that there's all this sort of engineering
*  knowledge, right, or single detection theory and stuff that that underpins
*  the study of it.
*  And the parts that don't have that is just so challenging. Right.
*  And so I just think there's so much opportunity
*  for sort of knowledge transfer from computer science to neuroscience and psychology.
*  Not just I mean, there's also, you know, sort of big data kinds of
*  there's data analysis kind of things as well.
*  But I'm talking more about sort of conceptual kind of theory. Yeah.
*  Level ideas.
*  I've never been as it's not clear to me
*  there's as much opportunity in the other direction.
*  The day I need neuroscience or psychology.
*  I know lots of people are excited about that.
*  I my the opportunities I've seen have mostly gone the other way.
*  So I'm more of a consumer in a sense of computer science than a producer.
*  Do you think that OK, so there's this kind of conflicting trend that
*  we become more and more specialized as time goes on in a science, right?
*  Because the body of knowledge grows so large.
*  And it used to be that there are Renaissance people, I'll say, not Renaissance men,
*  where you sort of learn, you know, if you went back 2000 years,
*  it wouldn't take much to, you know, to like, we know more about so many
*  things than people did 2000 years ago. Mathematics, for instance, right?
*  You know, even just in our lower level mathematical training.
*  Do you envision like a that people becoming more like Renaissance
*  people and learning these broader fields or is it going to continue
*  to get narrower and narrower where we're going to have to cross
*  communicate at conferences like like CCN, for instance?
*  Well, yeah, no, I do. I do.
*  I mean, I think that but I think that's what that is indeed why there are opportunities.
*  Right. Like because people X and people Y work in different.
*  You know, traditions and have different core knowledge.
*  There's always opportunities at the interface.
*  Right. And particularly if you have very well chosen ones like I think CCN does,
*  it can be very profitable to bring together people from different perspectives,
*  even within neuroscience. Right.
*  I mean, you know, I've spent a lot of time talking to people who work on memory,
*  like Daphne Shohammy and Deborah Tommy and so on.
*  And that's been very productive.
*  And it takes it takes like it takes a lot of work. Right.
*  Like it's not like there's like a lot of low hanging fruit
*  where you just get together and write a paper like it takes a lot of thinking
*  to drive these connections.
*  But there are lots of opportunities. Right.
*  Precisely. I think for the reason you say.
*  But so you don't you don't think like a future neuroscientist student, for instance, will
*  will need to incorporate all these bodies of knowledge.
*  I mean, will they be shooting themselves in the foot by being so limited
*  in their scope, for instance? Right.
*  I think you're right that the world that, you know, things get very specialized.
*  I do think, of course, I think everybody should know computer science and math
*  and stuff. Right.
*  But and I try to teach that to our students and propagated in our curriculum and stuff.
*  But there's of course there is a limit to what you can cram in someone's head.
*  And so we do have to work in teams.
*  And I do think that will become increasingly important.
*  Do you know this reminds me of this joke that Daniel Wolpert used to start his talks with
*  where he would plot the number of pages of Candela Schwartz
*  by edition. Right. Or by year.
*  Yeah. Right. And he would show his growing exponentially.
*  Right. And he extrapolated this forward to
*  to when his daughter was going to be in grad school or something.
*  And it was going to be a 50,000 page book.
*  And his ideas that like the sort of punchline of that joke was that
*  the job of experimentalists is to like make that book longer,
*  is to collect more stamps and fill it up with more facts.
*  And the job of theorists is to sort of bend the curve there and shorten it and derive
*  understanding and shorten the book, basically.
*  And the argument is that theorists are losing.
*  But maybe if we succeeded, maybe that's right.
*  Maybe if we really understood things, you really could be someone who understands all this stuff.
*  So this reminds me of like Society for Neuroscience, right, as a point of comparison,
*  that that conference has become so large.
*  And just to compare it to something like the CCN that and there are a bunch of these, right,
*  like COSIGN, for instance, right, that that have become like these smaller specialized
*  conferences where you can still get stuff done.
*  So in the in the textbook analogy, these would be like, I don't know, specialized shorter
*  textbooks. Right. But, you know, is there something special about these smaller type
*  conferences with respect to something like Society for Neuroscience?
*  And is it even worth going to Society for Neuroscience anymore?
*  In the same respect, is it worth reading Kendall and Schwartz, right?
*  The big neuroscience book.
*  I would probably read the Kendall and Schwartz before I went to SFN, honestly.
*  But I love these smaller conferences and I'm not sure I think the right way to think about
*  them is like hyper specialized.
*  I mean, it is, you know, I think.
*  COSIGN kind of grew out of the neuroscience part of NIPS sort of.
*  Splitting off and then blossoming into its own little subfield.
*  Right. And community.
*  And then I think CCN in some ways has split off from that.
*  With things like VSS, like a vision specific conference.
*  So there are lots of these offshoots that are smaller, that are more tenable.
*  And almost coming from a theoretical perspective.
*  Right. So these are like the theorists almost winning their smaller battles in the war or
*  something. Yeah.
*  And I think that CCN and also COSIGN and RLDM, which is one that I'm involved with as
*  well, first of all, decision making and Yale's also involved in this interdisciplinary
*  character they have makes them a little different from the international conference of
*  people who study the cell in the kidney or something.
*  Right. Like it's really it really is about kind of opening up our perspective on
*  neuroeconomics is another.
*  Right. They're explicitly kind of interdisciplinary and intercultural.
*  And I think that's very productive.
*  And there is a sort of size that makes that work.
*  And it's you know, they can't be everything.
*  And I think CCN can be COSIGN and vice versa, but I think they both work.
*  Are you going to be talking about replay at CCN?
*  Do you know, like, possibly what you might be?
*  I know it's a few months away.
*  I haven't completely decided.
*  I might talk about replay.
*  The other thing. So either I'm going to talk about replay or I'm going to talk about sort
*  of population coding and the dopamine system.
*  So that's the other the other sort of new computational project I'm sort of playing
*  with. So when you go to like something like CCN,
*  right, are you looking to take away new experimental information if you're coming from
*  the theory side? Or what's something that generally that you might come away from a
*  conference like that with?
*  So I think for me, again, the thing that that makes CCN special or
*  neuroeconomic special or LDM special is the chance to sort of hear a different
*  field. You know, how is, you know,
*  Yoshua Bengio thinking about things or how is Rissett and thinking about things?
*  I think that's.
*  You know, I spend all day reading papers in my, you know, in the sort of part of
*  science that I work in.
*  And so it's really refreshing to have this sort of different set of talks and
*  interactions and posters and conversations.
*  And I think that's what's really special about it.
*  And so for me, I think it's especially the computer science, but also there are sort of parts of the
*  human computational cognitive
*  science kind of world like memory or
*  or people who study perception or something that aren't sort of my people I see at the
*  really little meetings I go to with my friends all the time.
*  Right.
*  When you come across some field like that, that hasn't been touched by a sort of more
*  theoretical framework, do you do you just think, oh, my God, what's wrong with these
*  with this field or what?
*  I think there's an opportunity, right?
*  Like, you know, I think those aren't mutually exclusive.
*  Right. Yeah, I know. But so I've been to psychiatry
*  for just for instance, for a bunch of reasons and a bunch of us in kind of my
*  subfield have.
*  And there's a level at which the actual psychiatrists will say, you know, they have no
*  theory and it's a complete shambles.
*  They don't know, you know, they have no laboratory tests.
*  Right. The only part of medicine where, you know, the only thing that gives you a
*  diagnosis is, you know, a bunch of self-reported symptoms like they can't send you
*  for blood tests to test whether you really have what they think you have.
*  Right. And so it's a somewhat of a catastrophe.
*  Right. And a lot of opportunity.
*  And yet I'm not the kind of the you know, I also kind of assume that those guys are
*  smart people and girls and women that those people are smart scientists and
*  doctors and they know what they're doing and they have a lot of knowledge.
*  Right. And I think there's often opportunities and sort of trying to distill that
*  and sort of connect that up with more computational ways of thinking.
*  Yeah. My whole PhD postdoctoral work was this sort of my whole model based model
*  three thing was really about listening to these behavioral psychologists who study
*  habits and deliberation, behavior, and they have this very, I mean, they're
*  theorists in a sense, like they have these sort of word theories of how the
*  associative structures that make these things work and so on very clever experiments
*  and just a beautiful set of experiments and knowledge going back to told that and
*  before and sort of come figuring that out.
*  Right. Really taking that on board and reading it and understanding it and then
*  trying to kind of give it more of a computational flavor.
*  Gloss has been sort of, you know, something that working out forever.
*  Right. That's a lots of opportunities.
*  When you do give a talk, how does it feel these days relative to how it felt when
*  you were just starting out?
*  Were you ever nervous? You don't seem like a nervous speaker or, you know,
*  I say I get this.
*  I see I'm drinking water. Actually, I get this dry mouth.
*  Oh, yeah. Definitely have these.
*  I'm actually a very nervous person and I definitely have physical nervous
*  symptoms. But I also I guess it's the habits thing.
*  Right. Like certainly now I give talks and I sort of just zone out and it all sort
*  of comes out of me without me thinking about it too much anymore.
*  So that's different than it used to be when I was a kid.
*  What's one of the, you know, people have talked about their scientific moments,
*  right, where they realize they discover something, they realize something.
*  Do you have one of those moments like when you've been attending a conference
*  that has really shifted your focus or enlightened you or something that you
*  remember being at a conference like that?
*  Huh? I'm not sure I have these kind of aha moments in general.
*  Like not in scientific endeavors either.
*  Not. Yeah, it's like the the difference.
*  Like it takes a while for things to sort of sink in. Right.
*  Like often I have like a, you know,
*  I fight with someone about something and it takes me a few days to realize that
*  like actually there's something to it and like, you know, that changes my thinking.
*  But it's it never happens to me in the moment. Right.
*  And so the same at conferences.
*  Wait, are we talking about marriage or science here?
*  It's like, let's say a student.
*  But it's more of an incubation sort of thing, huh?
*  Yeah, exactly. Or like, yeah, you know, I think ideas have to sort of.
*  Yeah, definitely incubate or sort of work their way.
*  I mean, I feel like a lot of especially what I do.
*  The kind of theory that I most value is sort of trying to really understand things.
*  It's not so much like specific results or even specific ideas.
*  It's sort of how to think about things and how it all fits together and what's
*  the sort of the core issue.
*  I feel like that often takes a lot of time to refine and writing a paper,
*  rewriting a paper and giving talks about it.
*  I'm still sort of refining the way I talk about the stuff I did 15 years ago.
*  And so similarly, conferences, I, you know,
*  there's lots of ideas I got exposed to and those are influential to me.
*  Absolutely. But it's hard for me to sort of crisply say this is the moment that
*  like, you know, that I had this aha moment.
*  Yeah, it doesn't even have to be an aha moment.
*  I remember going when I was looking for postdocs and you don't have to answer,
*  you know, because you might not have a moment, but it just reminds me of I walked
*  up to I was looking for postdocs.
*  So I did some research on people that I might want to talk to.
*  And I walked up to this guy's poster.
*  He was a PI and the PI was there.
*  He was actually presenting his poster and he had never heard of me, you know,
*  and I asked him, you know, do you have like openings for your postdoc
*  for a postdoc position?
*  And he kind of his eyes kind of like widened and he was like, why are you talking to me?
*  This is like the wrong way to do this.
*  I don't know what he was thinking, you know, but.
*  Rich Sutton taught me how to tie my shoes at NIPS once.
*  You know, that's like the fancy, fancy tying.
*  You know, like I was just like tying my shoes.
*  Like I was hanging around with him at NIPS and he noticed to his credit that my shoes
*  came untied like every five minutes.
*  And he finally was like, you know, you're tying your shoes wrong.
*  If I know like, let me show you.
*  And I was like, leave me alone.
*  Like, and it sure enough, you know, I was doing something wrong and he fixed it for me.
*  So, oh, my God.
*  No, no, I want to know what you were doing wrong with your shoes.
*  This kind of thing, like, you know, left over right, right over left.
*  Like, I didn't realize you have to do that when you tie your shoes also.
*  Like, it turns out it matters.
*  Like you might not know either, but the order which taught me that if you do it the wrong
*  you like when you make a slipknot, you know, if you just yeah, turns out it matters.
*  Are you left handed? No.
*  So there you go, folks.
*  The moment, the conference moment from Nathaniel.
*  There it is.
*  So, Nathaniel, I had Tim Barron's on the show and we talked about a little bit about
*  replay because he works a little bit on that, a lot on that actually.
*  And I told him that you're going to be on and he said, oh, good.
*  Why don't you expose that guy for who he really is?
*  And so here's what this is what we're going to try to do.
*  OK, so I see.
*  So let's talk replay and reinforcement learning and some of your recent work here
*  just very broadly, because we've talked about reinforcement learning on the show
*  before, but reinforcement learning in reinforcement learning, the goal is to
*  maximize future expected rewards in an uncertain environment, essentially.
*  And you've done a lot of work on how and when we use what's called model based
*  reinforcement learning versus model free reinforcement learning.
*  Now, I had a friend in graduate school, he's a colleague friend, and he
*  self admittedly had a problem with sweets.
*  Like he couldn't not eat sweets if they were in front of him.
*  He would visit this cupcake shop, which is within walking distance of our lab.
*  And he told me a story one day, like he visited the shop and he was looking at
*  the cupcakes and one of the employees started taking the cupcakes out of the
*  display and he asked, you know, what are you doing with the, why are you taking
*  the cupcakes out?
*  And the way he tells a story, the employee slipped up quote unquote and told him,
*  oh, we have to throw these away at the end of the day because we can only keep
*  them for one day, kind of a fancier cupcake place.
*  And so the light went off in my friend's head and that evening he went and looked
*  through all of the dumpsters behind the cupcake shop, looking for the bag, opening
*  bags, looking for the cupcakes.
*  My question is, is that a problem with his model free reinforcement learning?
*  Or is it a deeper problem?
*  Yeah.
*  So this is a good example actually of why the sort of simple goals and habits
*  dichotomy isn't good enough.
*  So the version of this I often think about or often refer to is drugs.
*  Right.
*  So there's this story.
*  So the background of these stories, right, is that they're supposed to be, you
*  know, historically there's been this sort of two system idea that you have a
*  deliberative system that knows what's good for you and makes good choices and
*  thinks a lot about the value of things.
*  And there's an automatic system that can make mistakes and do things that are
*  sort of contextually inappropriate or for whatever reason, there's some habits
*  that you repeat a lot, but you repeat them again when you shouldn't and so on.
*  And one of the reasons people are excited about this idea, you know, many
*  reasons people are excited about this idea, all of them have to do with the
*  fact that this seems like a way of thinking about why we might be of two
*  minds of things, whether it's racism or moral dilemmas or drug abuse, right.
*  Compulsion.
*  And so the compulsion story is that, you know, drugs affect dopamine and dopamine
*  trains up these habits and so you have people who have these sort of almost
*  automatic behaviors that are wrong and that they know are wrong.
*  And if they were, it's this kind of imbalance between this automatic system
*  that's been maladaptively trained.
*  This falls under the rubric of model free reinforcement learning.
*  Yeah.
*  So that's the, so the habits are the sort of model free.
*  That's the sort of classic story of dopamine, you know, training up sort of
*  automatic stimulus response kind of behaviors, right.
*  But, but, and that seems, you know, that seems very appealing, but it sort of
*  can't really be the story.
*  And I think you're, you're a story about digging around for cupcakes as an
*  example of that, right.
*  It is, that might explain like the habitual movement of, you know, a
*  cigarette to your lips or something over and over again, but it can't really
*  explain the really motivated drug seeking, you know, very novel behaviors
*  that people do to obtain drugs.
*  Got to make this phone call to talk to this guy to get to this place to, yeah.
*  Yeah.
*  Things you've never done before, right.
*  So habits are sort of well-practiced actions and that might be part of drug
*  abuse, but it doesn't explain if it's really the case that I, you know, I know
*  that heroin is terrible for me and I shouldn't use it, why am I engaging in all
*  this planning to obtain it and, you know, how there's got to be some kind of
*  cross talk.
*  So why am I digging around in garbage bags for cupcakes I shouldn't eat
*  anyway?
*  And that's kind of disgusting, right.
*  That that can't be a habit, right.
*  So my favorite example of this actually is the, is the wire, right.
*  So you have these guys, Johnny and bubbles, the, the sort of, this, the
*  comic relief television show.
*  Yeah.
*  Why?
*  So the wire is the best television show ever made.
*  I tried to watch.
*  Okay.
*  Yeah.
*  It's hard to, yeah, it's hard to understand, but if you can, sort of
*  get past the, the, the dialect and understand what's going on, but they,
*  there are these junkies that are on it, you know, as sort of the comic relief is
*  not quite this sort of the, there's a sort of pathos to them, sort of clowns.
*  And it's like every week they have to engage in like some new, weird crime to
*  obtain drugs, like they rob an ambulance or they like fish with a fishing pole
*  off a building to grab drugs from, and, and it's always this fiction, but I think
*  it rings true and it's something that the, that a habit story can't possibly
*  explain, right?
*  There's sort of a pure model free, you know, I've very well practiced this
*  particular sequence of actions.
*  And so my body now does it automatically or it's locked in by dopamine, having
*  trained up maladaptive actions that can't be right.
*  So what's okay.
*  So then that's a more deliberative style of choosing actions and behavior.
*  How do these like model based and model free reinforcement learning constructs,
*  how do they map onto our brains?
*  I know you don't care about brains, but
*  no, you computational, you computer scientists, you're all the same, but, but
*  yeah, but what, what's like the very broad stroke picture of how, what, what
*  we've understood in the past of how they map onto different areas of the brain.
*  Yeah.
*  So the story of habits, right.
*  And there's this classic story going back to the nineties and Wolfram Schultz's
*  dopamine recordings, Peter, Dan Reed, Montague theory about this, you know,
*  this neuro modulated dopamine, which is released in these ascending projections
*  from the mid brain and sort of wash kind of most of the interesting parts of the
*  rest of the brain in this neuromodulated dopamine, which is involved in movement
*  and reward and so on drugs of abuse.
*  And it's supposed to carry this prediction error signal, which is exactly
*  the prediction error signal you would need different students expected in
*  observed rewards and so on for training up sort of, you know, I took this action
*  and it worked, so I'll take it next time.
*  So learning these habits, right.
*  So experiential learning, procedural learning of habits, this is called model
*  free reinforcement learning in the reinforcement learning in AI.
*  Another approach to this problem known as model based reinforcement learning is
*  more about mental simulation, right?
*  So I learn in the spatial case, a map of the world.
*  I learn where the, you know, the restaurants are and you put me down
*  somewhere and I can sort of.
*  Spin out paths in my head to try to figure out how to get to the restaurant or try to
*  figure out what the best path I could take is or something.
*  And importantly, this kind of learning can figure out new things that I've never
*  done before, like, you know, robbing an ambulance to get drugs or something.
*  Right.
*  It did the characteristic or digging through garbage bags for cupcakes.
*  It's able to extrapolate from knowledge about how the world works and sort of
*  mental simulations to derive sort of new decisions in a goal directed, creative,
*  flexible decisions, right.
*  And there's various evidence that even rats can do this as well.
*  And people can.
*  Less is known about how it works in the brain.
*  Probably the most selective thing, suggestive thing is this evidence
*  about hippocampus, right?
*  So there's a bunch of reasons to think that hippocampus is broadly involved in
*  this kind of computation or decision making or inference, whatever you want to call it.
*  And one of them is that in the case of spatial tasks, as you know,
*  hippocampus is famous for having these place cells that show you that if you
*  listen to them seem to represent where the animal thinks he is, right?
*  So you have a rat and these are tuned for locations.
*  When the animal runs to their location, they blitz cells, they blitz spikes.
*  And less famously, but more excitingly, they also sometimes respond to locations
*  where the animal isn't, for instance, when their animal is sort of standing
*  still at a choice point, it seems like they spin out for change.
*  Look, they spin out trajectories in front of the animal or behind the animal
*  after a reward and so on.
*  And so there had been an idea that you're actually seeing this kind of mental
*  simulation here, that this is the animal thinking about routes he could take and
*  evaluating whether they're good ones or trying to figure out where you can get or
*  how to get somewhere, right?
*  So that might be, and that's an idea we've been pursuing lately, how the brain,
*  or one of the ways the brain achieves this kind of flexible kind of goal
*  directed planning by mental simulation, model based reinforcement learning.
*  So we call it.
*  If you value the show, your contribution will definitely help improve it moving forward.
*  A lot of your previous work has been figuring out from the theoretical basis,
*  how the brain decides when to use model based versus how the brain decides when
*  to use model free.
*  And, and this work that you're talking about that we're going to talk about in
*  just a minute here with replay, I mean, you have become unsatisfied with an
*  account of these two processes occurring completely separately.
*  And instead, you know, you think it makes a lot more sense to use both processes
*  sort of together and to go back and forth.
*  So the story of each of them being used separately no longer seems to satisfy you.
*  Right.
*  Which has sort of led into this work with replay, which brings us to what I know of
*  what you're doing modern day.
*  I know you're beyond that now because, because of the way science works, but you
*  just talked a little bit about what replay is and what we know about it in, in
*  animals from a theoretical perspective.
*  So that's for like the neuroscience side.
*  So, so replay in artificial intelligence has sort of famously been used.
*  Well, I don't know how famous it is in a deep Q networks.
*  So the deep Q networks that learned the Atari games to play the Atari games so
*  well.
*  And in that case, the word replay meant simply like refeeding previous training
*  examples into the deep network.
*  And those training examples were drawn randomly, you know, from the previous examples
*  and you just refeed them in.
*  And that's, that was done to help remove these correlations that could occur
*  naturally, like in the sequences and the structure of the games that were being
*  played because those correlations in the sequences might actually slow the learning
*  of the network.
*  So you'd want to like feed these unstructured uncorrelated training examples in.
*  And more recently, there's been some work on figuring out how to prioritize which
*  previous training examples are the right ones to feed in, right?
*  So that you can speed up learning.
*  And it was shown that this speeds up learning in the, in the deep network.
*  It's frustrating to me actually, as a side note, that we continue in AI and in
*  neuroscience to use the same terms for different things, because this is replay
*  is that's different than what replay is from what we understand in the human
*  brain.
*  But anyway, you've recently developed a theoretical framework to account for how
*  brains might figure out which memories should be used in a given situation when
*  figuring out how to make a decision to maximize future rewards.
*  So it's a form of meta decision making essentially.
*  And this was published way back in 2018 in nature neuroscience called, called
*  the prioritized memory access explains planning and hippocampal replay.
*  And it integrates and accounts for a host of seemingly disparate facts about
*  replay.
*  Some of which you were just describing a few minutes ago.
*  Maybe you can just start by talking about how it brings together what's known,
*  what we know about replay, some of those facts.
*  Sure.
*  So there are an awful lot of, there've been an awful lot of experiments that,
*  you know, have revealed that in different circumstances, these hippocampal
*  neurons engage in this thing called replay, right?
*  That they represent locations and trajectories often, or at least pairs of
*  cells or something other than where the animal is.
*  So sometimes when he's asleep or quietly resting, other times during behavior,
*  there are these sharp wave events that where the series of hippocampal neurons
*  light up very rapidly and they often form a coherent trajectory, often starting
*  where the animal is and heading somewhere else in front of or behind him.
*  Is this the same as like sharp wave ripples?
*  This is sharp ripples of what's happening in the EEG during that.
*  And if you look at the neurons, as I understand it, there is this sort of
*  coherent population activity where a series of play cells light up.
*  So sharp wave ripples, sorry, just to interrupt, sharp wave ripples is
*  maybe the clearest oscillation, strongest oscillation that happens, that's
*  known in the brain and it happens in hippocampus.
*  A lot of people are familiar with gamma oscillations and different theta,
*  beta waves, et cetera, that are measured in EEG.
*  But sharp wave ripples, which correspond to what Nathaniel was talking about,
*  the sequences of neurons that light up apparently are just another oscillation
*  that occurs, but it's a very...
*  It's sort of a brief packet, right?
*  It's a brief packet, yeah.
*  Theta, right?
*  So theta is another rhythm, EEG rhythm that you see in hippocampus
*  when animals are running.
*  So sharp wave ripples happen when the animal is standing still.
*  When animals are running, you see this eight hertz oscillation in the EEG.
*  That's also associated with, this is sort of confusing and I actually get in
*  trouble with this and talks for confusing these things or deliberately mixing them
*  up, but it's also the case that during theta, there's this phenomenon known as
*  phase precession where the location represented by the neuron seems to sort
*  of oscillate back and forth a bit in front of the animal, but closer than
*  sharp wave ripples, I think, go farther.
*  So there's a second EEG event and a second type of non-local activity, but we're
*  mostly talking about the sharp wave ripples.
*  Sorry to interrupt.
*  Tim mentioned that last time, and I just let it slide, so I just wanted to
*  interject.
*  Yeah, yeah.
*  So sorry.
*  So then the question is, what do these things do?
*  And there are these exciting results from, say, Pfeiffer and Foster that say
*  that they run ahead of the animal.
*  And the animal's foraging for food and there's a goal and you see them sort of
*  tracing out the location of the goal and the animal runs there.
*  Right.
*  And so that really sounds like this sort of planning thing that we're excited
*  about.
*  And yet the first time I said this, I think it was to Lauren Frank, who's another
*  hippocampal physiologist.
*  He said that that's hogwash because the neurons respond, they fire behind the
*  animal, but they fire in front of the animal, maybe even more.
*  So it's clearly not really about forward planning.
*  Right.
*  So, and in fact, Foster himself became famous for discovering backwards replay
*  before he was working on forward replay, which is when the animal gets to the end
*  of the maze, he eats the food and then the play cells light up from where he came
*  from or where he could have come from.
*  Right.
*  So the whole sequence rewinds backwards behind the animal.
*  And you really know it's backwards because the place cells are directed.
*  So it's like the animal is running backwards in his place cells.
*  They actually know it's not playing out, running forward the other way.
*  It's playing out, running backwards behind him, rewinding.
*  So there's a, there's just a bunch of these different phenomena and they happen
*  at, they're all non-local trajectories.
*  There's other ones that happen in sleep.
*  And I think there intended to be a sense that partly because they're sort of
*  triggered at different times, they have different functions as far as like, I
*  mean, this is not my world, but if you read the literature on this, I think
*  people argue that, you know, maybe forward replay really is about planning
*  and backward replay is about credit assignment or learning or something.
*  And replay when you're asleep is about consolidation.
*  And maybe that actually is more related to the, the, the thing you mentioned
*  about, you know, making gradients sort of batching up gradients in, in, in deep
*  networks and system consolidation or something, it's certainly possible.
*  But the hope that we had was maybe we could view all of these as sort of
*  special cases of the same operation.
*  And that operation is the operation.
*  If I think about how do I get from here to there?
*  Another way of saying that is that in the world, sort of the, maybe the primary
*  problem of reinforcement learning or of decision-making is that my actions are
*  separated from their consequences.
*  It's based in time and that makes it hard to figure out what to do, but it also
*  makes it hard to sort of learn about how my actions are related to their
*  consequences, just, you know, in the brain, like how do I connect, you know,
*  running here in the maze to get to the end where there's the food, right?
*  Those two things happen separately.
*  And so the, I think the core idea, you know, one way to think about what replay
*  is doing is it's bringing those two things together, right?
*  Is it a lighting up sequences of in the, in this spatial case locations that you
*  could occupy sequentially so that you can sort of connect the thing at one end to
*  the thing at the other end.
*  And if you think of it that way, it doesn't necessarily have to be thinking
*  ahead about what I could do.
*  Like I can think about, Hey, I want to get a hamburger, you know, where can I go
*  find a hamburger, but I could also find a hamburger and be like, Hey, here's a
*  hamburger.
*  How could I have gotten here tomorrow?
*  Can I come here from my office, right?
*  And get another hamburger and think backwards, right?
*  And actually sort of serves the same purpose.
*  It's just happening in the other direction.
*  And when I'm asleep, I could dream about all the different ways of getting
*  hamburgers.
*  It's, it's, it's almost dinner time here.
*  You see, it's breakfast time here, but it still sounds good.
*  Yeah.
*  And so that's, that's sort of, you know, that's the sort of unifying explanation
*  that we, that we sort of offered.
*  And then that's the functional idea.
*  The functional idea is that it's, it's connecting actions to their valuable
*  consequences over these spatial trajectories, right?
*  And in reinforcement learning, that's called backups, right?
*  It's you have to compute the formal operation and reinforcement without
*  computing the long-term value of an action.
*  That this, this so-called state action value function and the Q function.
*  It's something about I'm going to take some action.
*  I want to know what's its long-term sum of expected cumulative future
*  discounted rewards, right?
*  And if I knew that, then it reduces the problem of choosing what to do to just
*  comparing a bunch of numbers for different actions that represent the
*  long run value and you compute those by these backups, right?
*  Like it's called a Bellman backup is what the version.
*  Yeah.
*  The Bellman's equation.
*  Yeah.
*  Yeah.
*  Um, so it's like adding up rewards over trajectory or a tree of future possible
*  trajectories or something.
*  Okay.
*  So that's the, that's the operation we suggest that we play could be doing in all
*  of these cases, right?
*  And then sort of what remains is trying to develop a theory of why is it that
*  you see this pattern, this circumstance and that pattern, that circumstance, and
*  a sort of a bunch of seemingly paradoxical results, or at least disparate
*  results about, about different circumstances, producing different
*  patterns of replay and the story there is a, is this prioritization story, right?
*  So we say, let's assume that this is what replay is for.
*  Let's try to develop at least a sort of toy model that gives us intuitions and
*  sort of formal sort of quantitative theorems about which location should I be
*  thinking about when, and that turns out to have reasonably interpretable components.
*  So part of it relates to you want to think about places you're going to be.
*  It's, it's, it's not worth my doing a bunch of work, computing stuff about
*  situations I'm never going to face, right?
*  So there's no point in my planning my Nobel Prize speech or something, right?
*  Well, so just to back up, so you brought all this under the, under essentially one
*  equation, which is the expected value of backup.
*  And I think what you're about to start talking about is the needs versus gains.
*  That's right.
*  Yeah.
*  Yeah.
*  So just to give the equation, like the equation is essentially this expected
*  value of backup equals needs, is it dot product or times?
*  It's times, yeah.
*  Times gains.
*  Yeah.
*  So, and so you're, you're just going into talking about the needs part of that
*  equation, I think, so go ahead and talk about needs and gains for us then.
*  Yeah.
*  So that, so that, yeah.
*  So just to, to why is it called the expected value of backup?
*  So we wanted to produce a rational model of these backup operations.
*  Like what place in the world should I be thinking about if I'm a rat at any
*  particular time, let's treat that.
*  Like all other decision theory, reinforcement type problems as itself,
*  unexpected value problem, maximization problem.
*  I, you know, I want to choose the one that's earned me the most rewards.
*  How will it earn me the most rewards?
*  If I think about some place and that helps me make better choices in the
*  future, that'll earn me more rewards.
*  Like literally let me vacuum up more food.
*  That's a value of computation, right?
*  Like a literal value of computation.
*  We want to measure that or approximate that at least that's an expected value.
*  It has a form like many expected values, like a probability times a magnitude.
*  So we call it probability need, right?
*  That's how likely am I going to be in this location?
*  Basically, if I'm not going to be there, all the thinking I do about what to do
*  there isn't going to help me.
*  And if I conversely, if I am going to be somewhere, then it's worth my thinking
*  about what to do there that's multiplied for each location by the second term we
*  call game, which is like, how much would I earn by figuring out what to do at
*  this location by doing some computation here, right?
*  And how much more food will this help me vacuum up?
*  So it's a balance between these two things, which together quantify for
*  different places in the world.
*  What's the value of thinking about them?
*  And in particular, thinking about the actions I can choose there, the value of
*  the actions I can choose there so as to make better choices and earn more food.
*  And, you know, one aspect of this is because it's the balance between these two
*  factors, because need is about imminence.
*  It basically wants to drive thinking in front of you.
*  It's like, you know, I'm about to turn left or right.
*  I really should think about what's left of me and what's right of me.
*  That's that's where the need is.
*  That's where I'm likely to be soon in the future.
*  Gain is about where do I know stuff that would be helpful for me to to learn about?
*  So so gain is about where are there rewards in the world that I haven't sort of
*  sufficiently connected to everything else?
*  I find this hamburger.
*  I should think about all the different ways I can exploit this.
*  Right.
*  And so that actually drives replay behind me, not necessarily where I came from, but
*  to places I could have come from.
*  And so it's the sort of interplay between those two things and the extent to which
*  they play out in a magnitude in different locations, in different circumstances that
*  we try to connect to all these patterns of replay in the literature.
*  So how does this relate to the model based versus model free concepts?
*  Is that too broad of a question?
*  No, it's it's it's sort of the key question in some ways.
*  So it is a sort of one level down from the sort of model based versus model free.
*  So you mentioned that I was sort of we were sort of dissatisfied.
*  I just said, by the way, this work is with Marcelo Matar, who's the sort of lead
*  author on all this that we're talking about.
*  So the conception in which we picked up, but certainly predates us of model based
*  versus model free and goals versus habits and deliberation versus automaticity and so
*  on, is this sort of two system trade off?
*  It's like I can either think or act.
*  And the question is, when should I think and when should I act?
*  Yeah.
*  And I think considerations much like the expected value of backup help you think
*  about when does the brain decide it's worth its time to deliberate and when does it think
*  it should just it knows what's best and should just go ahead and act faster.
*  So there's a time cost deliberation and the trades off against the chance of figuring
*  out something better.
*  So this is sort of very similar idea, but applied to the sort of discrete trade off.
*  So I think that basic logic makes a lot of sense.
*  I really do think I continue to think that's a deep insight that the brain has to manage
*  its computations, it's got to selectively allocate, spend its time and its resources
*  split between acting and computing.
*  And when it computes, it's got to figure out what to compute about.
*  And so I think of this story about replay as being kind of a more fine grained theory,
*  not just whether to think or not, but what to think about.
*  And the special case of that is not to think at all.
*  And to act, that's sort of a habits case.
*  But I think a lot of the action which we had sort of missed before, it's not really,
*  except in the sort of very small toy problems that we actually use in the laboratory,
*  you can't think about everything.
*  In the real world, the brain has to be choosy about which computation is going to do.
*  So I think as much of the action is in the case of spatial tasks,
*  which paths do I think about and which paths do I neglect?
*  As much as do I think at all?
*  This is meant to be a theory of that.
*  So in terms of brain energy, just spending metabolic energy in our brains,
*  it seems like the more meta we get, so it seems like we have, it's worthwhile to spend a lot more
*  time figuring out what we need to think about than actually thinking about it and acting on it.
*  Do you think that it's more that we spend more brain energy thinking about or deliberating about
*  what we need to think about, figuring out the environment and what's actually useful,
*  what's not useful versus actually working on the problem, getting to the food or something like
*  that? Does that make sense?
*  Well, I don't know. So first of all, I actually don't, I've never really
*  gotten a clear understanding about the sort of metabolic cost of all this.
*  Let's say computational resources then.
*  Yeah. Well, but so that's a lot. So this is a question like, what is the cost for? The
*  cost might just be time, right? If I really have to stand still and think, right? Or maybe a
*  slightly more refined version that is I have a certain number of working memory slots or something,
*  or I can only think about one trajectory at a time or something.
*  How about quantifying the information it takes to figure out what to think about versus the
*  information it takes to solve the problem?
*  I see. Maybe I think I misunderstood. So one question is just how do we,
*  when do we act and when do we think, right? But there's maybe an additional question,
*  which is the sort of turtles on turtles question. How do I figure out where to think about? And it's
*  absolutely true if this is what you're getting at, unless I misunderstood you,
*  that the theories we've described of how to direct your thinking are totally unrealistic,
*  that DeepMind is not running to implement these and speed up their computation, right?
*  Because the way we do it is we literally move to every location in the maze and we compute,
*  like, what would be the expected value backup here? Right? So that would spend a huge amount
*  of energy, as it were, thinking about what to do before even thinking about what to think about,
*  let alone thinking about it and then acting. And so this is not meant as a realistic process or
*  mechanism level theory of this sort of meta control problem of directing the replay.
*  It's meant to sort of settle in on the principles that should govern this. And then we separately
*  have to think of it as a realistic way that the brain can do this. But it's certainly,
*  you're absolutely right, there's sort of a diminishing return. If you think too hard
*  in the service of figuring out what to think about, you're wasting your time, right? Is that
*  was that where you were getting a little bit? Let me let me try to rephrase this. I'm not asking
*  well either, but you're definitely on the right track. And I'm kind of circling in here. But
*  so we don't experience all of the unconscious processing that's going on, right? So when I'm
*  going to go to the hamburger place, right? I'm not thinking like that there are all these different
*  possibilities. All I'm my experience of it is I just go to the hamburger place, right? But then
*  there are the all what what your theory is suggesting is that there are all these processes
*  taking place unconsciously that seem to be the majority of our cognition, I guess is another way
*  of putting it right. And then it suggests a minority of our cognition is actually implementing
*  some action or behavior. It's like 99% of what we do, of course, is under the hood. And we're
*  not aware of right. It just seems like a lot of resources being spent on these meta processes
*  that eventually get funneled into a behavior. We can move on if I'm not making sense either.
*  No, but I'm not. Yeah, I'm trying to think if I if I agree with you. Well, it's certainly true that
*  lots of stuff is going on that we're not conscious of. I certainly agree with that.
*  To my mind, the one of the insights of all this work or one of the key questions of all this work
*  is that the brain has to make smart choices about spending its computational resources,
*  whatever exactly those are, right? That has to be you just can't get by. And I think these examples
*  of these, you know, deep mind things doing random replay, you know, banks of power plants and,
*  you know, wherever it is that Google is, or, you know, churning out electricity to make this happen.
*  I think it's the Dallas in Oregon, maybe. I don't know.
*  Yeah, I mean, that you have the brain has to be selective, right? It doesn't have the
*  it doesn't have the electricity to, you know, to think about everything, right? And then in real
*  time. And so I what we sort of argued is that this problem, how do you manage your computations? How
*  do you decide what to think about and what not to think about, and when to think about it and when
*  to act? How does the brain do that? offers a really nice insights into all these sort of
*  weird phenomena like habits, compulsion, and you know, people say racism and stuff is a different
*  way of thinking about these really deep problems. And so I think there's something to that. But I
*  think that the thing that you're identifying is also that there has to be and we don't have
*  really clear mechanistic story of how the brain actually does this right in a way that you may
*  we make it sound like I think it is super important, right? But I think the brain must
*  have efficient ways to do it that only approximate the principles that we've tried to but sort of
*  very laborious kind of ideal observer analysis tried to lay out right, but that can't be how
*  it works. And your kind of intuition that my brain we spend all this time thinking about what to think
*  about can't be right. Right. I mean, this is a valid criticism, but can't there must be some way
*  of squaring the circle. Well, it's not even a criticism. I'm just it's just amazing that our
*  experience of ourselves that our intuition is so wrong. I think that I'm thinking about the problem,
*  but mostly I'm thinking about how to think about the problem without even knowing I'm thinking
*  about how to think about the problem, right? But maybe you have really smart, you know, reflexes
*  that direct your thinking. There actually there is a whole there's a sort of sub discussion within
*  my little tiny subdupes discipline, people think about this problem. There's a set of people think
*  this is all itself learned, right? So I'm going to learn by trial and error, how to learn by trial
*  and error or something. Yes. And I think that's crazy, right? I think there's no way you know,
*  it's hard enough to learn, let alone the trial and error learning of how to do that is going to
*  happen in order to magnitude slower, right? It's just, where's what I've got to figure out what to
*  do on day one when you put me in a new puzzle. So I think there's got to be really smart,
*  sort of pre tuned reflexes for this, if you call them that, like some point, there has to be that
*  constraint. Yeah, no, I think that's right. So we've been we've been talking about this,
*  and the examples you've been giving are spatial and sort of harking back to rodents and amazed
*  task often, you know, trying to find food and stuff. But I talked to Tim Barron, you know,
*  a few episodes ago, and, and he's done a lot of work on using these same principles in an abstract
*  knowledge cognitive map sense, right, that we can not only spatially navigate mazes, but
*  conceptually navigate con seps abstract concepts. I'm wondering if, if this expected value of backup
*  concept can map on to the conceptual space, as well as the spatial domain.
*  Um, I think the short answer is yes. So of course, there's a long answer. But the but but yes,
*  the nice thing about this kind of reinforcement learning decision theoretic formalisms is they
*  just work in state spaces, right? And figuring out what the state space is, is of course,
*  a whole separate issue. And one you'll probably talk to you all about. Yeah. But the theory is
*  really just talk about states and actions. It can be an Atari game, it can be a maze. It can be,
*  you know, all kinds of things. And it's a very general theory. And I think, too, I think there
*  is lots of evidence, you know, the hippocampus and related areas like entorhann cortex are involved,
*  like Jim says, in more than just space. And it probably is, you know, relations between states
*  or events or stuff in the world and understanding that that relational structure, much like a map of
*  space, you can have a sort of map of the rules of a game or something, right? One of the reasons
*  we're so excited about thinking about in terms of space is just that is a case, maybe the only case
*  where we have really clear technology and knowledge about how the brain represents it, that you can
*  actually look inside the animal's brain and see what routes he's thinking about, right. And so if
*  we're right, that this is the whole game is why do they think about which routes win and what makes
*  that happen? Like it just spatial tasks are really the most exciting place to look for that. But
*  presumably the same thing is true playing chess. We just don't have, you know, chess location cells
*  that we can look at necessarily. There's another this other things. Space is a little bit special
*  structurally. So it's, you know, for instance, it's reversible. You know, I can go forward or
*  backwards. It's deterministic. Like if I go north from here, I always end up in the same place.
*  And so there are aspects of the problem that are different, a little bit different, I think,
*  in different in other domains where those things aren't true. And those might involve other neural
*  substrates. And those might involve somewhat different computational. So we are computational
*  story was specialized for this particular case of a deterministic world, for instance,
*  just to make it simpler. I think we could write it down for probabilistic world that's more
*  complicated. Getting back to this idea of sort of meta decisions, which is just kind of in the realm
*  of what you do here. So it's like decisions like figuring out under what circumstances to act in a
*  certain way. How many meta levels are there? Do you think of computation?
*  Got to choose a number, man. You got to choose enough.
*  One. There's actually this there's this paper is an imaging, there's a set of imaging papers
*  that sort of met I think is it from David Bader or something, where, you know, you can actually make
*  animals or people do as people I guess do more and more deeply nested decision problems or something.
*  And you see that it like the activation moves forward like half an inch each time or something.
*  So to measure that went out of your print. That's the guy that I walked up to his poster
*  about the postdoc question, by the way. Yeah, that's hilarious. He's very nice.
*  Yeah, no, he's fantastic. But I always thought that, you know, I wanted to like literally test
*  that, you know, extrapolate the depth problems I could solve, and then try it on orangutan or
*  something that has less frontopolar cortex or something. But sorry, the serious question,
*  I don't think it's like literally a hierarchy, right? I think there's a useful distinction
*  between physical decisions about where to move your muscles and, you know, how to bloke a mode
*  in the world and stuff. And we, for a long time, realize that it's good to think about that in
*  terms of sort of decision theory and reinforcement learning and sort of rational sort of choice
*  models, you know, trying on economists also. I think the insight is just that there are all
*  these internal decisions the brain has to make about how to manage its resources and control
*  itself. And that we can think about those the same way, like with the same at least theoretical
*  machinery. I don't know that they live in like a set of a meta a meta meta a, right. But I think
*  the real thing that people have realized is the sum of the same theory and maybe also some of the
*  same like physical kind of machinery, mechanisms in the brain might serve both of those purposes,
*  right? So you don't think that it's like a trend of evolution to just starting from like the,
*  you know, the highest level or whatever. Some people think consciousness is a model of our
*  cognition, right? And, you know, so and what you're doing is kind of like a model of our
*  decision making. So then it might make sense to have a model of that model. And eventually,
*  it becomes unknown to us what advantages we would gain by modeling a model of a model of a model.
*  But it also seems to be a trend in evolution that a model of itself seems to be useful. I mean,
*  you can see this in DNA as well, obviously, right? Right. I mean, do you think that that's a
*  trend in in increasing complexity or solving problems? Yeah, I'm trying to think I mean,
*  another way of spinning that would not maybe changing it, but you know, evolution is really
*  good at copying stuff, right? Right. And reusing stuff. Yeah, or I mean, it's easy to
*  grow a third arm or something, right? Like, relatively speaking, I think, but or maybe a
*  third and a fourth, I don't know. But so I think there is this sort of principle of reuse where
*  you might have evolved something that's for controlling your limbs. And then it's relatively
*  easy to repurpose that to use it on controlling itself, you know, controlling the controller or
*  something or controlling some other, you know, set of decisions that are being made internally.
*  And so I do think that probably is partly because of how evolution works. But maybe also, as you say,
*  partly because that's useful for solving problems. Maybe that is a principle.
*  Wes, yeah, mind if I ask you a question? Yes. Hard question? No.
*  Do you think the podcast is boring? Yeah. Why do you think it's boring? Because like, you're only
*  like talking. What do you think would make it more entertaining, better? Songs and like,
*  yeah, songs. Like piano songs and stuff? Yeah. Thanks, guys. You're welcome.
*  So we were talking about, you know, the cost sort of computationally or information wise of these
*  sorts of things. And how energy inefficient something like, you know, AI systems are that
*  Google uses or something. Okay, and humans have this sort of lower level rote reinforcement
*  learning, model free reinforcement learning system, right? But if you're an AI, and your job is to,
*  you know, do some problems, would you ever want to even use a model free reinforcement learning
*  system? Or wouldn't you just want to spend the extra amount of energy on a model based
*  system to make sure you got it right? Well, but it's not just so. So I think that's a great
*  question. I think that's what it goes to the heart of the problem. But I think it's the same,
*  you know, if I'm a lunar lander or something, this thing that drives around the moon or self
*  driving car, the trade off is the same, right? You don't have infinite time. And I think the
*  core point is that if I'm a self driving car, I can stand still and burn out my battery,
*  deciding whether to turn left or right. And that's going to have diminishing returns.
*  I mean, to some extent, I should do that. You know, if I have to decide not to run somebody
*  over or something, but to some extent, I should go ahead and act right. And it's,
*  I think that really is I think that there are people who work on, you know, these kind of
*  vehicles, and are interested in these questions of how do I, how do I trade off thinking and acting
*  and why, you know, how do I efficiently allocate what computational resources I have, but presumably,
*  an electronic system, or even if we have come up with a better neuromorphic computing that uses
*  much less energy, relative to our own energy use, an AI would essentially have infinite
*  capacity, or at least so much more than we do. So the trade off might not be as necessary as my
*  question. It's actually a question. Think about a chess computer, right? Like, I think that's a
*  good example. And chess computers, you know, even in I think 2019 with AlphaGo 18, or whatever it is,
*  the whole game, you know, there are more chess positions than there are atoms in the universe,
*  and so the whole game is about, you know, which, which paths do I follow? Which which ones are
*  important? And that's, that's the same problem, right? It's about efficiently allocating
*  computation that goes back to the beginning of AI, and it continues to this day, and that a lot of
*  the action in AlphaGo is that problem coming up in different ways, right? It's what should I,
*  which paths do I think about? And when I think about them, which paths are likely to happen
*  afterwards? And it's all it's, it's, it's, that's a huge problem. So of course, the,
*  the quantitative trade off can differ, but I do think it's, it's sort of core to the problem in AI
*  as well. I also, I sort of wonder if this is a case, this particular example is something,
*  we were talking at the very beginning about whether psychology and neuroscience have anything to
*  offer AI. I sort of wonder if this is something, it's a problem I've worked on, but so I may be
*  biased if this is something where neuroscience and psychology might have something to offer
*  in the sense that I think this these ideas are sort of, my sense is that computer science does
*  a lot of work on analyzing the behavior of algorithms and when is this sorting algorithm
*  better than sorting algorithm and you know, for what size data sets and stuff. But that's
*  often extrinsic and there's relatively less work about inside the system, how can I trade these
*  things off? Not completely true, you know, microprocessors are constantly doing all kinds
*  of stuff to figure out how to occupy their cash and stuff. But it's, I think, relatively speaking,
*  this is, this is something that could be useful and hasn't been thought about for some applications
*  a whole lot. Do you think that's one of the most lacking things in AI? Do you have something that
*  you think is glaringly obvious that AI should be using more of in neuroscience or psychology? I
*  know it goes the other way pretty easily. So like I said, I'm not sure that I have great ideas
*  how to tell professionals in another field what they should be doing. Yeah, I mean, if I had to
*  place a bet on AI, just I would probably place the bet that the deep network pendulum is going to
*  swing again back towards systems people understand and you know, that it's time to start thinking
*  about the people who know how to sort of prove theorems again, their time will be coming rapidly.
*  It seems to be rapid. Yeah, it seems to. There's a lot of pushback on deep nets these days, it seems.
*  I mean, they're incredibly useful. Obviously, they've done, they've done, made huge, amazing
*  progress as a consumer facing technology, very rapidly solving all kinds of problems, you know,
*  that hadn't been solved before. But I'm just, you know, my guess is that the low hanging fruit will
*  be there and the people who the other approaches will start catching up and
*  showing their worth again. We'll see. We're starting to getting some of these more general
*  questions. But before we completely move off, I just what's the current state of are you still
*  working on on this tract of the expected value of backup and moving forward? What's the current
*  state right now? Yeah, well, so the awkwardness about the awkwardness about that, of course,
*  is that I don't have a rat lab, right? And rat experiments are, you know, much slower
*  than human experiments. And so we're trying to sort of develop the collaborations and
*  influence people to figure out what's the best way to really test these ideas. And I think this
*  paper has been well received. And I think that people are interested in we worked hard to try to
*  whittle it down to something that people could really understand and try to test. And that was
*  a tough I'm not sure we succeeded, but we worked hard on that anyway. And so I think there's work
*  to be done that we're trying to sort of plan really on rodent spatial experiments that have
*  more of a learning. I mean, historically, you know, on the one hand, this paper managed to
*  explain a lot of stuff that was in literature. But those experiments weren't really the right
*  experiments for testing this theory, right? They're not really kind of learning decision
*  making kind of experiments. They're just sort of incidentally, you know, animals randomly foraging
*  or something. Right. And so we we really want to sort of put the two strands together, have animals
*  do interesting learning problems and try to make predictions. So that's going on without slow.
*  There's sort of very limited things we can do with human neuroimaging on this as well.
*  And we're working on that. So we can see place cells in the hippocampus, but we can see faces
*  and houses. And if we sort of paint locations with faces and houses, we might be able to sort
*  of broadly see people thinking about different parts of the world and different times. We had
*  some success with that, but it's not it's not the same kind of fine grained measurements.
*  But the general gist is that it's time in the cycle of theory and experiment and modeling,
*  it's time for the experiments to more closely address the model. Is that am I reading you right?
*  I think so. I mean, there's always more theory to be done as well. And, you know, we've talked about
*  some of the some of the ways in which the theory is such as having a more realistic
*  model of the medic control and how that would actually work in the brain and stuff. There's
*  certainly things to be done. I also think that there are applications mentioned psychiatry and
*  drug abuse and stuff a few times. There's been a lot of success, even even given the limitations
*  we talked about an hour ago, thinking about drug abuse and other compulsive disorders in terms of
*  this kind of goal habit straight off that way of thinking not only has been sort of conceptually
*  useful, I think for people, it really is empirically the case that it seems like
*  there is a dimension of compulsive disorders that really does seem to be
*  trans diagnostically, you know, obsessive compulsive disorder and drug abuse and
*  compulsive gambling and eating disorders. There's something about those disorders that is really
*  related to imbalance in these kinds of processes of model based versus model free or meta decision
*  making. But I think that this this way of thinking things less about whether to think or not to think
*  and more about what to think about is really going to give us a kind of finer window,
*  not just on the problem of why am I digging around for cupcakes and garbage bags, but,
*  you know, hallucinations and rumination and other things that are really about kind of
*  mismanagement of your potentially about craving more positive phenomena, right, as opposed to just
*  sort of neglect phenomena where I did something stupid because I didn't think about it, right.
*  I think there are interesting ideas there. I'm looking forward to talking to Yael about
*  more about the computational psychiatry side of these things, too. So that'll be interesting.
*  What's the most critical open question that's intriguing you right now?
*  And I think the biggest the biggest question at some level, I think it's the question of CCN,
*  where does behavior come from? Right? Like what produces behavior? And that obviously is a big
*  question. But I think a lot of the interesting questions in neuroscience are about that. And a
*  lot of the sort of less interesting work in neuroscience, in my opinion, is the work that
*  neglects behavior or doesn't treat it as the sort of focus. And one of the great things about CCN,
*  I think, is it's a behavior conference. I have a let's see, what do I have in my pocket? Only
*  some change. But I'm willing to bet that I know the answer to your know your answer to this next
*  question. Let's say the question of figuring out behavior, right? That is intriguing to you
*  right now. What do you think we need more of to to figure this out? Do you think we need more
*  theory? Do you think we need more technology, more data, more models, if you had to choose one?
*  I think I think theory is is important. I mean, I don't think theory is an end in itself, exactly.
*  And I think it's all about the interplay between theory helping us understand experiments and
*  experiments helping us refine theories and so on. But and I've been very interested in my own work
*  and trying to really think hard about using theories and testing theories in the laboratory.
*  But I'm very pro theory, of course. I suppose what you were.
*  These are the quarters I'll be maintaining in my pocket and using in a one.
*  One of that. So I mean, and this is really related, but is theory the way that you approach
*  the lens through which you approach all problems? So we can talk about, for instance, David Maher's
*  levels, you know, like the computational level and the algorithmic level and the implementation
*  level. But, you know, do you approach it through like this sort of computational theory driven
*  level or through an evolutionary lens or through an ethical, you know, like, do you always approach
*  problems the same way and through what lens? Yeah, I'm a pretty unashamed Maher
*  computational level Maher fan, right? I really do think that a lot of the insight,
*  and this isn't incompatible with an evolutionary approach or whatever, obviously, but or
*  ethological, but there's so much insight in really specifying what the, you know, what the
*  organism's objective function is or something. What's the problem the organism is trying to
*  solve? Like one of the things I've learned from reinforcement, reinforcement is one thing. It's
*  like the Bellman equation. It's like a very careful quantification of what it is that you're
*  trying to do when you solve a decision problem that involves multiple steps, right? What does
*  it mean? Everything follows from that. Like you write that down carefully enough and all the
*  algorithms are just like different ways of evaluating the Bellman equation, you know,
*  for decades, right? And it's so beautiful. And there are all these algorithms for doing that.
*  And I think that's the interplay between the sort of computational, you know, goal and the
*  algorithms that instantiate or approximate that goal is sort of where, how I approach everything,
*  I guess, was a one trick pony in that respect. So let's get a little time machine. Let's move
*  forward 100 years. And we're thinking about our current era right now in neuroscience and AI.
*  What will we have to think or write about it? You know, what, how will people 100 years from now
*  view this era in neuroscience and AI? Well, I hope that they're, they view it as extremely primitive
*  and they understand a lot more. Maybe they'll have the, you know, the 60,000 page version of
*  Candle and Swartz and they'll long for a simpler time. No, by then there'll be more pages than
*  atoms in the universe. Yeah, exactly. This is why it actually that by the way, I tried to make that
*  plot recently and it slowed down like, you know, like, they have to keep up with their own. Yeah,
*  just the exactly, you know, I think it's hard to, of course, it's hard to predict.
*  I hope that we have, I mean, we just know so little, especially in neuroscience about how
*  the brain works, right? I think the reason that we know a lot about computer science,
*  I don't feel like the principles of computation AI are really, I feel like that's nice refinement.
*  And I don't think there's huge revolutions that are going to happen. I think it's, you know,
*  the crank keeps turning. So you think there's going to be a fundamental change shift in the
*  way we think about brains and, you know, another sort of revolution in neuroscience that's going
*  to really, we're going to look back on this and kind of be embarrassed. I mean, I think there's
*  sort of a hassle. I'm embarrassed now. I am too. Yeah. We don't know anything. I mean, it's just
*  so hopeless. Like, it's just so complicated. It's such a mess. You know, the reason that I'm so happy
*  talking at the computer science level is that that imposes some order on what would otherwise
*  just be, you know, just a mess. I think we're going to get better. We have to get better at
*  understanding it. And I think, you know, understanding computation in the abstract is part of that,
*  but I think we will get better in understanding the mechanism too. And at the moment, I think we
*  don't, I don't really have a hope currently, but that's going to hopefully change.
*  You have a hope that it's going to change. Well, if I, if I knocked your chair out the window and
*  you fell into a bath of liquid nitrogen or something, and I cryogenically froze you,
*  but on the way down in your fall, you got to tell me how long you wanted to be frozen.
*  What number, how many, how long would you want to be frozen?
*  Huh. I actually do think that kind of 100, 200 year kind of timeframe seems like the right,
*  at least for this purpose of revisiting where neuroscience is, that I think that's about the
*  right time to come back. I mean, so much has happened so fast, but still.
*  What about going back to the beginning of your own career? If you were going to start over,
*  how would you proceed differently? Or a similar question is, you know, how would you advise
*  people maybe of your same sort of mindset to begin their careers, even if they're,
*  you know, pretty early still in the career? Yeah, no, I think it's, that's obviously a great
*  question. The thing that I'm struggling with and Tim is as well, a lot of us is whether we need
*  rat labs, right? Or rodent labs. You need monkey labs. If you want to really slow your career down,
*  get a monkey lab. Yeah, well, that's it. That's either way, right? It's slow going. And I think
*  it's no accident, you know, and it's hard work and it requires a lot of expertise, attention and
*  thought. And it's, you know, I don't, I don't recommend it. Yeah. But on the other hand, like
*  there was this sort of, there was this moment in time that Tim and I and you know, we're all part
*  of and a bunch of us where, you know, human fMRI is something, it's a shared facility.
*  You could do experiments and do theory and, you know, mostly do theory and make a lot of progress.
*  And so there were just a whole bunch of us sort of made our careers that way where we used to go
*  back and forth between doing experiments that we could manage when we were sort of mostly full-time
*  theorists. And I think that's, you know, there's still stuff to do there. But like for me, these
*  questions that I'm running up against in the project we talked about, right. But and then
*  another project we didn't talk about their, their single neuron questions, the time scale
*  and the spatial scale is just not going to work with human neuroimaging. So we're sort of back,
*  are we going to bite the bullet and really invest in doing more detailed experiments? Right. And
*  maybe we're all at the point in our careers, we can do that now, or maybe it's too late. I'm not
*  sure. But I think, you know, Tim is also thinking about this, I think, just for instance.
*  That's going to slow it down, man. It's going to really slow it down.
*  It is. But yeah, it is that and that, you know, on the other hand, that's the still there I am
*  sold on the, you know, the exciting technologies and the things that are becoming possible.
*  And partly because the division of kind of labor and specialization, the people who are coming up
*  with the technologies aren't coming up with the behaviors and the, you know, computational models
*  and stuff, there really is. And maybe the other way to say this, apart from my own, outside of my
*  own sort of angst about my own career, the direction of what I'm going to work on, there's
*  real opportunities there, right, for people who know the stuff that, you know, my generation of
*  people knows, to take this into that world and run with it, right. I mean, that there's really
*  exciting stuff to be done there. It's not easy. And maybe, maybe it's not possible for someone
*  to know enough about viruses and electrodes and stuff at the same time they know about this,
*  and that just won't work. But it seems like there's real opportunities there. And questions are on
*  the face of it. What advice would you give to my nephew or something like or niece or something,
*  you know, like that's thinking about getting into this whole world, neuroscience, AI, cognition,
*  etc. No, part of it obviously is, you know, learn the math and the computer science and the modeling.
*  But I think, I do think if they were, you know, when I think about where do I want, where should
*  can I advise my grad students to go? Where are they going to make a difference and
*  have a comparative advantage and do new things? I think it's coming into contact with with areas
*  that haven't quite, you know, and one of them is kind of rhodid behavioral, you know,
*  fancy optogenetic neuroscience, right. And others are psychiatry. And, you know, I think
*  from where I'm sitting, the things that we're doing and know are worth knowing. And there are
*  lots of opportunities to take that, you know, to a field to new to conquer new areas and develop new
*  synergies. If you had to if you had a magic wand and you could just wave it and become an expert
*  in any topic that would help you forge ahead, what would what would that be? I mean, right now,
*  in the short term, I think it really would be like, rodent physiology. I know you think I'm crazy
*  here. And I have, you know, but there's just so many questions, like if I could just conjure up
*  a rat lab and, you know, that would be so that's worth doing, because it just takes so many
*  resources and it's such a drag to do that. That's worth waving a magic wand about. Exactly. Yeah,
*  but you notice I haven't actually done it because it really is. There's no wand. Yeah. So you have
*  an interesting situation in that both you and your wife, Yael Niv, are experts in this domain.
*  When you guys get together for holidays with family, what is it? What is it like trying to
*  describe what you do to family and you know, or friends who aren't in this field? I mean,
*  people are very polite, right? And you know, it's it's, you know, we can have polite conversations,
*  but it's hard to what's what's like the most difficult thing to communicate to have it land?
*  I mean, I think that not just with, you know, civilians, but with other neuroscientists. Yeah,
*  I feel like the the perspective, the sort of Marian perspective that what at least what I
*  really care about what really matters and what the way to really understand things is this
*  abstract level, the sort of what's the point of the endeavor, what you know, what's the result,
*  when should we be satisfied? I think, you know, when you talk to regular people, they have,
*  they have a view which we you know, which I also had and every, you know, lots of people have
*  that, you know, we're just going to sort of take apart the clock and like figure out how the little
*  pieces interact with little pieces, and we're going to figure out how the brain works. And then that
*  will, you know, help us build better computers or something. But and there's obviously a huge amount
*  of maybe the majority of neuroscience that's still kind of pursuing that. And my pessimism is
*  that that's just hopeless, right? That there are no organisms, we know the whole connectome for
*  forever, you have for decades, and, you know, don't understand a thing about how they work,
*  really. But thinking about things in a different way, and the goal is not this sort of physical
*  mimicry, or at least in the short term, is a tough thing to communicate both professionally and
*  personally, as it were. What is what's something that you used to believe that you consider naive
*  now? Well, that's an example, right? Actually, you know, the the first time when I first was
*  deciding where to go to grad school, actually, you know, I entered the field in 9697, right?
*  So I, you know, I came of age with the publication of this famous paper on the temporal difference
*  model, prediction error model of double neurons, right? Yeah. And I was actually thinking about
*  going to work with Peter, Dan, who I did end up working with my postdoc, during my PhD. And yeah,
*  I was reading this paper. And it just struck me as like, ridiculously abstract and obtuse,
*  and like removed from the real, you know, biology, basically. I probably have a version,
*  I probably threw it out. But somewhere, I probably have a version that had a version that was going
*  to marked up with my naive comments. Yeah, exactly. It's turned out my whole career is based
*  not just on this approach, but this paper, right? Yeah. But it, you know, it really does, you know,
*  you look at that paper, well, an appreciation for it, and it just looks like, and I encounter
*  this when I give talks, you know, like, what are you talking about? What does this have to do with
*  the brain, right? Like, it's just a bunch of symbols. And yeah, so it took me time to really,
*  to develop the conviction that that actually is the right way to think about things are a useful
*  way of thinking about things. You grew up in Boulder, right? Colorado. I did. Yeah.
*  I'm in Durango. What do I need to do in Boulder? Best place to eat in Boulder?
*  I like the kitchen, actually. Oh, the kitchen. I've heard of that place. Yeah. It's pretty good.
*  So did you grow up like, so people who live in Boulder really look down on people who don't
*  mountain climb and do like all sorts of at least like four or five different outdoor activities,
*  sort of semi professionally? Is that? Was that the case? I was never culturally all that. I moved
*  to New York and tried to pretend like that I'd always lived in New York and I was sort of more
*  of a Woody Allen. And in Boulder, I was never, you know, a rock climber, as it were. I see.
*  Well, Nathaniel, thank you so much. You spent so much time talking to me. I really appreciate it.
*  You can find Nathaniel on Twitter at Nathaniel Daw. And of course, I'll link to the paper and
*  some backup the paper we talked about and then some that sort of lead up to that paper as well.
*  I now release you to go continue your child care and eat a hamburger for God sakes.
*  Sounds great. Thank you. Thanks. Cool. Thanks a lot.
*  Brain Inspired is a production of me and you. You can support the show through Patreon for a
*  microscopic two or $4 per month. Go to braininspired.co and find the red Patreon button there.
*  Your contribution will help sustain and improve the show and prohibit any annoying advertisements
*  on other shows. To get in touch with me, email paul at braininspired.co. The music you hear
*  is by The New Year. Find them at thenewyear.net. Thanks for your support. See you next time.
*  Bye.

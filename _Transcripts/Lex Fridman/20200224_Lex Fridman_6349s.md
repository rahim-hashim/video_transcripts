---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 6349s
Video Keywords: ['michael i. jordan', 'machine learning', 'statistics', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 168544
Video Rating: None
Video Description: Michael I Jordan is a professor at Berkeley, and one of the most influential people in the history of machine learning, statistics, and artificial intelligence. He has been cited over 170,000 times and has mentored many of the world-class researchers defining the field of AI today, including Andrew Ng, Zoubin Ghahramani, Ben Taskar, and Yoshua Bengio.

This episode is presented by Cash App. Download it & use code "LexPodcast":
Cash App (App Store): https://apple.co/2sPrUHe
Cash App (Google Play): https://bit.ly/2MlvP5w

PODCAST INFO:
Podcast website:
https://lexfridman.com/podcast
Apple Podcasts:
https://apple.co/2lwqZIr
Spotify:
https://spoti.fi/2nEwCF8
RSS:
https://lexfridman.com/feed/podcast/
Full episodes playlist:
https://www.youtube.com/playlist?list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4
Clips playlist:
https://www.youtube.com/playlist?list=PLrAXtmErZgOeciFP3CBCIEElOJeitOr41

EPISODE LINKS:
(Blog post) Artificial Intelligence -- The Revolution Hasn’t Happened Yet:
https://hdsr.mitpress.mit.edu/pub/wot7mkc1

OUTLINE:
0:00 - Introduction
3:02 - How far are we in development of AI?
8:25 - Neuralink and brain-computer interfaces
14:49 - The term "artificial intelligence"
19:00 - Does science progress by ideas or personalities?
19:55 - Disagreement with Yann LeCun
23:53 - Recommender systems and distributed decision-making at scale
43:34 - Facebook, privacy, and trust
1:01:11 - Are human beings fundamentally good?
1:02:32 - Can a human life and society be modeled as an optimization problem?
1:04:27 - Is the world deterministic?
1:04:59 - Role of optimization in multi-agent systems
1:09:52 - Optimization of neural networks
1:16:08 - Beautiful idea in optimization: Nesterov acceleration
1:19:02 - What is statistics?
1:29:21 - What is intelligence?
1:37:01 - Advice for students
1:39:57 - Which language is more beautiful: English or French?

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# Michael I. Jordan Machine Learning, Recommender Systems, and Future of AI  Lex Fridman Podcast #74
**Lex Fridman:** [February 24, 2020](https://www.youtube.com/watch?v=EYIKy_FM9x0)
*  The following is a conversation with Michael I. Jordan,
*  a professor at Berkeley and one of the most influential
*  people in the history of machine learning,
*  statistics and artificial intelligence.
*  He has been cited over 170,000 times
*  and he has mentored many of the world-class researchers
*  defining the field of AI today,
*  including Andrew Eng, Zubin Garamani,
*  Van Tascar and Yoshua Bengio.
*  All this, to me, is as impressive as the over 32,000 points
*  in the six NBA championships of the Michael J. Jordan
*  of basketball fame.
*  There's a non-zero probability that I talk to
*  the other Michael Jordan, given my connection to
*  and love of the Chicago Bulls in the 90s,
*  but if I had to pick one, I'm going with the Michael Jordan
*  of statistics and computer science,
*  or as John LeCun calls him,
*  the Miles Davis of machine learning.
*  In his blog post titled,
*  Artificial Intelligence, The Revolution Hasn't Happened Yet,
*  Michael argues for broadening the scope
*  of the artificial intelligence field.
*  In many ways, the underlying spirit of this podcast
*  is the same, to see artificial intelligence
*  as a deeply human endeavor,
*  to not only engineer algorithms and robots,
*  but to understand and empower human beings
*  at all levels of abstraction,
*  from the individual to our civilization as a whole.
*  This is the Artificial Intelligence Podcast.
*  If you enjoy it, subscribe on YouTube,
*  give it five stars on Apple Podcast,
*  support it on Patreon, or simply connect with me on Twitter,
*  at Lex Friedman, spelled F-R-I-D-M-A-N.
*  As usual, I'll do one or two minutes of ads now,
*  and never any ads in the middle
*  that can break the flow of the conversation.
*  I hope that works for you,
*  and doesn't hurt the listening experience.
*  This show is presented by Cash App,
*  the number one finance app in the App Store.
*  When you get it, use code LexPodcast.
*  Cash App lets you send money to friends,
*  buy Bitcoin, and invest in the stock market
*  with as little as one dollar.
*  Since Cash App does fractional share trading,
*  let me mention that the order execution algorithm
*  that works behind the scenes to create the abstraction
*  of the fractional orders is, to me, an algorithmic marvel.
*  So big props for the Cash App engineers
*  for solving a hard problem that, in the end,
*  provides an easy interface that takes a step up
*  to the next layer of abstraction over the stock market,
*  making trading more accessible for new investors
*  and diversification much easier.
*  So once again, if you get Cash App from the App Store
*  or Google Play, and use the code LexPodcast,
*  you'll get $10, and Cash App will also donate $10 to first.
*  One of my favorite organizations
*  that is helping to advance robotics and STEM education
*  for young people around the world.
*  And now, here's my conversation with Michael I. Jordan.
*  Given that you're one of the greats in the field of AI,
*  machine learning, computer science, and so on,
*  you're trivially called the Michael Jordan
*  of machine learning.
*  Although, as you know, you were born first,
*  so technically MJ is the Michael I. Jordan of basketball,
*  but anyway, my favorite is Jan Lukuen calling you
*  the Miles Davis of machine learning,
*  because as he says, you reinvent yourself periodically
*  and sometimes leave fans scratching their heads
*  after you change direction.
*  So can you put, at first, your historian hat on
*  and give a history of computer science and AI
*  as you saw it, as you experienced it,
*  including the four generations of AI successes
*  that I've seen you talk about?
*  Sure.
*  Yeah, first of all, I much prefer Jan's metaphor.
*  Miles Davis was a real explorer in jazz
*  and he had a coherent story.
*  So I think I have one, but it's not just the one you lived,
*  it's the one you think about later.
*  What a good historian does is they look back
*  and they revisit.
*  I think what's happening right now is not AI.
*  That was an intellectual aspiration
*  that's still alive today as an aspiration.
*  But I think this is akin to the development
*  of chemical engineering from chemistry
*  or electrical engineering from electromagnetism.
*  So if you go back to the 30s or 40s,
*  there wasn't yet chemical engineering.
*  There was chemistry, there was fluid flow,
*  there was mechanics and so on.
*  But people pretty clearly viewed interesting goals,
*  tried to build factories that make chemicals products
*  and do it viably, safely, make good ones, do it at scale.
*  So people started to try to do that, of course,
*  and some factories worked, some didn't,
*  some were not viable, some exploded.
*  But in parallel, developed a whole field
*  called chemical engineering.
*  Chemical engineering is a field.
*  It's no bones about it.
*  It has theoretical aspects to it.
*  It has practical aspects.
*  It's not just engineering, quote unquote.
*  It's the real thing, real concepts are needed.
*  Same thing with electrical engineering.
*  There was Maxwell's equations, which in some sense
*  were everything you know about electromagnetism,
*  but you needed to figure out how to build circuits,
*  how to build modules, how to put them together,
*  how to bring electricity from one point to another
*  safely and so on and so forth.
*  So a whole field is developed called electrical engineering.
*  I think that's what's happening right now,
*  is that we have a proto field, which is statistics,
*  computer, more the theoretical side of it,
*  algorithmic side of it, computer science.
*  That was enough to start to build things, but what things?
*  Systems that bring value to human beings
*  and use human data and mix in human decisions.
*  The engineering side of that is all ad hoc.
*  That's what's emerging.
*  In fact, if you wanna call machine learning a field,
*  I think that's what it is.
*  That's a proto form of engineering based on statistical
*  and computational ideas of previous generations.
*  But do you think there's something deeper about AI
*  in his dreams and aspirations as compared
*  to chemical engineering and electrical engineering?
*  Well, the dreams and aspirations may be,
*  but those are 500 years from now.
*  I think that that's like the Greeks sitting there
*  and saying it would be neat to get to the moon someday.
*  Right.
*  I think we have no clue how the brain does computation.
*  We're just a clueless.
*  We're even worse than the Greeks
*  on most anything interesting scientifically of our era.
*  Can you linger on that just for a moment
*  because you stand not completely unique,
*  but a little bit unique in the clarity of that.
*  Can you elaborate your intuition of why we are,
*  like where we stand in our understanding of the human brain?
*  A lot of people say, neuroscientists say,
*  we're not very far in understanding human brain.
*  But you're saying we're in the dark here.
*  Well, I know I'm not unique.
*  I don't even think in the clarity,
*  but if you talk to real neuroscientists
*  that really study real synapses or real neurons,
*  they agree, they agree.
*  It's a hundreds of year task
*  and they're building it up slowly and surely.
*  What the signal is there is not clear.
*  We have all of our metaphors.
*  We think it's electrical, maybe it's chemical.
*  It's a whole soup.
*  It's ions and proteins and it's a cell.
*  And that's even around like a single synapse.
*  If you look at a electron micrograph of a single synapse,
*  it's a city of its own.
*  And that's one little thing on a dendritic tree,
*  which is extremely complicated electrochemical thing.
*  And it's doing these spikes and voltages
*  are flying around and then proteins are taking that
*  and taking it down into the DNA and who knows what.
*  So it is the problem of the next few centuries.
*  It is fantastic.
*  But we have our metaphors about it.
*  Is it an economic device?
*  Is it like the immune system?
*  Or is it like a layered set of arithmetic computations?
*  We have all these metaphors and they're fun.
*  But that's not real science per se.
*  There is neuroscience.
*  That's not neuroscience.
*  That's like the Greeks speculating
*  about how to get to the moon.
*  Fun, right?
*  And I think that I like to say this fairly strongly
*  because I think a lot of young people think
*  we're on the verge.
*  Because a lot of people who don't talk about it clearly
*  let it be understood that yes,
*  this is brain inspired.
*  We're kind of close.
*  Breakthroughs are on the horizon.
*  And unscrupulous people sometimes
*  who need money for their labs.
*  As I say unscrupulous, but people will oversell.
*  I need money from a lab.
*  I'm studying computational neuroscience.
*  I'm gonna oversell it.
*  And so there's been too much of that.
*  So step into the gray area between metaphor and engineering
*  with I'm not sure if you're familiar
*  with brain computer interfaces.
*  So a company like Elon Musk has Neuralink
*  that's working on putting electrodes into the brain
*  and trying to be able to read both read
*  and send electrical signals.
*  Just as you said, even the basic mechanism of communication
*  in the brain is not something we understand.
*  But do you hope without understanding
*  the fundamental principles of how the brain works,
*  we'll be able to do something interesting
*  at that gray area of metaphor?
*  It's not my area.
*  So I hope in the sense like anybody else hopes
*  for some interesting things to happen from research.
*  I would expect more something like Alzheimer's
*  will get figured out from modern neuroscience.
*  That there's a lot of human suffering
*  based on brain disease.
*  And we throw things like lithium at the brain.
*  It kind of works.
*  No one has a clue why.
*  That's not quite true, but mostly we don't know.
*  And that's even just about the biochemistry of the brain.
*  And how it leads to mood swings and so on.
*  How thought emerges from that.
*  We were really, really completely dim.
*  So that you might wanna hook up electrodes
*  and try to do some signal processing on that
*  and try to find patterns.
*  Fine, by all means go for it.
*  It's just not scientific at this point.
*  It's just, so it's like kind of sitting in a satellite
*  and watching the emissions from a city
*  and trying to affirm things about the micro economy
*  even though you don't have micro economic concepts.
*  I mean, it's really that kind of thing.
*  And so yes, can you find some signals
*  that do something interesting or useful?
*  Can you control a cursor or a mouse with your brain?
*  Yeah, absolutely.
*  And then I can imagine business models based on that.
*  And even medical applications of that.
*  But from there to understanding algorithms
*  that allow us to really tie in deeply
*  from the brain to computer.
*  I just, no, I don't agree with Elon Musk.
*  I don't think that's even, that's not for our generation.
*  It's not even for the century.
*  So just in the hopes of getting you to dream,
*  you've mentioned Kolmogorov and Turing might pop up.
*  Do you think that there might be breakthroughs
*  that will get you to sit back in five, 10 years
*  and say, wow?
*  Oh, I'm sure there will be,
*  but I don't think that there'll be demos that impress me.
*  I don't think that having a computer call a restaurant
*  and pretend to be a human is a breakthrough.
*  Some people present it as such.
*  It's imitating human intelligence.
*  It's even putting coughs in the thing
*  to make a bit of a PR stunt.
*  And so fine, the world runs on those things too.
*  And I don't want to diminish all the hard work
*  and engineering that goes behind things like that
*  and the ultimate value to the human race.
*  But that's not scientific understanding.
*  And I know the people that work on these things,
*  they are after scientific understanding.
*  In the meantime, they've got to kind of,
*  the trains got to run and they got mouths to feed
*  and they got things to do.
*  And there's nothing wrong with all that.
*  I would call that though, just engineering.
*  And I want to distinguish that between an engineering field
*  like electrical engineering, chemical engineering
*  that originally emerged that had real principles
*  and you really knew what you were doing
*  and you had a little scientific understanding,
*  maybe not even complete.
*  So it became more predictable
*  and it was really gave value to human life
*  because it was understood.
*  And so we don't want to muddle too much these waters
*  of what we're able to do versus what we really can do
*  in a way that's going to impress the next.
*  So I don't need to be wowed,
*  but I think that someone comes along in 20 years,
*  a younger person who's absorbed all the technology
*  and for them to be wowed,
*  I think they have to be more deeply impressed.
*  A young Kolmogorov would not be wowed by some of the stunts
*  that you see right now coming from the big companies.
*  The demos, but do you think the breakthroughs
*  from Kolmogorov would be,
*  and give this question a chance,
*  do you think they'll be in the scientific
*  fundamental principles arena
*  or do you think it's possible
*  to have fundamental breakthroughs in engineering?
*  Meaning, I would say some of the things
*  that Elon Musk is working with SpaceX and then others,
*  sort of trying to revolutionize the fundamentals
*  of engineering, of manufacturing, of saying,
*  here's a problem we know how to do a demo of
*  and actually taking it to scale.
*  Yeah, so there's going to be all kinds of breakthroughs.
*  I just don't like that terminology.
*  I'm a scientist and I work on things day in and day out
*  and things move along and eventually say,
*  wow, something happened,
*  but I don't like that language very much.
*  Also, I don't like to prize theoretical breakthroughs
*  over practical ones.
*  I tend to be more of a theoretician
*  and I think there's lots to do in that arena right now.
*  And so I wouldn't point to the Kolmogorovs,
*  I might point to the Edison's of the era
*  and maybe Musk is a bit more like that.
*  But, you know, Musk, God bless him,
*  also will say things about AI
*  that he knows very little about.
*  And he leads people astray when he talks about things
*  he doesn't know anything about.
*  Trying to program a computer to understand natural language,
*  to be involved in a dialogue we're having right now,
*  ain't gonna happen in our lifetime.
*  You could fake it, you can mimic,
*  sort of take old sentences that humans use and retread them,
*  but the deep understanding of language,
*  no, it's not gonna happen.
*  And so from that, you know, I hope you can perceive
*  that the deeper, yet deeper kind of aspects
*  in intelligence are not gonna happen.
*  Now, will there be breakthroughs?
*  No, I think that Google was a breakthrough.
*  I think Amazon is a breakthrough.
*  I think Uber is a breakthrough.
*  Bring value to human beings at scale in brand new ways
*  based on data flows and so on.
*  A lot of these things are slightly broken
*  because there's not a kind of a engineering field
*  that takes economic value in context of data
*  and planetary scale and worries about all the externalities,
*  the privacy.
*  You know, we don't have that field
*  so we don't think these things through very well.
*  But I see that as emerging
*  and that will be, you know, looking back from 100 years,
*  that will be a constituted breakthrough in this era,
*  just like electrical engineering was a breakthrough
*  in the early part of the last century
*  and chemical engineering was a breakthrough.
*  So the scale, the markets that you talk about
*  and we'll get to, will be seen as sort of breakthrough.
*  And we're in very early days
*  of really doing interesting stuff there.
*  And we'll get to that,
*  but it's just taking a quick step back.
*  Can you give, we kind of threw off the historian hat.
*  I mean, you briefly said that the history of AI
*  kind of mimics the history of chemical engineering, but.
*  I keep saying machine learning.
*  You keep wanting to say AI just to let you know,
*  I don't, you know, I'd resist that.
*  I don't think this is about,
*  AI really was John McCarthy as almost a philosopher saying,
*  wouldn't it be cool if we could put thought in a computer?
*  If we could mimic the human capability to think
*  or put intelligence in, in some sense, into a computer.
*  That's an interesting philosophical question.
*  And he wanted to make it more than philosophy.
*  He wanted to actually write down a logical formula
*  and algorithms that would do that.
*  And that is a perfectly valid, reasonable thing to do.
*  That's not what's happening in this era.
*  Right.
*  So the reason I keep saying AI actually,
*  and I'd love to hear what you think about it.
*  Machine learning has a very particular
*  set of methods and tools.
*  Maybe your version of it is that mine doesn't.
*  No, it doesn't. Mine is very, very open.
*  It does optimization, it does sampling, it does.
*  So systems that learn is what machine learning is.
*  Systems that learn and make decisions.
*  And make decisions.
*  So it's not just pattern recognition
*  and finding patterns.
*  It's all about making decisions in real worlds
*  and having close feedback loops.
*  So something like symbolic AI, expert systems,
*  reasoning systems, knowledge-based representation,
*  all of those kinds of things, search.
*  Does that neighbor fit into
*  what you think of as machine learning?
*  So I don't even like the word machine learning.
*  I think that with the field you're talking about
*  is all about making large collections of decisions
*  under uncertainty by large collections of entities.
*  Yes. Right?
*  And there are principles for that, at that scale.
*  You don't have to say the principles
*  are for a single entity that's making decisions.
*  Single agent or single human.
*  It really immediately goes to the network of decisions.
*  Is a good word for that or not?
*  No, there's no good words for any of this.
*  That's kind of part of the problem.
*  So we can continue the conversation to use AI for all that.
*  I just want to kind of raise the flag here
*  that this is not about, we don't know what intelligence is
*  and real intelligence.
*  We don't know much about abstraction
*  and reasoning at the level of humans.
*  We don't have a clue.
*  We're not trying to build that
*  because we don't have a clue.
*  Eventually it may emerge.
*  I don't know if there'll be breakthroughs,
*  but eventually we'll start to get glimmers of that.
*  It's not what's happening there right now.
*  We're taking data.
*  We're trying to make good decisions based on that.
*  We're trying to do it scale.
*  We're trying to do it economically viably.
*  We're trying to build markets.
*  We're trying to keep value at that scale.
*  And aspects of this will look intelligent.
*  Computers were so dumb before.
*  They will seem more intelligent.
*  We will use that buzzword of intelligence.
*  So we can use it in that sense.
*  But so machine learning, you can scope it narrowly
*  as just learning from data and pattern recognition.
*  But whatever, when I talk about these topics,
*  maybe data science is another word
*  you could throw in the mix.
*  It really is important that the decisions are as part of it.
*  It's consequential decisions in the real world.
*  Or am I gonna have a medical operation?
*  Am I gonna drive down this street?
*  Things that are scarcity.
*  Things that impact other human beings
*  or other environments and so on.
*  How do I do that based on data?
*  How do I do that adaptably?
*  How do I use computers to help those kind of things
*  go forward?
*  Whatever you wanna call that.
*  So let's call it AI.
*  Let's agree to call it AI.
*  But let's not say that what the goal of that is
*  is intelligence.
*  The goal of that is really good working systems
*  at planetary scale that we've never seen before.
*  So reclaim the word AI from the Dartmouth Conference
*  from many decades ago of the dream of human.
*  I don't wanna reclaim it.
*  I want a new word.
*  I think it was a bad choice.
*  I mean, if you read one of my little things,
*  the history was basically that McCarthy needed a new name
*  because cybernetics already existed.
*  And he didn't like, you know,
*  no one really liked Norbert Wiener.
*  Norbert Wiener was kind of an island to himself.
*  And he felt that he had encompassed all this.
*  And in some sense he did.
*  You look at the language of cybernetics,
*  it was everything we're talking about.
*  It was control theory and signal processing
*  and some notions of intelligence
*  and close feedback loops and data.
*  It was all there.
*  It's just not a word that lived on partly
*  because of maybe the personalities.
*  But McCarthy needed a new word to say,
*  I'm different from you.
*  I'm not part of your show.
*  I got my own.
*  Invented this word.
*  And again, as a kind of thinking forward
*  about the movies that would be made about it,
*  it was a great choice.
*  But thinking forward about creating a sober academic
*  and real world discipline, it was a terrible choice
*  because it led to promises that are not true.
*  That we understand.
*  We understand artificial perhaps,
*  but we don't understand intelligence.
*  As a small tangent, because you're one
*  of the great personalities of machine learning,
*  whatever the heck you call the field,
*  the, do you think science progresses by personalities
*  or by the fundamental principles and theories
*  and research that's outside of personalities?
*  Both.
*  And I wouldn't say there should be one kind of personality.
*  I have mine and I have my preferences
*  and I have a kind of network around me that feeds me
*  and some of them agree with me and some of them disagree.
*  But all kinds of personalities are needed.
*  Right now, I think the personality
*  that it's a little too exuberant,
*  a little bit too ready to promise the moon
*  is a little bit too much in ascendance.
*  And I do think that there's some good to that.
*  It certainly attracts lots of young people to our field.
*  But a lot of those people come in with strong misconceptions
*  and they have to then unlearn those
*  and then find something to do.
*  And so I think there's just gotta be some multiple voices
*  and I wasn't hearing enough of the more sober voice.
*  So as a continuation of a fun tangent
*  and speaking of vibrant personalities,
*  what would you say is the most interesting disagreement
*  you have with Jan LeCun?
*  So Jan's an old friend and I just say that
*  I don't think we disagree about very much really.
*  He and I both kind of have a let's build that kind of
*  mentality and does it work kind of mentality
*  and kind of concrete.
*  We both speak French and we speak French more together
*  and we have a lot in common.
*  And so if one wanted to highlight a disagreement,
*  it's not really a fundamental one.
*  I think it's just kind of what we're emphasizing.
*  Jan has emphasized pattern recognition
*  and has emphasized prediction.
*  And it's interesting to try to take that as far as you can.
*  If you could do perfect prediction,
*  what would that give you kind of as a thought experiment?
*  And I think that's way too limited.
*  We cannot do perfect prediction.
*  We will never have the data sets that allow me
*  to figure out what you're about ready to do,
*  what question you're gonna ask next.
*  I have no clue.
*  I will never know such things.
*  Moreover, most of us find ourselves during the day
*  in all kinds of situations we had no anticipation of
*  that are kind of very novel in various ways.
*  And in that moment, we want to think through what we want.
*  And also there's gonna be market forces acting on us.
*  I'd like to go down that street, but now it's full
*  because there's a crane in the street.
*  I gotta think about that.
*  I gotta think about what I might really want here.
*  And I gotta sort of think about how much it costs me
*  to do this action versus this action.
*  I gotta think about the risks involved.
*  A lot of our current pattern recognition
*  and prediction systems don't do any risk evaluations.
*  They have no error bars, right?
*  I gotta think about other people's decisions around me.
*  I gotta think about a collection of my decisions.
*  Even just thinking about like a medical treatment.
*  I gotta take the prediction of a neural net
*  about my health, about something consequential.
*  Am I about ready to have a heart attack
*  because some number is over 0.7?
*  Even if you had all the data in the world
*  that's ever been collected about heart attacks
*  better than any doctor ever had,
*  I'm not gonna trust the output of that neural net
*  to predict my heart attack.
*  I'm gonna wanna ask what if questions around that.
*  I'm gonna wanna look at some us or other possible data
*  I didn't have, causal things.
*  I'm gonna wanna have a dialogue with a doctor
*  about things we didn't think about
*  when we gathered the data.
*  I could go on and on, I hope you can see.
*  And I think that if you say prediction is everything
*  that you're missing all of this stuff.
*  And so prediction plus decision making is everything,
*  but both of them are equally important.
*  And so the field has emphasized prediction.
*  Ayan, rightly so, has seen how powerful that is.
*  But at the cost of people not being aware
*  that decision making is where the rubber really hits the road
*  where human lives are at stake,
*  where risks are being taken,
*  where you gotta gather more data.
*  You gotta think about the error bars.
*  You gotta think about the consequences
*  of your decisions on others.
*  You gotta think about the economy around your decisions.
*  Blah, blah, blah, blah.
*  I'm not the only one working on those,
*  but we're a smaller tribe.
*  And right now we're not the one
*  that people talk about the most.
*  But if you go out in the real world and industry,
*  at Amazon, I'd say half the people there
*  are working on decision making
*  and the other half are doing the pattern recognition.
*  It's important.
*  And the words of pattern recognition and prediction,
*  I think the distinction there, not to linger on words,
*  but the distinction there is more a constrained
*  in the lab data set versus decision making
*  is talking about consequential decisions in the real world
*  under the messiness and the uncertainty of the real world.
*  And just the whole of it,
*  the whole mess of it that actually touches human beings
*  and scale, like you said, market forces,
*  that's the distinction.
*  Yeah, it helps add that perspective,
*  that broader perspective.
*  I mean, you're right.
*  I totally agree.
*  On the other hand, if you're a real prediction person,
*  of course you want it to be in the real world.
*  You wanna predict real world events.
*  I'm just saying that's not possible with just data sets.
*  That it has to be in the context of strategic things
*  that someone's doing, data they might gather,
*  things they could have gathered,
*  the reasoning process around data.
*  It's not just taking data
*  and making predictions based on the data.
*  So one of the things that you're working on,
*  I'm sure there's others working on it,
*  but I don't hear often it talked about,
*  especially in the clarity that you talk about it.
*  And I think it's both the most exciting
*  and the most concerning area of AI
*  in terms of decision making.
*  So you've talked about AI systems
*  that help make decisions that scale in a distributed way,
*  millions, billions decisions,
*  and sort of markets of decisions.
*  Can you, as a starting point,
*  sort of give an example of a system that you think about
*  when you're thinking about these kinds of systems?
*  Yeah, so first of all,
*  you're absolutely getting into some territory,
*  which I will be beyond my expertise.
*  And there are lots of things
*  that are gonna be very not obvious to think about.
*  Just like, again, I like to think about history a little bit,
*  but think about, put yourself back in the 60s.
*  There was kind of a banking system
*  that wasn't computerized really.
*  There was database theory emerging.
*  And database people had to think about,
*  how do I actually not just move data around,
*  but actual money and have it be valid
*  and have transactions that ATMs happen
*  that are actually all valid and so on and so forth.
*  So that's the kind of issues you get into
*  when you start to get serious about things like this.
*  I like to think about as kind of almost a thought experiment
*  to help me think something simpler,
*  which is the music market.
*  And, because there is, to first order,
*  there is no music market in the world right now,
*  in our country for sure.
*  There are something called, things called record companies,
*  and they make money,
*  and they prop up a few really good musicians
*  and make them superstars,
*  and they all make huge amounts of money.
*  But there's a long tail of huge numbers of people
*  that make lots and lots of really good music
*  that is actually listened to by more people
*  than the famous people.
*  They are not in a market, they cannot have a career.
*  They do not make money.
*  The creators, the creators.
*  The creators, the so-called influencers or whatever,
*  that diminishes who they are, right?
*  So there are people who make extremely good music,
*  especially in the hip hop or Latin world these days.
*  They do it on their laptop, that's what they do.
*  On the weekend, and they have another job during the week,
*  and they put it up on SoundCloud or other sites.
*  Eventually it gets streamed, it now gets turned into bits.
*  It's not economically valuable.
*  The information is lost.
*  It gets put up there, people stream it.
*  You walk around in a big city,
*  you see people with headphones,
*  especially young kids listening to music all the time.
*  If you look at the data,
*  very little of the music they listen to
*  is the famous people's music, and none of it's old music.
*  It's all the latest stuff.
*  But the people who made that latest stuff
*  are like some 16 year old somewhere
*  who will never make a career out of this,
*  who will never make money.
*  Of course, there'll be a few counter examples.
*  The record companies incentivize to pick out a few
*  and highlight them.
*  Long story short, there's a missing market there.
*  Consumer producer relationship
*  at the level of the actual creative acts.
*  The pipelines and Spotify's of the world
*  that take this stuff and stream it along,
*  they make money off of subscriptions or advertising
*  and those things.
*  They're making the money, all right?
*  And then they will offer bits and pieces of it
*  to a few people, again, to highlight that,
*  you know, they simulate a market.
*  Anyway, a real market would be,
*  if you're a creator of music,
*  that you actually are somebody who's good enough
*  that people wanna listen to you,
*  you should have the data available to you.
*  There should be a dashboard
*  showing a map of the United States.
*  So in last week, here's all the places
*  your songs were listened to.
*  It should be transparent, vetable
*  so that if someone in down in Providence
*  sees that you're being listened to 10,000 times
*  in Providence, that they know that's real data,
*  you know it's real data,
*  they will have you come give a show down there.
*  They will broadcast to the people who've been listening
*  to you that you're coming.
*  If you do this right, you could, you know,
*  go down there and make $20,000.
*  You do that three times a year,
*  you start to have a career.
*  So in this sense, AI creates jobs.
*  It's not about taking away human jobs,
*  it's creating new jobs because it creates a new market.
*  Once you've created a market,
*  you've now connected up producers and consumers.
*  You know, the person who's making the music
*  can say to someone who comes to their shows a lot,
*  hey, I'll play your daughter's wedding for $10,000.
*  You'll say 8,000, they'll say 9,000.
*  Then you, again, you can now get an income up to $100,000.
*  You're not gonna be a millionaire, all right?
*  And now even think about really the value of music
*  is in these personal connections,
*  even so much so that a young kid wants to wear a t-shirt
*  with their favorite musician's signature on it, right?
*  So if they listen to the music on the internet,
*  the internet should be able to provide them
*  with a button that they push
*  and the merchandise arrives the next day.
*  We can do that, right?
*  And now why should we do that?
*  Well, because the kid who bought the shirt will be happy,
*  but more the person who made the music will get the money.
*  There's no advertising needed, right?
*  So you could create markets between producers and consumers,
*  take 5% cut, your company will be perfectly sound,
*  it'll go forward into the future,
*  and it will create new markets,
*  and that raises human happiness.
*  Now, this seems like, well, this is easy,
*  just create this dashboard,
*  kind of create some connections and all that,
*  but if you think about Uber or whatever,
*  you think about the challenges in the real world
*  of doing things like this,
*  and there are actually new principles gonna be needed.
*  You're trying to create a new kind of two-way market
*  at a different scale that's ever been done before.
*  There's gonna be unwanted aspects of the market,
*  there'll be bad people,
*  there'll be the data will get used in the wrong ways,
*  it'll fail in some ways, it won't deliver a value.
*  You have to think that through,
*  just like anyone who ran a big auction
*  or ran a big matching service in economics
*  will think these things through.
*  And so that maybe doesn't get it.
*  All the huge issues that can arise
*  when you start to create markets,
*  but it starts for at least for me, solidify my thoughts
*  and allow me to move forward in my own thinking.
*  Yeah, so I talked to, had a research at Spotify, actually,
*  and I think their long-term goal, they've said,
*  is to have at least one million creators
*  make a comfortable living putting on Spotify.
*  So, and I think you articulate a really nice vision
*  of the world and the digital and the cyberspace of markets.
*  What do you think companies like Spotify or YouTube
*  or Netflix can do to create such markets?
*  Is it an AI problem?
*  Is it an interface problem?
*  So interface design, is it some other kind of,
*  is it an economics problem?
*  Who should they hire to solve these problems?
*  Well, part of it's not just top down.
*  So the Silicon Valley has this attitude
*  that they know how to do it.
*  They will create the system,
*  just like Google did with the search box,
*  that will be so good that they'll just,
*  everyone will adopt that, right?
*  It's not, it's everything you said,
*  but really, I think missing that kind of culture, all right?
*  So it's literally that 16 year old
*  who's able to create the songs.
*  You don't create that as a Silicon Valley entity.
*  You don't hire them per se, right?
*  You have to create an ecosystem in which they are wanted
*  and that they're belong, right?
*  And so you have to have some cultural credibility
*  to do things like this.
*  Netflix, to their credit,
*  wanted some of that sort of credibility
*  and they created shows, content.
*  They call it content, it's such a terrible word,
*  but it's culture, right?
*  And so with movies, you can kind of go give
*  large sum of money to somebody
*  graduating from the USC film school.
*  It's a whole thing of its own,
*  but it's kind of like rich white people's thing to do.
*  And American culture has not been so much
*  about rich white people.
*  It's been about all the immigrants,
*  all the Africans who came and brought that culture
*  and those rhythms to this world
*  and created this whole new thing, American culture.
*  And so companies can't artificially create that.
*  They can't just say, hey, we're here,
*  we're gonna buy it up.
*  You got a partner.
*  And so, but anyway, not to denigrate,
*  these companies are all trying and they should
*  and I'm sure they're asking these questions
*  and some of them are even making an effort,
*  but it is partly a respect the culture
*  as a technology person.
*  You gotta blend your technology with cultural meaning.
*  How much of a role do you think the algorithm,
*  so machine learning has in connecting the consumer
*  to the creator, sort of the recommender system aspect
*  of this?
*  Yeah, it's a great question.
*  I think pretty high.
*  There's no magic in the algorithms,
*  but a good recommender system is way better
*  than a bad recommender system.
*  And recommender systems is a billion dollar industry
*  back even 10, 20 years ago.
*  And it continues to be extremely important going forward.
*  What's your favorite recommender system
*  just so we can put something?
*  Well, just historically, I was one of the,
*  I first went to Amazon.
*  I first didn't like Amazon
*  because they put the book people out of business
*  or the library, the local booksellers went out of business.
*  I've come to accept that there probably are more books
*  being sold now and poor people reading them than ever before
*  and then local books stores are coming back.
*  So that's how economics sometimes work.
*  You go up and you go down.
*  But anyway, when I finally started going there
*  and I bought a few books,
*  I was really pleased to see another few books
*  being recommended to me that I never would have thought of.
*  And I bought a bunch of them.
*  So they obviously had a good business model,
*  but I learned things and I still to this day
*  kind of browse using that service.
*  And I think lots of people get a lot,
*  you know, that is a good aspect of a recommendation system.
*  I'm learning from my peers in an indirect way.
*  And their algorithms are not meant to have them impose
*  what we learn.
*  It really is trying to find out what's in the data.
*  It doesn't work so well for other kinds of entities,
*  but that's just the complexity of human life, like shirts.
*  You know, I'm not going to get recommendations on shirts.
*  But that's interesting.
*  If you try to recommend restaurants,
*  it's hard.
*  It's hard to do it at scale.
*  But a blend of recommendation systems
*  with other economic ideas,
*  matchings and so on,
*  is really, really still very open research-wise
*  and there's new companies that are going to emerge
*  that do that well.
*  What do you think is going to the messy, difficult land
*  of say, politics and things like that,
*  that YouTube and Twitter have to deal with
*  in terms of recommendation systems?
*  Being able to suggest,
*  I think Facebook just launched Facebook News.
*  So they're having,
*  recommend the kind of news that are most likely
*  for you to be interesting.
*  You think this is AI-solvable,
*  again, whatever term one would use.
*  Do you think it's a solvable problem for machines
*  or is it a deeply human problem that's unsolvable?
*  So I don't even think about it at that level.
*  I think that what's broken with some of these companies,
*  it's all monetization by advertising.
*  They're not, at least Facebook,
*  I want to critique them,
*  but they didn't really try to connect a producer
*  and a consumer in an economic way.
*  No one wants to pay for anything.
*  And so they all, starting with Google, then Facebook,
*  they went back to the playbook
*  of the television companies back in the day.
*  No one wanted to pay for this signal.
*  They will pay for the TV box, but not for the signal,
*  at least back in the day.
*  And so advertising kind of filled that gap
*  and advertising was new and interesting
*  and it somehow didn't take over our lives quite, right?
*  Fast forward, Google provides a service
*  that people don't want to pay for.
*  And so somewhat surprisingly in the 90s,
*  they made, ended up making huge amounts
*  so they cornered the advertising market.
*  It didn't seem like that was going to happen,
*  at least to me.
*  These little things on the right-hand side of the screen
*  just did not seem all that economically interesting,
*  but that companies had maybe no other choice.
*  The TV market was going away and billboards and so on.
*  So they got it.
*  And I think that sadly that Google just has,
*  it was doing so well with that and making such,
*  they didn't think much more about how,
*  wait a minute, is there a producer-consumer relationship
*  to be set up here?
*  Not just between us and the advertisers market to be created.
*  Is there an actual market between the producer and consumer?
*  They're the producers, the person who created
*  that video clip, the person that made that website,
*  the person who could make more such things,
*  the person who could adjust it as a function of demand,
*  the person on the other side who's asking
*  for different kinds of things.
*  So you see glimmers of that now.
*  There's influencers and there's kind of a little glimmering
*  of a market, but it should have been done 20 years ago.
*  It should have been thought about.
*  It should have been created in parallel
*  with the advertising ecosystem.
*  And then Facebook inherited that,
*  and I think they also didn't think very much about that.
*  So fast forward and now they are making huge amounts
*  of money off of advertising,
*  and the news thing and all these clicks
*  is just feeding the advertising.
*  It's all connected up to the advertising.
*  So you want more people to click on certain things
*  because that money flows to you, Facebook.
*  You're very much incentivized to do that.
*  And when you start to find it's breaking,
*  so people are telling you, well,
*  we're getting into some troubles.
*  You try to adjust it with your smart AI algorithms, right?
*  And figure out what are bad clicks.
*  So maybe shouldn't be click-through rated.
*  I find that pretty much hopeless.
*  It does get into all the complexity of human life,
*  and you can try to fix it, you should,
*  but you could also fix the whole business model.
*  And the other thing is that really,
*  are there some human producers and consumers out there?
*  Is there some economic value to be liberated
*  by connecting them directly?
*  Is it such that it's so valuable
*  that people will be willing to pay for it?
*  All right?
*  And when they-
*  Micro payments, like small payments.
*  Micro, but even after you micro.
*  So I like the example.
*  Suppose next week I'm going to India.
*  Never been to India before, right?
*  I have a couple of days in Mumbai.
*  I have no idea what to do there, right?
*  And I could go on the web right now and search.
*  It's gonna be kind of hopeless.
*  I'm not gonna find.
*  I'll have lots of advertisers in my face, right?
*  What I really wanna do is broadcast to the world
*  that I am going to Mumbai
*  and have someone on the other side of a market look at me.
*  And there's a recommendation system there.
*  So they're not looking at all possible people
*  coming to Mumbai.
*  They're looking at the people who are relevant to them.
*  So someone in my age group,
*  someone who kind of knows me at some level.
*  I give up a little privacy by that,
*  but I'm happy because what I'm gonna get back
*  is this person can make a little video for me,
*  or they're gonna write a little two page paper
*  on here's the cool things that you want to do
*  in Mumbai this week, especially, right?
*  I'm gonna look at that.
*  I'm not gonna pay a micro payment.
*  I'm gonna pay $100 or whatever for that.
*  It's real value.
*  It's like journalism.
*  And as an odd subscription,
*  it's that I'm gonna pay that person in that moment.
*  Company is gonna take 5% of that.
*  And that person has now got it.
*  It's a gig economy, if you will,
*  but done for thinking about a little bit.
*  Behind YouTube, there was actually people
*  who could make more of those things.
*  If they were connected to a market,
*  they would make more of those things independently.
*  You don't have to tell them what to do.
*  You don't have to incentivize them.
*  Any other way.
*  And so, yeah, these companies,
*  I don't think I've thought long and hard about that.
*  So I do distinguish on Facebook on the one side,
*  who just not thought about these things at all.
*  I think thinking that AI will fix everything.
*  And Amazon thinks about them all the time
*  because they were already out in the real world.
*  They were delivering packages to people's doors.
*  They were worried about a market.
*  They were worried about sellers.
*  And they worry and some things they do are great.
*  Some things maybe not so great,
*  but they're in that business model.
*  And then I'd say Google sort of hover somewhere in between.
*  I don't think for a long, long time,
*  they got it.
*  I think they probably see that YouTube
*  is more pregnant with possibility
*  than they might have thought.
*  And that they're probably heading that direction.
*  But Silicon Valley's been dominated
*  by the Google Facebook kind of mentality
*  and the subscription and advertising.
*  And that's the core problem, right?
*  The fake news actually rides on top of that
*  because it means that you're monetizing
*  with clip through rate.
*  And that is the core problem.
*  You gotta remove that.
*  So advertisement, if we're gonna linger on that,
*  I mean, that's an interesting thesis.
*  I don't know if everyone really deeply thinks about that.
*  So you're right.
*  The thought is the advertisement model
*  is the only thing we have, the only thing we'll ever have.
*  So we have to fix, we have to build algorithms
*  that despite that business model,
*  find the better angels of our nature
*  and do good by society and by the individual.
*  But you think we can slowly,
*  you think, first of all,
*  there's a difference between should and could.
*  So you're saying we should slowly move away
*  from the advertising model and have a direct connection
*  between the consumer and the creator.
*  The question I also have is can we?
*  Because the advertising model is so successful now
*  in terms of just making a huge amount of money
*  and therefore being able to build a big company
*  that provides, has really smart people working
*  that create a good service.
*  So you think it's possible?
*  And just to clarify, you think we should move away?
*  Well, I think we should, yeah.
*  But we is the, you know, me.
*  Society.
*  Yeah, well, the companies.
*  I mean, so first of all, full disclosure,
*  I'm doing a day a week at Amazon
*  because I kind of want to learn more about how they do things.
*  So I'm not speaking for Amazon in any way,
*  but I did go there because I actually believe
*  they get a little bit of this
*  or trying to create these markets.
*  And they don't really use,
*  advertisement is not a crucial part of it.
*  That's a good question.
*  So it has become not crucial,
*  but it's more present if you go to Amazon website
*  and without revealing too many deep secrets about Amazon,
*  I can tell you that a lot of people in the company
*  question this and there's a huge questioning going on.
*  You do not want a world where there's zero advertising.
*  That actually is a bad world, okay?
*  So here's a way to think about it.
*  You're a company that like Amazon
*  is trying to bring products to customers, right?
*  And the customer, at any given moment,
*  you want to buy a vacuum cleaner, say.
*  You want to know what's available for me.
*  And it's not going to be that obvious.
*  You have to do a little bit of work at it.
*  The recommendation system will sort of help, right?
*  But now suppose this other person over here
*  has just made the world,
*  they spent a huge amount of energy.
*  They had a great idea.
*  They made a great vacuum cleaner.
*  They know, they really did it.
*  They nailed it.
*  It's an MIT, you know, Wizz kid
*  that made a great new vacuum cleaner, right?
*  It's not going to be in the recommendation system.
*  No one will know about it.
*  The algorithms will not find it
*  and AI will not fix that, okay, at all, right?
*  How do you allow that vacuum cleaner
*  to start to get in front of people, be sold?
*  Well, advertising.
*  And here what advertising is,
*  is a signal that you believe in your product enough
*  that you're willing to pay some real money for it.
*  And to me as a consumer, I look at that signal and I say,
*  well, first of all, I know these are not just cheap little ads
*  because we have now right now.
*  I know that these are super cheap, pennies.
*  If I see an ad where it's actually,
*  I know the company is only doing a few of these
*  and they're making real money is kind of flowing.
*  And I see an ad, I may pay more attention to it.
*  And I actually might want that
*  because I see, hey, that guy spent money
*  on his vacuum cleaner.
*  Oh, maybe there's something good there.
*  So I will look at it.
*  And so that's part of the overall information flow
*  in a good market.
*  So advertising has a role.
*  But the problem is of course,
*  that signal is now completely gone
*  because it just, you know, dominated by these tiny
*  little things that add up to big money for the company.
*  You know, so I think it will just,
*  I think it will change because societies just don't,
*  you know, stick with things that annoy a lot of people.
*  Oh, and advertising currently annoys people
*  more than it provides information.
*  And I think that Google probably is smart enough
*  to figure out that this is a dead, this is a bad model,
*  even though it's a hard, huge amount of money
*  and they'll have to figure out how to pull it away from it
*  slowly.
*  And I'm sure the CEO there will figure it out,
*  but they need to do it.
*  And they needed it to,
*  so if you reduce advertising, not to zero,
*  but you reduce it at the same time,
*  you bring up producer, consumer,
*  actual real value being delivered.
*  So real money is being paid and they take a 5% cut,
*  that 5% could start to get big enough to cancel out
*  the lost revenue from the kind of the poor kind
*  of advertising.
*  And I think that a good company will do that,
*  will realize that.
*  And there are, you know, Facebook, you know, again,
*  God bless them.
*  They bring, you know, grandmothers, you know,
*  they bring children's pictures into grandmothers' lives.
*  It's fantastic.
*  But they need to think of a new business model.
*  And that's the core problem there.
*  Until they start to connect producer, consumer,
*  I think they will just continue to make money
*  and then buy the next social network company
*  and then buy the next one.
*  And the innovation level will not be high
*  and the health issues will not go away.
*  So I apologize that we kind of returned to words.
*  I don't think the exact terms matter,
*  but in sort of defense of advertisement,
*  don't you think the kind of direct connection
*  between consumer and creator, producer,
*  is the best, like the,
*  is what advertisement strives to do, right?
*  So that is the best advertisement.
*  It's literally now, Facebook is listening
*  to our conversation and heard that you're going to India
*  and will be able to actually start automatically
*  for you making these connections
*  and start giving this offer.
*  So like, I apologize if it's just a matter of terms,
*  but just to draw a distinction,
*  is it possible to make advertisements just better
*  and better and better algorithmically
*  to where it actually becomes a connection?
*  Almost a direct connection.
*  That's a good question.
*  So let's put on that foot push line.
*  First of all, what we just talked about,
*  I was defending advertising, okay?
*  So I was defending it as a way to get signals
*  into a market that don't come any other way,
*  especially algorithmically.
*  It's a sign that someone spent money on it.
*  It's a sign they think it's valuable.
*  And if I think that if other thinks,
*  someone else thinks it's valuable,
*  then if I trust other people, I might be willing to listen.
*  I don't trust that Facebook though,
*  who's an intermediary between this.
*  I don't think they care about me, okay?
*  I don't think they do.
*  And I find it creepy that they know I'm going to India
*  next week because of our conversation.
*  Why do you think that?
*  So what, could you just put your PR hat on?
*  Why do you think you find Facebook creepy
*  and not trust them as do majority of the population?
*  So they're out of the Silicon Valley companies
*  I saw like, not approval rate,
*  but there's ranking of how much people trust companies
*  and Facebook is in the gutter.
*  In the gutter, including people inside of Facebook.
*  So what do you attribute that to?
*  Because when I-
*  Come on, you don't find it creepy
*  that right now we're talking that I might walk out
*  on the street right now that some unknown person
*  who I don't know kind of comes up to me and says,
*  I hear you going to India.
*  I mean, that's not even Facebook.
*  That's just, I want transparency in human society.
*  I want to have, if you know something about me,
*  there's actually some reason you know something about me.
*  That's something that if I look at it later
*  and audit it kind of, I approve.
*  You know something about me because you care in some way.
*  There's a caring relationship even,
*  or an economic one or something.
*  Not just that you're someone who could exploit it
*  in ways I don't know about or care about
*  or I'm troubled by or whatever.
*  And we're in a world right now
*  where that happens way too much.
*  And that Facebook knows things about a lot of people
*  and could exploit it and does exploit it at times.
*  I think most people do find that creepy.
*  It's not for them.
*  It's not that Facebook does not do it
*  because they care about them in any real sense.
*  And they shouldn't.
*  They should not be a big brother caring about us.
*  That is not the role of a company like that.
*  Why not?
*  Not the big brother part, but the caring, the trusting.
*  I mean, don't those companies, just to linger on it
*  because a lot of companies have a lot of information
*  about us, I would argue that there's companies
*  like Microsoft that has more information about us
*  than Facebook does and yet we trust Microsoft more.
*  Well, Microsoft is pivoting.
*  Microsoft under such an adult has decided
*  this is really important.
*  We don't wanna do creepy things.
*  Really want people to trust us to actually only use
*  information in ways that they really would approve of
*  that we don't decide, right?
*  And I'm just kind of adding that the health of a market
*  is that when I connect to someone who produced or consumer,
*  it's not just a random producer or consumer.
*  It's people who see each other.
*  They don't like each other, but they sense that
*  if they transact, some happiness will go up on both sides.
*  If a company helps me to do that in moments that I choose
*  of my choosing, then fine.
*  So, and also think about the difference between
*  browsing versus buying, right?
*  There are moments in my life, I just wanna buy a gadget
*  or something, I need something for that moment.
*  I need some ammonia for my house or something
*  because I got a problem with a spill.
*  I wanna just go in.
*  I don't wanna be advertised at that moment.
*  I don't wanna be led down various, that's annoying.
*  I want to just go and have it be extremely easy
*  to do what I want.
*  Other moments I might say, no, it's like today
*  I'm going to the shopping mall.
*  I wanna walk around and see things and see people
*  and be exposed to stuff.
*  So I want control over that though.
*  I don't want the company's algorithms to decide for me.
*  Right, and I think that's the thing.
*  It's a total loss of control.
*  If Facebook thinks they should take the control from us
*  of deciding when we want to have certain kinds
*  of information, when we don't, what information that is,
*  how much it relates to what they know about us
*  that we didn't really want them to know about us.
*  They're not, I don't want them to be helping me
*  in that way.
*  I don't want them to be helping them,
*  but they decide, they have control over what I want and when.
*  I totally agree.
*  So Facebook, by the way, I have this optimistic thing
*  where I think Facebook has the kind of personal information
*  about us that could create a beautiful thing.
*  So I'm really optimistic of what Facebook could do.
*  It's not what it's doing, but what it could do.
*  I don't see that.
*  I think that optimism is misplaced
*  because there's not a bit, you have to have a business model
*  behind these things.
*  Create a beautiful thing is really, let's be clear.
*  It's about something that people would value.
*  And I don't think they have that business model.
*  And I don't think they will suddenly discover it
*  by what you know, a long hot shower.
*  I disagree.
*  I disagree in terms of,
*  you can discover a lot of amazing things in a shower.
*  So.
*  I didn't say that.
*  I said they won't come.
*  They won't.
*  They won't do it.
*  But in the shower, I think a lot of other people
*  will discover it.
*  I think that this, so I should also, full disclosure,
*  I think that there's a company called United Masters,
*  which I'm on their board.
*  And they've created this music market.
*  They have a hundred thousand artists now signed on.
*  And they've done things like gone to the NBA.
*  And the NBA, the music you find behind NBA clips right now
*  is their music.
*  That's a company that had the right business model in mind
*  from the get-go, right?
*  Executed on that.
*  And from day one, there was value brought to,
*  so here you have a kid who made some songs
*  who suddenly their songs are on the NBA website, right?
*  And so, you know.
*  And so, you know.
*  And so, you know.
*  So you and I differ on the optimism of being able to
*  sort of change the direction of the Titanic, right?
*  So I.
*  Yeah.
*  I'm older than you.
*  So I think the Titanic's crash.
*  Got it.
*  But just to elaborate, because I totally agree with you.
*  And I just want to know how difficult you think
*  this problem is of, so for example,
*  I want to read some news.
*  There's a lot of times in the day where something
*  makes me either smile or think in a way
*  where I consciously think this really gave me value.
*  Like I sometimes listen to the daily podcast
*  in the New York Times.
*  Way better than the New York Times themselves, by the way,
*  for people listening.
*  That's like real journalism is happening for some reason
*  in the podcast space.
*  It doesn't make sense to me.
*  But often I listen to it 20 minutes.
*  And I would be willing to pay for that, like $5, $10,
*  for that experience.
*  Yeah, absolutely.
*  And how difficult, that's kind of what you're getting at
*  is that little transaction.
*  How difficult is it to create a frictionless system
*  like Uber has, for example, for other things?
*  What's your intuition there?
*  So first of all, I pay little bits of money to, you know,
*  to send, there's something called Quartz
*  that does financial things.
*  I like Medium as a site.
*  I don't pay there, but I would.
*  You had a great post on Medium.
*  I would have loved to pay you a dollar and not others.
*  But I wouldn't have wanted it per se
*  because there should be also sites
*  where that's not actually the goal.
*  The goal is to actually have a broadcast channel
*  that I monetize in some other way if I chose to.
*  I mean, I could now.
*  People know about it.
*  I could, I'm not doing it, but that's fine with me.
*  Also, the musicians who are making all this music,
*  I don't think the right model is that you pay
*  a little subscription fee to them, all right?
*  Because people can copy the bits too easily.
*  And it's just not that, it's not what the value is.
*  The value is that a connection was made
*  between real human beings.
*  And then you can follow up on that, all right?
*  And create yet more value.
*  So no, I think...
*  So there's a lot of open questions here.
*  A lot of open questions, but also, yeah,
*  I do want good recommendation systems
*  that recommend cool stuff to me, but it's pretty hard, right?
*  I don't like them to recommend stuff
*  just based on my browsing history.
*  I don't like them to base on stuff
*  they know about me, quote unquote.
*  What's unknown about me is the most interesting.
*  So this is the really interesting question.
*  We may disagree, maybe not.
*  That I love recommender systems
*  and I wanna give them everything about me
*  in a way that I trust.
*  Yeah, but you don't.
*  Because so for example, this morning I clicked on,
*  I was pretty sleepy this morning.
*  I clicked on a story about the Queen of England, right?
*  I do not give a damn about the Queen of England.
*  I really do not.
*  But it was click-bait.
*  It kinda looked funny.
*  And I had to say, what the heck are they talking about?
*  I don't wanna have my life heading that direction.
*  Now that's in my browsing history.
*  The system and any reasonable system will think
*  that I care about my Queen of England.
*  That's browsing history.
*  Right, but you're saying all the trace,
*  all the digital exhaust or whatever,
*  that's been kind of the models.
*  If you collect all this stuff,
*  you're gonna figure all of us out.
*  Well, if you're trying to figure out like kind of one person,
*  like Trump or something, maybe you could figure him out.
*  But if you're trying to figure out 500 million people,
*  no way, no way.
*  You think so?
*  No, I think so.
*  I think we are, humans are just amazingly rich
*  and complicated.
*  Every one of us has our little quirks.
*  Every one of us has our little things
*  that could intrigue us that we don't even know
*  and will intrigue us.
*  And there's no sign of it in our past,
*  but by God, there it comes.
*  And you fall in love with it.
*  And I don't want a company trying to figure that out for me
*  and anticipate that.
*  I want them to provide a forum, a market,
*  a place that I kind of go and by hook or by crook,
*  this happens.
*  I'm walking down the street
*  and I hear some Chilean music being played.
*  And I never knew I liked Chilean music.
*  Wow, so there is that side.
*  And I want them to provide a limited,
*  but interesting place to go.
*  And so don't try to use your AI to kind of figure me out
*  and then put me in a world where you figured me out.
*  No, create huge spaces for human beings
*  where our creativity and our style will be enriched
*  and come forward.
*  And it'll be a lot of more transparency.
*  I won't have people randomly, anonymously,
*  putting comments up.
*  And I'll special based on stuff they know about me,
*  facts that we are so broken right now,
*  especially if you're a celebrity.
*  And I don't want anybody that,
*  anonymous people are hurting lots and lots of people
*  right now.
*  And that's part of this thing that Silicon Valley
*  is thinking that, you know,
*  just collect all this information and use it in a great way.
*  So no, I'm not a pessimist.
*  I'm very much an optimist by nature,
*  but I think that's just been the wrong path
*  for the whole technology to take.
*  Be more limited, create, let humans rise up.
*  Don't try to replace them.
*  That's the AI mantra.
*  Don't try to anticipate them.
*  Don't try to predict them.
*  Because you're not gonna be able to do those things.
*  You're gonna make things worse.
*  Okay, so right now, just give this a chance.
*  Right now, the recommender systems
*  are the creepy people in the shadow
*  watching your every move.
*  So they're looking at traces of you.
*  They're not directly interacting with you.
*  Sort of your close friends and family,
*  the way they know you is by having conversation,
*  by actually having interactions back and forth.
*  Do you think there's a place for recommender systems
*  sort of to step, because you just emphasized
*  the value of human to human connection.
*  But just give it a chance, AI, human connection.
*  Is there a role for an AI system
*  to have conversations with you in terms of,
*  to try to figure out what kind of music you like,
*  not by just watching what you listen to,
*  but actually having a conversation,
*  natural language or otherwise?
*  Yeah, no, so I'm not against it.
*  I just wanted to push back against the,
*  maybe you're saying you have options for Facebook.
*  So there, I think it's misplaced.
*  I think that distributing-
*  I'm the one guy defending Facebook.
*  Yeah, no, so good for you.
*  Go for it.
*  That's a hard spot to be.
*  Yeah, no, good.
*  Human interaction, like on our daily,
*  the context around me in my own home
*  is something that I don't want some big company
*  to know about at all.
*  But I would be more than happy
*  to have technology help me with it.
*  Which kind of technology?
*  Well, you know, just-
*  Alexa, Amazon.
*  Well, a good, Alexa's done right.
*  I think Alexa's a research platform right now
*  more than anything else.
*  But Alexa done right, you know, could do things like,
*  I leave the water running in my garden
*  and I say, hey, Alexa, the water's running in my garden.
*  And even have Alexa figure out that that means
*  when my wife comes home that she should be told about that.
*  That's a little bit of a reasoning.
*  I would call that AI and by any kind of stretch,
*  it's a little bit of reasoning.
*  And it actually kind of would make my life
*  a little easier and better.
*  And, you know, I wouldn't call this a wow moment,
*  but I kind of think that overall rises human happiness up
*  to have that kind of thing.
*  But not when you're lonely.
*  Alexa knowing loneliness-
*  No, no, I don't want Alexa to be feeling intrusive
*  and I don't want just the designer of the system
*  to kind of work all this out.
*  I really want to have a lot of control
*  and I want transparency and control.
*  And if a company can stand up and give me that
*  in the context of new technology,
*  I think they're gonna, first of all,
*  be way more successful than our current generation.
*  And like I said, I was mentioning Microsoft,
*  I really think they're pivoting
*  to kind of be the trusted old uncle.
*  But, you know, I think that they get
*  that this is a way to go.
*  That if you let people find technology empowers them
*  to have more control and have control,
*  not just over privacy,
*  but over this rich set of interactions,
*  that people are gonna like that a lot more.
*  And that's the right business model going forward.
*  What does control over privacy look like?
*  Do you think you should be able to just view all the data?
*  No, it's much more than that.
*  I mean, first of all, it should be an individual decision.
*  Some people don't want privacy.
*  They want their whole life out there.
*  Other people's want it.
*  Privacy is not a zero one.
*  It's not a legal thing.
*  It's not just about which data is available
*  and which is not.
*  I like to recall to people that, you know,
*  a couple hundred years ago,
*  there was not really big cities.
*  Everyone lived in the countryside and villages.
*  And in villages, everybody knew everything about you.
*  You didn't have any privacy.
*  Is that bad?
*  Are we better off now?
*  Well, you know, arguably no,
*  because what did you get for that loss
*  of certain kinds of privacy?
*  Well, people helped each other.
*  Because they know everything about you.
*  They know something bad's happening.
*  They will help you with that, right?
*  And now you live in a big city, no one knows the amount.
*  You get no help.
*  So it kind of depends, the answer.
*  I want certain people who I trust
*  and there should be relationships.
*  I should kind of manage all those.
*  But who knows what about me?
*  I should have some agency there.
*  I shouldn't just be adrift in a sea of technology
*  where I have no agency.
*  I don't want to go reading things and checking boxes.
*  So I don't know how to do this.
*  I'm not a privacy researcher per se.
*  I recognize the vast complexity of this.
*  It's not just technology.
*  It's not just legal scholars meeting technologists.
*  There's got to be kind of whole layers around it.
*  And so when I alluded to this emerging engineering field,
*  this is a big part of it.
*  When electrical engineering came,
*  I wasn't around at the time,
*  but you just didn't plug electricity into walls
*  and all kind of worked.
*  I had to have like underwriter's laboratory
*  that reassured you that that plug's not going to burn
*  up your house and that that machine will do this and that
*  and everything.
*  There'll be whole people who can install things.
*  There'll be people who can watch the installers.
*  There'll be a whole layers,
*  whole onion of these kinds of things.
*  And for things as deep and interesting as privacy,
*  which is as least as interesting as electricity,
*  that's going to take decades to kind of work out,
*  but it's going to require a lot of new structures
*  that we don't have right now.
*  So it's kind of hard to talk about it.
*  And you're saying there's a lot of money to be made
*  if you get it right.
*  So a lot of money to be made.
*  And all these things that provide human services
*  and people recognize them as useful parts of their lives.
*  So yeah, the dialect sometimes goes
*  from the exuberant technologists to the no technology
*  is good kind of.
*  And that's in our public discourse,
*  and in this verse you see too much of this kind of thing.
*  And the sober discussions in the middle,
*  which are the challenging ones to have
*  or where we need to be having our conversations.
*  And actually there's not many forum for those.
*  That's kind of what I would look for.
*  Maybe I could go and I could read a comment section
*  of something and it would actually be this kind of dialogue
*  going back and forth.
*  You don't see much of this, right?
*  Which is why actually there's a resurgence of podcasts
*  out of all because people are really hungry
*  for conversation.
*  But there's technology is not helping much.
*  So comment sections of anything including YouTube
*  is not hurting and not helping.
*  And you think technically speaking it's possible to help.
*  I don't know the answers, but it's a less anonymity,
*  a little more locality, you know,
*  and you kind of enter in and you trust the people
*  there in those worlds so that when you start
*  having a discussion, you know,
*  not only is that people not gonna hurt you,
*  but it's not gonna be a total waste of your time
*  because there's a lot of wasting of time that,
*  you know, a lot of us, I pulled out of Facebook early on
*  because it was clearly gonna waste a lot of my time,
*  even though there was some value.
*  And so yeah, worlds that are somehow you enter in
*  and you know what you're getting
*  and it's kind of appeals to you.
*  New things might happen,
*  but you kind of have some trust in that world.
*  And there's some deep, interesting, complex
*  psychological aspects around anonymity,
*  how that changes human behavior that's quite dark.
*  Quite dark, yeah.
*  I think a lot of us are, especially those of us
*  who really love the advent of technology.
*  I loved social networks when they came out.
*  I was just, I didn't see any negatives there at all.
*  But then I started seeing comment sections,
*  I think it was maybe, you know,
*  one of the CNN or something.
*  And I started to go, wow, this darkness,
*  I just did not know about.
*  And our technology is now amplifying it.
*  Sorry for the big philosophical question,
*  but on that topic, do you think human beings,
*  because you've also, out of all things,
*  had a foot in psychology too,
*  do you think human beings are fundamentally good?
*  Like all of us have good intent that could be mined
*  or is it depending on context and environment,
*  everybody could be evil?
*  So my answer is fundamentally good,
*  but fundamentally limited.
*  All of us have very blinkers on.
*  We don't see the other person's pain that easily.
*  We don't see the other person's point of view that easily.
*  We're very much in our own head, in our own world.
*  And on my good days, I think that technology
*  could open us up to more perspectives
*  and more less blinkered and more understanding.
*  You know, a lot of wars in human history happened
*  because of just ignorance.
*  They didn't, they thought the other person was doing this,
*  well, the other person wasn't doing this,
*  and we have huge amounts of that.
*  But in my lifetime, I've not seen technology
*  really help in that way yet.
*  And I do believe in that.
*  No, I think fundamentally humans are good.
*  People suffer, people have grievances,
*  people have grudges, and those things cause them
*  to do things they probably wouldn't want.
*  They regret it often.
*  So no, I think it's a, you know,
*  part of the progress of technology is to indeed allow it
*  to be a little easier to be the real good person
*  you actually are.
*  Well put.
*  Do you think individual human life or society
*  could be modeled as an optimization problem?
*  Not the way I think, typically.
*  I mean, that's, you're talking about one of the most
*  complex phenomena in the whole, you know, in all of the
*  universe.
*  Which, individual human life or society as a whole?
*  Both, both.
*  I mean, individual human life is amazingly complex.
*  And so, you know, optimization is kind of just one
*  branch of mathematics that talks about certain kind
*  of things, and it just feels way too limited
*  for the complexity of such things.
*  What properties of optimization problems,
*  do you think most interesting problems
*  that could be solved through optimization?
*  What kind of properties does that surface have?
*  Non-convexity, convexity, linearity, all those kinds
*  of things, saddle points.
*  Well so optimization is just one piece of mathematics.
*  You know, there's like, even in our era we're aware
*  that say sampling is coming up examples of something.
*  Coming up with a distribution.
*  What's optimization, what's sampling?
*  Well, you can, if you're a kind of, a certain kind
*  of mathematician, you can try to blend them and make them
*  seem to be sort of the same thing.
*  But optimization is roughly speaking trying to find a point
*  that, a single point that is the optimum of a criterion
*  function of some kind.
*  And sampling is trying to, from that same surface,
*  treat that as a distribution or density and find points
*  that have high density.
*  So I want the entire distribution in a sampling paradigm,
*  and I want the, you know, the single point that's the best
*  point in the optimization paradigm.
*  Now if you were optimizing in the space of probability
*  measures, the output of that could be a whole probability
*  distribution, so you can start to make these things
*  the same, but in mathematics if you go too high up that kind
*  of abstraction arc, you start to lose the, you know,
*  the ability to do the interesting theorems,
*  so you kind of don't try to, you don't try to overly,
*  over abstract.
*  So as a small tangent, what kind of world view do you find
*  more appealing, one that is deterministic or stochastic?
*  Well that's easy, I mean I'm a statistician, you know,
*  the world is highly stochastic, I don't know what's gonna
*  happen in the next five minutes, right?
*  What you're gonna ask, what we're gonna do,
*  what I'll say.
*  Due to the uncertainty.
*  Due to the.
*  Massive uncertainty, you know, massive uncertainty.
*  And so the best I can do is have come rough sense
*  or probability distribution on things and somehow use that
*  in my reasoning about what to do now.
*  So how does the distributed at scale when you have
*  multi-agent systems look like, so optimization can optimize
*  sort of, it makes a lot more sense, sort of, at least
*  from my robotics perspective, for a single robot,
*  for a single agent trying to optimize some objective
*  function, when you start to enter the real world,
*  this game theoretic concept starts popping up.
*  That, how do you see optimization in this,
*  because you've talked about markets in a scale,
*  what does that look like?
*  Do you see it as optimization?
*  Do you see it as sampling?
*  Do you see, like how should you.
*  These all blend together and a system designer thinking
*  about how to build an incentivized system will have a blend
*  of all these things.
*  So, you know, a particle in a potential well is optimizing
*  a functional called a Lagrangian, right?
*  The particle doesn't know that.
*  There's no algorithm running that does that.
*  It just happens.
*  It's a description mathematically of something that helps
*  us understand as analysts what's happening, right?
*  And so the same will happen when we talk about, you know,
*  mixtures of humans and computers and markets and so on
*  and so forth, there'll be certain principles that allow us
*  to understand what's happening and whether or not the actual
*  algorithms are being used by any sense is not clear.
*  Now, at some point I may have set up a multi-agent
*  or market kind of system and I'm now thinking about
*  an individual agent in that system and they're asked
*  to do some task and they're incentivized in some way.
*  They get certain signals and they have some utility.
*  Maybe what they will do at that point is they just won't
*  know the answer.
*  They may have to optimize to find an answer.
*  Okay, so an outage could be embedded inside
*  of an overall market.
*  You know, and game theory is very, very broad.
*  It is often studied very narrowly
*  for certain kinds of problems, but it's roughly speaking
*  that it's just the, I don't know what you're gonna do
*  so I kind of anticipate that a little bit
*  and you anticipate what I'm anticipating
*  and we kind of go back and forth in our own minds.
*  We run kind of thought experiments.
*  You've talked about this interesting point
*  in terms of game theory.
*  You know, most optimization problems
*  really hate saddle points.
*  Maybe you can describe what saddle points are,
*  but I've heard you kind of mention that there's a branch
*  of optimization that you could try to explicitly look
*  for saddle points as a good thing.
*  Oh, not optimization, that's just game theory.
*  That's so, there's all kinds of different equilibrium
*  game theory and some of them are highly explanatory
*  behavior, they're not attempting to be algorithmic.
*  They're just trying to say, if you happen to be
*  at this equilibrium, you would see certain kind of behavior
*  and we see that in real life.
*  That's what an economist wants to do,
*  especially a behavioral economist.
*  In continuous differential game theory,
*  you're in continuous spaces, some of the simplest
*  equilibria are saddle points.
*  A Nash equilibrium is a saddle point.
*  It's a special kind of saddle point.
*  So classically in game theory, you are trying
*  to find Nash equilibrium and algorithmic game theory,
*  you're trying to find algorithms that would find them.
*  So you're trying to find saddle points.
*  So that's literally what you're trying to do.
*  But any economist knows that Nash equilibria
*  have their limitations.
*  They are definitely not that explanatory in many situations.
*  They're not what you really want.
*  There's other kind of equilibria and there's names
*  associated with these because they came from history
*  with certain people working on them,
*  but there will be new ones emerging.
*  So one example is a Stackelberg equilibrium.
*  So Nash, you and I are both playing this game
*  against each other or for each other.
*  Maybe it's cooperative and we're both gonna think it through
*  then we're gonna decide and we're gonna do our thing
*  simultaneously.
*  In a Stackelberg, no, I'm gonna be the first mover.
*  I'm gonna make a move, you're gonna look at my move
*  and then you're gonna make yours.
*  Now, since I know you're gonna look at my move,
*  I anticipate what you're gonna do
*  and so I don't do something stupid.
*  But then I know that you are also anticipating me
*  so we're kind of going back in some form of mind,
*  but there is then a first mover thing.
*  And so there's a different equilibria.
*  And so just mathematically, yeah,
*  these things have certain topologies, certain shapes
*  that are like salivary, algorithmically or dynamically,
*  how do you move towards them?
*  How do you move away from things?
*  So some of these questions have answers,
*  they've been studied, others do not,
*  and especially if it becomes stochastic,
*  especially if there's large numbers of decentralized things,
*  there's just young people getting in this field
*  who kind of think it's all done
*  because we have TensorFlow.
*  Well, no, these are all open problems
*  and they're really important and interesting
*  and it's about strategic settings.
*  How do I collect data?
*  Suppose I don't know what you're gonna do
*  because I don't know you very well, right?
*  Well, I gotta collect data about you
*  so maybe I wanna push you in a part of the space
*  where I don't know much about you so I can get data
*  and then later I'll realize that you'll never go there
*  because of the way the game is set up.
*  But that's part of the overall data analysis context.
*  Yeah, even the game of poker is fascinating space.
*  Whenever there's any uncertainty or lack of information,
*  it's a super exciting space.
*  Yeah.
*  Just linger on optimization for a second.
*  So when we look at deep learning,
*  it's essentially minimization
*  of a complicated loss function.
*  So is there something insightful or hopeful
*  that you see in the kinds of function surface
*  that loss functions,
*  that deep learning in the real world
*  is trying to optimize over?
*  Is there something interesting?
*  Is it just the usual kind of problems of optimization?
*  I think from an optimization point of view,
*  that surface first of all, it's pretty smooth.
*  And secondly, if it's over parameterized,
*  there's kind of lots of paths down to reasonable optima.
*  And so kind of the getting downhill to an optimum
*  is viewed as not as hard as you might have expected
*  in high dimensions.
*  The fact that some optima tend to be really good ones
*  and others not so good and you tend to,
*  sometimes you find the good ones
*  is sort of still needs explanation.
*  Yes, that's a total mystery.
*  But the particular surface is coming
*  from the particular generation of neural nets,
*  I kind of suspect those will change.
*  In 10 years, it will not be exactly those surfaces,
*  there'll be some others that are,
*  and optimization theory will help contribute
*  to why other surfaces or why other algorithms.
*  Layers of arithmetic operations
*  with a little bit of non-linearity,
*  that didn't come from neuroscience personally.
*  I mean, maybe in the minds of some of the people
*  working on it, they were thinking even about brains,
*  but they were arithmetic circuits in all kinds of fields,
*  computer science control theory and so on.
*  And that layers of these could transform things
*  in certain ways and that if it's smooth,
*  maybe you could find parameter values.
*  It's a big discovery that it's able to work at this scale.
*  But I don't think that we're stuck with that
*  and we're certainly not stuck with that
*  because we're understanding the brain.
*  So in terms of on the algorithm side,
*  sort of gradient descent,
*  do you think we're stuck with gradient descent
*  as variants of it?
*  What variants do you find interesting
*  or do you think there'll be something else invented
*  that is able to walk all over these optimization spaces
*  in more interesting ways?
*  So there's a co-design of the surface
*  and there are the architecture and the algorithm.
*  So if you just ask, if we stay with the kind
*  of architectures that we have now, not just neural nets,
*  but phase retrieval architectures
*  or matrix completion architectures and so on.
*  I think we've kind of come to a place where,
*  yeah, a stochastic gradient algorithms are dominant
*  and there are versions that are a little better than others.
*  They have more guarantees, they're more robust and so on.
*  And there's ongoing research to kind of figure out
*  which is the best time for which situation.
*  But I think that that'll start to co-evolve,
*  that that'll put pressure on the actual architecture.
*  And so we shouldn't do it in this particular way.
*  We should do it in a different way
*  because there's other algorithms now available
*  if you do it in a different way.
*  So that I can't really anticipate that co-evolution process.
*  But gradients are amazing mathematical objects.
*  They have a lot of people who start to study them
*  more deeply mathematically are kind of shocked
*  about what they are and what they can do.
*  I mean, think about it this way.
*  Suppose that I tell you, if you move along the x-axis,
*  you get, you go uphill in some objective by three units.
*  Whereas if you move along the y-axis,
*  you go uphill by seven units.
*  Now I'm gonna only allow you to move a certain unit distance.
*  What are you gonna do?
*  Well, most people will say, I'm gonna go along the y-axis.
*  I'm getting the biggest bang for my buck.
*  And my buck is only one unit.
*  So I'm gonna put all of it in the y-axis.
*  And why should I even take any of my strength,
*  my step size and put any of it in the x-axis
*  because I'm getting less bang for my buck.
*  That seems like a completely clear argument and it's wrong
*  because the gradient direction is not to go along the y-axis.
*  It's to take a little bit of the x-axis.
*  And to understand that, you have to know some math.
*  And so even a trivial so-called operator-like gradient
*  is not trivial and so exploiting its properties
*  is still very, very important.
*  Now we know that just pervading descent
*  has got all kinds of problems.
*  It gets stuck in many ways and it had never,
*  good dimension dependence and so on.
*  So my own line of work recently has been about
*  what kinds of stochasticity,
*  how can we get dimension dependence,
*  how can we do the theory of that.
*  And we've come up pretty favorable results
*  with certain kinds of stochasticity.
*  We have sufficient conditions generally.
*  We know if you do this, we will give you a good guarantee.
*  We don't have necessary conditions
*  that it must be done a certain way in general.
*  So stochasticity, how much randomness to inject
*  into the walking along the gradient.
*  And what kind of randomness?
*  Why is randomness good in this process?
*  Why is stochasticity good?
*  Yeah, so I can give you simple answers,
*  but in some sense again, it's kind of amazing.
*  Stochasticity just, you know, particular features
*  of a surface that could have hurt you
*  if you were doing one thing deterministically,
*  it won't hurt you because, you know, by chance,
*  you know, there's very little chance that you would get hurt.
*  And, you know, so here stochasticity, you know,
*  it just kind of saves you from some of the particular
*  features of surfaces that, you know,
*  and in fact, if you think about, you know,
*  surfaces that are discontinuous in a first derivative,
*  like, you know, absolute value function,
*  you will go down and hit that point
*  where there's non-differentiability, right?
*  And if you're running a deterministic algorithm,
*  at that point, you can really do something bad, right?
*  Whereas stochasticity just means it's pretty unlikely
*  that's gonna happen, that you're gonna hit that point.
*  So, you know, it's again, not trivial to analyze,
*  but especially in higher dimensions,
*  also stochasticity, our intuition isn't very good about it,
*  but it has properties that kind of are very appealing
*  in high dimensions for kind of law of large number of reasons.
*  So it's all part of the mathematics,
*  it's what's fun to work in the field
*  is that you get to try to understand this mathematics.
*  But long story short, you know,
*  partly empirically it was discovered
*  stochastic gradient is very effective
*  and theory kind of followed, I'd say, that.
*  But I don't see that we're getting clearly out of that.
*  What's the most beautiful, mysterious,
*  or profound idea to you in optimization?
*  I don't know the most, but let me just say that,
*  you know, Nesterov's work on Nesterov acceleration to me
*  is pretty surprising and pretty deep.
*  Can you elaborate?
*  Well, Nesterov acceleration is just that,
*  suppose that we are gonna use gradients
*  to move around into space for the reasons I've alluded to,
*  they're nice directions to move.
*  And suppose that I tell you
*  that you're only allowed to use gradients.
*  You're not gonna be allowed to,
*  you know, see this local person,
*  it can only sense kind of the change in the surface.
*  But I'm gonna give you kind of a computer
*  that's able to store all your previous gradients.
*  And so you start to learn something about the surface.
*  And I'm gonna restrict you to maybe move in the direction
*  of like linear span of all the gradients.
*  So you can't kind of just move
*  in some arbitrary direction, right?
*  So now we have a well-defined mathematical complexity model.
*  There's a certain classes of algorithms that can do that
*  and others that can't.
*  And we can ask for certain kinds of surfaces,
*  how fast can you get down to the optimum?
*  So there's an answers to these.
*  So for a, you know, a smooth convex function,
*  there's an answer,
*  which is one over the number of steps squared.
*  You will be within a ball of that size after K steps.
*  Gradient descent in particular has a slower rate,
*  it's one over K, okay?
*  So you could ask is gradient descent,
*  actually even though we know it's a good algorithm,
*  is it the best algorithm?
*  And the answer is no.
*  Well, not clear yet because what one over K score
*  is a lower bound.
*  That's probably the best you can do.
*  What gradient is one over K,
*  but is there something better?
*  And so I think it's a surprise to most,
*  though Nesterov discovered a new algorithm
*  that has got two pieces to it.
*  It uses two gradients.
*  And puts those together in a certain kind of obscure way.
*  And the thing doesn't even move downhill all the time.
*  It sometimes goes back uphill.
*  And if you're a physicist, that kind of makes some sense.
*  You're building up some momentum.
*  And that is kind of the right intuition,
*  but that intuition is not enough to understand
*  kind of how to do it and why it works.
*  But it does.
*  It achieves one over K squared,
*  and it has a mathematical structure.
*  And it's still kind of, to this day,
*  a lot of us are writing papers
*  and trying to explore that and understand it.
*  So there are lots of cool ideas in optimization,
*  but just kind of using gradients, I think, is number one.
*  That goes back 150 years.
*  And then Nesterov, I think,
*  has made a major contribution with this idea.
*  So like you said, gradients themselves
*  are in some sense mysterious.
*  They're not as trivial as mathematically speaking.
*  Coordinate descent is more of a trivial
*  when you just pick one of the coordinates
*  and build another one. That's how we think.
*  That's how our human minds think.
*  That's how our human minds think.
*  And gradients are not that easy
*  for our human mind to grapple with.
*  An absurd question, but what is statistics?
*  So here it's a little bit,
*  it's somewhere between math and science and technology.
*  It's somewhere in that convex hole.
*  So it's a set of principles that allow you
*  to make inferences that have got some reason to be believed.
*  And also principles allow you to make decisions
*  where you can have some reason to believe
*  you're not gonna make errors.
*  So all of that requires some assumptions
*  about what do you mean by an error?
*  What do you mean by the probabilities?
*  But after you start making some of those assumptions,
*  you're led to conclusions that,
*  yes, I can guarantee that if you do this in this way,
*  your probability of making error will be small.
*  Your probability of continuing to not make errors
*  over time will be small.
*  And probability you found something that's real
*  will be high.
*  So decision making is a big part of that.
*  Decision making is a big part, yeah.
*  So the original, so statistics,
*  short history was that it sort of goes back
*  as a formal discipline, 250 years or so.
*  It was called inverse probability
*  because around that era,
*  probability was developed sort of especially
*  to explain gambling situations.
*  Of course.
*  And-
*  Interesting.
*  So you would say, well, given the state of nature is this,
*  there's a certain roulette board
*  that has a certain mechanism in it.
*  What kind of outcomes do I expect to see?
*  And especially if I do things long amounts of time,
*  what outcomes will I see?
*  And the physicists started to pay attention to this.
*  And then people said, well, given,
*  let's turn the problem around.
*  What if I saw certain outcomes,
*  could I infer what the underlying mechanism was?
*  That's an inverse problem.
*  And in fact, for quite a while,
*  statistics was called inverse probability.
*  That was the name of the field.
*  And I believe that it was Laplace
*  who was working in Napoleon's government,
*  who needed to do a census of France,
*  learn about the people there.
*  So he went and gathered data
*  and he analyzed that data to determine policy
*  and said, well, let's call this field
*  that does this kind of thing statistics.
*  Cause the word state is in there.
*  In French, that's etah,
*  but it's the study of data for the state.
*  So anyway, that caught on
*  and it's been called statistics ever since.
*  But by the time it got formalized,
*  it was sort of in the thirties.
*  And around that time,
*  there was game theory and decision theory developed nearby.
*  People in that era didn't think of themselves
*  as either computer science or statistics
*  or control or econ.
*  They were all the above.
*  And so, von Neumann is developing game theory,
*  but also thinking of that as decision theory.
*  Wald is an econometrician developing decision theory
*  and then turn that into statistics.
*  And so it's all about,
*  here's not just data and you analyze it.
*  Here's a loss function.
*  Here's what you care about.
*  Here's the question you're trying to ask.
*  Here is a probability model
*  and here's the risk you will face
*  if you make certain decisions.
*  And to this day,
*  in most advanced statistical curricula,
*  you teach decision theory as the starting point.
*  And then it branches out
*  into the two branches of Bayesian and frequentist.
*  But that's, it's all about decisions.
*  In statistics, what is the most beautiful, mysterious,
*  maybe surprising idea that you've come across?
*  Yeah, good question.
*  I mean, there's a bunch of surprising ones.
*  There's something that's way too technical for this thing,
*  but something called James Stein estimation,
*  which is kind of surprising
*  and really takes time to wrap your head around.
*  Can you try to maybe?
*  I think I don't want to even want to try.
*  Let me just say a colleague at a Steven Stickler
*  at University of Chicago wrote a really beautiful paper
*  on James Stein estimation, which is helps to,
*  it's views a paradox.
*  It kind of defeats the mind's attempts to understand it,
*  but you can, and Steve has a nice perspective on that.
*  So one of the troubles with statistics
*  is that it's like in physics, or in quantum physics,
*  you have multiple interpretations.
*  There's a wave and particle duality in physics.
*  And you get used to that over time,
*  but it still kind of haunts you
*  that you don't really quite understand the relationship.
*  The electron's a wave and the electron's a particle.
*  Well, the same thing happens here.
*  There's Bayesian ways of thinking and frequentist,
*  and they are different.
*  They sometimes become sort of the same in practice,
*  but they are physically different.
*  And then in some practice, they are not the same at all.
*  They give you rather different answers.
*  And so it is very much like wave and particle duality,
*  and that is something you have to kind of
*  get used to in the field.
*  Can you define Bayesian and frequentist?
*  Yeah, in decision theory, you can make,
*  I have a video that people could see.
*  It's called, are you a Bayesian or a frequentist?
*  And kind of help try to make it really clear.
*  It comes from decision theory.
*  So, decision theory, you're talking about loss functions,
*  which are a function of data X and parameter theta.
*  So they're a function of two arguments, okay?
*  Neither one of those arguments is known.
*  You don't know the data a priori, it's random,
*  and the parameter's unknown, all right?
*  So you have this function of two things you don't know,
*  and you're trying to say, I want that function to be small.
*  I want small loss, right?
*  Well, what are you gonna do?
*  So you sort of say, well, I'm gonna average
*  over these quantities or maximize over them or something
*  so that I turn that uncertainty into something certain.
*  So you could look at the first argument and average over it,
*  or you could look at the second argument and average over it.
*  That's Bayesian and frequentist.
*  So the frequentist says, I'm gonna look at the X, the data,
*  and I'm gonna take that as random,
*  and I'm gonna average over the distribution.
*  So I take the expectational loss under X.
*  Theta's held fixed, all right?
*  That's called the risk.
*  And so it's looking at all the data sets you could get,
*  all right, and saying how well will a certain procedure
*  do under all those data sets?
*  That's called a frequentist guarantee, all right?
*  So I think it is very appropriate
*  when you're building a piece of software
*  and you're shipping it out there,
*  and people are gonna use it on all kinds of data sets.
*  You wanna have a stamp, a guarantee on it
*  that as people run it on many, many data sets
*  that you never even thought about,
*  that 95% of the time it will do the right thing.
*  Perfectly reasonable.
*  The Bayesian perspective says, well, no,
*  I'm gonna look at the other argument of the loss function,
*  the theta part, okay?
*  That's unknown, and I'm uncertain about it.
*  So I could have my own personal probability for what it is.
*  How many tall people are there out there?
*  I'm trying to infer the average height of the population.
*  Well, I have an idea roughly what the height is.
*  So I'm gonna average over the theta.
*  So now that loss function has only now, again,
*  one argument's gone.
*  Now it's a function of X.
*  And that's what a Bayesian does is they say,
*  well, let's just focus on the particular X we got,
*  the data set we got.
*  We condition on that.
*  Condition on the X, I say something about my loss.
*  That's a Bayesian approach to things.
*  And the Bayesian will argue that it's not relevant
*  to look at all the other data sets you could have gotten
*  and average over them, the frequentist approach.
*  It's really only the data sets you got, all right?
*  And I do agree with that, especially in situations
*  where you're working with a scientist,
*  you can learn a lot about the domain
*  and you're really only focused on certain kinds of data
*  and you gathered your data and you make inferences.
*  I don't agree with it though, in the sense that
*  there are needs for frequentist guarantees.
*  You're writing software, people are using it out there,
*  you wanna say something.
*  So these two things have to got to fight each other
*  a little bit, but they have to blend.
*  So long story short, there's a set of ideas
*  that are right in the middle,
*  they're called empirical Bayes.
*  And empirical Bayes sort of starts with the Bayesian framework.
*  It's kind of arguably philosophically more reasonable
*  in kosher, write down a bunch of the math
*  that kind of flows from that and then realize
*  there's a bunch of things you don't know
*  because it's the real world and you don't know everything.
*  So you're uncertain about certain quantities.
*  At that point ask, is there a reasonable way to plug in
*  an estimate for those things?
*  Okay, and in some cases, there's quite a reasonable thing
*  to do, to plug in.
*  There's a natural thing you can observe in the world
*  that you can plug in and then do a little bit more mathematics
*  and assure yourself it's really good.
*  So based on math or based on human expertise,
*  what are good?
*  They're both going in.
*  The Bayesian framework allows you to put
*  a lot of human expertise in,
*  but the math kind of guides you along that path
*  and then kind of reassures you at the end
*  you could put that stamp of approval.
*  Under certain assumptions, this thing will work.
*  So you asked the question, what's my favorite,
*  what's the most surprising nice idea?
*  So one that is more accessible
*  is something called false discovery rate,
*  which is you're making not just one hypothesis test
*  but you're making one decision,
*  you're making a whole bag of them.
*  And in that bag of decisions,
*  you look at the ones where you made a discovery,
*  you announced that something interesting had happened.
*  All right, that's gonna be some subset of your big bag.
*  In the ones you made a discovery,
*  which subset of those are bad?
*  There are false discoveries.
*  You'd like the fraction of your false discoveries
*  among your discoveries to be small.
*  That's a different criterion than accuracy or precision
*  or recall or sensitivity and specificity.
*  It's a different quantity.
*  Those latter ones are almost all of them
*  have more of a frequentist flavor.
*  They say, given the truth is that the null hypothesis is true,
*  here's what accuracy I would get.
*  Or given that the alternative is true,
*  here's what I would get.
*  So it's kind of going forward
*  from the state of nature to the data.
*  The Bayesian goes the other direction
*  from the data back to the state of nature.
*  And that's actually what false discovery rate is.
*  It says, given you made a discovery,
*  okay, that's conditioned on your data,
*  what's the probability of the hypothesis?
*  It's going the other direction.
*  And so the classical frequency look at that,
*  so I can't know that there's some priors needed in that.
*  And the empirical Bayesian goes ahead and plows forward
*  and starts writing down these formulas
*  and realizes at some point,
*  some of those things can actually be estimated
*  in a reasonable way.
*  And so it's a beautiful set of ideas.
*  So this kind of line of argument has come out.
*  It's not certainly mine,
*  but it sort of came out from Robbins around 1960,
*  and I think that Efron has written beautifully about this
*  in various papers and books.
*  And the FDR is, you know, Benyamini in Israel,
*  John Storey did this Bayesian interpretation and so on.
*  So I've just absorbed these things over the years
*  and find it a very healthy way to think about statistics.
*  Let me ask you about intelligence,
*  to jump slightly back out into philosophy perhaps.
*  Maybe you can elaborate,
*  but you said that defining just even the question
*  of what is intelligence is a very difficult question.
*  Is that a useful question?
*  Do you think we'll one day understand
*  the fundamentals of human intelligence and what it means,
*  you know, have good benchmarks for general intelligence
*  that we put before our machines?
*  So I don't work on these topics so much.
*  You're really asking the question for a psychologist,
*  and I've studied some, but I don't consider myself,
*  at least an expert at this point.
*  You know, a psychologist aims
*  to understand human intelligence, right?
*  And I think many of the psychologists I know
*  are fairly humble about this.
*  They might try to understand how a baby understands,
*  you know, whether something's a solid or a liquid
*  or whether something's hidden or not,
*  and maybe how a child starts to learn
*  the meaning of certain words, what's a verb,
*  what's a noun, and also, you know,
*  slowly but surely trying to figure out things.
*  But humans' ability to take a really complicated environment,
*  reason about it, abstract about it,
*  find the right abstractions, communicate about it,
*  interact and so on is just, you know,
*  really staggeringly rich and complicated.
*  And so, you know, I think in all humility,
*  we don't think we're kind of aiming for that
*  in the near future.
*  A certain psychologist doing experiments with babies
*  in the lab or with people talking
*  has a much more limited aspiration.
*  And, you know, Kahneman and Dversky
*  would look at our reasoning patterns,
*  and they're not deeply understanding
*  how we do our reasoning, but they're sort of saying,
*  hey, here's some oddities about the reasoning
*  and some things you need to think about it.
*  But also, as I emphasize some things I've been writing about,
*  you know, AI, the revolution hasn't happened yet.
*  Yeah, great blog post.
*  I've been emphasizing that, you know,
*  if you step back and look at intelligent systems
*  of any kind, whatever you mean by intelligence,
*  it's not just the humans or the animals or, you know,
*  the plants or whatever, you know.
*  So a market that brings goods into a city, you know,
*  food to restaurants or something every day is a system.
*  It's a decentralized set of decisions.
*  Looking at it from far enough away,
*  it's just like a collection of neurons.
*  Every neuron is making its own little decisions,
*  presumably in some way.
*  And if you step back enough,
*  every little part of an economic system
*  is making its own decisions.
*  And just like with the brain, who knows what any of the neurons
*  are doing, doesn't know what the overall goal is, right?
*  But something happens at some aggregate level.
*  Same thing with the economy.
*  People eat in a city and it's robust.
*  It works at all scales, small villages to big cities.
*  It's been working for thousands of years.
*  It works rain or shine, so it's adaptive.
*  So all the kind of, you know, those are adjectives
*  one tends to apply to intelligent systems.
*  Robust, adaptive, you know, you don't need to keep
*  adjusting it, self-healing, whatever.
*  Plus not perfect, you know,
*  intelligences are never perfect and markets are not perfect.
*  But I do not believe in this era that you can say,
*  well, our computers, our humans are smart,
*  but you know, no markets are not, more markets are.
*  So they are intelligent.
*  Now, we humans didn't evolve to be markets.
*  We've been participating in them, right?
*  But we are not ourselves a market per se.
*  The neurons could be viewed as the market of science.
*  You can, there's economic, you know,
*  neuroscience kind of perspectives.
*  That's interesting to pursue all that.
*  The point though is, is that if you were to study humans
*  and really be the world's best psychologist
*  to study for thousands of years
*  and come up with the theory of human intelligence,
*  you might have never discovered principles of markets.
*  You know, supply and demand curves and you know,
*  matching and auctions and all that.
*  Those are real principles and they lead to a form
*  of intelligence that's not maybe human intelligence.
*  It's arguably another kind of intelligence.
*  There probably are third kinds of intelligence or fourth
*  that none of us are really thinking too much about right now.
*  So if you really, and then all those are relevant
*  to computer systems in the future.
*  Certainly the market one is relevant right now.
*  Whereas understand human intelligence is not so clear
*  that it's relevant right now, probably not.
*  So if you want general intelligence,
*  whatever one means by that, or you know,
*  understanding intelligence in a deep sense and all that,
*  it is definitely has to be not just human intelligence.
*  It's gotta be this broader thing.
*  And that's not a mystery.
*  Markets are intelligent.
*  So you know, it's definitely not just a philosophical
*  stance to say we gotta move beyond human intelligence.
*  That sounds ridiculous.
*  But it's not.
*  And in that blockbuster, you define different kinds
*  of like intelligent infrastructure,
*  I which I really like is some of the concept
*  you've just been describing.
*  Do you see ourselves, if we see earth,
*  human civilization as a single organism,
*  do you think the intelligence of that organism
*  when you think from the perspective of markets
*  and intelligence infrastructure is increasing?
*  Is it increasing linearly?
*  Is it increasing exponentially?
*  What do you think the future of that intelligence?
*  I don't know.
*  I don't tend to answer questions like that
*  because you know, that's science fiction.
*  I was hoping to catch your off guard.
*  Well, again, because you said it's so far in the future,
*  it's fun to ask and you'll probably, you know,
*  like you said, predicting the future
*  is really nearly impossible.
*  But say as an axiom, one day we create a human level,
*  a superhuman level intelligent,
*  not the scale of markets, but the scale of an individual.
*  What do you think it would take to do that?
*  Or maybe to ask another question is how would that system
*  be different than the biological human beings
*  that we see around us today?
*  Is it possible to say anything interesting
*  to that question or is it just a stupid question?
*  It's not a stupid question, but it's science fiction.
*  Science fiction.
*  And so I'm totally happy to read science fiction
*  and think about it from time to my own life.
*  There was this like brain in a vat kind of, you know,
*  little thing that people were talking about
*  when I was a student.
*  I remember, you know, imagine that, you know,
*  between your brain and your body, there's a, you know,
*  there's a bunch of wires, right?
*  And suppose that every one of them was replaced
*  with a literal wire.
*  And then suppose that wire was turned
*  into actually a little wireless, you know,
*  there was a receiver and sender.
*  So the brain has got all the senders and receiver, you know,
*  on all of its exiting axons and all the dendrites
*  down the body, you have a replaced with senders and receivers.
*  Now you could move the body off somewhere
*  and put the brain in a vat, right?
*  And then you could do things like start killing off
*  those senders and receivers one by one.
*  And after you've killed off all of them,
*  where is that person?
*  You know, they thought they were out in the body
*  walking around in the world and they moved on.
*  So those are science fiction things.
*  Those are fun to think about.
*  It's just intriguing about what is thought,
*  where is it and all that.
*  And I think every 18 year old,
*  it's to take philosophy classes and think about these things.
*  And I think that everyone should think about
*  what could happen in society that's kind of bad and all that.
*  But I really don't think that's the right thing
*  for most of us that are my age group to be doing
*  and thinking about.
*  I really think that we have so many more present,
*  you know, first challenges and dangers
*  and real things to build and all that,
*  such that, you know,
*  spending too much time on science fiction,
*  at least in public for like this,
*  I think is not what we should be doing.
*  Maybe over beers in private.
*  That's right.
*  I'm welcome.
*  I'm not going to broadcast where I have beers
*  because this is going to go on Facebook
*  and I don't want a lot of people showing up there, but yeah.
*  I love Facebook, Twitter, Amazon, YouTube.
*  I'm optimistic and hopeful,
*  but maybe I don't have grounds for such optimism and hope.
*  Let me ask, you've mentored some of the brightest,
*  sort of some of the seminal figures in the field.
*  Can you give advice to people who are undergraduates today?
*  What does it take to take, you know, advice on their journey
*  if they're interested in machine learning, in AI,
*  in the ideas of markets from economics to psychology
*  and all the kinds of things that you're exploring,
*  what steps should they take on that journey?
*  Well, yeah, first of all, the door is open
*  and second, it's a journey.
*  I like your language there.
*  It is not that you're so brilliant
*  and you have great, brilliant ideas
*  and therefore that's just, you know,
*  that's how you have success
*  or that's how you enter into the field.
*  It's that you apprentice yourself,
*  you spend a lot of time, you work on hard things,
*  you try and pull back and you be as broad as you can,
*  you talk to lots of people
*  and it's like entering in any kind of a creative community.
*  There's years that are needed
*  and human connections are critical to it.
*  So, you know, I think about, you know,
*  being a musician or being an artist or something,
*  you don't just, you know, immediately from day one,
*  you know, you're a genius and therefore you do it.
*  No, you, you know, practice really, really hard on basics
*  and you be humble about where you are
*  and then you realize you'll never be an expert
*  on everything so you kind of pick
*  and then there's a lot of randomness
*  and a lot of kind of luck
*  but luck just kind of picks out
*  which branch of the tree you go down
*  but you'll go down some branch.
*  So, yeah, it's a community.
*  So, the graduate school is, I still think,
*  is one of the wonderful phenomena
*  that we have in our world.
*  It's very much about apprenticeship with an advisor,
*  it's very much about a group of people you belong to.
*  It's a four or five year process
*  so it's plenty of time to start from kind of nothing
*  to come up to something, you know, more expertise
*  and then start to have your own creativity start to flower
*  even surprising your own self.
*  And it's a very cooperative endeavor.
*  It's, I think, a lot of people think of science
*  as highly competitive and I think in some other fields
*  it might be more so.
*  Here it's way more cooperative than you might imagine
*  and people are always teaching each other something
*  and people are always more than happy to be clear.
*  So, I feel I'm an expert on certain kinds of things
*  but I'm very much not expert on lots of other things
*  and a lot of them are relevant
*  and a lot of them are, I should know,
*  but should in some sense, you know, you don't.
*  So, I'm always willing to reveal my ignorance
*  to people around me so they can teach me things
*  and I think a lot of us feel that way
*  about our field so it's very cooperative.
*  I might add it's also very international
*  because it's so cooperative.
*  We see no barriers and so the nationalism that you see,
*  especially in the current era and everything,
*  is just at odds with the way that most of us think
*  about what we're doing here.
*  Where this is a human endeavor and we cooperate
*  and are very much trying to do it together
*  for the benefit of everybody.
*  So, last question, where and how and why
*  did you learn French and which language
*  is more beautiful, English or French?
*  Great question.
*  So, first of all, I think Italian's actually
*  more beautiful than French and English
*  and I also speak that so I'm married to an Italian
*  and I have kids and we speak Italian.
*  Anyway, all kidding aside, every language allows you
*  to express things a bit differently
*  and it is one of the great fun things to do in life
*  is to explore those things.
*  So, in fact, when kids or teens or college students
*  ask me what is the study, I say, well, do what your heart,
*  where your heart is, certainly do a lot of math.
*  Math is good for everybody but do some poetry
*  and do some history and do some language too.
*  Throughout your life, you'll wanna be a thinking person.
*  You'll wanna have done that.
*  For me, yeah, French I learned when I was,
*  I'd say, a late teen.
*  I was living in the middle of the country in Kansas
*  and not much was going on in Kansas
*  with all due respect to Kansas.
*  And so my parents happened to have some French books
*  on the shelf and just in my boredom,
*  I pulled them down and I found this is fun
*  and I kind of learned the language by reading
*  and when I first heard it spoken,
*  I had no idea what was being spoken
*  but I realized I had somehow knew it from some previous life
*  and so I made the connection.
*  But then I traveled and just I loved to go
*  beyond my own barriers and my own comfort or whatever
*  and I found myself on trains in France
*  next to say older people who had lived
*  a whole life of their own and the ability
*  to communicate with them was special
*  and the ability to also see myself in other people's shoes
*  and have empathy and kind of work on that language
*  as part of that.
*  So after that kind of experience
*  and also embedding myself in French culture,
*  which is quite amazing,
*  languages are rich not just because there's something
*  inherently beautiful about it
*  but it's all the creativity that went into it.
*  I learned a lot of songs, read poems, read books
*  and then I was here actually at MIT
*  where we're doing the podcast today
*  and young professor, not yet married
*  and not having a lot of friends in the area
*  so I just didn't have, I was getting kind of a bored person
*  I said I heard a lot of Italians around,
*  there's happened to be a lot of Italians at MIT,
*  a lot of Italian professors for some reason
*  and so I was kind of vaguely understanding
*  what they were talking about.
*  I said well I should learn this language too.
*  So I did and then later met my spouse
*  and Italian, Bohemian, were part of my life
*  but I go to China a lot these days,
*  I go to Asia, I go to Europe
*  and every time I go I kind of am amazed
*  by the richness of human experience
*  and the people don't have any idea if you haven't traveled
*  kind of how amazingly rich and I love the diversity.
*  It's not just a buzz word to me, it really means something.
*  I love to embed myself with other people's experiences
*  so yeah learning language is a big part of that.
*  I think I've said in some interview at some point
*  that if I had millions of dollars
*  and infinite time or whatever,
*  what would you really work on if you really wanted to do AI?
*  And for me that is natural language
*  and really done right, deep understanding of language.
*  That's to me an amazingly interesting scientific challenge.
*  One we're very far away on.
*  One we're very far away but good natural language people
*  are kind of really invested in.
*  I think a lot of them see that's where the core of AI is,
*  if you understand that you really help human communication.
*  You understand something about the human mind,
*  the semantics that come out of the human mind and I agree.
*  I think that will be such a long time.
*  So I didn't do that in my career
*  just because I kind of I was behind in the early days.
*  I didn't kind of know enough of that stuff.
*  I was at MIT, I didn't learn much language
*  and it was too late at some point
*  to kind of spend a whole career doing that
*  but I admire that field.
*  And so my little way by learning language,
*  you know, kind of that part of my brain has been trained up.
*  Yeah, and was right.
*  You truly are the Miles Davis of machine learning.
*  I don't think there's a better place than it is.
*  Mike, it was a huge honor talking to you today.
*  Merci beaucoup.
*  All right, it's been my pleasure.
*  Thank you.
*  Thanks for listening to this conversation
*  with Michael I. Jordan.
*  And thank you to our presenting sponsor, Cash App.
*  Download it, use code LexPodcast.
*  You'll get $10 and $10 will go to FIRST,
*  an organization that inspires and educates young minds
*  to become science and technology innovators of tomorrow.
*  If you enjoy this podcast, subscribe on YouTube,
*  give it five stars on Apple Podcast,
*  support it on Patreon,
*  or simply connect with me on Twitter at Lex Friedman.
*  And now let me leave you with some words of wisdom
*  from Michael I. Jordan from his blog post titled,
*  Artificial Intelligence, the Revolution Hasn't Happened Yet,
*  and the call for the creation of a new branch of engineering.
*  The term engineering is often invoked in a narrow sense
*  in academia and beyond,
*  with overtones of cold, effectless machinery
*  and negative connotations of loss of control by humans.
*  But an engineering discipline can be what we want it to be.
*  In the current era, we have a real opportunity
*  to conceive of something that is not just a tool
*  but a tool that is a tool that is a tool
*  and we have a real opportunity
*  to conceive of something historically new,
*  a human-centric engineering discipline.
*  I would resist giving this emerging discipline a name,
*  but if the acronym AI continues to be used,
*  let's be aware of the very real limitations
*  of this placeholder.
*  Let's broaden our scope, tone down the hype
*  and recognize the serious challenges ahead.
*  Thank you for listening and hope to see you next time.
*  you

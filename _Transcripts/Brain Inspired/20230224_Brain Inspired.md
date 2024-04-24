---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 5678s
Video Keywords: []
Video Views: 811
Video Rating: None
---

# BI 161 Hugo Spiers: Navigation and Spatial Cognition
**Brain Inspired:** [February 24, 2023](https://www.youtube.com/watch?v=GcCov8Biv6Q)
*  I came away from this that I'm still very interested in is this idea of creating algorithms
*  that match the stupidity of humans or the genius together, that genius and stupidity.
*  So I have a cognitive map of my house, let's say. I have a cognitive map of my friend's
*  house. These are distinct cognitive maps. The spatial schema is maps of people's houses.
*  What do I expect to have when I arrive in another friend's house built from those experiences?
*  We ask people, did you grow up in a city or some other situation, suburb, rural, mix?
*  And then we're simplistically asking with linear models or linear mix models whether
*  people who grew up in those two different situations navigate differently. Is there
*  a difference? What we were really shocked when we first looked at the data, or I was
*  shocked, was that...
*  This is Brain Inspired. I'm Paul. My guest today is Hugo Spears, who runs the Spears
*  Lab at University College London. In general, Hugo is interested in understanding spatial
*  cognition like navigation in relation to other processes like planning and goal-related behavior
*  and how brain areas like the hippocampus and prefrontal cortex help coordinate these cognitive
*  functions. So in this episode, we discuss a range of his research and thoughts around
*  those topics. You may have heard about the studies that he's been involved with for
*  years regarding London taxi drivers and how their hippocampus changes as a result of their
*  grueling efforts to memorize how to best navigate London. So we talk about that. We discuss
*  the concept of a schema, which is roughly an abstracted form of knowledge that helps
*  you know how to behave in different environments. Probably the most common example used for
*  a schema is that we all have a schema for eating at a restaurant, independent of which
*  restaurant we visit. We know about servers and menus and so on. Hugo is interested in
*  spatial schemas for things like navigating a new city you haven't visited before. Hugo
*  also describes his work using reinforcement learning methods to compare how humans and
*  animals solve navigation tasks. And finally, we talk about the video game that he has been
*  using to collect a vast, vast amount of data related to navigation to answer questions
*  like how our navigation ability changes over our lifetimes, the different factors that
*  seem to matter more for our navigation skills, and many other questions. Learn more about
*  Hugo's work through the show notes at brain inspired co slash podcast slash 161. And
*  if you value what I do, you can help me keep doing it by supporting the show in various
*  ways that will cost you very little. Go to brain inspired co to learn more about that.
*  All right, here we go. You caused a little friction in my household recently when I told
*  my kids that there is this new game that they could download and play that they hadn't played
*  yet. We're pretty careful with what they can play, you know, and their screen time is like
*  So any missed opportunities and wasted time doesn't sit very well. And I blamed you because
*  I, you know, after learning more about what you're doing, and I was I came to them and
*  I said, I have this new game and I think you're really going to enjoy it because they like
*  Minecraft and they like, you know, these kinds of things. So I think that they would enjoy
*  navigational games. And of course, I downloaded it. Of course, it didn't work. It asked me
*  for a code. What's going on with that? What am I talking about, first of all? And and
*  why can't I play it?
*  Well, the game I'm guessing you've downloaded is called see your request. Yeah. And the
*  reason you need a code is that we changed over the way that game worked. It was completely
*  open to play in the past. And that meant people could do stuff with it and give us data, but
*  we couldn't tie it to anything else. It was all totally anonymized. So if I wanted to ask
*  you a couple of questions or invite to meet you or anything, I wanted to link that to you
*  couldn't do it. So we set it up with a code, but anyone can get a code office. They just need
*  to get in touch. I think they search see your request on the web. They'll find a way to get
*  in touch. And we are looking, I should say, later in this year to change that, though. So
*  that game, I'm sure we'll talk about it at length. But this year, we hope to relaunch it.
*  So you do stumble across it. You can play anonymously and do new things we've never done
*  before with it. So yeah, watch this space for some new things we'll be doing.
*  We'll come back to that later. But okay, so is it only researchers that can get access via a code
*  right now? Or anyone can? No, anyone can. Yes. So there are at least 60 different projects ongoing,
*  all using this code system. So those researchers hand out codes to people, and they contact them
*  and they get them to do typically get them to do other things like other tests, they might get them
*  to do running or fill out some other form questionnaires about their lifestyle, whatever it is
*  those researchers are doing. And then they just tie it back to code. But the neat thing for us is
*  that code lies the game to work away in the background and send the data directly to a server
*  in a charity. So there's no hit download to send the data to researchers. There's none of that.
*  Yeah, it's working well. Yeah. Okay. Well, I just wanted to make sure that I started off our
*  conversation with a complaint and we will come back to see her request in a bit. Yeah. You seem
*  busy. And I mean, well, let's start with your origin story, I suppose, because I'm not sure
*  if you've ever had a grant rejected up to this point. But I know you've come in just under the
*  deadline, or had very little time to write some grants to study what you want to study. But
*  let's back up even further. I know that you did a PhD with Neil Burgess and John O'Keefe,
*  and studying navigation, cognitive maps, etc. Were you always interested? Did you know that
*  that's what you wanted to do from the beginning? Or how did you come into thinking that being
*  interested in navigation and cognitive maps and so on? Yeah, I got interested that during I decided
*  to do an undergraduate degree in neuroscience, when it wasn't sexy. This is back in 1999. I mean,
*  brains becoming a big worry. The key book that led me into a lot of this was Francis Crick's book,
*  The Astonishing Hypothesis, where he says we're just neurons. And it's a provocative book.
*  And you can take issue with the word just, but it's a good book. And yeah, so I'd started my
*  degree in neuroscience, so I was enjoying it. But I sort of came across all sorts of bits of research
*  and stumbled across all the work on memory and thought that was amazing. And then what happened
*  to me was probably a lot of other scientists, I decided to do a finding your thesis project.
*  I remember going to see Samuel Zecchi about color vision, lots of other incredible scientists at
*  that time. But I stumbled across a project that was combining virtual reality, patients who'd had
*  brain surgery, and walking blindfold in the dark experiments at the Institute of Psychiatry, and
*  jumped on this crazy project. It just sounded amazing at the time. So that's when I first
*  or I into research on cognitive maps and spatial was with Mike Reche when he was at UCL. He left
*  him a while back and has been in the States for some time doing other research. But yeah,
*  after that undergraduate project, I got a call from Neil Burgess say, come up to my office.
*  I thought, what have I done? What have I done wrong? It was like the head teacher called
*  their office to because I was on this course. I mean, like, no, if you're interested in a PhD,
*  so that was my kind of route in. Yeah. So the project must have gone well for him to have called
*  you in. Yeah, it was he wanted to know all about he was thinking about doing something similar at
*  that point with patients who'd had so these are patients who'd had temporal lobe, lobectomy,
*  so temporal lobectomies, either in the left or right hemisphere. And back in the sort of late
*  90s, early 2000s, that was a big, amazing sort of idea of looking at brain relating brain structure
*  to function. And yeah, Neil back then had been hacking away when I met him, he'd hacked into
*  Duke Nukem, and then started to create this entire virtual town that resulted in the science paper
*  and lots of other papers. But the idea then was to combine that virtual reality game with testing
*  patients. And that's pretty much what I did with John and Keith and Neil, Neil Burgess is my
*  primary supervisor for three years was putting patients into virtual reality environments.
*  I kind of not stopped still still doing that in 2023. Yeah, I bet I think Duke Nukem has improved.
*  This is a person kind of how would you describe Duke Nukem? It's an it was an early first person
*  virtual kind of world game, right?
*  Yeah, it was. And I think the thing that that was interesting on Duke Nukem was there other they
*  were like Wolfenstein 3d there were other games at that time. So it was very soon after they created
*  games, you could move in 3d space through your screen. And they were really novel, but that one
*  kind of had more colors, more textures, more variety, and kind of attempted to recreate cinemas,
*  cafes, things in the real world that the other games hadn't done. So it was it was Neil Burgess
*  spotting that, oh, well, we could turn this into something that would test real life experiences,
*  as it was back then. Yeah. But yeah, it had a lot of violence, monsters swearing all that,
*  yeah, that are in video games. It was it was definitely wouldn't pass
*  current standards for appropriate. Yeah, I wasted a lot of time on Duke Nukem. And I'm not a big
*  video game player, but I remember playing that one. Not with not in a scanner or anything, though.
*  So I thought I had heard that you were going along your merry way and then read about
*  the famous place cells. And that changed your trajectory. And I mean, I don't know if I heard
*  that incorrectly. But but then just separately. So correct me if I'm wrong about that. But then
*  even separately, I wonder how many people this happened to because, you know, the idea
*  of discovering these place cells and the idea of all their place cells and that like changed,
*  gripped people and changed their career paths. Yeah, I think that has happened for me. It was grid
*  cells. I never I've never recorded. But it was very similar experience. I thinking, you know,
*  years back, I wondered about doing that. I probably not cut out for animal research. It's really
*  demanding and I'll do humans. And then working away in Neil Burgess and John O'Keefe had a kind
*  of joint lab back then was constantly exposed to the place or recording. And it was a really
*  exciting time papers being published every other week and see major discoveries in that period.
*  But yeah, certainly I can I can describe a number of other people I've worked with who
*  were doing one thing and then saw the place cells and this change dropped everything else
*  went to become studying place cells. But yeah, this the story of what happened to me was working
*  away. I was in my third postdoc working with Eleanor McGuire, getting to the end of that,
*  thinking what to do. And I spotted a fellowship, the Wellcome Trust that provided that where it
*  would provide you three years of funding for retraining, but you had to submit the grant to
*  be successful, you had to show it was the kind of career change where you could no one would hire
*  you to do this late into your career. So like you want to learn how to do genetics, but you
*  have no idea how to do it. It was like, oh, you can you can come and spend time doing that. I don't
*  think they'd factored in people doing single unit recording because it was just like start doing
*  that and you've only got three years to do a UK PhD. It's hard to learn all those techniques when
*  you're late into your career because you've got other things to juggle. The key like you said
*  there with that was I discovered the it was there on a Friday and the deadline was Monday.
*  And so the main thing is you just get the finance in order to say I want to I need finance for three
*  years, sort it out. And it got done. I thought it was insane to submit a grant that that quick.
*  But it was a whole weekend planning out three years of research and stuff I wasn't doing. So
*  I was very grateful to Kate Jeffrey, who is the PI that helped support me and do that.
*  I joined her lab. But yeah, it's a fantastic thing to be able to do.
*  Would you recommend waiting until three days before? I mean, you know,
*  this kind of procrastination method that like forces you to do the work, you know?
*  Yeah, no, it's there is that I mean, there's if you're forced against the time wall, then it can
*  focus the mind. But no, it's not not an advisable strategy. I also had one of the grant where
*  this is a this is a crazy for me another crazy story in my where the James McDonald Foundation
*  got on got in touch with me on April 1. I got an email on April April 1, April Fool's Day saying,
*  Congratulations, you've been invited to apply for $600,000. All you need to do is and I think I
*  stopped at the point is that all you need to do is and then they emailed me a week later saying,
*  we emailed you this we not had to reply. You've only got two weeks to the deadline. Are you sure
*  you don't want to? Wow. And I realized I missed this. So I yeah, I rapidly put that one together.
*  So yeah, two grants where it was very close to the deadline. But yeah, I wouldn't recommend it
*  to people do read when someone writes to you saying, we've got 600,000. It may be true. You
*  never know unless there are prints, unless they claim to be a prince, perhaps. Exactly. Yeah.
*  So you're a lot of what you study is navigation. And I know that you love taxi drivers. And you've
*  done a lot of the famous work with taxi drivers who have to learn this. What is it called the
*  knowledge? Yeah, the knowledge. Yeah. Yeah. Quote unquote. Right. Which is like basically how to
*  navigate all of London in the most efficient way possible. And they have to take this super
*  rigorous test before they can become cabbies. Maybe you can just add an I know this is like
*  beating a dead horse for you. But maybe you can just describe the you know, what what the kind of
*  the famous findings from those studies and and I don't know where you are. Because this was like
*  almost 20 years ago, right. And I don't know where you are because I know you're doing longitudinal
*  work and studying them as well. So maybe describe those results. And then any updates?
*  Yeah, absolutely. That's been a real joy to work with work on that project. So the key the key
*  work with taxi drivers all goes back to Ellen McGuire, who's a fellow of the Royal Society at
*  UCL. And I previously worked for three and a bit years with her as my supervisor. So back in 2000,
*  she and others from the brain imaging lab in London, the Phil described the function imaging lab.
*  She had decided in the day, this is quite a remarkable group of people. Why don't we scan
*  and measure the structure in their brain, which was a new approach back in 2000 around that time
*  to measure and use automated systems. But also they like looks reach the scans and measured it.
*  And the reason Eleanor decided to do this was that the in a range of other different animals,
*  like a food caching birds, squirrels and some other animals, their hippocampus changes seasonally
*  when they needed to remember things. And the animals that have higher memory demands tend to
*  have a larger hippocampus. So there's reasons across other species to think there'd be variation
*  in size. And as you said, taxi drivers on the way and explaining this, all they did a job like nine
*  to five is solving a spatial navigation problem. That's what they do all day, every day, using their
*  memory. So most if you get Uber or some other, they don't do that. They just follow a computer
*  system. But London taxi drivers, the licensed ones referred to as cabbies. Yeah, they have this exam
*  to get this little badge to work. And the exam is very simple. It's just ask a set of like 10
*  questions. It's just they're insanely hard. So they'll say things like, right, take me from
*  take me from Barrick Street to Brick Lane. What's every single street between those two very far
*  away points? And if you make a single error, like you, you know, you go, then they say, no, sorry,
*  you've made a mistake, come back next time. And so there are about 58,000 streets they could use.
*  So from a computational perspective, it's like a state space of 58,000 states of which the exam is
*  any two random ones. And there's only one solution that they've got to retrieve. But it takes about
*  four years. Typically, some can do it in two years, but it's often four years of study,
*  constant study of the street names. So the knowledge is really that the knowledge is street names.
*  It's not they need to know other points. So Eleanor found I keep the key going back to the
*  what so this is unusual. What she found was in 2000 that their posterior hippocampus bilaterally
*  was larger than control healthy non taxi drivers. And the longer they had been taxi drivers
*  cross sectionally, the larger their posterior hippocampus was. And so when I came into
*  joining this was that when I joined Eleanor's lab, this is 2003. The the aim of one of her grants was
*  let's compare them to bus drivers. Because bus drivers do a lot of the same things taxi drivers
*  do. It's just they don't have to remember things. They're just taking the same routes all the time.
*  So it's things like, you know, they're stuck getting visual motion, they're
*  dealing with the pollution, they're having to deal with annoying customers,
*  they live in London, all of these things are controlled for and there was, as before,
*  a larger posterior hippocampus and taxi drivers compared to bus drivers now. And the longer they
*  had been taxi drivers, the larger their posterior hippocampus was. And then while I was working with
*  Eleanor, we decided to scan them doing their job in an insane study that I wouldn't recommend that.
*  So it was this is a study we published in 2006 in NeuroImage. And in that study,
*  and I was discussing this with Dick passing him on email the other day, like Eleanor,
*  I remember the event she said to me, so how we look at this said, why don't you ask them what
*  they're thinking? And I said, what? She said, just ask them what they're thinking. And she had been
*  wondering about this for a while about the idea that people might actually be able to tell you
*  what's going on. And if you ask people to remember a whole day's experience is insane,
*  they course they can't, they can't do that. But what we did with that experiment was to put the
*  taxi drivers into a four million pound virtual reality simulation that we got a hold of because
*  it had been for a video game called The Getaway. And then for extensive careful work with engineers,
*  rebuilt the Sony PlayStation controller, it will pass through a metal detector in an airport
*  undiscovered. But for us, of course, we'd work inside an MRI scanner. And that was that was a
*  very hard task. But we then managed to put taxi drivers into a fully detailed simulation of
*  central London with pedestrians moving traffic, all of it, and hear the voices of people asking
*  them to go to places in a whole cast of famous neuroscientists were the voices. These were young
*  scientists then for now, heads of institutes. And yeah, no, we after all this painstaking work,
*  after they would do all this driving through London, we sat them down with a biscuit and a
*  cup of tea and said, here's the here's a video replay what's happening? Like what are they thinking?
*  Yeah, and they can tell you why they made that move. And it was the same with London taxi drivers,
*  they could tell you every reason why like, I didn't stop to let this guy go by to be nice.
*  I couldn't think about where to go. So I pulled over. Or I remember seeing Big Ben at that moment,
*  I had eye tracking to verify, are these things they're saying matching up with eye tracking?
*  90% of the time they were extremely reliable. But yeah, after all that painstaking work,
*  the only time the hippocampus was interested was the moment they had to first plan. So the whole
*  rest of the journey to their destination, there was no increased activity in their hippocampus.
*  A bit frustratingly, but that was the result that we uncovered there. And then yeah, that was back
*  in the day. And in recent years, I've decided, well, Eleanor's not done so much more with it.
*  There's a lot more to ask. Why don't we go back and ask taxi drivers some more things? So we've
*  just finished in the last year, an fMRI study that's only focused on that moment. So instead
*  of just taking a small sample of events where they have to plan, we now give them like 100
*  planning events like they do in their exam. And we're scrutinizing the fMRI signal for
*  for what's going on and exploiting the advances in computational models for looking at state spaces.
*  And it is they're planning over a network of spaces and it's great data. And of course,
*  unsurprisingly, we're measuring the volume of the hippocampus. We don't know yet. We're still
*  fruiting up. So I can't give you a does it replicate 23 years later answer yet, but we hope so.
*  Are these the same drivers though? Or is it longitudinal in that fashion?
*  No, this one is a cross section again, but we hope we can hang on to these
*  these people this time and scan them in another say, four or five years time.
*  Yeah. Gotcha. Are these drivers paid well?
*  Yeah, yeah, they are. I mean, you get in a taxi and you want to go seven minutes,
*  you'll have to fork out like, you know, maybe eight pounds. That's not they did charge quite
*  a bit to take a fully licensed taxi drive more expensive than Uber.
*  Naive question. I know. Wait, so you were saying that you were asking them what was the point of
*  asking them what they were thinking? First of all, I mean, while you're saying that I was
*  thinking my wife is like constantly asking me about my feelings and I have like no access to that.
*  I can't describe what I'm feeling and thinking at any given moment. So so these taxi drivers,
*  although it sounds like what they what they were describing was more like the reasoning behind
*  their actions kind of. It was it was a bit. I mean, it was it was one of those scenarios where if you
*  came back into your house and found like a dog had gone crazy and destroyed and then there's a vase
*  smashed everywhere and then you look like a whole sequence of events happen to you like that. And
*  there's a video replay and you see your face going like you could walk through what you remember.
*  And you might have they did they had whole sections where they say, I have no memory of this.
*  And they would say, and it would be I'm just driving down a straight road. There's nothing
*  to see. I might have been thinking about tomorrow, whatever mind wandering, but I don't know what I
*  was thinking. And then they bits they turn into a street and they'd say, Oh, my goodness. And it
*  would look boring to me. But they would say, What's happened to that shop? It's gone. There should be
*  a major, you know, supermarket there or they could anything that is sort of strange.
*  And we simulated one of the worst days you could have in London. So we didn't want to put them
*  through an easy journey. We constantly gave them blocked roads, customers changing their minds,
*  lots of things happening to them. So it created this flow of events and experiences that they
*  were really able to say, that's when I was thinking about this or that. And certainly when they were
*  replanning their route, we would see lots of prefrontal activity areas. You know, we know
*  lots of neuropsychological evidence and others that you would expect to see anterior frontal
*  lobe activity when you have to replan, but just no hippocampus. So okay, so their hippocampus,
*  like their posterior hippocampus lit up during the before the journey set off. And then it was not
*  active while the journey was happening. But when they had to retool, then it was the frontal cortex
*  that had a higher voltage. And if we were to do it again, I'd have measures of what exactly how
*  difficult the replanning is, because it's quite possible that maybe if it had been really difficult,
*  then then we might have seen the hippocampus involved. That would be my expectation now.
*  Back in 2006, we just had replanning or not replanning. And I think we missed out on,
*  but generally if it's there, it's only there for some replanning, but not a lot of it. That was my
*  conclusion by then. This kind of flies in the face of the classic navigational studies in rodents,
*  right? Where the place cell happens when, well, in this analog, the place cell would happen when
*  you turned on fifth street or something, right? That the place cell would fire, right? And then
*  other place cells would fire in different locations and stuff. But is it, you know,
*  recording bold signal, is it that it's just not sensitive enough to pick up the activity or,
*  you know, could there be that reason?
*  Yeah, it's a good question. And we have to be, it's very coarse, right? The bold signal is
*  an indirect measure of the neural activity, that's for sure. And here, you know, when you're
*  thinking about how the place cells would operate typically in a familiar space, pretty much, if you
*  looked at rats running through a maze or a box, and one of the most impressive features, and there's
*  a very nice paper by Caswell Barry's group on the monotonic, like it just maintains the same overall
*  rate of excitation around the entire environment. There's something incredibly beautiful about this
*  homeostatic system that doesn't really go up and down near the edges or the middle, it does
*  something very clever. And so taxi drivers driving through London, you wouldn't actually expect any
*  moment to moment changes in the overall bold signal if it's not. What you would expect is that if the
*  taxi drivers hit a dead end, they weren't expecting and have to now recompute what they're
*  doing, you might well expect shockwave ripples and to enter into some sort of off-line, non-task
*  focus, like, sorry, a non-stimulus oriented into your own thoughts and planning state, and that you
*  get a lot of shockwave ripples. And if you're getting shockwave ripples, you'd expect a lot
*  more bold signal in the hippocampus. So that's for me, the theoretical link between, we think the
*  hippocampus is involved in doing some memory-based planning through reactivating the maps, recalling
*  the information in those moments. And so I think that's why we saw it at the beginning of the
*  journey, because you have to recall, you're given a street name and you have to retrieve, where is
*  that? How am I going to get there? But for the rest of this, we just don't. That's the link in my mind
*  between what's going on between the neural, but it's speculation. We do need more data. We still
*  need it 2023. Yeah. Rats are humans. I was going to ask you this question, which is more difficult,
*  right? Recording and planning experiments and so on. But you already alluded to the fact that you
*  did this insane study with humans and that you wouldn't recommend. So now I was going to guess
*  you're going to say rats were harder to work with, but now I'm going to guess and say humans.
*  It all depends what you want to get them to do. That is the question. That is the point. What do
*  you want the rats of the humans to do? If you want rats to run around in a box, then they're great.
*  You've got them there. You don't have to invite them in. They're in a research laboratory.
*  But yeah, the behavior, if you're getting something simple, is fine. Getting rats to do
*  complex planning tasks or something more like humans, that is really hard. And we had a paper
*  last year in current biology where it took a lot like five years to work up a task that rats
*  really have to think about where they're going to go. That would also be hard for humans. The
*  humans would struggle similarly. So we could try and match rats and humans and the rat side is much
*  harder than the human side. Dumbing down the human side is making it harder for humans is like the
*  other flip side to that. So yeah, but overall rodent research is about four or five times harder than
*  the human work, I would say. You haven't worked with non-human primates. I know this isn't a side.
*  It's probably only of interest to me, but I'm always questioning because I worked with non-human
*  primates and I'm always questioning what would it have been like to be happy?
*  Yeah, no, I haven't. But I can imagine that three or four or five times harder becomes even harder
*  with non-human primates. And it depends what you're trying to do, of course. It's always the issue.
*  Yeah, yeah, yeah, true. So let's jump into this. You developed this task and you already talked
*  about, alluded to the paper that came out last year. And this is specifically to test navigation
*  skills and the neural underpinnings thereof in a setting where rats and humans are doing the same
*  task. So why was that important to do? And then just tell us about the wonderful successor
*  representation reinforcement learning algorithm that we've talked about a little bit on the show
*  before. But what was the question that you're asking? Why was it important to compare rats and
*  humans? Yeah, no, that's a great question. It seemed to me in the field, we've got lots of
*  research, like review articles and papers that are trying to combine rodent and human work together
*  and say, oh, look, these tell us about the same sort of things. I just did that with the taxi
*  drivers. I said, I think it's because we see this in rats, it's probably what's happening in humans.
*  But these are, it's always a bit of a marrying up very different scenarios and situations. So we
*  took the view of what if we would have actually directly linked this? So we have rats running the
*  same kind of trajectories that humans would actually run. Would you see similar patterns
*  in their behavior? That was the core question. But the key with that then for me was if,
*  you know, we often also think about rats and humans as having these different abilities,
*  like humans have a large prefrontal cortex. Again, I'm just trying to link together these
*  two species, like how different are their, how different is their their way of navigating? Or
*  are they actually quite similar? So one of the core questions in that experiment was,
*  are they very similar or very different? When we tried to equate, so always going to be different,
*  because you could never quite match it perfectly. But when you really work hard, can you get that?
*  And the answer is yes, there are very similar rats and humans in the way they navigate
*  mazes like this. But the other reason to set up this experiment really for me was
*  then we could test their behavior against models in the maze. We designed it, this experiment,
*  like a maze that would be useful for testing against reinforcement learning models. So again,
*  in the reinforcement learning field, you talked about a lot in the show, there's fantastic examples
*  of like four room mazes where you can look at the how, you know, applying some hierarchical
*  representation of sub goals and things in the models really helps involve and improve the match
*  to behavior and things like that, that people have worked on in reinforcement learning. But
*  I've known from working in rats for the, you know, from when I was going back to that training
*  fellowship of just how hard it is to get rats to do something interesting behaviorally that you
*  can match onto these reinforcement learning. It's amazingly, rats can screw things up in the most
*  amazing, elegant ways you wouldn't believe. They make it hard to run experiments, like they just
*  get interested in other things. And the key thing you've got to remember is that they've got a fur
*  coat, they've got to keep pristine and they need to go to the toilet, they've got all sorts of other
*  needs. They're prey, they don't want to be eaten. So there are all sorts of things going on that
*  aren't happening for undergraduate students and experiments. And they're quick, they run fast,
*  they like to move quickly. So all these things are going on. But the idea was that if we could
*  build this experiment where you would see comparable behavior where rats are not succeeding
*  all the time, humans are not succeeding all the time, they're failing, they're not failing so
*  badly, they're lost. So somewhere in between where you've got lots of errors, the purpose,
*  you learn nothing. So it took a while to get. And the key innovation in that experiment was having
*  a maze where the rats have to plan and go around obstacles to get to target locations, to get to
*  the goal. But when the maze changes, when you move those obstacles and those barriers,
*  visually there's not a big change. And that's because if you have a big visual change,
*  rats will get confused by where they are and spend time resent marking because they like to
*  pee on things and bite at stuff. So we have these canyons. So there's a maze full of canyons. They
*  run around on this surface trying to get to the target. And we could reconfigure the maze layout
*  to make that happen. Other groups have used similar approaches. John O'Keefe's group,
*  for example, have this honeycomb maze where things move up and down and ours was much cheaper. We
*  just move blocks between trials. But I was very pleased by how it worked with the rats.
*  But the other key reason for why you'd want to put rats and humans through the same test is that,
*  yes, you can apply them against the similar reinforcement learning algorithm set. But down
*  the line, as we've done since, you can then apply both the fMRI and the rodent single unit
*  recording or other rodent methods and then sync these up into the same trajectory space and the
*  same computational model. It seems like quite a powerful idea to have these cross species methods
*  that you can exploit human experiments and rodent experiments in one kind of
*  paradigm. So we're still working on that. That's hard to do as well.
*  But yeah, we're going to go back to what you said coming in. We were looking at the
*  rats and humans from the perspective of humans are thinkers. We plan, we mull over what we're
*  going to do. So you might expect humans to fit more with a model-based planning system,
*  where you simulate possible trajectories and you choose from a set. And there's wonderful
*  literature in the reinforcement learning field. People will be familiar with model-based
*  reinforcement learning. And you might think rats, having watched them, I have.
*  One of my expectations is that really habit, they like to build a habit quickly and run.
*  And so it's quite possible that a model-free system that just really emphasizes the optimal
*  actions the rats are taking might capture rats. And then as you discussed, there's this
*  successor representation model reinforcement learning model, which was devised by Peter
*  Diane in 1993. They kind of sat there for a while and became a big thing in the field.
*  But the idea there was that this might be, and Kim Stakenfeld had her paper with
*  prestigious co-authors in nature neuroscience, arguing that the hippocampus
*  has used as a successor representation from looking at the cells. So again, we wanted to
*  look at that with the data. And Kim Stakenfeld was probably very happy when we found that yeah,
*  the rats data and the human data in the way they move, the errors they make best fit the kind of
*  errors that a successor representation makes. And it's certainly a very sensible system to do
*  this flexible planning to not have to simulate every single time you move where you might want
*  to go, but to actually just cache a structure of the environment. But the person who deserves a
*  lot of credit in that project is Will Dacothi. He's the first author who was a PhD student in
*  my lab, who then is now a postdoc in Casual Barry's lab. And he really threw his heart and
*  soul into all the modeling, helping collect the Roman data, helping with the human data. It's a
*  hell of a PhD. What do you think about these different algorithms for, well, for example,
*  we'll stick with reinforcement learning algorithms, right? So in the study, you tested three different
*  very clean algorithms. And then the successor matched the behavior the best. But as we know,
*  let's say we assume that the brain does this cleanly as well. It has clean systems for separate
*  systems for successor representation type, for model-based reinforcement learning, and for
*  model-free reinforcement learning. But the reality is we don't actually know how separate these
*  systems are in the brain. Or really, if these clean algorithms map onto anything in the brain,
*  have this corresponding algorithmic mapping onto processes in the brain. And if they do,
*  they're all interacting. Would it be fair to say that they're all probably going on at the same
*  time and then vying for control or being controlled, which one's being used and so on? How do you think
*  about that in terms of the results that you got out of that study? That's an excellent perspective.
*  I've given a very basic perspective on that experiment, but you're absolutely right.
*  It doesn't make sense not to do that. So just like in everyday life, if you had to think
*  strategically from a model, everything you would do, I need to get the milk from my fridge that I
*  do every day. And I think it's just you would burn out from exhaustion and you need a lot of glucose
*  for your brain to just do that. So we have to have these habitual systems. And there are other times
*  where, yeah, if you can't, your route's blocked, there's a roadblockage in the real, navigating,
*  you can't use your habit system. You're going to have to do something else. So you're right.
*  In the real world, there are all these scenarios where it doesn't make sense that there's one
*  system. There's a lot of evidence that these are competing cooperative potentially systems
*  for solving problems. And I think maybe one of the ways of looking at our experiment is to say,
*  and this is a challenge of doing the work I do in navigation, is we set up experiments to test a
*  particular scenario that we thought was interesting. And it probably was oriented towards success with
*  the successor representation approach in that you had to do flexible planning, but it wasn't pushing
*  you like, my God, you have to rethink everything all the time. So I think that is the context there.
*  And that is the challenge of publishing research papers is you try and say, we did this work and
*  we think this is a, we see this and it makes sense that the successor representation can explain
*  this pattern of phenomenon. It may be used to guide, it may be part of the way we navigate,
*  but you change the paradigm and do something else, you would find very different results.
*  I think there's no question in my mind. But that's an empirical question, something we need to look
*  at. So I'm not claiming that, you know, it turns out the way we definitely navigate is a successor
*  representation. That would be a very false perspective. And I'm pretty sure we didn't say
*  that in the paper. We had a long discussion in there. We tried to bake and eat it, as I said to
*  someone that wrote to me afterwards. Yeah. Do you think though that something like the
*  successor representation would translate to non-navigational domains in the same proportion?
*  Or, you know, if you made a study and it kind of lended itself toward or was biased toward a
*  successor representation kind of strategy with, you know, with the relative different frequencies,
*  let's say of these three separate algorithms, I'm sorry, I keep rolling my eyes about these things,
*  but, you know, what kind of proportions are we using in our day to day lives?
*  Yeah. Yeah. I mean, that comes back to a nasty question again, which is for each person,
*  what is their daily life? Because some people's lives are really unpredictable. If we take you
*  and me, it's probably a lot of model free. Thank goodness. Because again, it's like a
*  tradition, you know. So there are beautiful experiments of people taking these models.
*  And, you know, when we were looking at our experiment, we were told the first to try this
*  by any means. Nathaniel Doerr had been doing a wonderful job of comparing, you've had him on
*  your show talking about his wonderful work comparing algorithms to people's behavior.
*  So yeah, this experiment was where, as far as I remember, he hadn't done rats and humans,
*  and we wanted to combine these two literatures together. But, and I should add, I mean, like,
*  it's not in the paper, because it's a very long paper as it is. But when we were trying to create
*  the experiment, it was very hard to get rats to show successful navigation behavior in these mazes.
*  Because I was changing the maze around, and they would just keep going down the dead ends or
*  hang around near the goal, but not getting to it. So they looked a lot in the early experiments,
*  like the model free algorithms, because we made the mazes so hard that you probably need a lot
*  of model based planning to solve them. And rats just don't naturally, you know, do that potentially,
*  humans might but rats certainly weren't. Yeah. So you said it took like five years to,
*  to get all this working. So was that just titrating for the rats behavior? Or did you
*  have to worry about humans like making it too easy for humans or anything?
*  Both, both the rats are much harder to get that to until, you know, it's projects to just take
*  with different people coming and going and building equipment, I hadn't a friend who's an architect,
*  design the maze, getting it all. So all those things just take time. So it's not like,
*  we were just held to, you know, to fight in a team of people for five years solid.
*  But yeah, the rats, just getting a scenario where the rats would run and show these wonderful,
*  flexible routes where, for me, the data in that study is beautiful, where I see rats
*  start a journey, they go into the maze, suddenly find that they can't walk towards the goal.
*  They've been doing that again and again, it's blocked. And then use their knowledge to run
*  right around the maze and find their way into the goal where they'd never done it before.
*  So it fit these kind of narratives. Rats don't tend to do that normally. But I think we built
*  up a scenario where they would, they could, they could learn how to do that through the
*  environment we picked. For the humans, it was really hard to reduce. We had to basically put
*  a lot of fog in humans in a foggy environment, because their vision were not fantastic. But
*  in the vision to spot changes in a maze far away. Once you've got the fog in there, humans become
*  quite dumb like rats. They just don't try to remember where all these edges in the maze are,
*  and they show the same sort of error patterns.
*  Dumb like rats. I thought the story was that we're supposed to appreciate animal intelligence a lot
*  more than we do. But you're saying perhaps, perhaps that's not the case.
*  Yeah, maybe I'm a bit overly like dumb like rats, like we were trying to get rats to do human
*  things. Whereas if the rats had built mazes for us, we'd look like unbelievably dumb. We couldn't
*  believe we couldn't smell the cheese at a distance. So yeah, we do have to.
*  So before we move on, just what's next on that project? I mean, do you have, does this tell you
*  anything about the way an AI agent should be built? Or how, you know, how to build intelligent
*  agents? Or is it more a story about the nature of our own navigational abilities?
*  It tells us that last part partly about how we, what sort of algorithms might explain the way
*  humans would solve a maze in a scenario like this. So that's one framing. But your question about AI,
*  I think is a good one over what does this tell us about AI and developing those. And you did
*  use a really nice phrase in your say, took three very clean, for that exact reason, very the
*  simplistically created models we could with no bells and whistles. We really wanted to have
*  very simple algorithms, see what they did. The takeaway I came away from this that I'm still
*  very interested in is this idea of creating algorithms that match the stupidity of humans,
*  or the genius together, that genius and stupidity. A lot of the work, if you look at the beautiful
*  work out of DeepMind that I've been following, because I know that I had my period in Ellen
*  Reguire's lab overlap with Demis, Demis' office. So I saw the rise of DeepMind.
*  And a lot of that's incredible showing these like better than the best world chess expert,
*  better than the best go player now. So we can show AI can do things at a super high level.
*  What I'm quite intrigued by is the idea of building AIs that can simulate dumb people,
*  because there's huge advantages to predicting people being dumb. And I'm sure we'll see more
*  of that work going on. But it's not something I see a lot of. I don't know if you've had guests
*  on your show talking about that. I don't tend to see a lot of discussion about building
*  AIs to capture stupid behavior. And then what do we do to rule this out or solve it? So I think
*  that's a really nice thing we'll see out of some of the... And this project did that. It helps,
*  but it shows that humans aren't, in this scenario, fantastic model-based planners.
*  They make errors that are not consistent with someone constantly planning. It's not what we do.
*  Although some humans in the experiment definitely were... Their data matched the model-based plan.
*  So I think that's one of my perspectives on this relation to AI and what's happening in
*  reinforcement learning. A related topic is ecological validity. So there's this craze right
*  now that experiments need to be more ecologically valid. And in a sense, you stripped that away from
*  both the humans and the mice because they have very different affordances in the world. Their
*  umvelts are very different. So an argument could be made, and I'm not trying to be critical. I'm
*  wondering about your thoughts on this, that by putting rats in it, taking them out of their
*  ecological environment, taking humans out of their ecological environment, what is really to be gained?
*  Because maybe what you should be doing is putting them both even more so in their ecological
*  environment, but then it's not a controlled, nice experiment where they're doing the same thing,
*  I suppose.
*  So that's a lovely question. I think that's great. And I think the answer is that you need a whole
*  range of data. So it's great to get fully ethological data on humans and rats when you're
*  looking at what they do. So it was a really nice study, 2021, looking at using RunKeeper, this app
*  for running where a team in MIT got hold of the data, very carefully, lots of discussions, and
*  were able to show algorithms for how humans make navigational choices in the wild, in their running
*  in New York. So that's one way of going away from what we're doing that shows you how the behavior
*  in the lab relates to the real world. But another way is, and that's just wonderful studies of rats
*  in the real world as well. But then, yeah, what's the rationale of bringing this in? And it's exactly
*  that, that you can't quite so easily get rats running out in the New York subway with optogenetics.
*  People are going to scream, it's not appropriate, not ethical to do that.
*  It's really recording from people, you can't move MRI scanners currently around. There's movement
*  to do more mobile brain imaging, but they're just methods that mean, can't do this, and what can we
*  do? So I think, going back to that, if we had all the best kit and abilities in the world, it would
*  all be out there, but we don't. We need control, we need some lab scenarios, and we don't have the
*  time to collect a thousand years of data. So I would also say that experiment we ran in the lab,
*  we have humans play a video game, a video game that's very much like what millions of people
*  are doing right now. They're playing video games like we did. And the rats, our maze experiment,
*  I think is more ecologically valid than most of the box or plus mazes or thing. It's much more
*  like the kind of scenario you'd find in burrows that rats would crawl through. It's got that
*  kind of irregular feature layout. So that's my pitch. I want to come back. Okay, so I know
*  you're doing work recently on schemas, and I realized I don't really know what a schema is,
*  but so we're going to talk about that. And I'll bring in the taxi drivers later in this little
*  conversation, this part of the discussion, I suppose. But in this paper, you distinguish between
*  a spatial schema, cognitive maps, and like event schemas. What is a schema? And do I have it right
*  are schemas making like a comeback in the neurosciences or in psychological sciences
*  in general? Or have they always been there? I see more and more about schemas these days.
*  Yeah, I mean, they were first brought in. So defining a schema, off the top of my head,
*  I'm sure there's a really nice definition out there on schemas. And it's in our recent Nature
*  Reviews Neuroscience article, I'm sure of that. So in terms of working on schemas,
*  this is the recent paper review I wrote with Shana Rosenbaum and Maurice Moskovich and Ndela
*  is the first author, she's fantastic. So the team wrote this, for me, this review on how can we think
*  about distinctions between cognitive maps and schemas. And you're right in the sense that
*  schemas were, as far as I'm aware, going back to Bartlett in the 1930s, psychologists thinking
*  about how you can remember events and things, but actually you abstract over knowledge.
*  So not that you learn like you can learn that Paris is the capital of France, this is a semantic
*  fact. But gathering a knowledge base about what's likely to be the case or likely to happen in
*  scenarios. Or if I go into a restaurant, what do I expect to be in restaurants or happen in restaurants?
*  So an event based schema is things like what do I expect to happen at birthday parties? So it's not
*  like a semantic fact, your brain retrieves and goes, oh, the answer is this. It's a set of
*  predictions really. So a part of the idea of a schema is predictions, a set of representations,
*  a representation of the brain, of course, you learn a whole podcast on what representations are,
*  but this idea of something that allows you to map on and have expectations. So the key point in that
*  article we wrote about cognitive maps and spatial schemas is that, A, there's been a lot of talk
*  about event schemas. What happens if what do you expect to happen at a birthday party?
*  And less so on what do you expect in a spatial environment, in a city, for example. Although
*  there's been a lot of work on rodents and spatial schemas. And the distinction between the cognitive
*  map and the spatial scheme we draw there is that a cognitive map is described by John O'Keefe and
*  Lynn Nadel in their key book and building on Edward Tolman's famous work on where he proposed
*  cognitive maps. It's the idea of an environment, you go into a new environment and you build a
*  internal representation, a map. It doesn't mean it's a vertical map. So people get really fixated
*  on this. It's how, what extent it is a map, but it is a system of representations of distances
*  and angles and information about spatial structure, but it is all vast environment.
*  So I have a cognitive map of my house, let's say. I have a cognitive map of my friend's house. These
*  are distinct cognitive maps. The spatial schema is maps of people's houses. What do I expect to
*  have when I arrive in another friend's house built from those experiences? And what we pointed out
*  in this article is a surprisingly little note about this. Where is the neural system for the
*  spatial schema really represented? And this is an article in Nature Reviews Neuroscience where the
*  first figure outlines where this may be in the brain. And it's a guess. I would really be honest
*  and say the data is not sufficient to really be confident about where that might be. So with
*  events schemas, so what do I expect at a birthday party? It seems like the ventromedial prefrontal
*  cortex in humans plays an important role in providing that information through your imaging
*  data and patients. But for spatial, we don't have as much information. So that's really the key
*  distinction to draw in your mind between a map of an environment you have learned versus a
*  gathering of lots of environments that becomes a schema. And we just link that into lots of ways
*  of thinking about urban analytics. There's been a lot of wonderful work on how we could represent
*  cities and how cities are structured. So it's a wide ranging review trying to talk to that.
*  But it's something, yeah, we still don't know much about. I'd love to know. I mean,
*  extending this to taxi drivers, there was a case when I was working with Eleanor McGuire,
*  an amnesic taxi driver. It's like a Venn diagram of amazing memory, loses memory.
*  Let's study this one person who every hundred years may come forward. And he could navigate
*  a lot of London really well. He could tell you an enormous amount of spatial information.
*  He retained a lot of semantic knowledge about London. And he had a lot of like schematic ways
*  of thinking about the space. It was just when he had to navigate really intricate routes,
*  he couldn't do it. And you definitely wouldn't want to pay him money to take you somewhere.
*  Was he still taxing?
*  No, he wasn't. So he was someone you'd shake his hand and say, hello, go and get a cup of tea
*  quickly, bring it back. And he would have forgotten who he were and introduce himself again.
*  And when he was navigating, so we used the big virtual city.
*  Yes, exactly like HM. He had severe bilateral hippocampal damage. And he was densely amnesic,
*  but able to navigate London. A lot of it, but not perfectly. So yeah, I think, yeah,
*  that's the story there from my side.
*  Yeah. So I'm asking this because after I read your paper on spatial schemas, I read another review,
*  or I think it was a book chapter on schemas, written, co-written by Alison Preston. Anyway,
*  she like at some point in there, there's a sentence that says something to the nature of
*  blah, blah, blah, a cognitive map, which can be considered a spatial schema.
*  So in that sentence, she was like equating spatial schema and cognitive maps. What you're saying is
*  a cognitive map is a specific navigational map, right? To a specific environment and
*  schemas are as an abstraction over many different kinds of environments. Like in the literature,
*  I don't know what your sense is, but is there agreement on what a schema is? I have trouble
*  conceiving, it's so abstract, or is it abstractions or is it an abstraction? And I have trouble
*  visualizing what a schema actually is and how it will be represented.
*  No, I think you've got it right. Your confusion is the way you should be, if you're reading
*  about this. The reason that's right is that it is confusing. There isn't a cross people way they
*  thought about it and described it gives rise to it because it's not precise. There's not a
*  computational relationship between these things. You can't say this is what you would define for
*  sure as a schema. And in our review, we try to pick up on the fact that we draw examples like
*  in cities, I expect the big wide streets to be important streets. And I can tell you a lot about
*  what I would do. And you can have an awareness and you can describe it, but at a lower level,
*  your brain is just drawing on information to make predictions about where you should go in a space
*  that is building on those learned representations of the environment.
*  Another way of looking at it is that ideally you'd build a perfect cognitive map. You wouldn't make
*  an error ever going into a new place. You go on holiday to the Bahamas, you don't make a single
*  mistake. The way you think about the space is perfect. But we're not like that. We do make errors.
*  And part of that might well come because you have a schema of what you expect in the Bahamas and how
*  the streets should be laid out. And it's wrong. You think everything should be 90 degrees,
*  all the turns, everything's rectilinear. And it turns out it isn't. And you get caught. So I think
*  that's one of the ways we were thinking about the way in which your prior knowledge, these
*  representations. Other people might say Hugo's wrong. I don't see them like that. That's not how
*  I think about schemas. And that's where we are. It isn't a term that everyone would agree on.
*  And Ali Preston's comment exactly fits that, where in our review we didn't agree with that.
*  But I wouldn't say there's some huge disagreement with this. I can see where she's coming from.
*  One of the reasons why I wanted to ask about schemas and bring back the idea of the taxi drivers and the
*  increasing posterior hippocampus is because we think of the brain as hierarchically organized,
*  right? From lower level details to more abstract concepts to schemas now. And in the paper,
*  and I'm going to throw the word gist in here also and ask you what's different. What is a gist relative
*  to a schema? And then how those map onto different parts of the hippocampus. And then you just said
*  schemas are located in, and we'll use this term loosely, ventromedial prefrontal cortex.
*  And you can kind of, I don't know, can you think of that as just higher in the higher structural
*  hierarchy of the brain from posterior hippocampus to anterior hippocampus? And then that's the end
*  of the ability of hippocampus and it needs to offload then on prefrontal cortex. Is that the
*  idea there? Yeah. Yeah. There's a lot going on. There's certainly lots of that the brain has to
*  have hierarchical structure. Just anatomically it has. It's not, it's not, that's not a hard thing
*  to argue. And I think the spatial gist is a bit of a, that was something we suggested in the article
*  that you could go to full schema of what do I expect in French cities, right? I go to France,
*  there's particular things to French cities. It's quite a high level representation of
*  my expectations that can go from right top. There's a center, there's a cathedral right down
*  to how the streets are. It's different to other countries. Whereas a spatial gist might be something
*  smaller, we argued, like just fragments of that, where you're capturing commonalities over experiences,
*  say possibly even in a single environment about the relationships between things.
*  And the confusion here is these things are a bit like they fall between that episodic memory and
*  semantic memory where you've got one shot, you've experienced this thing, you've encoded the way the
*  park benches were laid out, or you've got a lifetime of knowledge about how park benches are always
*  laid out. And a spatial gist might be somewhere between, oh, in this particular scenario, they
*  tend to be doing this. So it's gathering that kind of a knowledge that's not based on a single
*  episodic event. That might be the spatial gist. Then going into the brain anatomy, I think it's
*  important. There's a lot of debate, as you've seen recently, about localists, the interior of the
*  campus is doing dysfunction. And you've seen this debate. And I fall in the camp of where I think
*  people are talking across this. So for me, there's undoubtedly localization function. Yeah, there has
*  to be. Because of just the lower level structures about how we breathe. There are dedicated neurons
*  localized in your brain for allowing me to breathe. For me right now, they're not distributed,
*  they are set there. It's much more complex for the neocortex as to how that's localized.
*  But I think a really key thing is to think about these as the hippocampus does this. And I think
*  it's certainly the case, the neurons are transforming information through the network. And the key thing
*  that keeps coming up again in this context. So under this, we just talked about it in my
*  mazes is that's a particular context and experience. So when we say the hippocampus is doing this,
*  it seems like the evidence is the posterior hippocampus is more engaged in fine-grained detail.
*  There's a very nice review by Lynn Nadel and Maurice Moskovich and others in Jordan popping,
*  looking at that. So we in our review are building on that idea of more posterior detailed areas to
*  more broad towards the anterior parts. And there's also some evidence in the prefrontal cortex of this.
*  So I think that's where that comes from. But it's important not to think in my mind that it is
*  a localized, oh, it gets passed and then it gets offloaded. And it's much more of a,
*  you're in a particular situation and these circuits will operate and use the word circuits,
*  as in pathways of axons going between neurons. And there's huge feedback and dialogue and a lot
*  of processing going on. But yeah, getting the bottom of it, but it doesn't mean you can't look
*  and say, where is this tending to happen? Where is this localized to? I think is a reasonable
*  question. It's just how you draw inferences around it. But it's already got onto a tangent
*  about the recent... No. Yeah. They keep coming up every so often. Yeah.
*  I mean, I think, well, what is it? 99% of scientific disagreements are people talking
*  past each other. It's got to be close to that, right? Yeah. Yeah, absolutely. Yeah.
*  I'm sorry for my naivete about this, but so you brought up semantic versus episodic memories,
*  right? And does that kind of map on... So semantic is more generalized knowledge
*  thought to be accrued over time via many episodic memories. So in some sense, episodic memories are
*  like the nitty gritty detailed navigational memories, navigational memories, cognitive maps,
*  right? That we can kind of localize to the posterior hippocampus. Is there a posterior
*  to anterior, episodic to semantic indexing in the hippocampus as well? Do we know that?
*  That's a question. Not that I know of. I don't think people are conceiving it. So it's a really
*  nice question, but I don't think people are conceiving it of that way. If they are, I haven't
*  seen that argument made. There's lots of different perspectives, of course, and you've had lots of
*  wonderful guests on your program talking about how these things may work. But the impression
*  from a lot of research across the field would be the hippocampus is important for helping you
*  acquire, maintain, and hold on to recent experiences, both the anterior and the posterior.
*  The anterior is doing interesting things as well. The way it's organized is involved in suppressing.
*  There's a lot of different roles in stress and other functions. It's not just a system purely
*  for spatial memory. That's and certainly in humans. And if you think about the wonderful
*  concept cells, the Halle Berry cells and so on, they're distributed in the hippocampus. So
*  I always think back to that work. Whenever I'm thinking, I'm well raised in the cognitive
*  map field from John O'Keefe's UCL perspective, but it's really important to think about those
*  concept cells. So how the hippocampus is involved in semantic memory is much less clear, I think.
*  But there's the wonderful work from Farineh Varga-Khada back in 1997 when she discovered
*  the children with dense amnesia who could learn vast amounts of facts despite not having any
*  episodic memories because they had suffered hippocampal damage at birth or just after.
*  So we do see these amazing dissociations. The system is able to adapt to some things and not
*  others. It's telling us something. But yeah, still to this day, I think there's a lot of debate.
*  There's some very interesting reviews out there on how do we think about episodic and semantic
*  memory and how distinct are they really? They are a continuum. So I think it's
*  rich and interesting to think about these things. Yeah.
*  Do you think of a cognitive map to GIST, to schema? Are those three separate things or is that a
*  continuum? Yeah, that would be it. Well, yeah, if you think about it as an active process that you
*  grew up as a person in an environment, the moment you start moving around, I think,
*  would be the experience you would start to build maps of your environment, a cognitive map. But
*  you also start to acquire repeated experiences of what streets tend to be like, how wide they are.
*  So they're constantly in my mind going from the point as a child when you're developing your
*  hippocampus and these circuits to help find your way and remember things. In parallel, you'll be
*  building up that type of knowledge. And that happens throughout your whole life, really.
*  And then if you choose a career as an architect, you'll get even better at certain things if you
*  choose a career. So your experiences in life are going to shape the extent to which you
*  construct schemas from my mind, these expectations, these predictions that your brain has built.
*  Okay. So this is what I've been wondering about the London
*  taxi driver increased posterior hippocampus. And then thinking about if we buy into the idea
*  that the posterior is more concerned with the gritty details, and that as you move more anterior,
*  you are more concerned with more abstractions, higher level concepts, quote unquote. And then
*  I thought, why would I want my posterior hippocampus to be bigger? I would want my
*  anterior hippocampus to be bigger. I should not memorize cities. And that actually could be
*  detrimental because these taxi drivers also had slightly smaller anterior hippocampi. And I'm
*  wondering what the, if I don't remember, I don't know what the taxi drivers IQs are, if there's a
*  correlation to IQ and their ability to pass this test, like are low IQs more... No, I don't think
*  they've ever had their IQ tested. It would be interesting to do that. But I think they'd be
*  quite high IQ actually. I wouldn't say they'd probably be very typical, but if anything,
*  slightly higher because they spend all the time solving a complex puzzle. But the interesting
*  thing with that, like you just mentioned, in the early work and replicated, they had a smaller
*  anterior hippocampus, but that replicated with the bus drivers who have the same kind of background
*  of London, same level of education. So I don't think that shrinkage is to do with the other
*  things. It seems to be, I mean, this may relate. I mean, it was, it's in the original article,
*  a suspicion that it's some homeostatic process that, you know, Kevin Mitchell, who's, you know,
*  it may well have been on your program, I wouldn't be surprised. He said, you know, he said like,
*  if you keep doing this, surely it's going to explode out your skull. It's a tiny change.
*  It may be some conservation that you don't just keep adding here. There's some equilibrium in
*  the distribution hippocampus that it's getting altered. We really won't know. I mean, if somebody
*  manages to do a post-mortem collection of taxi driver brains at the end of my life career as a
*  professor, that would be amazing to discover that, but very hard to ethically and chase up and do.
*  Yeah, I'd still like to know. We still don't know in 2020. So 23 years later, we'd like to find out
*  if we still can replicate that effect, because it may be that it's, for all sorts of reasons,
*  may not still be the case. It has been replicated three times. So this is not a result
*  just a one-off and in a high profile journal. So we'll find out. I'll let everyone know when we
*  finally get the result. Okay. But if I were to force you to answer this, if you could shrink
*  and grow one area of your hippocampus, one region, and grow one region and shrink the other,
*  which would you shrink and which would you grow? I think I'd go for the duck. So I'm thinking
*  back. So I meant to say earlier that the taxi drivers have that shrink. They also are worse
*  at story recall and the ray figure copy, which is you see this abstract picture and you have to
*  recop copy it out. And then they come back with a blank page 15 minutes later and say,
*  could you redraw that picture you just drew from memory? And they're not clinically bad.
*  They're not impaired, but they are significantly worse than London bus drivers and non-taxi drivers.
*  So if you're going to answer your question, I'm thinking I probably would prefer the detail to
*  be retained because that's what I do as a scientist. There's a lot of picking through detail
*  than that sort of episodic recall. But my wife might say you could do with a better episodic
*  memory for what we're supposed to be doing tomorrow. She might have a different view.
*  Yeah. Okay. First of all, I mentioned IQ earlier and I probably shouldn't have even said anything
*  because it's not like if IQ is something that we created as a measure of intelligence. But I tend
*  to kind of think that intelligence is correlated with the higher order aspect of thinking, which
*  then would be correlated more with the anterior hippocampus function in this little story that
*  we're telling. But I mean, is that... Yeah. I think that's a little simplistic in the sense of
*  you're thinking about how... To go back to that model that was provided by Lynne Nydel and
*  Maurice Moskowitz, the detail is stored. There's a kind of... There's the storage,
*  but the processing of more fine grained information alongside more global information.
*  I'm not sure that that maps to the way of creativity or the way you could big picture
*  thinking. I'm not sure sure it's that... Just thinking about the kind of evidence. But it is
*  an interesting idea to think why are some people good at big picture thinking and others too detail
*  focused. Is it to do with the way they're using these circuits? I could be wrong. You could be
*  right. It's something that you could in theory test and find out. Our big creative people...
*  I do remember an experiment I would love to run but never got around to, but a famous author,
*  well at least famous to me, it was Will Self who'd written a lot of... He's an English writer,
*  said his brain was just exhausted with all the detail at the end of finishing a book.
*  It's that burnout for weeks and then he would come back and he said,
*  oh, I've got to scan writers when they finished submitting a 400 page book.
*  Because their entire world is in their head. And then a bit like writing a PhD,
*  somebody's probably going to do that at some point or may have done it and I missed it. But
*  I think there's some interesting questions there. Yeah. Well, I know that the story was too
*  simplistic and if you set it up an experiment, it seems rife for... If I did it, it seems rife for
*  just confirming my biases. By asking such a simplistic and dumb question, I'm going to get
*  an answer and probably a nature publication. No, I'm just kidding. I'm not going to criticize the...
*  Depending on what I claim. Right? Yeah. Okay. So moving forward, what's the next step in the
*  schema work? How are you testing it and how are you looking at the nature of the representations
*  that a schema is? Or are you? We're not. I mean, it's a great question. I was involved in that
*  review and I think we will carry on and do some analysis. The nearest thing to that is I work with
*  the London taxi drivers looking at how there it's not so much the... Yeah. But one way to look at
*  that is to think London, if you were planning a route through it, you could just plan over all
*  the possible states you've got to go through. Alternatively, you can structure it hierarchically
*  like this is the area I need to get to. Let's get to the area and then plan within it.
*  And so that gives rise to different predictions in how they plan. And that falls under that
*  kind of schema of how you are representing the structure. So we have evidence of that
*  and we're just writing that up in two different manuscripts where we're looking at. So that's
*  where I think we'll be reporting on something schema-like, which is about the hierarchical
*  structuring of knowledge in London. Yeah. What's higher than a schema?
*  Or sorry, what's more abstract than a schema?
*  Maybe a... It's an interesting probing question. So I had to really think about that one.
*  I mean, it's from the literature. I don't think anybody's suggesting something. So here I have
*  to make more of a joke about it, I think, than draw on actual art. But when I think about it,
*  it may be your life story. You tell me who are you? And it's like, I have to abstract over
*  lots of knowledge. But that's not so much a schema for what to predict, but gathering different bits
*  of all sorts of experiences to explain something. And you have an expectation there of what it is.
*  The schema is, what is that person expecting from me? It's not when I was two, this happened to me
*  a few months later when I was two and a half. That's not the level we want.
*  It's identity. It's like...
*  Identity, yeah. Your identity of yourself might be higher. But it's a great, great question.
*  Well done coming up with that. Well done coming up with it so quickly. I didn't have an answer to
*  it. So I like that answer though. Okay. Well, my podcasting schema tells me that it's time to move
*  on to Sea Hero Quest. So this is a video game and we started off talking about it where the game,
*  someone memorizes a map and the map has a few locations that they're going to navigate in a
*  little boat to. And it's like a virtual reality kind of game. And you had a company help develop
*  the game and then they advertised and you had something like seven billion people play the game.
*  And so something like that, right? Yeah, I think it's eight billion. But a lot of people
*  play the game except my children. And so and then from this game, you've been able to extract
*  lots of different information, even about people's sleeping habits there. Why men are so much better
*  at navigating than women. You must have gotten in trouble for just having that data come out.
*  Yeah, so give us the gist of the Sea Hero Quest and what you've found so far and just
*  the power of video games and using video games in scientific inquiry, I suppose.
*  Yes, I'll start with that maybe. Yeah, I'll try and give the life story of it in a nutshell,
*  and kind of keep it concise for this story. But yes, the power of games. And obviously,
*  when I started the podcast, I said I was attracted as an undergraduate to a video game
*  type. I did my PhD with video games. So I've been working for 20 years, exploiting video games
*  to test to put people into situations that allow me to rigorously test. What had happened in around
*  2015, maybe 2015, I started working with Michael Hornberger, who's a dementia research expert,
*  cognitive expert in dementia. And he runs the dementia research center in UEA,
*  University of Stanglia. So he and I have been working together. Could we help develop some
*  diagnostic tools for Alzheimer's? But she's an expert in involving video games, but it's
*  really hard to do. And then one day, he got an email, he got someone contacting him and said,
*  there's a company out there with an unlimited budget who would like to do something like this
*  kind of crazy thing we talked about earlier. And he contacted me and said, I've got this very strange
*  request for a one page outline for probably come to nothing. So we filled it out, help Michael apply
*  this, it went back. And then a couple of months later, he got an email saying, yep, you've been
*  picked. That's it. We want to work with you to do this thing. And it was at that point, it became
*  apparent that the funder was Deutsche Telekom or T-Mobile, whose revenue per annum there,
*  their turnover is 68 billion. So they have some money. They're not a poor, they're the largest
*  richest telecoms company. But their idea was just to take their advertising budget for one half year
*  or whatever it was for a year and do something really innovative. And they employed Saatchi and
*  Saatchi, this creative agency, who are famous in the UK for crazy advertising, employed them to
*  come up with a way to use the budget. And their idea was, let's make a video game that can do
*  something fun that gets your message about you care to people. And the idea they picked was
*  dementia, doing something with dementia. And then we got picked, Michael and I, to then create
*  a test that would hopefully help with Alzheimer's. So that's how we got there. It wasn't,
*  we got some games designers to come in and, oh no, it was a funder came to us for the specific
*  project, specifically asking and we gave them a project. But it was incredible. We got a
*  commercial games company we were able to pick and work with this company, Glitchers, then for a
*  whole year, a high speed developing, less than a year, I think we went from idea to out there
*  to produced, because that's the way a telecoms company would work. But you're right, it's a
*  video game. It was launched in 2016 on the App Store and Google Play. And you play a little boat
*  and you just, you go around trying to find sea creatures and take photographs of them
*  and share them with your friends. And because it was a telecoms company, you know, we had a
*  good advertising budget to promote it on all sorts of platforms. And one of the key things that budget
*  after a lot of negotiating from the PR team was they stalked and tracked down and harassed
*  PewDiePie, the number one YouTuber in the world at that point. I think he still may be the number
*  one YouTuber, but they convinced him to advertise it. And so he pitched on his YouTube channel.
*  Oh, is this like the, where people watch other people play video games?
*  Exactly. Exactly. So he's one of those people that plays video games and talks about them and does a
*  lot of other things. But he had 5 million people look at our game in two days. So it was an
*  incredible achievement. But he was paid a lot of funding to do that. And he donated all of it to
*  charity though. So I have to say very helpful guy and was good in that scenario. But that's some of
*  the background to how we ended up with 4 million people taking part. So we have people from 195
*  nations enter their data. I mean, you know, and one of the big things you should be asking is like,
*  are we really, you know, did everyone who said they were from the Vatican really from the Vatican,
*  which we doubt, you know, this is a great, we would look, we're looking forward to publishing an
*  article. It's just like, how much bias is there in a data set like this? How do you spot it? And
*  what is it? So we've seen the bias and excruciating fantastic detail, but it's good.
*  Like it's always there. It's in every lab experiment. You know, if you want to test
*  people in your lab and not everybody, not everyone's going to come off the street and do your
*  experiment. So I think, I think that's been amazing. Yeah. The game, the fact that effectively the game
*  generates time series data. So that was when you said video games for research, a really valuable
*  thing about video games is people will do lots of it. They enjoy it's a well-made game. You'll have
*  people in doing it in a naturalistic way. And we had the capability with a games company to do that.
*  So people intrinsically wanting to do this, unlike paying them. And the data is really rich. But what
*  I found with the project was that having lots of people play it, you can use the time series of
*  their data, of their trajectory data to look at things in a lot more detail than you ever could on
*  a normal test that's got a score of one to 25 or whatever. And so we've produced quite a lot of
*  papers just looking at the trajectory, like what's the distance people are traveling. So the really
*  good navigators take a short distance and they tend to be young people in their twenties.
*  In many countries, they tend to be male and they can the top place in the world. They might come
*  from as Finland, for example. So we were able to look over the data and understand how GDP seems
*  to correlate with performance in our task across the nations. But it's been an absolute joy to
*  look at big data so you can really screen through it, look at the consistency and then be quite
*  robust. You're no longer thinking about P values. You're just interested in effect size. How much
*  does this matter? So for example, we find that left-handers, they navigate maybe differently,
*  but they sleep longer by one minute. And it's not a real effect.
*  One minute longer? Is that what you said?
*  When our data set, that remember thing, that isn't a correct figure, but there will be a sleep
*  difference because you measured 700,000 people telling us whether they were left or right-handed.
*  And it will be significant if they sleep half a second longer with 700 data samples. It will
*  be significant, but it's meaningless. That's the kind of way of thinking about big data.
*  One of the stories that you tell is about how people from suburbs
*  tend to navigate better than people from cities, but not just from like inner cities, but not just
*  inner cities, inner cities that are laid out in a very grid-like manner, what you term grittiness.
*  If you live in a city that is really gritty, you're a terrible navigator in See Hero Quest.
*  And if you live in a suburb or a city that is less gritty or something more like Pittsburgh,
*  where I'm going to be soon again, that you tend to be better at navigating. So
*  I don't... Flesh that out a little bit more than I just simplistically did.
*  That is sort of capturing some of the key results. We published that in Nature in April last year,
*  where the key question we looked at with the data is very simple. We asked people,
*  did you grow up in a city or some other situation, suburb, rural mix? And the data clusters,
*  so it's very clear there are people from cities or not cities when you look at the data.
*  And then we'd simplistically asking with linear models or linear mix models, depending what's in
*  the model, whether people who grew up in those two different situations navigate differently.
*  Is there a difference? And like I said, you can get meaningless like, oh, they are, but they're
*  only a little bit better. And what we were really shocked when we first looked at the data, or I
*  was shocked, was that there is quite a reasonable difference. So across the lifespan from say early
*  20s through to late 70s, there's about a four to five year difference for men and women between
*  people who grew up inside and outside cities, where it's worse growing up inside cities.
*  But if you look at later in life, a woman who grew up, this is on average across all the different
*  nations we looked at, across all the different countries, a woman who grew up outside a city
*  in her 60s is equivalent to a woman who grew up inside a city. So 10 year difference in skill.
*  So for something to moderate your lifespan's ability is pretty shockingly big effect.
*  And then like you said, that's the average in the world. We found this effect was really big
*  in the USA, but very, very non and very overlapping with Argentina. So we're like,
*  why are Argentina and the United States coming out where some other countries are much further
*  down? Why is Ireland far back here? What is it about Ireland? And at that time, we'd
*  seen this geography paper, this analytical paper by Jeff Boeing went around on Twitter,
*  showing you could measure how gritty every city in the world was using his very simple analysis
*  of the entropy of the streets. If the streets are all lined up, you can measure that mathematically
*  as a highly organized low entropy system. But if you take somewhere like Sao Paulo,
*  there is almost no, there is no orientation in Sao Paulo, in central Sao Paulo, they all go
*  in different directions. It's highly entropic. And so Antoine Coutreau, who's the first author
*  and spent now five years looking at this data with us, initially as a postdoc and then as a PI,
*  he noticed this and said, let's look at that. And lo and behold, there was a very significant
*  correlation across 38 countries between the grittiness of the country's city streets and how
*  badly they were affected by growing up in a city. And so that was the central result in that research
*  paper. Then of course, to publish it in a highly rigorous journal, you go on a very long journey to
*  do a lot of other things like show not to do with where you live now, test the thighs and other
*  people replicate the effect, replicate the effect if you do a driving simulations, it's not taking
*  a boat around an aquatic environment because. But yeah, as you said, like in the game, we can look
*  at the entropy in the game levels. So across 45 levels, we could see that the really, really
*  disorganized levels maximally pull out this disadvantage of growing up in say Chicago.
*  So if someone from Chicago is going to find those much harder, but the title of the paper is not
*  cities are bad for your navigation. That's not what the title of the paper is. It's I forget the
*  exact title, but it's like entropy shapes your future spatial ability because we found that in
*  the really gritty levels in see your request, people from gritty cities actually had a slight
*  advantage. Although this is somewhat of an overlap with non city people. So it's not that it's so
*  that goes back to the schemas. So it seems that people who grew up in city environments have an
*  expectation of what they expect to see when they navigate a world and it biases them.
*  And so that's the real, there's a lot of, a lot of peripheral and loads of endless supplemental
*  figures in that paper to ram home the point and take it apart. And we had five reviewers who asked
*  a lot of questions about that data. It made it much better. Yeah. Yeah. The editor apologized.
*  Very sorry, but we've given you five reviewers to make sure every single one of them is happy
*  before we publish this. Oh my God. But is there a, so there's, you were saying that, you know,
*  there's not a story to be told necessarily of like where you should grow up or something.
*  And you were mentioning, you know, with such a large data set, you're going to get
*  good P values. Well, you're going to get effects. Just the question is like how large those effects
*  are. But then the question is, you know, even if those effects are kind of large, like, do I care?
*  Why do I care about whether I can navigate like for my real world experience moving through the
*  world? Like just because I can't get around quite as well in a city. Does that mean, you know,
*  do I really need to worry about that? How much should I worry about it?
*  I wouldn't worry about that. I mean, you know, I think if you look at clinical issues,
*  surgeons doing neurosurgery are not that worried about you losing your spatial skill
*  that they might tamper with your language ability. They're terrified. Right. So that is a known
*  factor in neurosurgery. You do not want to damage the language. So I think that's here. I agree. I
*  think it's fascinating. And it's one of the few studies in the world where we've looked at how
*  some experiences in childhood are then shaping your future experiences later. It's very hard to
*  study these on a mass scale, but we kind of, we would assume that it's likely in areas like language
*  and other aspects of how it's affected. But yeah, we shouldn't worry about it. I don't think. I think
*  the only thing there is I was really surprised. Like I said, this 10 year difference. And if you
*  think you're losing this skill, it's like, well, there is a clear advantage. And as Antoine said
*  to me once mulling over the data, it's like, well, you know, does it matter growing up in a gritty
*  city? Well, it turns out most of the world is not gritty. So you are kind of in disadvantage.
*  So it is better probably to grow outside cities and get that experience on average.
*  On average. So in the United States anyway, I guess people who voted for Trump are really
*  good at navigating and people who voted Democrat, maybe are just good at navigating. I hadn't thought
*  about this before, and I apologize if you are doing this work and I just overlooked it already,
*  but are you training reinforcement learning agents to play See Her Quest also? And then
*  comparing that like different kinds of reinforcement learning algorithms to the
*  different developmental stages of humans, etc. and how they navigate.
*  No, that's really, it's really nice to raise that because we have thought about that and
*  we've looked into it. We've recently got more funding to do things like that.
*  But actually, that's a good example where somebody to listen to your podcast might be interested in
*  this and get in touch because the data is so rich and so large that there's really good scope for
*  collaborators to join and do things. We do have three teams playing with the data. Every single
*  group who comes to do something with the data will see it differently and have their own questions.
*  So we haven't tried building reinforcement learning agents to do that, to play the game,
*  but it is plausible. It's a very interesting angle. And if anybody is interested, I mean,
*  I should also take this point to pitch and hopefully on the website, maybe we'll put some
*  details where the game is totally free for people to use for research. There's no cost
*  for anything. It's completely set up to maximum 60 projects, but also the data is completely
*  accessible. Everything we've done with it, someone can download and we'd be delighted to
*  facilitate someone doing something with this data. So hopefully more people will do things with this
*  data and we'd love to speak to them to help them do it. Do you have like a ton of other,
*  like I know that one of the things that you're interested in was sleep. Why were you interested
*  in sleep? And then of course the finding, the robust finding is that seven hours is the perfect
*  amount of sleep for navigation. Right. That's right. So this is our Nature Communications
*  article end of last year. Yeah. So when we set up, I should say when we, the data looks really rich,
*  right? And it is rich spatially. We have wonderful time series of 4 million people.
*  But maybe 70% or less fill out with these demographic questions. And working on the
*  project, we had a lot of fight with the developers and the team, but they said,
*  you really can't ask more than nine questions. People are not going to answer. I think they
*  might've, but their criteria as well was not only we wouldn't ask loads of questions, but it was,
*  these have to translate into 17 languages and be iconic. You can just click and expand. And so
*  sleep is an easy one to say how many hours of sleep do you typically get? But it does also
*  relate to sleep disruption and Alzheimer's. So a lot of our questions were kind of else, would this
*  help in refining the data? But it's a great question. And yeah, like you said, what we found
*  was that later in life, so after the age, after you're in your early fifties through to 70,
*  getting people who report seven hours are better navigators than people report eight, nine, or any
*  other range. It doesn't recommend you should sleep seven hours. It's just the people who tell you
*  that they sleep seven hours tend to perform better. So you can make that causal relationship and say,
*  it is good to get seven hours, but the data by itself doesn't provide the direct evidence for
*  that. But yeah, it was really striking. It wasn't. And the key exciting thing I saw in that data set
*  with the sleep data was observing a pattern no one had seen before. So it's not too surprising
*  that getting optimal sleep might help your cognitive skill. But what we hadn't known until
*  that paper was that if you look across the lifespan for reported sleep, it's not smooth.
*  There's something happening to humans that between the age of early life through the
*  end of your teenage years to 33, it declines. You get less and less. Probably when you've got
*  children, it's really low, plateaus. And then after 53, it goes higher. So it's not a smooth U shape.
*  And we don't know why. We say in the article, we don't know why those particular age bands
*  are fixed like this. But the amazing thing for us was when you separate the data set in half
*  and just say, we'll look at men and we'll look at women, you think these numbers are going to change.
*  And they didn't. 33, 53 for both men and women. And you say, well, all the Western people who've
*  got low to high GDP countries who are all living in rich scenarios with loads of facilities and
*  play video games and these groups, maybe they'll have different numbers to the people in low and
*  middle income countries. No, same numbers again, 33 and 53. So there's something going on with the
*  human lifespan and sleep around 33 and 53 on average that we don't know why. So maybe at the
*  end of my career, someone will answer me and say, oh, you know what it is. I don't know the moment.
*  At that point, you'll be sleeping more. I hope so. That's what the data suggests.
*  Yeah. Yeah. I know it's 10 PM in your world and your children have slept through this
*  whole thing. Thank you for that. We got lucky, but you got to get some sleep, even though you're at
*  that stage of your life where you don't get any sleep. You still need a little sleep. So I appreciate
*  you staying up so late to talk to me and finally doing this with me. We've had to reschedule a few
*  times. And so thanks. Oh, no problem. It's been a pleasure. I've been really enjoying your podcast
*  for years now. And yeah, it's real delighted to finally make it after scheduling onto this. I
*  really appreciate you taking the time to talk to me and yeah, I'll continue to enjoy your podcast
*  going forward. I'm sure it's fantastic around your guest. So great. And you've asked me fantastic
*  questions that other podcasters don't ask. And it's great. Really appreciate it.
*  I alone produce brain inspired. If you value this podcast, consider supporting it through Patreon to
*  access full versions of all the episodes and to join our discord community. Or if you want to learn
*  more about the intersection of neuroscience and AI, consider signing up for my online course,
*  Neuro AI, the quest to explain intelligence. Go to braininspired.co to learn more. To get in touch
*  with me, email paul at braininspired.co. You're hearing music by the new year. Find them at
*  the new year.net. Thank you. Thank you for your support. See you next time.

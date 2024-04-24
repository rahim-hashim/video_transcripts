---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 4266s
Video Keywords: ['Science & Medicine', 'Technology', 'episodes']
Video Views: 3592
Video Rating: None
---

# BI 035 Tim Behrens: Abstracting & Generalizing Knowledge, & Human Replay
**Brain Inspired:** [May 20, 2019](https://www.youtube.com/watch?v=TkxIOvcN3CE)
*  almost all of the really unusual things I've done have either been inspired by or crystallized
*  when I've seen something else happening at a conference.
*  But it's not like I see it and then I think I do the experiment.
*  It's like, okay, that sparks off an idea which then takes months to evolve, etc., etc., etc.
*  I also think it's really important to know your place in the broad scheme of neuroscience
*  and how neuroscience fits together and what role you're playing in it.
*  This is Brain Inspired.
*  Welcome, everyone. I'm Paul Middlebrooks. I apologize in advance. This introduction is going
*  to be just a bit longer, I think, than others. You heard there at the top for the second time
*  on the show, Tim Behrens, and you heard him talking about things related to scientific
*  conferences. Why, you ask? Well, I was lucky enough to have Tim on again, one, because he is
*  a glutton for punishment, but more importantly because he's giving a keynote lecture at the
*  upcoming Cognitive Computational Neuroscience Conference in September in Berlin. You can go
*  to the conference website to learn more about it, and that is CCNneuro.org. I'll link to it in the
*  show notes as well. You can find a list of the keynote speakers there and all of the relevant
*  information on how to submit, how to attend, and so on. I'm also going to link to a video of Thomas
*  Nazaralas who co-founded the conference with Kendrick Kaye where he explains its origins and
*  vision in more depth than I'll say here, but the CCN, as I'll call it, is a perfect fit for this
*  podcast because basically the whole idea is to bring together people in cognitive science,
*  artificial intelligence, and neuroscience to get them out of their metaphorical silos of thinking,
*  learn each other's languages, and share ideas and inspire each other. The CCN logo is even based
*  on a Venn diagram representing the vision of those three fields overlapping. That means it's
*  a perfect fit for you, and I have teamed up with the organizers of the CCN to interview the keynote
*  speakers leading up to the conference. So this is the first of what will hopefully be a series of
*  nine interviews since there are nine speakers, and I say hopefully because you never know what
*  will happen with scheduling and so on, but I already have three more scheduled and I'm working
*  out the others. So they'll be rolling out here over the next couple months, I suppose. So that's
*  exciting for all of us. Okay, so today again I talk with Tim Behrens, and if you haven't heard
*  our discussion on episode 24, I highly encourage you to listen to that first. It's not necessary,
*  but it does give a lot of the background for what we talk about today science-wise. The short,
*  quite incomplete picture of it is that Tim has been doing a ton of interesting work trying to
*  figure out how we generalize and abstract the structure and relations between concepts in our
*  head so that we can navigate among those concepts like we navigate in space, like walking around a
*  room or driving around a city, and he uses as a basis for this the hippocampus and the interrinal
*  cortex and what we historically know about them and what we don't know about them. I guess I'll
*  leave it at that for now, but he summarizes two of his recent works today. One about a model that
*  uses those principles to capture the kinds of neuronal activity found in the hippocampus and
*  interrinal cortex while performing the abstractions and generalizations that I just mentioned. And
*  another of his works that he talks about is about measuring and analyzing in humans the
*  phenomenon known as replay using Magnoencephalography or MEG. Okay, so we also talk about
*  conferences in general, and I think that you'll find his insights useful. We talk about the
*  wave-like nature of scientific progress in academia, a bit about what you can expect from
*  him at CCN, and the usual tangents I often take. Show notes are at braininspired.co slash podcast
*  slash 35. If you find the show valuable, you can find out how to support it for almost nothing via
*  Patreon. Just go to braininspired.co. Edward, Keven, Charlie, Alex, and Ben, thank you for your support.
*  Guys, let's all meet at CCN so you can tell me to stop playing guitar and singing midway
*  through the episodes like I plan to do soon. Hmm, a little foreshadowing. Okay, thanks for
*  listening, everyone. Please enjoy the good sport, quite English, and brilliant Tim Barons.
*  Alright, welcome back, Tim. Hi, nice to be back. Thanks for having me. Good to be back in this
*  situation. Oh, yeah, good. I had you on the show I just saw on Skype. It was four months ago,
*  which was episode 24. As you can guess by the speed of things in research, I've done loads and
*  loads of exciting new things since then. Oh, well, actually. Oh, he's modest, folks. He's modest. So,
*  Tim, I have, as you know, I've teamed up with the folks at the Cognitive Computational Neuroscience
*  Conference to interview the keynote speakers that will be talking in September in 2019 in Berlin.
*  And, you know, when we made this sort of agreement, they sent me the list of the keynote speakers,
*  and I see that you're on it. And I think, oh, good God, I got to talk to this guy again. He already
*  do enough damage on my show the first time. Okay, good. Let's move on. Anyway, you know,
*  between like recording each episode and editing each episode, I really don't get a chance to
*  listen to the final edited version. And it's kind of torture to listen to myself actually. But in
*  preparation for this, I did listen to our episode. And I really thought, wow, this is this is fantastic.
*  I'm so glad I do this show. Well, I've listened to a lot of the rest of this. Since then, I've
*  listened to a lot of lessons postcards, and I've had I quite often listened to them on my journey
*  to work. And I've learned a lot. So I think it's great, too. Oh, great. Well, thank you. Anyway,
*  the last time you're on, we talked about the history of place cells and grid cells in hippocampal
*  regions of the brain and your work on cognitive maps and the structure and relations between
*  abstract concepts. At one point, you even licked your nose. And if I remember correctly,
*  your tongue got stuck in your nostril. And that's why we had to stop talking that day. Yeah,
*  something like that. Yeah, I see you've gotten it out. So that's good. I'm happy about that.
*  There's still some remnants there. Boy, I'm glad we're video conferencing. I'm not in the same room.
*  Okay. But you have been really busy since we talked. So how's it going in general? Good. Yeah,
*  I'm still alive. I've still got some children. And so most of it's good. Yeah. Seems like the
*  group's got some new things to say, or at least might do in some time in the next two years. We've
*  got some results that we might have to write about. So that's good. Is this the busiest that
*  you've ever felt? And you know, it is? Is this the most productive stretch of your career thus far? I
*  know that you I mean, you have a long history, you know, with value based decisions. I mean,
*  basically, I do what I can do one thing at once. And so like, normally, we go through these waves,
*  and you spend a long time working on an idea, and everyone's working on that idea. And then
*  something sort of clicks into place. And so no one's writing. And then suddenly, things take
*  into place, you understand how to think about the problem, how to analyze data, and then lots of
*  things click into place. And then you have a lot of papers to write. And then if it all works well,
*  then you go through a period of writing grants. And then you get a chance to think of something
*  else, some other idea. And so yeah, I think you I think it is kind of noticeable in my just in my
*  publication record that there's it's a periodic, basically, nothing so far in 2019. And then we're
*  about I think there are like, where there's several things in the pipeline now, one of which is in
*  press, and then once on archiving was a niche last year, and we're writing a journal article about
*  it. And then there's a whole there's a there's quite a lot of other things in the writing phase
*  at the moment, they're all on this idea about how structure is represented and abstracted and
*  applied to new situations in reinforcement learning, and probably the mapping, etc, etc. And I
*  think everybody in the group has been working on that in different species, or in theory or in
*  different types of data. And so yeah, you're going to see a bunch of papers at least written,
*  whether whether accepted or not over the part over the next year or so, we're coming to the stage
*  where we understand something about this problem. And then I guess you'll see five years of nothing
*  for me again.
*  Well, that's what I was gonna ask if you with the wave metaphor, if you're just short of the
*  crest, and you'll be surfing down in the next year, or you know, how what's that, you know, where
*  you are on the wave?
*  We're writing we're writing this. I haven't written any data papers for three years. Really. I
*  wrote a big review last year, which sort of said we sort of previewed the kind of data paper I was
*  going to write this year is currently for theory and data papers being written in the lab and there
*  will be there will be a couple more this year as well. And then maybe I might think a decade after
*  that. Or whatever. That's how it works. Yeah, I mean, like, somehow, it fits in with the grant
*  cycle somehow, etc, etc. I mean, the whole I don't know, maybe other people have different
*  experiences of academia to me, but that's how it's always worked with me.
*  One of the minor actually reasons why I retired from academia is that when I was a, you know, a
*  grad student, I felt pretty busy. And then, you know, people, who is it was multiple people who
*  expressed this like, I know you feel busy now. But then when you become a postdoc, it actually, you
*  don't think it gets busier, but it actually does. And then when you become a faculty member,
*  it actually gets busier, even if you don't think it does. But what you're saying is, I mean, yes,
*  that there's this cycle these waves. So I wonder if the waves just get taller and taller, or does
*  it feel busy?
*  Or maybe I mean, so maybe maybe that's right. So for me, in particular, this might my feeling of
*  busyness and panic ties in with the funding cycle. So in the in the US, it is the case that I guess
*  people are often writing NIH grants, and there's no real cycle to it. So maybe I'm wrong. I don't
*  really know that well. But in if you happen to be fortunate enough to be well confirmed in the UK,
*  which is just like having a fairy godmother, it's just amazing thing. In that situation, you have
*  to renew your funding every five years, which takes a big chunk out of the year. But it's just
*  so happens that last year, I wrote a big grant. And this year after a big grant, which means that
*  effectively, two, three months out of the year is taken out, you're fucked, you squeeze everything
*  else in. And at the same time, we're finishing off a major theme of research. So yeah, I'm feeling
*  busy next year now. But I'm hopeful that next year, I'm just going to feel like I've got a dream
*  of some new science. And maybe that will last for five more years until the next funding cycle.
*  Well, thanks a lot for raising my blood pressure. Just thinking about it.
*  I'm sure that's really for everyone. Sorry.
*  No, well, yeah, I mean, you know, I'm remembering as a graduate student, even as a postdoc, how it's
*  very obvious when a grant funding cycle is coming up for due because all of a sudden, you have to
*  produce data, whatever state you're in, in your project, you've got to produce got to produce
*  something, we got to write something up, you know, so it's a it is a cycle.
*  Maybe maybe it's useful for people to know. I mean, it is just a feature of science that when you get
*  a bit more senior, you have constraints on your life that are not just about thinking about
*  science. Yeah.
*  Yeah. Okay, Tim, we're going to talk about some of your recent work in a few minutes here, like the
*  Tolman Eichenbaum machine, and hopefully a little bit about the phenomenon called replay in the
*  hippocampal system. But let's start really broad. And I want to ask a little bit questions in regards
*  to the CCN conference. So there's a ton of work being done to try to understand the function of the
*  hippocampal complex. And many of the neurophysiological phenomenon like replay. Do you
*  have a sense of like what you see as one or two of the most critical open questions about the
*  hippocampus or cognitive maps, you know, in this realm that you're working in?
*  So that question is always impossible to answer, because as an academic, you choose what you work
*  on. And so if I were to say something now that was different from what I worked on, then I'd be
*  really stupid, right? So
*  But you know, I mean, you could also choose on what you think would get funding. So but if yes, so
*  again, so I didn't I don't do that. Yeah. I, again, that's probably partly because of how lucky we are
*  in the UK to have the fairy godmother, the welcome trust, who are very supportive of just pure
*  intellectual curiosity. So I mean, the reason I'm choosing to work on the interaction of learning and
*  memory, the interaction of the abstraction of knowledge, and how that can be generalized in
*  hippocampal system and those things, is because I think they're fundamental problems in
*  understanding how what representations look like in the cognitive map. I think it'd be really
*  exciting. I think it'd be wonderful to know how those things are built and that those maybe are
*  developmental questions, which if you had access to different techniques, you could ask real
*  really interesting questions about. But somehow, knowledge is organized into a structured form,
*  which allows us to be flexible and use it in lots of different situations. And I think that the
*  nature of that organization is a very fundamental question. So I like working on that fundamental
*  question. And if there is one more fundamental question than what does that organization look
*  like? I suppose it's what are the rules which build that organization, which is, I suppose,
*  replay has a big role to play in that. And so I think that in order to understand the rules of how
*  you go about organizing knowledge from scratch in cortex, you might need to study, you might need
*  access to lots of neural recordings and interventions in development in sophisticated tasks,
*  which I think is a hard thing to do right now. So maybe if there's something that I love to see
*  someone do that I couldn't do, it might be something like that. But I do think it's true that
*  understanding principles for how knowledge is organized and how it's abstracted so that it can
*  be used flexibly. I think that's one of the more fundamental things to know about how we behave
*  in the world. And so I guess that's my answer. And I'm working on it in my own small way and other
*  people are too.
*  Isn't it? It's just so wonderful to work on what you think is important. What you know is important,
*  I should say.
*  I mean, so I mean, you didn't ask me what's the most important thing in the world to work on. I
*  may not. You asked me in my field, what's the most important thing? I think it would be slightly
*  depressing if even in your field, you weren't working on the thing that you thought was most
*  important.
*  What's the most important thing in the world to work on?
*  Yeah, good question. Cancer, maybe? I don't know. Or world peace?
*  World peace. All right. Well, thanks for being on the show again, Tim. It's been fun. We're gonna
*  go solve world peace now. So last time we talked about, like I said, the history of place cells and
*  grid cells. And along some point therein, I made the point that models in theory are kind of front
*  and center these days. And we chatted about sort of the progressive cycle of experiment and theory
*  and models and how place cells were a strong example of how experimental data actually
*  preceded the theory. And then you have this cycle that continues. In your world, in the realm of
*  cognitive maps and hippocampus and interontal cortex, what do you think that we need more of?
*  Do we need more technology, better technology, more data, like you were just saying? Better
*  models, better theories or something else? You know, is there something that is consistently you
*  think lacking that you wish we had more or better of?
*  Just to be clear as well. So my world really is frontal cortex. It's become hippocampus and
*  interontal cortex by coincidence, because I thought I needed to understand what information frontal
*  cortex was getting.
*  Well, this can apply broadly to the whole brain as well. But yeah.
*  So I think that if you were going to ask me what we need in frontal cortex, I think I would say, I
*  mean, it's pretty clear that we do need more theory. But I think there's very little in frontal
*  cortex, there's very little data, relevant data to constrain theory right now. So the reason I
*  think there's very little relevant data to constrain theory in frontal cortex is because most of the
*  situations where we know what frontal cortical neurons do are really very simple situations by
*  comparison to the very complicated situations that frontal cortex has evolved in. So almost all the
*  things we know about frontal cortex could be predicted by many, many different types of theory.
*  We don't know very much. Somehow because the hippocampal representations have been observed, as
*  you said earlier, in naturalistic tasks, and because they're so convenient to look at in
*  naturalistic tasks, we know rich things about them. We know the nature of the representation.
*  I think we don't know those rich things about neurons in frontal cortex, because we haven't seen
*  them in large structured tasks where we can really understand what is being represented in those
*  things. Often we know that this one codes for value, that one codes for negative reward, that
*  one codes for this, that or the other. But there's no situations really in which we can predict the
*  rich dynamics of the activity and use that to understand the mechanism. And so in motor
*  cortex, we have that because people record during complicated arm movements. And in hippocampus,
*  we have that because people record in free movement across in space. And in frontal cortex, we
*  don't have examples of animals making complicated plans or making complicated inferences in richly
*  structured worlds where we understand the structure of the world. So we can understand what
*  mathematical relationships there are between the structure of the world or the structure of plans
*  and the firing of neurons. And so I would say actually right now in frontal cortex, fun there
*  is to think of models of frontal cortex, those models will always be tough to evaluate without
*  a different type of data. That's kind of what I think I would say.
*  I mean, do you have a sense of how cognitive science, computational neuroscience, and AI can
*  best work together? Are we working together well? Or how can we improve how all of these
*  fields can be more symbiotic?
*  I think we're learning to. So cognitive neuroscience is both quite old and also changing
*  quite fast right now. So I guess it went through a bit of a revolution when it had the earliest
*  models in there from Peter Dayan and Nathaniel Doar, who I guess you're going to interview and
*  join the team people like that with Ray Dolan. So that made a big impact on cognitive neuroscience.
*  And I think that a new impact is being made by these new more sophisticated models that are
*  coming from the latest AI developments. And I think that this is a transformation of cognitive
*  science, cognitive neuroscience. So I feel like it should be applauded. So I mean, I guess
*  there is there are like every revolution, there are there'll be bits that last and bits that
*  don't last. And I don't know which those bits are. I mean, there's obviously a bit of a pattern at
*  the moment of like, recording lots of data and then building a big network and showing their
*  match. And although sometimes you learn stuff that way, I'm not sure that always you do. And so I
*  wonder whether whether that will be a long term game plan or whether instead trying to understand
*  some of the principles of the representations might be a more informative thing in the long term. I
*  wonder whether setting up networks that obey constraints that we know about the brain or might
*  be a productive avenue, particularly in systems that have very stereotypical architecture like
*  those corticosteroidal loops or the hippocampal interrinal loops as we've tried to do or things
*  like that might give us information about what how representations should interact with one another.
*  I think it's free form of just putting an LSTM to a task and saying these representations look like
*  my XYZ representations is cool, but I think that it will be evolved.
*  It'll probably peter out and give way to a more...
*  I don't know if it would peter out because I mean, it tells you something about how to compress your
*  tasks into something that can be represented in a vector. And I think that is a deep insight. But I
*  think that sometimes the brain has other constraints too.
*  I know that you have your hands on a lot of different animal models and a lot of different
*  areas of research really. But do you have any... And I know that you don't have any idea really
*  what you're going to be talking about when you give your keynote lecture at CCN. But what are
*  some of the possible very general topics that you might talk about?
*  I think that one possibility is to talk about the two things that I'm talking about today,
*  which is this model that we built which tries to account for generalization of structure
*  in the hippocampus and the entorhinal cortex, which tries to account for ideas both in the
*  spatial domain and in the relational memory domain that we're calling the Holman Eichenbaum machine.
*  And then of those same ideas we've used to study replay in humans and to argue that these
*  representations that allow remapping and generalization, those representations can be
*  seen in replay as well. And so that's one possibility. And I think that'll be fun.
*  Another possibility is so we've been taking this idea of structural obstruction and learning into
*  the reinforcement learning domain. And so we've been doing studies where people can learn about
*  one thing and that will give them information about other parts of the space because of the
*  correlation structure of bandits, for example. And we have theory and experiments in humans and
*  rodents that are doing that. And critically, we're asking similar kinds of questions there. And so
*  what we're really asking is whether that structure, that knowledge about the correlations
*  between things which let you make inferences from seeing one observation to, for example,
*  another bandit or another thing in the world. But so we're not just saying that can happen.
*  We're saying you can abstract that structural information and then apply it to two new bandits
*  or new sets of worlds. And so this information is encoded in this explicit way that is completely
*  abstracted from all of the sensory information. And there are these representations in both neurons
*  of mice and in representations in fMRI in all of our favorite brain regions,
*  the entorhinal cortex and medial frontal cortex that know abstractly that two things can be
*  related to correlated or anti-correlated with each other, but don't know which two things it is.
*  In the same way that grid cells know about the spatial relationship between things in general,
*  but don't know which particular sensory events happen at those places in different environments.
*  The third thing that I may talk about just briefly is we have some grid cell experiments in macaques,
*  which we'll be recording from at about that time. And so it's possible that there'll be a few monkey
*  grid cells in the talk as well. We'll see. That's my world, man. That's why I would come.
*  Yeah. So that'll be exciting because we have some of these non-spatial relational map tasks that are
*  really well trained in a couple of monkeys. One of them in particular knows this very, very large
*  relational map of 200 objects or something. And so it's going to be really excited to see what
*  happens in the cells there. Oh, there's always like that one star monkey. Yeah, the other one's good
*  too, but not quite as good. Yeah. Mine were more distinct. I had larger distinctions between levels
*  of intelligence when I was always. Do you get nervous when you give talks?
*  Have you ever and do you still? Yeah, yeah. Terrified. Terrified.
*  It's a strange kind of, I mean, it's not a terror that would stop you doing something, but
*  I get nervous. I get adrenaline. And then I get exhausted afterwards. I think that I'll have that
*  forever. I'm sure most people have that. But has it changed over the years? I mean,
*  my terror became something like, oh, you still have the same feeling, but you still know like,
*  oh, I know it's going to go okay. Whereas when you start off, you think I might actually die
*  in the middle of my talk. No, I never thought that. I think maybe I never went through the
*  experience of thinking that I wasn't going to be able to give a talk. I particularly conference
*  talks, I used to rehearse them very, very thoroughly. And I rehearsed them less thoroughly now.
*  Maybe it makes it more spontaneous. I don't know. I still rehearse them. I still definitely get that
*  feeling of adrenaline and of exhaustion. I mean, what I don't, I don't sort of care quite so much
*  what people think anymore as I used to. Yeah. And so I'm sort of maybe more honest about what's
*  good and bad about the work. I don't feel like I'm being judged in the same way that I used to feel
*  like I'm being judged. I feel like it's the grant panels that are judging me, not the conference
*  audiences, I suppose. Yeah, right. And I tell you, I'm terrified. But that is a different thing. The
*  terror that you have before an interview for a grant panel. That is a real kind of like,
*  if I don't get this, my whole lab might lose their jobs. Yeah. Oh, shit. Yeah. Yeah. I mean,
*  I'm taking notes here. So you think I should actually prepare for these interviews and for
*  my show or? I mean, so far, it seems like you do a better job than anyone else.
*  Good. Man, you're my favorite guest. Have I ever told you that? So if someone was on the fence about
*  attending your talk, what would you say to them to convince them that they really need to go to
*  your talk? They don't. I mean, like, it's like, I mean, nobody needs to know what I do. It's just
*  like, it's like, it's esoteric shit, man. There's no, there's no sense in which anybody in the world
*  needs to know what I do. I mean, they may find it interesting, they may not find it interesting.
*  But I'm talking about like, abstract ideas of knowledge organization in the hippocampus and
*  frontal cortex. How do you represent the structure of tasks, those kind of things. I'm not talking
*  about like how you feel your tax form in you don't need to come to my talk.
*  Believe it or not, I anticipated this response from you. I have been told. So I was on kind of
*  a half date one time, but there was someone else in the car. And I was driving around and he was
*  being really obnoxious. And I eventually made him get out of the car and walk home. And he was close
*  enough to home. He was within a mile. And of course, but he was out of his mind angry. And
*  but my girl I was dating looked at me, she said, she said, Well, you don't take shit from anyone,
*  do you? I guess not. So my question is, is it you seem like the type of person that doesn't take
*  shit from anyone? Is that an important attribute in science? You think? Why do you think I'd seem
*  like that? I think that the maybe it's just highly correlated the attitude of someone doesn't even
*  need to come to my talk. You don't care. You're confident enough in your own skin. And I don't
*  feel I don't feel judged by anybody. The people I feel judged by the people that are going to
*  give me money. I feel like I like it when people are interested in what I say. I don't think that
*  I don't I don't I'm not going to go out of my way to make them think that they need to come and listen
*  to me rather than somebody else. I suppose. I suppose that's what I think. I think that what
*  I have to say is extremely interesting. I don't know. Perfect. That's perfect. That's going to
*  make the sound bit at the beginning. I'm sure. No, it isn't. I'll sound like a cock. Yeah,
*  that's my whole goal, really. So anything? What do you think is, you know, important to try to take
*  home from conferences in general? Because they can be a real wash, you know? Yeah. Yeah. Normally,
*  I come home with an idea, the new idea or something. Actually, that is true, particularly from
*  the early days of cosign. I used to really feel inspired by them when I was a bit younger. Now,
*  I think still that's true. Yeah, I remember going to talks about songbirds and how credit assignment
*  was happening in the songbird system and having ideas for experiments of credit assignment in
*  cortex as well in the human cortex for reinforcement learning, which is obviously a completely different
*  thing. Like how do individual neurons get credit for producing songs versus how does like some
*  stimulus get credit in a reinforcement learning bandit task, for example. But I almost always
*  find something like that. It makes you think about a new way of thinking about your experiment,
*  those kinds of things. I find that valuable. I never have been so much of a conference
*  networker. I know people think that's an important thing. I normally try and hang out with my lab.
*  It's the time that I spend most with my lab out of- Like socially, yeah. Yeah, I just think that
*  it's certainly that. Yeah, I mean, yeah, it's nice to have space to think and it's nice to
*  have lots of people talking about ideas that are not the same thing that you think about all the
*  time but are related. I feel like almost all of the really unusual things I've done have either
*  been inspired by or crystallized when I've seen something else happening at a conference. But
*  it's not like I see it and then I think I do the experiment. It's like, okay, that sparks off an
*  idea which then takes months to evolve, et cetera, et cetera, et cetera. But I'm pretty sure that
*  a lot of the early inspirations have come from seeing something in some completely different
*  field in C. elegans or something. And then it's like, okay, that can fit with that, those kinds
*  of things. I think it's really important to do that. I also think it's really important to know
*  your place in the broad scheme of neuroscience and how neuroscience fits together and what role
*  you're playing in it because it can seem like what you're doing is really, really important.
*  And then you can see that someone else is doing something with some particular cell type in C.
*  elegans, which might also be, and like somehow just seeing how big neuroscience is, is like a
*  both humbling and inspiring experience. And it makes you think, I feel like that has made me think,
*  maybe not be scared to broaden out. So I think some people, so I've tried to work with theory,
*  with humans, with monkeys and with mice. And it might have been the case that that would be a
*  daunting thing to do if I'd always been doing, if I'd been going to conferences where I'd just seen
*  human fMRI all the time. But then, and then I think, well, like, I don't know, neuroscience is
*  huge. And this is actually just like one small piece of, it's not like that broader thing that
*  I'm trying to do. I'm just getting a few little angles on it. And I think that maybe that confidence
*  partly comes from just seeing the breadth of neuroscience, maybe. I mean, people talk about
*  different scientific moments they've had that have, you know, that have really stuck with them.
*  Like people in, like me, who did eye movement work in areas like frontal eye field in monkeys,
*  everyone always remembers the first time they're in the lab and they see the whooshing of a neuron
*  right before a monkey moves its eye. And you could just, you know, you hear it, you see it,
*  and then you see the eye movement. And that's like a scientific moment. So you mentioned,
*  you know, being at a conference and learning about songbirds and what was the credit assignment and
*  credit assignment, right. So, I mean, are there other is there a specific moment that sort of
*  stands out when you've been at a conference? I mean, is that an example of a moment where
*  you've been at a conference that has really stuck with you and is maybe I mean, I like really
*  elegant things as well. I remember very clearly watching Tim Vogel's tell me how to make sure my
*  network doesn't go doesn't become too excited with his with his inhibitory plasticity. I feel
*  that was just a beautiful piece of elegance that worked and that inspired me to do an experiment
*  with him that came directly from from watching conference talk of his. Yeah, I mean, so those
*  kinds of things I found exciting from conferences. I mean, that's a little different from first time
*  you see your first neuron or your first clean result. Sure. There is something exciting about
*  about data that you've acquired yourself, particularly if you can if you've predicted
*  what it's going to do. Yeah. And just that feeling that you know something that no one else in the
*  world knows. That's that's the reason for doing science really. Yeah, that's a crazy feeling.
*  Yeah, exactly. And doesn't matter how small it is or how big it is. That's a cool that's a cool
*  feeling. And I Yeah, I feel like I've been lucky enough to have that three or four times in my
*  career, even as early as the early early parts of my career, I saw the anatomy of the thalamus.
*  And we'd saw this just this beautiful structure emerge from just looking at connections.
*  That was a very, very profound moment to me. I just thought, wow. And yeah, some of the some of
*  the work on when I was working on how people know how fast to learn, for example. So seeing that
*  in monkeys and humans and showing them adapting their learning rates, depending on
*  various statistics of the environment, those kind of things. I won't forget those things.
*  And I guess I guess I would forget seeing that signature of grid cells in this non spatial tasks.
*  So I mean, I've thought, OK, that's kind of cool. And I guess that's like seeing your first neuron.
*  And again, also seeing my first neuron was kind of cool. Yeah.
*  Yeah. So I had Tony Zader on the last episode. And he we talked about the early days of Nips
*  and then how Cosine, which he founded, sort of developed out of that. And Cosine is a conference
*  that's still going really strong. And I know that you've presented the past few years at Cosine. And
*  now you're going to give a keynote at CCN. So Cosine and CCN are both really small conferences
*  relative to something that is huge, like SFN or something. So what is there something special,
*  special about smaller conferences with respect to a larger conference like SFN?
*  So for me, partly because I hate the idea of like planning my life in the future.
*  I don't like SFN, really. But I mean, in order to get the most out of SFN, you've got to fill
*  those planners in and make sure you're in the right place at the right time. And for me,
*  the future is like an abstract concept. It's not like organized into numbers with hours and days
*  in it. So I find it very difficult to make those kind of plans. Yeah. So I've never really had a
*  great experience of SFN. Cosine, I just love, I love just being able to sit there and learn about
*  interesting, exciting things about Drosophila escape behavior and C. elegans, motor neurons,
*  that talks I would never go to otherwise, but always have some conceptual relationship to
*  something that I thought of once left right of center or even if they haven't, maybe they will
*  in the future. The other thing that's pretty clear about cosine is that the quality is extremely
*  high. It's certainly higher than the average quality as a fan, you're much less likely to be
*  wasting your time, I think, at cosine than you are as a fan. So I think it's mostly an exceptional
*  conference. I have not yet been to CCN. It's only two years old, I think. Yeah. The reason I've not
*  yet been to CCN, I think mostly is because I am a sort of devout cosine follower and at the same
*  time, I've had kids and so the idea of going to more than one similar conference hasn't seemed
*  possible. Yeah. I'm really looking forward to going to CCN. It may easily be more appropriate
*  for me than cosine in the future. The topics are exciting and the quality looks high. And it's been
*  set up in a really, really good way. So I think it'll be exciting. It's also the idea that it's
*  more cognitive than cosine is an interesting and exciting thing, particularly, I think, because
*  the modelling and AI community are really interested in the cognitive side as well,
*  which historically, I feel like hasn't been the case. They've been very interested in vision
*  models and in circuit models, which is why cosine was such a good venue for them before. And now,
*  I think CCN will end up being a really good venue for those people. So I've got one thing that I
*  hope doesn't happen. I wonder if it will or won't. But I really hope that CCN doesn't just
*  become the human cosine, right? Because humans are cognitive and other animals aren't. I mean,
*  I think there's some danger of that happening from both fronts, really. So I,
*  cosine used to be a good venue for human behaviour, used to be a good venue for
*  interesting new paradigms that start off in humans that might end up in rodents, for example.
*  So sometimes the best ones of those come from fMRI. Sometimes they just come from human behaviour.
*  But cosine used to be a good venue for that. And I thought it was really valuable because
*  if you're like me and you work across species, then you can show things that are relevant in
*  rodents, mechanistically level in rodents or monkeys and then show their relevance in humans.
*  Or you can develop tasks in humans where it's easier and then take it down to look for mechanism.
*  And sometimes you can even look for mechanism, some types of mechanisms in human imaging data,
*  I think. That's a different debate. But yeah, so I thought that that was a really valuable thing.
*  And I think that isn't really available to you anymore at cosine. I think just because of the
*  pool of reviewers and because of how competitive it is and also because of what's happening in the
*  rodent world with like the most important thing being the number of neurons you can record from
*  and or the size of your deep net or the particularly amazing genetic manipulation you can make.
*  So, I mean, this year, we sent our lab sent, I guess, eight or so abstracts in across different
*  species and models. And so some of them were rodent ones, some of them were modeling ones,
*  and some of them were human ones. And everything got in apart from the human ones,
*  even though in some cases, it was exactly the same task in the rodent in the human.
*  The results were finished and completed and looked beautiful in the human. And we're just
*  starting analyzing the data in the rodents. It doesn't matter that the human one just gets
*  rejected. And so I think that the cosine, that's a problem for cosine in the future. And if CCN
*  take that niche, then it's great for CCN. But we also think that it's really important that those
*  worlds don't lose each other. That's my view. And so I really hope it doesn't just split down
*  that axis. So I guess that's what I think. Cool. Hey, do you want to talk a little bit of science?
*  Yeah, okay. So some of your recent work here, let's start off, and we'll keep this in kind of
*  broader strokes. The Tolman Eichenbaum machine generalizing structural knowledge in the hippocampal
*  interrinal system. I think this is so cool that you name the model, the Tolman Eichenbaum machine
*  after Edward Tolman and Howard Eichenbaum, until I realized how much the acronym TEM sounds like
*  TEM. I mean, there's a TEM. Is this some sort of Hofstadter strange loop you've got going on or
*  what? No, we thought it was. So I mean, this is a paper, guys, that isn't called the Tolman
*  Eichenbaum machine in its published form. So it's a paper that you can find on archives and
*  it was at NIPS last year. Yeah, I'll link to it in the show notes.
*  But we're currently writing it for a journal and we're writing a more accessible version of it.
*  And part of that, so I've shown Paul where we are so far with writing this. And we're trying to
*  explain why it solves problems that were introduced by Tolman and Eichenbaum in a way that
*  also produces the famous spatial representations that have been measured by like O'Keefe and
*  and the Moses. There's three nods in that title. I don't know whether Paul noticed the last nod,
*  but there's a nod to the fact that Tolman invented the idea of cognitive maps in order. And when he
*  did so, he wasn't just talking about space. He was talking about a systematic organization
*  of knowledge that would cover all of life. And there's a nod to the fact that Eichenbaum
*  and colleagues have related that to the idea of relational memory, the idea that you can
*  form representations of memories as a way of providing that organization of knowledge.
*  And the third nod is to the way that the machine works and the level of abstraction,
*  which is very much related to how the Helmholtz machine works from Peter Diane and Jeff Henton
*  and Terry Sienkowski and how the sleep-wake algorithm works with learning generative models
*  and replaying from those generative models to learn recognition models. So it's a bit like a
*  version of the Helmholtz machine, but one that learns to control hippocampal-like memory so that
*  it learns how to build relational memories, which can then do one-shot memories that can remember
*  things straight away. Because they're relational memories that know about the structure of the
*  world, like the Helmholtz machine does a bit, they can also make inferences in zero-shot about what
*  other things should be around. And so we show that if you build a machine a bit like that,
*  you can make a formal analogy between relational memory and space. So that really formalizes
*  that. And this idea of understanding the structure of the relationships and abstracting the structure
*  of the relationships is one of the reasons you can do that. And the second thing that I think is
*  cool about it is that if you make a machine that learns these problems, then in these relational
*  memory style problems, it learns how to do transitive inference, or it can navigate social
*  graphs so it knows that your brother's father is your father, but your father's brother is your
*  uncle, and those kinds of things. And so it can make predictions about who on those kind of
*  relational graphs. But also it can learn spatial graphs. And when it does so, it can account for
*  a lot of the types of representations that we see in hippocampus and intervimal cortex. So for
*  example, it can produce grid cells and place cells, but critically it can account for what
*  happens when they remap across environments, for example. So there are really interesting properties
*  for how place cells appear to reorganize themselves, just randomly reorganize themselves,
*  so that neighbors in one environment are not neighbors in another environment. But grid cells
*  don't, they seem to just reorient. So they keep the same relational structure, which means they
*  can impose this structural knowledge on the new hippocampal map. And so those kinds of things
*  happen in the Torment Eichenbaum machine. It accounts for remapping really nicely.
*  Well, has it been thought that remapping occurs randomly and this
*  sort of shows that it's not random, that it does keep the structural integrity?
*  So I'll get to that in a second.
*  Oh, okay.
*  Yeah. The other types of things that you can account for, for example, are all of these other
*  types of cells that are recorded in the, that tend to be recorded in the system. Like for example,
*  boundary cells or band cells, even these recent things like object vector cells that were in,
*  that were recently in nature from the Moser group. And so you can show that even though what you,
*  if you're trying to figure out what the next thing is, if you're trying to predict the next,
*  the next thing you'll see, then if you're just randomly moving around, then you need to,
*  you need good cells to do that. But if you start assuming that your machine is a bit like a mouse
*  or a rat, and so it likes, for example, walking around walls, or it likes approaching objects,
*  then that changes the transition structure of the world. And then in order to build representations
*  of those, of those new transition structures, you need things like object vector cells,
*  and band cells, and boundary cells, and those kinds of stuff. So it can start, I think, to account in
*  one framework for lots of cell types that are being recorded in the entorhinal cortex and hippocampus,
*  but also what happens when you, when you, when you try to generalize that knowledge from one place to
*  another. And the last thing that it does, as you were saying, is it, in order to do this, it makes
*  predictions for a very particular way in which this structural information is transferred
*  between the hippocampus and the entorhinal cortex, the other way around, the entorhinal
*  cortex and the hippocampus. And then, and so we can go and record that in a couple of different
*  data sets now. So we can record, we can show that this remapping isn't truly, it isn't truly random.
*  And so information about the structural relationships is preserved between the
*  entorhinal cortex and the hippocampus. But instead of, instead of neighboring place cells
*  in one world moving to neighboring places in another world, what they'll do is they'll move
*  to another peak of the same grid cell, basically. And so that preserves all the structural information
*  that's present in the grid cells, but makes it look as though they randomly reshuffle.
*  So that's a prediction that's made from the model. And that's held up in some data. So yeah,
*  those are the kinds of things we're saying in the paper. Maybe that's too much detail.
*  No, you just ran through all my questions and answered them all pretty much.
*  Okay, sorry.
*  No, no, that's great. Well, so I have actually only two more questions about it. One is,
*  I know it's a work in progress, a manuscript in progress, but there's a notion in there that it
*  could benefit AI systems. And I'm wondering if you have a sense of how something like the
*  Tormann Eichenbaum machine might benefit AI systems.
*  Well, what it does is abstract stuff. It abstracts structural knowledge about tasks.
*  So one of the problems with AI these days is that it takes forever to learn. So these are super,
*  the deep learning nets are supervised learning mechanisms, and they start off as tabula rosa.
*  And you can't transfer learning. There's a lot of work on transfer learning, which is
*  taking a neural net and then trying to, on one task and trying to learn a new task. Is that
*  something with the generalization and the abstraction help in transfer learning, for instance?
*  So, I mean, the idea is to explain how abstract knowledge is transferred to constrain new
*  representations in our brain. I think that this problem of transfer learning and abstraction are
*  two big, these problems are big open problems in AI. I don't know whether these are the best
*  solutions to those problems. And other people work on those problems too. I think they're
*  interesting solutions. And I think that the fact that they predict the representations that we can
*  measure in the brain will be of interest to people that study these problems in AI.
*  I think that relational memory is not usually used in AI. So people who use memory systems in AI
*  tend to use random access memories. Even the people that are doing episodic meta-learning,
*  those kinds of things tend to use random access memories. And these content addressable relational
*  memories, I think that contain knowledge about the relationship between every event and every
*  other event. I think that might be an interesting avenue for AI. I don't by any means think that
*  the machines that we have built are solving problems that the AI people can't solve in
*  other ways. It's not built for that reason. It's built to try to understand how the hippocampal
*  system solves the problem. But it's definitely also the case that James Whittington, who built
*  this lovely model, I should have mentioned that earlier. And all these ideas are his really.
*  So he is about to start a deep mind. I don't think that he'll have to start thinking all over again.
*  Cool. Exactly. So that's a really good overview. And again, I'll point people to the manuscript
*  that's available. Is it archive or bio archive? So there's two manuscripts available online
*  showing it. So I apologize to everybody that they're both very technical so far,
*  the ones available online. There is an archive paper, which was also a paper at NIPS 2018.
*  So we now have a draft manuscript that's much easier to understand, but I guess it won't be
*  submitted for a month or so. And therefore, then it will start its process. It might end up on
*  bio archive at some stage before that. I see. Okay. So you think it's time to say Bob's your uncle
*  on this one? Bob's what? Did you bury that? Oh, you did bite on it. Was that intentional? So you
*  put this the relational work that might be James's joke that I've missed. Is it James's joke? Okay.
*  So you guys will have to when the manuscript does come out, you have to look up to see if you can.
*  I realize what you're talking about now. And I suspect that's a joke that James put in his.
*  So Paul is talking about a graph in our manuscript, which is a family tree
*  in which Bob is someone's uncle. And I'm afraid so far missed out on that hilarity that James
*  has put in there for us. Oh, gosh. Well, James, I hope I didn't get you in trouble there. You know,
*  so well done. No, James, I got it. Okay, well, so let's take a few minutes to talk about replay.
*  This is a manuscript you have in press at cell called human replay spontaneously reorganizes
*  experience. So replay as a phenomenon has been associated with a lot of different putative
*  roles, right, like systems memory consolidation, navigational planning, reinforcement learning,
*  you know, working memory, recall, but it was originally discovered in sleeping. I don't know
*  if it was mice or rats, but it was rodents after having run around mazes. What is so just what is
*  replay and how has the interpretation of it changed since its discovery? So replay is
*  representations that are measured during experience, then are then recapitulated
*  during rest much faster than they were experienced. Often this happens during so often these are
*  recorded in the hippocampus, or I don't think there's any reason to think that only exists in
*  the hippocampus. And often they happen during these events called shockwave ripples, in which
*  there is a lot of very high frequency power expressed in the LFP of the hippocampal LFP.
*  And you get this big ripple and at the same time you get play cells activating and they activate in
*  a particular sequence, which is a meaningful sequence given the previous activation of cells
*  when the animal was running on the track. And so given some memory that you've had of running on
*  the track is now being reactivated during, I mean, at the time it was sleep, but also happens in
*  waking rest. That's why people thought that it was important for memory consolidation.
*  I guess there's also there's evidence for that. More recently, there have been these ideas,
*  been evidence of playing out trajectories that where pieces of the trajectory have been experienced
*  before, but separately. And so you might one day you might run down one route and then not turn off
*  it to the right. And then a different day you might run down the another route at a crossroads
*  across the other way across the crossroads. And then you might replay the sort of right turn that
*  you never made. Right. And so to say, OK, what would it be like to go down that down there?
*  And so that's brought up those kinds of result have brought up this idea that directly replaying
*  experience might be sampling from a generative model of how you think the world works. And
*  obviously your experience is what you use to build that generative model. But you can also so you
*  don't just have to play your experiences because you can also use your all this prior knowledge you
*  have about how the world works and that I've been talking about with the organization of knowledge
*  to build these interesting generative models of how the world works. And so that's the kind of
*  recent idea. And we have been doing work along those lines. But I think the way in this in the
*  paper that you're about to see that we're about to talk about, I think it's a pretty dramatic
*  reorganization of experience and it's in humans and it's non-spatial. And so those three things
*  make it interesting because if this replay is really there in arbitrary non-spatial tasks,
*  it can maybe underlie some pretty profound obstructions and models that we think about
*  that are different from ones that the rodents have. Yeah. So traditionally replay has been
*  studied in and measured in rodents. It plays out in space. Yeah. Yeah. And like you said,
*  this work is in humans. So how do you do in humans? Well, I should start off given my failure to
*  highlight James Whittington early enough in the last section. I'm going to highlight Yunze Liu
*  from UCL who's a PhD student who's done most of the work and Zeb Kerr Nelson who's at DeepMind and
*  is just fantastic and also was the first person to think of this technique in a slightly different
*  situation when he was working with Peter Down and Ray Dolan who's also been involved in this work.
*  So you can do it with MEG. Effectively what you do is you show people a bunch of pictures
*  and you measure the representation of those pictures in the MEG sensors. And each one of
*  those pictures or things, objects that you show them will have a different representation in the
*  MEG sensors so that you can look at the MEG sensors and say, all right, he's thinking of a
*  horse now and a chair now and a car now. And then you organize these pictures into some
*  knowledge structure in the subject's mind. That might be putting them in a sequence
*  or in other situations, putting them in a more complicated knowledge structure.
*  So they have to learn the sequence or the knowledge structure.
*  Yeah, except so in most of what we do, they learn that knowledge structure
*  the day before with different stimuli. So and then they can, but humans are great because they learn
*  it in an abstract knowledge structure that will then apply to any set of stimuli that you give them.
*  And then after you've measured the representations of these new stimuli,
*  now you can go and measure, now you can go and put these new stimuli in these abstract knowledge
*  structures. And then now they have a new model that they can go sample from. But you can play
*  games whereby the samples from this new model will be in a completely different order from the
*  experience, the direct experience you gave them. So you could teach them day before,
*  okay, the third thing you see will be the second element in sequence two. And the first thing you'd
*  see will be the fourth element. I mean, it's really abstract template knowledge structure.
*  They can learn these things well. And then they replay out one, two, three, four, one, two, three,
*  four, which are they replay the sequences that come from the true structure of the world and
*  not the sequences that come from the thing, the order that they saw things in. But in order to
*  measure this replay, you just you can just let the subject rest. And then you can ask those
*  representations that I earlier measured of the horse and the chair and the house or whatever,
*  do any of those happen again, rest? And if they do, what order do they do they come in? And you
*  can see that yes, not only do they recapitulate during rest, but they do so in these sort of
*  streaks, which are sort of about 40 or 50 milliseconds apart very rapidly, just like they
*  are in rodents. And they occur in order ABCD, which are the order that's implied by the structure.
*  Lastly, they co-occur with bursts of power at shockwave ripple frequency that look like they're
*  coming from the hippocampus. And so it looks like you can measure shockwave ripples in humans,
*  that they happen at the same time as replay events in humans, and that these replay events
*  are able to dramatically reorganize experience according to these abstract knowledge structures
*  that we think are a bit like how grid cells organize facial knowledge. Yeah. So those are
*  the kinds of things that are in that paper. One of the other things that interesting about that paper
*  is because we're measuring from the whole brain, it seems like it's a big disadvantage not to have
*  cellular resolution. And often it seems that way to me. But I don't think it is in this case.
*  So most of replay has been measured in dorsal hippocampus, which has very particular
*  representations of conjunctive representations of place. So like place cells. And so you're not
*  quite sure what makes up those place cells. And in dorsal hippocampus, it's unlikely that you'll see
*  the sensory part of the representation or the structural part of the representation, et cetera,
*  et cetera. If you recall from the whole brain, you can maybe measure different representations
*  simultaneously. And so we can tell you something about what representations replay and when they
*  replay. And so we can show, for example, that not only do you see a sensory portion of the
*  representation, i.e. not only does the representation go horse, chair, shoe, hotel, the images replay,
*  but also there's an abstract replaying of that structural knowledge that happens just before
*  a few tens of milliseconds before the horse. And so the representations actually look like
*  play position one, okay, horse, play position two, okay, chair, play position three, hotel,
*  et cetera, et cetera. So the representation has this abstract portion, a bit like what a grid cell
*  will be. Show me what the sensory thing is at position x equals four, y equals two. Hippocampus
*  says, okay, it was a chair. And so, but having access to whole brain measurements means that
*  you can look at those different parts of the representation. I think it's been an interesting
*  thing. And we can show that those abstract portions, those structural portions of the
*  representation, they transfer across different sequences, right? So in the same way that grid
*  cells transfer their knowledge across different facial environments. And so you get the same
*  representation playing across different sequences in the structural portion, but then they're tied
*  to different sensory events. All right, guys, you guys can hear how excited he is about this stuff.
*  It's really fun to listen to. And I don't, do you know how many, do you have a sense when it's going
*  to be out? Well, we're just making the graphical abstract, which they have to do before they
*  publish stuff there. And then I don't know how long it takes to publish stuff. I've never published
*  that before. Anyway, you guys will have to, if you go to CCN in Berlin, there's a chance that you
*  actually get to see a talk about this work. Tim, I've kept you a long time. Do you mind if I ask
*  you just a few more general questions before I let you go? Sure. If you could wave a magic wand
*  and voila, have a skill or a new corpus of knowledge or something that would help you
*  further your research in some subject, what would it be? I don't know, man. Time travel?
*  What is that travel back or forward? Stretching time. So every day I can live twice.
*  That would be useful. I'd like to be better at maths than I am. I'd like to, but I'd like to,
*  I'm not sure I would want to be able to record or manipulate anything anymore. I feel like the
*  ability to make clever friends, I think, would be the most important one to have. I feel like I've
*  been lucky with that in the past, but not by any skill. But if I could find lots of friends that
*  can do all the manipulation and recording for me, that would be great. That's your job as a PI,
*  isn't it? Yeah, exactly. Yeah, that would be fun. I need more time and I need to be clever at
*  thinking stuff. Oh, here's a skill I'd like. I'd like to be able to think in high dimensions.
*  Oh, yeah. No one can do that. Yeah. It seems like anyone that can do that is going to be
*  good at neuroscience in the near future. Good luck with that. I'll send the magic wand your way.
*  What's something that you used to believe that you consider naive now? This can be about brains
*  or cognition or intelligence somewhere in the realm of neuroscience AI.
*  Something that I used to believe that I now consider naive. I don't know. I went through a
*  long portion of my life trying to understand mechanism without representation.
*  So I had a number of papers, which I'm still really proud of, but which frustrated me
*  because I was trying to figure out what the medial frontal cortex was doing, how it was
*  processing value, how it was processing competition, but not knowing what representations it was acting
*  on. For a long time, I was going across the most interesting part of the problem. I feel like
*  when I started trying to develop tools for understanding what those representations
*  looked like and why, even though we've nowhere near solved that problem, but it feels like
*  that's been a much richer, deeper problem to work with, to me anyway.
*  I have the sense that naiveté is an underrated attribute for people because otherwise, if you
*  don't have naiveté, you may not move forward on anything if you don't know about the topic. I don't
*  know if you have thoughts about that. Yeah. I definitely think that a lot of the most
*  interesting things are done, maybe wouldn't have been done by more experienced people at the time.
*  They seem like silly things to do. Yeah, exactly. If you knew, yeah, I'm sure that's true.
*  I know that you have kids, you don't have time, you're a busy scientist. I have been unable to
*  enjoy fictional books for a long time now. It's even hard for me to enjoy a movie because I
*  can't suspend my disbelief. When I read fiction, it seems like a complete waste of time.
*  What's a fictional book I should read? Well, I mean, I also am kids and therefore,
*  I haven't read a fiction book for a long time. Please don't say Charles Dickens. Nothing by
*  Charles Dickens. No. What was the last fiction book I read? That you enjoyed.
*  Oh, man. I probably haven't read fiction book that I'd be... So I have read some fiction books
*  recently, but I haven't read a fiction book that I would be anything other than embarrassed to
*  mention. The romance genre doesn't count. I've read a lot of crap fiction books
*  I haven't read a high quality fiction book. Well, the last high quality book I read was Wolf Hall,
*  which isn't even fiction. So I haven't read a book that I've intended to learn something from
*  for a very long time since before. I haven't either. Isn't that up John
*  Krakauer would say that's a big problem. Yeah, I'm sure that's right. I'm sure. I mean,
*  I just, I used to read a lot of deeply sort of worthy and important books and I thought that was
*  an important experience for me. And then I had kids and I stopped and I should do it again.
*  I'll tell you what my wife does. So my wife is, who's much cleverer and more worldly informed than
*  I am, reads important and thought provoking books every day on the way to work and on the underground.
*  And I just piss her on my phone. That's why I do.
*  You listen to important podcasts like Brain and Spy.
*  I play games on my phone, etc, etc. When I should be reading deep books, those are the only real
*  time I have for reading deep books. My example, someone, because someone asked me,
*  I get recommendations all the time and I just keep saying like, I just can't, I can't get into them.
*  But then I realized, oh, I'm reading to my children at night, you know, every other night,
*  because my wife and I switch off. And some of them are like Roald Dahl, you know, Charlie and
*  Chocolate Faggots. So maybe that counts a little bit. I don't know.
*  You're a different stage from me, man. Like, like literally, I'm aware is my hat. That's what I'm
*  reading to my kids. Yeah, boy, that's a rough stage. Yeah, at least there's some plot lines coming up
*  in your life. There will be some plot lines. I mean, I will start reading again. It's not, I'm
*  not, I mean, I am mostly a completely incompetent, illiterate, ineducated, but, but like, I have read
*  some stuff before in my life and I will one day again, but I'm not doing anything, any reading now.
*  I just look forward to when it's enjoyable to me again, or when that's what I would just want one
*  good fictional work that'll draw me in. Last question here. So I do have Nathaniel
*  Dahl coming on the show. He's one of the keynote speakers and he does a lot of work in replay.
*  Any message you'd like me to pass along to Nathaniel when I speak with him?
*  As long as you make him look as stupid as he is, that's, that's, sorry.
*  Perfect. No, no, Nathaniel is a wonderful, inspiring, thoughtful friend. He's fantastic.
*  He's, I mean, he is. So, yeah, I mean, like a lot of my work, as everyone will know, a lot of my work
*  is inspired by a lot of his work and he is a clever cookie. Tim, it's been great having you again. I
*  just realized that in another four months it will be Berlin time, CCN time. So hopefully I'll get out
*  there and I'll get to see you and talk to you in another four months. Okay, cool. Excellent. It's
*  a regular thing. Thanks, man.
*  Bye.
*  you

---
Date Generated: April 13, 2024
Transcription Model: whisper medium 20231117
Length: 5326s
Video Keywords: ['dan kokotov', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 73213
Video Rating: None
---

# Dan Kokotov: Speech Recognition with AI and Humans | Lex Fridman Podcast #151
**Lex Fridman:** [January 04, 2021](https://www.youtube.com/watch?v=yTWa-Z1UQwU)
*  The following is a conversation with Dan Kokotov, VP of engineering at Rev.ai,
*  which is by many metrics, the best speech-to-text AI engine in the world.
*  Rev, in general, is a company that does captioning and transcription of audio by humans
*  and by AI. I've been using their services for a couple years now and planning to use Rev
*  to add both captions and transcripts to some of the previous and future episodes of this podcast
*  to make it easier for people to read through the conversation or reference various parts of the
*  episode since that's something that quite a few people requested. I'll probably do a separate
*  video on that with links on the podcast website so people can provide suggestions and improvements
*  there. Quick mention of our sponsors. Athletic Greens, all-in-one nutrition drink, Blinkist app,
*  summarizes books, Business Wars podcast, and Cash app. So the choice is health, wisdom, or money.
*  Choose wisely, my friends. And if you wish, click the sponsor links below to get a discount and to
*  support this podcast. As a side note, let me say that I reached out to Dan and the Rev team for a
*  conversation because I've been using and genuinely loving their service and really curious about how
*  it works. I previously talked to the head of Adobe Research for the same reason. For me,
*  there's a bunch of products, usually software, that comes along and just makes my life way easier.
*  Examples are Adobe Premiere for video editing, iZotope RX for cleaning up audio,
*  Auto Hotkey on Windows for automated keyboard and mouse tasks, Emacs as an ID for everything,
*  including the universe itself. I can keep on going, but you get the idea. I just like talking
*  to people who create things I'm a big fan of. That said, after doing this conversation, the folks at
*  Rev.ai offered to sponsor this podcast in the coming months. This conversation is not sponsored
*  by the guest. It probably goes without saying, but I should say it anyway, that you cannot buy your
*  way onto this podcast. I don't know why you would want to. I wanted to bring this up to make a
*  specific point that no sponsor will ever influence what I do on this podcast or to the best of my
*  ability, influence what I think. I wasn't really thinking about this. For example, when I interviewed
*  Jack Dorsey, who is the CEO of Square that happens to be sponsoring this podcast, but I should really
*  make it explicit. I will never take money for bringing a guest on. Every guest on this podcast
*  is someone I genuinely am curious to talk to or just genuinely love something they've created.
*  As I sometimes get criticized for, I'm just a fan of people and that's who I talk to. As I also talk
*  about way too much, money is really never a consideration. In general, no amount of money
*  can buy my integrity. That's true for this podcast and that's true for anything else I do.
*  If you enjoy this thing, subscribe on YouTube, review on the Apple podcast, follow on Spotify,
*  support on Patreon, or connect with me on Twitter at Lex Friedman. And now here's my conversation
*  with Dan Kokotov. You mentioned science fiction on the phone, so let's go with the ridiculous
*  first. What's the greatest sci-fi novel of all time in your view? And maybe what ideas do you
*  find philosophically fascinating about it? The greatest sci-fi novel of all time is Dune,
*  and the second greatest is The Children of Dune, and the third greatest is The God Emperor of Dune.
*  I'm a huge fan of the whole series. It's just an incredible world that he created. I don't know if
*  you've read the book or not. No, I have not. It's one of my biggest regrets, especially because a
*  new movie is coming out. Everyone's super excited about it. It's ridiculous to say,
*  and sorry to interrupt, is that I used to play the video game, it used to be Dune. I guess you
*  would call that real-time strategy. Right, right. I think I remember that game. Yeah, it was kind
*  of awesome, 90s or something. I think I played it actually when I was in Russia. I definitely remember
*  it. I was not in Russia anymore. I think at the time that I used to live in Russia, I think
*  video games were about the specification of Pong. I think Pong was pretty much the greatest game I
*  ever got to play in Russia, which was still a privilege in that age. So you didn't get color?
*  You didn't get like... Well, so I left Russia in 1991. 1991, okay. So I was one of the few
*  lucky kids because my mom was a programmer. So I would go to her work. I would take the metro.
*  I got her work and play like on, I guess the equivalent of like a 286 PC, you know?
*  Nice, with floppy disks. Yes. So okay, back to Dune.
*  Back to Dune. And by the way, the new movie I'm pretty interested in, but
*  the original... You're skeptical?
*  I'm a little skeptical. I'm a little skeptical. I saw the trailer. I don't know. So there's a David
*  Lynch movie, Dune, as you may know. I'm a huge David Lynch fan, by the way. So the movie is
*  somewhat controversial, but it's a little confusing, but it captures kind of the mood of the
*  book better than I would say most any adaptation. And like Dune is so much about kind of mood and
*  the world, right? But back to the philosophical point. So in the fourth book, God Emperor of Dune,
*  there's a sort of setting where Leto, one of the characters, he's become this weird sort of
*  God Emperor. He's turned into a gigantic worm. I mean, you kind of have to read the book to
*  understand what that means. So the worms are involved.
*  Worms are involved. You probably saw the worms in the trailer, right?
*  And in the video. So he kind of like merges with this
*  worm and becomes this tyrant of the world and like oppresses the people for a long time, right? But
*  he has a purpose. And the purpose is to kind of break through kind of a stagnation period
*  in civilization, right? But people have gotten too comfortable, right? And so he kind of
*  oppresses them so that they explode and like, go on to colonize new worlds and kind of renew
*  the forward momentum of humanity, right? And so to me, that's kind of like fascinating, right?
*  You need a little bit of pressure and suffering, right? To kind of like make progress, not get
*  too comfortable. Maybe that's a bit of a cruel philosophy to take away.
*  That seems to be the case, unfortunately. Obviously I'm a huge fan of suffering.
*  So one of the reasons we're talking today is that a bunch of people requested that
*  I do transcripts for this podcast and do captioning. I used to make all kinds of YouTube videos
*  and I would go on Upwork, I think, and I would hire folks to do transcription.
*  And it was always a pain in the ass from being honest. And then I don't know how I discovered Rev,
*  but when I did, it was this feeling of like, holy shit, somebody figured out how to do it just
*  really easily. I'm such a fan of just when people take a problem and they just make it easy.
*  There's so many things in life that you might not even be aware of that are painful.
*  Then Rev, you just give the audio, give the video, you can actually give a YouTube link,
*  and then it comes back a day later or two days later, whatever the hell it is, with the captions.
*  All in a standardized format. It was truly a joy. I thought I had, just for the hell of it,
*  talk to you. It just made my soul feel good. One other product I've used like that
*  is for people who might be familiar, called iZotope RX. It's for audio editing.
*  And that's another one where it was like, you just drop it. I dropped in the audio and it just
*  cleans everything up really nicely. All the stupid, the mouth sounds and sometimes there's
*  background sounds due to the malfunction of the equipment, it can clean that stuff up.
*  It has a general voice denoising. It has automation capabilities where you can do
*  batch processing and you can put a bunch of effects. I mean, it just, I don't know.
*  Everything else sucked for voice-based cleanup that I've ever used. I've used Audition,
*  Adobe Audition. I've used all kinds of other things with plugins. You have to figure it all
*  out. You have to do it manually. Here, it just worked. That's another one in this whole pipeline
*  that just brought joy to my heart. Anyway, all that to say is Rev put a smile to my face.
*  So Kimi, you maybe take a step back and say, what is Rev and how does it work? And Rev or rev.com?
*  Rev, rev.com. Same thing, I guess. We do have rev.ai now as well, which we can talk about later.
*  Like, do you have the actual domain or is it just...
*  The actual domain, but we also use it kind of as a sub-brand. So we use rev.ai to denote our
*  ASR services. Rev.com is kind of our more human and to the end user services.
*  So it's like WordPress.com and WordPress.org. They actually have separate brands that,
*  I don't know if you're familiar with what those are. They provide almost like a separate branch of...
*  A little bit. I think with that, it's like, WordPress.org is kind of their open source,
*  and WordPress.com is sort of their hosted commercial offering. With us, the
*  differentiation is a little bit different, but maybe a similar idea.
*  Okay. So what is Rev? Before I launch into what is Rev,
*  I was going to say, you're talking about Rev was music to your ears. Your spiel was music to my
*  ears. To us, the founders of Rev, because Rev was kind of founded to improve on the model of
*  Upwork. That was kind of their original, or part of their original impetus. Our CEO, Jason,
*  was an early employee of Upwork. So he was very familiar with their...
*  Upwork the company.
*  Upwork the company. And so he was very familiar with that model and he wanted to make the whole
*  experience better because he knew like when you go... At that time, Upwork was primarily programmers.
*  So the main thing they offered is if you want to hire someone to help you code a little site,
*  you could go on Upwork. You could browse through a list of freelancers, pick a programmer, have a
*  contract with them and have them do some work. But it was kind of a difficult experience because
*  for you, you would kind of have to browse through all these people. And you have to decide, okay,
*  well, is this guy good or is somebody else better? And naturally, you're going to Upwork because
*  you're not an expert. If you're an expert, you probably wouldn't be getting a programmer from
*  Upwork. So how can you really tell? So there's a lot of potential regret. What if I choose a bad
*  person? They're going to be late on the work. It's going to be a painful experience. And for
*  the freelancer, it was also painful because half the time, they spent not on actually doing the
*  work but kind of figuring out how can I make my profile most attractive to the buyer. They're not
*  an expert on that either. So Rob's idea was let's remove the barrier. Let's make it simple. We'll
*  pick a few verticals that are fairly standardizable. We actually started with translation and then we
*  added audio transcription a bit later. And we'll just make it a website. You go, give us your files.
*  We'll give you back the results as soon as possible. Originally, maybe it was 48 hours. Then we made it
*  shorter and shorter and shorter. There's a rush processing too. There's a rush processing now.
*  And we'll hide all the details from you. That's exactly what you're experiencing.
*  You don't need to worry about the details of how the sausage is made. That's really cool.
*  So you picked a vertical. By vertical, you mean basically a service category.
*  Why translation? Is Rev thinking of potentially going into other verticals in the future?
*  Or is this the focus now is translation, transcription, language?
*  The focus now is language or speech services, generally speech to text,
*  language services. You can kind of group them however you want.
*  Originally, the categorization was work from home. So work that was done by people on the
*  computer. We weren't trying to get into task rabbit type of things. And something that could
*  be relatively standard, not a lot of options. So we could kind of present the simplified interface.
*  So programming wasn't a good fit because each programming project is kind of unique.
*  We're looking for something that transcription is, you have five hours of audio, it's five
*  hours of audio. Translation is somewhat similar in that you can have a five-page document and then
*  you just price it by that. And then you pick the language you want and that's mostly all it is to
*  it. So those were a few criteria. We started with translation because we saw the need and
*  we picked up kind of a specialty of translation where we would translate things like board
*  certificates, immigration documents, things like that. And so they were fairly,
*  even more well-defined and easy to kind of tell if we did a good job.
*  You can literally charge per type of document. So what is it now? Is it per word or something
*  like that? How do you measure the effort involved in a particular thing?
*  So now for audio transcription, it's per audio unit.
*  For translation, we don't really actually focus on it anymore. But back when it was still a main
*  business of rabbit was per page or per word, depending on the kind of...
*  Because you can also do translation now on the audio, right?
*  Like subtitles. So it would be both transcription and translation. That's right.
*  I wanted to test the system to see how good it is. Is Russian supported?
*  Think so. Yeah. It'd be interesting to try it out.
*  But now it's only in the one direction. So you start with English and then you can have subtitles
*  in Russian. Not really the other way. Got it. Because I'm deeply curious about this.
*  When COVID opens up a little bit, when the economy, when the world opens up a little bit.
*  You want to build your brand in Russia? No, I don't. First of all, I'm allergic to the
*  word brand. I'm definitely not building any brands in Russia. But I'm going to Paris
*  to talk to the translators of Dostoevsky and Tolstoy. There's this famous couple that does
*  translation. And I'm more and more thinking of how is it possible to have a conversation
*  with a Russian speaker? Because I have just some number of famous Russian speakers that I'm
*  interested in talking to. And my Russian is not strong enough to be witty and funny. I'm already
*  an idiot in English. I'm an extra level of like awkward idiot in Russian, but I can understand it.
*  And I also wonder how can I create a compelling English Russian experience for an English
*  speaker? There's a guy named Grigori Perlman who's a mathematician who obviously doesn't
*  speak any English. So I would probably incorporate a Russian translator into the picture.
*  And then it would be like a, not to use a weird term, but like a three, like a three,
*  three person thing where it's like a dance of like, I understand it one way. They don't
*  understand the other way, but I'll be asking questions in English. I don't know. I don't know
*  the right way. It's complicated, but I feel like it's worth the effort for certain kinds of
*  people. One of whom I'm confident is Vladimir Putin. I'm for sure talking to, I really want
*  to make it happen because I think I could do a good job with, but the right, you know,
*  understanding the fundamentals of translation is something I'm really interested in. So that's
*  why I'm starting with the actual translators of like Russian literature, because they understand
*  the nuance and the beauty of the language and how it goes back and forth. But I also want to see
*  like in speech, how can we do it in real time? So that's, that's like a little bit of a baby
*  project that I hope to push forward. But anyway, it's a challenging thing. So just to share,
*  my dad actually does translation, not, not professional. He's a, he writes poetry.
*  That was kind of always his, not a hobby, but he's, he's, you know, he had a job, like a
*  day job, but his passion was always writing poetry. And then we got to America and like,
*  he started also translating, first he was translating English poetry to Russian. Now
*  he also goes the other, the other way. You kind of gain some small fame in that world anyways,
*  because recently this poet, like Lewis Clark, I don't know if you know, some American poet,
*  she was awarded the Nobel Prize for Literature. And so my dad had translated
*  one of her books of poetry into Russian. He was like one of the few. So you kind of like,
*  they asked him and gave an interview to Radio Svoboda, if you know what that is. And he kind
*  of talked about some of the intricacies of translating poetry. So that's like an extra
*  level of difficulty, right? Because translating poetry is even more challenging than translating,
*  just, you know, it's interviews. Do you remember any, any experiences and challenges to having to
*  do the translation that that's the got to you, like something he's talked about? I mean, a lot
*  of it, I think is word choice, right? It's the way Russian is structured is first of all quite
*  different than the way English is structured, right? Just there is inflections in Russian and
*  gender as they don't exist in English. One of the reasons actually why machine translation is
*  quite difficult for English to Russian and Russian to English because they're such different
*  languages. But then English has like a huge number of words, many more than Russian actually,
*  I think. So it's often difficult to find the right word to convey the same emotional meaning.
*  Yeah, Russian language, they play with words much more.
*  So you're mentioning that Rev was kind of born out of trying to take a vertical on upwork and then
*  standardize it. So I just kind of make the freelancer marketplace idea better, right?
*  Better for both customers and better for the freelancers themselves. Is there something else
*  to the story of Rev finding Rev? Like what did it take to bring it actually to life? Was there any
*  pain points? Plenty of pain points. I mean, as often the case, it's with scaling it up, right?
*  And in this case, the scaling is kind of scaling the marketplace, so to speak. Rev is essentially
*  a two-sided marketplace, right? Because there's the customers and then there's the Revvers.
*  If there's not enough Revvers, Revvers are real-color freelancers. So if there's not
*  enough Revvers, then customers have a bad experience, right? It takes longer to get
*  your work done, things like that. If there's too many, then Revvers have a bad experience
*  because they might log on to see what work is available and there's not very much work, right?
*  So kind of keeping that balance is a quite challenging problem and that's a problem we've
*  been working on for many years and we're still refining our methods, right?
*  If you can kind of talk to this gig economy idea, I did a bunch of different psychology
*  experiments on Mechanical Turk, for example. I've asked to do different kinds of very tricky
*  computer vision annotation on Mechanical Turk and it's connecting people in a more systematized way.
*  I would say between task and what would you call that? Worker is what Mechanical Turk calls it.
*  What do you think about this world of gig economies, of there being a certain kind of
*  there being a service that connects customers to workers in a way that's massively distributed,
*  potentially scaling to, it could be scaled to like tens of thousands of people, right?
*  Is there something interesting about that world that you can speak to?
*  Yeah, well we don't think of it as kind of gig economy. To some degree,
*  I don't like the word gig that much, right? Because to some degree it diminishes
*  the work being done, right? It sounds kind of like almost amateurish. Well, maybe in like
*  music industry, like gig is a standard term, but in work it kind of sounds like it's frivolous.
*  To us, it's improving the nature of working from home on your own time and on your own terms,
*  right? And kind of taking away geographical limitations and time limitations, right?
*  So many of our freelancers are maybe work-from-home moms, right? And they don't want the traditional
*  nine-to-five job, but they want to make some income. And Rev kind of allows them to do that
*  and decide exactly how much to work and when to work. Or by the same token, maybe someone wants to
*  live the mountaintop life, right? Cabin in the woods, but they still want to make some money.
*  And generally that wouldn't be compatible before this new world. You kind of have to choose. But
*  with Rev, you feel like you don't have to choose. Can you speak to what's the demographics,
*  distribution, where do Revvers live? Is it from all over the world? Do you have a sense of
*  what's out there? From all over the world, most of them are in the US. That's the majority.
*  Because most of our work is audio transcription, and so you have to speak pretty good English.
*  So the majority of them are from the US, so we have people in some other of the English-speaking
*  countries. And as far as like US, it's really all over the place. For some of the years now,
*  we've been doing these little meetings where the management team will go to some place and
*  we'll try to meet Revvers. And pretty much wherever we go, it's pretty easy to find
*  a large number of Revvers. The most recent one we did was in Utah. But anywhere, really.
*  Are they from all walks of life, these young folks, older folks?
*  Yeah, all walks of life, really. Like I said, one category is the work from home, students who want
*  to make some extra income. There are some people who maybe have some social anxiety, so they don't
*  want to be in the office, and this is one way for them to make a living. So it's really pretty
*  wide variety. But on the flip side, for example, one Revver we were talking to was a
*  person who had a fairly high-powered career before and was kind of taking a break.
*  She was almost doing this just to explore and learn about the gig economy, quote unquote.
*  So it really is a pretty wide variety of folks.
*  Yeah, it's kind of interesting through the captioning process for me to learn about the
*  Revvers because some are clearly weirdly knowledgeable about technical concepts.
*  You can tell by how good they are at capitalizing stuff,
*  technical terms, like in machine learning and deep learning. I've used Rev to annotate,
*  to caption the deep learning lectures or machine learning lectures I did at MIT. And it's funny,
*  a large number of them were like, I don't know if they looked it up or were already knowledgeable,
*  but they do a really good job. They invest time into these things. They will do research,
*  they will Google things to kind of make sure they get it right. But to some of them, it's actually
*  part of the enjoyment of the work. They'll tell us, I love doing this because I get paid to watch a
*  documentary on something and I learn something while I'm transcribing. Pretty cool.
*  Yeah. So what's that captioning transcription process look like for the Revver? Can you maybe
*  speak to that to give people a sense? Like how much is automated, how much is manual,
*  what's the actual interface look like, all that kind of stuff?
*  Yeah. So we've invested a pretty good amount of time to give our Revvers the best tools possible.
*  So typical day forever, they might log into their workspace, they'll see a list of
*  audios that need to be transcribed. And we try to give them tools to pick specifically the ones
*  they want to do. So maybe some people like to do longer audios or shorter audios.
*  People have their preferences. Some people like to do audios in a particular subject or from
*  a particular country. So we try to give people the tools to control things like that. And then when
*  they pick what they want to do, we'll launch a specialized editor that we've built to make
*  transcription as efficient as possible. They'll start with a speech-rec draft. So we have our
*  machine learning model for automated speech recognition. They'll start with that. And then
*  our tools are optimized to help them correct that. So it's basically a process of correction.
*  Yeah. It depends on, I would say the audio. If audio itself is pretty good, like probably like
*  our podcast right now would be quite good. So they would do a fairly good job. But if you
*  imagine someone recorded a lecture, you know, in the back of a auditorium, right? Where like the
*  speaker is really far away and there's maybe a lot of crosstalk and things like that, then maybe they
*  wouldn't do a good job. So the person might say like, you know what, I'm just going to do it from
*  scratch. Yeah. So it kind of really depends. What would you say is the speed that you can possibly
*  get? Like what's the fastest? Can you get, is it possible to get real time or no? As you're like
*  listening, can you write as fast as? Real time would be pretty difficult. It's actually a pretty,
*  it's not an easy job. You know that we actually encourage everyone at the company to try to be a
*  transcriber for a day, transcriptionist for a day. And it's way harder than you might think it is,
*  right? Because people talk fast and people have accents and all this kind of stuff. So real time
*  is pretty difficult. Is it possible? Like there's somebody, we're probably going to use Rev
*  to caption this. They're listening to this right now. What's, what's, what do you think is the
*  fastest you could possibly get on this right now? I think on a good audio, maybe two to three X,
*  I would say, real time. Meaning it takes two to three times longer than the actual audio of the,
*  of the podcast. This is, this is so meta. I could just imagine the Revvers working on this right
*  now. You're way wrong. You're way wrong. This takes way longer, but yeah, definitely. You doubted me.
*  Okay. So you mentioned ASR. Can you speak to what is ASR? Automatic speech recognition?
*  How much, like what is the gap between perfect human performance and perfect or pretty damn good
*  ASR? Yeah. So it's our automatic speech recognition. It's a class of machine learning problem,
*  right? To take, you know, speech, like we were talking and transform it into a sequence of
*  words, essentially. Audio of people talking. Audio, audio to words. And, you know, there's a variety
*  of different approaches and techniques, which we could talk about later if you want. So, you know,
*  we think we have pretty much the world's best ASR for this kind of speech, right? So there's,
*  there's different kinds of domains, right? For ASR, like one domain might be voice assistants,
*  right? So Siri, very different than what we're doing, right? Because Siri, there's fairly limited
*  vocabulary. You know, you know, you might ask Siri to play a song or, you know, order a pizza or
*  whatever. And it's very good at doing that. Very different from when we start talking in a very
*  unstructured way. And Siri will also generally like adapt to your voice and stuff like this.
*  So for this kind of audio, we think we have the best. And our accuracy,
*  right now, I think it's maybe 14% word error rate on our test suite that we generally use to measure.
*  So word error rate is like one way to measure accuracy for ASR, right?
*  So what's 14% word error rate?
*  So 14% means across this test suite of a variety of different audios,
*  it would be, it would get in some way 14% of the words wrong. 14% of the words wrong.
*  Yep. So the way you kind of calculate it is you might add up insertions, deletions,
*  and substitutions, right? So insertions is like extra words. Deletions are words that we said, but
*  weren't in the transcript, right? Substitutions is, you said apple, but I said, but they are
*  thought it was able something like this. Human accuracy, most people think realistically, it's
*  like 3% to 2% word error rate would be like the max achievable. So there's still quite a gap,
*  right? Would you say that, so YouTube, when I upload videos often generates automatic captions.
*  Are you sort of from a company perspective, from a tech perspective, are you trying to beat YouTube?
*  Google, it's a hell of a, Google, I mean, I don't know how seriously they take this task,
*  but I imagine it's quite serious. And they, you know, Google is probably up there in terms
*  of their teams on, on ASR or just NLP, natural language processing, different technologies.
*  So do you think you can beat Google on this kind of stuff? Yeah, we think so.
*  Google just woke up on my phone.
*  This is hilarious. Okay.
*  Now Google is listening, sending it back to headquarters. Who are these rough people?
*  But that's the goal?
*  No, yeah, I mean, we measure ourselves against like Google, Amazon, Microsoft, you know,
*  some of the, some smaller competitors. And we use like our internal tests with it. We try to compose
*  it of a pretty representative set of audience. Maybe it's some podcasts, some videos, some
*  interviews, some lectures, things like that. Right. And we beat them in our own testing.
*  And actually Rev offers automated, like you can actually just do the automated captioning.
*  So like, I guess it's like way cheaper, whatever it is, whatever the rates are.
*  Yeah. Yeah. So it's a, by the way, it used to be a dollar per minute for captioning and transcription.
*  I think it's like a dollar 15 or something like that.
*  Uh, $1.25 now. Yeah. It's pretty, it's pretty cool. That was the other thing that was surprising to me.
*  It was actually like the cheapest thing you could one of the, I mean, I don't remember it being
*  cheaper. You could on upward get cheaper, but it was clear to me that this, that's going to be really
*  shitty. Yeah. So like you're also competing on price. I think there were words that were
*  like, I don't know, I don't know, I don't know. I don't know. I don't know. I don't know. I don't
*  know. I don't know. I don't know. I don't, I don't know. I think they were services that you can get
*  like similar to Rev kind of, um, feel to it, but it wasn't as automated like the drag and drop,
*  the entirety of the interface. It's like the thing we're talking about. I'm such a huge fan
*  of like frictionless, like, uh, Amazon's single, uh, by button, whatever that one click, the one
*  That's genius right there.
*  Like that is so important for services.
*  Yeah.
*  That simplicity.
*  And I mean, rev is, is, uh, almost there.
*  I mean, there's like some, I'm trying to think.
*  So I, I think I've, uh, I stopped using, uh, this pipeline, but rev offers it
*  and that I like it, but it was causing me some issues, uh, on my side, which
*  is, um, you can connect it to like Dropbox and it generates the files and Dropbox.
*  So like it, it, it, it closes the loop to where I don't have to go to rev
*  at all and I can download it.
*  Uh, sorry, I don't have to go to rev at all and to download the files.
*  It could just like automatically copy them.
*  You put in your Dropbox and a day later or maybe a few hours later,
*  depending on the gig and rush just shows up.
*  Yeah.
*  Yeah.
*  I was trying to do it programmatically too.
*  Is there an API interface you can, I was trying to through like, through
*  Python to download stuff automatically.
*  But then I realized this is the programmer in me.
*  Like, dude, you don't need to automate everything like in life, like flawlessly.
*  Cause I wasn't doing enough captions to justify to myself the time investment
*  into automating everything perfectly.
*  Yeah.
*  I would say if, uh, if you're doing so many interviews that your biggest road
*  block is, uh, clicking on the rough download, but now you're talking about
*  Musk levels of business.
*  But for sure we have like a variety of ways to make it easy.
*  You know, there's the integration you mentioned, I think it's through a
*  company called Zapier, which kind of can connect, um, Dropbox to rev and, uh,
*  vice versa, we have an API if you want to really like customize it, you know,
*  if you want to create the Lex Friedman, you know, uh, CMS or, or whatever.
*  But this whole thing.
*  Okay, cool.
*  So can you speak to the, the ASR a little bit more?
*  Like, what is it?
*  Uh, what does it take like approach wise machine learning wise?
*  How hard is this problem?
*  How do you get to the 3% error rate?
*  Like, what's your vision of all of this?
*  Yeah.
*  Well, the 3% rate error rate is definitely that's, that's the grand vision.
*  Um, we'll see what it takes to get there.
*  Um, but we believe, you know, in, in ASR, the biggest thing is the data, right?
*  Like, that's true of like a lot of machine learning problems today, right?
*  The more data you have and high quality, the data, the better label the data.
*  Um, yeah, that's how you get good results.
*  And we had Rev have kind of like the best data like we have.
*  Thank you.
*  You're literally, your, your literal model is annotating the data.
*  Our business model is being paid to annotate data.
*  Uh, so it's kind of like a pretty magical flywheel.
*  Yeah.
*  And so we've kind of like ridden this flywheel to, to, to this point.
*  Um, and we think we're still kind of in the early stages of figuring out all the
*  parts of the flywheel to use, you know, because we have the final transcripts.
*  Um, and we have the, um, the audios and we train on that, but we in principle
*  also have all the edits that the Revvers make, right?
*  Um,
*  Oh, that's interesting.
*  How can you use that as data?
*  We, we had, that's, that's something for us to figure out in the future, but
*  you know, we feel like we're only in the early stages, right?
*  So the data, but the data is there.
*  That'd be interesting.
*  Like, uh, almost like recurrent neural net for fixing, for fixing transcripts.
*  I always remember we did a segmentation annotation for, uh, for driving data.
*  So it's segmenting the scene, like visual data and you can get all, so it was
*  drawing people were drawing polygons around different objects and so on.
*  And it feels like it always felt like there was a lot of information in the
*  clicking, the sequence of clicking that people do, the kind of fixing of the
*  polygons that they do.
*  Now there's a few papers written about how to draw polygons, like with a
*  recurrent neural nets to try to learn from the human clicking, but it was just
*  like experimental, you know, it was one of those like CVPR type papers that
*  people do like a really tiny data set.
*  It didn't feel like people really try to do it seriously.
*  Yeah.
*  I wonder, I wonder if there's information in the fixing that's high, that, that
*  provides deeper set of signal than just like the raw data.
*  The intuition is for sure.
*  There must be, right?
*  It must be in all kinds of signals and how long you took to, you know, make
*  that edit and stuff like that.
*  And it's going to be like up to us.
*  That's why like the next couple of years is like super exciting for us.
*  Right.
*  So that's what like the focus is now is you mentioned Rev.ai.
*  That's where you want to.
*  Yeah.
*  So Rev.ai is kind of our way of bringing this ASR to, you know, the rest of the
*  world, right?
*  So when we started, we were human only, you know, then we kind of created this
*  Temi service.
*  I think you might've used it, which was kind of ASR for the consumer.
*  Right.
*  So if you don't want to pay a dollar 25, but you want to pay now it's 25 cents
*  a minute, I think, and you get there the transcript, the machine generated
*  transcript, you get an editor and you can kind of fix it up yourself.
*  Right.
*  Then we started using the ASR for our own human transcriptionists.
*  And then the kind of Rev.ai is the final step of the journey, which is, you know,
*  we have this amazing engine.
*  What can people build with it?
*  Right.
*  What kind of new applications could be enabled if you have
*  SpeedTrack that's that accurate?
*  Do you have ideas for this or is it just providing it as a service and seeing
*  what people come up with?
*  It's providing it as a service and seeing what people come up with and kind
*  of learning from what people do with it.
*  And we have ideas of our own as well, of course, but it's a little bit like, you
*  know, when AWS provided the building blocks, right.
*  And they saw what people built with it and they try to make it easier to build
*  those things, right.
*  And we kind of hope to do the same thing.
*  Although AWS kind of does a shitty job of like, I'm continually surprised
*  like Mechanical Turk, for example, how shitty the interface is.
*  We're talking about like Rev making me feel good.
*  Like when I first discovered Mechanical Turk, the initial idea of it was like,
*  it made me feel like Rev does, but then the interface is like, come on.
*  Yeah, it's horrible.
*  Why, why is it so painful?
*  Does nobody at Amazon want to like seriously invest in it?
*  Felt like you can make so much money if you took this effort seriously.
*  And it feels like they have a committee of like two people just sitting back,
*  like, like a meeting.
*  They meet once a month.
*  Like, what are we going to do with Mechanical Turk?
*  It's like two websites make me feel like this, that and craiglist.org,
*  whatever the hell it is.
*  It feels like it's designed in the nineties.
*  Well, Craigslist basically hasn't been updated pretty much since the guy
*  originally built.
*  Do you seriously think there's a team, like how big is the team
*  working on Mechanical Turk?
*  I don't know.
*  There's some team, right?
*  I feel like there isn't.
*  I'm skeptical.
*  Yeah.
*  Well, if nothing else, they benefit from, you know, the other teams, like
*  moving things forward, right?
*  In a small way.
*  Possibly.
*  But I know what you mean.
*  We do, we, we use Mechanical Turk for a couple of things as well.
*  And yeah, it's painful.
*  Yeah, it's painful, but yeah, it works.
*  I think most people, the thing is most people don't really use the UI, right?
*  Like, so like we, for example, we use it through the API, right?
*  So, yeah, but even the API documentation and so on, like it's super outdated.
*  Like, yeah, it's, I don't, I don't even know what to, I mean, the same,
*  my same criticism, as long as we're ranting, my same criticism goes to the
*  APIs of most of these companies at Google, for example, the API for the
*  different services is just the documentation is so shitty.
*  Like it's not so shitty.
*  I should, I should actually be, uh, I should exhibit some gratitude.
*  Okay.
*  Let's practice some gratitude.
*  The, the, you know, the documentation is pretty good.
*  Like most of the things that the API makes available is pretty good.
*  It's just that in the sense that it's accurate, sometimes outdated, but like
*  the degree of explanations with examples is only covering, I would say like
*  50% of what's possible and it just feels a little bit like there's a lot of
*  natural questions that people would want to ask that doesn't, uh, doesn't get
*  covered and it feels like it's almost there.
*  Like it's such a magical thing.
*  Like the maps API, YouTube API.
*  I, there's a bunch of stuff.
*  I gotta imagine it's like, you know, there's probably some team at Google, right?
*  Responsible for writing this documentation.
*  That's probably not the engineers, right?
*  And probably this team is not, you know, where you want to be.
*  Well, it's a, it's a weird thing.
*  I sometimes think about this, uh, for somebody who wants to also, uh, build
*  the company, I think about this a lot.
*  You know, YouTube, the, you know, the service is one of the most magical, like
*  I'm so grateful that YouTube exists.
*  And yet they seem to be quite clueless on so many things like that.
*  Everybody's screaming them at, like it feels like.
*  Whatever the mechanism that you use to listen to your quote unquote
*  customers, which is like the creators is not very good.
*  Like there's literally people that are like screaming why, like, uh, they're
*  new YouTube studio, for example, there's like features that, that were like begged
*  for, for a really long time, like being able to upload multiple videos at the same
*  time that wasn't missing for a really, really long time.
*  Now, like there's probably things that I don't know, which is maybe for that kind
*  of huge infrastructure is actually very difficult to build some of these features.
*  But the fact that that wasn't communicated and it felt like you're not being heard.
*  Like, I remember this experience for me and it's not a pleasant experience.
*  And it feels like the company doesn't give a damn about you.
*  And that's something to think about.
*  I'm not sure what that is that might have to do with just like small groups working
*  on these small features and these specific features, and there's no
*  overarching like dictator type of human that says like, why the hell are we
*  neglecting like Steve jobs type of characters?
*  Like there's people that we need to, we need to speak to the people that like
*  want to love our product and they don't.
*  Maybe at some point you just get so fixated on the numbers, right?
*  And it's like, well, the numbers are pretty great, right?
*  It's like people are watching, you know, doesn't seem to be a problem, right?
*  And you're not like the person that like build this thing, right?
*  So you really care about it.
*  Yeah.
*  You know, you just stare, you came in as a product manager, right?
*  You got hired sometime later.
*  Your mandate is like increased this number, like, you know, 10%.
*  Right.
*  And that's brilliantly put.
*  Like if you, this is the, okay.
*  If there's a lesson in this is don't reduce your company into a metric of like how
*  much, uh, like you said, how much, how much people watching the videos and so on.
*  And, and, and like convince yourself that everything is working just because the
*  numbers are going up.
*  Yeah.
*  There's something you have to have a vision.
*  You have to, uh, you have to want people to love your stuff because love is
*  ultimately the beginning of like a successful long-term company is that they
*  always should love your product.
*  You have to be like a creator and have that like creators love for your own
*  thing, right?
*  Like, and you paint by, you know, these, these comments, right?
*  And probably like, uh, Apple, I think did this generally like really well.
*  You know, they're, they're well known for kind of keeping teams small, even
*  when they were big, right?
*  And, you know, he was an engineer, like there's that book, uh, creative
*  selection, I don't know if you read it by a, um, Apple engineer named Ken
*  Kosyanda it's kind of a great book actually, because unlike most of these
*  business books where it's, you know, here's how Steve job ran the company.
*  It's more like, here's how life was like for me, you know, an engineer here,
*  the projects I worked on and here, what it was like to pitch Steve jobs, you
*  know, on like, you know, I think it was in charge of like the keyboard and the
*  audit correction, right?
*  And at Apple, like Steve jobs reviewed everything.
*  And so he was like, this is what it was like to show my demos to Steve jobs and
*  you know, to change them because like Steve jobs didn't like how, you know, the
*  shape of the little key was off because the rounding of the corner was like not
*  quite right or something like this.
*  I just famously let's take look for this kind of stuff, but because the teams
*  were small, you really owned this stuff, right?
*  So you really cared.
*  Yeah.
*  Elon Musk does that similar kind of thing with Tesla, which is really interesting
*  that there's another lesson in leadership in that is to be obsessed with the
*  details and like he talks to like the lowest level engineers.
*  Okay.
*  So we're talking about ASR and so this is basically where I was saying, we're
*  going to take this like ultra seriously and then what's the mission to try to
*  keep pushing towards that 3%.
*  Yeah.
*  And kind of try to, try to build this platform where all of your, you know,
*  audits, all of your meetings, you know, they're as easily accessible as your
*  notes, right?
*  Like, so like, imagine all the meetings the company might have, right?
*  You know, I'm now that I'm like no longer a programmer, right?
*  Then I'm a quote unquote manager.
*  That's less like my day as in meetings, right?
*  Yeah.
*  And, you know, pretty often I want to like see what, what was said, right?
*  Who said it, you know, what's the context, but it's generally not really
*  something that you can easily retrieve, right?
*  Like imagine if all of those meetings were indexed, archived, you know, you
*  could go back, you could share a clip like really easily, right?
*  So that might change completely.
*  It's like everything that's said converted to text might change completely
*  the dynamics of what we do in this world, especially now with remote work, right?
*  Exactly.
*  Exactly.
*  It was, was zoom and so on.
*  That's, that's fascinating to think about.
*  I mean, for me, I care about podcasts, right?
*  And one of the things that was, you know, I'm torn.
*  I know a lot of the engineers at Spotify, so I love them very much because
*  they, uh, they dream big in terms of like, they want to empower creators.
*  So one of my hopes was with Spotify that they would use a technology like
*  rev or something like that to, to start converting everything into, uh, into
*  texts and make it indexable.
*  Like one of the things that's that sucks with podcasts is like, it's hard to find
*  stuff like the, the model is basically subscription, like you find, uh,
*  it's similar use it's similar to what YouTube used to be like, which is you
*  basically find a creator that you enjoy and you subscribe to them and like, you
*  just, uh, you just kind of follow what they're doing, but the search and
*  discovery wasn't a big part of YouTube, like in the early days, but that's what
*  currently with podcasts, like is the search and discovery is, uh, like
*  non-existent you're basically searching for like the dumbest possible thing,
*  which is like keywords in the titles of episodes.
*  Yeah.
*  So even aside from searching this cover, like all the time, so I listened to like
*  a number of podcasts and, um, you know, there's something said and I want to like
*  go back to that later because I was trying to, I'm trying to remember, what
*  do you say, like maybe like recommended some cool product that I want to try out.
*  And like, it's basically impossible.
*  Maybe like some people have pretty good show notes, so maybe you'll get lucky
*  and you can find it, right?
*  But I mean, if everyone had transcripts and it was all searchable, it was a
*  game changer, maybe so much better.
*  I mean, that's one of the things that I wanted to, I mean, one of the reasons
*  we're talking today is I wanted to take this quite seriously, the, the red thing.
*  I just been lazy.
*  So, uh, because I'm very fortunate that a lot of people support this
*  podcast, that there's enough money now to do a transcription and so on.
*  It w it seemed clear to me, especially like CEOs and sort of, uh, like
*  PhDs, like people write to me who are like graduate students in computer
*  science or graduate students or whatever the heck field.
*  It's clear that their mind, like they enjoy podcasts when they're doing
*  laundry or whatever, but they want to revisit the conversation in a much more
*  rigorous way and they really want to transcript, like it's clear that they
*  want to like analyze conversations.
*  Like so many people wrote to me about a transcript for your Shabach conversation.
*  Just a bunch of conversations.
*  And then on the Elon Musk side, like reporters want, like they want to write a
*  blog post about your conversation.
*  So they want to be able to pull stuff.
*  And it's like, they're essentially doing on your conversation,
*  transcription privately.
*  They're doing it for themselves and then starting to pick, but it's so much easier
*  when you can actually do it as a reporter, just look at the transcript.
*  Yeah.
*  And you can like embed a little thing, you know, like into your article, right?
*  Here's what they said.
*  You can go listen to like this clip from the section.
*  I'm actually trying to, trying to figure out, I'll probably on the website create
*  like a place where the transcript goes, like as a webpage so that people can
*  reference it, like reporters can reference it and so on.
*  I mean, most of the reporters probably want to write click bait articles that
*  are complete falsifying, which I'm fine with.
*  It's the way of journalism.
*  I don't care.
*  Like I've had this conversation with a friend of mine, a mixed
*  martial artists, the Ryan Hall.
*  And we, we talked about, you know, as I've been reading the rise and
*  fall, the third Reich and a bunch of books on Hitler and we brought up
*  Hitler and he made some kind of.
*  Comment where like we should be able to forgive Hitler and, uh, you know, like
*  we were talking about forgiveness and we were bringing that up as like the
*  worst case possible thing is like even, you know, for people who are Holocaust
*  survivors, one of the ways to let go of the suffering they've been through is
*  to, is to forgive.
*  And he brought up like Hitler is somebody that would potentially be the
*  hardest thing to possibly forgive, but it might be a worthwhile pursuit
*  psychologically, so on, blah, blah, blah.
*  Doesn't matter.
*  It was very eloquent, very powerful words.
*  I think people should go back and listen to it.
*  It's powerful.
*  And then all these journalists, there's all these articles written about like
*  MMA fight, UFC fight, right?
*  Fight or lost Hitler.
*  No, like, well, no, they didn't, they were somewhat accurate.
*  They didn't say like a loves Hitler.
*  They said, um, thinks that, uh, if Hitler came back to life, we should forgive him.
*  Like they kind of, it's kind of accurate ish, but it, the headline
*  make it sound a lot worse than, than, uh, than it was, but I'm fine with it.
*  That's the way that that's the way the world, I want to, I want to almost make
*  it easier for those journalists and make it easier for people who actually care
*  about the conversation to go and look and see for themselves, for themselves.
*  There, there's something about podcasts, like the audio that makes it difficult
*  to, to go to jump to a spot and to look for that, for that particular information.
*  I think some of it, you know, I'm interested in creating like myself
*  experimenting with stuff.
*  So like they taking rev and creating a transcript and then people can go to it.
*  I do dream that like, I'm not in the loop anymore that like, you know, Spotify
*  does it right.
*  Like automatically for everybody because ultimately that one click
*  purchase needs to be there.
*  Like,
*  I mean, like it kind of wants support from the entire ecosystem, from the
*  tool makers and the podcast creators, even clients, right?
*  I mean, imagine if like, um, most podcast apps, you know, if it was a standard,
*  right, here's how you include a transcript into a podcast, right?
*  Like it's just an RSS feed ultimately.
*  Um, and actually, uh, just yesterday I saw this company called Buzzsprout,
*  I think they're called.
*  Uh, so they're trying to do this.
*  They, uh, propose the spec, um, an extension to their, uh, RSS format to
*  reference podcasts, uh, reference transcripts in a standard way.
*  Yeah.
*  And they're talking about like, there's one, uh, client dimension that will
*  support it, but imagine like more clients support it, right?
*  So any podcast you could go, um, and see the transcripts right in your
*  like normal podcast app.
*  Yeah.
*  I mean, somebody, so I have somebody who works with me, uh, is works with
*  helps with advertising, uh, with advertising.
*  Uh, Matt is awesome guy.
*  He mentioned Buzzsprout to me, but he says it's really annoying because
*  they want exclusive, uh, they want to host the podcast.
*  This is the problem with Spotify too.
*  Uh, this is where I'd like to say like F Spotify.
*  There's a magic to RSS with podcasts.
*  Is it can be made available to everyone.
*  And then there's all, there's this ecosystem of different podcast
*  players that emerge and they compete freely.
*  And that, that's a, that's a beautiful thing that that's why I go on
*  exclusive like Joe Rogan went exclusive.
*  Um, I'm not sure if you're familiar with, he went to Spotify.
*  As a huge fan of Joe Rogan, I've been kind of nervous about the whole thing,
*  but let's see, let's, I hope this Spotify steps up.
*  They've added video, which was very surprising that they were
*  meaning you can subscribe to the RSS feed anymore.
*  It's only in Spotify for now.
*  You can until December 1st and December 1st, it all, everything
*  disappears in Spotify only.
*  I, uh, you know, and Spotify gave them a hundred million dollars for that.
*  So it's, it's a, it's an interesting deal, but I, I, you know, I did some
*  soul searching and I'm glad he's doing it.
*  But if Spotify came to me with a hundred million dollars, I wouldn't do it.
*  I wouldn't do well.
*  I have a very different relationship with money.
*  I hate money, but I just think I believe in the pirate radio
*  aspect of podcasting the freedom.
*  And that there's something about the open source spirit.
*  The open source spirit is just doesn't seem right.
*  It doesn't feel right.
*  That said, you know, because so many people care about Joe Rogan's program,
*  they're going to hold Spotify's feet to the fire.
*  Like one of the cool things, what Joe told me is the reason he likes working
*  with Spotify is that they, they're like ride or die together, right?
*  So they, they want him to succeed.
*  So that's why they're not actually telling him what to do, but what people
*  think they, they don't tell them, they don't give them any notes on anything.
*  They want him to succeed.
*  And that's the cool thing about exclusivity with a platform is like,
*  you're kind of want each other to succeed and that process can
*  actually be very fruitful.
*  Like YouTube, it goes back to my criticism.
*  YouTube generally, no matter how big the creator, maybe for PewDiePie,
*  something like that, they want you to succeed.
*  But for the most part, from all the big creators I've spoken with,
*  Veritasium, all those folks, you know, they get some basic assistance, but
*  it's not like YouTube doesn't care if you succeed or not.
*  They have so many creators.
*  Like a hundred other.
*  They don't care.
*  So, and especially with, um, with somebody like Joe Rogan, who YouTube sees
*  Joe Rogan, not as a person who might revolutionize the nature of news and
*  idea space and nuanced conversations.
*  They see him as a potential person who, uh, who, uh, has racist guests on, or
*  like, you know, they see him as like a headache potentially.
*  So, you know, a lot of people talk, talk about this.
*  It's, it's a hard place to be for YouTube actually is figuring out with the
*  search and discovery process of how do you filter out conspiracy theories and
*  which conspiracy theories represent dangerous untruths and which conspiracy
*  theories are like vanilla untruths.
*  And then even when you start having meetings and discussions about what is
*  true or not, it starts getting weird.
*  Yeah.
*  It's starting to get weird.
*  It's difficult these days, right?
*  I worry more about the other side, right?
*  Of too much, you know, too much censorship.
*  Well, maybe censorship is the right word.
*  I mean, uh, censorship is usually government censorship, but still,
*  uh, yeah, putting yourself in a position of arbiter for these kinds of things.
*  It's very difficult and people think it's so easy, right?
*  Like, cause like, well, you know, like no Nazis, right?
*  What a simple principle.
*  Uh, but you know, yes, I mean, no one likes Nazis, but it's like many
*  shades of gray, like very soon after that.
*  Yeah.
*  And then, you know, of course everybody, you know, there's some people that call
*  our current president, a Nazi, and then there's like, so you start getting, uh,
*  Sam Harris.
*  I don't know if you know that is wasted.
*  I, in my opinion, his conversation with Jack Dorsey, I lost, I spoke with
*  Jack before on this podcast and we'll talk again, but Sam brought up, uh,
*  Sam Harris does not like Donald Trump.
*  I do listen to his podcast.
*  I'm familiar with his views on the matter.
*  And he, uh, he has Jack Dorsey is like, how can you not ban Donald Trump from
*  Twitter?
*  So, you know, there's a set, you have that conversation.
*  You have a conversation where some number or some significant number of people
*  think that the current president of the United States should not be on your
*  platform.
*  And that's like, okay.
*  So if that's even on the table as a conversation, then everything is on the
*  table for conversation.
*  And yeah, it's, it's tough.
*  I'm not sure where I land on it.
*  I'm with you.
*  I think that censorship is bad, but I also think the
*  ultimately, I just also think, you know, if you're the kind of person that's
*  going to be convinced, you know, by some YouTube video, you know, that I don't
*  know, our government has been taken over by aliens.
*  It's unlikely that like, you know, you'll be returned to sanity simply because,
*  you know, that video is not available on, on, on YouTube, right?
*  Yeah, I'm with you.
*  I tend to believe in the intelligence of people and we should, we should trust
*  them.
*  But I also do think it's a responsibility of platforms to encourage more love in
*  the world, more kindness to each other.
*  And I don't always think that they're great at doing that particular thing.
*  So that, that, um, there, there's a nice balance there.
*  And I think philosophically, I think about that a lot.
*  Where's the balance between free speech and like encouraging people, even though
*  they have the freedom of speech to not be an asshole.
*  Yeah.
*  Right.
*  That's not a constitutional, like, uh, so you have the right for, to, for free
*  speech, but like, just don't be an asshole.
*  Like you can't really put that in the constitution that the Supreme Court
*  can't be like, just don't be a dick.
*  But I feel like platforms have a role to be like, just be nicer.
*  Maybe do the carrot, like encourage people to be nicer as opposed to the
*  stake of censorship, but I think it's, it's an interesting machine learning problem.
*  Just be nicer.
*  Machine.
*  Yeah.
*  Machine learning for niceness.
*  It is.
*  I mean, that's possible.
*  Yeah.
*  I mean, it is, it is a thing.
*  Um, for sure.
*  Jack Dorsey kind of talks about it as a vision for Twitter is how do we
*  increase the health of conversations.
*  I don't know how seriously they're actually trying to do that though.
*  Uh, which is one of the reasons that I'm in part considering entering that space.
*  It's difficult for them, right?
*  Because, you know, it's kind of like well known that, you know, people are kind of
*  driven by, you know, rage and, you know, uh, outrage maybe is a better word, right?
*  Outrage drives engagement and well, these companies are judged by engagement, right?
*  So it's in the short term, but this goes to the metrics thing that we were talking
*  about earlier.
*  I do believe I have a fundamental belief that if you have a metric of long-term
*  happiness of your users, like not short-term engagement, but long-term
*  happiness and growth and both like intellectual, emotional health of your
*  users, you're going to make a lot more money.
*  You're going to have long like you should be able to optimize for that.
*  You don't need to necessarily optimize for engagement.
*  Yeah.
*  And that'll be good for society too.
*  Yeah, no.
*  I mean, I generally agree with you, but it requires a patient person with, you
*  know, trust from Wall Street to, to, to be able to carry out such a strategy.
*  This is the, this is what I believe the Steve jobs character and Elon Musk
*  character is like, you basically have to be so good at your job, right?
*  You got to pass for anything that you can hold the board and every, all the
*  investors hostage by saying like, either we do it my way or I leave and
*  everyone is too afraid of you to leave.
*  Right.
*  Cause they believe in your vision.
*  So that, but that requires being really good at, uh, really good at what you do.
*  It requires being Steve jobs and Elon Musk.
*  And there's kind of a reason why like the third name doesn't come
*  immediately to mind, right?
*  Like there's maybe a handful of other people, but it's not that many.
*  It's not many.
*  I mean, people say like, why are you like, people say that I'm like a fan of Elon
*  Musk, I'm not, I'm a fan of anybody who's like Steve jobs and Elon Musk.
*  And there's just not many of those folks.
*  It's a guy that made us believe that like we can get to Mars, you know, in 10 years.
*  Right.
*  I mean, that's kind of awesome.
*  And it's kind of making it happen, which is like, it's, it's great.
*  You know, I've gone like that kind of like spirit, right?
*  Like from a lot of our society, right?
*  Yeah.
*  Like we can get to the moon in 10 years and like we did it.
*  Right.
*  Yeah.
*  Especially in this time of, uh, so much kind of existential dread that people are
*  going through because of COVID.
*  Like having rockets that just keep going out there now with humans.
*  I don't know that, uh, it just like you said, I mean, it gives you a reason to
*  wake up in the morning and dream for us engineers too.
*  Uh, it, um, this is inspiring as hell, man.
*  I w let me ask you this, the worst possible question, which is, uh, so you're
*  like at the core, you're a programmer, you're, um, an engineer, but now you made
*  the unfortunate choice, uh, or maybe that's the way life goes of basically moving away
*  from the low level work and becoming a manager, becoming an executive, having
*  meetings, uh, what's, what's that transition been like?
*  It's been interesting.
*  It's been a journey, maybe a couple of things to say about that.
*  I mean, I got into this, right?
*  Because, uh, as a kid, I just remember this like incredible amazement at being
*  able to write a program, right?
*  And something comes to life that kind of didn't exist before.
*  I don't think you have that in like many other fields.
*  Like you have that with some other kinds of engineering, but you may be a little
*  bit more limited with what you can do.
*  Like, right.
*  But with a computer, you can literally imagine any kind of program, right?
*  Uh, so it's, it's a little bit Godlike.
*  Uh, what do you do like when you create it?
*  Uh, and so, I mean, that's why I got into it.
*  Do you remember like first program you wrote or maybe the first program that
*  like made you fall in love with computer science?
*  Uh, I don't know what was the first program.
*  It's probably like trying to write one of those, uh, games and basic, you know,
*  like emulate the snake game or whatever.
*  Um, I don't remember it to be honest.
*  Uh, but I enjoyed like, that's why I always loved about, you know, being a
*  program is just the creation process.
*  And, um, it's a little bit different when you're not the one doing the creating.
*  Uh, and you know, another aspect to it, I would say is, you know, when you're a
*  programmer, when you're an individual contributor, it's kind of very easy to
*  know when you're doing a good job, when you're not doing a good job, when you're
*  being productive, when you're not being productive, right?
*  You can kind of see like you try to make something and it's like slowly
*  coming together, right?
*  And when you're a manager, you know, it's more diffuse, right?
*  Like, well, you hope, you know, you're motivating your team and making them
*  more productive and inspiring them.
*  Right.
*  But it's not like you get some kind of like dopamine signal because you're
*  like completed X lines of code, you know, today.
*  Uh, so kind of like you missed that dopamine rush a little bit, uh, um,
*  when you first, um, become, but then, you know, slowly you kind of see, yes,
*  your teams are doing amazing work, right?
*  And you, you can take pride in that.
*  Um, you can get like, uh, uh, what is it?
*  Like a ripple effect of a dope or somebody else's dope.
*  Yeah.
*  Yeah.
*  You live off other people's dopamine.
*  So is there pain points and challenges you have to overcome from becoming,
*  from going to a programmer to becoming a programmer of humans?
*  Programmer of humans.
*  I don't know.
*  Humans are difficult to understand, you know, uh, you know, it's like one of
*  those things like trying to understand other people's motivations and what
*  really drives them.
*  It's difficult.
*  Maybe you like never really know, right?
*  Do you find that people are different?
*  Yeah.
*  Like I, I, one of the things, like I had a group at MIT that, you know, I found
*  that like some people I could like scream at and criticize like hard and that
*  made them do like much better work and really push them to their limit.
*  And there's some people that I had to nonstop compliment because like they're
*  so already self critical, like about everything they do that I have to be
*  constantly like, like I cannot criticize them at all because they're already
*  criticizing themselves and you have to kind of encourage and like celebrate
*  their little victories.
*  And it's kind of fascinating like how that, the complete difference in people.
*  Definitely people respond to different motivations and different loads of
*  feedback and you kind of have to figure it out.
*  It was like a pretty good book, which is the reason now the name escapes me
*  about management first break all the rules.
*  First break all the rules.
*  First break all the rules.
*  It's a book that we generally like ask a lot of like first time managers to
*  read the ref and like one of the kind of philosophies is managed by exception,
*  right?
*  Which is, you know, don't like have some standard template, like, you know, here's
*  how I tell this person to do this or the other thing.
*  Here's how I get feedback like managed by exception, right?
*  Every person is a little bit different.
*  You have to try to understand what drives them and tailor it to them.
*  Since you mentioned books, I don't know if you can answer this question, but
*  people love it when I ask it, which is are there books, technical fiction or
*  philosophical that you enjoyed or had an impact on your life that you would
*  recommend?
*  You already mentioned Dune, like all of the, all of the Dune.
*  The second one was probably the weakest, but anyway, so yeah, all of the Dune is
*  good.
*  I mean, yeah.
*  Can you just slow little tangent on that is how many Dune books are there?
*  Like, do you recommend people start with the first one?
*  If you, if that was, yeah, you gotta have to read them all.
*  I mean, it is a complete story, right?
*  So you start with the first one, you gotta read all of them.
*  So it's not like a tree, like that, like a creation of like the universe that
*  you should go in sequence.
*  It's kind of a chronological storyline.
*  There are six books in all.
*  Then there's like many kind of books that were written by Frank Herbert's son,
*  but those are not as good.
*  So you don't have to bother with those.
*  Shots fired.
*  Shots fired.
*  But the main sequences is good.
*  So what are some other books?
*  Maybe there's a few.
*  So I don't know that like, I would say there's a book that, you know, I don't
*  know, turned my life around or anything like that, but here's a couple that I
*  really love.
*  So one is Brave New World by Aldous Huxley.
*  And it's kind of incredible how prescient he was about like what a Brave New World
*  might be like, right?
*  You know, you kind of see genetic sorting in this book, right?
*  Where there's like these alphas and epsilons and, you know, like, you know,
*  genetic sorting in this book, right?
*  Where there's like these alphas and epsilons and how from like the earliest
*  time of society, like they're sorted.
*  And like, you can kind of see it in a slightly similar way today where, well,
*  one of the problems with society is people are kind of genetically sorting a
*  little bit, right?
*  Like there's much less, like most marriages, right?
*  Are between people of similar kind of intellectual level or socioeconomic status.
*  More so these days than in the past.
*  And you kind of see some effects of it in stratifying society and kind of he
*  illustrated what that could be like in the extreme.
*  Different versions of it on social media as well.
*  It's not just like marriages and so on.
*  Like it's genetic sorting in terms of what Dawkins called memes, these ideas
*  being put into these bins of these little echo chambers and so on.
*  Yeah, I know.
*  So that's the book that's I think a worthwhile read for everyone.
*  In 1984 is good, of course, as well.
*  Like if you're talking about dystopian novels of the future.
*  Yes, it's a slightly different view of the future, right?
*  But I kind of like identify with Brave New World a bit more.
*  Yeah, speaking of not a book, but my favorite kind of dystopian science
*  fiction is a movie called Brazil, which I don't know if you've heard of.
*  I've heard of and I know I need to watch it.
*  But yeah, because it's in.
*  Is it in English or no?
*  It's an English movie.
*  And it's a sort of like dystopian movie of authoritarian incompetence, right?
*  It's like nothing really works very well.
*  The system is creaky, but no one is kind of like willing to challenge it.
*  Just things kind of amble along.
*  It kind of strikes me as like a very plausible future of like, you know,
*  what authoritarianism might look like.
*  It's not like this, you know, super efficient evil dictatorship of 1984.
*  It's just kind of like this badly functioning, you know, but.
*  It's status quo, so it just goes on.
*  Yeah, that's one funny thing that stands out to me is in
*  whether it's authoritarian dystopian stuff or just basic like, you know,
*  if you look at the movie Contagion, it seems that in movies,
*  government is almost always exceptionally competent.
*  Like it's like used as a storytelling tool of like extreme competence.
*  Like, you know, you use it whether it's good or evil, but it's competent.
*  It's very interesting to think about where much more realistically is
*  its incompetence and that incompetence is itself
*  has consequences that are difficult to to predict.
*  Like bureaucracy has a very boring way of being evil.
*  I'm just you know, if you look at the show, HBO show Chernobyl,
*  it's a really good story of how bureaucracy, you know,
*  leads to catastrophic events,
*  but not through any kind of evil in any one particular place,
*  but more just like the it's just the system kind of system,
*  distorting information as it travels up the chain.
*  That people unwilling to take responsibility for things.
*  It's just kind of like this laziness resulting in evil.
*  There's a comedic version of this.
*  I don't know if you've seen this movie called The Death of Stalin.
*  Yeah, I like that.
*  I wish it wasn't so there's a movie called Inglorious Bastards about,
*  you know, Hitler and, you know, so on.
*  For some reason, those movies pissed me off.
*  I know a lot of people love them, but like.
*  I just feel like there's not enough good movies even about Hitler.
*  There's good movies about the Holocaust, but even Hitler,
*  there's a movie called Dawnfall that people should watch.
*  I think it's the last few days of Hitler.
*  That's a good movie.
*  Turned into a meme.
*  But it's good. But on Stalin, I feel like I may be wrong on this,
*  but at least in the English speaking world,
*  there's not good movies about the evil of Stalin.
*  That's true. Let's try to see that.
*  Actually, so I agree with the Inglorious Bastard.
*  I didn't love the movie
*  because I felt like kind of the stylizing of it, right?
*  The whole like Tarantino kind of Tarantinoism, if you will,
*  kind of detracted from it and made it seem like unserious a little bit.
*  But Death of Stalin, I felt differently.
*  Maybe it's because it's a comedy to begin with.
*  It's not like I'm expecting, you know, seriousness, but
*  it kind of depicted the absurdity of the whole situation in a way.
*  Right. I mean, it was funny, so maybe it does make light of it.
*  But it's not the girls probably like this, right?
*  Like a bunch of kind of people that are like, oh, shit. Right.
*  Like, you're right.
*  But like the thing is, it was so close
*  to like what probably was reality.
*  There was caricaturing reality to where,
*  I think, an observer might think that this is not like
*  they might think it's a comedy in one in reality.
*  This is that's the absurdity of how people act with dictators.
*  I mean, that's I guess it was too close to reality for me.
*  The kind of banality of like what were eventually like fairly evil acts.
*  Right. But like, yeah, they're they're just a bunch of people trying to survive.
*  And I'm saying because I think there's a good I haven't watched it yet.
*  The good movie and the movie on Churchill
*  with Gary Oldman, I think is girl.
*  And I made me make it that up.
*  I think he won like he was nominated for an Oscar or something.
*  So I like I love these movies about these humans and Stalin.
*  Like Chernobyl made me realize the HBO show that there's not enough movies
*  about Russia that capture.
*  That spirit, I'm sure it might be in Russia and there is.
*  But the fact that some British dude that like did comedy,
*  I feel like he did like hangover, some shit like that.
*  I don't know if you're familiar with the person who created Chernobyl,
*  but he was just like some guy that doesn't know anything about Russia.
*  And he just went in and just studied it, like did a good job of creating
*  and then got it so accurate, like poetically.
*  And the fact that you need to get accurate, he got accurate.
*  Just the spirit of it down to like the balls that pets use,
*  just the whole feel of it.
*  And it's nice. It's good. Yeah, I saw this here.
*  Yeah, it's incredible.
*  She made me made me wish that somebody did a good like
*  1930s, like starvation at Stalin, like to like leading up to World War II
*  and in World War II itself, like Stalingrad and so on.
*  Like. I feel like that story needs to be told.
*  Millions of people died.
*  And it's to me, it's so much more fascinating that Hitler,
*  because Hitler is like a caricature of evil almost
*  that it's so especially with the Holocaust.
*  It's so difficult to imagine that something like that is possible ever again.
*  Stalin, to me, represents something that is possible.
*  Like the so interesting, like the bureaucracy of it
*  is so fascinating that it potentially might be happening in the world now.
*  Like they were not aware of like North Korea, another one that
*  like there should be a good film on like the possible things
*  that could be happening in China with overreach of government.
*  I don't know. There's a lot of possibilities there, I suppose.
*  Yeah, I wonder how much, you know, I guess the archives should be
*  maybe more open nowadays, right?
*  I mean, for a long time, they just waited now. Right.
*  Anyways, no one in the West knew for sure.
*  Well, there's a I don't know if you know, there's a guy named Stephen Kotkin.
*  He is a historian of Stalin that I spoke to on this podcast.
*  I'll speak to him again.
*  The guy knows his shit on Stalin.
*  He like read everything.
*  And it's so it's so fascinating to.
*  To to talk to somebody
*  like he knows Stalin better than Stalin himself.
*  It's crazy. Like you have to say, I think he's at Princeton.
*  He is basically his whole life is the stalling stalling.
*  Yeah, it's great.
*  And in that context, he also talks about and writes about Putin a little bit.
*  I've also read at this point, I think every biography of Putin, English,
*  English biography of Putin, I need to read some Russians.
*  Obviously, I'm mentally preparing for a possible conversation with Putin.
*  So what is your first question to Putin when you have him on your on the podcast?
*  I.
*  It's interesting you bring that up.
*  The first of all, I wouldn't tell you, but I can't get away now.
*  But I actually haven't even thought about that.
*  So my current approach and I do this with interviews
*  often, but obviously that's a special one.
*  But I try not to think about questions until last minute.
*  I'm trying to sort of get into the mindset.
*  And so that's why I'm soaking in a lot of stuff,
*  not thinking about questions, just learning about the man.
*  But in terms of like human to human, it's like I would say it's
*  I don't know if you're a fan of mob movies, but like the mafia,
*  which I am a good fellow and so on.
*  He's much closer to like mob morality, which is like
*  mob morale. Maybe I could see that.
*  But I like your approach anyways of this extreme empathy, right?
*  It's a little bit like, you know, Hannibal, right?
*  Like if you ever watched the show Hannibal, right, they had that guy.
*  We know Hannibal, of course, like, yeah.
*  Sounds like the lambs.
*  But there was a TV show as well.
*  And they focused on this guy, Will Durant,
*  who's a character like extreme empath, right?
*  So in the way he like catches all these killers, he pretty much
*  he can empathize with them, right?
*  Like you can understand why they're doing things they're doing.
*  Right. And it's a pretty excruciating thing, right?
*  Like because you're pretty much like spending half your time in the head of
*  evil people, right? Like, but I mean, I definitely try to do that with
*  with others. So you should do that in moderation.
*  But I think it's a pretty safe place, safe place to be.
*  One of the cool things with this podcast, and I know you didn't sign up
*  to hear me listen to this bullshit, but that was interesting. I.
*  And what's his name? Chris Latner, who's a Google.
*  Oh, he's not Google anymore. Sci fi. He's legit.
*  He's one of the most legit engineers I've talked with.
*  I talked with him again on this podcast and whether he gives me private advice
*  a lot. And he said for this podcast, I should like interview,
*  like I should widen the range of people because that gives you
*  much more freedom to do stuff like.
*  So his idea, which I think I agree with, with Chris, is that you go to the extremes.
*  You just like cover every extreme base and then it gives you freedom to then
*  go to the more nuanced conversations.
*  It's kind of I think there's a safe place for that.
*  There's certainly a hunger for that nuanced conversation, I think, amongst people
*  where, like on social media, you get canceled for anything slightly tense.
*  That there's a hunger to go full.
*  You go so far to the opposite side.
*  And it's like the mystifies it a little bit, right?
*  Yeah, that there is a person behind all of these things.
*  And that's the cool thing about podcasting, like three, four hour conversations that
*  that it's very different than a clickbait journalism.
*  It's like the opposite that there's a hunger for that.
*  There's a willingness for that.
*  Especially now, I mean, how many people do you even see face to face anymore?
*  Right. Like this, you know, it's like not that many people like in my day to day,
*  aside from my own family, that, like I said, across it, it's sad,
*  but it's also beautiful.
*  Like I've gotten the chance to like like our conversation now.
*  There's somebody I guarantee you there's somebody in Russia
*  listening to this now, like jogging.
*  There's somebody who is just smoke some weed, sit back on a couch and just like
*  enjoying. Like, I guarantee you that we'll write in the comments right now that,
*  yes, I'm in St. Petersburg.
*  I'm in Moscow, whatever.
*  And we're in their head and they have a friendship with us.
*  And I'm the same way. I'm a huge fan of podcasting.
*  It's a beautiful thing. I mean, it's a it's a weird one way human connection.
*  Like before I went on Joe Rogan and still I'm just a huge fan of his.
*  So it was like we had I've been a friend with Joe Rogan for 10 years, but one way.
*  Yeah, from this way, from the from the St. Petersburg way.
*  Yeah, the same way.
*  And it's a real friendship.
*  I mean, now it's like two way, but it's still surreal.
*  And that's the magic of podcasting.
*  I'm not sure what to make of it.
*  That voice is not even the video part.
*  It's the audio that's magical that I don't know what to do with it.
*  But it's people listen to three, four hours.
*  Yeah, we evolved over, you know, millions of years, right, to be very fine
*  tuned to things like that. Right.
*  Yeah. Oh, expressions as well, of course. Right.
*  But, you know, back back in the day on the, you know, on the savanna,
*  you have to be very tuned to, you know, whether you have a good relationship
*  with the with the rest of your tribe or a very bad relationship.
*  Right. Because if you had a very bad relationship, you're probably
*  going to be left behind and eaten by the lions.
*  Yeah. But it's weird that the tribe is different now.
*  Like you could have a connection, one way connection with Joe Rogan,
*  as opposed to the tribe of your physical vicinity.
*  But that's why, like, you know, it works with the podcasting.
*  But it's the opposite of what happens on Twitter.
*  Right. Because all those nuances are removed.
*  Right. You're not connecting with the person.
*  Yeah. Because you don't hear the voice.
*  You're connecting with like an abstraction. Right.
*  It's like some some stream of tweets.
*  Right. And it's very easy to.
*  A sign to them, any kind of like evil intent,
*  you know, or dehumanize them, which is much harder to do when it's a real voice.
*  Right. Because like you realize it's a real person behind the voice.
*  Let me try this out on you.
*  I sometimes ask about the meaning of life.
*  Do you your your father now?
*  In engineer, you're building up a company.
*  Do you ever zoom out and think like, what the hell is this whole thing for?
*  Like, why? Why are we descended to vapes even on this planet?
*  What's what's the meaning of it all?
*  That's a pretty big question.
*  I think I don't allow myself to think about it too often, or maybe like
*  life doesn't allow me to think about it too often.
*  But in some ways, I guess the meaning of life is kind of
*  contributing to this kind of weird thing we call humanity.
*  Right. Like it's in a way, I think of humanity as like a living and evolving
*  organism, right. That like we all contributing in a sway way, but just by existing,
*  by having our own unique set of desires and drives. Right.
*  And maybe that means like creating something great.
*  And it's bringing up kids who, you know,
*  are unique and different and seeing like, you know, they can enjoy what they do.
*  But I mean, to me, that's pretty much it.
*  I mean, if you're not a religious person, right, which I guess I'm not.
*  That's that's the meaning of life.
*  It's in the living and in creation and the creation.
*  Yeah, there's something magical about that engine of creation.
*  Like you said, programming, I would say.
*  I mean, it's even just actually what you said with even just programs.
*  I don't care if it's like some JavaScript thing on a button on the website.
*  It's like magical that you brought that to life.
*  I don't know what that is in there, but that seems that's probably some
*  version of recreation of like reproduction and sex, whatever.
*  That's in evolution.
*  But like creating that HTML button
*  has has echoes of that feeling.
*  And it's magical.
*  Right. I mean, if you're religious person, maybe you could even say, right,
*  like we were we were created in God's image, right?
*  Well, I mean, I guess part of that is the drive to create something ourselves.
*  Right. I mean, that's that's that's part of it.
*  Yeah, that HTML button is the creation in God's.
*  Yeah. So maybe hopefully it'll be something a little more
*  so dynamic, maybe bigger.
*  Some dynamic. Yeah, maybe some some JavaScript, some React
*  and so on. But no, I mean, I think.
*  That's what differentiates us from the apes, so to speak.
*  Yeah, we did a pretty good job.
*  Then it was honor to talk to you.
*  Thank you so much for being part of creating one of my favorite
*  services and products.
*  This is actually a little bit of an experiment.
*  Allow me to sort of fanboy with some of the things I love.
*  So thanks for wasting your time with me today.
*  Well, it's awesome. Thanks for having me on and giving me a chance to try this out.
*  Awesome.
*  Some words from Ludwig Wittgenstein.
*  The limits of my language means the limits of my world.
*  Thank you for listening and hope to see you next time.

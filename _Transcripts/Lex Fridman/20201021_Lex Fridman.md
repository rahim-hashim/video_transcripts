---
Date Generated: April 13, 2024
Transcription Model: whisper medium 20231117
Length: 11326s
Video Keywords: ['george hotz', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 1313572
Video Rating: None
---

# George Hotz: Hacking the Simulation & Learning to Drive with Neural Nets | Lex Fridman Podcast #132
**Lex Fridman:** [October 21, 2020](https://www.youtube.com/watch?v=_L3gNaAVjQ4)
*  The following is a conversation with George Hotz, AKA GeoHot, his second time on the podcast.
*  He's the founder of Comma AI, an autonomous and semi-autonomous vehicle technology company
*  that seeks to be, to Tesla, autopilot what Android is to the iOS. They sell the Comma 2 device for
*  $1,000 that when installed in many of their supported cars can keep the vehicle centered
*  in the lane even when there are no lane markings. It includes driver sensing that ensures that the
*  driver's eyes are on the road. As you may know, I'm a big fan of driver sensing. I do believe Tesla
*  Autopilot and others should definitely include it in their sensor suite. Also, I'm a fan of Android
*  and a big fan of George for many reasons, including his non-linear out-of-the-box brilliance
*  and the fact that he's a superstar programmer of a very different style than myself.
*  Styles make fights and styles make conversations. So I really enjoyed this chat and I'm sure we'll
*  talk many more times on this podcast. Quick mention of each sponsor followed by some
*  thoughts related to the episode. First is FourSigmatic, the maker of delicious mushroom coffee.
*  Second is Decoding Digital, a podcast on tech and entrepreneurship that I listen to and enjoy.
*  And finally, ExpressVPN, the VPN I've used for many years to protect my privacy on the internet.
*  Please check out the sponsors in the description to get a discount and to support this podcast.
*  As a side note, let me say that my work at MIT on autonomous and semi-autonomous vehicles led me to
*  study the human side of autonomy enough to understand that it's a beautifully complicated
*  interesting problem space, much richer than what can be studied in the lab.
*  In that sense, the data that Cama.ai, Tesla Autopilot, and perhaps others like Cadillac
*  Super Cruiser are collecting gives us a chance to understand how we can design safe, semi-autonomous
*  vehicles for real human beings in real world conditions. I think this requires bold innovation
*  and a serious exploration of the first principles of the driving task itself.
*  If you enjoyed this thing, subscribe on YouTube, review it with Five Stars and Apple Podcasts,
*  follow on Spotify, support on Patreon, or connect with me on Twitter at Lex Friedman.
*  And now, here's my conversation with George Hotz.
*  So last time we started talking about the simulation, this time let me ask you,
*  do you think there's intelligent life out there in the universe?
*  I've always maintained my answer to the Fermi paradox. I think there
*  has been intelligent life elsewhere in the universe.
*  So intelligent civilizations existed, but they've blown themselves up. So your general intuition is
*  that intelligent civilizations quickly, like there's that parameter in the Drake equation.
*  Your sense is they don't last very long. How are we doing on that? Have we lasted pretty good?
*  Oh, yeah. I mean, not quite yet. Well, it's like the IQ required to destroy the world falls by
*  one point every year. Okay. So technology democratizes the destruction of the world.
*  When can a meme destroy the world? It kind of is already, right?
*  Somewhat. I don't think we've seen anywhere near the worst of it yet. The world's going to get weird.
*  Well, maybe a meme can save the world. Have you thought about that? The meme lord Elon Musk
*  fighting on the side of good versus the meme lord of the darkness, which is not saying anything bad
*  about Donald Trump, but he is the lord of the meme on the dark side. He's a Darth Vader of memes.
*  I think in every fairy tale, they always end it with, and they lived happily ever after. And I'm
*  like, please tell me more about this happily ever after. I've heard 50% of marriages end in divorce.
*  Why doesn't your marriage end up there? You can't just say happily ever after. So
*  the thing about destruction is it's over after the destruction. We have to do everything right
*  in order to avoid it. And one thing wrong, I mean, actually, this is what I really like about
*  cryptography. Cryptography, it seems like we live in a world where the defense wins
*  versus nuclear weapons. The opposite is true. It is much easier to build a warhead that splits
*  into 100 little warheads than to build something that can take out 100 little warheads. The offense
*  has the advantage there. So maybe our future is in crypto.
*  So cryptography, right. The Goliath is the defense. And then all the different hackers are the
*  are the Davids. And that equation is flipped for nuclear war. Because there's so many,
*  one nuclear weapon destroys everything, essentially. Yeah. And it is much easier to
*  attack with a nuclear weapon than it is to like, the technology required to intercept and destroy
*  a rocket is much more complicated than the technology required to just, you know,
*  orbital trajectory, send a rocket to somebody. So, okay, your intuition that the war intelligent
*  civilizations out there, but it's very possible that they're no longer there.
*  It's kind of a sad picture. They enter some steady state, they all
*  wirehead themselves. What's wirehead? Stimulate their pleasure centers.
*  And just, you know, live forever in this kind of stasis. They become, well, I mean, I think the
*  reason I believe this is because where are they? If there's some reason they stopped expanding,
*  because otherwise they would have taken over the universe. The universe isn't that big,
*  or at least, you know, let's just talk about the galaxy, right? 70,000 light years across.
*  I took that number from Star Trek Voyager. I don't know how true it is. But yeah, that's not big.
*  All right. 70,000 light years is nothing. For some possible technology that you can imagine
*  that can leverage like wormholes or something like that. You don't even need wormholes. Just a von
*  Newman probe is enough. A von Newman probe and a million years of sublight travel, and you'd have
*  taken over the whole universe. That clearly didn't happen. So something stopped it.
*  So you mean if you, right, for like a few million years, if you sent out probes that travel close,
*  what's sublight? You mean close to the speed of light?
*  Let's say 0.1C.
*  And it just spreads. Interesting. Actually, that's an interesting calculation.
*  So what makes you think that we'd be able to communicate with them? Like,
*  like, yeah, what's, why do you think we would be able to be able to comprehend
*  intelligent lies that are out there? Like, even if they were among us kind of thing,
*  like, or even just flying around? Well, I mean, that's possible. It's possible that there is some
*  sort of prime directive. That'd be a really cool universe to live in. And there's some reason
*  they're not making themselves visible to us. But it makes sense that they would use the same,
*  well, at least the same entropy. Well, you're implying the same laws of physics. I don't know
*  what you mean by entropy in this case. Oh, yeah. I mean, if entropy is the scarce resource in the
*  universe. So what do you think about like Stephen Wolfram and everything is a computation? And then
*  what if they are traveling through this world of computation? So if you think of the universe as
*  just information processing, then what you're referring to with entropy and then these pockets
*  of interesting complex computation swimming around, how do we know they're not already here?
*  How do we know that this, like all the different amazing things that are full of mystery on earth
*  are just like little footprints of intelligence from light years away? Maybe. I mean, I tend to
*  think that as civilizations expand, they use more and more energy and you can never overcome
*  the problem of waste heat. So where is there waste heat? So we'd be able to, with our crude methods,
*  be able to see like there's a whole lot of energy here, but it could be something we're not. I mean,
*  we don't understand dark energy, right? Dark matter. It could be just stuff we don't understand at all,
*  or they can have a fundamentally different physics, you know, like that we just don't even
*  comprehend. Well, I think, okay, I mean, it depends how far out you want to go. I don't think physics
*  is very different on the other side of the galaxy. I would suspect that they have, I mean,
*  if they're in our universe, they have the same physics. Well, yeah, that's the assumption we have,
*  but there could be like super trippy things like, like our cognition only gets to a slice,
*  and all the possible instruments that we can design only get to a particular slice of the
*  universe. And there's something much like weirder. Maybe we can try a thought experiment.
*  Would people from the past be able to detect the remnants of our,
*  would be able to detect our modern civilization? And I think the answer is obviously yes.
*  You mean past from a hundred years ago? Well, let's even go back further. Let's go to a
*  million years ago. The humans who were lying around in the desert probably didn't even have,
*  maybe they just barely had fire. They would understand if a 747 flew overhead.
*  Oh, in this vicinity, but not if a 747 flew on Mars, like, because they wouldn't be able to see
*  far, because we're not actually communicating that well with the rest of the universe. We're doing
*  okay. Just sending out random like fifties tracks of music. True. And yeah, I mean, they'd have to,
*  you know, the, we've only been broadcasting radio waves for 150 years and well, there's your light
*  cone. So yeah. Okay. What do you make about all the, I recently came across this. I haven't talked to
*  David's flavor. I don't know if you caught what the videos that Pentagon released and the New
*  York Times reporting of the UFO sightings. So I kind of looked into it, quote unquote, and
*  there's actually been like hundreds of thousands of UFO sightings, right? And a lot of it, you can
*  explain the way in different kinds of ways. So one is that could be interesting physical phenomena
*  to it could be people wanting to believe. And therefore they conjure up a lot of different
*  things that just, you know, when you see different kinds of lights, some basic physics phenomena,
*  and then you just conjure up ideas of possible out there, mysterious worlds. But you know,
*  it's also possible. Like you have a case of, um, David Fravor, who is a Navy pilot, who's, you know,
*  a lead as legit as it gets in terms of humans who are able to perceive things in the environment
*  and make conclusions, whether those things that are threat or not. And he and several other pilots
*  saw a thing. I don't know if you followed this, but they saw a thing that they've
*  since then called tech talk that moved in all kinds of weird ways. They don't know what it is.
*  It could be technology developed by, by the United States and they're just not aware of it.
*  And the surface level from the Navy, right? It could be different kinds of lighting technology
*  or drone technology, all that kind of stuff. It could be the Russians and the Chinese,
*  all that kind of stuff. And of course their mind, our mind can also venture into the possibility
*  that it's from another world. Have you looked into this at all? What do you think about it?
*  I think all the news is a Psyop. I think that the most plausible thing is real. Yeah. I listened to
*  the, I think it was Bob Lazar on Joe Rogan. And like, I believe everything this guy is saying.
*  And then I think that it's probably just some like MK ultra kind of thing, you know?
*  What do you mean? Like they, they, they, you know, they made some weird thing and they called it an
*  alien spaceship, you know, maybe it was just to like stimulate young physicists minds, we'll tell
*  them it's alien technology and we'll see what they come up with. Right. Do you find any conspiracy
*  theories compelling? Like have you pulled at the string of the, of the rich complex world of
*  conspiracy theories that's out there? I think that I've heard a conspiracy theory that conspiracy
*  theories were invented by the CIA in the sixties to discredit true things. Yeah. So, you know,
*  you can go to ridiculous conspiracy theories like flat earth and pizza gate and, you know,
*  these things are almost to hide, like conspiracy theories that like, you know, remember when the
*  Chinese like locked up the doctors who discovered coronavirus? Like I tell people this and I'm like,
*  no, no, no, that's not a conspiracy theory. That actually happened. Do you remember the time that
*  the money used to be backed by gold and now it's backed by nothing? This is not a conspiracy theory.
*  This actually happened. That's one of my worries today with the idea of fake news is that when
*  nothing is real, then like you dilute the possibility of anything being true by
*  conjuring up all kinds of conspiracy theories and then you don't know what to believe. And then
*  like the idea of truth of objectivity is lost completely. Everybody has their own truth.
*  So you're used to control information by censoring it. Then the internet happened and
*  governments are like, oh shit, we can't censor things anymore. I know what we'll do.
*  You know, it's the old story of the story of like tying a flag with a leprechaun tells you
*  his gold is buried and you tie one flag and you make the leprechaun swear to not remove the flag
*  and you come back to the field later with a shovel and there's flags everywhere.
*  That's one way to maintain privacy, right? Is like in order to protect the contents of this
*  conversation, for example, we could just generate like millions of deep fake conversations where
*  you and I talk and say random things. So this is just one of them and nobody knows which one
*  is the real one. This could be fake right now. Classic steganography technique.
*  Okay. Another absurd question about intelligent life because you're an incredible programmer
*  outside of everything else we'll talk about just as a programmer.
*  Do you think intelligent beings out there, the civilizations that were out there had computers
*  and programming, did they, do we naturally have to develop something where we engineer machines
*  and are able to encode both knowledge into those machines and instructions that process that
*  knowledge, process that information to make decisions and actions and so on? And would those
*  programming languages, if you think they exist, be at all similar to anything we've developed?
*  So I don't see that much of a difference between quote unquote natural languages and programming
*  languages. I think there's so many similarities. So when asked the question, what do alien languages
*  look like? I imagine they're not all that dissimilar from ours. And I think translating in and out of them
*  wouldn't be that crazy.
*  It was difficult to compile like DNA to Python and then to see. There is a little bit of a gap
*  in the kind of languages we use for our touring machines and the kind of languages nature sees
*  a little bit. Maybe that's just, we just haven't, we haven't understood the kind of language that
*  nature uses well yet.
*  DNA is a cat model. It's not quite a programming language. It has no sort of a serial execution.
*  It's not quite a, yeah, it's a cat model. So I think in that sense, we actually completely
*  understand it. The problem is, you know, well, simulating the kind of language that we use
*  and simulating on these cat models, I played with it a bit this year, is super computationally
*  intensive. If you want to go down to like the molecular level where you need to go to see a lot of these
*  phenomenon like protein folding. So yeah, it's not that it's not, it's not that we don't understand it.
*  It just requires a whole lot of compute to kind of compile it.
*  For our human minds, it's inefficient both for the data representation and for the programming.
*  Yeah, it runs well on raw nature. It runs well on raw nature. And when we try to build emulators or
*  that, uh, well, the man's law kind of tried it.
*  It runs in that. Yeah. You've commented elsewhere. I don't remember where that, uh, one of the
*  problems is simulating nature is tough. And if you want to sort of deploy a prototype, I forgot how
*  you, you put it, but it made me laugh, but animals or humans would need to be involved in order to,
*  in order to try to run some prototype code on, um, like if we're talking about COVID and viruses
*  and so on, if you were trying to engineer some kind of defense mechanisms, like a vaccine
*  against COVID or all that kind of stuff that doing any kind of experimentation like you can
*  with like autonomous vehicles would be very technically cost, technically and ethically costly.
*  I'm not sure about that. I think you can do tons of, uh, crazy biology and in test tubes.
*  I think my bigger complaint is more, Oh, the tools are so bad.
*  Like literally you mean like, like I'm not brazen. I'm not pipetting shit. Like you're handing me up.
*  I got to no, no, no, no, there has to be some like automating stuff and like the,
*  yeah, but human biology is messy. Like it seems like,
*  look at those Doranos videos. They were a joke. It's like, it's like a little gantry. It's like
*  a little XY gantry high school science project with the pipette. I'm like, really? You can't
*  build like nice microfluidics and I can program the, you know, computation to bio interface. I
*  mean, this is going to happen, but like right now, if you are asking me to pipette 50 milliliters of
*  solution, I'm out. This is so crude. Yeah. Okay. Let's get all the crazy out of the way. Uh, so
*  a bunch of people asked me since we talked about the simulation last time, uh, we talked about
*  hacking the simulation. Do you have any updates, any insights about how we might be able to go about
*  hacking simulation? If we indeed do live in a simulation?
*  I think a lot of people misinterpreted the point of that South by talk. The point of the South by
*  talk was not literally to hack the simulation. Uh, I think that this, we, this is, this is an idea
*  is literally just, I think theoretical physics. I think that's the whole, you know, the whole goal,
*  right? You want your grand unified theory, but then, okay, build a grand unified theory,
*  search for exploits. Right. I think we're nowhere near actually there yet. My hope with that was
*  just more to like, like, are you people kidding me with the things you spend time thinking about?
*  Do you understand like kind of how small you are? You are, you are bites and God's computer,
*  really? And the things that people get worked up about and, you know,
*  so basically it was more a message of, uh, we should humble ourselves that we get to, uh,
*  like what, what are we humans in this byte code? Yeah. And not just humble ourselves, but like,
*  like I'm not trying to like make people guilty or anything like that. I'm trying to say like,
*  literally look at what you are spending time on. Right. What are you referring to? You're referring
*  to the Kardashians. What are we talking about? Um, I'm referring to, no, the Kardashians,
*  everyone knows that's kind of fun. I'm referring more to like the economy, you know, this idea that
*  we got to up our stock price like, or, or what is, what is the goal function of humanity?
*  You don't like the game of capitalism. Like you don't like the games we've constructed for
*  ourselves as humans. I'm a big fan of, of, of capitalism. I don't think that's really
*  the game we're playing right now. I think we're playing a, a different game where the rules are
*  rigged. Um, okay. Which games are interesting to you that we humans have constructed and which
*  aren't, which are productive and which are not actually, maybe that's the real point of the,
*  of the talk. It's like, stop playing these fake human games. There's a real game here. We can
*  play the real game. The real game is, you know, nature wrote the rules. This is a real game.
*  There still is a game to play. But if you look at, sorry to interrupt, but I don't know if you've
*  seen the Instagram account, nature is metal. The game that nature seems to be playing is a lot,
*  a lot more cruel than we humans want to put up with, or at least we see it as cruel. It's like
*  the bigger thing eats the smaller thing and, uh, does it to impress another big thing
*  so it can mate with that thing. And that's it. That seems to be the entirety of it.
*  Well, there's no art, there's no music. There's no comma AI. There's no comma one, no comma two,
*  no George Hots with his brilliant talks at South by Southwest. See, I disagree though. I disagree
*  that this is what nature is. I think nature just provided basically a open world MMORPG. And, um,
*  you know, here it's open world. I mean, if that's the game you want to play, you can play that game.
*  But that is not, isn't that beautiful? I know if you play Diablo, they used to have a, I think cow
*  level where it's, so everybody will go just, they figured out this, like the best way to gain like
*  experience points. This is just slaughter cows over and over and over. And, uh, so they figured
*  out this little sub game within the bigger game that this is the most efficient way to get experience
*  points. And everybody somehow agreed that getting experience points in RPG context, where you always
*  want to be getting more stuff, more skills, more levels, keep advancing. That seems to be good.
*  So might as well spend sacrifice, actual enjoyment of playing a game, exploring the world
*  and spending like hundreds of hours of your time in college. I mean, the number of hours I spent
*  in college level, I'm not like the most impressive person because people have probably thousands of
*  hours there, but it's ridiculous. So that's a little absurd game that brought me joy in some
*  weird dopamine drug kind of way. So you don't like those games. You don't think that's us humans
*  failing the nature. And that was the point of the talk. So how do we hack it then?
*  Well, I want to live forever and I want to live forever. And this is the goal. Well,
*  that's a game against nature. Yeah. Immortality is the good objective function to you.
*  I mean, start there and then you can do whatever else you want because you got a long time.
*  What if immortality makes the game just totally not fun? I mean, like, why do you assume immortality
*  is somehow a good objective function? It's not immortality that I want a true immortality where
*  I could not die. I would prefer what we have right now. But I want to choose my own death. Of course.
*  I don't want nature to decide when I die. I'm going to win. I'm going to beat you.
*  And then at some point, if you choose commit suicide, like how long do you think you'd live?
*  Until I get bored. See, I don't think people like in like brilliant people like you that really
*  ponder living a long time are really considering how a meaningless life becomes. Well, I want to
*  know everything and then I'm ready to die. As long as there's a, why do you want, isn't it
*  possible that you want to know everything because it's finite? Like the reason you want to know,
*  quote unquote, everything is because you don't have enough time to know everything. And once you have
*  unlimited time, then you realize like, why do anything? Like why learn anything?
*  I want to know everything and then I'm ready to die. So you have, yeah.
*  It's not, it's not a, like it's a terminal value. It's not, it's not in service of anything else.
*  I'm conscious of the possibility. This is not a certainty, but the possibility is of that engine
*  of curiosity that you're speaking to is actually a symptom of the finiteness of life. Like without
*  that finiteness, your curiosity would vanish like a, like a, like a morning fog. All right. Cool.
*  Then Koski talked about love like that. Then let me solve immortality and we change the thing in
*  my brain that reminds me of the fact that I'm immortal tells me that life is finite. Maybe
*  I'll have it tell me that life ends next week. Right. I'm okay with some self-manipulation like
*  that. I'm okay with, with deceiving. Oh, Rica changing the code. If that's the problem, right?
*  If the problem is that I will no longer have that, that curiosity, I'd like to have backup
*  copies of myself, uh, which I, yeah. Well, which I check in with occasionally to make sure they're
*  okay with the trajectory and they can kind of override it. Maybe a nice, like, I think of like
*  those wave nets, those like logarithmic go back to the copies. But sometimes it's not reversible.
*  Like, uh, I've done this with video games. When, once you figure out the cheat code or like you look
*  up how to cheat old school, like single player, it ruins the game for you. Absolutely. I know
*  that feeling. But again, that just means our brain manipulation technology is not good enough
*  yet. Remove that cheat code from your brain. What if we call, so it's also possible that if we figure
*  out immortality, that all of us will kill ourselves before we advanced far enough to, uh, to be able
*  to revert the change. I'm not killing myself till I know everything. So that's what you say now,
*  because your life is finite. You know, I think yes, self-modifying systems gets,
*  comes up with all these hairy complexities. And can I promise that I'll do it perfectly? No,
*  but I think I can put good safety structures in place. So that talk in your thinking here
*  is not literally referring to, uh, a simulation in that our, our universe is a kind of computer
*  program running in a computer. That's more of a thought experiment. Um, do you also think of
*  the potential of the sort of, uh, Bostrom Elon Musk and others that talk about an actual
*  program that simulates our universe? Oh, I don't doubt that we're in a simulation. I just think
*  that it's not quite that important. I mean, I'm interested only in simulation theory as far as
*  like it gives me power over nature. Uh, if it's totally unfalsifiable, then who cares?
*  I mean, what do you think that experiment would look like? Like somebody, uh, on Twitter asked,
*  ask George what signs we would look for to know whether or not we're in the simulation,
*  which is exactly what you're asking is like the step that precedes the step of knowing how to get
*  more power from this knowledge is to get an indication that there's some power to be gained.
*  So get an indication that there you can discover and exploit cracks in the simulation
*  or it doesn't have to be, you know, in the physics of the universe. Yeah. Show me. I mean,
*  like a memory leak could be cool. Some scrying technology, you know, what, what kind of technology
*  scrying? What's that? Oh, that's a weird, uh, scrying is the, is the, uh, paranormal ability to,
*  like, like remote viewing, like being able to see somewhere where you're not. Um, so, you know,
*  I don't think you can do it by chanting in a room, but, um, if we could find as a memory leak,
*  basically, it's a memory leak. Yeah. You're able to access parts you're not supposed to. Yeah.
*  Yeah. Yeah. And thereby discover a shortcut. Yeah. Maybe I memory leak means the other thing as well,
*  but I mean like, yeah, like an ability to read arbitrary memory. Right. Um, and that one's not
*  that horrifying. The right ones start to be horrifying. Read it. Right. So the reading is
*  not the problem. Yeah. It's like Heartfleet for the universe. Oh boy. The writing is a big, big
*  problem. It's a big problem. It's the moment you can write anything, even if it's just random noise.
*  That's terrifying. I mean, even without, even without that, like even some of the, you know,
*  the nanotech stuff that's coming, I think is. I don't know if you're paying attention, but
*  actually Eric Weinstein came out with the theory of everything. I mean, that came out, he's been
*  working on a theory of everything in the physics world called geometric unity. And then for me,
*  from computer science person, like you, Stephen Wolfram's theory of everything of like hypergraphs
*  is super interesting and beautiful, but that not from a physics perspective, but from a computational
*  perspective, I don't know, have you paid attention to any of that? So again, like what would make me
*  pay attention and like why, like I hate string theory is okay. Make a testable prediction,
*  right? I'm only interested in, I'm not interested in theories for their intrinsic beauty. I'm
*  interested in theories that give me power over the universe. So if these theories do, I'm very
*  interested. Can I just say how beautiful that is? Because a lot of physicists say I'm interested
*  in experimental validation and they skip out the part where they say to give me more power in the
*  universe. I just love the clarity of that. I want a hundred gigahertz processors. I want transistors
*  that are smaller than atoms. I want like power. That's true. And that's where people from aliens
*  to this kind of technology where people are worried that governments, like who owns that power?
*  Is it George Hots? Is it thousands of distributed hackers across the world? Is it governments?
*  Is it Mark Zuckerberg? There's a lot of people that, I don't know if anyone trusts
*  any one individual with power, so they're always worried. It's the beauty of blockchains.
*  That's the beauty of blockchains, which we'll talk about on Twitter. Somebody pointed me to a story,
*  a bunch of people pointed me to a story a few months ago where you went into a restaurant in
*  New York, and you can correct me if I'm wrong, and ran into a bunch of folks from a company,
*  a crypto company, who are trying to scale up Ethereum. They had a technical deadline related
*  to a solidity to OVM compiler. These are all Ethereum technologies. You stepped in,
*  they recognized you, pulled you aside, explained their problem, and you stepped in and helped them
*  solve the problem, thereby creating legend status story. Can you tell me the story in a little more
*  detail? It seems incredible. Did this happen? Yeah, yeah, it's a true story. It's a true story.
*  They wrote a very flattering account of it. The company is called Optimism,
*  it's spin off of Plasma. They're trying to build L2 solutions on Ethereum. Right now,
*  every Ethereum node has to run every transaction on the Ethereum network. This doesn't scale,
*  because if you have N computers, well, if that becomes two N computers, you actually still get
*  the same amount of compute. This is like O of 1 scaling, because they all have to run it. Okay,
*  fine, you get more blockchain security, but blockchain is already so secure. Can we trade
*  some of that off for speed? That's what these L2 solutions are. They built this thing which kind of
*  sandbox for Ethereum contracts, so they can run it in this L2 world and it can't do certain things
*  in L world, in L1. Can I ask you for some definitions? What's L2? Oh, L2 is layer two.
*  L1 is like the base Ethereum chain, and then layer two is like a computational layer that runs
*  elsewhere, but still is kind of secured by layer one. I'm sure a lot of people know,
*  but Ethereum is a cryptocurrency, probably one of the most popular cryptocurrencies, second to Bitcoin,
*  and a lot of interesting technological innovations there. Maybe you could also slip in,
*  whenever you talk about this, any things that are exciting to you in the Ethereum space.
*  And why Ethereum? Well, I mean, Bitcoin is not Turing complete. Ethereum is not technically
*  Turing complete with a gas limit, but close enough. With a gas limit? What's the gas limit?
*  Resources? Yeah, I mean, no computer is actually Turing complete. Right.
*  Right. You're going to find out RAM. You know, I can actually solve the whole problem.
*  What's the word gas limit? You have so many brilliant words. I'm not even going to ask.
*  That's not my word. That's Ethereum's word. Ethereum, you have to spend gas for instruction.
*  So like different opcodes use different amounts of gas, and you buy gas with ether
*  to prevent people from basically DDoSing the network.
*  So Bitcoin is proof of work. And then what's Ethereum?
*  It's also proof of work. They're working on some proof of stake Ethereum 2.0 stuff.
*  But right now it's proof of work. It uses a different hash function from Bitcoin.
*  That's more ASIC resistance because you need RAM.
*  So we're all talking about Ethereum 1.0. So what were they trying to do to scale this whole process?
*  So they were like, well, if we could run contracts elsewhere,
*  and then only save the results of that computation, you know, well, we don't actually
*  have to do the compute on the chain. We can do the compute off chain and just post what the results
*  are. Now, the problem with that is, well, somebody could lie about what the results are.
*  So you need a resolution mechanism. And the resolution mechanism can be really expensive
*  because, you know, you just have to make sure that like the person who is saying, look,
*  I swear that this is the real computation. I'm staking $10,000 on that fact.
*  And if you prove it wrong, yeah, it might cost you $3,000 in gas fees to prove wrong,
*  but you'll get the $10,000 bounty. So you can secure using those kinds of systems.
*  So it's effectively a sandbox which runs contracts. And like, just like any kind of normal
*  sandbox, you have to like replace syscalls with, you know, calls into the hypervisor.
*  Sandbox, syscalls, hypervisor. What do these things mean?
*  As long as it's interesting to talk about.
*  Yeah. I mean, you can take like the Chrome sandbox is maybe the one to think about, right?
*  So the Chrome process is doing a rendering. Can't, for example, read a file from the file system.
*  Yeah.
*  It has, if it tries to make an open syscall in Linux, the open syscall, you can't make it open
*  syscall. No, no, no. You have to request from the kind of hypervisor process or like, I don't know
*  what's calling Chrome, but the, hey, could you open this file for me? And then it does all these
*  checks and then it passes the file handle back in if it's approved. So that's, yeah.
*  So what's the, in the context of Ethereum, what are the boundaries of the sandbox that we're talking
*  about? Well, like one of the calls that you actually reading and writing any state to the
*  Ethereum contract or to the Ethereum blockchain. Writing state is one of those calls that you're
*  going to have to sandbox in layer two, because if you let layer two just arbitrarily write to the
*  Ethereum blockchain. So layer two is really sitting on top of layer one. So you're going to
*  have a lot of different kinds of ideas that you can play with. Yeah. And they're all, they're not
*  fundamentally changing the source code level of Ethereum. Well, you have to replace a bunch of
*  calls with calls into the hypervisor. So instead of doing the syscall directly, you replace it with a
*  call to the hypervisor. So originally they were doing this by first running the solidity as the
*  language that most Ethereum contracts are written in. It compiles to a bytecode. And then they wrote
*  this thing they called the transpiler. And the transpiler took the bytecode and it transpiled
*  it into OVM safe bytecode. Basically bytecode that didn't make any of those restricted syscalls and
*  added the calls to the hypervisor. This transpiler was a 3000 line mess. And it's hard to do. It's
*  hard to do if you're trying to do it like that, because you have to kind of like deconstruct the
*  bytecode, change things about it and then reconstruct it. And I mean, as soon as I hear this,
*  I'm like, well, why don't you just change the compiler? Right? Why not the first place you
*  build the bytecode, just do it in the compiler? So yeah, you know, I asked them how much they wanted
*  it. Of course, measured in dollars and a wing mill. Okay. And you wrote the compiler. I modified,
*  I wrote a 300 line diff to the compiler. It's open source. You can look at it. Yeah, it's yeah. I
*  looked at the code last night. It's cute. Yeah, exactly. Cute is a good word for it. And it's
*  C++. So when asked how you were able to do it, you said, you just got to think and then do it right.
*  So can you break that apart a little bit? What's your process of one, thinking and two, doing it
*  right? You know, the people I was working for amused that I said that. It doesn't really mean
*  anything. Okay. I mean, is there some deep, profound insights to draw from like how you
*  problem solve from that? This is always what I say. I'm like, do you want to be a good programmer?
*  Do it for 20 years. Yeah. There's no shortcuts. No. What are your thoughts on crypto in general? So
*  what parts technically or philosophically do you find especially beautiful? Maybe.
*  Oh, I'm extremely bullish on crypto long term, not any specific crypto project, but this idea of,
*  well, two ideas. One, the Nakamoto consensus algorithm is, I think, one of the greatest
*  innovations of the 21st century. This idea that people can reach consensus, you can reach a group
*  consensus using a relatively straightforward algorithm is wild. And like, you know,
*  Satoshi Nakamoto, people always ask me who I look up to. It's like whoever that is.
*  Who do you think it is? Elon Musk? Is it you?
*  It is definitely not me. And I do not think it's Elon Musk. But yeah, this idea of our groups
*  reaching consensus in a decentralized yet formulaic way is one extremely powerful idea from crypto.
*  Maybe the second idea is this idea of smart contracts. When you write a contract
*  between two parties, any contract, this contract, if there are disputes, it's interpreted by lawyers.
*  Lawyers are just really shitty overpaid interpreters. Let's compare a lawyer to Python.
*  I never thought of it that way. It's hilarious.
*  So Python, I'm paying even 10 cents an hour. I'll use the nice Azure machine. I can run Python for
*  10 cents an hour. Lawyers cost $1,000 an hour. So Python is 10,000x better on that axis. Lawyers
*  don't always return the same answer. Python almost always does.
*  Cost.
*  Yeah. I mean, just cost, reliability, everything about Python is so much better than lawyers.
*  So if you can make smart contracts, this whole concept of code is law.
*  I love and I would love to live in a world where everybody accepted that fact.
*  So maybe you can talk about what smart contracts are.
*  So let's say we have even something as simple as a safety deposit box.
*  Safety deposit box that holds a million dollars. I have a contract with the bank that says two out
*  of these three parties must be present to open the safety deposit box and get the money out.
*  So that's a contract with the bank and it's only as good as the bank and the lawyers.
*  Let's say somebody dies and now, oh, we're going to go through a big legal dispute about whether,
*  oh, well, was it in the will? Was it not in the will? It's just so messy. And the cost
*  to determine truth is so expensive versus a smart contract, which just uses cryptography
*  to check if two out of three keys are present. Well, I can look at that and I can have certainty
*  in the answer that it's going to return. And that's what all businesses want is certainty.
*  You know, they say businesses don't care. Viacom YouTube. YouTube's like,
*  look, we don't care which way this lawsuit goes. Just please tell us so we can have certainty.
*  I wonder how many agreements in this book, because we're talking about financial transactions only
*  in this case, correct? The smart contracts. Oh, you can go to anything. You can go. You
*  could put a prenup in the theory of blockchain. Married smart contracts. Sorry, divorce lawyers.
*  You're going to be replaced by Python. OK, so that's another beautiful idea. Do you think
*  there's something that's appealing to you about any one specific implementation?
*  So if you look 10, 20, 50 years down the line, do you see any like Bitcoin, Ethereum,
*  any of the other hundreds of cryptocurrencies winning out? Is there like, what's your intuition
*  about the space? Are you just sitting back and watching the chaos and look who cares what emerges?
*  Oh, I don't, I don't speculate. I don't really care. I don't really care which one of these
*  projects wins. I'm kind of in the Bitcoin is a meme coin camp. I mean, why does Bitcoin have
*  value? It's technically kind of, you know, not great. Like the block size debate. When I found
*  out what the block size debate was, I'm like, are you guys kidding? What's the block size debate?
*  You know what? It's really, it's too stupid to even talk. People can look it up, but I'm like,
*  wow, you know, Ethereum seems the governance of Ethereum seems a much better. I've come around
*  a bit on proof of stake ideas. You know, very smart people thinking about some things.
*  Yeah. You know, governance is interesting. It does feel like Vitalik. Like it does feel like an open
*  even in these distributed systems, leaders are helpful because they kind of help you drive the
*  mission and the vision and they put a face to a project. It's a weird thing about us humans.
*  Geniuses are helpful. Like the tablet. Yeah. Brilliant.
*  Leaders are not necessarily. Yeah. So you think the reason he's a, he's the face
*  of a theorem is cause he's a genius. That's interesting. I mean, that was,
*  um, it's interesting to think about that. We need to create systems in which, uh,
*  the quote unquote leaders that emerge are the geniuses in the system.
*  I mean, that's arguably why the current state of democracy is broken is the people who are
*  emerging as the leaders are not the most competent, are not the superstars of the system.
*  And it seems like at least for now in the crypto world, oftentimes the leaders are the superstars.
*  Imagine at the debate, they asked, what's the sixth amendment? What are the four fundamental
*  forces in the universe? What's the integral of two to the X? Yeah. I'd love to see those questions
*  asked. And that's what I want as our leader. It's a little bit of Bayes rule. Yeah. I mean, even,
*  oh, wow. You're hurting my brain. It's that my standard was even lower, but I would have loved
*  to see just as basic brilliance. Like I've talked to historians, there's just these,
*  they're not even like, they don't have a PhD or even education history. They just, uh,
*  like a Dan Carlin type character who just like, holy shit, how did all this information get into
*  your head? They're able to just connect a Genghis Khan to the entirety of the history of the 20th
*  century. They know everything about every single battle that happened. And they know the,
*  the, the, like the game of Thrones of the, of the different power plays and all that happened there.
*  And they know like the individuals and all the documents involved. And it's, and they integrate
*  that into their regular life. It's not like they're ultra history nerds. They're just,
*  they know this information. That's what competence looks like. Yeah. Cause I've seen that with
*  programmers too. Like that's what great programmers do. But yeah, it would be, uh,
*  it's really unfortunate that those kinds of people aren't emerging as, as our leaders,
*  but for now, at least in the crypto world, that seems to be the case. I don't know if that always,
*  uh, you could imagine that in a hundred years, it's not the case. Right.
*  Crypto world has one very powerful idea going forward. And that's the idea of forks.
*  Right. I mean, uh, you know, imagine, uh, we'll use a less controversial example. Um, this was
*  actually in my joke, uh, app in 2012. I was like, Barack Obama, Mitt Romney, let's let them both be
*  president. Right. Like imagine we could fork America and just let them both be president. And
*  then the Americas could compete and you know, people could invest in one, pull their liquidity
*  out of one, put it in the other. You have this in the crypto world, Ethereum forks into Ethereum
*  and Ethereum classic. And you can pull your liquidity out of one and put it in another
*  and people vote with their dollars. Um, which forks companies should be able to fork. I'd love to
*  fork Nvidia, you know? Yeah. Like different business strategies and then try them out and see,
*  see what works. Like even take, uh, uh, yeah, take comma AI that closes its source and then
*  take one that's open source and see what works. Take one that's purchased by GM and one that
*  remains Android renegade and all these different versions and see the beauty of comma AI. Someone
*  can actually do that. Yeah. Please take comma AI and fork it. That's right. That's the beauty of
*  open source. So you're, I mean, we'll talk about autonomous vehicle space, but it does seem that
*  you're really knowledgeable about a lot of different topics. So the natural question,
*  a bunch of people ask this, which is, uh, how do you keep learning new things? Do you have like
*  practical advice if you were to introspect, like taking notes, allocate time, or do you just mess
*  around and just allow your curiosity to drive? I'll write these people a self-help book and I'll
*  charge $67 for it. I will, I will write, I will write chapter one. I will write on the cover of
*  the self-help book. All of this advice is completely meaningless. You're going to be a sucker and buy
*  this book anyway. And the one lesson that I hope they take away from the book is that I can't give
*  you a meaningful answer to that. That's interesting. Let me translate that is you haven't really
*  thought about what it is you do systematically because you could reduce it. And there's some
*  people, I mean, I've met brilliant people that, um, this is really clear with athletes. Some are
*  just, you know, the best in the world at something and they, they have zero interest in writing a
*  like a self-help book or how to master this game. And then there's some athletes who
*  become great coaches and they love the analysis, perhaps the over analysis and you right now,
*  at least at your age, which is an interesting, you're in the middle of the battle. You're like
*  the warriors that have zero interest in writing books. Uh, so you're in the middle of the battle.
*  So you have, yeah, this is, this is a fair point. I do think I have a certain aversion
*  to, um, this kind of deliberate intentional way of living life.
*  You're eventually the hilarity of this, especially since this is recorded,
*  it will have revealed beautifully the absurdity when you finally do publish this book.
*  And I guarantee you, you will. The story of comma AI would be, maybe it'll be a biography
*  written about you. That'll be, that'll be better. I guess you might be able to learn some cute
*  lessons if you're starting a company like comma AI from that book. But if you're asking generic
*  questions, like how do I be good at things? Dude, I don't know. Well, learn. I mean, the
*  interesting do them a lot. I do them a lot, but the interesting thing here is learning things
*  outside of your current trajectory, which is what it feels like from an outsider's perspective. I
*  mean that, uh, you know, that, I don't know if there's advice on that, but it is an interesting
*  curiosity when you become really busy, you're running a company.
*  Hard time.
*  Yeah. But like there's a natural inclination and trend, like just the, the, the momentum of life
*  carries you into a particular direction of wanting to focus. And this kind of dispersion
*  that curiosity can lead to gets harder and harder with time. Cause you're, you get really good at
*  certain things and it sucks trying things that you're not good at, like trying to figure them
*  out. I mean, you do this with your life streams is you're on the fly figuring stuff out. You don't
*  mind looking dumb. You just figured out, figured out pretty quickly. Sometimes I try things and I
*  don't figure them out. My chest rating is like a 1400 despite putting like a couple hundred hours
*  in it's pathetic. I mean, to be fair, I know that I could do it better if I did it better, like don't
*  play, you know, don't play five minute games, play 15 minute games at least. Like I know these things,
*  but it just doesn't, it doesn't stick nicely in my knowledge tree. All right. Let's talk about
*  comma AI. What's the mission of the company? Let's like look at the biggest picture.
*  Oh, I have an exact statement. Solve self-driving cars while delivering shippable intermediaries.
*  So long-term vision is have fully autonomous vehicles and make sure you're making money
*  along the way. I think it doesn't really speak to money, but I can talk, I can talk about what
*  solve self-driving cars means. So self-driving cars of course means you're not building a new
*  car. You're building a person replacement. That person can sit in the driver's seat and drive you
*  anywhere a person can drive with a human or better level of safety, speed, quality comfort.
*  And what's the second part of that? Delivering shippable intermediaries is well, it's a way to
*  fund the company. That's true, but it's also a way to keep us honest. If you don't have that,
*  it is very easy with this technology to think you're making progress when you're not.
*  I've heard it best described on hacker news as you can set any arbitrary milestone,
*  meet that milestone and still be infinitely far away from solving self-driving cars.
*  So it's hard to have like real deadlines when you're like Cruz or Waymo,
*  when you don't have revenue. Is that, I mean, is revenue essentially
*  the thing we're talking about here? Revenue is, capitalism is based around consent. Capitalism,
*  the way that you get revenue is real capitalism, commas in the real capitalism camp. There's
*  definitely scams out there, but real capitalism is based around consent. It's based around this
*  idea that like, if we're getting revenue, it's because we're providing at least that much value
*  to another person. When someone buys a thousand dollar comma two from us, we're providing them
*  at least a thousand dollars of value where they wouldn't buy it. Brilliant. So can you give a
*  world wind overview of the products that ComA.I provides like throughout its history and today?
*  I mean, yeah, the past ones aren't really that interesting. It's kind of just been refinement
*  of the same idea. The real only product we sell today is the comma two. Which is a piece of
*  hardware with cameras. So the comma two, I mean, you can think about it kind of like a person,
*  you know, in future hardware will probably be even more and more person like. So it has,
*  you know, eyes, ears, a mouth, a brain, and a way to interface with the car.
*  Does it have consciousness? Just kidding. That was a trick question. I don't have consciousness
*  either. Me and the comma two are the same. You're the same? I have a little more compute than it.
*  It only has like the same compute as a B. You're more efficient energy wise for the compute you're
*  doing. Far more efficient energy wise. 20 pay to flops, 20 wants. Crazy. You lack consciousness.
*  Sure. Do you fear death? You do. You want immortality. Of course I fear death. Does
*  ComA.I fear death? I don't think so. Of course it does. It very much fears well, it fears negative
*  loss. Oh yeah. Okay. So comma two, when did that come out? That was a year ago? No, two.
*  Early this year. Wow. Time. It feels like, yeah. 2020 feels like it's taking 10 years to get to the
*  end. It's a long year. It's a long year. So what's the sexiest thing about comma two feature wise?
*  So I mean, maybe you can also linger on like, what is it? Like what's its purpose? Cause there's a
*  hardware, there's a software component. You've mentioned the sensors, but also like what is
*  its features and capabilities? I think our slogan summarizes it well. A comma slogan is make driving
*  chill. I love it. Okay. Yeah. I mean it is, you know, if you like cruise control, imagine cruise
*  control, but much, much more. So it can do adaptive cruise control things, which is like slow down for
*  cars in front of it, maintain a certain speed, and it can also do lane keeping. So staying in the lane
*  and do it better and better and better over time. It's very much machine learning based.
*  So there's cameras, there's a driver facing camera too. What else is there? What am I thinking? So the
*  hardware versus software, so open pilot versus the actual hardware of the device. What's, can you
*  draw that distinction? What's one, what's the other? I mean, the hardware is pretty much a cell phone
*  with a few additions, a cell phone with a cooling system and with a car interface connected to it.
*  And by cell phone, you mean like Qualcomm, Snapdragon. Yeah. The current hardware is a
*  Snapdragon 821. It has a wifi radio, it has an LTE radio, it has a screen.
*  We use every part of the cell phone. And then the interface with the car is specific to the car. So
*  you keep supporting more and more cars. Yeah. So the interface to the car, I mean, the device itself
*  just has four CAN buses, has four CAN interfaces on it that are connected through the USB port to the
*  phone. And then, yeah, on those four CAN buses, you connect it to the car and there's a little
*  harness to do this. Cars are actually surprisingly similar. So CAN is the protocol by which cars
*  communicate. And then you're able to read stuff and write stuff to be able to control the car,
*  depending on the car. So what's the software side? What's open pilot? So I mean, open pilot is,
*  the hardware is pretty simple compared to open pilot. Open pilot is, well, so you have a machine
*  learning model, which it's in open pilot. It's a blob. It's just a blob of weights. It's not like
*  people are like, oh, it's closed source. I'm like, it's a blob of weights. What do you expect?
*  Primarily neural network based. Well, open pilot is all the software kind of around that neural
*  network. That if you have a neural network that says, here's where you want to send the car,
*  open pilot actually goes and executes all of that. It cleans up the input to the neural network. It
*  cleans up the output and executes on it. So connects. It's the glue that connects everything
*  together. Runs the sensors, does a bunch of calibration for the neural network, deals with
*  if the car is on a banked road, you have to counter steer against that. And the neural
*  network can't necessarily know that by looking at the picture. So you do that with other sensors
*  and fusion and localizer. Open pilot also is responsible for sending the data up to our servers
*  so we can learn from it, logging it, recording it, running the cameras, thermally managing the
*  device, managing the disk space on the device, managing all the resources on the device.
*  So what, since we last spoke, I don't remember when, maybe a year ago, maybe a little bit longer.
*  How has open pilot improved? We did exactly what I promised you. I promised you that by the end of
*  the year, you'd be able to remove the lanes. The lateral policy is now almost completely end to end.
*  You can turn the lanes off and it will drive slightly worse on the highway if you turn the
*  lanes off, but you can turn the lanes off and it will drive well trained completely end to end on
*  user data. And this year we hope to do the same for the longitudinal policy. So that's the
*  interesting thing is you're not doing, you don't appear to be, you can correct me, you don't appear
*  to be doing lane detection or lane marking detection or kind of the segmentation task or
*  any kind of object detection task. You're doing what's traditionally more called like end to end
*  learning. So entrained on actual behavior of drivers when they're driving the car manually.
*  This is hard to do. You know, it's not supervised learning.
*  Yeah. But the, so the nice thing is there's a lot of data. So it's hard and easy, right?
*  It's a, we have a lot of high quality data. Yeah. Like more than you need in the center. Well,
*  we have way more than we do. We have way more data than we need. I mean, it's, it's an interesting
*  question actually, because in terms of amount, you have more than you need, but the, you know,
*  driving is full of edge cases. So how do you select the data you train on? I think this is an
*  interesting open question. Like what's, what's the cleverest way to select data? That's the
*  question Tesla is probably working on. That's, I mean, the entirety of machine learning can be,
*  they don't seem to really care. They just kind of select data, but I feel like that if you want to
*  solve, if you want to create intelligent systems, you have to pick data well. Right. And so do you
*  have any hints, ideas of how to do it? Well, so in some ways that is the definition I like of
*  reinforcement learning versus supervised learning in supervised learning, the weights depend on the
*  data. Right. And this is obviously true, but the, in reinforcement learning, the data depends on the
*  weights. Yeah. And actually both ways. That's poetry. So how does it know what data to try and
*  know? Well, let it pick. We're not there yet, but that's the eventual. So you're thinking this
*  almost like a reinforcement learning framework. We're going to do RL on the world.
*  Every time a car makes a mistake, user disengages. We train on that and do RL in the world,
*  ship out a new model. That's an epoch, right? And for now you're not doing the Elon style,
*  promising that it's going to be fully autonomous. You really are sticking to level two and like,
*  it's supposed to be supervised. Oh, it is definitely supposed to be supervised. And we
*  enforce the fact that it's supervised. We look at our rate of improvement in disengagements.
*  OpenPilot now has an unplanned disengagement about every a hundred miles. This is up from 10 miles,
*  like maybe, maybe, uh, maybe a year ago. Yeah. So maybe we've seen 10 X improvement in a year,
*  but a hundred miles is still a far cry from the hundred thousand you're going to need.
*  So you're going to somehow need to get, um, three more 10 X's in there.
*  And you're, what's your intuition? You're basically hoping that there's exponential
*  improvement built into the baked into the cake somewhere.
*  Well, that's even, I mean, 10 X improvement, that's already assuming exponential, right?
*  There's definitely exponential improvement. And I think when Elon talks about exponential,
*  like these things, these systems are going to exponentially improve. Just exponential doesn't
*  mean you're getting a hundred gigahertz processors tomorrow, right? Like it's going to still take a
*  while because the gap between even our best system and humans is still large.
*  So that's an interesting distinction to draw. So if you look at the way Tesla is approaching the
*  problem and the way you're approaching the problem, which is very different than the rest of the
*  self-driving car world. So let's put them aside is you're treating most of the driving task as a
*  machine learning problem. And the way Tesla is approaching it is with the multitask learning,
*  you break the task of driving into hundreds of different tasks and you have this multi-headed
*  neural network that's very good at performing each task. And there's presumably something on top
*  that's stitching stuff together in order to make control decisions, policy decisions about how you
*  move the car. But what that allows you, there's a brilliance to this because it allows you to
*  master each task like lane detection, stop sign detection, traffic light detection,
*  drivable area segmentation, vehicle bicycle, pedestrian detection. There's some localization
*  tasks in there. Also predicting how the entities in the scene are going to move.
*  Everything is basically a machine learning task. Whether it's a classification, segmentation,
*  prediction. And it's nice because you can have this entire data engine that's mining for edge cases
*  for each one of these tasks. And you can have people like engineers that are basically masters
*  of that task. They become the best person in the world at, as you talk about the cone guy for
*  Waymo, the become the best person in the world at cone detection. So that's a compelling notion
*  from a supervised learning perspective. Automating much of the process of edge case discovery and
*  retraining neural network for each of the individual perception tasks. And then you're looking at the
*  machine learning in a more holistic way, basically doing end-to-end learning on the driving tasks.
*  Supervised trained on the data of the actual driving of people they use, AI. Like actual human
*  drivers doing manual control plus the moments of disengagement that maybe with some labeling
*  could indicate the failure of the system. So you have a huge amount of data for positive control
*  of the vehicle, like successful control of the vehicle, both maintaining the lane as I think
*  you're also working on, longitudinal control of the vehicle and then failure cases where the
*  vehicle does something wrong that needs disengagement. So like what, why do you think
*  you're right and Tesla is wrong on this? And do you think you'll come around the Tesla way?
*  Do you think Tesla will come around to your way?
*  If you were to start a chess engine company, would you hire a Bishop guy?
*  See, we have, this is Monday morning quarterbacking is yes, probably.
*  So, Oh, our rook guy. Oh, we stole the rook guy from that company. Oh, we're going to have real
*  good rooks. Well, there's not many pieces, right? You can, uh, there's not many guys and gals to
*  hire. You just have a few that work in the Bishop, a few that work in the rook. But is that not
*  ludicrous today to think about in a world of alpha zero? But alpha zero is a chess case. So the,
*  the fundamental question is how hard is driving compared to chess? Because so long term end to end
*  will be the right solution. The question is how many years away is that?
*  And that's going to be the only solution for level five for the only way we get that.
*  And of course, Tesla is going to come around to my way. And if you're a rook guy out there, I'm sorry.
*  The cone guy. I don't know. We're going to specialize each task. We're going to really
*  understand rook placement. Yeah. I understand the intuition you have. I mean, that,
*  that, uh, is very compelling notion that we can learn the task end to end, like the same compelling
*  notion you might have for natural language conversation. But I'm not sure. Because one
*  thing you sneaked in there is the assertion that it's impossible to get to level five without this
*  kind of approach. I don't know if that's obvious. I don't know if that's obvious either. I don't
*  actually mean that. I think that it is much easier to get to level five with an end to end approach.
*  I think that the other approach is doable, but the magnitude of the engineering challenge may
*  exceed what humanity is capable of. So, but what do you think of the Tesla data engine approach,
*  which to me is an active learning task is kind of fascinating is, is breaking it down into these
*  multiple tasks and mining their data constantly for like edge cases for these different tasks.
*  Yeah. But the tasks themselves are not being learned. This is feature engineering.
*  I mean, it's, it's, uh, it's a higher abstraction level of feature engineering for the different
*  tasks. It's task engineering in a sense. It's slightly better feature engineering,
*  but it's still fundamentally is feature engineering. And if anything about the history
*  of AI has taught us anything, it's that feature engineering approaches will always be replaced
*  and lose to end to end. Now, to be fair, I cannot really make promises on timelines,
*  but I can say that when you look at the code for stockfish and the code for alpha zero,
*  one is a lot shorter than the other, a lot more elegant, required a lot less programmer hours to
*  write. Yeah, but there was a lot more murder of bad, uh, agents on the, uh, alpha zero side.
*  By murder, I mean, uh, agents that played a game and failed miserably. Yeah. Oh,
*  oh, in simulation that failure is less costly in real world. It's,
*  do you mean in practice? Like alpha zero has lost games miserably. No, I haven't seen that. No,
*  but I know, but the, the, the, the requirement for alpha zero is a simulator to be able to like
*  evolution, human evolution, not human evolution, biological evolution of life on earth from the
*  origin of life has murdered trillions upon trillions of organisms on the path to us humans. Yeah. So
*  the question is, can, can we, uh, stitch together a human like object without having to go through
*  the entirety process of evolution? Well, no, but do the evolution and simulation. Yeah,
*  that's the question. Can we simulate, so do you have a sense that it's possible to simulate some
*  as you zero is exactly this new zero is, is the solution to this new zero I think is going to
*  be looked back as the canonical paper. And I don't think deep learning is everything. I think that
*  there's still a bunch of things missing to get there, but new zero I think is going to be looked
*  back as the kind of cornerstone paper of this whole deep learning era. And new zero is the
*  solution to self-driving cars. You have to make a few tweaks to it, but new zero does effectively
*  that it does those rollouts and those murdering in, in a learned simulator and a learned dynamics
*  model. I was, it's interesting. It doesn't get enough love that I was blown away when I, I was
*  blown away when I read that paper. I'm like, you know, okay, I've always said a comma, I'm going to
*  sit and I'm going to wait for the solution to self-driving cars to come along. This year I saw
*  it. It's me zero. So, uh, sit back and let the winning roll in. So your sense, just to
*  elaborate a little bit to link on the topic, your sense is neural networks will solve driving. Yes.
*  Like we don't need anything else. I think the same way chess was maybe the chess and maybe Google are
*  the pinnacle of like search algorithms and things that look kind of like a star. Um, the pinnacle
*  of this error is going to be self-driving cars. But on the, on the path that you have to deliver
*  products and it's possible that the path to full self-driving cars will take decades. I doubt it.
*  How long would you put on it? Like what, what are we, you're chasing it. Tesla's chasing it.
*  What are we talking about? Five years, 10 years, 50 years in the 2020s,
*  in the 2020s, the later part of the 2020s.
*  With the neural network. Well, that would be nice to see. And on the path to that,
*  you're delivering products, which is a nice L2 system. That's what Tesla's doing. A nice L2 system
*  just gets better every time. L2. The only difference between L2 and the other levels is who
*  takes liability. And I'm not a liability guy. I don't want to take liability. I'm level two forever.
*  Hmm. Now on that little transition, I mean,
*  how do you make the transition work? Is, uh, is this where driver sensing
*  comes in? Like, how do you make the, cause you said a hundred miles, like, is, is there some
*  sort of human factor psychology thing where people start to overtrust the system, all those kinds of
*  effects once it gets better and better and better and better, they get lazier and lazier and lazier.
*  Is that like, how do you get that transition? Right. First off, our monitoring is already
*  adaptive. Our monitoring has already seen adaptive driver monitoring. Is this the camera that's
*  looking at the driver? You have an infrared camera in the, our policy for how we enforce the driver
*  monitoring is seen adaptive. What's that mean? Well, for example, in one of the extreme cases,
*  um, if you, uh, if the car is not moving, we do not, uh, actively enforce driver monitoring.
*  Right. Um, if you are going through a, uh, like a 45 mile an hour road with lights, um, and stop
*  signs and potentially pedestrians, we enforce a very tight driver monitoring policy. If you are
*  alone on a perfectly straight highway, um, and this is, it's all machine learning. None of that
*  is hand coded. Actually the stop is hand coded, but. So there's some kind of machine learning
*  estimation of risk. Yes. Yeah. I mean, I've always been a huge fan of that. That that's a,
*  because, uh, it's difficult to do every step into that direction is a worthwhile step to take. It
*  might be difficult to do really well. Like us humans are able to estimate risk pretty damn well,
*  whatever the hell that is. That feels like one of the nice features of us humans. Uh, cause like
*  we humans are really good drivers when we're really like tuned in and we're good at estimating
*  risk. Like when are we supposed to be tuned in? Yeah. And you know, people are like, oh, well,
*  you know, why would you ever make the driver monitoring policy less aggressive? Why would
*  you always not keep it at its most aggressive? Because then people are just going to get
*  fatigued from it. Yes. When they get annoyed, you want them, you want, you want the experience to be
*  pleasant. Obviously I want the experience to be pleasant, but even just from a straight up safety
*  perspective, if you alert people, when they look around and they're like, why is this thing alerting
*  me? There's nothing I could possibly hit right now. People will just learn to tune it out.
*  People will just learn to tune it out, to put weights on the steering wheel, to do whatever,
*  to overcome it. And remember that you're always part of this adaptive system. So all I can really
*  say about, you know, how this scale is going forward is yeah, something we have to monitor for.
*  We don't know. This is a great psychology experiment at scale. Like we'll see. Yeah. It's
*  fascinating. Track it and making sure you have a good understanding of attention
*  is a very key part of that psychology problem. Yeah. I think you and I probably have a different,
*  come to it differently, but to me it's an, it's a fascinating psychology problem to explore something
*  much deeper than just driving. It's a, it's such a nice way to explore human attention
*  and human behavior, which is why, again, we've probably both criticized Mr. Elon Musk
*  on this one topic from different avenues. So both offline and online, I had little chats with Elon and
*  like, I love human beings as a, as a, as a computer vision problem, as an AI problem,
*  it's fascinating. He wasn't so much interested in that problem. It's like in order to solve driving,
*  the whole point is you want to remove the human from the picture.
*  And it seems like you can't do that quite yet. Eventually. Yes. But you can't quite do that yet.
*  So this is the moment where you can't yet say, I told you so, uh, to Tesla,
*  but it's, it's getting there because I don't know if you've seen this, there's some reporting that
*  they're in fact starting to do driver model. They ship the model in shadow mode, uh, with the,
*  I believe only a visible light camera. It's a, it might even be fisheye. Uh, it's like a low
*  resolution, low resolution, visible light. I mean, to be fair, that's what we have in the Eon as
*  well. Our last generation product. This is the one area where I can say our hardware is ahead of
*  Tesla. The rest of our hardware way, way behind, but our driver monitoring camera.
*  So you think, uh, I think, um, uh, third row Tesla podcast or somewhere else, I've heard you say that
*  obviously eventually they're going to have driver monitoring.
*  I think what I've said is Elon will definitely ship driver monitoring before he ships level five.
*  Before level five. And I'm willing to bet 10 grand on that. And you bet 10 grand on that.
*  I mean, now I know what to take the bet, but before maybe someone would have,
*  I should have got my money. Yeah. It's an interesting bet. I think, I, I think you're right.
*  I'm actually on a, on a human level because he's been, he's made the decision.
*  Like he said that drive monitoring is the wrong way to go, but like you have to think of, uh,
*  as a human, as a CEO, I think that's the right thing to say when like,
*  sometimes you have to say things publicly that are different than when you actually believe,
*  because when you're producing a large number of vehicles and the decision was made not to
*  include the camera, like, what are you supposed to say? Like our cars don't have the thing that I
*  think is right to have. Uh, it's an interesting thing, but like on the other side, as a CEO,
*  I mean, something you could probably speak to as a leader. I think about me as a human
*  to publicly change your mind on something. How hard is that? Well, especially when assholes like
*  George Haas say, I told you so. All I will say is I am not a leader and I am happy to change my mind.
*  And I think you on will. Yeah, I do. Uh, I think he'll come up with a good way to
*  make it psychologically okay for him. Well, it's such an important thing, man, especially for a
*  first principles thinker, cause he made a decision that, uh, driver monitoring is not the right way
*  to go. And I could see that decision and I could even make that decision. Like I was on the fence
*  too. Like I'm not a driver monitoring is such an obvious, simple solution to the problem of
*  attention. It's not obvious to me that just by putting a camera there, you solve things.
*  You have to create an incredible, compelling experience. Just like you're, you're talking
*  about it. I don't know if it's easy to do that. It's not at all easy to do that. In fact, I think
*  so as a creator of a car that's trying to create a product that people love, which is what Tesla
*  tries to do, right? It's not obvious to me that, uh, you know, as a design decision, whether adding
*  a camera is a good idea from a safety perspective either, like in the human factors community,
*  everybody says that like you should obviously have driver sensing drive monitoring, but like
*  that that's like saying it's obvious as parents, you shouldn't let your kids go out at night,
*  but okay. But like they're still going to find ways to do drugs.
*  Yeah. You have to also be good parents. So like it's, it's much more complicated than just the,
*  you need to have driver monitoring. I totally disagree on, okay, if you have a camera there
*  and the camera's watching the person, but never throws an alert, they'll never think about it.
*  Right. The, the, the driver monitoring policy that you choose to, how you choose to communicate
*  with the user is entirely separate from the data collection perspective. Right. Right.
*  So, you know, like there's one thing to say, like, you know, tell your teenager, they can't do
*  something. There's another thing to like, you know, gather the data so you can make informed
*  decisions. That's really interesting, but you have to make that. That's the interesting thing about
*  cars. Uh, but even true with common AI, like you don't have to manufacture the thing into the car
*  is you have to make a decision that anticipates the right strategy long-term. So like you have
*  to start collecting the data and start making decisions. It started, it started at three years
*  ago. I believe that we have the best driver monitoring solution in the world. Um, I think
*  that when you compare it to super cruise is the only other one that I really know that shipped
*  and ours is better. What, uh, what do you like and not like about super cruise? Um, I mean,
*  I had a few super cruise, uh, the sun would be shining through the window, would blind the
*  camera and it would say, I wasn't paying attention. I was looking completely straight.
*  I couldn't reset the attention with a steering wheel touch and super cruise would disengage.
*  Like I was communicating to the car. I'm like, look, I am here. I am paying attention. Why are
*  you really going to force me to disengage? And it did. Um, so it's, it's a constant conversation
*  with the user and yeah, there's no way to ship a system like this. If you can OTA, right, we're
*  shipping a new one every month. Sometimes we balance it with our users on discord. Like when
*  sometimes we make the driver monitoring a little more aggressive and people complain,
*  sometimes they don't, you know, we want it to be as aggressive as possible where people don't
*  complain. It doesn't feel intrusive. So being able to update the system over the air is an
*  essential component. I mean, that's probably to me, you mentioned, uh, I mean, to me, that is
*  the biggest innovation of Tesla that it, it made it. People realize that over the air updates is
*  essential. Yeah. I mean, was that not obvious from the iPhone? The iPhone was the first real
*  product that OTA'd I think. Was it actually, that's brilliant. You're right. I mean, the game
*  consoles used to not right. The game consoles were maybe the second thing that did. Wow. I
*  didn't really think about it. One of the amazing features of a smartphone isn't just like the
*  touchscreen isn't the thing. It's the ability to constantly update. Yeah, it gets better. It gets
*  better. Love my iOS 14. Yeah. Uh, well, one thing that I probably disagree with you on,
*  on driver monitoring is you said that it's easy. I mean, you tend to say stuff is easy. I'm sure
*  the, uh, I guess you said it's easy relative to the external perception problem.
*  Can you elaborate why you think it's easy? Feature engineering works.
*  For driver monitoring, feature engineering does not work for the external.
*  So human faces are not human faces and the movement of human faces and head and body
*  is not as variable as the external environment. Yeah. Is there intuition?
*  Yes. And there's another big difference as well. Um, your reliability of a driver monitoring system
*  doesn't actually need to be that high. The uncertainty, if you have something that's
*  detecting whether the human's paying attention and only works 92% of the time, you're still getting
*  almost all the benefit of that because the human, like you're training the human, right?
*  You're, you're, you're dealing with a system that's really helping you out. It's a conversation. It's
*  not like the external thing where guess what? If you swerve into a tree, you swerve into a tree,
*  right? Like you get no margin for error. Yeah. I think that's really well put. I, I think that's
*  the right, exactly the place where, um, where comparing to the external perception,
*  the control problem, the driver monitoring is easier because you don't, the bar for success is
*  much lower. Yeah. But I still think like the human face is more complicated actually than the
*  external environment, but for driving, you don't give a damn. I don't need, yeah, I don't need
*  something. I don't need something that complicated to, to, to have to communicate the idea to the
*  human that I want to communicate, which is yo system might mess up here. You got to pay attention.
*  Yeah. See that's, that's my love and fascination is the human face. And it feels like this is a nice
*  place to, um, create products that create an experience in the car. So like, it feels like
*  there should be more richer experiences in the car, you know, like that's an opportunity for
*  like something like on my eye or just any kind of system, like a Tesla or any of the autonomous
*  vehicle companies is because software is in this much more sensors and so much is on our software
*  and you're doing machine learning anyway, there's an opportunity to create totally new experiences
*  that we're not even anticipating. You don't think so? Nah. You think it's a box that gets you from A
*  to B and you want to do it chill. Yeah. I mean, I think as soon as we get to level three on highways,
*  okay, enjoy your candy crush, enjoy your Hulu, enjoy her, you know, whatever, whatever. Sure.
*  You get this. You can look at screens basically versus right now. What do you have music and
*  audio books? So level three is where you can kind of disengage in and stretches of time.
*  Well, you think level three is possible, like on the highway going for a hundred miles and you can
*  just go to sleep. Oh yeah. Uh, sleep. So again, I think it's really all on a spectrum. I think that
*  being able to use your phone while you're on the highway and like this all being okay and being
*  aware that the car might alert you and you have five seconds to basically. So the five second
*  things you think is possible. Yeah, I think it is. Oh yeah. Not, not in all scenarios, right? Some
*  scenarios it's not, but it's the whole risk thing that you mentioned is nice is to be able to estimate
*  like how risky is this situation. That's really important to understand. One other thing you
*  mentioned comparing comma and autopilot is that, um, something about the haptic feel of the way
*  comma controls the car when things are uncertain, like it behaves a little bit more uncertain when
*  things are uncertain. That's kind of an interesting point. And then autopilot is much more confident
*  always, even when it's uncertain until it runs into trouble. Yeah, that's, that's a funny thing.
*  I actually mentioned that to Elon, I think. And then the first time we talked, he wasn't biting
*  is like communicating uncertainty. I guess common doesn't really communicate uncertainty explicitly
*  communicates it through haptic feel like what's the role of communicating uncertainty? Do you think,
*  Oh, we do some stuff explicitly. Like we do detect the lanes when you're on the highway and we'll
*  show you how many lanes we're using to drive with. You can look at where it thinks the lanes are.
*  You can look at the path and we want to be better about this. We're actually hiring,
*  want to hire some new UI people. UI people. You mentioned this because it's such an,
*  it's a UI problem too, right? It's, we have, we have, we have a great designer now,
*  but you know, we need people who are just going to like build this and debug these UIs, QT people.
*  Is that what the UI is done with this QT? The new UI is in QT. C++ QT.
*  Yeah. Tesla uses it too. Yeah. We had some react stuff in there.
*  React JS or just react. React is his own language, right? React native. React native.
*  React is a JavaScript framework. Yeah. It's all, it's all based on JavaScript, but it's,
*  you know, I like C++. What do you think about, uh, dojo with Tesla and their foray into what appears
*  to be specialized hardware for our training? You know, that's, I guess it's something maybe
*  you can correct me for my shallow looking at it. It seems like something that Google did with DPUs,
*  but specialized for, uh, driving data. I don't think it's specialized for driving data.
*  It's just legit. Just TPU. They want to enter, go the Apple way. Basically everything required
*  in the chain is done in-house. Well, so you have a problem right now and this is
*  one of my, one of my concerns. I really would like to see somebody deal with this. If
*  anyone out there is doing it, I'd like to help them if I can. Um, you basically have two options
*  right now to train. Uh, your options are Nvidia or Google. Um, so Google is not even an option. Uh,
*  their TPUs are only available in Google cloud. Uh, Google has absolutely onerous terms of service
*  restrictions. Uh, they may have changed it, but back in Google's terms of service, it said
*  explicitly, you are not allowed to use Google cloud ML for training autonomous vehicles or for
*  doing anything that competes with Google without Google's prior written permission. Well, okay.
*  I mean, Google is not a platform company. Uh, I wouldn't, I wouldn't touch TPUs with a 10 foot
*  pole. So that leaves you with the monopoly. Uh, Nvidia, uh, so I mean, you're not a fan of,
*  well, look, I was a huge fan of 2016 Nvidia. Jensen came sat in the car. Um,
*  cool guy. When the stock was $30 a share, uh, Nvidia stock has skyrocketed. Um, I witnessed
*  a real change and who was in management over there in like 2018. And now they are
*  uh, let's exploit. Let's take every dollar we possibly can out of this ecosystem. Let's
*  charge $10,000 for a 100s because we know we got the best in the game. And let's charge $10,000
*  for an a 100 when it's really not that different from a 30 80, which is six 99. Um, the margins
*  that they are making off of those high end chips are so high that, I mean, I think they're shooting
*  themselves in the foot just from a business perspective, because there's a lot of people
*  talking like me now who are like, somebody's got to take Nvidia down.
*  Yeah. Where they could dominate Nvidia could be the new Intel. Yeah. To be inside everything,
*  essentially. And, and, and yet the winners in certain spaces, like autonomous driving, the
*  winners, only the people who are like desperately falling back and trying to catch up and have a
*  ton of money, like the big automakers are the ones interested in partnering with Nvidia.
*  Oh, and then I think a lot of those things are going to fall through. If I were Nvidia,
*  sell chips, sell chips at a reasonable markup to everybody, to everybody without any restrictions,
*  without any restrictions. Intel did this. Look at Intel. They had a great long run.
*  And video is trying to turn their third, like trying to productize their chips way too much.
*  They're trying to extract way more value than they can sustainably. Sure. You can do it tomorrow.
*  Is it going to up your share price? Sure. If you're one of those CEOs is like, how much can
*  I strip mine this company? And I think, you know, and that's what's weird about it too.
*  Like the CEO is the founder. It's the same guy. I mean, I still think Jensen's a great guy.
*  He is great. Why do this? You have a choice. You have a choice right now. Are you trying to cash
*  out? Are you trying to buy a yacht? If you are fine. But if you're trying to be the next huge
*  semiconductor company, sell chips. Well, the interesting thing about Jensen is he is a big
*  vision guy. So he has a plan like for 50 years down the road. So it makes me wonder like,
*  how does price gouging fit into it? Yeah. How does that like, it's, it doesn't seem to make sense.
*  The plan. I worry that he's listening to the wrong people. Yeah. That that's the sense I have too
*  sometimes. Cause I, despite everything, I think Nvidia is an incredible company. Well, one sort
*  of, I'm deeply grateful to Nvidia for the products they've created in the past. Right. And so
*  the 1080 Ti was a great GPU. Still have a lot of them. It was. Yeah. But at the same time,
*  it just feels like, it feels like you don't want to put all your stock in Nvidia. And so like Elon
*  is doing, what Tesla is doing with autopilot and Dojo is the Apple way is because they're not
*  going to share Dojo with George Hots. I know they should sell that chip. Oh, they should sell that
*  even their, their accelerator, the accelerator that's in all the cars, the 30 watt one,
*  sell it. Why not? So open it up. Make me, why does this has to be a car company?
*  Well, if you sell the chip, here's what you get. Yeah. Make some money off the chips. It doesn't
*  take away from your chip. You're going to make some money, free money. And also the world is
*  going to build an ecosystem of tooling for you. Right. You're not going to have to fix the bug
*  in your tan H layer. Someone else already did. Well, the question, that's an interesting question.
*  I mean, that's the question Steve jobs asked. That's the question Elon Musk is perhaps asking is,
*  uh, do you want Tesla stuff inside other vehicles in, inside potentially inside like, uh,
*  iRobot vacuum cleaner? Yeah. I think you should decide where your advantages are. I'm not saying
*  Tesla should start selling battery packs to automakers because battery packs to automakers,
*  they are straight up in competition with you. If I were Tesla, I'd keep the battery technology
*  totally as far as we make batteries. But the thing about the Tesla TPU, um, is anybody can build that
*  just a question of, you know, are you willing to spend the money? It could be a huge source
*  of revenue potentially. Are you willing to spend the a hundred million dollars? Right. Anyone can
*  build it and someone will. And a bunch of companies now are starting trying to build AI accelerators.
*  Somebody's going to get the idea right. And yeah, hopefully they don't get greedy because they'll
*  just lose to the next guy who finally, and then eventually the Chinese are going to make knockoff
*  and video chips. And that's from your perspective. I don't know if you're also paying attention to
*  Stan Tesla for a moment. Uh, Dave, uh, Elon Musk has talked about a complete rewrite
*  of, uh, the neural net that they're using. That seems to, again, I'm half paying attention,
*  but it seems to involve basically a kind of integration of all the sensors to where
*  it's a four dimensional view. You know, you have a 3d model of the world over time, and then you can,
*  I think it's done both for the, for the actually, you know, so the neural network is able to,
*  in a more holistic way, deal with the world and make predictions and so on, but also to make the
*  annotation task more, uh, you know, easier, like you can annotate the world in one place and it
*  kind of distributed itself across the sensors and across a different, like the hundreds of tasks
*  that are involved in the hydro net. What are your thoughts about this rewrite? Is it just like some
*  details that are kind of obvious that are steps that should be taken, or is there something
*  fundamental that could challenge your idea that end to end is the right solution? Uh, we're in
*  the middle of a big view right now as well. We're having shipped a new model in a bit. Of what kind?
*  Uh, we're going from 2d to 3d. Right now, all our stuff, like for example, when the car pitches back,
*  the lane lines also pitch back, uh, because we're assuming the flat world,
*  flat world hypothesis. Uh, the new models do not do this. The new models output everything in 3d.
*  So there's still no annotation. So the 3d is, it's more about the output. Yeah. Uh, we have,
*  we have Z's and everything. Uh, we've, yeah, we had a disease. Um, we, we unified a lot of stuff as
*  well. Uh, we switched from TensorFlow to PyTorch. Uh, my understanding of what Tesla's thing is,
*  is that their annotator now annotates across the time dimension. Uh, I mean, cute. Why are you
*  building an annotator? I find their entire pipeline. I find your vision, I mean, the vision
*  event to end very compelling, but I also like the engineering of the data engine that they've
*  created in terms of supervised learning pipelines. That thing is damn impressive. You're basically,
*  the idea is that you have hundreds of thousands of people that are doing data collection for you by
*  doing their experience. So that's kind of similar to the Kamaeai model. And you're able to mine that
*  data based on the kind of edge cases you need. I, I think it's harder to do in the end to end
*  learning the mining of the right edge cases. Like that's where feature engineering is actually
*  really powerful because like us humans are able to do this kind of mining a little better. But,
*  but yeah, there's obvious, as we, as we know, there's obvious constraints and limitations to
*  that idea. Uh, Carpathi just tweeted. He's like, um, you get really interesting insights. If you
*  sort your validation set by loss and look at the highest loss examples. Yeah. Uh, so yeah, I mean,
*  you can do, we have, we have a little data engine like thing. We're training a segnet. Um, and it's
*  not fancy. It's just like, okay, train the new segnet, run it on a hundred thousand images and
*  now take the thousand with highest loss, select a hundred of those by human, put those, get those
*  ones labeled, retrain, do it again. Right. So it's, it's a much less well-written data engine. Uh,
*  and yeah, you can, you can take these things really far and it is impressive engineering.
*  And if you truly need supervised data for a problem, yeah, things like data engine are the high end
*  of the, what is attention? Is it human paying attention? I mean, we're going to probably build
*  something that looks like data engine to push our driver monitoring further. Um, but for driving
*  itself, you have it all annotated beautifully by what the human does. So yeah, that's interesting.
*  I mean, that applies to driver attention as well. Do you want to detect the eyes? Do you want to
*  detect blinking and pupil movement? Do you want to detect all the like face alignments, the landmark
*  detection and so on, and then doing kind of reasoning based on that, or do you want to take
*  the entirety of the face over time and do end to end? I mean, it's obvious that eventually you
*  have to do end to end with some calibration, some fixes and so on, but it's, uh, like,
*  I don't know when that's the right move. Even if it's end to end, there actually is, there is no
*  kind of, um, that you have to supervise that with humans, whether a human is paying attention or
*  not is a completely subjective judgment. Um, like you can try to like automatically do it with some
*  stuff, but you don't have, if I record a video of a human, I don't have true annotations anywhere
*  in that video. The only way to get them is with, you know, other humans labeling it really. Well,
*  I don't know. Uh, you, you, so if you think deeply about it, you could, you might be able to,
*  depending on the task, maybe a discover self annotating things like, you know, you can look at
*  like steering wheel, reverse or something like that. You can discover little moments of lapse of
*  attention. I mean, that's, that's where psychology comes in. Is there indicate, cause you have so,
*  so much data to look at. So you might be able to find moments when there's like just in attention
*  that even with smartphone, if you want to detect smartphone use, you can start to zoom in. I mean,
*  that's the gold mine. That's sort of the comma AI. I mean, Tesla is doing this too, right? Is there,
*  they're doing annotation based on it's like, uh, self-supervised learning too. It's just a small
*  part of the entire picture. It's that's kind of the challenge of solving a problem in machine
*  learning. If you can discover self annotating parts of the problem, right? Our driver monitoring team
*  is half a person right now. I would, you know, once we have scaled to a full, once we have two,
*  people, once we have two, three people on that team, I definitely want to look at self-annotating
*  stuff for, for attention. Let's go back for a sec to, uh, to a comma and what, you know,
*  for people who are curious to try it out, how do you install a comma in say a 2020 Toyota Corolla
*  or like, what are the cars that are supported? What are the cars that you recommend and what does
*  it take? You have a few videos out, but maybe through words, can you explain what's the take
*  to actually install the thing? So we support, uh, I think it's 91 cars, 91 makes and models. Um,
*  we've got to a hundred this year. Nice. The, yeah, the 2020 Corolla, great choice. The, um, 2020
*  Sonata, uh, it's using the stock longitudinal. It's using just our lateral control, but it's a
*  very refined car. Their longitudinal control is not bad at all. Um, so yeah, Corolla, uh, Sonata,
*  or if you're willing to get your hands a little dirty and look in the right places on the internet,
*  the Honda Civic is great, uh, but you're going to have to install a modified EPS firmware in order
*  to get a little bit more torque. Um, and I can't help you with that. Comma does not efficiently
*  endorse that. Um, but we have been doing it. We didn't ever release it. Uh, we waited for someone
*  else to discover it. And then, you know, and you have a discord server where people, there's a very
*  active, uh, developer community as opposed to, so depending on the level of experimentation
*  you're willing to do, that's the community. If you, if you just want to buy it and you have
*  a supported car, it's 10 minutes to install. There's YouTube videos. It's Ikea furniture level.
*  If you can set up a table from Ikea, you can install a Comma 2 in your supported car and it
*  will just work. Now you're like, Oh, but I want this high-end feature or I want to fix this bug.
*  Okay. Well, welcome to the developer community. Uh, so what if I wanted to, this is something I
*  asked you offline, uh, like a few months ago, if I wanted to run my own code to, um, so use
*  Comma as a platform and try to run something like OpenPilot, what does it take to do that?
*  Um, so there's a toggle in the settings called enable SSH. And if you toggle that, you can SSH
*  into your device. You can modify the code. You can upload whatever code you want to it. Um, there's
*  a whole lot of people. So about 60% of people are running stock Comma. Uh, about 40% of people are
*  running forks. And there's a community of, there's a bunch of people who maintain these forks and
*  these forks support different cars or they have, you know, uh, different toggles. We, we try to keep
*  away from the toggles that are like disabled driver monitoring, but you know, there's some people
*  might want that kind of thing. And like, you know, yeah, you can, it's your car. It's your, I'm not
*  here to tell you, you know, uh, we, we have some, you know, we ban, if you're trying to
*  subvert safety features, you're banned from our discord. I don't want anything to do with you,
*  but there's some forks doing that. Got it. So you encourage responsible forking. Yeah. Yeah.
*  We encourage some people, you know, yeah, some people are like, like there's forks that will do,
*  um, some people just like having a lot of, uh, readouts on the UI, like a lot of like flashing
*  numbers. So there's forks that do that. Some people don't like the fact that it disengages
*  when you press the gas pedal, there's forks that disable that. Got it. Now the, the stock
*  experience is, is what like, so it does both lane keeping and longitudinal control all together.
*  So it's not separate. Like it is an autopilot. No. So, okay. Um, some cars we use the stock
*  longitudinal control. We don't do the longitudinal control in all the cars. Uh, some cars, the ACCs
*  are pretty good in the cars. It's the lane keep that's atrocious and anything except for autopilot
*  supercruise. But, you know, you just turn it on and it, it works. What does this engagement
*  look like? Yeah. So we have, I mean, I'm very concerned about mode confusion. Uh, I've
*  experienced it on supercruise and autopilot where like autopilot, like autopilot disengages. I don't
*  realize that the ACC is still on the lead car moves slightly over and then the Tesla accelerates to
*  like whatever my set speed is super fast. And like, what's going on here? Um, we have engaged
*  and disengaged and this is similar to my understanding. I'm not a pilot, but my understanding
*  is either the pilot is in control or the copilot is in control. And we have the same kind of
*  transition system, either open pilot is engaged or pilot is disengaged, engaged with cruise control,
*  disengage with either gas break or cancel. Let's talk about money. What's, uh, the business
*  strategy for comma profitable. Well, it's your, your, so congratulations. Uh, what, uh, so basically
*  selling, so we should say comma cost, uh, a thousand bucks, comma two, 200 for the interface
*  of the car as well. It's 1200. I'll send that. Nobody is usually upfront like this. You gotta,
*  you gotta add the tack on, right? Yeah. I love it. This, I'm not gonna lie to you. Trust me,
*  it will add $1,200 of value to your life. Yes. It's still super cheap. 30 days, no questions,
*  ask money back guarantee and prices are only going up. You know, if there ever is future hardware,
*  it costs a lot more than $1,200 to comma threes in the works. So it could be all I, all I will
*  say is future hardware is going to cost a lot more than the current hardware. Yeah. The people that
*  use, uh, the people I've spoken with that use comma, I use open pilot, they, first of all,
*  they use it a lot. So people that use it, they, they fall in love with our retention rate is
*  insane. Which is a good sign. Yeah. It's a really good sign. Um, 70% of comma two buyers are daily
*  active users. Yeah. It's amazing. Um, also we don't plan on stopping selling the comma two,
*  like, like it's, you know, so whatever you create that's beyond comma two, it would be, uh, it would
*  be potentially a phase shift. Like it's, it's so much better that like you could use comma two and
*  you can use comma, whatever you want. It's 3.4, one kind of 42. Yeah. You know, autopilot hardware,
*  one versus hardware to the comma two is kind of like hardware one. Got it. Got it. You can see
*  you both got it. I think I heard you talk about retention rate with a BR headsets that the average
*  is just once. Yeah. Just fast. I mean, it's such a fascinating way to think about technology.
*  And this is really, really good sign. And the other thing that people say about commas, like
*  they can't believe they're getting this 4,000 bucks, right? It's, it seems, it seems like a,
*  some kind of steal. So, uh, but in terms of like long-term business strategies that basically to
*  put, so it's currently in like a thousand plus cars, uh, 1200 more. Uh, so yeah,
*  dailies is about, uh, dailies is about 2000. Weekly is about 2500. Monthly is over 3000.
*  Wow. We've grown a lot since we last talked. Is the goal, like, can we talk crazy for a second?
*  I mean, what's the goal to overtake Tesla? Let's talk. Okay. So I mean,
*  Android did overtake. Yeah, that's exactly it. Right. So yeah, they did it. I actually don't
*  know the timeline of that one, but let, let, let's talk, uh, cause everything is in alpha now.
*  Autopilot, you could argue is an alpha in terms of towards the big mission of autonomous driving.
*  And so what, yeah, as your goal to overtake millions of cars, uh, essentially,
*  of course, where would it stop? Like it's open source software. It might not be millions of
*  cars with a piece of comma hardware, but yeah, I think open pilot at some point will cross over
*  autopilot in, in, in users, just like Android crossed over iOS. How does Google make money from
*  Android? Uh, it's, it's complicated. Their own devices make money.
*  Google, Google makes money by just kind of having you on the internet. Uh, Google search is built in
*  Gmail is built in Android is just a shill for the rest of Google's ecosystem. Yeah. But the problem
*  is Android is not, is a, is a brilliant thing. I mean, Android arguably changed the world. So
*  there you go. That's, you can, you can feel good ethically speaking, but as a business
*  strategy is questionable. So hardware, so hard. I mean, it took Google a long time to come around
*  to it, but they are now making money on the pixel. You're not about money. You're more about winning.
*  Yeah, of course. No, but if only, if only 10% of open pilot devices come from comma AI,
*  you still make a lot. That is still, yes, that is a ton of money for our company,
*  but can't somebody create a better comma using open pilot or are you basically saying,
*  well, I'll compete. Well, I'll compete. Can you create a better Android phone than the Google
*  pixel? Right. I mean, you can, but like, I love that. So you're confident, like, you know what
*  the hell you're doing. Yeah. It's, it's, uh, uh, confidence and merit. I mean, our money,
*  yeah, our money comes from working some electronics company. Yeah. And put it this way. So we sold,
*  we sold like 3000 comma twos, um, I'm at 2,500 right now. Uh, and like, okay, we're probably
*  going to sell 10,000 units next year, right? 10,000 units, even just a thousand dollars a unit. Okay.
*  We're at 10 million in, uh, in, in, in, in revenue, um, get that up to a hundred thousand,
*  maybe double the price of the unit. Now we're talking like 200 million revenue.
*  Yeah. Actually making money. Oh, uh, one of the rare semi-autonomous or autonomous vehicle
*  companies that are actually making money. Yeah. Yeah. You know, if you have, if you look at a
*  model, when we were just talking about this yesterday, if you look at a model and like,
*  you're testing, like you're AB testing your model and if you're, you're, you're one branch of the AB
*  test, the losses go down very fast in the first five epochs. Yeah. That model is probably going
*  to converge to something considerably better than the one with the losses going down slower.
*  Why do people think this is going to stop? Why do people think one day there's going to be a great,
*  like, well, Waymo is eventually going to surpass you guys. No, they're not.
*  Do you see like a world where like a Tesla or a car like a Tesla would be able to basically press
*  a button and you'd like switch to open pilot and you know, you load in? No. So I think, so first off,
*  I think that we may surpass Tesla in terms of users. I do not think we're going to surpass
*  Tesla ever in terms of revenue. I think Tesla can capture a lot more revenue per user than we can,
*  but this mimics the Android iOS model. Exactly. There may be more Android devices, but you know,
*  there's a lot more iPhones than Google pixels. So I think there'll be a lot more Tesla cars sold
*  than pieces of comma hardware. And then as far as a Tesla owner being able to switch to open pilot,
*  does iOS, does iPhones run Android? No, but you can if you really want to do it,
*  but it doesn't really make sense. Like it's not, it doesn't make sense. Who cares? What about if
*  a large company like automakers, 4GM Toyota came to George Hots or on the tech space, Amazon,
*  Facebook, Google came with a large pile of cash. Would you consider being purchased?
*  What did you see that as a one possible? Not seriously. No. I would probably
*  see how much shit they'll entertain for me. And if they're willing to like jump through a bunch of
*  my hoops, then maybe, but like, no, not the way that M&A works today. I mean, we've been approached
*  and I laugh in these people's faces. I'm like, are you kidding? Yeah. You know, because it's so,
*  it's so demeaning. The M&A people are so demeaning to companies. They treat the startup world as
*  their innovation ecosystem. And they think that I'm cool with going along with that so I can have
*  some of their scam fake fed dollars, you know, fed coin. What am I going to do with more fed coin?
*  Fed coin. Fed coin, man. I love that. So that's the cool thing about podcasting actually is
*  people criticize, I don't know if you're familiar with the Spotify giving Joe Rogan 100 million.
*  I don't know about that. And, you know, they respect, despite all the shit that people are
*  talking about Spotify, people understand that podcasters like Joe Rogan know what the hell
*  they're doing. So they give them money and say, just do what you do. And like, the equivalent for
*  you would be like, George, do what the hell you do because you're good at it. Try not to murder
*  too many people. Like, try, like there's some kind of common sense things like just don't go on a
*  weird rampage of. Yeah, it comes down to what companies I could respect, right? You know,
*  could I respect GM? Never. No, I couldn't. I mean, could I respect like a Hyundai? More so.
*  Right. That's, that's a lot closer. Toyota? What's your? Nah, nah, nah. It's like Korean is the way
*  I think. I think that, you know, the Japanese, the Germans, the U S they're all too, they're all too,
*  you know, they all think they're too great to be honest. What about the tech companies?
*  Apple? Apple is of the tech companies that I could respect. Apple is the closest. Yeah. I mean,
*  I could never. It would be ironic if, if, if common AI is, is acquired by Apple. I mean,
*  Facebook, look, I quit Facebook 10 years ago because I didn't respect the business model.
*  Google has declined so fast in the last five years. What are your thoughts about
*  Waymo as present and future? Let me, let me say, let me start by saying something nice, which is,
*  I've visited them a few times and have, have written in their cars and the engineering that
*  they're doing, both the research and the actual development and the engineering they're doing
*  and the scale they're actually achieving by doing it all themselves is really impressive.
*  And the, the balance of safety and innovation and like the cars work really well for the routes
*  they drive, like they drive fast, which was very surprising to me. Like it drives like the speed
*  limit or faster than the speed limit. It goes and it works really damn well. And the interface is
*  nice and channel Arizona. Yeah. Yeah. And challenge in a very specific environment. So it's, I, you
*  know, it gives me enough material in my mind to push back against the mad men of the world,
*  like a George Hots to be like, like, cause you kind of imply there's zero probability they're
*  going to win. Yeah. And after I've used, after I've written in it to me, it's not zero. Oh,
*  it's not for technology reasons. Bureaucracy. No, it's worse than that. It's actually for product
*  reasons. I think. Oh, you think they're just not capable of creating an amazing product?
*  No, I think that the product that they're building doesn't make sense.
*  So a few things you say the way most are fast benchmark away against a competent Uber driver.
*  Right. Right. The Uber driver's faster. It's not even about speed. It's the thing you said.
*  It's about the experience of being stuck at a stop sign because pedestrians are crossing nonstop.
*  That I like when my Uber driver doesn't come to a full stop at the stop sign. Yeah. You know,
*  full stop at the stop sign. Yeah. You know, and so let's say the way most are 20% slower than,
*  than an Uber, right? Um, you can argue that they're going to be cheaper. And I argue that users
*  already have the choice to trade off money for speed. It's called Uber pool. Um, I think it's
*  like 15% of rides at Uber pools, right? Users are not willing to trade off money for speed.
*  So the whole product that they're building is not going to be competitive
*  with traditional ride sharing networks. Right. Um, like, and also
*  whether there's profit to be made depends entirely on one company having a monopoly.
*  I think that the level for autonomous ride sharing vehicles market is going to look a lot like the
*  scooter market. If even the technology does come to exist, which I question who's doing well in
*  that market. It's a race to the bottom. Well, they could be, it could be closer to like an Uber
*  and a Lyft where it's just a one or two players. Well, the scooter people have given up trying to
*  market scooters as a practical means of transportation. And they're just like, they're
*  super fun to ride. Look at wheels. I love those things. And they're great on that front. Yeah.
*  But from an actual transportation product perspective, I do not think scooters are
*  viable and I do not think level four autonomous cars are viable. If you, um, let's play a fun
*  experiment. If you ran, let's do a Tesla and let's do Waymo. If, uh, Elon Musk took a vacation for
*  a year, he just said, screw it. I'm going to go live in an Island, no electronics. And the board
*  decides that we need to find somebody to run the company. And they, they decide that you should
*  run the company for a year. How do you run Tesla differently? I wouldn't change much.
*  Do you think they're on the right track? I wouldn't change. I mean, I'd have some
*  minor changes, but even, even my debate with Tesla about, you know, end to end versus segnats,
*  like that's just software. Who cares? Right? Like it's not going to, it's not like you're doing
*  something terrible with segnats. You're probably building something that's at least going to help
*  you debug the end to end system a lot. Right. It's very easy to transition from what they have
*  to like an end to end kind of thing. Right. Uh, and then I presume you would, uh,
*  in the model Y or maybe in the model three, you started adding driver sensing with infrared.
*  Yes, I would add, I would add, I would add infrared camera, infrared lights right away to those cars.
*  Um, and start collecting that data and do all that kind of stuff. Yeah. Very much. I think
*  they're already kind of doing it. It's, it's an incredibly minor change. If I actually were CEO
*  of Tesla, first off, I'd be horrified that I wouldn't be able to do a good job as Elon.
*  And then I would try to, you know, understand the way he's done things before. You would also have
*  to take over his Twitter. So I don't tweet. Yeah. What's your Twitter situation? Why, why,
*  why are you so quiet on Twitter? I mean, the comma is like, what, what's your social network
*  presence like? Cause you, you, on Instagram, you're, you, uh, you do live streams. You're,
*  you're, you're, um, you understand the music of the internet, but you don't always fully
*  engage into it. You're part time. I used to have a Twitter. Yeah. I mean, it's the Instagram is a
*  pretty place. Instagram is a beautiful place. It glorifies beauty. I like, I like Instagram's values
*  as a network. Um, Twitter glorifies conflict quarter glorifies, you know, like, like, like,
*  like, like, you know, just shots taking shots of people. And it's like, you know,
*  Twitter and Donald Trump are perfectly perfect for each other. So Tesla's on, uh, Tesla's on the
*  right track in your view. Yeah. Okay. So let's try, let's like really try this experiment. If you ran
*  Waymo, let's say they're, I don't know if you agree, but they seem to be at the head of the pack of
*  the kind of, uh, what would you call that approach? Like it's not necessarily lighter based because
*  it's not about lighter level four, robot taxi, level four, robot taxi, all in before any,
*  before making any revenue. Uh, so they're probably at the head of the pack. If you were
*  said, uh, Hey George, can you please run this company for a year? How would you change it?
*  Uh, I would go, I would get Anthony Levandowski out of jail and I would put him in charge of the
*  company. Um, let's try to break that apart. Why do you, do you want to make, do you want to
*  destroy the company by doing that? Or do you mean, or do you mean, uh, you like renegade style
*  thinking that, uh, pushes that, that like throws away bureaucracy and goes to first principle
*  thinking? What, what do you mean by that? Um, I think Anthony Levandowski is a genius and I think
*  he would come up with a much better idea of what to do with Waymo than me.
*  So you mean that unironically he is a genius. Oh yes. Oh, absolutely. Without a doubt. I mean,
*  I'm not saying there's no shortcomings, but in the interactions I've had with him,
*  yeah. What, um, he's also willing to take like, who knows what he would do with Waymo. I mean,
*  he's also out there like far more out there than I am. Yeah. There's big risks. What do you make
*  of him? I was, I was going to talk to him in his pockets and I was going back and forth.
*  I'm, I'm such a gullible, naive human. Like I see the best in people and I slowly started to realize
*  that there might be some people out there that like have multiple faces to the world. They're
*  like deceiving and dishonest. I still refuse to like, I, I just, I trust people and I don't
*  care if I get hurt by it, but like, you know, sometimes you have to be a little bit careful,
*  especially platform wise and podcast wise. What are you, what am I supposed to think?
*  So you think, you think he's a good person? Oh, I don't know. I don't really make moral judgments.
*  It's difficult to, I mean this about the way I actually, I mean that whole idea very non-ironically
*  about what I would do. The problem with putting me in charge of Waymo is Waymo is already $10
*  billion in the hole. Right? Whatever idea Waymo does, look, Comma's profitable, Comma's raised
*  $8.1 million. That's small, you know, that's small money. Like I can build a reasonable consumer
*  electronics company and succeed wildly at that and still never be able to pay back Waymo's 10 billion.
*  So I think the basic idea with Waymo, well forget the 10 billion because they have some backing, but
*  your basic thing is like, what can we do to start making some money?
*  Well, no, I mean my bigger idea is like whatever the idea is that's going to save Waymo,
*  I don't have it. It's going to have to be a big risk idea. And I cannot think of a better person
*  than Anthony Lewandowski to do it. So that is completely what I would do as CEO of Waymo.
*  I would call myself a transitionary CEO, do everything I can to fix that situation up.
*  Transitionary CEO. Yeah.
*  Because I can't do it. I can't, I mean, I can talk about how what I really want to do is just
*  apologize for all those corny ad campaigns and be like, here's the real state of the technology.
*  Yeah. They have several criticisms. I'm a little bit more bullish on Waymo than you seem to be,
*  but one criticism I have is it went into corny mode too early. Like it's still a startup,
*  hasn't delivered on anything. So it should be like more renegade and show off the engineering
*  that they're doing, which just can be impressive as opposed to doing these weird commercials of
*  like your friendly car company. I mean, that's my biggest, my biggest snipe at Waymo is always,
*  that guy's a paid actor. That guy's not a Waymo user. He's a paid actor. Look here,
*  I found his call sheet. Do kind of like what SpaceX is doing with the rocket launch is just
*  put the nerds up front, put the engineers up front and just like show failures too.
*  I love SpaceX's, yeah.
*  Yeah. The thing that they're doing is right. And it just feels like the right, but-
*  We're all so excited to see them succeed.
*  Yeah.
*  I can't wait to see Waymo fail. You lie to me. I want you to fail. You tell me the truth. You
*  be honest with me. I want you to succeed.
*  Yeah. Yeah. And that requires the renegade CEO.
*  Right. I'm with you. I'm with you. I still have a little bit of faith in Waymo for the renegade
*  CEO to step forward, but-
*  It's not, it's not John Kravchuk.
*  Yeah. It's, you can't-
*  It's not Chris Hempston. And those people may be very good at certain things.
*  Yeah.
*  But they're not renegades.
*  Because these companies are fundamentally, even though we're talking about billion dollars,
*  all these crazy numbers, they're still like early stage startups.
*  I mean, I just, if you are pre-revenue and you've raised $10 billion, I have no idea.
*  This just doesn't work. It's against everything Silicon Valley. Where's your minimum viable
*  product? Where's your users? Where's your growth numbers? This is traditional Silicon Valley.
*  Why do you not apply it to what you think you're too big to fail already?
*  Like, how do you think autonomous driving will change society? So the mission is for
*  karma to solve self-driving. Do you have like a vision of the world of how it'll be different?
*  Is it as simple as A to B transportation or is there like, cause these are robots.
*  It's not about autonomous driving in and of itself. It's what the technology enables.
*  I think it's the coolest applied AI problem. I like it because it has a clear path to monetary value.
*  But as far as that being the thing that changes the world, I mean, no, like there's cute things
*  we're doing in common. Like who'd have thought you could stick a phone on the windshield and it'll
*  drive. But like really the product that you're building is not something that people were not
*  capable of imagining 50 years ago. So no, it doesn't change the world in that front.
*  Could people have imagined the internet 50 years ago? Only true genius visionaries. Everyone could
*  have imagined autonomous cars 50 years ago. It's like a car, but I don't drive it.
*  See, I have this sense and I told you like I'm my long-term dream is robots with which you have
*  deep, with whom you have deep connections. And there's different trajectories towards that.
*  And I've been thinking so been thinking of launching a startup. I see autonomous vehicles
*  as a potential trajectory to that. That's not where the direction I would like to go. But I
*  also see Tesla or even common AI like pivoting into robotics broadly defined. That's at some stage in
*  the way like you're mentioning the internet didn't expect. Let's solve, you know, when I say a comma
*  about this, we could talk about this, but let's solve self-driving cars first.
*  Got to stay focused on the mission. Don't don't don't you're not too big to fail for however much
*  I think commas winning like no, no, no, no, no, you're winning when you solve level five self-driving
*  cars. And until then you haven't won and won. And, you know, again, you want to be arrogant in the
*  face of other people. Great. You want to be arrogant in the face of nature. You're an idiot.
*  Stay mission focused. Brilliant put. Like I mentioned, thinking of launching a startup,
*  I've been considering actually before COVID. I've been thinking of moving to San Francisco.
*  Oh, I wouldn't go there. So why is, uh, well, and now I'm thinking about potentially Austin
*  and we're in San Diego now, San Diego, come here. So why, what, um, I mean, you're,
*  you're such an interesting human. You've launched so many successful things. What, uh, why San
*  Diego? What do you recommend? Why not San Francisco? Have you thought so in your case,
*  San Diego with Qualcomm and staff dragon? I mean, that's an amazing combination,
*  but that wasn't really why that wasn't the why. No, I mean, Qualcomm was an afterthought. Qualcomm
*  was, it was a nice thing to think about. It's like, you can have a tech company here. A good one. I
*  mean, you know, I like Qualcomm, but no, um, well, so why San Diego better than the, why does San
*  Francisco suck? Well, so, okay. So first off, we all kind of said, like, we want to stay in California.
*  People like the ocean, you know, California for, for its flaws. It's like a lot of the flaws of
*  California are not necessarily California as a whole. And they're much more San Francisco specific.
*  Yeah. Um, San Francisco. So I think first tier cities in general have stopped wanting growth.
*  Uh, well, you have like in San Francisco, you know, the voting class always votes to not build
*  more houses because they own all the houses and they're like, well, you know, once people have
*  figured out how to vote themselves more money, they're going to do it. It is so insanely corrupt.
*  Um, it is not balanced at all, like political party wise, you know, it's, it's, it's a one party
*  city. And for all the discussion of diversity, it's has, it's stops lacking real diversity of
*  thought of background of, uh, approaches, the strategies of ideas. It's, it's kind of a strange
*  place that is the loudest people about diversity and the biggest lack of diversity.
*  I mean, that's, that's what they say, right? It's the projection projection. Yeah. Yeah. It's
*  interesting. And even people in Silicon Valley telling me that's, uh, like high up people,
*  everybody is like, this is a terrible place. It doesn't make sense. Coronavirus is really
*  what killed it. San Francisco was the number one, uh, Exodus during coronavirus.
*  We still think San Diego is a good place to be. Yeah. Yeah. I mean, we'll see, we'll see what
*  happens with California a bit longer term. Like Austin's and Austin's an interesting choice. I
*  wouldn't, I wouldn't, I don't have really anything bad to say about Austin either, except for the
*  extreme heat in the summer, um, which, but that's like very on the surface, right? I think as far as
*  like an ecosystem goes, it's cool. I personally love Colorado. Colorado is great. Uh, yeah. I mean,
*  you have these states that are, you know, like just way better run. Um, California is, you know,
*  it's especially San Francisco. It's on a tie horse and like, yeah. Can I ask you for advice
*  to me and to others about what's the take to build a successful startup? Oh, I don't know. I haven't
*  done that. Talk to someone who did that. Well, if you know, uh, this is like another book of years
*  I'll buy for $67, I suppose. Uh, so there's, um, one of these days I'll sell out. Yeah, that's right.
*  Jail breaks are going to be a dollar and books are going to be 67. How I, uh, how I jail broke
*  the iPhone by George Hots. That's right. How I jail broke the iPhone and you can do
*  in 21 days. That's right. Oh God. Okay. I can't wait. But quite so you haven't introspective,
*  you have built a very unique company. I mean, not, not you, but you and others,
*  but I don't know. Um, there's no, there's nothing you haven't interest, but you haven't really
*  sat down and thought about like, well, like if you and I were having a bunch of,
*  we're having some beers and you're seeing that I'm depressed and whatever I'm struggling,
*  there's no advice you can give. Oh, I mean more beer.
*  Yeah. I think it's all very like situation dependent. Um, here's okay. If I can give a
*  generic piece of advice, it's the technology always wins. The better technology always wins
*  and lying always loses. Build technology and don't lie.
*  I'm with you. I agree very much. Long run, long run. Sure. It's still long run. You know what?
*  The market can remain irrational longer than you can remain solvent. True fact. Well, this is,
*  this is an interesting point because I ethically and just as a human believe that, um,
*  um, like, like hype and smoke and mirrors is not at any stage of the company is a good strategy.
*  I mean, there's some like, you know, PR magic kind of like, you know,
*  Oh, I'm looking around a new product. If there's a call to action, if there's like a call to action,
*  like buy my new GPU, look at it. It takes up three slots and it's this big. It's huge. Buy my GPU.
*  Yeah, that's great. If you look at, you know, especially in that, in the AI space broadly,
*  but autonomous vehicles, like you can raise a huge amount of money on nothing. And the question to
*  me is like, I'm against that. I'll never be part of that. I don't think, I hope not willingly not,
*  but like, is there something to be said to, uh, essentially lying to raise money,
*  like fake it till you make it kind of thing? I mean, this is Billy McFarland, the fire
*  festival. Like we all, we all experienced, uh, you know, what happens with that. No,
*  no, don't fake it till you make it be honest and hope you make it the whole way. The technology
*  wins, right? The technology wins. And like there is, I'm not, you just like the anti-hype, you know,
*  that's that's a Slava KPSS reference, but, um, hype isn't necessarily bad. I loved camping out
*  for the iPhones. Um, you know, and as long as the hype is backed by like substance, as long as it's
*  backed by something I can actually buy and like it's real, then hype is great. And it's a great
*  feeling. It's when the hype is backed by lies that it's a bad feeling. I mean, a lot of people call
*  Elon Musk a fraud. How could he be a fraud? I've noticed this, this kind of interesting effect,
*  which is he does tend to over promise and deliver. What's, what's the better way to phrase it?
*  Promise a timeline that he doesn't deliver on. He delivers much later on. What do you think about
*  that? Cause I do that. I think that's a programmer thing. I do that as well. You think that's a really
*  bad thing to do or is that okay? I think that's again, as long as like you're working toward it
*  and you're going to deliver on it and it's not too far off. Right. Right. Like, like,
*  you know, the whole, the whole autonomous vehicle thing, it's like, I mean, I still think Tesla's on
*  track to beat us. I still think even with their, even with their missteps, they have advantages.
*  We don't have, um, you know, Elon is better than me at, at, at like marshaling massive amounts of
*  resources. So, you know, I still think given the fact they're maybe making some wrong decisions,
*  they'll end up winning. And like, it's fine to hype it if you're actually going to win. Right.
*  Like if Elon says, look, we're going to be landing rockets back on earth in a year and it takes four,
*  like, you know, he landed a rocket back on earth and he was working toward it the whole time. I
*  think there's some amount of like, I think what it becomes wrong is if you know, you're not going
*  to meet that deadline. If you're lying. Yeah. That's brilliantly put. Like this is what people
*  don't understand. I think like Elon believes everything he says as far as I can tell he does.
*  And I detected that in myself too. Like if I, it's only bullshit. If you, if you're like
*  conscious of yourself lying. Yeah. I think so. Yeah. Now you can't take that to such an extreme,
*  right? Like in a way, I think maybe Billy McFarland believed everything he said too.
*  Right. That's how you start a cult and then everybody kills themselves. Yeah. Yeah. Like
*  it's, you need, you need, if there's like some factor on it, it's fine. And you need some people
*  to like, you know, keep you in check, but like, if you deliver on most of the things you say and just
*  the timelines are off. Yeah. It does piss people off though. I wonder, but who cares in a long arc
*  of history, the people, everybody gets pissed off at the people who succeed, which is one of the
*  things that frustrates me about this world is they don't celebrate the success of others.
*  Like there's so many people that want Elon to fail. It's so fascinating to me. Like what
*  is wrong with you? Like, so Elon Musk talks about like people short, like they talk about financial,
*  but I think it's much bigger than the financials. I've seen like the human factors community,
*  they want, they want other people to fail. What, why, why? Like even people, the harshest thing is
*  like, you know, even people that like seem to really hate Donald Trump, they want him to fail.
*  Or like the other president, or they want Barack Obama to fail. It's like,
*  it's weird, but I want that. I would love to inspire that part of the world to change because
*  well, if the human species is going to survive, we should celebrate success.
*  But it seems like the efficient thing to do in this objective function that like we're all striving
*  for is to celebrate the ones that like figure out how to like do better at that objective function
*  as opposed to like dragging them down back into the mud. I think there is, this is the speech I
*  always give about the commenters on Hacker News. So first off, something to remember about the
*  internet in general is commenters are not representative of the population. I don't
*  comment on anything. You know, commenters are representative of a certain sliver of the population.
*  And on Hacker News, a common thing I'll see is when you'll see something that's like, you know,
*  promises to be wild out there and innovative. There is some amount of, you know, checking them
*  back to earth, but there's also some amount of, if this thing succeeds, well, I'm 36 and I've
*  worked at large tech companies my whole life. They can't succeed because if they succeed,
*  that would mean that I could have done something different with my life. But we know that I couldn't
*  have, we know that I couldn't have, and that's why they're going to fail. And they have to root
*  for them to fail to kind of maintain their world image. So tune it out.
*  And they comment, well, it's hard. So one of the things I'm considering, startup-wise, is to
*  change that. Because I think it's also a technology problem. It's a platform problem.
*  Because the thing you said most people don't comment, I think most people want to comment.
*  They just don't because it's all the assholes who are commenting.
*  Exactly. I don't want to be grouped in with them.
*  I'm not. You don't want to be at a party where everyone is an asshole.
*  But that's a platform problem. I can't believe what Reddit's become. I can't believe the group
*  thing in Reddit comments. Reddit is an interesting one because there's subreddits. And so you can
*  still see, especially small subreddits, that are little like havens of joy and positivity and
*  deep, even disagreement, but nuanced discussion. But it's only small little pockets. But that's
*  emergent. The platform is not helping that or hurting that. So I guess naturally,
*  something about the internet, if you don't put in a lot of effort to encourage
*  nuance and positive good vibes, it's naturally going to decline into chaos.
*  I would love to see someone do this well. I think it's very doable.
*  I feel like Twitter could be overthrown.
*  Yashoback talked about how if you have like and retweet, that's only positive wiring.
*  The only way to do anything negative there is with a comment. And that's like that asymmetry
*  is what gives Twitter its particular toxicness. Whereas I find YouTube comments to be much better
*  because YouTube comments have an up and a down and they don't show the downloads.
*  Without getting into depth of this particular discussion, the point is to explore possibilities
*  and get a lot of data on it. Because I mean, I could disagree with what you just said. The point
*  is it's unclear. It hasn't been explored in a really rich way. Like these questions of how to
*  create platforms that encourage positivity. I think it's a technology problem. And I think
*  we'll look back at Twitter as it is now. Maybe it'll happen within Twitter, but most likely
*  somebody overthrows them. We'll look back at Twitter and say, we can't believe we put up with
*  this level of toxicity. You need a different business model too. Any social network that
*  fundamentally has advertising as a business model, this was in the social dilemma, which I didn't
*  watch, but I liked it. It's like, there's always the, you're the product, you're not the... But
*  they had a nuanced take on it that I really liked. And it said, the product being sold is influence
*  over you. The product being sold is literally your influence on you. Like, that can't be. If
*  that's your idea, okay. Well, guess what? It cannot be toxic. Yeah. Maybe there's ways to spin it,
*  like with giving a lot more control to the user and transparency to see what is happening to them,
*  as opposed to in the shadows, it's possible. But that can't be the primary source of...
*  But the users aren't, no one's going to use that. It's not...
*  It depends. It depends. It depends. I think that you're not going to... You
*  can't depend on self-awareness of the users. It's a longer discussion because you can't depend on it,
*  but you can reward self-awareness. Like, for the ones who are willing to put in the work of
*  self-awareness, you can reward them and incentivize and perhaps be pleasantly surprised how many people
*  are willing to be self-aware on the internet. Like we are in real life. Like, I'm putting in a lot
*  of effort with you right now being self-aware about if I say something stupid or mean, I'll
*  look at your body language. Like, I'm putting in that effort. It's costly. For an introvert,
*  it's very costly. But on the internet, fuck it. Most people are like, I don't care if this hurts
*  somebody. I don't care if this is not interesting or if this is, yeah, it's mean or whatever.
*  I think so much of the engagement today on the internet is so disingenuine too. You're not doing
*  this out of a genuine, this is what you think. You're doing this just straight up to manipulate
*  others. Whether you're in... You just became an ad. Okay. Let's talk about a fun topic, which is
*  programming. Here's another book idea for you. Let me pitch. What's your perfect programming setup?
*  So like this by George Hotz. So like what, listen, you're... Give me a MacBook Air,
*  sit me in a corner of a hotel room and I'll still have food. So you really don't care. You don't
*  fetishize like multiple monitors, keyboard. Those things are nice and I'm not going to say no to them,
*  but did they automatically unlock tons of productivity? No, not at all. I have definitely
*  been more productive on a MacBook Air in a corner of a hotel room. What about IDE? So
*  which operating system do you love? What text editor do you use? IDE? Is there something that
*  is like the perfect... If you could just say the perfect productivity setup for George Hotz.
*  It doesn't matter. It literally doesn't matter. I guess I code most of the time in Vim. Literally
*  I'm using an editor from the seventies. You didn't make anything better. VS code is nice
*  for reading code. There's a few things that are nice about it. I think that there you can build
*  much better tools. How like IDA's xrefs work way better than VS codes. Why? Yeah, actually that's a
*  good question. Like why? I still use, sorry, Emacs for most... I've actually never... I have to confess
*  something dark. I've never used Vim. I think maybe I'm just afraid that my life has been a waste.
*  I'm not evangelical about Emacs. This is how I feel about TensorFlow versus PyTorch.
*  We've switched everything to PyTorch now. Put months into the switch. I have felt like I've
*  wasted years on TensorFlow. I can't believe it. I can't believe how much better PyTorch is.
*  I've used Emacs and Vim. It doesn't matter. Yeah, still just my heart somehow. I fell in love with
*  Lisp. I don't know why. The heart wants what the heart wants. I don't understand it, but it just
*  connected with me. Maybe it's the functional language that first I connected with. Maybe it's
*  because so many of the AI courses before the deep learning revolution were taught with Lisp in mind.
*  I don't know. I don't know what it is, but I'm stuck with it. At the same time, why am I not
*  using a modern ID for some of these programming? I don't know. They're not that much better. I've
*  used modern IDs too. At the same time, so not to disagree with you, but I like multiple monitors.
*  I have to do work on a laptop. It's a pain in the ass. Also, I'm addicted to the Kinesis
*  weird keyboard. You could see there. Yeah, so you don't have any of that. You can just be on a
*  MacBook. I mean, look at work. I have three 24 inch monitors. I have a happy hacking keyboard. I have
*  a Razer Death Hatter mouse. But it's not essential for you. No. Let's go to a day in the life of
*  George Hots. What is the perfect day productivity wise? We're not talking about like Hunter S.
*  Thompson drugs. Let's look at productivity. What's the day look like? Hour by hour, is there any
*  regularities that create a magical George Hots experience? I can remember three days in my life,
*  and I remember these days vividly when I've gone through kind of radical transformations to the way
*  I think. And what I would give, I would pay $100,000 if I could have one of these days tomorrow,
*  the days have been so impactful. And one was first discovering Elias Yudkowsky on the Singularity
*  and reading that stuff. And like, my mind was blown. The next was discovering the Hutter price,
*  and that AI is just compression. Like finally understanding AIXI and what all that was. I like
*  read about it when I was 18, 19, I didn't understand it. And then the fact that like
*  lossless compression implies intelligence, the day that I was shown that. And then the third one is
*  controversial. The day I found a blog called Unqualified Reservations and read that and I was
*  like, wait, which one is that? That's what's the guy's name? Curtis Yarvin? Yeah. So many people
*  tell me I'm supposed to talk to him. Yeah, he looks, he sounds insane. Brilliant, but insane
*  or both. I don't know. The day I found that blog was another like, this was during like, like,
*  Gamergate and kind of the run up to the 2016 election. And I'm like,
*  wow, okay, the world makes sense now. This is like, I had a framework now to interpret this,
*  just like I got the framework for AI and a framework to interpret technological progress. Like
*  those days when I discovered these new frameworks were. Oh, interesting. So it's not about,
*  but what was special about those days? How'd those days come to be? Is it just you got lucky? Like,
*  sure. I like, well, you just encountered a harder prize on, on hacking news or something like that.
*  Like what? But you see, I don't think it's just, see, I don't think it's just that like,
*  I could have gotten lucky at any point. I think that in a way. You were ready at that moment.
*  Yeah, exactly. To receive the information. But is there some magic to the day today of like,
*  like eating breakfast and it's the mundane things. Nothing.
*  No, I drift through, I drift through life.
*  Without structure.
*  I drift through life, hoping and praying that I will get another day like those days.
*  And there's nothing in particular you do to, to be a receptacle for another, for day number four.
*  No, I didn't do anything to get the other ones. So I don't think I have to really
*  do anything now. I took a month long trip to New York and I mean, the Ethereum thing was
*  the highlight of it, but the rest of it was pretty terrible. I did a two week road trip and I got,
*  I had to turn around. I had to turn around. I'm driving in Gunnison, Colorado,
*  pass through Gunnison and the snow strikes coming down. There's a pass up there called Monarch Pass
*  in order to get through to Denver. You got to get over the Rockies. And I had to turn my car around.
*  I couldn't, I watched, I watched F-150 go off the road. I'm like, I gotta go back. And
*  like that day was meaningful because like, like it was real. Like I actually had to turn my car
*  around. It's rare that anything even real happens in my life, even as, you know, mundane is the fact
*  that, yeah, there was snow. I had to turn around, stay in Gunnison, leave the next day.
*  Something about that moment felt real. Okay. So actually it's interesting to break apart the
*  three moments you mentioned, if it's okay. So I always have trouble pronouncing his name, but
*  Alousa Yurkowski. So what, how did your worldview change in starting to consider the,
*  the exponential growth of AI and AGI that he thinks about and the, the threats of
*  artificial intelligence and all that kind of ideas. Like, can you, is it like, can you maybe
*  break apart like what exactly was so magical to you as a transformational experience?
*  Today, everyone knows him for threats and AI safety. This was pre that stuff. There was,
*  I don't think a mention of AI safety on the page. This is, this is old Yurkowski stuff. He'd probably
*  denounce it all now. He'd probably be like, that's exactly what I didn't want to happen. Sorry, man.
*  Is there something specific you can take from his work that you can remember?
*  Yeah. It was this realization that computers double in power every 18 months and humans do not.
*  And they haven't crossed yet. But if you have one thing that's doubling every 18 months and one
*  thing that's staying like this, you know, here's your log graph. Here's your line. You know, you
*  calculate that. And that, did that open the door to the exponential thinking? Like thinking that,
*  you know what, with technology, we can actually transform the world.
*  It opened the door to human obsolescence. It opened the door to realize that in my lifetime,
*  humans are going to be replaced.
*  And then the matching idea to that of artificial intelligence with the Hutter Prize.
*  You know, I'm torn. I go back and forth on what I think about it. But the basic thesis is it's nice,
*  it's a nice compelling notion that we can reduce the task of creating an intelligent system,
*  a generally intelligent system into the task of compression.
*  So you can think of all of intelligence in the universe, in fact, as a kind of compression.
*  Do you find that? Was that just at the time you found that as a compelling idea?
*  Do you still find that a compelling idea? I still find that a compelling idea.
*  I think that it's not that useful day to day. But actually, one of maybe my quests before that was
*  a search for the definition of the word intelligence. And I never had one. And I definitely have a
*  definition of the word compression. It's a very simple, straightforward one. And you know what
*  compression is, you know what lossless is lossless compression, not lossy lossless compression.
*  And that that is equivalent to intelligence, which I believe, I'm not sure how useful that
*  definition is day to day. But like, I now have a framework to understand what it is.
*  And he just 10x the the the prize for that competition, like recently a few months ago,
*  you ever thought of taking a crack at that? Oh, I did. Oh, I did. I spent I spent the next.
*  After I found the prize, I spent the next six months of my life trying it. And well,
*  that's when I started learning everything about AI. And then I worked with vicarious for a bit. And
*  then I learned read all the deep learning stuff. And I'm like, okay, now I like I'm caught up to
*  modern AI. And I had I had a really good framework to put it all in from the compression stuff.
*  Right, like some of the first some of the first deep learning models I played with were
*  were gtt gpt, basically, but before Transformers before it was still RNNs to do character
*  prediction. But by the way, on the compression side, I mean, the especially neural networks,
*  what do you make of the lossless requirement with the harder prize? So, you know, human
*  intelligence and neural networks can probably compress stuff pretty well, but there will be
*  lossy. It's imperfect. You can turn a lossy compression into a lossless compressor pretty
*  easily using an arithmetic encoder, right? You can take an arithmetic encoder, and you can just encode
*  the noise with maximum efficiency, right? So even if you can't predict exactly what the next
*  character is, the better a probability distribution you can put over the next character,
*  you can then use an arithmetic encoder to write, you don't have to know whether it's an E or an I,
*  you just have to put good probabilities on them. And then, you know, code those. And if you have,
*  it's a bits of entropy thing, right? So let me on that topic could be interesting as a little side
*  tour. What are your thoughts in this year about GPT three, and these language models and these
*  transformers? Is there something interesting to you as an AI researcher? Or is there something
*  interesting to you as an autonomous vehicle developer? Nah, I think I think it's overhyped.
*  I mean, it's not like it's cool. It's cool for what it is. But no, we're not just going to be
*  able to scale up to GPT 12 and get general purpose intelligence. Like your loss function
*  is literally just, you know, you know, cross entropy loss on the character, right? Like,
*  that's not the loss function of general intelligence. Is that obvious to you? Yes.
*  Can you imagine that, like to play devil's advocate on yourself, is it possible that you can
*  the GPT 12 will achieve general intelligence with something as dumb as this kind of loss function?
*  I guess it depends what you mean by general intelligence. So there's another problem with
*  the GPTs. And that's that they don't have a they don't have long term memory. Right. Right. So like,
*  just GPT 12, a scaled up version of GPT two or three, I find it hard to believe.
*  Well, you can scale it in. It's so it's a hard quarter, hard coded length,
*  but you can make it wider and wider and wider. Yeah. You're going to get you're going to get
*  cool things from those systems. But I don't think you're ever going to get something that can like,
*  you know, build me a rocket ship. What about self driving? So, you know, you can use transformer
*  with video, for example. You think is there something in there? No, because look, we use we
*  use a grew. We use a grew, we could change that grew out to a transformer. I think driving is
*  much more Markovian than language. So Markovian, you mean like the memory, which which aspect of
*  I mean that like most of the information in the state at t minus one is also in the info is in
*  state t. Yeah. Right. And it kind of like drops off nicely like this, where sometime with language,
*  you have to refer back to the third paragraph on the second page. I feel like there's not many like
*  you can say like speed limit signs, but there's really not many things in autonomous driving that
*  look like that. But if you look at to play devil's advocate is the risk estimation thing that you've
*  talked about is kind of interesting is it feels like there might be some longer term aggregation
*  of context necessary to be able to figure out like the context. I'm not even sure I'm believing my
*  my we have a nice we have a nice like vision model which outputs like a one or two four
*  dimensional perception space. Can I try transformers on it? Sure, I probably will.
*  At some point, we'll try transformers. And then we'll just see do they do better? Sure. I'm
*  but it might not be a game changer. Well, I'm not like like might transformers work better than
*  grooves for autonomous driving? Sure. Might we switch? Sure. Is this some radical change? No.
*  Okay, we use a slightly different, you know, we switch from our nns to grooves like okay,
*  maybe it's squeezed to transformers. But no, it's not. Yeah. I well on the on the topic of
*  general intelligence, I don't know how much I've talked to you about it. Like what
*  do you think will actually build an AGI? Like if you look at Ray Kurzweil with Singularity,
*  do you have like an intuition about you're kind of saying driving is easy? Yeah. And
*  it I tend to personally believe that solving driving will have really deep important impacts
*  on our ability to solve general intelligence. Like, I think driving doesn't require general
*  intelligence. But I think they're going to be neighbors in a way that it's like deeply tied.
*  Because it's so like driving is so deeply connected to the human experience,
*  that I think solving one will help solve the other. But but so I don't see that I don't see
*  driving is like easy and almost like separate than general intelligence. But like what's your vision
*  of a future with a singular? Do you see there'll be a single moment like a singularity where it'll be
*  a phase shift? Are we in the singularity now? Like what do you have crazy ideas about the future in
*  terms of AGI? Definitely in the singularity now. We are, of course, of course, look at the bandwidth
*  between people, the bandwidth between people goes up. Right? The singularity is just, you know,
*  when the bandwidth but what do you mean by the bandwidth of communications tools, the whole world
*  is networked. The whole world is networked. And we raise the speed of that network, right?
*  Oh, so you think the communication of information in a distributed way is a empowering thing for
*  collective intelligence? Oh, I didn't say it's necessarily a good thing. But I think that's like,
*  when I think of the definition of the singularity, it seems kind of right. I see, like,
*  it's a change in the world beyond which, like the world would be transformed in ways that we can't
*  possibly imagine. I mean, I think we're in the singularity now in the sense that there's like,
*  you know, one world and a monoculture and it's also linked. Yeah. I mean, I kind of share the
*  intuition that the singularity will originate from the collective intelligence of us ants versus the
*  like some single system AGI type thing. Oh, I totally agree with that. Yeah, I don't I don't
*  really believe in like, like a hard take off AGI kind of thing. Yeah, I don't think I don't even
*  think AI is all that different in kind from what we've already been building. With respect to
*  driving, I think driving is a subset of general intelligence. And I think it's a pretty complete
*  subset. I think the tools we develop at comma will also be extremely helpful to solving general
*  intelligence. And that's, I think the real reason why I'm doing it. I don't care about self driving
*  cars. It's cool problem to beat people at. But yeah, I mean, yeah, you're kind of you're two minds.
*  So one, you do have to have a mission and you want to focus and make sure you get you get there. You
*  can't forget that. But at the same time, there is a thread that's much bigger than the connects the
*  entirety of your effort. That's much bigger than just driving. With AI, and with general intelligence,
*  it is so easy to delude yourself into thinking you figured something out when you haven't.
*  If we build a level five self driving car, we have indisputably built something. Yeah. Is it
*  general intelligence? I'm not going to debate that. I will say we've built something that provides
*  huge financial value. Yeah, beautifully put. That's the engineer and credo. Like just just build the
*  thing. It's like that's why I'm with with with with the line on the go to Mars. Yeah, it's a great one.
*  You can argue like who the hell cares about going to Mars. But the reality is set that as a mission,
*  get it done. And then you're going to crack some pro problem that you've never even
*  expected in the process of doing that. Yeah. Yeah. I mean, I think if I had a choice between humanity
*  going to Mars and solving self driving cars, I think going to Mars is better. But I don't know,
*  I'm more suited for self driving cars. I'm an information guy. I'm not a modernist. I'm a
*  postmodernist. Postmodernist. All right. Beautifully put. Let me let me drag you back to programming
*  for a sec. What three maybe three to five programming languages should people learn?
*  Do you think like if you look at yourself, what did you get the most out of from learning?
*  Well, so everybody should learn C and assembly. We'll start with those two. Right. Assembly. Yeah.
*  If you can't code in assembly, you don't know what the computer is doing. You don't understand like
*  you don't have to be great in assembly, but you have to code in it. And then like you have
*  to appreciate assembly in order to appreciate all the great things C gets you. And then you have to
*  code and see in order to appreciate all the great things Python gets you. So I'll just say assembly
*  C and Python. We'll start with those three. The memory allocation of C and the fact that
*  assembly is to give you a sense of just how many levels of abstraction you get to work on
*  in modern day programming. Yeah. Yeah. Graph coloring for assignment, register assignment,
*  compilers. Like, you know, you got to do, you know, the compiler computer only has a certain
*  number of registers, yet you can have all the variables you want to see function.
*  You know, so you get to start to build intuition about compilation, like what a compiler gets you.
*  What else? Well, then there's, then there's kind of a, so those are all very imperative
*  programming languages. Then there's two other paradigms for programming that everybody should
*  be familiar with. I'm one of them is functional. You should learn Haskell and take that all the way
*  through. Learn a language with dependent types like Coq. Learn that whole space, like the very
*  PL theory, heavy languages. And Haskell is your favorite functional. Is that the go-to?
*  You'd say? Yeah, I'm not a great Haskell programmer. I wrote a compiler in Haskell once.
*  There's another paradigm. And actually there's one more paradigm that I'll even talk about
*  after that, that I never used to talk about when I would think about this. But the next paradigm
*  is learn Verilog of HDL. Understand this idea of all of the instructions executed once.
*  If I have a block in Verilog and I write stuff in it, it's not sequential. They all execute it once.
*  And then like think like that. That's how hardware works.
*  So I guess assembly doesn't quite get you that. Assembly is more about compilation
*  and Verilog is more about the hardware, like giving a sense of what actually is the hardware is doing.
*  Assembly, C, Python are straight like they sit right on top of each other. In fact, C is,
*  well, C is kind of coded in C, but you could imagine the first C was coded in assembly
*  and Python is actually coded in C. So you can straight up go on that.
*  Got it. And then Verilog gives you, that's brilliant.
*  And then I think there's another one now. Everyone should, Carpathi calls it programming 2.0,
*  which is learn a, I'm not even going to, don't learn TensorFlow, learn PyTorch.
*  So machine learning. We've got to come up with a better term than programming 2.0 or,
*  but yeah.
*  It's a programming language.
*  I wonder if it can be formalized a little bit better. It feels like we're in the early days
*  of what that actually entails.
*  Data-driven programming?
*  Data-driven programming. Yeah. But it's so fundamentally different as a paradigm
*  than the others. Like it almost requires a different skill set.
*  But you think it's still, yeah. And PyTorch versus TensorFlow, PyTorch wins.
*  It's the fourth paradigm. It's the fourth paradigm that I've kind of seen. There's like this,
*  you know, imperative functional hardware. I don't know a better word for it. And then ML.
*  Do you have advice for people that want to, you know, get into programming,
*  want to learn programming. You have a video. What is programming noob lessons, exclamation point.
*  And I think the top comment is like warning. This is not for noobs.
*  Do you have a noob like TLDW for that video, but also
*  a noob-friendly advice on how to get into programming?
*  You are never going to learn programming by watching a video called learn programming.
*  The only way to learn programming, I think, and the only one is the only way everyone I've ever
*  met who can program well learned it all in the same way. They had something they wanted to do,
*  and then they tried to do it. And then they were like, oh, well, okay, this is kind of,
*  you know, it'd be nice if the computer could kind of do this thing. And then,
*  you know, that's how you learn. You just keep pushing on a project.
*  So the only advice I have for learning programming is go program.
*  Somebody wrote to me a question like, we don't really, they're looking to learn about recurring
*  neural networks and saying like, my company's thinking of using recurrent neural networks
*  with time series data, but we don't really have an idea of where to use it yet. We just want to,
*  like, do you have any advice on how to learn about these are these kind of general machine
*  learning questions. And I think the answer is like, actually have a problem that you're trying to
*  solve and just, I see that stuff. Oh my God. When people talk like that, they're like,
*  I heard machine learning is important. Could you help us integrate machine learning with macaroni
*  and cheese production? You just, I don't even, you can't help these people. Like who lets you
*  run anything? Who lets that kind of person run anything? I think we're all, we're all beginners
*  at some point. So it's not like they're a beginner. It's like, my problem is not that they don't know
*  about machine learning. My problem is that they think that machine learning has something to say
*  about macaroni and cheese production. Or like, I heard about this new technology. How can I use it
*  for why? Like, I don't know what it is, but how can I use it for why? That's true. You have to
*  build up an intuition of how, cause you might be able to figure out a way, but like the prerequisites,
*  you should have a macaroni and cheese problem to solve first. Exactly. And then two, you should
*  have more traditional, like the learning process should involve more traditionally applicable
*  problems in the space of whatever that is of machine learning and then see if it can be applied
*  to that competition. At least start with, tell me about a problem. Like if you have a problem,
*  you're like, you know, some of my boxes aren't getting enough macaroni in them. Can we use
*  machine learning to solve this problem? That's a much, much better than how do I apply machine
*  learning to macaroni and cheese? One big thing, maybe this is me talking to the audience a little
*  bit, cause I get these days so many messages, advice on how to like learn stuff. Okay. My,
*  this, this, this is not me being mean. I think this is quite profound actually is you should
*  Google it. Oh yeah. Like one of the, uh, like skills that you should really acquire as an engineer,
*  as a researcher, as a thinker, like one, there's two, two, two complimentary skills. Like one
*  is with a blank sheet of paper with no internet to think deeply. And then the other is to Google the
*  crap out of the questions you have. Like that's actually a skill. I don't know. People often talk
*  about, but like doing research, like pulling at the thread and like looking up different words,
*  going into like GitHub repositories with two stars and like looking how they did stuff,
*  like looking at the code or going on Twitter, seeing like there's little pockets of brilliant
*  people that are like having discussions. Like if you're a neuroscientist, go into signal
*  processing community. If you're an AI person going into the psychology community, like
*  switch communities, like keep searching, searching, searching, because it's so much better to invest
*  in like finding somebody else who already solved your problem than than is to try to solve the
*  problem. And cause they've often invested years of their life, like entire communities are probably
*  already out there who have tried to solve your problem. I think they're the same thing. I think
*  you go try to solve the problem and then in trying to solve the problem, if you're good at solving
*  problems, you'll stumble upon the person who solved it already. Yeah. But the stumbling is really
*  important. I think that's a skill that people should really put, especially in undergrad,
*  like search. If you ask me a question, how should I get started in deep learning? Like especially
*  like that is just so Google-able. Like the whole point is you Google that and you get a million
*  pages and just start looking at them. Yeah. Start pulling at the threads, start exploring,
*  start taking notes, start getting advice from a million people that have already like spent
*  their life answering that question actually. Oh, well, yeah. I mean, that's definitely also,
*  yeah. When people like ask me things like that, I'm like, trust me, the top answer on Google is
*  much, much better than anything I'm going to tell you. Right? Yeah. People ask, it's an interesting
*  question. Let me know if you have any recommendations. What three books, technical or fiction or
*  philosophical had an impact on your life or you wouldn't recommend perhaps? Maybe we'll start with
*  the least controversial Infinite Jest. Infinite Jest is a... David Foster Wallace. Yeah, it's a
*  book about wireheading really. Very enjoyable to read, very well-written. You will grow as a person
*  reading this book, its effort. And I'll set that up for the second book, which is pornography.
*  That's called Atlas Shrugged, which... Atlas Shrugged is pornography? Yeah, I mean, it is. I will not
*  defend the... I will not say Atlas Shrugged is a well-written book. It is entertaining to read,
*  certainly, just like pornography. The production value isn't great. There's a 60-page monologue
*  in there that Anne Rand's editor really wanted to take out and she paid out of her pocket to keep
*  that 60-page monologue in the book. But it is a great book for a kind of framework of human
*  relations. And I know a lot of people are like, yeah, but it's a terrible framework.
*  Yeah, but it's a framework. Just for context, in a couple of days, I'm speaking with, for
*  probably four plus hours, with Yaron Brook, who's the main living remaining objectivist.
*  Objectivist. Interesting. So I've always found this philosophy quite interesting on many levels.
*  One of how repulsive some large percent of the population find it, which is always funny to me
*  when people are unable to even read a philosophy because of some... I think that says more about
*  their psychological perspective on it. But there is something about objectivism and Anne Rand's
*  philosophy that's deeply connected to this idea of capitalism, of the ethical life is the productive
*  life. That was always compelling to me. I didn't seem to interpret it in the negative sense that
*  some people do. To be fair, I read that book when I was 19. So you had an impact at that point. Yeah.
*  Yeah. And the bad guys in the book have this slogan, from each according to their ability,
*  to each according to their need. And I'm looking at this and I'm like, these are the most... This
*  is Team Rocket level cartoonishness. No bad guys. And then when I realized that was actually the
*  slogan of the Communist Party, I'm like, wait a second. Wait, no, no, no, no, no. You're telling
*  me this really happened? Yeah, it's interesting. I mean, one of the criticisms of her work is she
*  has a cartoonish view of good and evil. The reality, as Jordan Peterson says, is that
*  each of us have the capacity for good and evil in us, as opposed to there's some characters who
*  are purely evil and some characters are purely good. And that's in a way why it's pornographic.
*  The production value. I love it. Well, evil is punished and there's very clearly...
*  There's no... Just like porn doesn't have character growth, neither does Alan Sherald.
*  Brilliant. Well put. But 19-year-old George Hotz, it was good enough.
*  What's the third? You have something? I could give these two, I'll just throw out.
*  They're sci-fi. Perputation City. Great thing to start thinking about copies of yourself.
*  That is Greg Egan. That might not be his real name. Some Australian guy. Might not be Australian.
*  I don't know. And then this one's online. It's called The Metamorphosis of Prime Intellect.
*  It's a story set in a post-singularity world. It's interesting.
*  Either of the worlds, do you find something philosophical interesting in them that you
*  can comment on? I mean, it is clear to me that Metamorphosis of Prime Intellect is written by
*  an engineer, which is... It's very almost a pragmatic take on a utopia in a way.
*  Positive or negative? Well, that's up to you to decide reading the book. And the ending of it is
*  very interesting as well and I didn't realize what it was. I first read that when I was 15.
*  I've reread that book several times in my life. And it's short. It's 50 pages. I want you to go
*  read it. Sorry, this is a little tangent. I've been working through the foundation. I haven't
*  read much sci-fi in my whole life and I'm trying to fix that. The last few months,
*  there's been a little side project. What's to you as the greatest sci-fi novel that people should
*  read? I mean, I would say like, yeah, Premutation City, Metamorphosis of Prime Intellect. I don't
*  know. I didn't like Foundation. I thought it was way too modernist. Do you like Dune and all of
*  those? I've never read Dune. I've never read Dune. I have to read it. Fire Upon the Deep is interesting.
*  Okay. I mean, look, everyone should read Neuromancer. Everyone should read Snow Crash.
*  If you haven't read those, start there. Yeah, I haven't read Snow Crash.
*  You haven't read Snow Crash? Oh, it's very entertaining. Go to Lesher Bach and if you want
*  the controversial one, Bronze Age Mindset. All right. I'll look into that one.
*  Those aren't sci-fi, but just to round out books.
*  A bunch of people asked me on Twitter and Reddit and so on for advice. What advice would you give
*  a young person today about life? Yeah, I mean, looking back, especially when you're a young
*  younger and you continued it, you've accomplished a lot of interesting things. Is there some advice
*  from those? From that life of yours that you can pass on? If college ever opens again, I would love
*  to give a graduation speech. At that point, I will put a lot of somewhat satirical effort into this
*  question. Yeah. You haven't written anything at this point. Oh, you know what? Always wear sunscreen.
*  This is water. Like you're plagiarizing. I mean, but that's the like, clean your room. Yeah,
*  you can plagiarize from all of this stuff. Self-help books aren't designed to help you.
*  They're designed to make you feel good. Whatever advice I could give, you already know. Everyone
*  already knows. Sorry, it doesn't feel good. Right? You know. If I tell you that you should
*  eat well and read more, it's not going to do anything. I think the whole genre of those kind
*  of questions is meaningless. I don't know. If anything, it's don't worry so much about that
*  stuff. Don't be so caught up in your head. Right. I mean, in the sense that your whole life,
*  if your whole existence is like moving version of that advice, I don't know. There's something in
*  you that resists that kind of thinking and that in itself is just illustrative of who you are.
*  And there's something to learn from that. I think you're clearly not overthinking stuff.
*  Yeah. And you know what? It's a gut thing. Even when I talk about my advice, I'm like,
*  my advice is only relevant to me. It's not relevant to anybody else. I'm not saying you
*  should go out if you're the kind of person who overthinks things to stop overthinking things.
*  It's not bad. It doesn't work for me. Maybe it works for you. I don't know.
*  Let me ask you about love. Yeah. I think last time we talked about the meaning of life,
*  and it was kind of about winning. Of course. I don't think I've talked to you about love much,
*  whether romantic or just love for the common humanity amongst us all. What role has love
*  played in your life? In this quest for winning, where does love fit in?
*  Well, the word love, I think means several different things. There's love in the sense of,
*  maybe I could just say there's love in the sense of opiates and love in the sense of
*  oxytocin and then love in the sense of maybe a love for math. I don't think it fits into
*  either of those first two paradigms. So each of those, have they given something to you
*  in your life? I'm not that big of a fan of the first two. Why?
*  Because for the same reason I'm not a fan of, for the same reason I don't do opiates and don't take
*  ecstasy. There were times, look, I've tried both. I like opiates way more than I like ecstasy.
*  But they're not. The ethical life is the productive life. So maybe that's my follow
*  with those and then like, yeah, a sense of, I don't know, like abstract love for humanity.
*  I mean, the abstract love for humanity, I'm like, yeah, I've always felt that. And I guess
*  it's hard for me to imagine not feeling it. And maybe there's people who don't and I don't know.
*  Yeah, that's just like a background thing that's there. I mean, since we brought up drugs, let me
*  ask you, this is becoming more and more a part of my life because I'm talking to a few researchers
*  that are working on psychedelics. I've eaten shrooms a couple of times and it was fascinating
*  to me that like the mind can go like, just fascinating the mind can go to places I didn't
*  imagine it could go. And I was very friendly and positive and exciting. And everything was kind of
*  hilarious in the place, wherever my mind went. That's where I went is, what do you think about
*  psychedelics? Do you think they have, what do you think the mind goes? Have you done psychedelics?
*  What do you think the mind goes? Is there something useful to learn about the places it goes?
*  Once you come back?
*  You know, I find it interesting that this idea that psychedelics have something to teach
*  is almost unique to psychedelics, right? People don't argue this about amphetamines.
*  And that's true.
*  And I'm not really sure why. I think all of the drugs have lessons to teach. I think there's
*  things to learn from opiates. I think there's things to learn from amphetamines. I think
*  there's things to learn from psychedelics, things to learn from marijuana.
*  But also at the same time, recognize that I don't think you're learning things about the world. I
*  think you're learning things about yourself. And, you know, what's the even, it might have even been,
*  might even have been a Timothy Leary quote. I don't want to misquote him, but the idea is
*  basically like, you know, everybody should look behind the door. But then once you've seen behind
*  the door, you don't need to keep going back. So I mean, and that's my thoughts on all real drug use,
*  too. So maybe for caffeine.
*  It's a little experience that it's good to have, but.
*  Oh, yeah. No, I mean, yeah, I guess. Yeah. Psychedelics are definitely.
*  So you're a fan of new experiences, I suppose, because they all contain a little,
*  especially the first few times it contains some lessons that can be picked up.
*  Yeah. And I'll revisit psychedelics maybe once a year. Usually small, smaller doses.
*  Maybe they turn up the learning rate of your brain. Have heard that? Like that?
*  Yeah, that's cool. Big learning rates have pros and cons.
*  Last question. This is a little weird one, but you've called yourself crazy in the past.
*  First of all, on a scale of one to 10, how crazy would you say are you?
*  Oh, I mean, it depends how you, you know, when you compare me to Elon Musk and Anthony
*  Lewandowski, not so crazy. So like, like a seven.
*  So like, like a seven. Let's go with six.
*  Six. Six. What?
*  I like seven. Seven's a good number.
*  Seven. All right. Well, I'm sure day by day changes, right? So, but you're in that,
*  in that area. What? In thinking about that, what do you think is the role of madness?
*  Is that a feature or a bug if you were to dissect your brain?
*  So, okay, from like a, like mental health lens on crazy, I'm not sure I really believe in that.
*  I'm not sure I really believe in like a lot of that stuff. Right? This concept of,
*  okay, you know, when you get over to like, like, like, like, hardcore bipolar and schizophrenia,
*  these things are clearly real, somewhat biological. And then over here on the spectrum,
*  you have like, add and oppositional defiance disorder, and these things that are like,
*  wait, this is normal spectrum human behavior. Like this isn't,
*  you know, where's the, the line here? And why is this like a problem? So there's this whole,
*  you know, the neurodiversity of humanity is huge. Like, people think I'm always on drugs.
*  People are always saying this to me on my streams. And like, guys, you know, like,
*  I'm real open with my drug use. I'd tell you if I was on drugs. And, I mean, I had like a cup of
*  coffee this morning, but other than that, this is just me. You're witnessing my brain.
*  Yeah. In action. So, so the word madness doesn't even make sense. And then you're in the rich
*  neurodiversity of humans. I think it makes sense, but only for like some insane extremes.
*  Like if you are actually like visibly hallucinating, you know, that's okay. But
*  there is the kind of spectrum on which you stand out. Like that, that's like, if I were to look,
*  you know, at decorations on a Christmas tree or something like that, like if you were a decoration
*  that would catch my eye. Like that thing is sparkly. Whatever the hell that thing is.
*  There's something to that. Just like refusing to be boring or maybe boring is the wrong word,
*  but to, yeah, I mean, be willing to sparkle, you know? It's like somewhat constructed. I mean,
*  I am who I choose to be. I'm going to say things as true as I can see them. I'm not going to lie.
*  But that's a really important feature in itself. So like whatever the neurodiversity of your,
*  whatever your brain is, not putting constraints on it that force it to fit into the mold of
*  what society is like defines what you're supposed to be. So you're one of the specimens that
*  doesn't mind being yourself. Being right is super important, except at the expense of being wrong.
*  Without breaking that apart, I think it's a beautiful way to end it, George. You're one
*  of the most special humans I know. It's truly an honor to talk to you. Thanks so much for doing it.
*  Thank you for having me.
*  Thanks for listening to this conversation with George Hotz. And thank you to our sponsors,
*  Four Sigmatic, which is the maker of delicious mushroom coffee, Decoding Digital, which is a
*  tech podcast that I listen to and enjoy, and ExpressVPN, which is the VPN I've used for many
*  years. Please check out these sponsors in the description to get a discount and to support
*  this podcast. If you enjoy this thing, subscribe on YouTube, review it with Five Stars and Apple
*  Podcasts, follow on Spotify, support on Patreon, or connect with me on Twitter at Lex Friedman.
*  And now, let me leave you with some words from the great and powerful Linus Torvald.
*  Talk is cheap. Show me the code. Thank you for listening and hope to see you next time.

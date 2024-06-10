---
Date Generated: June 10, 2024
Transcription Model: whisper medium 20231117
Length: 4477s
Video Keywords: ['complexity', 'mathematics', 'networks', 'synchronization']
Video Views: 23226
Video Rating: None
Video Description: Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2019/04/08/episode-41-steven-strogatz-on-synchronization-networks-and-the-emergence-of-complex-behavior/

Patreon: https://www.patreon.com/seanmcarroll

One of the most important insights in the history of science is the fact that complex behavior can arise from the undirected movements of small, simple systems. Despite the fact that we know this, we’re still working to truly understand it — to uncover the mechanisms by which, and conditions under which, complexity can emerge from simplicity. (Coincidentally, a new feature in  Quanta on this precise topic came out while this episode was being edited.) Steven Strogatz is a leading researcher in this field, a pioneer both in the subject of synchronization and in that of small-world networks. He’s also an avid writer and wide-ranging thinker, so we also talk about problems with the way we educate young scientists, and the importance of calculus, the subject of his new book.

Steven Strogatz received his Ph.D. in applied mathematics from Harvard, and is currently the Jacob Gould Schurman Professor of Applied Mathematics at Cornell. His work has ranged over a wide variety of topics in mathematical biology, nonlinear dynamics, networks, and complex systems. He is the author of a number of books, including SYNC, The Joy of x, and most recently Infinite Powers. His awards include teaching prizes at MIT and Cornell, as well as major prizes from the Joint Policy Board for Mathematics, the American Association for the Advancement of Science, the Mathematical Association of America, and the Lewis Thomas Prize.
---

# Episode 41: Steven Strogatz on Synchronization, Networks, and the Emergence of Complex Behavior
**Mindscape Podcast:** [April 08, 2019](https://www.youtube.com/watch?v=B7DxSTu4pzA)
*  Hello everyone and welcome to the Mindscape Podcast. I'm your host Sean
*  Carroll. In today's episode we're gonna tackle a perennial big question in the
*  natural sciences, trying to understand the sense in which the world is
*  complicated. Now I mean this in a very particular way. I mean there's a way the
*  world could be which is completely chaotic, right? Like things just happening
*  at random, there's no order or structure anywhere. There's another way the world
*  could be which is completely rigid and orderly, right? The actual world is
*  somewhere in between these two things. There's sort of poles of chaos and order
*  and we balance ourselves in between. That's one feature but the other is no
*  one planned it, right? There's not a central designer that says this is how
*  things should be. The universe somehow organizes itself. And when I say
*  the universe, especially of course here on earth in the biosphere. So today's
*  guest is actually a mathematician, Steven Strohgatz. He has become very well known
*  for his popular books on mathematics but he's equally successful as a
*  researcher. As I mentioned in the podcast, he's the author of a paper that
*  has well over 30,000 citations which makes a regular physicist like me very
*  jealous. And one of the founders of both the field of studying synchronization,
*  spontaneous synchronization of different physical systems. And then out of that
*  study came the study of networks and in particular small world networks. The way
*  that many systems like the human brain or the internet are organized where it
*  is neither just you talk to your nearest neighbors nor you talk to everybody but
*  again somewhere in between. How does this sort of mixture of chaos and order
*  naturally come about through the working out of math and its equations? So Steve
*  is a wonderful communicator and a real pioneer in this field so I think you're
*  gonna enjoy this conversation. Let's go!
*  Steven Strohgatz, welcome to the Mindscape podcast. Thanks very much, Sean. I mean you
*  are very well known as a popularizer of math but also you're extremely well
*  known as a doer of math. I tend to think of the math you do as almost kind of
*  physics. It's not the you know the pure math that is proving esoteric things.
*  You're really hands dirty there in the real world. I mean how did you come to
*  think of yourself as an applied mathematician? That's not something
*  that most people grow up wanting to be. Hmm, that's a good point and I didn't
*  even know it existed. When I was in college I thought I wanted to be a math
*  major and they had a whiz kid linear algebra class for you know the people
*  who had done very well in math in high school. So I found myself in there and I
*  got crushed in my first semester of college. Got the worst grade that I ever
*  got in college in that course and it was you know was the kind of course that is
*  supposed to be like to weed out the people who don't have the right stuff to
*  be a pure mathematician. They were trying to decide who who's gonna be the
*  mathematician of the future and otherwise people because a lot of kids
*  in high school think they're pretty good in math and the idea was correct them
*  very early on. So I have to say to this day I still resent that course because
*  they put a really quite weak teacher in there and so it was a real sink or swim
*  experience for all of us and I definitely was taking in a lot of water.
*  This would be a big deviation from the plan of the podcast but that's okay I
*  mean actually I'll say that my best podcasts have involved deviations from
*  the plan but let me just remark that we live in a culture in physics and in math
*  of this weed them out sink or swim let's do ask them to do impossible things and
*  see who suffers the least and I personally think that that is not really
*  the way to make the best scientists or mathematicians. Well of course I agree
*  with you and you know as a weed or a would-be weed almost weeded out I mean I
*  think we lose a lot of talent with that kind of approach and there's no need to
*  be that discouraging so yeah I mean I do kind of want to go along on this thread
*  because I think it's something a lot of people have experienced this feeling of
*  having once loved some subject and then getting discouraged in college and it's
*  not necessarily a bad thing if you know long as it turns out okay you go in some
*  other direction so in my case I thought well maybe maybe I really meant to do
*  physics and so to respond to your earlier question I took a lot of physics
*  too which was always a great interest of mine but it was a lot of the idea I love
*  the idea that physics is where you went by after being weeded out because that
*  is not how physicists think of themselves come on I'm not saying I'm not
*  saying that just thought math was my thing because I didn't feel like I had
*  certainly I was a disaster in the lab I knew that already from high school and I
*  felt like I could my physical intuition never seemed especially great I don't
*  know especially like free body diagrams things pushing on you even action and
*  reaction I always found that very mysterious so it is don't don't feel bad
*  yeah but the math part of it when it once it was converted to equations then
*  I felt very secure so I thought that was my natural strength but then I started
*  to think otherwise after this one very proof oriented course and I had never
*  really had any experience with trying to do rigorous math proofs at that point
*  in my life so anyway I enjoyed the physics course especially enjoyed
*  sophomore sorry it was the spring semester of my freshman year we took a
*  course we I think because these other kids that were in the same cohort out
*  of the electricity and magnetism book by Purcell I know I know that you would
*  know that book and maybe some of your listeners will know that book that's one
*  of the most beautifully written textbooks in any subject I would say I
*  think do you agree with that yeah no we didn't use it when I was
*  undergraduate but I know it since then it's very very good I mean what was so
*  interesting to me about it was that it didn't just tell you for instance that
*  the force between two charges is going to be along the line between the charges
*  let's suppose it's the electrostatic forces how much does a proton pull on
*  an electron you know that that's going to be some force and in high school I
*  had learned this thing Coulomb's law that the force would go along that line
*  between them but what was so interesting to me and Purcell is that he said that
*  follows from the symmetry of space but that's not just a property of this force
*  that's a property about space because if you imagine those two particles by
*  themselves in an empty universe otherwise empty there would be no
*  assuming that space is the same in all directions there is no other preferred
*  direction than this line between them so it has to be along that line and
*  whether you believe that argument or not I just was entranced by the idea that
*  you could you could make an argument like that yeah you could see how this
*  would light up the mathematician inside you so anyway I've taken a big long
*  detour from your original question but I the point was that I always like math
*  but I did like the math of the real world or at least the sort of semi real
*  world that we study in classes like physics class not the real real world
*  where I had to you know catch my clothes on fire make sparks in the lab or
*  something I mean I studied cosmology and quantum mechanics so I can't make any
*  claims to being too involved with the real real world but it's applied math is
*  an interesting field right I mean in I guess pure math is the alternative it's
*  really about proofs right you know here's some we're gonna prove some
*  things there's also physicists math which is this wonderful growing field
*  where we say things we think are true and we give some arguments for them but
*  we don't actually prove things and I think applied math I have the feeling is
*  somehow in between those poles well it means many different things to many
*  different people so some some see applied math as I mean just to be clear
*  since we haven't really said about these things there are these two roughly
*  speaking two flavors of math so there's math that looks inward at itself which
*  is what I think of as pure math and there's math that looks outward at the
*  world at the world very broadly construed it could be oceanography it
*  could be the universe it could be biology whatever but it's it's a math in
*  the service of something else or sometimes it's math inspired by something
*  else you know like something beautiful that happens in physics can be then the
*  beginning of a new mathematical theory and some people would still call that
*  pure math but I would think of that as part of applied math or maybe close to
*  what you just called the physicist math do you actually in your daily in your
*  work in your papers are you typically proving a theorem or you know I noticed
*  that one of the wonderful things about your work is it very often you sort of
*  figure out what the answer to the question is by doing some computer
*  simulations that's true yeah I'm a no-holds-barred style I really I you
*  know I've definitely been called a physicist by many of my mathematician
*  friends that they see me as using the spirit of physics and I do from the
*  physics culture that I absorbed I learned that it's you know that that you
*  should try lots of different things you can guess you can use intuition you can
*  use physical reasoning you could use computers you could do all kinds of
*  different sometimes a proof is great if you can do a proof but it's not the only
*  game in town whereas in pure math that is the the end-all and be-all is to
*  prove theorems I never never know so I'm definitely not one of those for me it's
*  there's all kinds of ways of getting evidence and trying to understand what's
*  true I'm definitely interested in the truth about the equations or the
*  mathematical models that I study but I sort of actually feel a lot of infinity
*  affinity with artists I must say this could take us in an interesting
*  direction I what you have yeah I mean from some of your writing although we
*  never met I get the feeling you'll resonate with this but I I'm really
*  interested in something that you maybe you could call like mathematical
*  impressionism that is instead of making a photo realistic painting of the world
*  or the mathematical equivalent I I like to get inspired by something in nature
*  or in the world and then do something that's much simpler that's that's the
*  essence of what's out there sort of like the way the impressionist painters
*  didn't try to capture the details they weren't interested in that they were
*  trying to with their either their dots or their bold strokes convey the heart
*  of whatever that was and so I I like my models to be for instance there was one
*  paper that I did with my colleague Rennie Morolo mathematician at Boston
*  College where we were thinking about a certain problem but it reminded us of a
*  fireflies that all flash in sync you know all flashing on and off together
*  and yet what we did was not an accurate model of real fireflies I would never
*  claim that and we were careful in the discussion at the end of the paper to
*  explain why fireflies were quite different from what we were pretending
*  in this paper yet they were somehow like the essence of what the fireflies were
*  doing so yeah and that's that I mean to a physicist that just makes perfect sense
*  I mean it's obviously there's math involved but the idea of distilling down
*  some complicated thing to the simplest possible description that captures
*  something vital about it is what we do for living in our own minds uh-huh so
*  I've always liked that attitude in physics and I do feel it has a lot in
*  common with an artistic impulse and yeah well let's just be clear it's not like
*  this is something that everyone would agree with there there are quite a few
*  applied mathematicians who say that's not good enough you you should really
*  try to make a model that that is testable and the ultimate arbiter is
*  reality like if your model doesn't do the right things in experiments or
*  doesn't match observations even qualitatively then you've gone too far
*  you know then you've lost the essence so I mean I sort of believe that I agree
*  that if you've gone too far of course you have lost the essence but the truth
*  is if I'm really being honest about it I care more about math than nature okay
*  that's a dirty thing to say no go ahead if you're in the math department it's
*  okay well that's right and that's why I'm not a physicist yeah because I think
*  a physicist ultimately does care about getting the science right and there's
*  this evil part of me that says if it's beautiful but a little bit wrong I'm okay
*  with that it's still beautiful yeah difference between fine artists and a
*  photojournalist absolutely right or an illustrator well maybe so I mean there's
*  an old flattering conversation for comparison from your perspective right
*  I'm the illustrator you're the fine artist well it's just a matter of what
*  people are interested in you know so I think as long as you're honest about
*  what you're trying to do then I think it should be okay it's just it's just where
*  you pretend that something is realistic and it's not then you're gonna get in
*  trouble and you know the example you used is perfect because I wanted to
*  segue into this whole question of you know get to an example of what you've
*  been working on for your whole life I suppose I guess it's applied
*  mathematician themes come back and forth rather than just working on one big
*  problem for your whole life but the fireflies are the example that you used
*  in your book sink to introduce the reader to this wonderful thing that
*  appears all over nature in very different forms where you have
*  independent agents doing something and yet they naturally fall into
*  synchronization it was that firefly paper that you alluded to there the
*  first example of when you thought about that phenomenon it's certainly one of
*  our very earliest I say our because again that person I mentioned earlier
*  Rene Morolo I did a lot of this work with him he was and still is probably my
*  best friend and we did a lot of this when we were just starting our career so
*  I was a postdoc he was a new assistant professor but anyway yeah it was very
*  early that was in the early 1990s and to me it's part of a larger theme a cosmic
*  theme about order emerging out of disorder I always found that spooky
*  almost theological you know because in physics in the simplest case like say in
*  thermodynamics classes we learn that things tend to disorder if you have a
*  closed system with no energy coming in or getting out and we do you know then
*  then the second law tells us that system is going to just come to equilibrium and
*  it'll be disordered sort of maximally it'll as we you know in the jargon the
*  entropy will keep increasing so but yet we see fantastically organized structures
*  all around us we see civilization we see you know biology organizing itself into
*  ecosystems and living things cells I mean there's it's an there's this
*  fantastic fight between the forces that want not want but you know that make the
*  universe tend to greater disorder and yet we see all kinds of what looks like
*  spontaneous order all around us so that's still somewhat mysterious from a
*  physics perspective although we it's not to say we're contradicting the second
*  law that's not possible that's correct law more or less I mean we could talk
*  about that but let's not leave that's not going there no actually I'm a this is
*  one of my pet peeves you have not said to any of my pet peeves but there's a
*  pet peeve I have about how people talk about the second law where they say what
*  everyone says which is that in a closed system you tend to disorder and then
*  they stop and then they say but look at these open systems you get order but
*  they can't help but telling themselves you know the order appears in this open
*  system despite the second law despite yeah exactly there's no despite me
*  that's like saying the moon orbits the earth despite the force of gravity
*  because you think that gravity pulls things together and the moon doesn't
*  fall so it's obviously despite the force of gravity but so I just you know react
*  against that no you didn't do it you're not guilty of it but I think that
*  there's a lot of work yet to be done in figuring out how open systems do
*  organize themselves and how entropy is actually part of the reason why that
*  happens not something being opposed by it sure we're on the same page with that
*  I mean that's that's the challenge of non-equilibrium thermodynamics that it
*  has to somehow be consistent with what we already know to be true from the
*  equilibrium or close to equilibrium case yeah and yet the math is and the
*  conceptualization the physics part of it they're just very difficult and that's
*  some of the most exciting research going on right now in in non-equilibrium
*  statistical physics so I and apparently fireflies for an example of this no you
*  know I don't approach it from a physics perspective because first of all I never
*  took step step Mac statistical mechanics I never went that far in physics so I
*  don't really know what I'm talking about here but I did work at it from the
*  perspective of someone interested in differential equations which allow us to
*  describe systems that change in time or in space or both and you know so
*  something like fireflies you can make a little abstract version of them where
*  you think of well what's going on with a firefly if you have you have a single
*  firefly that you're keeping alive in a jar you know that you've captured out in
*  your backyard then it will flash and then it's flash has stopped and then it's
*  sort of dark for a while and then it somehow is building up its readiness to
*  flash until it reaches some we don't know really what's going on but there's
*  probably something happening in its nervous system where it's got a little
*  timer some little circuit neural I mean I think literally it's not known exactly
*  how the flash rhythm works yeah that's interesting I was gonna ask is that we
*  really I don't know obviously but it's still not even known you think well I
*  mean we know something about the chemistry of what the substance is that
*  that you know sort of ignites and flashes we know about the enzymes that
*  degrade it but I loosely speaking it's a bit analogous to something we all learn
*  in the first year of physics where there's a charge between two complex you
*  know on the capacitor plates that's building up it's like in the jargon an
*  RC circuit right or a relaxation oscillator something is building up
*  toward a threshold and when it reaches that threshold and you get a sudden
*  discharge which in this case would be the firefly flashing or in the case of
*  the RC circuit would be the capacitor dumping its charge and then starting to
*  build up again as it charges up so we at Rennie Merlo and I made this little
*  model of effectively lots of little relaxation oscillators building up
*  discharging and every time somebody discharges it kicks everybody else up a
*  little bit closer to their firing threshold or they get excited or
*  something like that yeah that's right and it's be and that part we know is
*  correct qualitatively that fireflies not only flash but they see the flashes of
*  others and adjust the timing of their flash rhythm in response to the flash of
*  others we know that from experiments where you can use a pen flashlight to
*  be in it like an artificial firefly and if you periodically flash your flashing
*  flashlight at this firefly you for instance you can play tricks on you could
*  flash a little faster than its normal rhythm and then you'll see that firefly
*  sort of scurrying to keep up not literally moving its feet but it flashes
*  a little bit faster to get stay in sync with your abnormally fast flashlight up
*  to limits I mean if you drive it more than like 20% faster than it wants to go
*  it can't keep up and then it falls out of sync this is not helping the
*  reputation of mad scientists and sadistic experimenters on the animal
*  kingdom they do a lot of worse things well anyway so so we do know that there
*  are interaction rules that can be measured through the kind of experiments
*  I just measured and so the hypothesis was always that what's happening in a
*  congregation of fireflies is they're all both flashing and receiving flashes from
*  others and adjusting in accordance with some rules and so then the big math
*  problem is and it's something that transcends biology they're not trained
*  to solve a question like this if every firefly is individually obeying the
*  rules that you can measure then is it the case that synchrony will emerge
*  automatically every time in such a population and that turns out to be
*  quite a hard math problem because of the discontinuities in it that you know I
*  said when there's a flash then first of all the flash is like a sudden impulse
*  just a quick on and then quick off and then also we imagine that the to
*  continue that that capacitor analogy that the discharge is very fast so the
*  firefly like sort of so to speak instantly goes back to its baseline
*  before it starts charging up again and so when you have jumps yeah when you
*  have jumps in any kind of system that you're trying to describe with math
*  unfortunately the apparatus that we use in math assumes everything is smooth and
*  continuous and doesn't jump around discontinuously so when you say yeah
*  when you say the apparatus I mean this is these are all human constructions
*  right like the math we're used to doing is comfortable with this so this is why
*  you get paid the big bucks to sort of generalize that way of thinking a little
*  bit yeah thank you I didn't mean if apparatus in a laboratory I meant the
*  tools that we use specifically I'm avoiding using the word calculus but
*  that's really what I want to say that calculus is predicated on the idea that
*  things can change but they only change smoothly they don't jump you know
*  discontinuously from one place to another whereas these fireflies sort of
*  act like they do at least it would be sudden flashes and the sudden response
*  to flashes and so what made the problem hard and why it was a research problem
*  for us was that you know how do you accommodate something that is on the one
*  hand continuously charging up towards its threshold but then at the same time
*  it can suddenly flash and suddenly discharge and go back so it was this
*  mixture of continuity and discontinuity that made the math abnormal and and
*  weird and challenging and this is all started by you know in a very scientific
*  way in the sense that we saw the fireflies doing this this had been known
*  for a long time that fireflies got into sync somehow and I guess as a human being
*  your first guess is that well there's a boss firefly there's a leader that is
*  telling them what to do there's a conductor for the orchestra but that
*  didn't seem to pan out empirically so your question was could it be
*  self-organizing this coming into yes exactly right right I did get a little
*  ahead of myself there with talking about the math it is a great story that you
*  know people that lived in Thailand or Malaysia had known about this they'd
*  seen it forever but the first Westerners to come to those parts of the world like
*  Sir Francis Drake from England in the 1500s there are ships logs that we can
*  read of his sailors saying as we go down these rivers you know like the river to
*  Thailand there's there these strange creatures that live in the mangrove
*  trees that flash and they call them lightning bugs you know I could call
*  them growing up in Philadelphia so you know that's so many yeah lightning bugs
*  fireflies whatever you want to call them they but that what was spectacular is
*  that there would be tree after tree for miles along the riverbank filled with
*  these fireflies thousands of them it seemed and they it's like you could
*  visualize it almost like a Christmas tree with Christmas lights on it except
*  that these are beetles that you know we think of they're not there these little
*  beetles have this strange flashing property and they the whole tree will
*  ignite and get dark simultaneously and it goes on all night long and it's just an
*  amazing spectacle so but the question was as you said how is it possible these
*  are not the most ingenious creatures they're just you know they're just little
*  bugs yeah and and at the beginning of the night they're not doing that when
*  they fly into the trees you know as the Sun goes down they're totally disorganized
*  if you if you get there at dusk you don't see the phenomenon it builds up
*  over the night and it takes a while but by the middle of the night it's
*  perfectly organized so that was always the question is it that there's as you
*  say is there some kind of master firefly like a conductor for the orchestra and
*  they're all following the lead of that one that's not going to be a very robust
*  biological way of doing it because if a bird eats that particular maestro you
*  know what then it's not going to work that night yeah so who appoints the head
*  firefly that doesn't it doesn't seem biologically on the other hand you have
*  to keep in mind that there are things in biology organized like that like there
*  is a queen bee who is different from the other bees so it's not unthinkable that
*  there is a king firefly but no one ever found one and so the the prevailing view
*  today is that it's done this spontaneous synchronization is an emergent phenomenon
*  that it as you say it's self-organizes you don't need an external signal like
*  lightning in the jungle you don't I mean those were the old theories that there
*  was you know look it's in the tropics there's gonna always be some lightning
*  storms and all the fireflies get startled by the lightning flash and that kind of
*  pre synchronizes them all as they respond in shock to that lightning bolt
*  but that's ridiculous because it happens every night even if it's not
*  raining so anyway but there were like I say there were it was a very old problem
*  and it was only by around the 1960s that those experiments that I mentioned with
*  pen flashlights demonstrated that that the fireflies are both reacting to
*  flashes as well as emitting them and the conjecture was always that they somehow
*  through that process of interaction come into sync but no biologist could figure
*  out how to demonstrate that because they didn't have the computers that could do
*  I mean it's not the way that they think they have different training so you
*  really needed a physicist or a mathematician to try to work on this and
*  the mechanism is just that the fireflies are looking at each other and somehow
*  what they see is affecting their rate of firing that's right exactly so yeah if
*  they see you know a flash when they were not expecting to see one it might tell
*  them oh god I'm a little bit late and then not consciously but through just
*  some unconscious processes in their nervous system because we don't think of
*  them as having much consciousness they just automatically adjust their timing
*  something in their nervous system changes in response to seeing this flash
*  such that on the next time they will be more nearly in sync with that flash and
*  it's not an especially complicated form of order especially sophisticated but
*  still it's self-organizing in the sense that there was no teleology right there
*  was no goal there was no idea that we're gonna get together and do this it's just
*  everyone's doing their own individual thing and sudden or not so suddenly but
*  y'all ultimately they're all doing the same thing I saw you you know do the same
*  thing at a TED talk where you ask everyone to clap in the audience and
*  very quickly they're all clapping in rhythm yeah that's an interesting
*  comparison because there the audience knows it's trying to get in sync and but
*  but yeah you're right that the fireflies don't have any particular goal and there
*  are different theories about why they're doing it I mean I should clarify it's
*  only the male fireflies that are doing this it's definitely something going on
*  with mating you know it's not it's not just all fireflies the females are
*  flying around and they're looking for males to mate with and it seems that
*  well so this is where the biologists haven't quite figured out what they want
*  to say they used to say the idea was that all the fireflies of a certain
*  species would get in sync because it would send their message the farthest
*  possible distance because you would make a very bright signal that could escape
*  you know the darkness of the jungle you could sort of the females could find
*  them from far away because there'd be this beacon like here's where all the
*  boys are you know but still from a Darwinian perspective how is it to my
*  advantage if I look just like my neighbor you know maybe she'll come in
*  do the females flash at all they will flash yeah I mean sometimes they they
*  will flash they actually do a little dance of light where they flash and then
*  if the male is flashing in the right way that is they want to mate with someone
*  of the right species because if you go with the wrong species you could get
*  eaten yeah okay but so but they do they send signals to each other and you know
*  if the flashing is done in a way that they find attractive that or from
*  someone of their species then they'll actually be drawn toward it so yeah but
*  the females are flashing too there's a lot of signaling to find each other and
*  make sure everybody's on the same page and your your mathematical result was it
*  that this kind of spontaneous ordering by a synchronization is inevitable or it
*  happens under the right circumstances is it rare and fragile or generic or what
*  well so yeah that's the the particular model that we made was the simplest
*  possible thing where we imagine every firefly could see every other firefly
*  and that isn't really true you know really they would mostly see the ones
*  that are near them in a tree and they wouldn't be paying very much attention
*  to one that's a mile down the river yeah but we ignored that so we did what in
*  physics would be called the infinite range approximation where every firefly
*  is imagined to be able to interact with everyone else out to infinite distance
*  away from them the reason for doing that is that when you're studying something
*  that consists of a million interacting you know complicated there they're sort
*  of complicated for the reasons I said with this RC circuit analogy so if
*  you're trying to study the collective behavior of a million of these little
*  tricky things you don't want to think have the additional complication of who
*  exactly is talking to who so because we didn't even know how to solve the
*  simpler problem yeah so so yeah so in the case that we did with everyone
*  interacting with everyone we proved actually this is one of the few times we
*  did actually really prove a theorem we proved that for this model they would
*  always synchronize in the sense that then it's not that there wasn't a
*  possibility of something else happening it's just that there was zero chance of
*  it happening so in in the jargon it's like this if I what I want to say is it
*  had probability zero yeah it's not the same so what's a good analogy for this I
*  don't know for physicists it's gonna happen you know you're you're a
*  mathematician you're trying to be more careful don't bother it's gonna happen
*  zero probability doesn't mean that there aren't possibilities of it happening it's
*  just that you'd never see them in practice I mean to give a loose analogy
*  if I throw a pencil in the air there is some possibility it could land on its
*  point and balance yeah that is possible it just you're never gonna see that
*  that's right I mean it's possible that the popular vote for president would be
*  exactly a tie right yeah yeah these things can happen but your your
*  mathematical notion of you know measure zero is even less than that this is just
*  not very likely so that's the idea the fireflies are gonna come into
*  synchronization that was great that was a great triumph and then but the one of
*  the wonderful things and one one of the wonderful things consistently about good
*  math is that it finds application all over the place so in the brain and how
*  we sleep and things like that similar notions come to rise right mm-hmm
*  that's true there there's so many different examples of spontaneous
*  synchronization that are important in science and in medicine and nature so you
*  know like you mentioned the brain so a lot of neuroscientists will tell you that
*  synchronous oscillation of neurons in the brain is related to phenomena like
*  attention and memory you can sort of see sometimes when if you're looking under an
*  fMRI machine you know that's like people call them brain scans or they talk about
*  what part of the brain lights up when someone's doing a certain task or
*  whatever very often the way the brain will sort of get itself okay so here's
*  an example suppose I'm looking at an apple you know what that's and I can
*  recognize that it's an apple you might think that's kind of obvious of course
*  you can recognize it but not everyone can there are people with brain damage
*  who can't recognize simple objects anymore so what there's actually a
*  miraculous thing happening in our brains when we see an apple on the table and
*  recognize it as an apple and not something else we think about what's
*  involved you have specialized neurons that detect color there are others that
*  are looking at shape there are some you know that are thinking about other
*  qualities of the apple and we somehow put all those different qualities
*  together to recognize one whole coherent object the apple and what you observe in
*  the brain when that's happening is that the parts of the brain that are noticing
*  color are actually firing electrically at the same frequency as the parts that
*  are noticing you know shape or whatever so so so synchronous oscillation is the
*  brain's way of the biologists call it the binding problem how do you bind all
*  the different features of an object into a coherent single object to recognize
*  that it's not just a bunch of different things happening in your brain all at
*  once interesting so it's not just that there's a part of my brain saying I'm
*  seeing something red and another part saying I'm seeing something apple-shaped
*  but they're saying it in synchrony with each other and somehow that lets the
*  brain or our conscious perception say that is an apple yeah and it says that
*  right exactly those separate things that are all oscillating in sync are all
*  meanwhile other parts of the brain that are not paying attention or that are
*  thinking about or you know like interested in other aspects they they're
*  out of sync and so they're ignored that it's the brains way of telling itself
*  what's what's all part of one object or one sensation go ahead I was just gonna
*  say I'll be very honest and confess that I didn't actually read this chapter of
*  your book I just you know remember the the chapter title so I wanted to ask you
*  about it but does this imply that there's a separate part of the brain that
*  is keeping track of the frequency of oscillations to say oh yes this is a
*  coherent thing mmm that's an interesting question yeah it might be I
*  think the thalamus is often regarded as a relay station for that it takes in
*  signals from different parts of the brain and it might do some of the
*  binding of of what's happening elsewhere right okay I'm not positive I've got
*  that right so your listeners correct you scientists and the physicists so you
*  know you're allowed to say that you did not an expert on the part I'm not sure
*  but I am pretty confident that if you ask most brain researchers now they'll
*  tell you the binding problem is solved by synchronization or at least that's
*  the best current guess now I should say you don't always want things in sync in
*  your brain so epilepsy is a famous disease you know you can picture
*  someone having those during a seizure the most famous symptom is these rhythmic
*  convulsions and the rhythmic twitching and convulsions is that many millions or
*  neurons are discharging in perfect step when they're not supposed to yeah that I
*  did know about this is a problem and this is this is always one of the
*  problems with organization that you want the right amount of it yeah exactly so
*  yeah you can have pathological synchrony too and where does sleep come into this
*  I literally just yesterday was having a conversation with a bunch of scientists
*  in different areas about you know so why do we sleep and the answer is often
*  well there's this chemical that puts us to sleep but there's the higher level
*  question what is the purpose of falling asleep is this kind of research relevant
*  there it could be that question wow you know I mean that takes me back my PhD
*  was about sleep research I worked on human sleep and circadian rhythms those
*  24-hour rhythms that we have in hormone fluctuations and body temperature and
*  lots of other internal rhythms so you know but nobody has ever really believe
*  it or not figured out why we need to sleep it might sound ridiculous like my
*  mother when I was a kid say she actually had she had a theory she said because
*  you have too much sleepy gas mechanistic theory I like it yeah she said when
*  you're awake the longer you're awake the more sleepy gas you build up and then
*  eventually when you get so much of it then you have to go to sleep and then it
*  goes away so she was actually doing the RC circuit model that I talked about
*  earlier where something builds up to a threshold and then she imagined it gets
*  degraded and chewed up when you're asleep but actually that isn't so far off from
*  what one of the leading theories of what's going on is that there are sleep
*  substances that are measurable there are peptides that that can be detected for
*  instance there's a classic experiment from a long long time ago maybe about on
*  the order of a hundred years ago where researchers kept sleep sorry sheep the
*  animal the farmyard animal you keep a sheep awake how would you do that I
*  mean you could probably keep bothering it and disturbing it and poking it I
*  don't know so they did something to keep the poor sheep awake for way past its
*  bedtime so it's letting let it read Twitter that'll be enough yeah you can
*  do sleep deprivation on an animal and then the experiment was take a little bit
*  of the blood of that animal that is sleep deprived and injected into another
*  sheep and that other sheep falls asleep right away okay so is that that certainly
*  seems to imply to my scientific mind that there is a chemical tracer in the
*  blood that saying dude you should go to sleep yeah that so that and we've over
*  the years isolated candidates for that for a long time it was thought to be
*  something called me or amyl peptide that was the the alleged sleep substance I
*  think others have been found since then so it's possible that that's one of the
*  things that's happening that just being awake and active produces biochemical
*  byproducts of activity that that give you the subjective sensation of feeling
*  tired and that that is you need to restore yourself back to having less of
*  that stuff so sleep is partly for that but it seems there's a lot more going on
*  with sleep I mean there are ecological reasons to sleep depends on if you're a
*  predator or prey you know if you're a prey you want to be in your burrow
*  especially when it's not favorable for you right you're like an animal that
*  wants to be out in the daytime then you better be hiding when it's nighttime
*  when all those nocturnal animals are looking for food so you can see how
*  synchronization it gets involved with all these different things certainly
*  about to fly to Europe and I know that jet lag is something that hits me very
*  hard and apparently that's in part because different circadian rhythms
*  inside your body get out of sync with each other mm-hmm they're right exactly
*  that is what jet lag is it's it's a funny thing a lot of people get confused
*  about it and they say I've heard so many people say oh I don't get jet lag I just
*  you know I I stay up all night and then I sleep it off the next day and then I'm
*  better but what they're what they're not noticing is that jet lag just is not
*  only about sleep and sleep disruption there are all these other rhythms that
*  we're not so aware of that are inside of us like you know I mean you could if you
*  think about it you're aware but when do you want to go to the bathroom yeah when
*  do you feel hungriest when are you most alert those are internal rhythms and
*  then there are others that like I say body temperature is going up and down
*  even if you lie still in bed and people have done experiments like this just
*  keep someone awake in bed all day long you can measure their temperature and is
*  going up and down like a nice sine wave so there there are internal rhythms of
*  temperature of alertness and what happens during jet lag is that even if
*  your sleep gets on to the local time your internal rhythms are still back at
*  home time that's the lag in jet lag yeah every individual person has a lot of
*  things going on inside them that can be in or out of synchronization it really
*  does matter right that's right and so the there are things in the outside world
*  that help to resynchronize us what's most important is sunlight but food is
*  another one the timing of your meals will affect and melatonin of course
*  people have heard now of this brain hormone melatonin that you can use as a
*  pill for a sleeping pill or for circadian rhythm restoration pill but I
*  have to say I've always been skeptical of melatonin not having used it so
*  maybe those of you people out there who are listening and do use it and swear by
*  it I'm not saying don't use it but I can tell you that in experiments picograms
*  of melatonin are enough to be biologically active that is that'd be a
*  one follow that's like 12 zeros right you know picogram is a tiny tiny tiny
*  amount of melatonin has a biological action so I can't imagine how much is
*  in a pill I think it's like a trillion times more than your brain wants so I
*  feel like really you're taking such an ungodly amount of melatonin I would be
*  scared to do it but I don't hear of anyone having trouble with it so I'm
*  probably wrong you know I'll confess I think the melatonin is a miracle drug
*  for me and it could be entirely psychosomatic but because I don't take
*  sleeping pills and I generally have no trouble sleeping and even if I take you
*  know Nyquil I wake up feeling groggy and I just don't want to do that but when I
*  travel and I I want to get to sleep with something like the local bedtime I
*  take melatonin it puts me out and I feel no after-effects the next day it's well
*  I got to start doing it I mean this is a case where I'm too much of a theorist
*  yeah well you know it could be killing me long term I don't know but hope not
*  yeah okay you you you raised this issue and I really wanted to leap in at the
*  time but I knew we had other things to talk about so I didn't you raise this
*  issue with the fireflies of the approximation where every firefly is
*  seeing every other firefly now obviously that's not true but maybe it's a good
*  enough approximation to get what's going on in something like the brain it's even
*  obviously less true and it's kind of super important that it's not true right
*  every neuron is not talking to every other neuron and I think correct me if
*  I'm wrong that this kind of consideration led you to think about the
*  phenomenon of networks and how things were connected which eventually resulted
*  in a paper that has so many citations of my jealousy is overwhelming well it is
*  that's right that it was it was a desire to move away from that very
*  unrealistic infinite range approximation and to just start paying attention to
*  whatever new phenomena would occur if we if we tried to be a bit more realistic
*  about the networks that really do occur in so many different phenomena that they
*  got us thinking about what came to be called small world networks so the the
*  phrase small world is supposed to make you think of that experience that we all
*  have when we get on a plane or go to a cocktail party and you meet somebody and
*  you start talking and then you realize oh yeah my cousin went to that summer
*  camp and you know so then people say oh it's a small world because it seems
*  like how is that possible we how can we be so or there's also the counterpart
*  you know the other phrase that you hear all the time is six degrees of
*  separation yeah that I know someone who knows someone and we can connect
*  ourselves to anybody it seems through just a very small number of mutual
*  acquaintances or chain of acquaintances well I'll mention a popular game right
*  that Kevin Bacon game with with actors I'll mention that this morning Jennifer
*  my wife is a science journalist said do you know a guy named Eric Winfrey and
*  of course yes because he's a professor at Caltech but also I realized you know
*  he I think is the nephew of one of your collaborators or mentors in the in the
*  synchronization game right he's actually the son oh he's the son yeah he's Art
*  Winfrey son and Art Winfrey was my closest mentor of my career it's a small
*  world yeah it's a small world when I went to work with Art Winfrey he at that
*  time he had a 12 or 10 year old son Eric who has gone on to be a great
*  scientist and is your colleague at Caltech but who also I'm notable about
*  the two of them is that they're one of the few father and son double MacArthur
*  award winners they both got MacArthur prizes that's something to tell your
*  dad like I got my own MacArthur now yeah so two geniuses in the family but and
*  Eric was very smart little boy I'm not surprised he's turned out to be a very
*  smart professor too and it's actually not surprising because we're all
*  academics and scientists and so forth but if you did a very simple view of the
*  world where everyone knew you know whoever lived within five miles of them
*  and nobody else then it would take a huge number of steps of separation for
*  me to get from someone in another continent and the small world network
*  phenomena says no it's really just not like that at all yeah that's right
*  that's that's what's so counterintuitive because we do have this
*  strong sensation that I only know the people that live near me geographically
*  or that are in my department at work or you know go to my church or whatever it
*  is so we feel like we move in small circles and so that's why we are always
*  so surprised and say oh wow that's weird it's a small world and yet you know if
*  we were statistically minded we should be thinking this small world thing keeps
*  happening to me it must not be that right because everybody experiences it
*  so it's there must be some explanation and one of the things that Duncan Watts
*  who was my grad student at the time was interested in his father had said to him
*  do you know that you're only six handshakes from the president you know
*  that you could find some people you may not have ever met let's say in this case
*  Donald Trump but you might know someone who knows someone and within six
*  handshakes you you'd know someone who knows Trump yeah so that that struck
*  Duncan as an interesting thing because at the time he was trying to study not
*  fireflies but crickets you know there are crickets that can chirp in unison
*  it's the analog of the fireflies flashing in unison so the biologists
*  speak of choruses of crickets that are all chirping at the same time and we
*  have us particular species of those crickets snowy tree crickets as they're
*  called that live in Ithaca and so we thought we could do experiments on these
*  and see if some of the mathematical models of synchronization actually
*  predict what the crickets are really doing that would be new because the case
*  of the fireflies in Thailand much harder to go all the way to Thailand and
*  capture them but the crickets are right here in the orchards in Ithaca New York
*  where I you know I teach at Cornell and so we have we have mass like the
*  grandmaster of sonic synchronization right here this snowy tree crickets so
*  we thought that would make a nice experiment for Duncan to do for his a
*  project for his PhD work and so he learned how to capture the crickets and
*  keep them alive and we were starting to put them in little soundproof boxes so
*  that they could we could control how strongly they could hear each other and
*  you know like sort of try to set up an experiment with the help of a bio
*  acoustics expert named Tim Forrest anyway it was in the course of doing
*  these cricket experiments that Duncan started to think about I wonder you know
*  when the crickets are out there in the orchard who's actually listening to who
*  do they all hear each other that can't be right maybe they only hear the ones
*  right next to them and so he got to thinking about connectivity in general
*  and then he threw a brainstorm has remembered this thing his dad had said
*  about six handshakes from the president and so he came into my office one day and
*  said I how would if things were connected in this small world or six
*  degrees of separation way would they synchronize better than if they were
*  just connected to their neighbors or would they I mean how would how would it
*  work and I thought I don't know I mean I don't even know how you do this six
*  degrees thing what and so we realized there's a whole big math problem what
*  explains the small world and not only that but how would it affect
*  synchronization and Duncan said it's much bigger than synchronization it
*  would because anything that's connected like that you'd think it would make a
*  big difference because everyone is so close to everyone in the sense of the
*  small world just a few hops away from everyone else so like how would that
*  affect diseases spreading yeah at the time actually people were talking about
*  HIV a lot you know it doesn't get discussed as much anymore but during the
*  height of the AIDS epidemic you would hear people say if you sleep with
*  someone you're not just sleeping with them you're sleeping with everyone that
*  they slept with and everyone that that person slept with so the idea was out
*  there that you know you feel like you're only interacting with a low-risk group
*  but actually you're only a few steps away from from you know from the virus
*  let's say I think I'd actually like I would like to try explaining these two
*  concepts that you talk about in the book that are that are relevant to
*  characterizing these networks the idea of the shortest path between two people
*  in the network and the separate idea of the clustering right like how many
*  people are connected to overlapping friends mm-hmm that's something really
*  different terms totally yeah it's it's not not very hard the idea of path
*  length is just the idea that we were talking about with six degrees that if I
*  mean like let's say you and I we've never actually shaken hands right so
*  we haven't met but and I don't actually know what our shortest path is but we
*  could start naming physicists and mathematicians that we've met like I
*  okay I'm gonna guess I'm guessing you've shaken Brian Green's hand I have he's
*  been a previous podcast guest so okay so and I know Brian Green because I've
*  known him since he was a high school student so so that would make and I
*  don't think there's any faster route I mean I that's one handshake from me to
*  Brian and one handshake from him to you so we're two degrees of separation apart
*  and that's our shortest possible yeah that's our path length right so path
*  length is just what's the shortest route from one node in a network to
*  another and so okay so that's one thing you can calculate for a network you'll
*  look at all the shortest paths between any pair of points in the network and
*  then that average is what we would call the average path length in the network
*  which is basically a way of quantifying this idea that everyone's about the
*  number six is not important it's just that it's a small number of steps from
*  any point to any other point even in a very big network like something the size
*  of the world with seven billion people but but if your network were more like
*  a lattice where you only knew your nearest neighbors then the average path
*  length would be enormous that's right so right if you picture a checkerboard like
*  think of the nodes in the network as being the squares of a checkerboard on a
*  say literally a checkerboard which is eight by eight if you wanted to go from
*  diagonally opposite corner the fastest way you could get there well you could go
*  down the diagonal I guess but that would still be eight squares in between yeah
*  and so there if the world starts getting big that shortest path is also getting
*  very big it would not be you know like in a world if it were seven was it well
*  seven billion sort of hard to take the square root but if it were okay so let's
*  say it was it was ten to the tenth so we had ten billion people on earth which we
*  will pretty soon if we're ten billion people on earth and they were standing
*  in this big square checkerboard pattern that would then be as you said ten to
*  the fifth so that's a hundred thousand people on each side of the square
*  hundred thousand degrees of separation I would say six degrees of separation
*  they'd say a hundred thousand degrees of separation right and no one would say
*  it's a small world because it wouldn't be right so the point being that that
*  worlds don't have to be small the checkerboard world is not small and yet
*  our world is small so so that was a question that Duncan and I wondered
*  about what does it take to make a world small the other question though is you
*  know that the common-sense answer to this what does it take to make the world
*  small comes from an old idea that like suppose I have a I know a hundred people
*  or whatever number you want to pick it could be a thousand but let's say it's a
*  like I know them well enough that they could they would lend me money right you
*  know maybe I have a hundred close friends and contacts and relatives okay
*  so if I know a hundred people and each of them knows a hundred people then
*  naively I can just figure out how small the world is by saying a hundred times
*  a hundred or in your scientific notation that's ten to the two times ten to the
*  two that's ten to the fourth and if I want to get to ten to the tenth I have
*  to do this five times so you know it'd be five degrees of separation if the
*  world were such that I know a hundred people and everyone else knows a hundred
*  people except not the same hundred people that's the trick in other words
*  if there's no overlap then this simple multiplication of a hundred times itself
*  doing that five times that will be enough but that's the trick as you say
*  the problem is that of the hundred people I know when they know a hundred
*  people a lot of those are the same people because we live near each other
*  or because we're in the same profession or whatever and so that's the pro that's
*  what we're calling clustering the fact that it's not just a random choice of a
*  hundred people anywhere on earth but so we have a more precise definition of
*  clustering which is we imagine you could think of it this way think of two people
*  you know and now ask do they know each other now maybe they do like maybe they
*  don't like maybe someone you're thinking of right now is someone you went to high
*  school with and someone else is somebody that you know now from work and they've
*  never met and they don't know each other okay so those two people don't know each
*  other even though they both know you but you could also think of two of the
*  people at work maybe they do know each other so the concept we had for
*  clustering is pick any two of your friends and ask what's the probability
*  that they're also friends of each other yeah okay so it's an it's a number from
*  zero to one and in some types of worlds that number will be very small and close
*  to zero and in other types of worlds it would be very also we used expressions
*  like we imagined kind of fraternity world where you know the only people you
*  know are the people in your fraternity so of course two of your friends will
*  know each other because they're in the fraternity too right okay so that in
*  that kind of world the clustering coefficient as we called it will be very
*  close to one it's almost a certainty that your friends will know each other
*  whereas if you picked your hundred friends at random on the surface of the
*  earth you know for me there's one in Ethiopia and one in Indonesia and then
*  each of them pick their friends at random hundred friends somewhere else
*  on earth there's very little chance that two friends of yours would know each
*  other that just that Dodds are way against it that they would happen to
*  happen you know they there's no reason they'd pick out of their hundred people
*  out of 10 billion why would they pick those same friends and these two
*  examples I think these are sort of like the classic kinds of networks that
*  people had been thinking about either everyone knows everybody else so there's
*  lots of clustering and the path is also also very short or nobody knows every
*  anybody else and so the path can be short but there's no clustering is that
*  right well let's see if we got that right I mean I didn't get it right I
*  think not quite so the like the checkerboard world or actually we often
*  don't use a checkerboard we used to like to think of it as people standing in a
*  circle right so if all 10 billion people were just standing out there in a big
*  circle where the hundred people they know are the ones right next to them in
*  the circle so there I have 50 friends on my left and 50 on my right and I don't
*  know anybody else and the same for everybody else in the circle the same
*  thing that's a very big world because for me to get a message let's say to
*  someone diametrically opposite me I have to go leapfrogging around in steps
*  of 50 right and it's gonna take a long time to get over 5 billion people away
*  so path length very long but clustering very yeah it is clustering yeah high
*  clustering because of my 50 friends on either side they will overlap a lot right
*  you know if I move as I move to my friends there so those worlds that kind
*  of world has very high clustering but very long path yeah and the other kind
*  of world the random world has very is very small but it has no clustering
*  right and so what we thought was this kind of paradoxical thing is that our
*  lives it feels like our lives are very clustered most of our friends do know
*  each other or at least many of them do much more so than if the world were
*  random but yet the world seems small almost as small as if it were random
*  right and so that wasn't obvious how could you have both because the real
*  world somehow does have both could you make a model that has both and what
*  Duncan and I realized but mainly him was that what was really important I mean
*  one way to do it and we thought this was the way it was probably done is if
*  people had certain number of far-flung connections to give you an example of
*  what I'm talking about I used to play a lot of chess on the internet and I got
*  to be friends with a guy in Holland and I mean I would say he was really my
*  friend I knew how many kids he had and I knew about his life and I never met
*  him actually face to face but I feel like he was my friend but the point
*  being if I wanted to get a message to somebody in Holland I could use my link
*  to him and there'd be a chance he would know that person or he'd know someone
*  who would know the person in other words there was this bridge where I was
*  suddenly connected to somebody I had no business being connected to except that
*  we both like to play chess on the internet and that bridge not only made
*  me closer to everyone in Holland but everyone that I know is also now much
*  closer to everyone in Holland although they don't realize it right right
*  because they know me and I can take the bridge you know what I mean so likewise
*  more conceptually if you had a friend from high school who is now a classical
*  pianist suddenly you have a whole bunch of connections it's a short distance to
*  you to everyone in the classical music world exactly right and and so what's
*  interesting about this mechanism we call the shortcuts is that the shortcuts
*  really make the world very small very quickly though you don't sense it
*  because you don't realize you're connected to everyone in the classical
*  music world right I mean because it doesn't sort of operate in your
*  consciousness but you are and so this this shortcut mechanism we showed that
*  very very few shortcuts were enough to make the world incredibly small and that
*  seemed to be a very generic phenomenon that because it took so few of them it
*  seemed like most networks would have this property because you kind of in
*  order to avoid it you had to scrupulously avoid having any shortcuts
*  in a network and so we made a prediction back in well I guess it was a now I'm
*  just spacing out what night when did that paper come out hmm it was a while
*  ago yeah I think it was okay 98 yeah yeah that sounds right yeah 1998 the
*  paper came out in 1998 and so we had said the brain for instance will turn
*  out to be a small world network when we can measure all the connection that we
*  haven't yet measured all the connections between all the neurons there's
*  estimated to be trillions of neurons in the brain tens of trillions I think so
*  we don't know what the connectome as they call it is for the brain but we do
*  know the connectome of a tiny worm that's the one nervous system that's been
*  completely mapped out called C elegans oh yeah my favorite little tiny worm
*  yeah so we know every neuron in its body there's about 300 of them it's only a few
*  I think something like on the order of a thousand cells in the whole creature but
*  by looking at the the nervous system of this worm we showed that it actually
*  satisfied our criteria for a small world that it was much more clustered than a
*  random world yeah but it also had path length about comparable to a random
*  world so it was as small as it could be well much more clustered and the
*  internet and a whole bunch of other networks in the real world networks lots
*  of real-world networks turn and since then I mean in the 20 years since then
*  it's been abundantly documented that that our prediction was right lots of
*  naturally occurring networks will be small worlds and you could ask well okay
*  so what but what's interesting is that small worlds allow for very fast
*  propagation of information through these shortcuts so anything that needs to
*  coordinate itself or act as a as a coordinated unit but is very big a small
*  world mechanism is a really good way to do it but also it's dangerous in the
*  case of like the HIV example anything that can spread for good or for bad will
*  spread much faster on a small world than it would on on say on a lattice or a
*  ring and also typically a wonderful example of self-organization right like
*  nobody planned it out you said naturally occurring these there's
*  mechanisms that typically give rise to networks just like this mm-hmm right
*  they're found all over the place and as you say there's no central planner
*  there's no need to design it it just sort of happens on its own I did want to
*  mention one thing earlier actually that I sort of I hit head in my head but
*  didn't say out loud which was that there's another way of making the world
*  small that you could imagine which we deliberately did not imagine which is
*  you could imagine that there's somebody that everybody knows right I mean if
*  everybody knows Lois Weisberg so I use that example because Malcolm Gladwell
*  wrote an article a long time ago called six degrees of Lois Weisberg that she
*  was this person in in Chicago that seemed to know jazz musicians and she
*  knew newspaper people and just everybody knew Lois Weisberg anyway so
*  that's one way that the world can be small if everyone knows these super hubs
*  these connectors right then of course everyone's just a few degrees away
*  because they're all close to Lois Weisberg but we didn't think that was
*  really gonna be first of all that felt like cheating like of course that will
*  make the world small if you have that but more to the point we thought that's
*  not really gonna be how nature will use it that's not the mechanism because for
*  one thing it's hard for the Lois Weisbergs out there to maintain all
*  those connections it's a lot of energetic cost a lot of it's just hard
*  and you don't need to right well you don't need it I mean of course you might
*  have it but but you don't need it the shortcut mechanism and you need only
*  very few of those doesn't cost much and that that will do the job for you but so
*  we deliberately ignored also I I would say that I had been told by my friends
*  in neuroscience that every neuron in the brain connects to about that is make
*  synapses with about 10,000 others okay which might sound like a lot but then
*  when you remember that there's you know trillion neurons in the brain or
*  something like that or maybe it's a hundred billion but it's it's way way
*  more than 10,000 yeah but it's a lot yeah okay right so it's on the order of a
*  So that's right so if it's 10 to the 11th but there's only 10 to the 4 synapses per
*  neuron yeah you're dead you know that's a factor of 10 to the 7th difference so
*  it's a very sparse network in that sense you're not connected to anything like
*  the whole network and there are no Lois Weisbergs in the brain so we we
*  deliberately didn't want to pay attention to those networks and the reason
*  I'm harping on this is because we missed the boat it turns out that there are a
*  lot of networks that use hubs the most obvious being airports you know if you
*  think of the airport airport system and for air travel you fly to a hub and the
*  hub has a lot of routes going into it so there are some networks that use this
*  hub mechanism to make the world small and so that was studied by other people
*  and we didn't you know like I say it's an interesting thing like in the history
*  of science that sometimes you'll have a prejudice about what you think the way
*  the world should be and you deliberately don't let yourself entertain another
*  possibility because it strikes you as ugly or too simple or irritating in some
*  way the world is very is very irritating because they keep doing different
*  things in different circumstances and different model yeah employment but still
*  like it's a little bothersome sometimes anyway those kinds of networks with the
*  hubs were published you know an analysis of them came out the year after our
*  paper on the small world rake Albert and her advisor Laszlo Barabasi wrote a
*  paper about what they called scale free networks that had not only hubs but also
*  a distribution of the jargon is degree that's how many connections any
*  individual node has how many friends in our earlier social network analogy so
*  if you ask how many people have say 10 friends how many have a hundred friends
*  how many have a thousand friends you can find people with more or less big
*  Rolodex's and it obeyed a power law in that you know there was the probability
*  of having a certain number of friends went down like the number of friends to
*  some power one over it was an inverse you know like one over X to some power
*  because to three or so one point two so that technically point two would be a
*  small world network but it has this extra feature that they're also lowest
*  Weisberg's there were lowest Weisberg's and also sort of like things a little
*  bit less than lowest Weisberg you had sort of lowest Weisberg's at all scales
*  right of degree they were small worlds they didn't have the right clustering
*  properties actually at least in the first models so we missed the hubs
*  Barabasi and Albert missed the clustering and since then people have
*  figured out that real networks are more complicated than the models either of us
*  proposed which was no surprise we were both putting out really idealized simple
*  models and do you think for thought experiments because this is within the
*  realm of self-organization I mean these kind of networks we can speculate a
*  little bit it's late in the podcast these are at the heart of how complexity
*  and complicated interconnected systems arise in a world that is ultimately
*  governed by the second law of thermodynamics and things run down well
*  it's all I can say is it both of these are common network themes the small
*  world theme and the scale free there there are a lot of other things going on
*  we've we've learned a lot more about networks in the past 20 years so they
*  were they were very stimulating early ideas I think we could say that I
*  wouldn't I wouldn't claim that either one of them is in kind of I mean the
*  small world law is pretty much a universal lot that almost every real
*  world network is going to be a small world by our criteria yeah scale free
*  has not held up as well but it's still a pretty common theme to say if you the
*  power law part is the part that's not reliable if you just ask is the
*  distribution of degrees something that obeys a heavy tail meaning it doesn't
*  look like a bell-shaped curve with a exponentially damped tail but as
*  something that's got a lot of a lot more of these lowest Weisberg's than you
*  would think yeah that does seem to be true yeah a heavy tail distribution has
*  a lot more things you might think are unlikely or improbable than you would
*  get by doing sort of traditional bell curve like probability distribution
*  that's right and the other word so the world is full of things like that and
*  we're still learning to deal with them maybe you know earthquakes or solar
*  flares are examples of these which means that you know terrible disasters can
*  happen a lot more frequently than we might guess uh-huh it's true there are a
*  lot of those heavy tail distributions in natural disasters yeah with floods
*  wildfires I mean they the statistics of those are often very heavy tailed so
*  okay clearly we have enough room for a whole nother podcast down the line so
*  that is good but I do want to give you a chance because you mentioned right at
*  the beginning how the very favorite tool of every mathematician which is calculus
*  isn't an obvious fit to the kinds of studies you want to do with the fireflies
*  where there seem to be some kind of discontinuous jump and nevertheless
*  your most recent book is about calculus so I think many people think of calculus
*  as there's nothing new there like we've done calculus a long time ago and in
*  fact my memory of it is you know one might say a terrible class I had in high
*  school what is it that you think makes us need another book about calculus
*  right now well I would sing the praises of calculus I think it's one of the
*  greatest achievements in the history of humanity you know this is something that
*  took about more than 2,000 years to develop starting from the days of
*  Archimedes up through Isaac Newton and Leibniz and I'm taking a very broad view
*  of what I mean by calculus but let's say roughly speaking the systematic use of
*  infinity to solve hard problems right you know that's the thrilling idea in
*  calculus that you can take a hard problem and chop it up into infinitely
*  small that is infinitely many infinitesimally small pieces and then
*  those turn out to be easier problems to solve those small ones and then if you
*  can figure out a way to put them back together which is what we call integral
*  calculus or integrating a differential equation then you can do the kind of math
*  that has changed the world I mean that's the math that let Maxwell predict
*  the phenomenon of wireless that's letting us talk to each other right now
*  yeah I always try to gloss calculus as saying it's the statement that a
*  medium-sized thing can be thought of as an infinite number of infinitely small
*  things yeah that's a great great insight and it it literally changed the world we
*  can't without it we wouldn't have radio we wouldn't have television we wouldn't
*  have turned the tide in the fight against HIV so in the book I'm trying to
*  make it's called infinite powers and I'm trying to make the case about just how
*  how revolutionary calculus was when it was invented and how it's still giving
*  us gifts today but I feel that there's a need to do it while it's true as you say
*  it's not the newest thing under the Sun a lot of people in fact like million more
*  than a million students in the US alone take calculus every year and for them
*  it's something that they do the advanced placement test and they don't
*  know what the heck they you know why did I do that yeah it's often just taught as
*  like a lot of there's a lot to learn I mean there's a lot of technical things
*  to learn about how to do this kind of integral or that kind of derivative but
*  I feel like the great human story of this fantastic idea that I would rank
*  right up there with evolution and quantum theory you know this is a
*  fantastic thing that I want people to understand just how rich the story is and
*  and and how world-changing it was and still is yeah that's that's why I add
*  some to me it's not another calculus book it's a book that's we know it those
*  of us who are professional scientists know these things but I don't think that
*  the typical high school student or even someone who might be teaching it in high
*  school they may not realize this this very broad context of what calculus has
*  done for the world well Jennifer wrote a book about calculus called the calculus
*  diaries and the gimmick was that a 40 something year old English major learns
*  calculus and learns to apply it to the world so I was helpful as you know an
*  experimental test subject when we went to Vegas or drove a car and just noticed
*  all the different ways in which you could think about the phenomena using
*  calculus so I completely agree with you that people just don't quite appreciate
*  how absolutely universal it is and if you really get what calculus is trying to
*  tell you your view of the world changes in a profound way perfect right exactly
*  so I feel like that that needs to be better known that this shouldn't just be
*  for insiders you know I really I feel it's a beautiful thing it's an inspiring
*  thing and so I know there are people out there who would who would like to know
*  this and I should say I've written the book for this sort of person actually
*  that you and I both like to write for the educated person who's curious but
*  who is not a professional physicist or mathematician or may not have even taken
*  these subjects in college maybe was happy to be done with them in high school
*  yeah well I think that's what makes it interesting because we probably there's
*  a pre-existing resonance with the word calculus in many people's minds and it
*  won't always be positive so you don't have a blank slate to deal with you're
*  trying to push up against some resistance and and that's a fun challenge
*  to take up yes it is yep all right Steve is drunk guys thanks so much for
*  your time thank you Sean this is great fun I'll definitely be recommending all
*  your books and I want to read more about small worlds and scale-free networks and
*  things like that and we will have you on the podcast again to dig into them
*  further okay my pleasure I hope I will all right thanks a lot
*  you

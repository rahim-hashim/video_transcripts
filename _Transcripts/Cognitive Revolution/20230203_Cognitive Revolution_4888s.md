---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 4888s
Video Keywords: []
Video Views: 3298
Video Rating: None
---

# The Pixel Revolution with Playground AI's Suhail Doshi
**Cognitive Revolution "How AI Changes Everything":** [February 03, 2023](https://www.youtube.com/watch?v=Waii0i1bBFY)
*  It's kind of like that moment in mobile where it was just a complete like Wild West gold rush
*  and nobody had a clue what was going to work. And so just all like thousands, tens of thousands of
*  experiments occur simultaneously. And you end up getting things like Uber and some things like grow
*  really rapidly and then fall because they fall out of relevance, they have good retention.
*  And some things just have this incredible lasting power for a decade. So
*  feels like that will happen again. In one short year, image generation technology has achieved
*  multiple breakthroughs and revolutionized the world of creativity and art. Today, with mere words,
*  in just seconds, anyone can generate all sorts of high quality images and dedicated AI artists can
*  create top-notch award-winning art. Nathan, how did we get here? Well, Eric, do you remember where
*  you were when you first saw the Dali Avocado Chair? That was the original Dali announced two
*  years ago in January, 2021. Dali never launched to the public, but OpenAI did open source the image
*  classifier clip, which turned out to be all that the programmer artist community needed to make
*  some incredible breakthroughs. Within months, we started to see clip guided image generation models
*  and by late 2021, they were producing amazing results. The core idea known as denoising was,
*  like many AI breakthroughs, both simple and profound. The world already contained massive
*  data sets of images and captions, and it's easy to degrade images by adding a bit of noise.
*  So if an AI model could be trained to answer the question, what would this image look like if it
*  were just a little less noisy and a little more like the user's request? It would in theory become
*  possible to go from pure noise to high resolution images simply by denoising over and over again.
*  Sure enough, it worked. And in April, 2022, OpenAI, building on the open source community's work,
*  launched Dali 2. They were very careful at first. For a while, you couldn't even generate realistic
*  human faces. But their monopoly position and the editorial control was short lived because just four
*  months later, Stability AI dropped the weights of stable diffusion, which roughly matched Dali 2
*  in capabilities and unleashed an unprecedented wave of experimentation and creativity worldwide.
*  Since then, image generation has scaled faster than almost any technology in human history.
*  It's inspired entirely new products and become ubiquitous in familiar products as well.
*  Artists have been split on the topic. Huge numbers of creative people have developed
*  all new workflows, techniques, and styles, which were either previously impossible or
*  prohibitively expensive. But many have also felt understandably threatened. After all,
*  what happens to artists when anyone can create art? And it's precisely this wave of change that
*  our guest Suhail Doshi of Playground AI has dove into. While working to build a computer in the
*  cloud with Mighty, Suhail noticed the take-up and AI capabilities and just couldn't look away.
*  A few months later, he declared that he was going all in on AI, and Playground AI was born.
*  Playground AI is one of the highest performing AI image creators in the world today,
*  with one of the most generous free plans anywhere. Suhail's vision is to give users complete control
*  over pixels, not just text to image, but what you think is what you get for image, video, and 3D.
*  The Cognitive Revolution podcast is supported by Omnike. Omnike is an omnichannel creative
*  generation platform that lets you launch hundreds of thousands of ad iterations that actually work,
*  customized across all platforms with the click of a button. Omnike combines generative AI and real
*  time advertising data to generate personalized experiences at scale.
*  Suhail, welcome to the Cognitive Revolution podcast. Stoked to have you. By way of introduction,
*  why don't you talk about the evolution for you? What was the AI moment for you when you realized
*  I have to go all in on this? What was that moment like when you give a background as to what you're
*  up to in the process? I think sometime around early last year, we were making a browser called
*  Mighty. The goal of Mighty was to make a new kind of computer. We were hoping that if we could put
*  it in a data center that that would afford us to make a computer that no one had ever imagined
*  before. It would be a lot faster, a whole number of tasks that you would use web apps for. It was
*  extremely controversial. One of the things that I started to poke at as the team was building the
*  browser was I started to wonder, just watching the steady advancements of AI even just early
*  last year, around April, May, I think April, Dali came out, things like that, started to unfurl.
*  I started to wonder if we could make big improvements to the address bar in the browser.
*  Turns out, we know a lot about the address bar in Chromium, too much. One of the things we learned
*  is that it doesn't have a lot of intelligence to it. It's actually not very smart. It's very
*  quite dumb. I think Google is not terribly, and I'm sure the PMS at Google are terrified to change
*  this address bar because they make any change and search yield goes down and they make less.
*  Then they could lose billions of dollars. This code is very crafty. It's almost unchanged for
*  the last five years. I thought to myself, could we make this better? There's this funny thing in
*  the address bar where at least at that time, if you went to a recent link, something you go to
*  frequently, it would always be at the bottom of the address bar, not the top. There are all these
*  inefficiencies with the address bar. We use it every day, hundreds of times, thousands of times
*  a day. I just thought, boy, it sure would be cool if we could make a better address bar predictor.
*  I typed something in and we could just predict where you would want to go. We started to try to
*  collect all this information and try to make a better address bar predictor as all often
*  with our users and stuff and our own staff. We started to see if we could do that. That
*  really gave me the bug. It was at that point that I had to go and do research and figure out
*  how I would go do this. I started meeting more PPAI researchers in the community.
*  That really gave me the bug of like, wow, these things are really, really amazing.
*  I just kept finding more things, more the pace, the momentum of everything that was happening
*  was incredible. I even remember just feeling like, gosh, why hasn't GPT-3 had been out
*  for a couple of years and still nothing was very, very close to its performance? I think
*  that's maybe a little bit different now. There's more arguments to say folks like Anthropic and
*  whatever are competing to a degree, but it's actually quite old. Then we started working on
*  things like summarization in the browser. If you went to a blog post, could we use GPT-3
*  to summarize these blog posts? Because people don't read that much. Could we summarize everything in
*  three bullet points and then we started to learn about hallucinations with AI? We just kept thinking
*  of more features that were more AI focused, but for the browser. That started my first
*  foray into everything. How did you explore the idea of DMAs in terms of, okay, this is the
*  Playgrounds product that I want to build? I remember staying up late one night. I had been
*  kind of contemplating. I had been working on a Windows launch for Mighty and it was just taking
*  a long time. I didn't have a lot to do, but I had been constantly thinking about AI. It was
*  this thing that I couldn't get out of my head for some reason. I remember it was 11 o'clock at night
*  and I just went to my Apple Notes and I wrote down every company for every part of the space.
*  I did my own market map. There was no market map, so I just did my own in my Apple Notes.
*  I remember writing, who's doing logging and visualization, which was more or less like
*  Mixpanel, but for AI training. It was Weights and Biases. I remember writing all these different
*  companies. There's Replicate.com, which does inference. There's all these various infrastructure
*  companies and then there's the foundation model companies and so on and so forth. Image generation,
*  everything. I remember getting to this end part where I wrote, I was like, okay, all these things
*  are kind of filled. Not all these things are very interesting to me. I would rather, if I were to
*  work on anything, I'd want to work on actual research. That's the most interesting part to me.
*  It's hard, hard-won stuff and true invention. I remember getting to prompt, who's doing anything
*  with prompts? It was a very silly idea at the moment, but one thing I had remembered was I had
*  played a lot around with OpenAI's Playground Editor and the UI just kept getting more complicated,
*  more and more sophisticated. It went from, I remember two years ago, it was just a text box,
*  basically. Now on the right side, you have this pane and it had all these sliders and things you
*  could mess with, different models. They even had this way where you could insert text and then it
*  would fill in the text surrounding the text. I was like, holy shit, this is turning into a product
*  that they can't even maintain. It went from a demo area, just mess around, so that you go and
*  use their API. It turned into this crazy product. Then there's Jasper, which has also made a whole
*  UI around the API just for content marketing. You could just tell that there's all this
*  craziness going on with the prompt thing. The prompt itself needed a product just to play with
*  it. I had this moment of, other than Jasper, there doesn't seem like there was anything at that time.
*  I wasn't sure what to do. It seemed like there were these two areas you could make this really
*  complicated prompt editor, chain prompts together. It turned out I was like, hmm, I don't know what
*  that would become. That doesn't make sense. If it was really big, I should just do it.
*  Then there was this other thing that was happening, which is I think that stable diffusion dropped.
*  I had gotten a preview from E-mod a week or two before it dropped. I think I got the weights.
*  I could mess around in a notebook. Then that thing happened. There was Dolly, stable diffusion,
*  and then the prompts were very interesting there, very intricate.
*  It just dawned on me that actually what we don't want is a text box. What we really want are
*  really great UI controls to mess around with these things to get really good results.
*  And because I felt like this thing that was about to happen with text with GPT-3,
*  that complicated UI, I felt very strongly that that was absolutely going to happen with images.
*  It didn't make sense to me that we'd live in a command line mode forever with images.
*  I think that just completely clicked and then you could totally see how
*  the product could evolve from there. So far, that's been true.
*  If you were to imagine Playground in say two years, what is it that you hope to create for people?
*  We do have a pretty clear plan actually for what we want to do with Playground,
*  but I can give you the midterm. So right now what we want to do is we want to combine great AI
*  research and product design to invent a new kind of creative tool. We're not trying to replace
*  Photoshop or Illustrator. You could think of this new creative tool as something that could have
*  been, it could be its own tool in the Adobe Creative Suite. That's probably our starting point.
*  We suspect that there is something new there. One thing that's really different than say
*  the products that are within the Adobe Creative Suite is we're not really targeting the users of
*  Adobe Photoshop or Illustrator. Those users already have great skills. They already know
*  how to use these tools. There's plenty of tutorials and content for them to do it.
*  They can get really fine grain results. What we want to do is try to target all the people
*  maybe don't have those skills actually. If you wanted to change the color,
*  if you wanted to add a necklace to a woman, you could do that. It could be this really subtle
*  change. As long as you had good taste or whatnot, then you could be really happy with the result.
*  Other people could be happy with the result. Probably the midterm goal right now is just
*  making a really fantastic creative tool. Right now I think Playground for the most part is a toy.
*  We're like this glorified image generator, write some text, get an image. One of the problems with
*  that is that you can't really make subtle changes. You don't have a lot of control. It's a lot like
*  a loot box. You just type some words in, get an image. It sure would be nice if we can start to
*  have more control, have more subtle edits, and have more creative control over these things.
*  It's not just like a prompt. I think that would be our midterm goal. Just an extremely strong
*  AI-first creative tool that lets you make any image that you can imagine. Then you can use
*  text or you can use controls, UI controls, just like any other tool. Talk about the long-term
*  goal as well. Paint the vision for us. I think that what we want to try to do is we're trying
*  to go after the domain and modality of pixels. There's a whole bunch of companies right now
*  that are going after language. So many companies are going after language.
*  I think that you could probably think what we're trying to do is we're trying to make
*  a large language image model. I don't know if there's a word for this. I don't know. I'm
*  just going to make one up. We're trying to make like a LLIM or something. Basically, our goal is
*  to make something that a skilled person could accomplish with Photoshop or Illustrator.
*  But with our products, that would be the midterm. The long-term would be something that can edit
*  create, edit, and understand pixels. For instance, imagine I were to take your face, Eric,
*  and I could put you in this amazing scene in the matrix with a red trench coat jacket.
*  Then we'd want an instruction that could say, hey, can you change that jacket to black?
*  By the way, I actually like the gun to be held in his left hand, not his right hand.
*  So that'd be an example of creating something from thin air, but then also instructing it to
*  make it highly editable, to make even the subtlest change, but still capturing the
*  essence of everything that you want it to be like. Then understanding could be something like,
*  imagine there was a video and there's 30 seconds of a video. It sure would be nice to make some
*  kind of large language image model that could understand maybe 30 seconds of the video lapse
*  could be described what happened. Can we say everything that occurred in that video
*  and summarize it, for instance? I think the long-term plan is just kind of really be focused on
*  pixels, pixel space. In time, hopefully we could do things with 3D if and when there's a market
*  there. Definitely video, but really anything with pixels is really exciting to us. For the most part
*  right now, we're just building an AI research team, building little blocks. I think a lot of
*  those little blocks that we do, that we research, like little tiny models that do really incredible
*  things in turn will help us go and build the really great large language image model. I think
*  this year we should have our version of what would be maybe a GPT-2 for pixels, something like that.
*  Fascinating. We're going to get into the weeds of Playground, but first I want to ask a higher
*  level question, which is the controversy. This is very new for people. I remember you had a
*  couple threads early on just kind of introducing your work, talking about it. They went viral
*  on Twitter. Some communities found them and got really scared. Other people with other friends
*  who've created AI-generated art, some people got really excited about it. Some people got really
*  mad about it. What's either surprised you about it or how have we seen that even evolve just in
*  the past few months as people have gotten more used to it or more even hip to this thing is
*  happening? How do you see that playing out? I think around October I got canceled by the art
*  community for saying something that I didn't actually think was controversial. I didn't know
*  at the moment. All I said was, wow, I really believe that AI art is art. Then I showed some
*  images of stuff that I had made that I just thought was really cool and amazing. I hate to
*  say the art community because I do think AI art is art, but the non-AI art community subgenre
*  was really upset with this. I ended up getting super canceled for a week on Reddit and Twitter.
*  I didn't even find the Reddit post until a month later. I was like, oh, I got canceled on Reddit.
*  I didn't know. That's how you know you're really canceled. You can't even find all the
*  information. I'm just kidding. Yeah, I guess they blocked out my name and then no one told me. Then
*  I found it later. I just thought that was so interesting. I think that first, of course,
*  internally you feel a little defensive and whatnot. I think there are a lot of people
*  that are really, really defensive about this on the AI art side. They obviously feel like artists.
*  We interact with them every day. They definitely feel like artists. Weird things are already
*  happening now where we have the AI art people signing their name on their images when they
*  put it on Playground. We see these little signatures from some of our top users. They're
*  really, really good and people don't know how to replicate anything that they're doing. I think
*  then people not being able to easily reproduce their work is a good sign of what's coming.
*  If anything, we're making a tool that's going to make that harder. It's not just going to be like
*  a tiger by Greg Rokowski. Anyone can make that and they're just quote,
*  stealing Greg Rokowski's work. I think that whole thing is going to go away.
*  But the controversy was really interesting because I definitely got all kinds of weird
*  things like death threats and mean insults. But there were occasional people, there was an
*  occasional bright light where eventually I went from defensive feeling to I decided to be more
*  curious and I started talking to some of these users that are really upset. At least the ones
*  that could be, you could have more of a constructive conversation. I don't think that either side is
*  going to be convinced of one another. I don't think anyone is looking to convince the other
*  ones. But I did have a conversation and I do think that for the most part, people just feel
*  really threatened. They feel really, really threatened. There is this thing that they really
*  love and they're passionate about and now there's this other thing that comes along and basically
*  just makes what they feel like they love and do that they sometimes can barely make any money from.
*  It just makes what they're doing, it makes them feel like it's all obsolete.
*  And the tech audience, the tech focused audience is not really sensitive to this. The tech audience
*  loves this kind of thing. They're like, great, we've made software that can automate all these
*  things that we don't need. We love that as programmers. Automation is great. But on the
*  art creative side, this is very threatening and very not exciting. And I just had this back and
*  forth with this user and I said, hey, maybe you can find ways to incorporate this in your workflow.
*  You could probably get an advantage because you know how to draw and you have more skills
*  and expertise that's adaptable. And so I think that's going to be true for some audiences.
*  There are just some people that just have this love for drawing with a pencil and a piece of
*  software is never going to change that for them and it would be not fun for them. But I also think
*  that a software tool isn't going to replace that anytime soon. The joy of drawing and the people
*  that like you having manually drawn something is really great. It reminds me of listening to
*  an artist on Spotify and then there's going to the concert. Going to the concert is definitely
*  worse audio, but you go because there's this concert and it's fun and it's exciting and there's
*  this touch to it. And I just don't think these things are going to get replaced. I really believe
*  that human plus machine is like the best end result, at least for art. Art is for us, it's for humans.
*  Is it the right mental model to say that this advancement is going to make the best artists
*  even more economically valuable? It's going to empower them. It's going to make non-artists,
*  it's going to give them artistic capabilities. And for some middling artists, it's going to hurt
*  their economic prospect. How would you edit that summary of the mental model? What do you expect?
*  I produce music, so I think a lot about this in terms of the analogy of music. There was a time
*  when people made music and the way you made music was you had to learn the instrument.
*  And then along came the drum machine and it was cheap, cheaper, and you could sample inside of it
*  and you could get an eight bar loop. And the result of that was like one of the best results
*  of that in my opinion, my personal opinion, was that we got amazing hip hop. We changed music.
*  You could still be in a band and you could still make the same music you made 20 years ago,
*  but then we got hip hop. That was awesome. Some of the biggest artists in the world were influenced
*  people that had those drum machines. And then we went from the drum machine to we had real computers
*  and then you had digital audio workstations, DAWs, like Ableton and 3D loops and stuff like that,
*  whatever logic, whatever people use. I use Ableton. And then we could get entire symphony in
*  our computer. Then we could make sounds that nobody could make, even someone that had an
*  instrument. There were no instruments. The computer was now a customized instrument for every kind of
*  sound. And so now you get people, artists like Skrillex, that make sounds that you just couldn't
*  even imagine. And the reason I bring up that analogy is because I think that happens,
*  that constantly happens with any kind of art. Not just like pixel based art. It's that the art
*  changes and it evolves and new possibilities occur. And so I think what's going to happen
*  is that we're going to see something completely new. We're not going to just see like impressionist
*  paintings from a hundred years ago. We're going to see like amazing, we're going to see whatever
*  the Skrillex of pixels in art is going to be. Something we couldn't have previously imagined.
*  And it's going to be so cool. I don't know that I can tell you because I can't even imagine it
*  yet. So my feeling about this is that there's still going to be people in bands playing guitars,
*  still going to be people on their drum machine. Like Mike Dean is this famous producer, but he
*  like doesn't like all this like synth stuff anymore. He's got his own vintage feeling. He's
*  made like all kinds of tracks behind Kanye. And then you're going to see these new artists,
*  these new age artists that just blow us away. I don't know. Art represents a lot of culture
*  and it's going to represent an old time and a new time. So part of what is obviously,
*  I think unnerving people a little bit is just the speed with which all this is happening.
*  You mentioned Dolly 2, just to briefly revisit the timeline was like April last year. So that's
*  only nine months ago. And then stable diffusion. I don't have the date at my fingertips, but I
*  think that's still at most like six months ago. And now you are operating in a space that is
*  changing by the week. And you've said on Twitter a bunch of times every week there's a breakthrough.
*  So I'd love to hear from the recent past, then approaching your midterm vision.
*  How do you think about what published research out there is like worth your time? Which ones you want
*  to grab and work into the product ASAP? The recent edit launch that you guys did, which I think is
*  super interesting, seems to be a great example of that. And obviously you're building on top of that.
*  You mentioned your own research. I'd love to hear how your research in-house relates to
*  foundation models more generally and kind of how you see yourself both like writing,
*  staying ahead of that wave, contributing to that wave. There's a lot going on at once. And
*  that's been a challenge for me as an AI product builder. I want to hear how you are approaching it.
*  Yeah, I mean, we definitely stay on top of reading the research papers. So I think that's the first
*  area where we are able to kind of stay on the cutting edge. Like at our company, we do weekly
*  paper reads almost, where we go as a team and we read papers and try to understand them.
*  I think the next step down from that is, obviously people are dropping models. I mean,
*  this is definitely a bigger, it's kind of like a worrisome fear that I think a lot of people have
*  and calls into question what the defensibility of some of these companies look like,
*  these AI companies look like, which is you could spend a couple of months on like training a model
*  and then someone just like drops the weights for the model. And for real, I don't know what weights
*  are. There's like encoded numbers that represent the model that allow the model to get you like
*  amazing results. That's how you get from text to an image. And so yeah, there's definitely this fear
*  of like, well, you know, are we working on something that is already being worked on that
*  will probably be open sourced and then therefore be kind of like this commodity. I think that we
*  try to be as adaptable as possible as a startup. We put some bets in some areas. We're putting
*  some bets in areas that we think are really valuable, probably not being worked on.
*  And then we play some bets on, and then sometimes when the model drops or something like that,
*  in this case, I want to give a shout out to Timothy Brooks and Alexia, I think there's
*  one other author, I don't remember their name, but they were the ones, they were the researchers that
*  did instruct picks to picks, which ended up being our edit feature. We did some customization with
*  that to make it better than what they originally dropped. But sometimes, yeah, they dropped their
*  paper or not. So the paper had been out, we had read it, we were going to train a model. We were
*  already on track to like basically building it because we didn't know when or if they were going
*  to really drop the weights. And then they dropped it on Thursday, on a Thursday. So I guess that was
*  like two weeks ago, Thursday. And then as soon as that hit, we were just like, we dropped everything.
*  Because we knew we had a very clear plan on the fact that we wanted more of an instructable
*  AI model that can make subtle edits. We didn't know how good it could be yet, until we played
*  with it. And we played with it very quickly. And we're like, yep, it's amazing. And so we just put
*  the whole team together and we worked on a Sunday, launched on Monday at 2pm. That was like the
*  deadline. No matter what we had, we were going to ship it. And so I think you have to do both.
*  I think you have to make big investments. And I think you have to be adaptable. I think you
*  have to do this if you're a product focused company first. I think if you're one of the big
*  foundation model companies that have raised hundreds of millions of dollars or billions,
*  and you're trying to build something from scratch, then you have more leeway because
*  you're not exactly in that same rat race. Although you are. These days you are. The pace is
*  relentless. I'm sure GPT-4 is right around the corner. So I'm sure that scares people
*  that are competing in that realm. So I think we're following what our users want. We know
*  what all of our users want. And so when we see something that's valuable, we will just work on
*  it as fast as possible. Yeah, that's awesome. The speed of a Thursday weight drop to a Monday
*  launch, I think, is a great illustration of not only just how fast you guys are able to work,
*  but how fast you feel like you have to work to stay ahead of the rest of the market because it's
*  all happening so fast. Talk a little bit about the things that you plan to do over the next,
*  say, year or two. We chatted a little bit offline about placing text in images, and that's still
*  something I think we've only seen, to my knowledge, in a couple of papers that have not published the
*  weights. You said that that's a big challenge, but a goal. So tell us a little bit about that
*  challenge and maybe a couple other challenges that you have on the horizon that you're investing in
*  solving. For the most part, I think you should expect that we're only going to give users more
*  and more control over the kinds of creations that they make. In my opinion, this sort of era,
*  at least for the perspective of images, image creation, I think prompts are going to be less
*  and less valuable in time, I hope. I agree with Ilya, who's one of the co-founders at OpenAI,
*  that to a degree, prompts are mostly like a bug. You have to write paragraphs of text to get
*  world-class images, and that's a shame. It's just total experimentation.
*  I would love to invent something. There's like a wissy wig, which is like,
*  what you see is what you get, but I would really like to do what you think is what you get.
*  I think in our case, I just really think that if you see an image and you want to make a very subtle
*  change or edit, or you see a style that you really love in the world, and you want to try to replicate
*  that onto your image in some very small way, as long as you can imagine it, I'd like to be able
*  to produce that for you. So I think we're going to invest very heavily in a really great user
*  experience for a creative pro tool. It should be on the level of something like Figma. It should
*  be collaborative. It should be really rich and powerful. We want to give people all the bells
*  and whistles. We don't want it to just be a box, and then that's it. You have no control over
*  anything. If there are knobs and sliders and things that we can offer people to have this
*  perfect fine-gain control, we want to do that. Yeah, with things like text, right now it looks
*  like there's maybe a model called Deployed, and it's not out yet by the stability folks.
*  It's really cool. They clearly found a way to do text. It seems like it might be based off of
*  Google's Hardy image model or something. I think that we'd like to go a step further.
*  One example of something that I think would be really amazing is an AI model that can actually
*  invent forms of topography, not just write aerial font on a white background sign that
*  Aveya is holding. It'd be really interesting if you could write anything you wanted, but
*  the composition was taken care of, and it invented fonts, fonts that didn't exist. Why are we
*  constrained to the finite space of fonts in Google Docs or whatever? We should be able to invent.
*  I want it to be kind of curly, and I want the kerning to look like this, and I want it to be
*  kind of like this, and I want it to be red, and I want it to have this amazing neon hue.
*  I remember learning Photoshop as a kid, and I used to make logos and stuff, and I remember
*  learning all the little intricacies of making really cool fonts or logos. It'd be just really
*  interesting if we could synthesize fonts. That would be very disruptive, I think, to the world.
*  It's better to apply taste. In music, there's this thing that's like, if it sounds good, it is good.
*  I feel like with pixels, if it looks good, it is good. It'd be really cool if there was a way to
*  do that with fonts and backgrounds and landscapes and patterns and blending images. We just really
*  want people to feel as creative as possible. I think you can imagine that kind of like a really
*  amazing Canvas Editor ProTool type thing. Yeah, that's awesome. I always remember this
*  scene from The Simpsons from years ago where Mr. Burns is at some sort of museum for an unveiling
*  of a new art exhibit, and they pull the curtain, and he gets to see it, and he says,
*  well, I'm no art critic, but I know what I hate. I feel like that's kind of the vibe that you're
*  going for here where if it looks good, it is good, and people can make that judgment sub-second,
*  probably a lot of times. We know this. We know this with Apple products. I feel like Apple is
*  the greatest institution in the world that has proven that users know what good design looks like,
*  feels like. They can tell the difference. They can really discern the difference when the details all
*  square up correctly. I think humanity is quite good at discerning it. Something you said that caught
*  my ear was, I believe you said, what you think is what you get. I want to hear your take on the
*  concept of latent space. I find that that's a phrase that gets bandied around a lot, and I
*  kind of think that everybody has a different either visualization or mental model of what
*  latent space is, how you navigate it. How do you conceive of that? What's the latent space in your
*  brain? All latent space means to me is that a latent is just like a lower dimensionality
*  representation of an image. Images have RGB, and so that's a lot of numbers and values. Can
*  you represent that image into a more encoded, compressed lower dimensional space? From there,
*  it's just like you can just imagine a 3D graph of X, Y, and Z, and then there's a dot somewhere in
*  that 3D graph, and then there's just the clustering of possible images from there.
*  One of my favorite examples probably that I got from just learning about stuff, I think probably
*  learning from some other AI researcher that did tutorials and stuff, is if you have the word
*  tiger or something, and then you want it to turn the tiger into a Van Gogh painting, there's some
*  vector where you're pushing the tiger towards the area of Van Gogh paintings in that space.
*  You can just imagine, this is really hard to do in 2D, let alone audio, but yeah,
*  you just like this, you can imagine an arrow, and the arrow is pointing to where all the Van Gogh
*  paintings might be in this three-dimensional space, and so that's how you get to a Van Gogh looking
*  tiger. That's how I represent it in my head, and it's just lower dimensionality, so obviously
*  it's not going to represent everything, but it should represent a lot of things.
*  Yeah, thank you, that's fascinating. I'm really going to be very intrigued to see.
*  Is there a more colloquial version of this?
*  Well, I don't think even the reduction in dimensionality is necessarily something that
*  people are thinking about when they think about it. I don't know what, I really don't know,
*  like this is a very exploratory question for me, for us to try to get at how different people
*  think about this, but I sort of envision it almost like, I kind of think of it as like Sam Harris'
*  moral landscape a little bit, where you've got all these different local maxima and minima,
*  it's just such a crazy unknown topology that things that I think could be nearby in the latent
*  space representation may in fact be quite different when it comes to that if it looks good,
*  it is good sort of thing. Certainly, I see that in the product, right? I'll give you the exact same
*  prompt and we'll vary the seed, and I'll get things that are not at all what I had in mind,
*  and then I'll get something that's like, quite very much what I had in mind, and it seems like
*  there is some weird, there's some sort of extra quality dimension that is not fully represented
*  in that latent space, right? Because those things are clearly clustered together in some
*  semantic sense, they're local to each other in some sense, but yet they come out visually looking
*  extremely different, and I like one and I hate the other. What is the nature of that space where
*  such a small perturbation in the input can lead to such totally different outputs? I don't feel
*  like I have a great intuition for that, and I'm trying hard to build it up.
*  Yeah, all that a latent is, it's just a lower dimensionality of an image. So if you just
*  imagine 512 by 512 image and then RGB, so then it's just basically 512 times 512 times 3,
*  and those are all the possible dimensions of that image. And all a latent space, all a latent is,
*  is something that's more compressed, something that's a smaller number of values. That's a
*  latent. And the reason why you compress it is because we don't have infinite GPU compute,
*  or we don't have infinite time. And so you compress everything down to something that's like,
*  you know, actually, I only really want this to be, I only want to represent this as like a 64 by 64,
*  but instead of 3, I want to represent it as like 100. And that, I haven't done the math in my head,
*  but that might be like, that's lower, that's like a smaller number, set of numbers than 512 by 512
*  times 3. It's just smaller. And so you believe that like, okay, well, I'm not encoding everything
*  about the image, so I might lose some information. But it's not different than like encoding and
*  compression. So you might, you might get like lossiness, like a JPEG is like a lossy image.
*  You can think of it as like, maybe like latent space is almost like a JPEG. Or latent is like
*  a JPEG is maybe like the easiest way, maybe the easiest analogy. And it's latent space
*  is just where that dimensional vector, that dimensional value is in this very, very high
*  dimensional space. As humans, we can only perceive it as like 3D. It's obviously way more
*  number of dimensions than that. And so that's why like, the smallest change in like even your
*  seed value can get like something crazy. You know, it's suddenly it's like red hair instead of green
*  hair, but you know, that they kind of like the essence of what you're going for is still sort
*  of there. Like the style, for instance, is like if you want to like watercolor and use the word
*  watercolor painting, you still get like a watercolor painting, but like, you know, the hair is changed.
*  Because it's still super high dimensional space. But, but it's not it's obviously not like
*  doesn't represent everything. Anyway, I hope hope maybe that's helped.
*  I love it. It's great. You know, we'll see what our what resonates most with our audience over
*  time, obviously, but yeah, well, there's always a funny meme, like there's like the meme of like,
*  you know, obviously, people use these image generation things to make, to make like amazing
*  close up portraits of like women. And so there's like this meme of like people like searching for
*  their girlfriend in late space, which is, you know, definitely, it's a valid it's a valid meme,
*  actually, for truthful meme. Yeah, there was a really fascinating recent article by a guy who
*  used character AI. And on character AI, you can create your own, you know, characters with just
*  a couple sentences. So this guy who was pretty knowledgeable about language models going in,
*  and felt like you know, this wasn't a risky behavior for him to engage in,
*  asked character AI to conjure up, I believe he said an AGI designed to provide the ultimate GFE.
*  And next thing you know, he's starting to fall in love with this thing in kind of a weird way. And,
*  you know, he's got these kind of competing ideas where he's like, I know, on one hand, like even
*  how this technology works, but then I'm also like feeling these feelings. And you know, he starts to
*  kind of justify to himself, like, why it's actually, you know, real, and like, what is reality anyway,
*  and like, she's not really any less real than me, you know. And then at some point, he like pulled
*  himself out of it. But fascinating exploration of the latent space there, for sure, highly
*  recommend that we can maybe things are going to be crazy next year. So a couple maybe just kind of
*  rapid fire questions, then we can zoom out and talk a little bit of big picture stuff toward the
*  end. But I was kind of struck by a couple bits of the product itself. And you know, I see kind of,
*  obviously want to hear how you see it, but I see a lot of relevance, potentially from your experience
*  to what you're doing now. So from like, mighty, obviously, you're scaling compute in the cloud.
*  Now, you know, scaling these image generations in the cloud seems like there would probably be some
*  significant overlap there. How has your compute scaling experience translated to playground? How
*  big of a deal is that in this work? I think cost is really important. Right now, I think a lot of
*  people are not super excited about image generation because, or at least running it as like a business,
*  because the costs are quite high, margins are kind of thin. So there's kind of this like general
*  concern of like, how do you make this thing a real business? One skill that we got from mighty that
*  is replicable in this situation is we're really good at buying hardware, locating it in a facility,
*  managing that infrastructure. And it's kind of crazy. Like I wouldn't, I wouldn't, it wouldn't
*  be the thing I would jump to if I started playground. That maybe be like, one day, we'll do
*  that, you know, but because we have a couple million dollars worth of machines lying around,
*  and we've already done it all, you know, it's quite easy for us. We know we have all the
*  relationships with suppliers, vendors, and everything. So yeah, I think I mentioned that,
*  yeah, we're like about to go buy like a couple hundred GPUs, do make an order for that. We're
*  just like testing one small benchmark, but we're about to make that order maybe this week or next
*  week. I think that just gives us like a pretty big advantage around like owning everything from
*  like the hardware all the way to the end product. And it allows us to be really aggressive about
*  performance and latency costs. And that just gives us like other advantages. They're just all these
*  big tailwinds from GPUs. And, you know, for instance, like we can do things where like we can buy
*  the most cutting edge hardware, we can even get it before it even hits some of the suppliers.
*  Because of our relationships and outfit a lot of our servers with them. So I think that like that's
*  really cool, really interesting. Yeah, that's fascinating. And I mean, you said that kind of
*  gives you some other advantages. I am going to take a guess you tell me if I'm right or wrong,
*  that one of those advantages is seems like you guys are pretty free plan focused, like I'm not
*  getting pushed to buy. And I imagine that is kind of part of a bigger strategy to try to scale
*  the feedback that you're collecting. And I was kind of noticing also, like, you guys are not
*  that pushy on the feedback. Like it's you have the three point scale, like, you know, good, bad,
*  neutral, and you don't force me to do it. I was kind of wondering how you came to that. And if
*  that's still a work in progress, like a couple ideas that I had were like, what if you generated
*  two images each time and had people choose? Like, would that be a, you know, viable way to kind of
*  trade off some of your costs, especially where you have an advantage there for, you know,
*  potentially more scalable feedback? Unpack that however you will. Yeah, we're very, very, very,
*  we try to be as generous as we can on the free tier. Part of the reason why is because I think
*  that the best is yet to come. I don't think we need to be like overly aggressive about image
*  generation. I also think that like, I had learned this mistake from mixed panel, but like whenever
*  you make pricing usage based usage doesn't always correlate with value. If I make 50 images,
*  did I get a linear improvement? Did I get like a linear benefit? Did I get like 50 units of benefit?
*  No, sometimes I got to generate 50 images to get one good image, right? Sometimes I do 100 images
*  to get one good image. I mean, learn this from mixed panel because we used to like collect data
*  points. But like, what's the difference between collecting 100 million things versus a billion?
*  I mean, 100 million is a pretty big sample. So you're gonna get the same number of insights.
*  This is the same thing. It's not like 50 generations of an image gets you 50 better.
*  You get 50 images that you can now use. So I definitely just don't think image generation
*  correlates strongly with value. That's one thing. And it'd be like if you went into Photoshop,
*  and every time you made a stroke, like you'd be like, Okay, well, you got charged for that.
*  That would be kind of crazy. And so that's one thing. The second thing is you're right.
*  We definitely do care about like data labeling, acquisition, ratings. Yeah, we're not too pushy
*  about it. I think the reason why is because we already get a lot of ratings. And I think our
*  bigger problem is probably not acquiring more ratings at the moment. Our bigger problem is
*  trying to figure out how to denoise the ratings to get better signal. Yeah, because like people
*  certainly will go rate their input. Like there's some people that will just rate like any image
*  that they made as something they loved. And so that's like not very helpful.
*  So there's a real question around like, how do we denoise this data before we go and ask more of
*  the collection of it? I definitely think like, probably asking users, Hey, do you think this
*  image or this image is better of these two images? That's definitely a good idea, let alone like,
*  you know, you have these four images, which one's which one's good. So I think we just are kind of
*  like awashed right now with data. So that's probably one reason why it's not too important.
*  And yeah, I mean, we're also collecting other kinds of data, just may not be very obvious to
*  people what kind of information we're collecting. And it's not like PII data or anything. It's like
*  kind of how they're interacting with a product to help us create in events, new kinds of models
*  that they'll probably love. But yeah, so I think I think the overall strategy is pretty much just
*  like have a great generous free tier. It just helps us acquire users to help us acquire I mean,
*  I think the best companies will do a good job with the following, which is you make a good or
*  okay product that happens to get you a lot of users, which then helps you get lots of interesting
*  first party training data, which then lets eases the complexity of engineering for your AI researchers
*  to create new kinds of models, which helps you create new kinds of features, which makes you go
*  from like an okay, great product to like an amazing product. And I think the company that succeeds at
*  getting that flywheel to spin as rapidly as possible will be some of the biggest companies
*  in the world. You know, we're not the only ones doing this, like you could go to like chat GPT.
*  And I think you can like say with like one of the answers to the conversation or not. So like,
*  they're already generating one of the biggest data sets ever. I mean, it's like probably on the
*  order of billions now. So it's like, crazy. I don't know how you're going to keep up like
*  you even if you launched your version of chat GPT, it probably never be as exciting because
*  everyone would be over it. So now it's like, how do you go and collect the data? That's part of
*  the reason why we also sprint so fast on things. I was going to ask a kind of question downstream
*  of mixed panel as well. And you sort of alluded to it. But can you tell us any more about kind of
*  the role that like a B style testing plays in your product development process today? And
*  you know, how is that still like, you know, cannon for you as part of the product process?
*  I was actually never really that excited about AB testing. We never it was never like a super
*  exciting thing at mixed panel. One reason is, is because people often don't like when you do an
*  AB test, you have to like make an AB test. That's not a subtle change. Usually, sometimes subtle
*  changes work. Often they don't have to like make very big changes to see like real differences in
*  AB tests. Because otherwise, otherwise you need a lot more data to see the true conversion difference.
*  No, I mean, I just mostly check, I mostly just track vitals, like how many daily active users
*  we have, I probably look at like a dash, I'm still pretty data crazy. So I probably have like a
*  dashboard. I have two dashboards with like 16 metrics each. And it's like just my daily like
*  routine. It's like getting coffee, I go and look at the dashboard, I'm like, great, everything is
*  going the way I expect or, you know, whatever, hopefully all the numbers aren't crashing all of
*  a sudden, which would probably mean like there's a deep problem in the product. And you know,
*  it's like you live by your numbers to an extent. But I have often I always I always observe with
*  companies that the ones that were overly data driven also missed on something, they miss like
*  the qualitative side of their business. Like, you know, I had a friend who used to say that,
*  you know, her metrics were like, really, really good. And, you know, users loved her product.
*  But then like, when you talk to her users, like friends of mine, like, I hate this thing. And so
*  we'd never be able to reconcile like this problem between the metrics and what people would say.
*  And I feel like that hid kind of some of the problems. So I go a lot more, it's kind of strange,
*  but I probably care a lot more about qualitative information than quantitative information,
*  the quantitative tells me was my intuition, my experiment correct. But it doesn't tell me what
*  to do. Yeah, it's like, am I going in the right direction? Probably. But it definitely doesn't
*  tell me like, what feature I should build or, you know, we don't run any A-B tests, actually,
*  just talk to users. Have there been any moments where you have opened up that dashboard and seen
*  something that did not look healthy? And you know, you realize like, no, we actually did take a step
*  in the wrong direction here and, you know, had to learn something in backtrack.
*  I mean, playgrounds only like four or five months old, I'm sure that will happen.
*  So I feel like, you know, it's, it's kind of funny, it's kind of harkens back to our conversation
*  around like when Dolly got released, and when stable diffusion got released, we all look back
*  and like, wait, it's been like four or five months. Shit. I don't think we've shipped,
*  we've shipped funny things. Like I think last week, we shipped something kind of funny, which was,
*  we didn't realize that one of our API endpoints was actually bottlenecking all the, like bottlenecked
*  on throughput of image generation. So when we made the API, like two times faster or something,
*  literally the amount, the quantity of image generated, images generated just like jumped to X.
*  Just surprised me. I mean, we obviously don't have all the monitoring and stuff we need set up,
*  because we're still really immature as a company, but it just was like, wow, if you give everyone,
*  if you stop timing out or having errors on our API, and then you just increase the overall
*  throughput, like the users just absorbed it instantly, it was kind of amazing to watch.
*  And that really taught me a lesson of being like, more thoughtful about like on monitoring metrics
*  of like GPU utilization and throughput. Obviously, we can't just keep buying GPUs, because we'll just
*  burn cash. But that was a really cool moment of like, man, they really, they will just absorb
*  anything we give them. Yeah. We'll just keep going. Fascinating. So just to repeat that back and make
*  sure I, and our listeners can understand it accurately. You found some bottleneck that
*  ultimately made things twice as fast, and you immediately saw a 2X jump in how many images are
*  generated. I mean, it might be more, it's still going up. So I don't even know where we'll end.
*  Yeah, it's still like, I would suggest a model of people kind of sitting down at their computer
*  with like a finite time to either like accomplish this or not. And they'll do as many generations
*  as they can fit into that window. Is that kind of how you think about how people are using it?
*  I mean, I just think like, it's, you know, it's definitely a distribution. You know,
*  the average user will do like 45 to 50 a day. But then like the hardcore power users,
*  they just blow pat, they'll just hit our limit very rapidly. Like we do, we give people 1000
*  free images to generate a day. And we picked 1000 because it was the 90th percentile when there
*  were no limits. And I mean, just to put this in perspective, like, you know, you go to like,
*  I won't I won't name names. But if you go to like any of these other image generation services,
*  they give you like 100 a month or something. And you have to buy credits 100 a month, we give 1000
*  a day. And you think like, who's sitting around just doing like 1000 images a day, and lots of
*  people turns out. And so I mean, I think those hardcore, intense users are just spend all day
*  on your product. I think that's like true of all kinds of great products in the world. You know,
*  people just use it, you like love it, and they play with it. You have people doing Twitch streams,
*  all kinds of crazy things. So it's really, it's really interesting. I mean, for some people,
*  they will tell us that they like cures, it makes them cures like their anxiety. We hear all kinds
*  of interesting things. I mean, obviously, people get obsessed about certain things sometimes.
*  But yeah, yeah, I mean, it just I mean, it was like an API for like our dream booth models. So
*  we have all these custom filters. And people love them. But we didn't realize that they were quite
*  like the they were returning like quite slowly. So our overall throughput was slow. And it just like,
*  yeah, very, very interesting. Yeah, that's fascinating. It is amazing. Sometimes the
*  surprises that you find in those user conversations, we're going to talk to the founder and CEO of
*  replica in a future podcast. And one of the things I heard her say about having built,
*  you know, a very primitive chatbot that I believe originally was just to support like an online
*  banking experience. This was back in Russia, she's from Russia. So you know, everything is new.
*  She builds this online banking chatbot assistant, you know, again, way before anything like GPT three.
*  And going into the field, you know, going into small towns in rural Russia, she talked to a
*  woman and this stuck with her and it stuck with me to just hearing her repeat it. She talked to this
*  woman who said, nobody cares for me like this. And she was like, Oh, my, you know, this is way
*  bigger than helping people, you know, with their online banking, you know, the need runs a lot
*  deeper. So interesting to hear, you know, kind of a similar thing there with helping people with
*  anxiety and all that kind of stuff. Yeah, we I almost like want to keep it almost limited,
*  because there's I always I sort of worry that it's like, people get too obsessed. Like, if we just
*  keep increasing the limit, like, you know, is that is that the behavior really want from humanity? I
*  don't know. Obviously, they can buy like if you buy our pro plan, you'll get like, two x more.
*  But I'm like, man, people are like hitting people are starting to hit our 1000 limit
*  more and more frequently than you know, even just a couple months ago. So I don't know,
*  we might have to increase it something or something. But there Yeah, there's kind of
*  this question of like, hmm, do we want this level of obsession? I don't know. Maybe it's not good.
*  Yeah, well, if it's any consolation, I think it's going to be a more urgent issue on the virtual
*  friend side, more broadly than it will be for the image creation side in the short term. So you'll
*  have some, you know, examples potentially to follow, you could chat with an image.
*  In time, you'll be able to just like look at an image, you look at any inanimate object and just
*  talk and talk to it. Like you can you can encapsulate like an image of anything like a chair,
*  like a really cool looking chair and be like, I would like to talk to you.
*  You'll be able to talk to it is totally doable. I don't know. I don't know anyone that's doing it.
*  But I think it's very possible. It's very I think it's probably trivial to do if the chat people
*  wanted to do it. Yeah, character AI is kind of is close to that if not already there. I mean,
*  their bots can they do generate images if you ask for that as part of the chat and you can create
*  a like or upload, I believe, like a profile photo for it. And I don't know if that feeds into its
*  personality in any way, I had kind of assumed it didn't. But maybe in fact, it does.
*  Well, like, like, so we know that like about a picture speaks 1000 words. And so like, if you
*  type in like, you know, you're like, like, for some words, like Benjamin Franklin, that's like
*  very clear, there's a bunch of data around Benjamin Franklin on the internet. But if you
*  wanted to do something like more esoteric, you have to like really describe the character, I wonder.
*  And that's like pretty low dimensionality, like the human, the English language doesn't actually
*  have that much dimensionality to it. Right. But if you take an image, an image has like incredible
*  dimensionality to it. Everything about the chair and the colors and like, I just would find that
*  really interesting. But I haven't seen anyone try it out. I'm excited to see someone try it out. Not
*  that we're going to build like a chat feature. We can talk to our images, but it'd be really
*  interesting as an as a as like an experiment. It's like a very like, early web vibes type
*  experiment, like something random that someone will do. Probably go viral.
*  Yeah, I think actually, that's a big part of my worldview right now is that all these different
*  things are developing at a pretty amazing clip, but it's largely all happening in parallel.
*  And, you know, I think we're going to obviously, you know, fully expect that we're going to continue
*  to see research breakthroughs and, you know, fundamental techniques advance. But even kind
*  of leaving that aside, it just seems like all these different things have not been really
*  productized. You're doing that. But, you know, as you said, it's only been a couple months.
*  They certainly haven't been like refined and fully hammered into shape, you know, for a general
*  public audience quite yet. And then maybe most importantly, they haven't been integrated. So,
*  you know, you've got all these little islands of like awesome AI functionality, but very few,
*  you know, even have the time to zoom out and kind of try to get a broad survey of that landscape,
*  let alone, you know, has any of the work started to integrate these things in,
*  you know, all the ways that will eventually happen. So I totally think you're onto something
*  there that like you generate an image, next thing you know, it's a character. And, you know, that
*  that kind of recombining, you know, call it ensembling, call it, you know, integrating,
*  I think that's going to be a huge driver of change over the next few years. And we're just
*  starting to see that. Yeah, I mean, I think I think there's going to be this moment that's going to,
*  I don't know if it will be an important moment, but I think there'll be this moment that's very
*  similar and akin to the internet mashups of Web 2.0, where people would like take Google Maps,
*  and they would combine it with Flickr and then Yelp. And then you get like this interesting,
*  weird app that's like the combination of these three services. You can totally do that with AI
*  models. You know, you can combine a playground image with like chat GPT, and then combine that
*  with like something else. And you get these like really intricate products as a result. And so I
*  think the age of like the AI internet mashup will come back. I think we're already starting
*  to see some of that. You know, there's like random hackers just like messing around making weird
*  things. The problem is, you don't know what will actually like stick and be big, important. I think
*  that a lot of people are going to start to move up towards making apps, because it's too complicated
*  and too expensive to like focus on core foundational AI research. It requires a lot.
*  It requires a lot more knowledge than just like taking the fast AI course, fortunately.
*  As someone who has done it, I still feel like I don't know a lot, done even more than just that.
*  And so I think that there's going to be a lot of applications, a lot of people experimenting.
*  It's kind of like that moment in mobile, where it was just a complete like Wild West gold rush,
*  and nobody had a clue what was going to work. And so just all like thousands,
*  10s of thousands of experiments occur simultaneously. And you end up getting things
*  like Uber and you know, whatnot. And some things like grow really rapidly and then fall because
*  they fall out of relevance, they didn't have good retention. And some things just have this incredible
*  lasting power, you know, for a decade. So it feels like that will happen again. And I don't know,
*  you just go to hugging face and look at models. And there's just like, thousands of them. And they
*  do all kinds of interesting things. And then, you know, a week later, there'll be like 10 more.
*  10 more like, you know, something called blip two came out yesterday. And it's really exciting to me,
*  it might be really boring to other people. But one of the demos they have for blip two was
*  that you could literally actually blip two had the had the thing that I just described, which was,
*  you could like, talk to the image. You could be like, you could have a picture of Obama being sad,
*  and you could be like, why is Obama sad? Just try to describe like, oh, you know, there's a thing
*  going on in the background. And you know, whatever. You're gonna be like, why is it sweating? Oh,
*  it was playing tennis and like, whatever. So in blip was like an amazing model to do image to
*  caption, which is really cool. And so it just I haven't even experimented with blip two and
*  its capabilities. So there's just so much that is happening. And the pace is so on is relentless.
*  And I don't think the blip two thing was very popular. But I think he is actually a big deal,
*  probably. Yeah, you're talking to the right person about for singing the praises of blip. It's
*  actually one of my favorite models at waymark, which is my company where we do much more structured
*  AI video creation. We work with like media companies, you know, for example, TV companies,
*  where the requirements are, you know, very rigid in terms of like, this must be a 30 second spot,
*  or it cannot air, you know, and it has to be 30 seconds to the frame. Or it just can't air,
*  right. So we have a lot more kind of scaffolding in place. And we're using AI to fill in that
*  scaffolding. But the scaffolding is all kind of pre constructed. blip has been hugely valuable
*  for us in terms of we actually use the image text matching portion to figure out out of a user's
*  images, which may be hundreds. Typically, these are, you know, small business advertisers, and
*  they've got often hundreds of images that are in our product. And now we're generating with language
*  models, a script that, you know, tries to tell their story, we kind of give them, you know,
*  little prompt opportunity to where they we can unpack that into a full script. And then what
*  images need to go with that? I've been on a, you know, quite a quest to find the best models for
*  solving that problem. blip remains number one. And so you just my afternoon just got filled in,
*  because blip two is going to be is going to be of high interest to me for sure.
*  Yeah, yeah, the pace is like that. Yeah, it's like you wake up in the morning, have this idea of what
*  you're going to do for the day, and then blip two drops, and you're like, I'm going to race the rest
*  of my day. Yeah, literally, I think that's just happening to me right now. So on the basic level,
*  you're relatively new to this, right? So you've jumped in to a super fast moving field and tried
*  to get to the edge of it as quickly as possible. I'd love to hear how you've done that, how you
*  would encourage others to do that. And then if you're comfortable sharing a little bit on like,
*  what is your kind of internal research agenda? You know, what kind of training strategies are
*  you pursuing? And again, I know, you know, you won't want to share all the details of that. But
*  as much as you're comfortable with, we'd love to hear. Yeah, I can't share the can't share
*  specifically the areas of research that we're working on just yet, or the techniques. But
*  yeah, I mean, I had been I had probably taken, you know, wide variety of like AI courses over
*  the last like six or seven years. So a lot of it has been a little bit of a catch up or re review.
*  But even that stuff was pretty shallow, I would say it's not anywhere as deep as I feel like I've
*  gone now. I think, you know, I think one way to kind of accelerate thing one way that I accelerated
*  things is I just found AI mentors and like kind of bartered with them. You know, I could barter
*  knowledge about startups or whatever they want in the world. And so I just had people that would
*  help me basically get unstuck. And that sort of keeps changing. Now I have a team so I don't need
*  it. My team's already better than me. So I don't really need AI mentors anymore. They're just like
*  team. And it's really I actually think the fastest way to learn is to build.
*  I really discourage people from binge watching YouTube videos of notable people doing AI courses.
*  I think that is a very that's a fine way to get a general sense of things and understand the industry
*  and be able to talk somewhat intelligently about it. But I don't think like maybe it's good for
*  like if you're just like an investor or something. But I think it's probably not the right way to go
*  if you want to actually do deeper research. You know, something greater than just like
*  calculating cosine similarity between beddings or something, you know, you want to do real
*  fundamental research, I think you need to like write code. My maybe faith, maybe I think the best
*  YouTube series, the best series that I could recommend to early people early on. I think
*  Caparties new series is really, really good. It didn't exist when I was starting like restarting
*  out last year, I was doing the fast AI course. I really recommend Caparties course because
*  he just has a style that's like, he's a very humble guy. And he goes through everything just
*  like from the basics, you just need Python, he's not doing anything fancy. And he just
*  builds everything up. It might not be the best way to learn if you prefer top down learning,
*  the fast AI course might get you more excited if you need to get more motivated. But those are the
*  two things I would do. I think probably the most valuable thing though, has been not working in
*  isolation. I think for a long time, I was just grinding through in isolation learning. But now
*  that I have kind of like a team with me, it's really nice to like get on a call for like an hour
*  and just talk to the research team about like some idea in my head, or get some explanation
*  of something or reading papers together. It feels a little bit like you're in class or like you're
*  in a study group. That's been really motivating. And then having a project in mind that really
*  is motivating helps you want to stay up till like two o'clock in the morning, just to get something
*  done or watch the end of a train run. So that's about as much as I could like advise at the moment.
*  Obviously, you guys already had with Mighty, a lot of hardcore engineering and you talked earlier
*  about co-locating your own servers and managing that on a level that most startups don't find to
*  be an attractive proposition. So you had deep skills and capabilities there already. What have
*  you found needed to change about your team? What were the skill sets that you were like,
*  this is what we have to go out and add to our team for us to be competitive in this space?
*  Yeah, unfortunately, when we pivoted from Mighty to Playground, we did have to let a whole bunch
*  of people go. And they all like, I think almost all of them really understood. I mean, it was
*  kind of like we had a band and if we went in, the band was fine for Mighty. But then if the,
*  if we moved everybody to Playground, it was like we had too many drummers on the band. So we were
*  kind of like, what do we do with that? And so, you know, we quickly figured out that we definitely
*  needed to make more space for a bigger AI research team. So we're actually still looking for like one
*  very senior AI researcher. We only have one slot left to fill. But yeah, I mean, we're kind of like
*  looking right now. I mean, it's kind of, I think it's good to have a good team mix, like people
*  that are like junior, people that are like very senior, people that are mid-level. I think it's
*  good to have that team mix because then, you know, it's not like your senior AI researchers
*  feel like they have to do something. Like you might have like a valuable thing you want people
*  to do as a company, but not everyone's excited to do it. So it's really good to have like a good
*  team mix of people who find different kinds of projects more interesting. That's one thing I do
*  for every, I do for all teams, not like something specific to AI research. The second thing is,
*  I asked Sam for some advice from OpenAI. I think back in like December, we had like a 30-minute
*  conversation, or I was just like, hey, can you teach me the pitfalls and things of like how to
*  run an AI research team? I don't know how to do this, probably going to do badly. Can you help me?
*  And I think, you know, I learned a lot of things. But one of the things I was very curious about was
*  to what extent you allow AI researchers to wander. Like I'm very like, let's ship things
*  as rapidly as possible. Let's, you know, clarify scope. Let's figure out what we need to build,
*  quality, move quickly. But AI research is like, you know, Sam basically was like, yeah,
*  stuff takes like 10 times longer than, you know, building a web app. And so I was really curious
*  how much do you allow people to kind of wander and meander because you might not get good results.
*  I think Greg Brockman also at OpenAI has like a tweet that I'll paraphrase. It's kind of like,
*  you know, at first things like don't work at all and they keep not working. And then eventually
*  it's like amazing. Something along those lines. He said it better than I'm saying it, but because
*  he had to write it in tweet. But I think that I think that I think that's right. I think that
*  we're experiencing that. We don't have a lot of data points as much as they do, but we tend to
*  let our researchers kind of wander. Probably not as much as OpenAI because OpenAI has like a really
*  broad remit, but we care about like pixels and creative tools. So there's obviously like these
*  guardrails, but for the most part, we're just, I don't know. It's like, you don't know that's the
*  reality of research and research is hard won. And so we're just like looking for wins, looking for
*  like treasure everywhere. Yeah. Zooming out a bit, earlier you were talking about how you
*  were exploring the idea maze. I'm curious if you were focused as a VC in the space, what would be
*  your mental model be for what kinds of companies, you know, will endure or should I look to invest
*  in verse which ones to perhaps stay away from? They might create some value, but they won't,
*  they won't capture it or be durable. Yeah. I have definitely been thinking about that.
*  Definitely talking, actually having conversations with other VCs or friends.
*  And one thing that I saw, I've gone to a number of AI dinners, you know, people,
*  people like, you know, the founders of like character mid journey or whoever. And then even
*  people like AI, just engineers that work at some of those companies, very helpful to get like
*  perspectives all over the place. And, you know, I would, we would kind of ask these questions of
*  like what matters here. And so there's a general consensus that we're going to, if we haven't
*  already, we're starting to run out of data that we can use from the public internet.
*  Like maybe by the end of the year, largely we'll have like saturated all of that. And
*  partly there's, I think, I think someone else said this, that a lot, there's still a lot of data.
*  It's just privately held. Like it's probably like exponentially growing in, in like a private
*  ecosystem, like mobile apps, but a lot of public data is like limited and not to mention like
*  copyright issues and stuff like that. It might be like a whole nother set of issues. So, you know,
*  I think the first thing is like having some advantage around data, I think is really critical.
*  It might not be a enduring advantage for like a decade, but surely can be a big advantage for like
*  many years. I think the second advantage is like, I think there's like a, I think there's
*  like a space where like you could probably make a really amazing product that happens to use AI
*  to build some kind of new consumer network effect. But we're not really seeing that yet.
*  Like we're still using kind of the old ways with consumer, but there's probably some,
*  some new tricks and it requires like a lot of experimentation as consumer does.
*  I don't know what that is, but like an example of like this not going well is AI avatars.
*  And it might not be a fad actually, if it were power, if it were plugged into something that had
*  a real distribution network and network effect. But so there's kind of this question of could we
*  have bootstrapped something into a network effect with some novel way of using AI to solve some
*  interesting problem for users. So I tend to look at like, I would find that really interesting.
*  I think that like, there's some problems with like some of the foundation model focus companies.
*  I think like the less generous thing I could say is that they're like making
*  APIs in search of a problem. And this approach of doing this might work fine if you are open AI
*  and you have billions of dollars and you can pursue like 10 experiments at once, 10, you know, 10, 50,
*  100 million dollar experiments at once. And maybe you'll land with a product that has product market
*  fit. Maybe that's chat GBT, I don't know. I don't know what those numbers look like. But
*  I think that it could be really tough to do that unless you're so well capitalized like open AI.
*  That approach is not maybe replicable. And you might have to do the basics. Like we're not
*  trying to replicate the open AI approach. We are making a product. We're trying to go from a product
*  down to a foundation model, not a foundation model to product. And we'll see if that works.
*  Yeah. And I think I so I think, you know, it's I think there's a lot of buzz around the idea that
*  there'll be mass will the large language models be commoditized? I think it's totally valid.
*  For a long time, I had that I had that view that like basically the LMS and everything will converge
*  there'll be commodities. Where's the real business in this thing? But the deeper I go in trying to do
*  research, the harder the more I realize how hard it is, how hard one it all is. And I am not I'm
*  not as confident about that anymore. Like maybe maybe over a very long time span, these things
*  will inevitably all technology becomes obsolete over a long time scale. But I don't think that
*  people I you know, I think people that just have a shallow sense of this research are underestimating
*  the complexity of how you build these models and how difficult it is. Sure, stable diffusion can
*  get trained for $600,000 on how many GPUs. But if you want to build something that endures and gets
*  better, that requires very concerted investment instead of resources, you cannot just raise 100
*  million dollars and say, boom, we've got a foundation model, you have to, you have to hire
*  AI researchers, like you have to find clever ideas is very hard. It's just like software in that way.
*  It's not like you can paralyze everything with with money. So, you know, I would just say, like,
*  I'm not so sure that it'll be as commoditized as people think. But I think certainly, like,
*  I think like the prior generation of the model, like, you know, like a GPT two or three,
*  it can be kind of like, every two years, the model will get commoditized. But the but the state of
*  the art model endures for those two years. That could be a world we live in. It's kind of like
*  a little like, it's pretty similar to like CPUs. And the thing is, is that what customers want is
*  the state of the art thing, they often don't want the, you know, nobody's nobody wants to use GPT
*  two. You want the best thing you can get because you have to compete with everybody. And your
*  competition is going to use the state of the art. And so then then there's kind of this argument
*  around fine tuning. But even that argument, I think is fairly weak, because a lot of the things
*  that you might fine tune today become not you don't even need to you, you could use the the new
*  state of the art LM model. And it can do what you previously could do with fine tuning, without
*  fine tuning. And so I think people don't fully internalize that the fine tuning thing is also
*  not as defensible. But if I were VC, you know, the other thing I would consider is like, if the
*  company has something that they can fine tune on that is private data, that could be really defensible.
*  So there are a couple like valid and valid things. But yeah, I think data real hard when AI research
*  network effects all those, all those things are largely like kind of the same from traditional
*  software still I think apply in this world. So you've got an 18 month old kid. What do you
*  think their life is going to look like when they are your age? What does 2050 look like in your mind?
*  Gosh, sometimes my wife and I have this conversation of like, what thing could occur in the future that
*  would make us feel uncomfortable, you know, like in our era. And I think like the answer to that
*  would be like, I think I've answered this as like, what if my son wanted to marry an AI or something?
*  And I'm like, I don't know how I would feel about it. I feel deeply uncomfortable, I think right now.
*  So yeah, I mean, I just, I just think like the most weird thing will just be like, you're,
*  my kid will be like friends with some AI robot thing, and he won't go outside, and he'll be really
*  obsessed with it. And we'll be like, shouldn't you get like real friends? And, you know, and it'll be
*  this like very, you know, it's like, it's like when my parents saw me on the internet all the time,
*  they must have just like, thought I was probably getting into trouble, which I was, and doing bad
*  things. And, you know, I just think that, you know, it's, it's just, it's crazy. It's just, you could,
*  you could just be, you could be, you could totally see kids just chatting with like some random AI
*  thing, it'd be like the most interesting conversation they've ever had. It's unlimited,
*  and it's always interested in you. And, you know, it's giving you like really cool insights to life.
*  And, I mean, I don't know, I mean, humans, humans have, don't have unlimited energy. So,
*  I don't know what if my son just like, maybe he maybe some of his friends, some of his best
*  friends will be AI things. And that'll be just so weird to me. He'll be like, you don't get it, dad.
*  Yeah, you don't get it. You know, this isn't real. And then there'll be something that's like more
*  advanced than the Turing test, you know, probably at that point, it'll be and he'll reference that.
*  It'll be like deeply philosophical. I mean, the other crazy thing could be
*  that I told some friends a couple weeks ago that it doesn't seem too far off that we'll have like,
*  the first like AI religion. And the crazy thing is that you can talk to your God, and your God
*  will give you answers. Yeah, so what if my son like joined, you know, some new religious AI
*  spaghetti monster religion, but you can talk to the spaghetti monster. And it could be like a
*  really positive thing for humanity, it could have good values and principles, but we would all just
*  be like, no, this isn't real, right? And then be like offensive. Anyway, that would be the other
*  weird thing. Yeah, I think that's a great place to wrap this podcast and aptly named the Cognitive
*  Revolution. So thanks so much for joining us today. Yeah, thank you for having me.

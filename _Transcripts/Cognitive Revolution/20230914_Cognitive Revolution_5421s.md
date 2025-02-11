---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 5421s
Video Keywords: []
Video Views: 466
Video Rating: None
---

# AI-Powered Filmmaking with Waymark's Stephen Parker and Josh Rubin
**Cognitive Revolution "How AI Changes Everything":** [September 14, 2023](https://www.youtube.com/watch?v=c1pPiGD7cBw)
*  This stuff, it was exceptionally hard,
*  maybe even harder than a traditional animation.
*  You're working with an unknown artist in the room
*  who can give you exactly what you want,
*  or who can give you some random wonderfulness,
*  or some, as other people say, grotesque image.
*  So it's a huge challenge.
*  In order for it to be good,
*  there needs to be, like, a big 500-foot human vision.
*  Hello, and welcome to the Cognitive Revolution,
*  where we interview visionary researchers,
*  entrepreneurs, and builders
*  working on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas,
*  and together, we'll build a picture
*  of how AI technology will transform work, life,
*  and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host, Eric Torenberg.
*  Hello, and welcome back to the Cognitive Revolution.
*  Today, I'm thrilled to be speaking
*  with my longtime friends and teammates,
*  Stephen Parker and Josh Rubin, creative leads at Waymark,
*  and creators of The Frost, a groundbreaking short film
*  made entirely with Dolly 2-generated imagery.
*  For a bit of context on the AI journey
*  that Stephen, Josh, and I have been on together,
*  from 2017 to 2021, Waymark had built the easiest-to-use
*  video creation app on the market,
*  and the quality of the video templates
*  that Stephen, Josh, and the creative team produced
*  was our standout feature.
*  However, feedback showed that users wanted more
*  than an easy-to-use DIY solution.
*  What they really wanted was an app
*  that could create content for them.
*  Now, I had been interested in AI forever
*  and was always looking for AI tools to enhance our product,
*  but I'd only done a tiny bit of hands-on development
*  because, frankly, none of the AI technology
*  available at the time really worked for our purposes.
*  That first started to change with OpenAI's release of GPT-3,
*  and in September 2021,
*  when we successfully fine-tuned the Curie model
*  for the first time,
*  I became convinced that generative AI was the solution.
*  Some on the team, I think, thought that I'd lost it
*  when I used my prerogative as CEO
*  to pause just about everything else we were doing,
*  up to and including board meetings,
*  to organize a generative AI 101 crash course for the team
*  and reorient our product roadmap entirely around generative AI.
*  Stephen and Josh, to their credit, came along for the ride
*  and have since caught the AI wave in their own unique way.
*  While I've got my 10,000 hours of AI usage
*  with a mix of language, computer vision,
*  and text-to-speech models,
*  Stephen and Josh have gone super deep on AI art.
*  We got first wave access to Dolly2
*  as an OpenAI innovation partner customer in early 2022,
*  and since then, Stephen has personally generated
*  over one million images with Dolly2.
*  The result? The Frost is not just a proof of concept,
*  but a legitimate 12-minute film with a coherent narrative
*  and a consistent aesthetic.
*  In this episode, we get a behind-the-scenes look
*  at their creative process,
*  a sense for the challenges they face
*  and the strategies they use to overcome them.
*  And overall, one of the most sophisticated accounts
*  of the current state of AI art that you'll hear anywhere
*  from a team using these tools
*  with the highest level of taste, vision, and skill.
*  Creating the Frost was not easy,
*  but this project does show how transformative generative AI
*  is likely to be as it continues to mature.
*  Only seven people are credited on this film.
*  Josh and Stephen, our Waymark team members,
*  Tommy Herman, Zach Poley, and Lexi Dietz,
*  and collaborators Matt Sessions and Robert McFalls.
*  As always, we appreciate your reviews and your online shares,
*  but this time, I really want to encourage you
*  to watch the film itself,
*  and also the trailer they've recently released for The Frost 2,
*  which they are already making
*  with an entirely new generation of AI tools.
*  We'll have links to these in the show notes
*  and also to some visual behind-the-scenes content
*  and an MIT Tech Review write-up of the film as well.
*  Now, please enjoy this fascinating conversation
*  with Stephen Parker and Josh Rubin,
*  AI creative pioneers and makers of The Frost.
*  Josh Rubin, Stephen Parker,
*  welcome to the Cognitive Revolution.
*  Thanks for having us.
*  Very excited to have you both.
*  Obviously, we've worked together for a long time at Waymark,
*  where you guys have led the creative department
*  and brought a level of creative quality
*  to the work that we do that was certainly previously inaccessible
*  to the likes of me.
*  So, very much appreciate that over the years.
*  But today, we're here to talk about your recent project,
*  which you've done at Waymark,
*  but kind of for broader exploratory and creative purposes,
*  and that is The Frost.
*  I guess, for starters, tell us, what is The Frost?
*  The Frost is a short film, 12 minutes, part one.
*  It is a film that we created using dolly images, essentially,
*  which are still images that we prompt for,
*  curate, and then take into After Effects,
*  cut up, use puppetry, various styles of animation,
*  run the images through DID,
*  do a whole bunch of things to essentially create video
*  from still imagery,
*  and then assemble a short film out of that new quasi-video.
*  I would say that Josh probably has more to say
*  about what The Frost is than me.
*  He is the director on the project.
*  But it's just fundamentally about the exploration
*  of what new AI can enable for creators.
*  Yeah, I mean, it was...
*  The Frost was kind of a happy, wonderful accident.
*  It was kind of born out of the curiosity
*  to see if we can make a film generated completely
*  out of AI imagery.
*  What I mean by film, it's more like,
*  not just like a montage of images set to music
*  and to see if we can animate them
*  and to get the images looking as best as possible.
*  I think there's a lot of people out there in the world
*  doing that, doing that well,
*  and doing that probably better than us.
*  What I mean by film is to create a narrative
*  out of AI-generated imagery.
*  Could it be possible? Is it possible?
*  We saw the text-to-image generations
*  as the beginning of AI cinema,
*  which is the beginning of this whole new revolution
*  in entertainment, really.
*  And we just saw the beginning of it.
*  And The Frost was kind of like an experiment put into action.
*  Yeah, and then three and a half months later,
*  and 13 minutes later, we had a narrative.
*  We kind of, for better or worse,
*  we achieved our goal.
*  So we're quite happy with it.
*  Yeah, it's been very well received.
*  I think it's been really interesting to see
*  how the sort of media has kind of taken an interest
*  in the project and what seems to capture people's attention most
*  is this kind of standard that you're speaking about, right?
*  Where you're...
*  You guys really set out to do something
*  that is not a proof of concept,
*  but instead saying, given these new tools,
*  can we create something that we as creators and filmmakers
*  would be proud of and that people would actually want to watch,
*  not as a pure AI curiosity,
*  but as something that hopefully stands up
*  against other entertainment on its merits, right?
*  I think that's a key difference in the way
*  that you guys approach this project
*  relative to so many things where people are like,
*  look what I kind of spit out, look what AI spit out for me.
*  There's a lot more...
*  I guess I don't really know a lot about your process
*  and I don't really, to be honest,
*  know a lot about filmmaking in general.
*  So maybe you could take us through the process
*  and maybe highlight kind of to the degree
*  that it differs from a traditional filmmaking process,
*  obviously in many ways,
*  especially at the kind of technical execution level
*  where it does.
*  But even maybe just starting at kind of the conceptualization,
*  how different did this play out?
*  How differently did this play out relative to a traditional project
*  when it came to just the first questions of like,
*  what are we trying to make? What story are we trying to tell?
*  Did you feel like you could start with the same questions
*  or did you have to approach it in a fundamentally different way
*  given the different tools that you were going to be using?
*  I thought the genesis for the project was...
*  I mean, it's a very different process
*  from when you're kind of ideating a completely original piece
*  without any kind of images to go off of, really.
*  Normally, you start with a script or an idea.
*  You start with an idea, then it kind of evolves to the script phase
*  and then you kind of storyboard things out.
*  And then if you're lucky, if you have enough money,
*  then you get to shoot the thing, right?
*  And you go location scouting,
*  you choose your environments and your sets
*  and scenes, and then you kind of go out and film it.
*  And with Dali, it kind of gives you a great starting point.
*  Like, it gives you some place to start.
*  And whether you take to it or not, that's up to the creator.
*  But what happened with our project was,
*  you know, Steven was extremely excited about this new technology
*  and just went gung-ho in terms of generating all these fantastic,
*  extremely photorealistic, cinematic images
*  that really lent themselves to, you know, just fantasizing about,
*  like, about, hey, this could become a movie.
*  And so it was easy, at least for me,
*  to see, you know, Steven's initial Frost series,
*  whereas I think it was a series of, you know, 20 or 30 images.
*  And from there, you know, basically,
*  these images were faces and mountains
*  and closeups of gear and things like that.
*  It's like, it was the beginning of a world.
*  And all it kind of needed was a story to kind of tie it into.
*  So, like, we had this amazing starting point for this,
*  which normally you don't get unless you're kind of drawing inspiration
*  from a bunch of different things,
*  and then you ultimately have to make it your own.
*  But with, you know, a Dolly image generation,
*  it gave us this incredible starting point
*  that we could just hit the ground running with.
*  So let's dig in on each of those a little bit more.
*  I think, you know, people have seen a lot of cool stuff,
*  I would say, you know, safe to say.
*  If they're listening to this podcast,
*  they've seen some cool AI art.
*  Probably, though, you know, it's often the case
*  with different AI systems that you kind of,
*  you know, to a first approximation,
*  kind of get out of it what you put into it
*  in the sense that if you don't have any vocabulary
*  or expertise in an area,
*  then you kind of get amateurish stuff out.
*  And that seems to be true, both on the image,
*  you know, creative side,
*  and also on the language models as well, right?
*  You know, some of the most creative
*  and interesting projects in both realms
*  are predicated on the person, you know,
*  the creator really knowing deeply what they're doing.
*  So I'd love to help people leave this conversation
*  with a little bit better sense of like,
*  how can they prompt for consistency
*  or kind of create a world?
*  You know, when I go in there myself,
*  I feel like, okay, I, you know, I want an image of this.
*  It doesn't really come out how I'm looking.
*  I kind of mess around if it's still not,
*  how it's looking, you know,
*  how I'm wanting it to look in my head,
*  like, I'll just give up or I try something else.
*  But to make, you know, I don't know how many cuts
*  there are in this 12-minute film,
*  but it seems like, you know, typically,
*  whatever, every two seconds or something,
*  you've got a lot of shots over the course of 12 minutes.
*  And so to sustain an aesthetic for a full 12 minutes
*  to make something that ultimately feels coherent,
*  seems like you really pushed on this frontier of consistency,
*  predictability.
*  So I'd love to hear kind of more about how you conceptualize that
*  and the techniques that you and the team developed.
*  Right, so I think it's important to kind of imagine in your mind
*  how you think these images were captioned originally,
*  because those captions are critical
*  in the training of the data set
*  and are kind of a fundamental first base
*  for how to think about getting images.
*  So before everybody had access,
*  I was taking a lot of prompts from people,
*  and people would just kind of give me random prompts,
*  and I would help to improve those prompts.
*  Right, and they would say things like, you know,
*  I really want to get something that looks like a photo,
*  a real photograph of a gray alien skull.
*  You know, and so they would just put gray alien skull
*  into an AI image generator,
*  and they would get back an illustration or a painting
*  or something that, you know, didn't look like a skull at all,
*  or maybe it wasn't a gray alien.
*  So I would say things to them like,
*  hey, let's imagine this were real,
*  and there were a gray alien skull.
*  You know, where would it be?
*  It would probably be somewhere like Museum of Natural History.
*  Right, it would be in New York,
*  and like I want you to see it in your mind as that thing,
*  and like now we're going to prompt,
*  and we're going to say like the skull of a gray alien,
*  and it would be in, you know, circa 1946 or whatever
*  in the Museum of Natural History.
*  Something like that really sets up a kind of contextual framing
*  for DALI or an AI image generator
*  in a way that helps it to understand what are we going for,
*  what are we looking for, and where might we find that thing.
*  And so, you know, if you were to imagine
*  gray alien skulls being captioned
*  also inside of something like National Geographic, right?
*  Like let's imagine there's a photograph of a gray alien skull
*  held in a museum collection taken in the 60s.
*  Now we want to prompt for that image.
*  That is really the way to think about achieving images,
*  for me, inside of these generators.
*  Hey, we'll continue our interview in a moment
*  after a word from our sponsors.
*  If you're a startup founder or executive
*  running a growing business, you know that as you scale,
*  your systems break down and the cracks start to show.
*  If this resonates with you,
*  there are three numbers you need to know, 36,000, 25,000, and 1.
*  36,000, that's the number of businesses
*  which have upgraded to NetSuite by Oracle.
*  NetSuite is the number one cloud financial system,
*  streamline accounting, financial management,
*  inventory, HR, and more. 25.
*  NetSuite turns 25 this year.
*  That's 25 years of helping businesses do more with less,
*  close their books in days, not weeks, and drive down costs.
*  One, because your business is one of a kind,
*  so you get a customized solution for all your KPIs
*  in one efficient system with one source of truth.
*  Manage risk, get reliable forecasts, and improve margins,
*  everything you need all in one place.
*  Right now, download NetSuite's popular KPI checklist,
*  designed to give you consistently excellent performance,
*  absolutely free, at netsuite.com slash cognitive.
*  That's netsuite.com slash cognitive
*  to get your own KPI checklist.
*  netsuite.com slash cognitive.
*  Omniki uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work,
*  customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it,
*  and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
*  So if we kind of take the pre-context
*  and then apply it to a production like The Frost,
*  the first thing we really want to do
*  is just kind of set up a contextual prompt structure
*  that looks like,
*  hey, what kind of image do you want?
*  Portraits. I want portraits from the film,
*  then let's give it an imaginary film name.
*  For The Frost, we called it Tundra,
*  just because it's kind of a tweak on the word tundra,
*  and felt like something that wouldn't be in there,
*  but, you know, was like pointed enough to kind of set the mood.
*  So we want portraits from the film Tundra,
*  then we're going to add a comma,
*  and Oxford commas are a huge part of, you know,
*  crafting the prompt, if you will,
*  but the next section is kind of like,
*  okay, what are we shooting, right?
*  So we're shooting people climbing a snowy mountainside, right?
*  That's kind of the subject matter of the prompt.
*  And then we put another comma,
*  and we say something like filmed by, you know,
*  various famous like Hollywood cinematographer or director.
*  And now it's kind of like, okay,
*  if you were to imagine the location of that image in a data set,
*  you know, maybe it would be in a blog post about a film,
*  or maybe it would be like in an IMDB kind of still or caption,
*  or maybe it would be, there's tons of film sites, right?
*  And so sort of like imagine the imaginary caption
*  for this film image that is really kind of pointing
*  to where that image might be hypothetically,
*  and also kind of an art directed structure.
*  We have a structure that's like,
*  hey, I want this type of image from this imaginary project.
*  Here's the subject I want in this particular instance.
*  And then we can add additional kind of consistency information to the end.
*  So maybe it's like always directed by the same director,
*  or maybe it's not, but we always want like a consistent element
*  to be in our shot, like the color yellow,
*  or, you know, the colors blue and gray in the case of the frost.
*  And by setting up what I keep referring to as a contextual wrapper like this,
*  we kind of have a frame around the subject matter.
*  And now what we do is we go in and we play with that subject matter
*  to kind of achieve different shots.
*  So if you go look at the frost and you think of it not as kind of like moving video,
*  but just like one representative image from each of those video moments,
*  that is, you could basically substitute that out
*  for the subject matter portion of the product.
*  That's what helped us get the look of the frost.
*  There's a couple extra things that I think would help in continuity
*  to answer that question, like that definitely helped us
*  in terms of attaining that at times seamless look.
*  The whole thing took place outside in the snow.
*  Right, so when we're cutting from shot to shot,
*  that's an easy transition for your brain to make like,
*  okay, well, in this shot, it might not be exactly the same background
*  and those tents might not be the same as it was in that reverse shot,
*  but I'm buying it because there's snow and there's mountains.
*  So that was huge, like kind of creating an environment that was outside.
*  Because once we got inside, that's a whole different ball of wax too.
*  Also, you know, another challenge with this stuff was that,
*  was to try and create like, you know, cinematic continuity.
*  And, you know, by that, I mean, just like, okay,
*  just the fundamentals of a conversation,
*  where you have a shot and a reverse shot.
*  And that kind of stuff was the most challenging.
*  So once we had that look, then we kind of had to go back in and refine,
*  okay, that's when we had to kind of use our knowledge and apply it.
*  Because it's like, okay, you can only have a certain amount of wide shots
*  within a scene, you need to punch in,
*  or you need more wide shots.
*  So you need a different angle, you need a profile, you need this.
*  And so like, having that knowledge like, of filmmaking, essentially,
*  was a great help.
*  Because that's what we, you know, once we had our foundational shots,
*  our big master shots that the teams created,
*  then it's like, all right, how do we enter this world?
*  How do we explore this world in a cinematic way,
*  in a way that audiences are used to experiencing?
*  And that's where like, the real specific prompting came into play.
*  And sometimes, and you know, we got mixed results out of that.
*  You know, sometimes we get exactly what we want.
*  And then other times, we kind of let Dolly take the reins
*  and got some great stuff there.
*  So...
*  Right, I think that's a good way to think about it,
*  maybe for the audience, is like, not so much me, but my team.
*  They're like, they're really trying to get out there
*  and dig up the raw materials.
*  My raw material, like, think of cinematography,
*  think of these shots.
*  That's kind of my side of it.
*  Then Josh's side of it is like, making that into a film,
*  like focusing on the story, figuring out like,
*  how to build a story out of those raw materials.
*  And then we kind of get into an iterative feedback loop
*  where, you know, he's like, okay, this scene is working
*  or this scene isn't working.
*  I need more reverse shots here.
*  You know, how do we, let's go take a crack at that.
*  And then we try to go mine for some more of that type of shot
*  and bring it back to him.
*  And then, yeah, maybe it is working
*  or maybe it isn't working.
*  We need to make a tweak.
*  Like, definitely the biggest thing in all of this,
*  I mean, that's kind of like a standard flow
*  or could be considered a standard flow
*  in terms of iteration around a project like this.
*  But Dolly or any AI gen is like kind of an artist on its own.
*  It's almost like a, you know, a cinematographer
*  that you don't fully control.
*  And I think what's interesting about all this
*  is that, you know, we talk a lot about these things
*  or we refer to them quite often as tools.
*  But there's also sort of an artist component there.
*  There's definitely an unknown with the AI
*  that is just not fully within your control.
*  And so we have to treat those AIs
*  as if they were themselves artists
*  and sort of like be willing to be receptive
*  to what they give us in the moment,
*  on the day, in this shot or any other shot.
*  And then, you know, see what we like,
*  see what new ideas come out of that.
*  That's definitely kind of the most new aspect of this,
*  I would say, because in a typical production,
*  you control everything, you know, you go there,
*  you are direct the scene, you set it up the way you want it,
*  you have the talent you want,
*  you've got a script exactly what you want them to say,
*  like you may deviate here and there,
*  you know, as encouraged by the director,
*  but fundamentally, like you're in control.
*  In the case of image gen, it's kind of like,
*  it's much more like an active substrate
*  that you're trying to sort of manage and mess around with
*  in order to create something
*  that fits into your project and works for you.
*  If this were real, let's imagine it were real.
*  Where would it exist? Who would have created it?
*  How would it be described?
*  So that you're not just starting off with,
*  you know, a kind of naive, you know, purely descriptive thing,
*  but you're trying to bring in all these other associations
*  and kind of marshaling the, you know,
*  the vast knowledge base that the system can draw on.
*  And the language model side too,
*  we've had a couple moments like this in the past
*  where, you know, I've been trying to use adjectives
*  to get a language model to do something for me,
*  like write better, you know, copy, right,
*  for our videos at Waymark.
*  And then occasionally, you'll say something to me like,
*  why don't you tell it to make it like David Ogilvie wrote it?
*  And then I'll be like, oh, yeah, that's quite a different approach,
*  but in some ways, way more powerful, right?
*  Because I'm usually very like literal
*  and kind of sitting there,
*  much like you're kind of, you know,
*  gray alien skull example, I'll be like,
*  I want concise copy and I want vivid copy
*  and I want memorable copy and I want, you know,
*  all these sort of, you know, action verbs
*  and I'm kind of just giving it like a checklist.
*  And you are instead invoking a master,
*  which is I think something probably a lot of people
*  could stand to benefit from in really any project
*  that they're doing.
*  So that's a bottom line that I think, you know,
*  people should definitely take away
*  and incorporate into their own usage.
*  You know, there's this kind of iterative cycle,
*  not knowing a lot about filmmaking.
*  To me, that sounds like pretty profoundly different, right?
*  I mean, I imagine in some cases,
*  especially with all sorts of technology that is used,
*  you can kind of patch over things
*  that you didn't actually film when you were doing the filming,
*  you know, later at the editing stage.
*  But still, I also would imagine that like,
*  you're pretty limited in most cases by
*  what did you actually capture
*  when you were in the capture phase?
*  And it's not easy, right, to go back and like,
*  reset up the set and bring the actors back together.
*  So this fundamentally does kind of change the flow
*  from one that is much more planned out in advance
*  and kind of, you know, waterfall,
*  to use like a software analogy,
*  to now one that is actually much more kind of agile
*  and allows you to, you know,
*  to spin back to the raw materials anytime you want.
*  Am I overstating how different that is?
*  Or is that really like a very different reality
*  for making a film?
*  No, it's super different.
*  I mean, you can punch in as sort of as you were referring to
*  on various projects, whether it's, you know, audio or
*  something else with video.
*  But yeah, it's very expensive and time consuming
*  to go back and shoot this stuff.
*  How I would set it up though for the audience is like,
*  it's really a trade.
*  Because yes, it's very iterative.
*  You can go back anytime you want.
*  You can revisit shots, get new material,
*  stuff that, you know, would otherwise kind of cost you
*  a fortune to go back and reshoot and rethink about.
*  The trade, however, is like you're not fully in control.
*  You still have to take those ideas again from Dolly,
*  from Mid Journey, from whoever.
*  And yes, you're getting more, but you're also getting more,
*  again, is not within your control.
*  And this is really where Josh, I think, has stuff to say about,
*  you know, what that process actually feels like coming from,
*  you know, the world of a traditional director to a newer
*  project like this.
*  I mean, that was probably the most revolutionary, most
*  eye opening.
*  Oh, shit moment that I had during this project was when
*  we were actually we're we're in the cutting room.
*  We had our we had our stills.
*  They were still yet to be animated.
*  And, you know, it's like just like in any kind of creative
*  process, you're kind of searching for more.
*  You want to make it as best as possible, you know, the best it
*  could possibly be like, yeah, this is cool.
*  And this shot is kind of cutting with that and the music is
*  hitting right.
*  And like we're you know, these two people are talking and it's
*  a scene.
*  But like, wouldn't it be great if this could happen?
*  And then, you know, in it, right, like you said, in a in a
*  in a normal traditional production, even an animation
*  to go back to shoot is is a luxury that, you know, is that
*  a lot of people can't afford to do.
*  It's like you got to work with what you have a lot of time,
*  especially if it's already in the can.
*  And with Dolly, you can in real time say, all right, let's get
*  this hand clutching this rope.
*  That's going to, you know, that's going to heighten the
*  drama. We want this scene to be super tense, like when the
*  person is, you know, clean for their life and is slipped off
*  the mountains like, OK, how do we heighten those moments?
*  And and we could literally engage the team for a prompt.
*  They can get us back an image within 20 minutes.
*  And then we could put it in the timeline, watch it down and
*  know that's not working.
*  The fingers are messed up or, you know, let's let's pull back
*  even more.
*  Have them outpaint it like two times or something.
*  Ah, that's it.
*  Beautiful.
*  And then you have your shot and that's how that's how the.
*  The Polish phase happens, really, it's just like that's how this
*  thing became polished.
*  And like I think as as these models get, you know, start to
*  develop even more, we're just going to see the Polish get even
*  that that phase just be faster and and like be more
*  exhilarating.
*  Yeah, in terms of practicality there, I think Josh mentioned
*  the storyboard earlier, which we do use.
*  But I think in our case, something that's different is ours
*  is really an active storyboard.
*  Right. So we use just a whiteboard website that, you know,
*  all the team members can go and see simultaneously and kind of
*  work on collectively.
*  But, you know, we kind of have a row for each scene and images
*  laid out in sequence there.
*  But, you know, the images can be taken down and new image gets
*  put up or we make space and put a new image in.
*  And those images are not like a hypothetical or concepted or
*  like an idealized version of what we want.
*  Those images are actually what we're working with.
*  So we go through this active storyboard phase where without
*  worrying about the animation or anything else, we're just kind
*  of worried about a sequence of stills.
*  And I do think that's not totally different from like an
*  animatic process or something.
*  But it's nice to just be able to do that continually throughout
*  the project.
*  And so as Josh was saying, like, OK, he's decided in the
*  scene he really wants a tight close up of somebody gripping a
*  rope.
*  All right.
*  Seems straightforward enough.
*  But now, like, the variable part is, is that hand like masculine
*  or feminine, young or old?
*  What does that rope look like?
*  Is it like, you know, a sleek black mountain climbing rope of
*  some sort?
*  Or is it like an old nautical rope from a ship, you know, from
*  the 1600s or whatever?
*  And you really like getting all of it back at the same time.
*  And then you kind of have to decide, like, you know, what
*  fits here.
*  And obviously you hope to hone it and get more specific than
*  that.
*  But hopefully that kind of like helps to contextualize and
*  provide an example for people of even though you've ID'd this
*  very simple thing, like all the variability that comes or like
*  explodes out of that one maybe individual request.
*  When it comes to faces, you know, the continuity of the
*  characters through the movie, you had mentioned the tents, you
*  know, in the background can kind of change and you can kind of
*  get away with it because, you know, it seems coherent enough
*  and people kind of, you know, don't latch on to those kinds
*  of details.
*  But for things like the characters faces, I would assume
*  first of all, you know, a lot lower ability to slip past, you
*  know, the viewer when those things change or are kind of
*  inconsistent from scene to scene.
*  And that seems like it would be really hard to get consistent
*  across, you know, a bunch of different shots, a bunch of
*  different contexts.
*  So how did you approach that problem of getting these
*  characters to feel coherent across all these different
*  images when in fact, like, presumably they're being kind of
*  generated from scratch each time, right?
*  Yeah, I mean, it was stupid hard in the context of our project,
*  to be clear, because we're working with Dolly because it's
*  you know, back in time in terms of the tech.
*  Like another like caveat for now is like this is much easier now
*  within mid journey, which you can do either by blending
*  images together, which will kind of give you a consistent
*  character or feeding it like uploading an original image and
*  then asking for like subtle variation on that image.
*  It's still not perfect, but it's a lot easier today than it was
*  then in terms of back then.
*  I think we yes, we really spent a lot of time banging our head
*  against the wall.
*  Josh, in particular, just.
*  Yeah, I remember I was all the time trying to ask, you know,
*  like, couldn't we just kind of follow a group and like, let's
*  make the story about the group so that we don't have to care
*  too much about any particular character.
*  Josh was like, and I'm kind of twisting his arm the whole time
*  in that direction.
*  But, you know, there was this one character, Dr.
*  Alrick, that he was like, look, we like we really need time
*  with a few characters.
*  You know, you've got to find some way to give me a
*  consistent character.
*  Like, you know, he was very amenable to many different
*  possibilities for how that might manifest.
*  But ultimately, the thing we kept coming back to is like
*  this idea of an archetype.
*  Right.
*  So I think not to be understated is just the prevalence and
*  significance of archetypes within these image generators.
*  Right.
*  You can think about a common archetype like a statue of the
*  Virgin Mary that we've all seen 100 different times all over
*  the world.
*  Dolly or any image gen has certainly like seen a ton of those
*  statues.
*  You can also think of an archetype in terms of something
*  like the Mona Lisa that's essentially the same image, but
*  a million different times in the data set.
*  There's a lot of different ways to think about this.
*  But we for the character of Ulrich, the archetype we set up
*  is like a gray haired, wily-esque mad scientist in a
*  white lab coat, you know, with long gray hair and glasses,
*  something archetypical enough that, you know, it's not the
*  same person.
*  But like if you study the faces, obviously the faces are
*  changing.
*  But the idea is really to kind of just establish continuity so
*  that that character feels like the same character.
*  Josh uses a lot of tricks there.
*  But like at the gen level, we're really working with
*  archetypes and thinking about it in that way, knowing that,
*  again, we're not going to get the same thing.
*  We're just kind of like in an address field of possibility for
*  what the generator may return.
*  That is a huge thing, Dr.
*  Ulrich, you know, to try and get that character.
*  There's a scene in the movie where, you know, this Dr.
*  Ulrich character is, you know, making a speech at the at the
*  United Nations trying to save the world.
*  And it's action packed.
*  And when you're hoping to get action and movement and, you
*  know, and kind of meet the bar that's been set by, you know,
*  modern day editing techniques, it's like you kind of have to go
*  there. You have to cut.
*  You have to make cuts.
*  You kind of you got to move your camera.
*  You got to you got to play the game that's already been that's
*  been set in motion.
*  So we were just we found this this tropey archetype of like
*  the mad scientist.
*  And then, you know, at first I was like, yeah, it's not the same
*  guy. And how do guys how do we get the face, you know,
*  transplanted onto this shot?
*  And it's just like it's not going to happen.
*  Right. And it's like we but after a while, you know, you
*  take a step back from the project and it's like you look
*  at the you look at the scene and when the voices, you know,
*  and the voice of Dr.
*  Ulrich was read and that's the you know, that's a consistent
*  voice and the music is put into play.
*  And I bought it, you know, it's like, oh, it's the same guy.
*  But if you look at it from shot to shot, it's not it's some of
*  them look very different.
*  One guy looks like Santa Claus and he's, you know, probably 30
*  pounds heavier.
*  And the other guy is is a little more is a little on the more
*  trim side.
*  And and he's got a couple different facial features.
*  But, you know, we're relying on that like suspension of
*  disbelief that is just like very prevalent in a lot of
*  moviemaking anyways.
*  So we were just really leaning on that with with these
*  characters, especially with that character, because he
*  probably makes the most appearances.
*  So that was a huge struggle.
*  And I'm kind of I'm really proud of how that turned out.
*  Yeah, that's super interesting.
*  I honestly had not studied it that closely.
*  And, you know, I've watched a few times, but in retrospect,
*  you know, hearing what you're saying now, it just kind of,
*  you know, it just kind of worked for me.
*  Like I didn't really notice those variations or think twice
*  about it, frankly.
*  Human perception is actually kind of accommodates a lot of
*  things like we're not really trained to to be on the lookout
*  for things like this.
*  I mean, there's a really interesting, you know,
*  potential lesson here for kind of human A.I.
*  interaction in general, right?
*  That like certain things that we're not primed for are really
*  easy to slip past us.
*  We've we've got no prior context or reason to be on the lookout
*  for a person to be like not the same person from scene to scene.
*  It just doesn't happen.
*  So in reality, then you can actually slip a lot past
*  somebody because they're they're kind of prior, so to speak,
*  on that happening is just so low that, you know, it doesn't it
*  has to be pretty egregious, I guess, or maybe not pretty
*  egregious, maybe too strong, but it has to be significant to get
*  over a threshold where people would see it if they didn't
*  specifically come in looking for that.
*  I think it speaks to the power of the story to not our story,
*  but just the power of storytelling.
*  And when people are engaged in a story, you could forgive a lot
*  of things.
*  You know what I mean?
*  It's like there's a whole there's countless, you know,
*  Reddit boards dedicated to like, you know, gaffes in movies, you
*  know, or you could see the did you spot the boom in the shot?
*  Did you spot like this actor wasn't the same actor as in this
*  scene? And it's just like a lot of that stuff we don't catch just
*  because like you if you're watching a story, you want to be
*  engaged, you want to feel and so like that's that did nothing but
*  help our cause with this.
*  It was a cool thing to see put into practice.
*  So going back to your comments about the you know, the shot
*  with the rope, right?
*  What kind of hand is it?
*  What kind of rope is it?
*  All these little details.
*  How much of that are you accomplishing through iterating
*  on a single image?
*  Like people have seen these kind of mask and fill techniques or
*  out paint techniques.
*  When an image actually gets to the point where you're going to
*  use it, you know, how often is that something that like Dolly
*  spit out?
*  You're like, great, we'll use it versus, you know, it's been
*  something out.
*  But then you went and, you know, re drew the rope five times and,
*  you know, the hand five times.
*  How much of that kind of image level, you know, partial
*  editing and reworking are you doing?
*  Quite a bit, quite a bit.
*  I mean, most of the images have some particularly with Dolly
*  because, you know, those images are starting out so small and
*  then kind of scaling up from there in terms of the way the
*  images are generated.
*  You know, you're often like going back and correcting an eye
*  or, you know, painting over hands or something in order to
*  try to get a better result.
*  The rope example is a quality example in terms of adding a
*  new shot in that you want.
*  But I think in many, many, many of the shots, there's just some
*  aspect of it that you want to touch up or make different or,
*  you know, sometimes Dolly just does crazy things like it'll
*  just throw a random object into the background.
*  You know, it's kind of a fun, like creative occurrence.
*  But also when you're looking for consistency and there's like a
*  steel palette or something in the background that just like
*  has no reason for being there.
*  Then Josh is making notes like get rid of this, get rid of
*  this, please change this.
*  Another example is like, OK, these outside shots are great,
*  but I'd need a fire.
*  Like, can I get some plumes of smoke?
*  So things like that are happening all the time.
*  And then in terms of like the real cheating Photoshop work
*  that we're doing in this process, like the one thing we
*  really needed was this sort of MacGuffin object.
*  I think of it that way anyway.
*  And it was this idea of a transponder that is sort of
*  moving up the mountain with these characters over the course
*  of the story.
*  And so in order to achieve that, we went into Dolly to first
*  create that object, you know, went through many, many, many
*  sort of prop iterations on what that thing might look like.
*  Once we had it, though, in a few different angles, then that is
*  an example of an object that literally gets composited or you
*  can think of it as stitching it into various shots over the
*  course of the film so that it's there, so that we have that kind
*  of one little consistent object that can follow you through
*  the film and sort of help add another layer of continuity.
*  Can you unpack that notion of a MacGuffin for folks that aren't
*  familiar with it?
*  The MacGuffin is kind of the idea of an answer, an object or
*  as something that isn't really there, it's more the idea of it
*  that's there.
*  So I'm not exactly using it in the correct, like in the context
*  that it would most often be used in terms of like a film where
*  people are searching for a thing that's the MacGuffin, it's the
*  answer, it's the object, they may find it or not find it, it
*  kind of gives meaning to the story without providing like
*  substantive meaning itself.
*  The transponder is similar in that it's not a real transponder,
*  it's not really there, it is something we're just kind of
*  stitching throughout the film.
*  I think of it that way because it's not really coming from the
*  generator in place, right?
*  Like we're putting it in in order to add this kind of idea
*  of consistency to the project.
*  So maybe I'm equivocating a bit there, but it's how I think of
*  the construction of the film.
*  So another kind of challenge, Josh had mentioned this kind of
*  shot and counter shot or was it reverse shot, characters in
*  dialogue, you're going to kind of see over each one's shoulder,
*  right?
*  People can recall how that often happens in the movies and TV
*  that they watch.
*  It strikes me that if you want to go back and replace a rope,
*  there's pretty good tools to do that, right?
*  Where you can mask it out and try it again and iterate on that.
*  But for broader composition, that's obviously a lot tougher,
*  right?
*  You can't just like mask it, you know, it's about you're masking
*  out the whole thing is like, yeah, the layout, you know, the
*  whole kind of composition of this, you know, if it's wrong,
*  it's kind of wrong.
*  You can't just kind of locally change that.
*  So how did you work on that and how would you describe kind of
*  what the tools can and can't do there?
*  Right.
*  I mean, there's actually like benchmarks around this where
*  people are like, you know, can you create an image where
*  there's like, you know, one blue circle and a red square and the
*  red square has to be below the blue circle, whatever these kind
*  of compositional, you know, sort of somewhat stilted, but, you
*  know, clearly defined compositional tests.
*  Yours are obviously much more kind of in the eye of the
*  beholder in terms of whether they're going to pass or not.
*  But I imagine that must have been a real challenge.
*  And, you know, what do you do to try to dial that in and, you
*  know, get the hit rate up to an acceptable level?
*  A couple of things to think about there.
*  One, it's always getting better, you know, like the ability to
*  prompt for unique things and unique situations, which I think
*  is ultimately what you're getting at there is all the time
*  improving.
*  So I would just put that up front to Josh is asking for any
*  number of things.
*  He's not just asking for small tweaks to the hand or a rope.
*  Like he's very often saying, like, I want a different
*  background here or, you know, I like this character from the
*  image.
*  I want them combined with another AI image.
*  And so, you know, there is kind of like some compositing
*  happening at the level of like putting images together.
*  If you want to think of them almost as collage, like from the
*  dolly generated images, that's another way you can think of it.
*  But then I guess, like, at an artistic level, there's multiple
*  things happening as well.
*  One thing is like sort of knowing what form looks like to
*  begin with is going to give you a much better idea of where you
*  should be, you know, erasing, if you will, in order to sort of
*  force a better image to arrive based on the amount of space
*  you've taken away.
*  And that is like also contributing to the available
*  space to paint back in.
*  So.
*  If you want to refine a form, you know, thinking about it as
*  an artist, there is like definitely a structure or a method
*  of attack in terms of how you are in painting and out
*  painting with an image.
*  But then also you have to go back to the data set and think
*  again to the data set.
*  This is like I remember we had a number of shots that were
*  daytime shots that Josh wanted to see fires in.
*  And they were like overhead shots of the camp.
*  He wanted fires to be there.
*  And it's like, you know, if you just go do a survey of film or
*  go do a survey of this type of image, like there just won't be
*  that many examples of images that are like daytime with a
*  brightly burning flame as well.
*  Like you might get that at night.
*  You might get that in other contexts.
*  And so a lot of times it feels like you should be able to just
*  ask for, you know, object X, a fire right here in this place.
*  But.
*  All of the informational context surrounding the place where that
*  object goes is contributing to how the machine is going to
*  paint into that space.
*  And then that's also coupled with like the sort of contextual
*  information that lives in the data set.
*  There are other times like the color grade of an image.
*  I remember we were trying we had shots that were very, very,
*  very blue, and we were trying to paint in something like a red
*  scarf or a purple scarf or yellow scarf and like all of
*  those colors.
*  There is no way that after a film has been graded that that
*  color is going to show up bright in the final image.
*  So there are many, many instances in film where like
*  someone is wearing a bright piece of costume or whatever.
*  But after the grade happens, the color grade.
*  Those colors become much more faded.
*  And so Dolly is never going to paint in like an electric red
*  or an electric purple into that scenario, because it's never
*  seen any examples historically in terms of the way lighting
*  works in these images that is.
*  You know, going to give it any indication that that should
*  happen. That's an interesting mystery in terms of where we are
*  with the training right now is kind of like trying to twist the
*  arm of these machines to like reach into new or novel spaces
*  to create things where there really isn't great kind of pre
*  context around what this thing should look like in the images.
*  That also is a bit of a tangent, but like that's cashing out in
*  many ways when you're interacting with these generators.
*  If an idea is complex, well understood, but maybe like
*  without pre context, you're going to get a fuzzier image.
*  You know, it's almost like the machine is having to think about
*  a lot of different things at once.
*  And so, like, you know, you're really kind of getting something
*  that's maybe a little fuzzy or maybe a bit more painterly when
*  there's a really clear idea of what that thing is.
*  It's almost like, you know, the image dials in to something
*  more specific, much more detailed.
*  All that's a long way of saying all these things are kind of
*  happening at the same time.
*  And at an iterative level, we're kind of just listening to what
*  Josh wants and doing our best to get that thing.
*  But we also have to be conscious of what is possible in this
*  image, given what it sort of already looks like, such that we
*  don't like step wildly out of bounds and make a novel request
*  that's just kind of impossible for the machine.
*  I mean, I think this is another really fundamental point for
*  different kinds of AI systems as well, right?
*  It's like the notion of can AIs have breakthrough insights?
*  You know, can they have eureka moments?
*  Can they suggest science experiments that are actually
*  worth running because there's enough insight behind it that
*  makes it like a not previously kind of well-trod hypothesis?
*  In this case, you know, can it create stuff that like doesn't
*  look like anything in the set?
*  In general, my read is like that's very tough and almost
*  vanishingly rare.
*  Certainly, you know, and I've looked for things like can it
*  come up with good science experiments ideas?
*  You know, with current systems, I would say not really.
*  You know, it can take a good science experiment idea and
*  start to map out the steps.
*  But I haven't seen any examples where it would actually give you
*  a really good science experiment idea upfront.
*  But I guess, you know, so in the context of this image stuff,
*  like we have seen things like the avocado chair.
*  How do you make sense of something like the avocado chair,
*  which, you know, maybe that exists somewhere out there,
*  but, you know, that's pretty vanishingly rare.
*  I don't know.
*  I'm just kind of trying to get a little bit better understanding
*  of what are the kinds of like never before seen things that
*  it can do versus the kinds of, you know, never before seen
*  things that you're still feeling like are impossible.
*  This is definitely at the forefront of a lot of different
*  machine learning research and insight being worked on yet to
*  be developed, et cetera.
*  I don't have the definitive answer on this.
*  You're going to get lots of different answers from lots of
*  different people.
*  But I think there is important thinking like within this realm
*  of questioning.
*  So the way I think about it and the way I appreciate these
*  image generators the most is really celebrating the fact
*  that there was a data set that contributed to them.
*  You know, I don't like to interact with these machines
*  kind of.
*  Apart from that thought and that appreciation,
*  I think at a high level, this is really like an exploration
*  of human history that I feel like I'm taking part in.
*  The way I think about that sort of metaphorically or
*  hypothetically is by thinking about that latent space and
*  thinking about kind of a 3D space where a lot of points
*  exist.
*  And I think of those points as sort of all the things
*  previously created, all the things that exist within that
*  data set.
*  Another way to think about it is maybe like a library of Babel
*  analogy or a space where all possible things exist.
*  But if we were to conceive of a thing like a space where all
*  things exist, then the data set is like only the things we've
*  found within that space of possibility.
*  And then what we're actually interacting with with this
*  generative approach is really the space between that set of
*  coordinates.
*  So to reframe it within a space of all possible things,
*  there are all the things we've found and now we're interacting
*  with the space between all the objects we've found.
*  So in the case of the avocado chair, like, no, there weren't
*  a lot of avocado chairs, but like there are a lot of
*  avocados.
*  There are a lot of chairs.
*  There are also a lot of avocado pillows.
*  There's a lot of like there is a ton of different chair designs
*  that look like many, many things.
*  Certainly many of them have been close to the shape of an
*  avocado.
*  And if I were like thinking about the space between those
*  points where like an avocado comes close to a chair, like
*  probably that is like occurring many, many, many times.
*  The fact that the machine is able to, you know, create an
*  inference point between those two and manifest it as like an
*  image of a chair is not that surprising to me.
*  And there are a lot of cool examples where that happens in
*  ways that just like we haven't thought of yet.
*  And that's kind of like where the novel happens here, right?
*  It's like what happens when we blend two, three, five points
*  that we haven't really blended before.
*  That's the sort of everything is a remix philosophy.
*  That's the idea that, you know, we're getting to new places by
*  mixing the places where we've previously been.
*  And there is great opportunity for that to happen.
*  There are a ton of like just purely abstract kind of artists
*  who are producing novel, I would say, just by kind of like
*  putting unique concepts together.
*  But I think that is very, very different from asking the
*  machine to like fundamentally travel outside of the space of
*  points that we know about and get to a new point, a new
*  location, a novel location.
*  That really doesn't happen.
*  And it's my understanding that that is not really like.
*  The space we're working with when we interact with a chat
*  GPT, a dolly or a mid journey.
*  I still a little bit struggle with like, why can't the scarf
*  be super vivid red or, you know, just things like that that seem
*  like that doesn't seem too conceptually.
*  Crazy.
*  Maybe it's more of just a you only have so much like a
*  bandwidth, right?
*  You only have so much data you can communicate to the model in
*  your prompt.
*  And so it kind of has to have I don't know.
*  I'm struggling, though, because it's like you can get avocado
*  chair.
*  Seems like you should be able to get that bright red scarf if
*  you want it, you know, even if it's like not super coherent
*  with the rest of the shot.
*  Yeah, I mean, I'll just jump in for a second like the pre
*  context, though, of the prompt is important there, right?
*  Like in the case of an avocado chair and really with any
*  prompt, the less kind of specific it is, the more opportunity
*  there is for like what I would call open blending, just, you
*  know, intersection between points or like force
*  intersection.
*  The more we contextualize it, the more we say like, oh, I'm
*  looking for cinematic 8K portraiture from a hypothetical
*  film, you know, by this director or lit this way, like
*  within this context, like we are triangulating into a tighter
*  and tighter realm of the space.
*  Right.
*  The avocado chair is like a great example of if I could
*  pull from any image in this data set and put it together
*  with any other image in this data set in this like, you
*  know, mathematical mind of the AI, then a lot more freedom
*  is available to me.
*  And also to be certain, like the mid journeys of the world
*  are all the time doing a better and better job of being
*  able to make ad hoc demands even within context for things
*  like the bright red scarf in a very, very blue cast image.
*  So that's kind of happening.
*  It's happening through our LHF.
*  It's happening through a bunch of other techniques for the
*  type of images that get generated.
*  And we are still developing and figuring out like arm twisty
*  ways to like have these machines generate the sort of images
*  that we want to see them generate.
*  But I also think it's worth thinking about like being in
*  the space, vectoring into more and more specific places in
*  that space and then like contextually what that means
*  for, you know, what the AI sees in terms of like its local
*  area of what it might grab from.
*  It still does cool stuff all the time, stuff that's really
*  creative.
*  I mean, Dolly trolls with the Mona Lisa continuously.
*  And I don't know that people know that if they haven't, you
*  know, generated 100,000 images with it or something like that,
*  or they're not looking for it.
*  And maybe, you know, maybe the developers toss it in from time
*  to time as, you know, a prepend or an append to the prompt.
*  I don't know.
*  Maybe Dolly just does it because it's seen the Mona Lisa so many
*  times that like, you know, it will throw the Mona Lisa in here
*  and there.
*  But, you know, like in the case of Dolly, Mona Lisa is really
*  kind of a character, a ghost in the machine, if you will, that
*  just like shows up in all kinds of different places and context,
*  maybe as a background character, as a photo real version, as a
*  like photo bomb sort of character.
*  In another instance, as a drawing, as an illustration, as
*  a sculpture in many, many different scenarios, Mona Lisa
*  just kind of pops up in the most creative ways.
*  And that's just one example.
*  But, you know, it is really, really fun and funny at times
*  to see that level of creativity is sort of coming from the
*  machine that's happening all over the place.
*  The suggestions that the AI is making through its lack of
*  specific knowledge are also really, really cool.
*  Like I see a lot of clothing that the machine conceives of
*  this kind of like a mix of two different ideas.
*  You know, it's a button down shirt like yours, but maybe it
*  ends right where that top button ends.
*  And, you know, it's a poncho from there on out, you know, and
*  it's kind of like, you know, the machine has no reason to care.
*  You know, even though we talk about kind of bias in these
*  machines at the art level, it's really willing to kind of mix
*  and match and pull from so many different things that like.
*  It's really creative, it's really interesting and it's
*  really unique at times.
*  Fascinating.
*  OK, so.
*  Just being somewhat mindful of time, I want to talk a little
*  bit about the motion techniques that you guys used in this
*  project, then I kind of want to get a little bit of an update
*  on like where you're going next.
*  I understand there's a frost too in the works and, you know, as
*  you've mentioned several times, the tools are improving and
*  the you know, what's available is changing and you're probably
*  going to use significantly different tools and techniques
*  for the second installment.
*  So really interested to hear about how that's going.
*  And then maybe just to conclude, we could kind of zoom out for a
*  second and like talk about the big picture of, you know, what
*  all this means for.
*  Content creation in general, you know, content consumption, you
*  know, it seems like it's going to have a significant impact.
*  I'd love to hear your speculations about that.
*  But with that road map, tell me about the motion.
*  You know, one comment that we've heard from a reviewer is that
*  the vibe of the film is, I'm quoting, grotesque and
*  unsettling.
*  And I think, you know, that obviously plays nicely with the
*  story that you guys are telling.
*  I wonder to what degree that is kind of a, you know, is that was
*  that like an early, late twenty twenty two, early twenty
*  twenty three constraint where you were kind of like, hey, this
*  technology is still kind of in the uncanny valley.
*  Let's just make it uncanny valley and grotesque and
*  unsettling because it plays that way.
*  Could you have made something that, like, you know, wasn't
*  grotesque and unsettling?
*  And I'm understanding that that is in the motion layer.
*  Correct me if I'm wrong with that assumption.
*  But it seems like Dolly, too, you know, is spitting out pretty
*  realistic, not uncanny valley images.
*  And I'm guessing it's the motion layer that was kind of
*  introducing this sort of this vibe.
*  But correct my misconceptions there.
*  Yeah, I the motion was.
*  Was was a challenge, right, because we have these very
*  cinematic images that featured human beings and human beings
*  move a certain way and human beings have appendages that
*  look a certain way.
*  And, you know, knees bend at a certain angle and elbows bend
*  and fingers move.
*  And sometimes Dolly doesn't want to give you all of those
*  appendages in anatomically correct places that, like,
*  would, you know, beget a traditional human movement.
*  So we figured out quite early that our movement was, at least
*  with the humans, the human characters was going to be a
*  very rudimentary look, you know, like it looked at at.
*  Especially with the climbing up of the mountain, that was
*  probably like where the motion was most evident and was going
*  to be featured the most like you needed to show.
*  You need to show them moving up the mountain.
*  That was done in a couple of ways, so I can go into.
*  But when we were using the Dolly generated images, you kind of
*  had to just go the course puppeteer way in terms of
*  After Effects, like literally like taking an arm, moving it,
*  you know, very time consuming way and or a knee and moving it
*  up and then down.
*  And with our we leveraged our amazing animator.
*  I want to call him out.
*  His name is Matt Sessions.
*  He's been working with Weymark for a long time and he did a
*  tremendous job like breathing life into this project with
*  the motion.
*  So I definitely want to want to call him out.
*  We were playing into the characters.
*  We had no choice.
*  You know, this is what Dolly was giving us and we had this is
*  what we're working with.
*  We're working with characters that, you know, might not have
*  a hand or might not have a complete foot.
*  So it's like, how do you animate that?
*  You know what I mean?
*  He's like, well, you got to you got to keep keep keep them
*  climbing up the mountain, so to speak.
*  So we were doing our best there.
*  And also, like in terms of the climbing, like we were still
*  like really inspired by like the Akira Kurosawa movie,
*  The Blizzard, which is featured in in like the anthology piece
*  Dreams, which is like just now being remastered.
*  I think this release this week by Criterion is really cool.
*  But like in that piece, like the characters move a certain way.
*  It's a very slogish kind of movement that that like we felt
*  good about.
*  It's like, OK, like, you know, Kurosawa is is doing this like
*  up the mountain, like we can do it.
*  So like it was it was a great inspiration to have.
*  And also something that I was looking at when I was seeing
*  storyboards come together and then I was seeing the early
*  animations is like it was just coming off as like this is a
*  graphic novel come to life.
*  And, you know, sometimes you just you just want to see the
*  graphic novel.
*  You want to see the comic book just move a little.
*  It doesn't have to be realistic.
*  It doesn't have to be, you know, like in 24 frames per
*  second movement.
*  It's just you want to see a little movement and like and
*  we're good.
*  And that that goes a long way.
*  And that's kind of how we got that look.
*  And, you know, whether it's grotesque or not, like that's
*  up to the viewer to decide.
*  I'm not going to comment on that.
*  There's also different other motion animation that we set
*  into into play to really breathe life into this thing to get
*  the kind of scope that we wanted in terms of like a group
*  of people moving up a mountain and not like really concentrate
*  on moving every single appendage.
*  It's like it would be too time consuming.
*  We kind of we utilized a 3D models from Mixamo, which are
*  basically like 3D characters that you can buy.
*  And and and and animate in a kind of a coarse way and like
*  intersperse them throughout the frame.
*  So like that helped us give us the a little more fluid motion
*  throughout.
*  So do you think you could have done like a different genre at
*  this stage?
*  You know, I'm kind of wondering, like, what if we came back and
*  said, all right, we want to do a romantic comedy with the same
*  tech.
*  Would that just be impossible given, you know, the sort of
*  limitations of how realistic, you know, is it is it wouldn't
*  be possible to make somebody the object of romantic desire
*  with this with this tech?
*  Or is that just not quite there yet?
*  I mean, maybe if you just want to do it as still images,
*  honestly, like we can get something very photo real.
*  But I think, you know, that's a very good question.
*  Like I'll let Josh jump in.
*  But I mean, my immediate reaction to romantic comedy is
*  like, I can't think of anything harder to try to do where, like
*  subtlety of facial expression where, like, so many back and
*  forth between people.
*  Yeah, I mean, we're definitely afforded a lot of things by the
*  genre, by the scope, by the kind of interesting world building
*  that we had around the project.
*  A much more character driven thing would just be really,
*  really difficult right now.
*  I agree.
*  I mean, one of the biggest challenges of this piece was to
*  try and mine emotion out of these characters.
*  You know, it's like we could get like really amazing, you know,
*  photorealistic, frozen nomads, nomads or whatever.
*  And like, but they be, you know, like, for example, like when we
*  were when we were building the avalanche scene, like, all right,
*  we need people in here looking up, looking up at, you know, up
*  at the mountain.
*  And sometimes it would just give us people looking up, you know,
*  in, you know, like like a romantic gaze, even though in
*  our prompt, it was just like in utter terror.
*  They are they are they are about to die.
*  You know, panic exclamation point, exclamation point, like
*  trying to throw everything at it to try and like, you know,
*  receive something back that resembled like a human being in
*  distress.
*  Sometimes like we just wouldn't get that back.
*  You know what I mean?
*  And we had to go in there and manually sometimes and, you
*  know, tweak eyebrows, tweak lip position.
*  And what's what's really cool, we started implementing at the
*  very tail end of the project was, you know, Photoshop has
*  like has like a little AI emotion element to it.
*  So we were able to kind of tweak, you know, some facial
*  stuff with using Photoshop and also some some after effects
*  techniques as well.
*  And also with inpainting, you know, there's a lot of
*  inpainting in this trying to get trying to get a smile, trying
*  to get a frown, trying to get that.
*  So I think, yes, answer your question.
*  A romantic comedy might prove to be difficult now.
*  I mean, there's this new tech that we're just starting with
*  the Frost 2.
*  I don't want to get I don't know if we want to talk about
*  that. I want to talk about it if you're open to talk about it.
*  And, you know, not to like spoil the story or anything,
*  but just the the fact of how fast things are changing.
*  It hasn't been that many months since we were doing the first
*  version and released the first edition of this and tools are
*  changing. Things are getting easier.
*  So I'd love to hear, you know, what are the big advances that
*  are making the second edition, you know, different in terms of
*  your process and different in terms of the possibility of
*  what you can create?
*  What are you using tool wise and what more can you create than
*  before? Voice is another one, too, that I'm really interested
*  in. And we've seen, you know, it seems like we're hitting some
*  thresholds right now in terms of the viability of like deep fake
*  voices for better or worse.
*  You know, would you consider a voice for the next generation?
*  I mean, there's a lot of different frontiers, too, that
*  could be considered.
*  Josh just put together a trailer for the Frost 2 and I'll let him
*  speak to all of the new tech there.
*  And I think maybe just a short preamble there is we obviously
*  started creating the Frost at a time when the tech to us was
*  much more new and then an interesting phenomenon working
*  on the project is like we're totally eclipsed by the tech by
*  the end of it.
*  Right.
*  We also the Frost ended up being a way bigger project than we
*  thought it would be initially.
*  Like we imagine it as just a couple minute piece to begin
*  with and then ended up with like a part one running at 13
*  minutes by the end of it.
*  So we kind of have this thing where like our first pancake
*  ends up also like being the whole brunch.
*  And that's like, how do you do that effectively?
*  It's a bit kind of like live iterate and react for us over
*  the course of time.
*  But one of the things lately we've started to, I think, like
*  become attracted to is this idea of the Frost as an IP, a
*  recognizable IP or storyline that people hopefully at some
*  point become familiar with and then can watch sort of more
*  through these technologies as new tech comes along.
*  And I think that's just, you know, for us, we like that idea
*  because the world of is kind of moving so quickly.
*  It's like, you know, you only kind of get one chance very
*  often to see a thing, think about it, and then it's onto
*  the next, you know, 10 things on the day.
*  So the idea of an intellectual property of some sort, a
*  storyline that you can sort of follow along with and also
*  experience new tech with is becoming a really cool idea to
*  us.
*  So I'll let Josh talk about that new tech.
*  Yeah. So for the Frost, too, we at least for the trailer and
*  for a lot of our tests that were running, we're using
*  Runway Gen 2, which is basically a text to video model,
*  which is something, you know, that when we were making the
*  Frost back in, you know, starting the Frost back in
*  January or December of last year, we didn't even think it's
*  like, oh, that's two years away, whatever it is.
*  At least I was thinking.
*  But I mean, it's here.
*  And I think like as as we were finishing, like cutting this
*  trailer, as I was finishing cutting it, like they just
*  released a newer version of Runway Gen 2, where instead of
*  giving you a four second output, which is kind of limiting, it
*  gives you an 18 second output, which is plenty of time to give
*  any filmmaker to tell the story of a shot and or a scene if
*  you want to just keep that one, you know, keep that one shot
*  running. So or just like it's it's a it's tremendous
*  advancement. And it seems like it's only getting better.
*  But I mean, just interacting with that was was pretty
*  different in that the images were moving, you know, we're
*  not no longer getting still images and then breathing life
*  into them like the life is already being had, you know,
*  breathe into them. And so it's like there's a there's, you
*  know, with that comes more issues. It's like, no, well,
*  now, this person's head is, you know, resembling a tomato more
*  than it is like a humid head. And yeah, we can't use that
*  shot anymore. So it does it does different weird stuff, you
*  know, it's like you're counting different, different little
*  weird, weird quirks that it has. But like, you know, I feel
*  like that'll get ironed out. And like, as as we work with it
*  more, we'll be able to kind of articulate our best practices
*  there. But yeah, it's just super exciting to have worked with
*  that. So the new technique is now just straight text
*  prompting with Gen two. That's the focus at present. Yeah,
*  that's interesting. There's also images involved in those
*  prompts at times, too, which, you know, it's cool because
*  like you can go over to a dollar mid journey, like craft sort
*  of the image that you want.
*  Runway to use in order to create that scene. And now you can do
*  a couple of things. You can just do a pure text prompt. You can
*  do that image plus a text prompt to sort of like ask for the
*  type of movement you want, or you can just use that image
*  only and just see what runway spits out as a result of that
*  image. So it's kind of three things available to to there.
*  Now, in painting, as Josh was saying, like in painting, out
*  painting, these things are I mean, they can be done
*  rotoscoping can be done, but like it's way more taxing to do
*  that than typically to just kind of like prompt for another
*  generation. So there is kind of less flexibility at the level
*  of video output. But, you know, it's kind of
*  we're building a flow now where we're sort of like achieving the
*  image first. In many cases, not all but in many cases, and sort
*  of using that as a starting point for the generation of
*  these clips. You also mentioned AI voice, Josh, you are using AI
*  voice.
*  When we were voicing Frost part one, we auditioned a ton of AI
*  voices just just because there's so many different characters. And
*  it's like, you know, it's a job to go in and, and, and audition
*  people hear different clips from people reading lines. It's a
*  whole it's a thing. And so we were hoping to maybe employ some,
*  some AI VO and it just wasn't it wasn't happening. It wasn't it
*  didn't sound real. It didn't. They were just it was too
*  quirky. It was too robotic sounding, whatever. But now,
*  during, you know, our time with the Frost two, it's like the
*  advancements are significant, especially applying them in a
*  dramatic context. You know, I don't know anything about like,
*  anything outside of, you know, a drama, but within this dramatic
*  context, it's like some of them really, really excel. So yeah,
*  we were blown away.
*  What are the tools that have jumped out to the most right now
*  in the AI voice?
*  I like 11 labs.
*  Their pro voice clones are insane. Recently, I have been
*  just amazed by that I'm waiting for mine, that I can, you know,
*  delegate the whole podcast adventure to the AI as well. Also
*  play HT, you know, former guest on the show, they just released
*  something in the last few days that I think we we really want
*  to check out too, because, man, it is, you know, to be able to
*  prompt emotion on top of just the text. I don't know if 11
*  Labs has that you can tell me if they do, but the ability to go
*  in and be like, you know, this is set in anger, you know,
*  versus set in surprise versus whatever. I mean, just a whole
*  new layer of control that has just as far as I know, just come
*  online with their last release. So it's, you know, your your
*  toolkit is expanding exponentially right now.
*  Yeah, I mean, it is a bit of a sign of a like, it is really,
*  really nice as artists to start to see these tools begin to
*  incorporate more of a tool set that we need in order to kind of
*  like get emotion out of things. And you know, like, Josh was
*  talking about trying to mine for motion inside of Dali, I really
*  think a lot of that is like, a lot of the emotion has just kind
*  of been RLH death, like to death out of these data sets. And it's
*  understandable at the level of like, you know, creating images
*  that feel scary to people, faking real world events,
*  disasters, that sort of thing. But like, at the level of drama
*  or action movie or sci fi, you know, like, you need people to
*  look scared at times, you need to be able to put explosions
*  into the scene, you need people to sound angry in their voice
*  delivery or happy, you need them to be able to cry, argue with
*  each other, love each other, like the full range of human
*  emotion and visual expectation. Like, we need that as artists in
*  order to create effectively with these tools. So I think, like,
*  we're starting to see it, there's a delicate balance there.
*  I can understand, like why it's not there initially, but we're
*  spending so much time talking about what's in these data
*  sets, we don't really spend a lot of time talking about what
*  artists really need in order to like, get the full range of
*  capability out.
*  I think that's maybe a good place to transition to the last
*  thing I wanted to ask you guys about, which is just the broad
*  future of all this stuff. I mean, obviously, for context,
*  you know, we've got multiple Hollywood strikes going on right
*  now, writers and actors. And in general, people are, you know,
*  kind of expecting a lot of disruption in this space. I
*  think, you know, you could look at that from the standpoint of
*  production, you know, what roles, you know, become more or
*  less important, how does the mix of jobs change? How do the
*  budgets change? I think it's also really interesting to
*  consider, like, what gets created, you know, and how does
*  that change? I think an important point that our good
*  friend and CEO Alex always says is like, we just never would
*  have done this, you know, otherwise, right? Like, we
*  didn't have the budget to do the traditional production and
*  never would have dreamed of it. So this is something that just
*  simply could not and would not have existed before. And that's
*  an important, you know, an additional layer to bring to the
*  whole thing, because it's not just about the way things are
*  produced changing, but also what can be produced changing. But
*  there's just so many different, you know, fallouts from this
*  economic, cultural, you know, atomization, perhaps of people
*  kind of falling into their own. I mean, we're already, you
*  know, very concerned about echo chambers and information silos
*  and, you know, algorithms, you know, curating content just for
*  you in a way that, you know, may or may not always be healthy.
*  But it seems like there's also, you know, a lot of potential for
*  things to be created, you know, just for you in the future. So
*  how you know, you guys have been really at the forefront of this.
*  And I wonder what, you know, if you try to peek around the
*  corner, you know, beyond frost two, you know, but kind of
*  extrapolating that to three, four or five. But where do you
*  think this goes? Or can you even, you know, predict that at
*  this point?
*  I mean, a few things there. We did this for fun. You know,
*  we're not a film production company. We're a technology
*  company at Weymark. We're, you know, our mission is fundamentally
*  about people being able to make their own commercial. You know,
*  so we were able to pursue this project really as a luxurious
*  byproduct of the fact that we're out there kind of looking at new
*  tech on behalf of our customers and trying to figure out what
*  the best ways are there are for us to like incorporate this
*  stuff and be the best practitioners we can so that, you
*  know, when we do have times where we need to like construct
*  a prompt or something in our own workflow, in the case of our
*  customers, we know how best to do that. Right. So this is
*  really about us kind of understanding what's possible.
*  And that's really like what got us to the frost and what gives
*  us this kind of fun area to play in. That said, like, because
*  this is fun, because this is not for profit, because this is
*  kind of just, you know, to share and hopefully share a lot of
*  knowledge as well about, you know, the creation and the
*  process. You know, my own opinion is just kind of like, I
*  think there's still room for a lot of things. There's still
*  kind of like room for all of us. You know, the tech is certainly
*  going to transform roles. It's going to create a lot of new,
*  cool and interesting roles that we haven't thought of yet. It's
*  going to enable, you know, much, much smaller groups of people
*  the pursuit of these projects. You know, I would like to think
*  of that as a lot of people without means previously to
*  become filmmakers or do things creatively or, you know, going
*  to have the capability to do that very, very soon. And I think
*  that is a very exciting idea. I also think some jobs are going
*  to go away. Certainly, that's kind of just the reality of
*  technology in our world that's kind of couched at the level of
*  artists. I don't necessarily think I buy into that argument
*  so much. I think like, yeah, maybe if you have only one
*  modality of art creation and you never plan on expanding that or
*  trying something new, then okay, like that, you know, there's
*  going to be issues for you down the road. But if you embrace
*  these tools and think about, you know, the use of them in your
*  own workflow, I think just about every artist can find something
*  cool and find new paradigms and new possibilities for
*  themselves. I think like, you know, the ability to fine tune
*  now in AI on your own work, if I were, you know, an individual
*  fine artist who maybe hasn't given this a shot yet or hasn't
*  really thought about it, the idea to go fine tune on your own
*  work and then kind of explore with the AI within the sort of
*  realm of what you're already doing sounds like a very new and
*  exciting thing for me to think about. Also, you know, when we
*  prompt for things like a specific artist or a specific
*  production type, we're only kind of getting an amalgam from the
*  AI that's based off of, you know, a myriad of things that
*  seen in the data set, we're getting results back that like
*  have an artist noted properly. We're also getting results where
*  an artist isn't noted properly. And so like really getting a
*  melange that like though it may say one artist like represents
*  any number of people and in the case of film like is
*  representing, you know, everyone from screenwriter to grip to
*  just armies of people untold that are represented there in
*  the data set but are not like equivalent to the artist's name
*  that someone might put into a prompt. So I think that is an
*  important thing for us to consider and then maybe to build
*  on, you know, like, I'm excited about the idea of, you know,
*  directors coming along and and authoring definitively a fine
*  tuning that other people in society can maybe purchase or
*  license the ability to use, you know, what they like, exactly
*  what they wanted the machine to understand their artist
*  thumbprint as and for people to be able to like mix and match
*  those definitively authored fine tunings with others. I think
*  that is a new kind of like, like economic explosion potential
*  that I'm really trying to talk about right now more openly and
*  be a big advocate for because I think that is maybe like a
*  healthy new world where artists and creators can intersect and
*  find a lot of benefit. And then last thing I'll say and then
*  I'll shut up is just that in terms of what I put out into the
*  world versus what I've created, I'm going to hit a million
*  images generated this year here in about two months running my
*  numbers. You know, I put out a small fraction of that into the
*  world in terms of what I let people see. That's okay with me.
*  I have my own like, worlds that explore I explore my own kind of
*  stories I enjoy by myself. And that is going to happen for a
*  lot of people in a lot of ways going forward. And I think we
*  can just kind of try to be a bit more understanding about that
*  and appreciate that for what it is.
*  That's a hot topic right now. I have friends and family in
*  Hollywood who are, you know, worried about this and ask me
*  about it all the time. So it's definitely controversial. I can
*  tell you from my experience that, you know, directing this
*  movie and, and trying to trying to see this production through.
*  This is not easy. This stuff, it was exceptionally hard, maybe
*  even harder than like a traditional animation. It just
*  because of there's just you're you're working with an unknown
*  artist in the room who can give you can give you exactly what
*  you want or can give you some random wonderfulness or some as
*  other people say grotesque image. And so it's a huge
*  challenge. And I do believe that like there are still going to
*  there's there needs to be a
*  in order for it to be good, I think, like a human vision,
*  there needs to be like, like a big 500 foot vision that a human
*  being has at least I'm talking about making a narrative film.
*  I don't know how far away we are from that. But from from where
*  the human being is not engaged at all. But
*  because right now you can't really just ask chat GPT to write
*  you a screenplay feed that screenplay into another AI. And
*  then all of a sudden you have a movie. It's not really how it
*  works. There's a lot of tweaking, there's a lot of human
*  conversations, there's a lot of, you know, critical thought that
*  needs to go into this thing. And so think it's, it's a great
*  tool. And it's improving every day. So, you know, 20 years from
*  now, 10 years from now, that might happen, you might, you
*  might be able to type in a prompt and, and, and get your
*  your ready made movie. But right now,
*  it's you still need, you still need the human to kind of be the
*  storyteller, in my opinion.
*  Well, the AI assisted enabled short film that you guys have
*  created is the frost. It has been reviewed all over the place
*  on the internet, you can watch it on YouTube, and we will
*  certainly be keeping an eye out for the frost to with a whole
*  range of new techniques and look forward to continuing to follow
*  your work as you guys continue to pioneer what it means to
*  create truly high level content with AI. This has been a ton of
*  fun guys, Josh Rubin and Stephen Parker. Thank you for being part
*  of the cognitive revolution. It is both energizing and
*  enlightening to hear why people listen and learn what they value
*  about the show. So please don't hesitate to reach out via email
*  at tcr at turpentine.co or you can DM me on the social media
*  platform of your choice. I'm going to key uses generative AI
*  to enable you to launch hundreds of thousands of ad iterations
*  that actually work customized across all platforms with a
*  click of a button. I believe in Omniki so much that I invested
*  in it, and I recommend you use it to use cog rev to get a 10%
*  discount.

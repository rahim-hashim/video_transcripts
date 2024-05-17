---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 3581s
Video Keywords: []
Video Views: 1790
Video Rating: None
---

# The AI Copilot Revolution with Div Garg of MULTI·ON
**Cognitive Revolution "How AI Changes Everything":** [July 13, 2023](https://www.youtube.com/watch?v=PR2Mdlx5eik)
*  We want to unlock parallelism for humanity where like currently you can imagine like we are all single threaded.
*  We can do only one task at a time.
*  But if we could have AI, we could launch like maybe like, I don't know, like a hundred AI agents at a time, all the AI agents do the work and then tell you like, oh yeah, this work is done.
*  And then you can like sort of like coordinate that.
*  And in the core, I believe like you need to have some sort of tenants if you want to build really intelligent AI agents.
*  And one of them should be like, an agent should not be able to modify its own source code.
*  Because if it's able to modify its source code, then it could like self evolve, it could do like really weird things.
*  I don't think GPT-4 is there yet when it comes to a lot of really complex reasoning.
*  And so you might need some like big tools in the foundation model layer.
*  In a week, you have like 20 foundation models dropping and like, I don't know, like a hundred papers published.
*  So it's definitely the progress is crazy.
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers, entrepreneurs and builders working on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas and together we'll build a picture of how AI technology will transform work, life and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host, Eric Thornburg.
*  Hello and welcome back to the Cognitive Revolution.
*  My guest today is Div Garg, founder of Multion, the world's first personal AI agent and life co-pilot.
*  Until recently, Div was a PhD student and adjunct faculty at Stanford, where he created and taught a class called Transformers United, which explored how the revolutionary transformer architecture is already beginning to unite such previously disparate fields as natural language processing, computer vision, biology, and much more.
*  Now, because he believes that AI agents will become one of the most important parts of the AI technology wave, Div has taken leave of the PhD program, raised venture capital and is currently building the Multion team so that people no longer have to browse the web alone.
*  This is our third show about AI agents and I'm really struck by how different the product and rollout strategies seem to be.
*  Flo Crivello, the CEO of Lindy, often posts images of intricate workflow automations that Lindy has created for him based on detailed prompts.
*  Matt Welch, the CEO of Fixie, has launched a public facing agent platform as a playground for developers, but is really targeting enterprise customers.
*  And Div, with Multion, has wrapped an AI agent up in a Chrome extension so that users can easily delegate tasks to it, can watch what it's doing and supervise along the way, and can even assist in real time, as necessary.
*  The AI agent space is fascinating and in my view it really does merit a diversity of approaches.
*  Each strategy, of course, has its own strengths and weaknesses and time will tell which one ultimately wins out.
*  But after testing a bit over the last couple of weeks, I can say that Multion is really fun to use.
*  Watching it navigate the web, explain its reasoning, and attempt to move forward toward whatever goal you gave it, really does feel like a glimpse of the AI powered future.
*  In this conversation, we talk about Multion's product strategy and roadmap, their natural language approach to skills for Multion, Div's vision for how AI agents will impact human work,
*  the steps that they're taking to ensure user safety, the standards of reliability that Div believes Multion will need to achieve to see mass adoption, and lots more along the way.
*  I really loved Div's tremendous energy and positivity and I found this conversation extremely interesting.
*  If you agree, as always, we'd appreciate it if you'd give us a review on Apple or Spotify, leave a comment on YouTube, or simply share the show with friends.
*  If you have any feedback or suggestions, you can reach us by email at tcr at turpentine.co or DM me on Twitter where I am at LeBenz.
*  Now, I hope you enjoyed this conversation with Div Garg of Multion. Div Garg, welcome to the cognitive revolution.
*  Yeah, happy to be here.
*  I'm excited to talk to you. So you are the founder of the AGI company, Inc., also known as Multion, which is online for limited users for now at multion.ai.
*  And, you know, from what I understand, you have left the comfortable environment of a Stanford PhD in machine learning and thrown yourself into the incredibly turbulent waters of trying to build an AI agent startup in the midst of, you know, one of the craziest technology environments ever.
*  So to get started, tell us a little bit about that.
*  So definitely, I would say like this seems to be the right time to go and like start building AI applications and agents. And I think the best startups have gone during like, almost like you have a very big technology revolution happening.
*  There's a lot of turbulence, a lot of players are getting like shift upshifter. And I would say like, this is still early enough where we want to go and like sort of start building AI applications that can be useful in everyday life.
*  So I would say like, I still think like agents are still early, but this is the right time to like go start building them as a startup and start solving the problems there. And even if it takes you like, say like five years or like more, I think this is the right time to like start building and like tinkering with them and solving them as like a problem.
*  Yeah, definitely. If you wait until it's easy, then it's definitely too late to, you know, be in on the ground floor of the value creation. So that definitely makes sense. I want to get into a lot of detail about how it works and all that kind of stuff. But what's up with how did you come up with the incorporated name of the AGI company, Inc. And where does the name multi on come from?
*  Sure, sure. So that's a good question. The AGI company was just like, it was really funny. So I was checking online, is this a name that's available? And I was actually surprised like this is a name available. So I went and registered it. And so we're not actively using that name for now. We're also, we just like using multi on. Maybe we will like start using it in the future. Maybe we can spin up a nonprofit or something.
*  The nonprofit controlled startup is all the rage these days. So what about multi on? Where does that come from as a name?
*  Yes, yes. So I would say, yeah, so this is like, I would say I have a physics background. I did some like international physics on here. It's back in the day. And the name is actually inspired by like a hypothetical like quantum particle that's present at every place at the same time. So it's like if you have like some like neutron, muon, fermions, like multi on.
*  Fascinating. Okay, I blind spot for me. I didn't even make the connection. For me, it meant just like something that was on in multiple ways, I guess. I don't know. I was kind of thinking of it as my you know, my AI assistant that's always on or something like that.
*  Yeah, I think people think of it too.
*  How are you thinking about that for you?
*  And the field is moving very fast. So it's definitely hard to consolidate the research with the product because all the iteration cycles are really fast. And even like in a week, you have like 20 foundation models dropping and like, I don't know, like 100 papers published. So it's definitely the progress is crazy.
*  For us, I think like the nice thing is, we really like the open source community. And like we see that as like a way where we can like bootstrap on top of developments there, as well as like do collaborations to sort of like, like take the best approaches and like pull in to what we are doing as an agency company.
*  What's the status of the company right now? I noticed that you have put out the call for hiring, but I haven't seen any fundraising announcements. So is that would you like to break any news here on the cognitive revolution?
*  Sure, sure. So we are in the middle of a seed race. We have got some really good term sheets. And also you'll see an announcement in like maybe a few weeks. So can't disclose yet.
*  Cool. We'll keep an eye out for that. But I would not doubt that you would have any trouble raising a few million bucks in a seed round at least. So watch this space, everybody. So what roles are you looking for? What is kind of your, I assume it's multiple things. And obviously, it's like people who are obsessed with AI, but anything in particular that you are in need of right now?
*  Sure. So I would say like in general, we are focused on hiring journalists at our current stage. And I think like we're focusing on hiring people who are really passionate about AI and agents. And they can like basically define the culture of the company as we grow and like build it up. And I think we're looking for everyone from like hardcore full-stack folks to backend engineers to AI specialists, even like research engineers. And I think we want to solve like agents as like both of our AI research problem as well as a product problem. Okay, like what's it like UI, UX?
*  How do we build into a product that everyone can use, make it reliable? And they're also like really useful and interactive.
*  Ian, I'm having flashbacks to our, my conversation with Arvind from Perplexity, who has a pretty similar background in multiple ways, including like having spent, you know, serious time in research. And also just the fact that, you know, they have set a very high bar for how fast they ship.
*  And I see you guys also shipping very quickly, you know, very short time between iterations. So that's a high compliment actually in my mind. Where do you think we are right now in this agent development? Do you think that the product is already useful or still just kind of a hobbyist thing? What is the path to actual like agent based utility?
*  Definitely. So I think that's a good question. So I would say for most agents, you will see like say AutoGPT or BPHR, even like a lot of like coding like agents. They're very early, like you can use them for very simple applications. For multi-unit, I would say we are like a bit further higher in terms of like you have actual applicability currently where you can ask people to say like online shop for you, read dinner, like book flights, so on. I think like the biggest thing we're trying to solve is like how do we make it really reliable? And how do we reduce the variance of like the value of the product? And I think that's a good question.
*  So I think like we are trying to solve that problem. So I think like a lot of the problems are like making it really reliable and making it very predictable. And those are the problems we're trying to focus on currently.
*  So let's get into then a little bit how it works. The first thing that seems like a actually huge decision point is when you're creating an AI agent product, and I've, you know, sampled a demo to at least like a number of them at this point, is kind of at what level does this thing operate in the first place? We've seen, you know, a couple different paradigms designed there where, you know, sometimes it's like it works all in the cloud, and you kind of, you know, define
*  some little agent to do some little thing in some platform. That's, you know, a probably not super flattering description of some of the things I've tried, but you know, that's, it's, it's executing over there somewhere, you know, far from you. Then there's like the OS level co-pilot concept. And then there's what you've chosen, which is the browser extension, ride along kind of co-pilot.
*  Mode. How did you choose that? What do you see as the big pros and cons? I have some thoughts, but I want to hear yours.
*  Sure, definitely. So then the biggest, like one choice you made this is to make it like really seamless in terms of user experience, and also like optimism distribution. And so currently, like if you go to the Chrome Web Store, it's like a one click install. Once you install, like that's it.
*  That's all you need. And if you want to sign up and make an account for us, you can start using Multimedia. And in your current browser, it has access to your like current logins. Like you can use it on any website you are authorized to.
*  So that makes it like seamless and very easy to get started. And that's one of the reasons we chose to make the choice. I would say another advantage is if something goes wrong or the agent is confused, it can simply ask the user for help.
*  So it's like, oh, it can ask like say, can you log into this website? Can you solve this capture for me, for example? And that gives you like a lot of like very like immediate interaction to the user where like the agent can correct it.
*  And so the user can correct the agent and we can use that as like a feedback loop, which we can like find in the agent on to improve it for future interactions.
*  I think, you know, to now share my perspective, I think this is a pretty smart approach. I could see an OS level approach, you know, kind of having some similar advantages.
*  But the fact that I'm logged into everything in my browser and that you kind of get that for free by adding on a browser extension that acts in the same space as I do as a human user, that even if it's not like the final form of this long term, definitely feels like a really good place to get started.
*  And in my testing of it, I've kind of experienced that where it's like, oh my God, you know, this morning, for example, I was on the other phone with a teammate. I wanted to add him to a GitHub repository.
*  So I just tried it with I'm going to say it's the first thing how you say it multi on and you know, so I pull up the new tab and I just say like, go I asked him what's your GitHub username and I said, okay, go to this repo and add this user.
*  And right off the bat, it's like other paradigms, you know, I'm immediately stuck with authentication.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  I'm going to key uses generative AI to enable you to launch hundreds of thousands of ad iterations that actually work customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it and I recommend you use it to use cog rev to get a 10% discount.
*  And, you know, anybody who has, you know, had to go authorize some, you know, temporary, whatever special purpose key out of GitHub, you know, I'm immediately like, oh God, I have to go do that, you know, and I have to do that for everything I want to connect or oh yeah, this, you know, that really bogs down.
*  I kind of always say access is always the hardest part.
*  So that's really tough. But with this, it just allows you know the AI to kind of ride in the same space as me.
*  I'm not watching it, it navigates to my thing, it, you know, was able to find going to the team page, it was able to search, you know, go pull up the add a collaborator, it was able to search for the guy's username and find him.
*  And then I did experience also what you were saying around kind of my ability to intervene and like help it if I need to, which obviously is like, not the long term product vision, but there was a step where it was kind of getting confused where it had like found the guy in the search results, but it needed to click before it could actually click invite.
*  And it wasn't quite, you know, clicking the click to get to the invite click to be accessible. And so it was kind of stuck. But then I just clicked the thing. And, you know, I think this kind of gets to my next question of like, the model seems to be sort of a, you know, just kind of a simple loop, right, where I injected my little action and changed the state space.
*  And then as it kind of took the next read of the space, it was like, oh, now I'm able to proceed. Because you know, something kind of just got easier for me or whatever, something happened good. And now I can, you know, my barrier has been removed, it kind of just continued on.
*  So I think that paradigm is super, super interesting. One question I do have, does it have the ability to interact with other extensions? Like I have LastPass. How does that relate? I haven't quite figured that part out yet.
*  Yeah, I'll definitely say like, this is also funny, like for that use case, I've actually used it for similar like use cases like adding like people to GitHub. I've also used it for like sending like, like DocuSign stuff is actually pretty good. Like I can say like send this like whatever contact to someone can actually go and do that whole thing.
*  And also the ability to like, interject, I think that's great. And then we can use that as like fine tuning samples to improve the ability to on the road. So we're actually building this like, like a recorder mode where like you can like sort of teach it like give it a demo like, oh, maybe this is how you should do it.
*  And if you just show some query, maybe one or two times, then it will know exactly what's the best way to do it. And I was slightly explaining on this like, one thing I've noticed is like, if any agent, it's doing something for the first time, it might take a longer roundabout path.
*  But if you can like sort of like give it some sort of like feedback or demonstration, it can like learn the shortest path. And I think that helps a lot. And that's sort of the approach we are trying to take to improve performance over time.
*  And just answer the second one. Yeah, it's like definitely like, like ability to like interact with other extensions is like, plus we are trying to explore. So for example, like for passwords, like one password has an API. So we are building an integration with the password API, and also other extensions.
*  And so this is a work in progress where we can interact with a lot of existing browser solutions to simplify the flows. Currently, multi-on can also use Honey, for example. So if you're on Amazon and you want to check out, and if you see like there's a Honey coupon, you can apply and the agent can go and actually just apply the coupon for you and like get you a discount.
*  Cool, interesting. So the core architecture, if I, I'm kind of guessing, and you can, you know, tell me where I'm right or wrong and share as much additional details you want to. But in kind of keeping with the paradigm of like working from a sort of research foundation into product, it seems like the kind of initial core of it is essentially a react paradigm where you're looping through and kind of each cycle you are working through.
*  And then you are taking kind of a snapshot of like, first of all, what goal have I been given? What is the current state of affairs that I'm looking at? There's this kind of interesting and we can share some videos to accompany this kind of little chat that isn't so much.
*  So it's kind of a chat, you can chat with it if you need to along the way, but a lot of times it's just telling you what it's thinking and what it's going to do. And then there's the actual action. So that's kind of the baseline react, you know, research paper. It seems like then now you're you're starting to be interested to hear if there's any, you know, major deviations from that. But I know like the next big thing too is then layering on the skills component to that.
*  Definitely. Yeah, so I think on high level that's very correct. That's what you're doing. I would say like, we have like three parts of the system. So one is we have like our representations or models, where we take the DOM and make it into like the compact text and
*  which we can give it like a like a planner model, which is like a GPT-4 or some other similar element that can build on the task and find out what are the right actions to take for this particular task. And then we can do something similar to a react paradigm where we have an inner thought and the agent can decide based on the objective, okay, what is the right thing to do? And then like similar to the right actions.
*  We also have our own intermediate action grammar and that action grammar helps a lot where instead of like directly generating JavaScript code, we like generate like commands in our own action like language. And this has the ability where we can like type check them, we can verify everything safe.
*  There's no like malicious activity, there's no prompt injection, for instance. And after we have verified that, we can compile that from action grammar to actual DOM level events for the website. And we have found that this helps generalization a lot.
*  Compared to just like code. And for the agent, I will say we use some very interesting tricks. So if you have something like Auto GPT or Baby AGI, for example, the biggest issue they have is like they have this thing called almost like task divergence, where if you give them an original objective, they will like diverge away from it and don't know how to like
*  And for us, I think the way we have formulated the problem is we tell the agent to always try to reach like come as close to the original objective as possible. And we basically give this like in a prompt like never give up, like always try to go as close to possible. So I would say like, yes, like the never give up is like something that helps a lot.
*  Yeah, it's the psychology component of language, the positive self talk or the need for grit. Grit is me language model grit is kind of what you're trying to to coax out of it. So it sounds like there are a couple of expanding on this kind of core react concept.
*  concept. There it sounds like our specialist modules that wasn't clear to me if these are like language model powered or just explicit code, because you could kind of imagine doing either right if you have a Dom Lord knows like Dom's are terrible, you know, ginormous messes these days, you know, long gone are the days of like highly semantic HTML, unfortunately, no such luck, you know, for us these days. So you could imagine.
*  Just writing kind of classic code to try to compress that you could also imagine having a like specialist, let either you know specialist 3.5 turbo or Claude instant prompt or even a fully you know fine tune specialist model to help understand the HTML. What do you what do you find there is kind of working or how do you see that evolving?
*  Yeah, so I think it's very interesting. So for the representation side, like I will say, we have three modules, so like a representation module, like a planner module, and like the actual action module.
*  And initially we started everything except the planner was like, maybe just like low level like, like, like more like heuristic code, and I'll be transitioning everything to a model. So on the representation side, we like can take a combination of the screenshot plus like, like the Dom, and we can have embeddings from the Dom and we can have embeddings from the image.
*  And then we can feed it to like a like a representation model that can combine them together. And this is similar to maybe like what something like instruct blip does get like a combined representation, which could be in this case we have made a choice of making it like text space so it's easy to analyze, it's easy to like see what's happening.
*  And then we can give that as a prompt to the planner model. Like this is like the state representation. And this is a user query, what should we do next. And once the planner can make like, okay, this is how the sub task we need to accomplish, we can like feed that to the action layer.
*  Yeah, okay. Very interesting. So is it.
*  You've got kind of a joint, a joint vision text representation.
*  And it's a, we've had the blip authors actually on the, on the show and an early episode but it was before instruct blip.
*  But I'm affiliated with that as well. That ultimately caches out though to a text output right in the end of kind of the representation it's it's a semantic representation, where you would be clicking on like, oh, I mean I guess then when the action
*  module is going to act, it's acting on a semantic action space so it's like saying click this button, not click at, you know, coordinates 100 200.
*  Yeah, so I'll say it's still a semantic representation.
*  And we can give like IDs to each element, and then like predict which ID to choose. And that helps a lot.
*  We can also, we haven't seen the need for actual coordinates.
*  But that can also be choice if you want to move the cursor to an exact coordinate.
*  You could also potentially predict the coordinate to move it to and then make a choice there. Yeah, it's all kind of on the table. Once once the, the modal barriers are broken down, you know everything kind of starts to become possible.
*  So, GPT four you kind of said, you know, or similar for the central planning model.
*  Does that in practice mean like GPT four today or is there any, in my experience like for these kinds of executive planning long range planning type tasks.
*  GPT four is kind of in a league of its own. Is that what you found also. Yeah, I'll say like, when it comes to like long term reasoning and like planning capabilities we have found GPT four to be the best.
*  We have experimented with like, like, like open source models like cloud 100k. And what we're in the process is like we have collected a lot of like interaction data so we already have like 50,000 like web interaction samples, and we are like starting to fine tune our own like
*  models so we can find in a Falcon 4DB model, and we're starting to do that. And pretty soon we could potentially transition to all in house models.
*  And the nice thing here is like the approach we're taking is where we are launching the product, getting data, improving the product over time using the data. And then, and then I saw like collecting more data and improving it.
*  And so we've seen like this is something that can give you a feedback loop where you can collect like the data that matters the most to the user, and improve the model there and I continuously like build this like loop like continuously get improvements.
*  And like I was like almost no one is going to be doing that so this gives us like an interesting advantage in this space.
*  Well it's a little tricky to necessarily define right because one in my red teaming with GPT four back in the fall of last year. One of the things I really tried to explore and certainly not as deeply as you have but is this kind of self delegation, you know concept
*  can GPT four like break problems down. I use the more kind of recursive structure, I guess inspired by, you know, some do more thought of recursive self improvement I kind of went toward recursive delegation, which I don't think now is like really probably the right
*  I'm to build a product around but you know I was just kind of doing my own messing around. I found that one really hard thing though was, how do I actually know if I've succeeded, you know for a given task and I was even just doing you know some pretty basic tasks like go online find some information.
*  And then I tried to create my sort of validation layer on top. But I found that for many many things, it was pretty hard to determine if I'd actually succeeded or not so are you detecting success or failure like automatically or is the, you know, are you to some degree relying on the user to kind of tell you when it worked or didn't work.
*  I would say in our case we are relying. It's like automatic.
*  So the model is able to predict whether it has fulfilled the task or not.
*  And we also are experimenting with a separate critic module where the critic could say like oh, like is this task complete for this particular objective, even the current set of actions.
*  And I think even for Voyager I think they took a similar approach, and I've seen this to be pretty reliable in practice.
*  So that seems like yeah some things will lend itself better to that than others. One of your videos that I've seen was the world's first AI booked flight.
*  And I guess for one thing you could kind of determine like, is a flight booked or not, you know, if you ever get to a success message that has like a confirmation code, then, you know, it's pretty safe to say you've booked something.
*  You could still have some questions around like, did I actually book what the user wanted me to book?
*  And there's, you know, varying degrees of rightness on that too. Like, did I take them to the right city? You know, is it the right, did I get the right flight given the options? Did I book the right seat? I mean, you know, did I get their traveler number in there?
*  You have this feature too of like your profile, which I haven't explored in depth yet, but you know, I also, I'm interested in your thoughts on kind of the future of memory.
*  But right now you kind of big text box, put your profile here, say, you know, tell us who you are. And then presumably the future of that is like more elaborate, you know, kind of memory systems on a per user basis as well.
*  But so I tried something else. I'm throwing a lot at you can kind of unpack this at length, but I tried something the other day where I was like, go get me my three, find the URLs for my three most liked LinkedIn posts.
*  And it got as far as my feed. And so it was like doing okay. But then it never actually gave me back like here are three URLs. And I wasn't quite sure like, did it already think it had succeeded by kind of getting there?
*  Or, I don't know exactly what happened. I'm not sure how you would even determine if you were successful. You know, here are three URLs, but are they, you know, the most liked URLs? How do you think about that? Kind of, you know, it's tough to ground some of these, these tasks, right?
*  Yeah, I think that is, yeah, that's a good point. Because I suppose even if you complete a task, it's possible like you completed the task like wrong. So maybe you booked the wrong pet, for example, or ordered something wrong. And I think that's also a concept of failure from our standpoint.
*  It's hard to detect because like the agent might just think like it's doing the right thing, and it has successfully completed the task. And in this case, I think we found like if you have a separate agent that is just like a critic agent or a validation agent,
*  that can help a lot. And at each point, it can verify, oh, like, is this the right thing, corresponding to the right thing, what the user's original like, query or objective was. And we can make a feedback loop there where the critic agent can like criticize any decision and give it as a correction to the, to sort of like the agent actor model.
*  So this is something we have played with. Second thing we can also do is we can have a user sort of like, like acknowledgement flow, where like you can put something in your cart, or like maybe like go all the way to the checkout for a flight. But before pressing the buy button, it will like ask the user like, okay, like I found this flight, can send you a screenshot. Do you want me to like choose this file? Do you want a different one? And if the user says yes, then you can go and proceed to actually complete the whole thing. And this is also one way where we can like make it safe. And if you want to go and complete the whole thing, you can go and complete the whole thing. And if you want to go and complete the whole thing, you can go and complete the whole thing. And if you want to go and complete the whole thing, you can go and complete the whole thing. And if you want to go and complete the whole thing, you can go and complete the whole thing. And if you
*  want to make sure like you don't accidentally made it make up end up making the wrong purchase, for example.
*  Yeah, that makes a lot of sense. How do you envision that kind of maturing? You know, in the obviously like early kind of demo era of the product? I largely just watch it right. So I kind of have the fun is doing the, you know, riding along and seeing what it does and what it gets
*  right and doesn't and, you know, helping it get over a little humps with my, you
*  know, extra injected click and you're not recording that now, but there is the kind
*  of a mode that you're developing where you will start to record those manual
*  interventions.
*  Definitely.
*  Um, yeah.
*  So I think like one is like, just like recording interventions and you can use
*  that as like, um, like the next time it really would like to just learn it.
*  And, um, and like, we'll like remember like the interventions and what sort of
*  corrections you get and improve its behavior automatically.
*  And we can do like in context learning for this, we can also do fine
*  tuning, uh, or the model where once we collect a lot of like this sort of
*  interventions from like, uh, a lot of our users, we can like find in the model
*  to improve the performance, um, where it's currently not working.
*  Is the vision sort of to have a, like, I set something off on it, on a task.
*  And then I kind of go do my own thing.
*  And then maybe I get like a notification, you know, three minutes later.
*  That's like multi on is ready to have you review, you know, before
*  purchase or whatever.
*  Yes.
*  So I think, yeah.
*  Um, I would say we have a lot of things planned, uh, down the pipeline, but in a
*  high level, you can think like, suppose you want to make it say, order a burger
*  near you, for example.
*  And so maybe like the first time you ordered, you might want to watch and see
*  what's going, maybe if it doesn't, you know, can intervene, give it a correction.
*  And then you can maybe like play around with like two, three times, have some
*  fun, like sort of like guiding it, interacting with it.
*  Um, and once you know, it's like reliable enough, then you can just like
*  leave it in the background.
*  And, uh, when the agent is done, it will just send you a notification.
*  Okay.
*  I'm done.
*  It could also be like a mobile notification.
*  You can be anywhere, uh, like my town will be able to run in the cloud.
*  So you can be like, uh, like just like be anywhere.
*  You can say like, Oh, like, get me a burger.
*  Um, it will turn on the cloud, do the task for you and send you a notification,
*  which could be like, okay, like I found this thing, um, potentially along with
*  the screenshot and then you can like acknowledge, um, whether to like finish
*  the task or to actually get the, like say the burger in this case, or do you
*  want it to like cancel it or do something else?
*  How does that cloud mode relate to off?
*  Cause I'm imagining like a headless browser in the cloud or whatever, where
*  I'm not logged in to, you know, all my accounts.
*  Yes.
*  Uh, that's an interesting question.
*  I would say we are working on a lot of things.
*  Uh, but I feel like we have cracked this problem and there it's too early to
*  like say like, uh, uh, like how exactly we're doing, but I think we have a
*  really like a nice and elegant way to like sort of like solve the art issue.
*  Cool.
*  Well, that's a, that's a genuine breakthrough.
*  Uh, if you could make that work smoothly, it is a huge selling point for so many
*  of these experiences right now.
*  So then tell me about the memory side.
*  So you've got, uh, I understand.
*  Okay.
*  We've got, for one thing, my kind of profile, which I can currently like
*  just manually manage and, you know, tell it, you know, my name is Nathan
*  and my emails, this and my, you know, I prefer a window seat, whatever.
*  And then you also have kind of seemingly system level memory that is like the
*  skills, and again, this is kind of, you know, close follow as I understand it
*  on research progress, where was it even a month ago yet that, um, I think this
*  is an Nvidia project, right?
*  The Voyager project of, I referred to this as the LLMs as lifelong learners
*  where they're going out and doing stuff in this, in the Voyager case, it's
*  Minecraft, figuring out how to do stuff successfully and then storing
*  these successful subroutines.
*  Your skills though, as I've seen them are like way higher level, more to like
*  natural language than the Voyager skills, which were like very granular kind of
*  Minecraft execution code from what I've seen of your skills, it's like a sort of
*  note card length, highly, you know, abstracted away from all that detail
*  kind of summary of like what it is you're trying to do and roughly how to do it.
*  So help me understand that a little bit better.
*  I'm a little, I guess my surprise there is I, I wouldn't expect that it would be
*  the high level thing that the, that the agent would need as much, you know, I
*  would, when I talk to GPT-4 and I say, how do you go book a flight?
*  It's kind of like, well, you go to kayak and you search for stuff and it seems
*  like it kind of knows the general direction, but then it really gets bogged
*  down in low level details.
*  So I guess I'm a little surprised that the skills are so high level or maybe
*  I'm missing something so enlighten me.
*  Sure, sure, sure.
*  Uh, like I'll start with the memory part first.
*  Um, so the memory, I think the current feature we have is like, it's like a
*  scratch pen and so this is almost like having like extending notes with your
*  agent where you can like say like, oh, this is my personal details.
*  I want, this is what I like.
*  This is what I don't like.
*  There's my zoom link.
*  You can give it instructions like, okay, like always like add zoom links to my
*  calendar invites, for example, or like, don't do this thing, whatever.
*  And it can like remember that as like embeddings and like account for
*  preferences, like, so this is like more like explicitly you give like some
*  preferences to the model and, um, we're trying to make this like really secure.
*  So like you can store your credit cards there if you want, you can store
*  passwords there and we're going to do everything as client side, it's private
*  and secure.
*  Um, so that's built like a, like a secure way to like give information, uh, to
*  the agent.
*  So this is a second layer we're building is I would say more like, um, interactive
*  memory where like, when you interact with the agents, it will like actively
*  learn preferences over time.
*  So like the first time you say, say order a burger near me, it might ask you
*  like, okay, what's your address?
*  And once you tell it your address, it can remember that and use that, um, as
*  like a long-term memory in the future.
*  Um, so if we say something like next, like, okay, like find me, um, like a
*  haircut place nearby, it can like, okay, it now knows your location and can
*  customize and so over time, like the more you use it, the more it will learn about
*  your preferences.
*  And so this is a layer we are currently building, uh, which we call it, which
*  we are calling as a personalization, uh, to the end user.
*  And I think that's a lot very interesting.
*  Um, and like, there's a lot of things you can do there.
*  Um, and coming to the second point around skills.
*  Yeah, I think, yeah, it's interesting.
*  Like the choice you made around skills is to keep them high level.
*  Like how we're thinking about skills is almost like, you can think what the
*  agent currently does is like, it goes from natural language instructions to each
*  single line of code, uh, or like actions in a sense.
*  So it's like, uh, for each natural language, pretty say, okay, like, okay,
*  like I take this action for then second action, her action, whatever.
*  So it's a basically like each line of that, uh, action put, and what we want to
*  do is instead of breaking like each line of the actions, we want to break like
*  high level action functions in a sense.
*  Um, and this can be like sort of like almost like skills where we say, um,
*  maybe like send, uh, maybe like follow someone on Twitter, for example.
*  So you could have some sort of like, say like a function that's defined, that's
*  like follow, uh, on Twitter can take an input, which would be user ID and it
*  already knows, okay, what are the actions that are needed for this function?
*  Uh, that, and, and then, and in that case, like, instead of like predicting each
*  line of, uh, like action code, you very basically like choose like the action
*  functions and like, uh, combine them together.
*  Uh, so that's how we're sort of thinking about skills and the current skills are
*  also a combination of scripting and natural language.
*  So they, they're very high level and the choice we have made because of this is
*  like, anyone can go and develop their own skills that they want to.
*  So if you want to develop your own customized workflow, or you want to give
*  it like some sort of personality where you want to make it act like a recruiter
*  on LinkedIn, or you want it to like, say like act like a, uh, uh, socially, like,
*  like a social influencer, for instance, you can make a skill around that, uh,
*  all in natural language and like feed it to the, uh, agent.
*  And we're trying to develop a whole ecosystem around it where we can have a
*  directory where people can go and afford skills, share skills with each other.
*  And like the agent can pull in the best tool automatically for each share website.
*  And I think this can allow like the agent to improve really fast and people
*  to also like, uh, contribute, uh, to the agent.
*  And so, yeah, so I would say in a sense, uh, yeah, that's what we're trying to do.
*  And we have seen like high level instructions actually work really well.
*  It's almost like if you are a teacher and you're guiding the student, like
*  if the student makes a mistake and tell them, oh, you made this mistake, or
*  maybe like, this is something you can do better.
*  Um, maybe you should like click here to open this dropdown instead of
*  typing on the top down.
*  And if you can like give that instruction, um, that can help, uh,
*  improve the behavior of the agent.
*  It's almost like the skills are kind of additional kind of conceptual guidance
*  on things where it didn't immediately work, but you're trying to keep the
*  guidance high level enough that users can write their own without having to
*  get down to the like level of your action language, which I guess is, um,
*  you know, it's on some of those, maybe it's something you don't
*  necessarily want to share anyway.
*  Um, if that's a, you know, a key part of what, you know, what makes the whole thing go.
*  So, so that makes sense.
*  So there's not a skill is does not, is not stored as like actual procedure at all.
*  That's all still generated dynamically at runtime each time.
*  Uh, correctly.
*  Yes.
*  But what not so imagine this track to this is we could like, if you have the
*  natural language description of a skill, then we can have a model like generate
*  the actual like action code for that particular skill, uh, at the runtime.
*  And then we can also cache it.
*  So you don't have to next actually, uh, like to generate the action code each time.
*  You can just like refetch whatever's already generated and use it.
*  But for a user, they just need to define the natural language interaction and
*  another layer can go on the compile actual code.
*  Presumably though, you also have to have some input of like
*  current state for most of these skills, right?
*  Like to generate the actual action code, you're going to want to be responsive
*  to runtime conditions too.
*  How do you think about, um, drift, you know, there, there's just obviously,
*  you know, Twitter, uh, announces and launches updates on a unpredictable
*  schedule these days.
*  Uh, so just to take that one as a, uh, you know, a sample, I think these
*  things are often kind of forgotten and not states forgotten by you, but like,
*  you know, weekend hackathon type projects age really poorly when, you know,
*  all of a sudden it's like, yeah, but somebody made a tweet to their website
*  and now your whole thing doesn't work anymore.
*  How do you think about kind of keeping up with the ongoing evolution of things?
*  Or, you know, you've got a skill, but even at a semantic level, that skill
*  could be out of date if they change, you know, the flow.
*  So yeah, how do you think about that challenge?
*  Yeah.
*  So I think that's the beauty of keeping everything as a natural
*  language, um, high level instruction.
*  Um, so one is like, if, if that high level natural language instruction is still
*  correct, then we can dynamically recompile the skill, uh, to get sort of
*  the new action code and even if like something changes for the website, it's
*  very easy for anyone like a basically like who doesn't even have a technical
*  background, who just go and like change the, the high level language, um, into
*  like what is like now correct.
*  And then the, then we can like compile, recompile that to the actual action code.
*  Um, so I think it just like removes the technical barrier around actually
*  understanding a low level, like what are things that might be needed and anyone,
*  any sort of user can go and like, sort of like play around and like, uh, build
*  things on top.
*  How do you think about, so that also then makes me think, how do you think
*  about malicious skills?
*  You know, if I, if I imagine this kind of rolling out to a lot of users, I'm
*  interested also in your timelines on sort of, you know, at what point do you
*  think multi on goes wide because, you know, it's actually useful to non
*  hobbyist people I've been saying for a couple of months now, six months.
*  So basically from GPT for launch and the initial agent craze, I was like, give
*  them six months, you know, that'll probably bring us do around like.
*  October.
*  I'm interested to hear how you kind of think of when those things would
*  crystallize, but then as that also comes online and goes to scale now, you know,
*  if I'm aware of the, the fact that like, I can go in and semantically modify some
*  skills, you know, couldn't I just go in and modify a skill to be like, by the way
*  in the middle here, like Venmo, all your money to my, you know, uh, to my Venmo
*  handle.
*  And if you're already logged into Venmo, you know, those things are hard to, to
*  undo, right?
*  Like the Venmo probably doesn't have an established protocol for my agent did it.
*  And I didn't mean to, uh, I didn't mean to set all that money.
*  Can you help me out?
*  I think Venmo is going to kind of be confused by that.
*  So how do you think about, you know, just use your safety?
*  I mean, there's so many levels to that problem, but that's just one that's, you
*  know, jumping to the forefront of my mind.
*  Definitely.
*  So I would say that's one of the reasons we are in a closed beta where we have
*  the choice, but if you want to launch, we could just like launch basically everyone
*  by through the Chrome, like a web store, uh, using an extension.
*  Um, the reason we have like made the choice to keep our current like user best
*  small is to be able to make sure like everything is safe.
*  There's nothing malicious, but like, uh, like do like red teaming, uh, safety checks.
*  And, uh, and yeah, so this is like a very good point.
*  So in terms of launch, I will say we are planning a Stanford launch, uh, in the
*  next month, and so we'll start from there and like sort of see, okay, like how
*  do you watch our like user, uh, how are people using it?
*  How can we sort of make it more safe, uh, to keep it into the, in a closed sort
*  of like environment.
*  And then once we know, okay, like what are the considerations on the system to
*  improve it, we can do like a much finer launch.
*  And so we are thinking of this into like phases where we do like a small
*  launches first, and then we'll do a bigger launch after that.
*  Um, and this helps a lot with like security, a lot of the digreptic, like
*  making sure everything is safe because, uh, especially with like very general
*  web interaction agents like this, like if something goes wrong, that can cause a
*  very massive change action.
*  Um, and we might not be able to come and like stop it in time.
*  Um, so we want to make sure that we don't cause anything like that.
*  Um, and also like for skills, um, yeah, really good point.
*  Um, I would say like when it comes to choosing skills, we can like, maybe like
*  make a skill like protected or something like where it can't be modified by anyone.
*  So this is like, if this goes there, like it may be like only someone who has,
*  like some sort of a spatial access can go and change those skills or the agent
*  to be able to use them, or we can also do something like you can only change
*  individual skills.
*  So you can change me like, uh, skills that you define yourself, but you can
*  change someone else's skill for instance.
*  And so like the only person you will affect is yourself.
*  And so you won't be able to affect or create like malicious use for other users.
*  Um, yeah.
*  And I would say what you're more worried about is like prompt injection attacks,
*  where like people can just go and like hide prompts on websites and, uh, that
*  can cause like weird things where like someone can just go and like hide like a
*  crypto wallet link on a website and say like, distribute this crypto wallet to
*  everyone.
*  And so this is something that we are trying to be very like safe about.
*  Um, and we have a lot of tricks to make sure everything is safe.
*  One thing is because we can, uh, type check our action, like code in a sense
*  before we actually simulate it in the browser.
*  We can like make sure, okay, there was nothing malicious in this action code
*  that we have created.
*  Um, there's no sort of like red flags.
*  There's no privacy violations.
*  There's no nothing like, um, like hacking sort of like, uh, attempts happening.
*  And once we have verified it, then we can actually, uh, simulate those actions.
*  And that also obviously like, uh, adds like a great safety layer where we can
*  certify everything safe, um, before we do it.
*  Do you have an explicit sense of like how safe things need to be, to be deployed?
*  You know, people think about this in terms of like self-driving cars, you know,
*  and I think we're kind of irrational on that one in that it seems like until
*  it's clearly an order of magnitude safer than humans, it probably has no chance
*  of getting deployed and you know, to me, it seems like we maybe want to be a
*  little bit more aggressive than waiting for like full order of magnitude better,
*  you know, to start taking advantage of some of this stuff.
*  I don't even know what the baseline is for a product like multi-on, but how do
*  you think about how many, you know, people per million can have like, you
*  know, some adverse event, maybe that's not even the right way to think about it,
*  but it's a tough one.
*  Definitely.
*  So I would say like this, like, um, ways to think about this, one is just like
*  risk, if you're autonomous driving, like the risk is like you will basically kill
*  someone and then you need to be 99.999% like accurate in a sense, uh, if you want
*  to like reduce that risk, uh, when it comes to like a lot of web interaction,
*  the risk is much lower, especially in consumer settings.
*  In enterprise, I think the risk is higher.
*  That's why they're not like starting enterprise.
*  I would say like a lot of consumer use cases, like the risks are more like,
*  maybe you might send a wrong message to someone, maybe you might make a slightly
*  wrong purchase and a lot of this are like reversible, so you can like, uh,
*  written back order for instance, and you cancel things.
*  Even if you send it all wrong messages to someone, you can be like, Oh, sorry,
*  Matt, yeah, I messed up.
*  And it's actually really funny, uh, if you tell that to someone.
*  So then like, yeah, so it all depends on like, what's are the risky scenarios.
*  And like what we have done is like a blacklisted websites, which can be very
*  risky. So for example, like banking websites, for example, or other websites
*  where like it might be more like a sort of like a risk to the user and, and, and
*  like low risk settings, I think it's completely fine to just deploy it, have
*  people interact with it, um, and improve it over time.
*  And I think this is the approach we are trying to take with multi-on where, uh,
*  let people interact with it, have fun with that and like, uh, make it like
*  much better over time.
*  You know, you're doing a lot of kind of hard work on, it sounds like a lot of
*  cases, right?
*  I mean, the fact that you've already kind of got a blacklist for sites, like
*  there's a lot of little things like that, that presumably you are gradually
*  banging out and kind of sanding down all these rough edges.
*  But then there's also potentially just like more breakthrough changes, you
*  know, whether it's just foundation models get better, or maybe we see like
*  new foundation models specifically built for agents.
*  Uh, what do you think are going to be the big things that really unlock this?
*  And then, yeah, give me your timeline too, for like, when does this actually
*  become something where, you know, people that don't really care about AI for
*  intellectual reasons or curiosity reasons actually just use this because it's
*  better than, you know, using the internet browser themselves.
*  There's a lot of like, uh, hurdles around just like making sure the experience is
*  great.
*  Um, like finding the right combination of experience and engineering to make sure
*  people can like use this like, uh, reliably and have the best experience
*  possible.
*  And, um, yeah, I would say I think we, I think we'll be ready in terms of what we
*  need.
*  I think we are there at least for simple tasks, unless you want to do like
*  something like book me a one week trip to Italy, for example, like we are still
*  like far away from doing that.
*  But if you want to like, yeah, maybe like book me a flight to like Venice, for
*  example, on this particular day from this airport, this is something we can
*  already do.
*  Um, and then we can like make sure like we are doing this really reliably and
*  add verification checks.
*  Um, so yeah, so when it comes to like simple, like tasks like that, I think we
*  are mostly there, um, with some rough edges currently.
*  And I think in the next three months, I think you should be good where we can
*  like just give it to non-technical people, have them play around with it.
*  Like sort of like, uh, be like a browser companion or like try to change how
*  like people interact with the browsers.
*  Um, and when it comes to more complex tasks, I think that will take more time,
*  especially if it's like a very abstract, high level tasks.
*  I don't think GPT-4 is there yet, uh, when it comes to a lot of really complex
*  reasoning.
*  And so you might need some like, uh, big, uh, throughs in the foundation model
*  layer, where you can have it like too much more complex reasoning, uh, involving
*  maybe like 20 plus, uh, uh, steps, um, which it currently do.
*  What do you think about this for the kind of future of work?
*  So much of the stuff that people do, and, you know, I've mentioned to you offline
*  that I'm involved in, uh, AI advisory work with a friend's company, which is
*  in the executive assistant space.
*  And we're really trying to figure out like, how does a human EA relate to
*  these kinds of AI assistance?
*  I guess you said like, how far is far?
*  And that's kind of maybe one way to think about the question because today our
*  clients, you know, wouldn't really, they want to delegate all this stuff, right?
*  They want to delegate, book the thing at a high level and have it get done.
*  So they're probably not going to switch, you know, in the immediate or near-term
*  from working with a human who can handle that kind of task to an AI, which can
*  kind of take parts of it and accelerate bits of it, but can't really do the whole
*  thing.
*  Do you think that there is a, like, what is your expectation for that kind of
*  ever higher level sort of thing?
*  Like is, do you see this kind of leveling out, you know, S curving out to a place
*  where it's like, generally things kind of remain the same and this is sort of a
*  tool for assistance.
*  Do you see this kind of not leveling out and becoming, you know, something that
*  literally rivals, you know, human employees?
*  Where are we headed?
*  Yeah, that's a good question.
*  I would say initially, at least we think of ourselves more as like a supplementary
*  aid rather than a replacement for a lot of like current like assistance.
*  I would say like, if you are actually thinking like for a lot of our initial
*  users, they might actually be like prosumers or like assistants who want to simplify
*  their lives in terms of like, they're doing.
*  And so I think we will, I think we are currently more supplement maybe in the next
*  couple of years.
*  I think it's possible you have human level full capabilities, but I think we're still
*  a bit far ahead.
*  What I see is like the evolution from like humans actually doing everything themselves
*  to becoming more like organizers, where you can like instead of like booking, say like
*  going to calendars, booking all the meetings or like going to different websites for
*  ordering food on different restaurants, for example, or whatever booking flights.
*  If you're an EA, you could just go to Multion and the Multion will go and do the
*  whole thing. But you just become a coordinator for the system.
*  So you're like, oh, now do this, now do that.
*  And basically like Multion will do all the actual interactions, all the web
*  navigation stuff. But you become like the planner or the coordinator.
*  And I think that is something that we can still replace because I don't think
*  foundation models are there yet.
*  It might take a couple of years where they actually can do this really reliably
*  without failing. And I think like the great thing about that is like we simplify a
*  lot of like complex, very boring interactions where even for EA, the hard
*  thing about the lives is just like you just have to go and interact with 100
*  different services. And if you can just like remove that from the lives, I think we
*  can make and simplify a lot of like jobs and improve the quality of work.
*  How do you think about safety in the big picture of this?
*  Obviously, the, you know, AI safety debates have heated up tremendously in recent
*  months. And, you know, famously, some major thought leaders in the space have
*  signed on to the extinction risk statement.
*  It seems like the, you know, rogue agent AI is kind of the most likely path
*  towards some sort of short term, not necessarily mega disaster in the short term,
*  but, you know, the kind of thing that would be a real like shock to society to
*  see, oh my God, AI, a rogue AI agent did that.
*  My sense right now is that we're kind of limited more by just the limitations of
*  the power of the best models than we are by any actual safety measures that we
*  have. Like it's what my GPT-4 red teaming bottom line was, I think it is safe to
*  release this model because its power is finite, not because you have it under
*  control, really. So how do you see that race dynamic shaping up where like the
*  capabilities are obviously improving, the safety systems are not mature, you know,
*  and you're sitting at this intersection of kind of maybe the most likely vector
*  for like something crazy to happen in the, you know, in the short or medium term.
*  Like the safety mechanism we need to have in AI agencies is like have some sort of
*  kill switch. And like one is like, okay, like you want to be able to disable them.
*  And there's like some mechanism where you pull a lever and it's like, okay, it's
*  that it won't like basically won't take any other actions. I think the current
*  kill switch is just your API. So it's like you just run out of your open AI
*  game budget and then undo anything. So I think that's a current kill switch.
*  I think that's very to agents in a sense, which is like one good way.
*  But I think you can also maybe have like more explicit like controls where like
*  you just like disable it from like interacting with the algorithms, for instance,
*  or you have more like hardware level safety mechanisms too. So I think this would
*  be interesting to see in the core. I believe like you need to have some sort of
*  tenants if you want to build really intelligent agents. And one of them should
*  be like, agents should not be able to modify its own source code because if
*  it's able to modify the source code and put like self involved, it could do like
*  really weird things. It could find like ways, maybe like if GPT-4 doesn't work,
*  you can find like a cloud API key on the internet and they start using it or
*  stuff like that. So I think that should be like one of the tenants where like,
*  like it doesn't have source code access to itself.
*  Maybe it has like very explicit like access to different websites or you have
*  permissive layers on what it can do or cannot do. For us,
*  obviously the funny thing is like when I initially started working on this back
*  in February, I showed this to a professor at Stanford and was like, you know,
*  like you literally invented like invented Skynet.
*  Like this is basically what Skynet is supposed to be. And I was like,
*  I'm like, yeah, in a sense. And there, well, the thing is like, it's like,
*  I would say it's not there yet in terms of like,
*  when it's like foundation models and second is also like how you think about it.
*  Like if you make this into a system that's useful,
*  you reduce the chance of it going rogue, you build in the safety mechanisms.
*  I think you can build this into a very interesting technology.
*  Anything else that you wanted to share about your technology,
*  your product vision for the future before we run out of time?
*  Sure. Sure. I would say for us, I think like we really care about like,
*  can we like simplify or automate a lot of mundane things in life?
*  So you can imagine like currently there's like a,
*  you have to interact with like a hundred different services.
*  It's really hard to do a lot of things where like, like,
*  maybe like we could have some sort of AI,
*  which can just like send like emails to people automatically or could just like
*  coordinate for events for you or automate a lot of those things.
*  And I think this is where we see ourselves where like,
*  we just want to intrinsically understand the user really well and like automate
*  things that they can just like delegate.
*  So instead of you going and doing everything yourself, you just tell the AI,
*  Oh yeah, do this for me. And the AI goes and does it.
*  And so in a sense you're calling this sort of like,
*  you want to unlock parallelism for humanity where like currently you can imagine
*  like we are all single threaded. We can do only one task at a time.
*  But if we could have AI, we could launch like maybe like, I don't know,
*  like a hundred AI agents at a time, all the AI agents do the work and then tell you
*  like, Oh yeah, this work is done. And then you can like sort of like coordinate that.
*  And I think that's what we see as the,
*  maybe might be the evolution of technology where you just can coordinate a lot of
*  these like AI agents to do your work.
*  And it unlocks like a async of it primitive for us where we can like
*  actually like become more parallel threaded if you can do this really well.
*  It's fascinating vision.
*  Nice early execution and a really cool product that I've enjoyed
*  piloting and playing around with. Div, Gurg of Multion.
*  Thank you for being part of the cognitive revolution.
*  Cool. Sounds good. And yeah, thanks. And inviting me here.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad
*  iterations that actually work customized across all platforms with a click of a
*  button. I believe in Omnike so much that I invested in it and I recommend you use
*  it to use cog rev to get a 10% discount.

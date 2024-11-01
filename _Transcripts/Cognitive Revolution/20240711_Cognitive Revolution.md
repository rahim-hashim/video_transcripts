---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 4571s
Video Keywords: []
Video Views: 788
Video Rating: None
Video Description: Nathan explores the future of food production with Rajat Bhageria, founder and CEO of Chef Robotics. In this episode of The Cognitive Revolution, we delve into how AI and robotics are revolutionizing food assembly, potentially reshaping the entire food industry. Discover insights on imitation learning, data flywheel effects, and the vision of accessible, customizable meals produced by robotic kitchens.

Apply to join over 400 founders and execs in the Turpentine Network: https://hmplogxqz0y.typeform.com/to/JCkphVqj

RECOMMENDED PODCAST: Complex Systems
Patrick McKenzie (@patio11) talks to experts who understand the complicated but not unknowable systems we rely on. You might be surprised at how quickly Patrick and his guests can put you in the top 1% of understanding for stock trading, tech hiring, and more.

Spotify: https://open.spotify.com/show/3Mos4VE3figVXleHDqfXOH
Apple: https://podcasts.apple.com/us/podcast/complex-systems-with-patrick-mckenzie-patio11/id1753399812

SPONSORS:
Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

CHAPTERS:
(00:00:00) About the Show
(00:02:40) Chef Robotics
(00:04:09) Food Manufacturing
(00:06:52) Food assembly
(00:11:08) Setting up a robot
(00:14:00) Onboarding process
(00:18:08) Sponsors: Oracle | Brave
(00:20:16) Self fine-tuning
(00:22:59) Variation in the human powered setting
(00:29:53) Safety constraints
(00:32:15) Portfolio of customers
(00:33:43) Sponsors: Omneky | Squad
(00:35:30) Evolution of the AI strategy
(00:40:14) Generative AI in robotics
(00:43:27) Eurekas and bootstrapping
(00:45:43) Time to onboard a new ingredient
(00:47:15) Inner loops of the system
(00:49:17) How controlled does the environment have to be?
(00:52:51) Compute, Energy
(00:54:12) Reliability
(00:59:52) Current challenges
(01:02:47) Humanoid robots
(01:06:42) Business model
(01:07:58) Future vision
(01:11:51) Ghost kitchens and kitchenless houses
(01:14:35) Final message
(01:15:49) Outro
---

# A Foundation Model for Food, with Chef Robotics CEO Rajat Bhageria
**Cognitive Revolution:** [July 11, 2024](https://www.youtube.com/watch?v=ZUTVwgbM13w)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution. Today my guest is Rajat Bagheria,
*  founder and CEO of Chef Robotics, a pioneering company that's taking on one of the biggest
*  challenges and commercial opportunities in AI today. How to incorporate the latest advances
*  into embodied systems so that they can reliably handle the diversity of real world contexts
*  and deliver practical economic value. Chef focuses on food assembly, which I was surprised to learn
*  constitutes an estimated 70% of labor costs in food manufacturing facilities, more than ingredient
*  preparation and cooking combined, and Chef Robots have now assembled some 20 million meals.
*  In this conversation, Rajat shares a detailed account of Chef's technology,
*  including the form factor of their robots, their use of imitation learning, the tremendous efforts
*  they've made to ensure consistency in dynamic environments, their multi-layered strategy for
*  resolving production issues, the data flywheel effects they are beginning to see, and how they
*  are leveraging that data to create a new foundation model for food manipulation.
*  Looking ahead, Rajat sees Chef's robots moving into commercial kitchens of all kinds and believes
*  we will ultimately see a reorganization of the food industry with a proliferation of cheaper and
*  more customizable meal options produced in robotic ghost kitchens and delivered by small autonomous
*  drones. Perhaps surprisingly, in contrast to the more familiar Jetson-style vision of domestic
*  robots that cook for us in our homes, Rajat envisions a world in which the cost of high
*  quality food approaches the cost of ingredients and thus home kitchens become an optional add-on
*  for hobbyist home chefs. As someone who is always looking for realistic glimpses of daily life in
*  the AI-enabled future, I found this vision quite thought-provoking and it's inspired me to think
*  about what other second-order effects we might ought to expect. As always, we appreciate it when
*  listeners share the show and we'd love to hear your feedback. You can contact us via our website,
*  cognitiverevolution.ai, or you can DM me on your favorite social network. And briefly, if you're
*  an AI engineer or an AI advisor who's excited about helping diverse real economy businesses
*  apply AI technology, or if you're interested in sponsoring the Cognitive Revolution, I would be
*  excited to hear from you. Now, I hope you enjoy my conversation with Rajat Bagheria, founder and CEO
*  of Chef Robotics. Rajat Bagheria, founder and CEO of Chef Robotics, welcome to the Cognitive Revolution.
*  Thank you, Nathan. I'm super excited to be here. I am too. This is cool. We've done, obviously,
*  a ton of episodes on a ton of different things, including a few on robotics research, but I think
*  this is the first time that we'll have an opportunity to talk about a product that is
*  deployed at some non-trivial scale in the robotics wild. So I'm excited to get into that with you.
*  I guess, for starters, you want to just give us the very high-level overview of what is Chef Robotics,
*  and then I'll dig into all the technical and socio-technical nooks and crannies from there.
*  Yeah, that sounds good. So yeah, Chef Robotics, we make AI-enabled robots for the food industry.
*  We're starting with actually food manufacturing, and that's because it's actually a very
*  relatively good place to collect training data, add ROI to customers, and we can talk more about
*  the nuances of that, but it's a really good starting point where we can relatively quickly
*  ship robots. It's like L2 autonomy, you could say, in the AV parlance, and we can generate ROI for
*  our customers. And of course, the more robots we deploy in this area, the better that our chain
*  data set gets, and our AI gets, which then allows us to have a more dexterous system, which then
*  allows us to do hopefully more complex applications, such as GhostKitchens, such as Fast Casuals,
*  etc. The ultimate goal, of course, is to deploy an AI-enabled robot in really every commercial
*  kitchen around the country and the world. So that's broadly what we do, and of course, we leave it
*  from there. Cool. So when you say food manufacturing, what should I conjure up in my imagination
*  there? Is this a packaged meal that I would get from a Costco type outlet that is getting created?
*  Yeah, more or less, yes. When most people think about food manufacturing, they think that's
*  already automated, basically, and actually there are parts of it that are automated.
*  So if you think about if I'm Kraft Heinz making ketchup or something, it's already automated.
*  On the other end, that's called low-mix manufacturing, where essentially you don't
*  have that many SKUs. So let's say you have 10 SKUs. What you're going to do is get 10 dedicated
*  lines for each of the SKUs, and you run them all day long. Then there's this idea of high-mix
*  manufacturing. High-mix manufacturing is if you have hundreds of SKUs, for example meals. So
*  prepared sandwiches, salads, party trays, meals you say at Costco or Trader Joe's, frozen meals,
*  things like that. Meals you might even find at the hospital, for example, fish and trays, schools.
*  There are a lot of variety. There are some people like vegetarian meals, some people like meat
*  lovers, some people are vegans, some people are gluten-free, et cetera, et cetera. Each of these
*  has 20 different SKUs within it. So there's just a lot of SKUs. So the way that these meals are
*  actually made in status quo is actually a very manual process, a lot more manual than people
*  might think. You essentially have these long conveyor lines where you have people scooping
*  food from big tubs into individual containers. And that's the kind of the chad, at least,
*  that we're kind of going after to start. Interesting. So what is the form factor?
*  I've checked out and seen a little bit of the video footage on the website. It appears to be a
*  arm that is mounted to a table. Is that right? We have these modules. These modules are actually
*  encasters. So you move them around easily, wheels basically. Right? You can move them around easily.
*  And it's kind of like a mobile manipulator, I guess you could say. But basically, like,
*  our customers aren't moving these robots around all the time. It's like maybe once a day, twice
*  a day type thing. So you actually don't need to be autonomously mobile. We have a six-stop arm on
*  it, it's a collaborative system. And then there's a bunch of different sensors on it, like RGBD
*  cameras, force stroke sensors, scales, a bunch of different sensors that kind of help us make sense
*  of the world, make sense of the environment. And that's kind of it. It's a very simple system.
*  And then you might have different kind of end effectors, different utensils based on what you're
*  manipulating. On the hardware side, we really try to make it an extremely simple system that
*  we can kind of mass manufacture. It's not like we're trying to make custom hardware for a customer.
*  It's really let's have a module and this module is the same footprint as a person. In other words,
*  it can slide onto an existing line without retrofitting. Let's mass manufacture it. Let's
*  use mostly off-the-shelf hardware. And then it's really put our sort of tiers into the autonomy and
*  make it as flexible as possible so you can do as many tasks as we possibly could.
*  Interesting. Okay. So I'm imagining now I have a household of seven. So we do not infrequently
*  buy the Costco prepared meals. And I'm imagining the sort of before is like people standing at
*  workstations and doing a assembly line type process, except managed where the individual
*  tasks are done by different people. So is it like today a person is sitting there chopping onions
*  all day that go into the stir-fryer or whatever. And then strategically people can get one of your
*  robots and say, okay, we now don't have to have a human chop the onions. We'll have a robot chop
*  the onions. They put in and they can roll this thing around and put it into different positions
*  and then do it's not a mounted arm, but it is arms, right? It's like primarily, is it one arm? Is
*  it two arms? Do the arms work together? Tell me a little bit more about the arms. Yeah. The way you
*  can think about the process right now is in basically every commercial kitchen, there's
*  three processes. There's prepping, there's cooking, and there's assembly or plating. Plating is what
*  you might see at Chipotle, right? Which is a human kind of scooping ingredients out of a hotel pan,
*  a tub, and they're scooping that into a burrito or tray or a bowl, whatever it might be, but that
*  instance, what you find is actually that the most labor intensive process is actually the assembly
*  or plating. And the reason for this, and we can talk about this more, but the cooking and the prep
*  actually scales relatively sublinearly when it comes to at least non-fine dining. For fine dining,
*  cooking is the most expensive, but for everything else, so like food trucks, fast casuals, prisons,
*  hotels, universities, K-12s, manufacturing, everything else, airline catering, all of that,
*  the prepping and cooking scale sublinearly. In other words, if you need more volume or if you
*  need more throughput, you don't necessarily need more humans. And then on the other hand,
*  the assembly scales more linearly. In other words, if you need more throughput or volume,
*  you usually need nearly more humans. So we really focus on food assembly. So your kind of picture
*  is correct though, right? So when you come to a production room, you would find a long conveyor,
*  you'd find 20 people standing on either side of it. Each person would have a big tub of food.
*  They basically have a utensil, maybe they're using their hands. A scooping ingredient out of these
*  big tubs into trays or wraps or burritos or sandwiches and move down the line. And they might
*  be doing this in a 34 degree room, which is actually the usual status quo. And so that's the
*  status quo. And so now what we do is we make this row module. It's the same footprint as a person.
*  It can just slide onto an existing line, take the same footprint, but there doesn't need to be any
*  retrofitting. And then basically we do the same thing that a human might be doing, right? The idea,
*  of course, is that this is a very kind of hard job, right? It's extremely monotonous. It's 34
*  degrees. Oftentimes, like I said, you're actually touching frozen ingredients there and you can't
*  even feel your fingers after five minutes. So there's an extremely high turnover rate and it's
*  really hard to hire for this job. So I think our idea, of course, at least for this go-to-market,
*  is that we can help these customers really have human equivalent that can then allow them to offset
*  that existing labor to a different part of the plant. And that existing set of folks can hopefully
*  help with doing kind of higher value tasks, things that humans really should be doing,
*  continuous improvement. Let's improve this process and make it more efficient, material handling,
*  things like that, right? So how the process might work. Now to your other question about number of
*  arms, right now we actually use one arm. And that's, at least with this task, the food assembly task,
*  which is of course, like just to be clear, 70% of the labor in food companies. So it's a gigantic
*  market just if we just do food assembly, right? So we're not too worried about things more than
*  that at the moment, but of course the idea is that we can do more down the line. Right now the hardware
*  very much is one robot arm per module, but of course we can have multiple end effectors,
*  multiple utensils per robot arm to do various things. Okay. That's really interesting. The fact
*  that 70% of the labor goes into plating is definitely not something I would have guessed.
*  Calls to mind, we did an episode with one of the founders of Codium and kind of somewhat similar
*  stat when it comes to how much time software developers actually spend coding is only maybe
*  a third of their time as well. So that's surprising, but interesting. Okay. How do people
*  set these things up if they get a robot from you and now they, I don't know if this comes in a box
*  and they assemble it or go on site and assemble it for them and interested in kind of some of those
*  delivery details, but once they've got the thing on wheels and they can roll it around and it's
*  okay, Mr. Robot, this is your station. What does the process look like of dialing in its behavior to
*  this particular meal and the serving size and the place it's supposed to go, et cetera?
*  Yes. And then of course that's the hard part, right? I think there's two different parts to this.
*  So on the day of production, let's say, so I guess maybe take a step back, like we ship the robots
*  in crates, they're like wooden crates, they'll arrive. The deployment process itself is actually
*  quite simple. You literally take the robot out of the crate. It's already on wheels. You slide it
*  onto the line. Usually it's a food facility. So they'll wash it down and do sanitation and
*  they'll take like a swab, like a material swab to just make sure there's no pathogens we're
*  introducing. But anyways, basically you slide it onto the line. We require two inputs from the
*  facility, which all kind of facilities have. One is just 110 AC power. And then two is like compressed
*  air. And that's just to actually manipulate the end effector, right? It's a pneumatic end effector.
*  So you plug those two things in and that's like set up. And then part one now for actually using
*  it is by somebody who's actually on the floor. So on the floor, we try to make it as simple as
*  you possibly can imagine. And the reason for this is like our audience is not technical folks. It's
*  not often even English speaking folks. It's often people who haven't, don't have a four year
*  college degree, et cetera, right? So we try to make it as simple to use as maybe they would use an oven
*  at their house, which is to say you go up to the robot, there's this nice touchscreen and you can
*  use your gloves. Just, Hey, this is the meal I want to rent. So this line today is doing the pad time
*  meal. Just made that up, but whatever meal is doing. So I'm doing the pad time meal and robot number
*  one is going to do the noodles. Okay, great. So now you have that. And then the system will say,
*  okay, great. Now you need to attach this particular utensil. We'll recommend utensil to attach. The
*  user will attach this utensil. And at that point, what will happen is the user will load the tray of
*  food right into the module. And basically the system will fine tune itself, which is to say
*  it'll pick and dump ingredients from one pan to the other. And just like really fine tune with this
*  particular batch of ingredient. And the reason, by the way, this is important is that the thing
*  with food is it's first of all, it's an organic compound, but also it's cut and cooked by a human.
*  And every human, of course, is different. And every single day it's different. No batch of food is
*  ever the same. Even if you like it to be the same, it's not. So you have to fine tune for that
*  particular batch, which is to say today the cook added a little bit, they cooked a little bit
*  longer or less long. It's more sticky than we would have expected, or it's more oily, or maybe
*  it's a little more dense, or maybe there's different parts of them. Like if it's a curry,
*  maybe it's different parts of the curry are less dense or more dense. There's different properties
*  that change based on the material. And at that point, basically it's fine tuned. You press play
*  and it'll start to pick and place onto the line. So that's kind of the day of. And again,
*  that's an extremely simple process. This process is in really any language you want. So you can do
*  it in Spanish, you can do it in whatever language you want as a user. So that's the production day
*  of process. Now there's another process, which is, okay, how do you actually onboard a new ingredient?
*  Now, when we're first initially deploying the robots to a customer site, for a new customer,
*  our solutions engineering team would do this for the customer so that the customer kind of is ready
*  to go day of. But now on an ongoing basis, what we do is we create a lot of software to allow our
*  customers to self onboard new ingredients. So the way this might work, let's say I'm a production
*  manager now, or I'm a planning manager, and I have a new meal that I'm running next week, or maybe
*  even tomorrow. The way this kind of works is that each of our customers have these like what we're
*  calling meal cards, they're kind of like PDFs. And this meal card might say, okay, well, the first
*  ingredient is going to be the noodles, and it's going to have this image, and it's going to be
*  this portion size, and I want to place it into compartment two. And you may be like seven or
*  eight ingredients on this meal card. So what we do is we have a web app that we give to customers,
*  and we essentially have them upload those meal cards, and then we'll use a VLM to kind of
*  parse that. And we'll take that unstructured data about all these metadata about this meal into our
*  database. That's step one. Now, actually, that is sufficient to actually have the robot run. You can
*  imagine that just with that information, which is here's the ingredient name, here's the portion
*  size, you can run. But of course, the consistency might not be very good, it might be spilling, it
*  might not be placing as precisely as you need it to place. In other words, the performance might
*  not be there right then and there with just initial kind of ingestion. So you need to do some stuff,
*  which is to say, you need to kind of have a labeling process to actually make this run with
*  high performance at runtime. So now what we do is we try to get as much information as we possibly
*  can. So the starting policy of how the robot manipulates this novel ingredient is a good one,
*  right? So now we kind of go ingredient by ingredient. So let's take the noodles.
*  Now we have the image, we have the string name, we might have the portion size, maybe the compartment.
*  So we take all this information, and we say, okay, so we use LLM to kind of give the users a few
*  different image. We ask the user a few different questions. And for each question, we give them
*  different images so they can have a slider about, okay, where does this ingredient stand from an
*  attribute perspective. For the noodles, we might, and we of course ask intelligent questions,
*  we might ask the question, okay, how long are the particle sizes? And on the very left side,
*  it might be like an edible piece. On the right side, it might be like a very long piece of noodle.
*  And again, our goal is to get as much understanding from the user as we possibly can about
*  this ingredient. Another question might be, okay, how sticky is it? We might show a ingredient
*  that's very sticky, like maybe it's kin cheese. And then on the other side, we might show an
*  ingredient that's very non-sticky, like water. And of course, there's generated images in between
*  here. So we generate those questions, we generate those images. And now basically, the user has told
*  us, and this takes all of a minute, by the way, the user has told us, like, here's generally some
*  attributes about this new ingredient. So now we have those attributes, we have the image itself,
*  we have the string name, we have a portion, we have the compartment, all of this kind of comes
*  together. And we have a model that she spits out the starting policy of the ingredient. Of course,
*  the starting policy is based off of existing production data. So at this point, Chef has made
*  18 million servings in production, we have a ton of production data, I've done thousands of
*  different ingredients, right? The starting policy for this novel ingredient is probably based on
*  something we've done in the past. So now we have a starting policy. And then you can deploy that
*  starting policy, the user, the production management, deploy that starting policy on the
*  web app to the system itself. And now we're back to that initial story. So now when the system,
*  when maybe the line manager now, or even the line worker actually says, Hey, I want to run the
*  pad time, I'm running the noodles, they'll slide the noodles pan into the system, it'll pick and
*  dump and it will fine tune that starting policy to a more fine tune policy for that particular
*  batch of noodles. And for that particular customer's batch of noodles, which is of course
*  different than every other customers, how they cut and crop the noodles. That's broadly how the
*  onboarding process works for us right now. Hey, we'll continue our interview in a moment after a
*  word from our sponsors. AI might be the most important new computer technology ever. It's
*  storming every industry and literally billions of dollars are being invested. So buckle up.
*  The problem is that AI needs a lot of speed and processing power. So how do you compete without
*  costs spiraling out of control? It's time to upgrade to the next generation of the cloud,
*  Oracle Cloud Infrastructure, or OCI. OCI is a single platform for your infrastructure,
*  database, application development and AI needs. OCI has four to eight times the bandwidth of other
*  clouds, offers one consistent price instead of variable regional pricing. And of course,
*  nobody does data better than Oracle. So now you can train your AI models at twice the speed and
*  less than half the cost of other clouds. If you want to do more and spend less like Uber, eight
*  by eight and Databricks Mosaic, take a free test drive of OCI at oracle.com slash cognitive. That's
*  oracle.com slash cognitive. Oracle.com slash cognitive. The Brave Search API brings affordable
*  developer access to the Brave Search index, an independent index of the web with over 20 billion
*  web pages. So what makes the Brave Search index stand out? One, it's entirely independent and
*  built from scratch. That means no big tech biases or extortionate prices. Two, it's built on real
*  page visits from actual humans collected anonymously, of course, which filters out tons of junk data.
*  And three, the index is refreshed with tens of millions of pages daily. So it always has accurate
*  up to date information. The Brave Search API can be used to assemble a data set to train your AI
*  models and help with retrieval augmentation at the time of inference, all while remaining affordable
*  with developer first pricing. Integrating the Brave Search API into your workflow translates to
*  more ethical data sourcing and more human representative data sets. Try the Brave Search
*  API for free for up to 2000 queries per month at brave.com slash API.
*  And that first process sounds like a foundation model for this form factor, where it can take in
*  any of a super wide range of variables. And then are you actually fine tuning that same underlying
*  model with, it sounds like a self fine tuning process where like actual weights are getting
*  changed based on a few iterations of whether the noodles hit the spot or not?
*  Yes, at least for the former, I think like, Shaft has been in production for a couple years before
*  foundational models were really a thing, I would say. So there are a bunch of parts that are
*  foundational models, and there's some parts that are more like deep learning, right? Like deep neural
*  networks, CNNs, things like that. So now what we're doing is actually today as of right now,
*  basically, we're making up, like you said, like more generalized food manipulation model for that
*  first kind of process. And then on the system itself, like you said, yeah, there's like fine
*  tuning that's happening on the system's doing that itself. And the way this of course works is that
*  we have a lot of metrics, right? So we can close the loop. And there's a few metrics that matter
*  for Shaft, right? The most obvious metric is the pick weight, which is to say if you wanted x
*  ounces, how close are you to x ounces? And of course, we look at both the kind of bias,
*  which is like, where's the average pick weight away from the target? How far is it in the mean
*  as a whole, the whole distribution? But we also look at like standard deviation, things like that.
*  So that's the pick weight aspects. And then we can also look at other aspects. So we do placement QA.
*  So we can get a sense of, okay, like when you place, is the food spreading the way it should?
*  Is it spilling into the other compartment? And we have different scores that we assign for
*  placement based on this. That's another metric we have. Another metric we of course have is like,
*  so it's reliability, and there's a lot of proxies for reliability. So one proxy, for example, might
*  be like, one of the things, for example, we do is we have force torque sensors in the robot. So we
*  can say, okay, let's take a path that's going to minimize the incidence of like things, of protective
*  stops, for example, to make sure that the robot doesn't protect us. So the idea of protective
*  stop, by the way, is that collaborative robots are kind of pressure and force limited to 150
*  Newtons for safety, physical human safety. That's great. But sometimes, of course,
*  it'll protect a stop when you don't want it to protect itself, which is to say when you're
*  manipulating food, we try to prevent that, for example, from a reliability perspective,
*  because of course, that means that the line will be down for whatever 30 cents, which is
*  the end of the world, but it's not great either. And then we also look at things like, okay,
*  we can measure the pressure and the flow of the end effector itself. So we can make sure that we're
*  not crushing the material and things like that. So there's a few different kinds of things we do
*  to really make sure that this model as it's picking and dumping, it's actually converging
*  to a policy that's going to maximize some of these outcomes we want, mainly pick weight.
*  That's the most important for the customers. How much variation is there on that in,
*  let's just start with maybe like a human powered setting. I think it's always instructive actually
*  to get these baselines and in so many instances, they're just not there. People have the sort of
*  sense of the human is doing a good job. What is a good job and how much variation is there in what
*  is currently passing as a good job. So I'd be interested to know what the accuracy and consistency
*  of a pick weight is with humans and how you guys compare to that as a robot.
*  Yeah, no, it's a really good question. And actually it's a really important question.
*  And the reason for this, by the way, is like when our customers, and basically this is true
*  for humans, I think, like they have this perspective that the robot should be like perfect. You see this
*  in autonomous vehicles too, right? Like people expect an AV to be perfect. People certainly expect
*  our robots to be perfect. Like I've had conversations where like customers like, oh, you do this like cool
*  AI thing, right? If you use AI, then obviously it's got to be perfect. So the whole point, why am I
*  getting a robot that's not perfect? So like, you know, from a sales perspective and a customer
*  success perspective, that of course leads to like a lot of like mental churn for both parties where
*  it's like, well, the robot's never going to be perfect because the input, the food itself,
*  it's very highly variable. Actually, yeah, so part of our kind of deployment process, our solutions
*  engineering process is that when we first deploy with the customer, we'll actually go and take
*  baselines. And these baselines are basically like, okay, let's actually collect human data in a kind
*  of as blind as we can get manner. So we try to do that to like really understand where the humans
*  are. And what's interesting is that, you know, when we actually present this data to the customer,
*  they are like, often not in belief of that. They don't believe how bad their humans are basically,
*  because they have these like very tight bounds oftentimes. And we show them this human collected
*  data. And it's, oh, wow, this is actually not that great. But by the way, what that does then is that
*  sets our bar. Like that's like, we have to meet or beat that. And one of the things that's interesting
*  with the food industry is that it's these governing bodies like FDA and USDA. And of course,
*  the customer itself, like you and I as customers, right, we, people really care about if the meal
*  itself is like, x ounce is like five ounces, if you're below five, then it's really bad. Right.
*  So what that means is that like, the customers like the leadership at any of our customers,
*  your food companies, they are very highly incentivized to make sure they're never under
*  because there's gonna be fines and maybe cost their customers are going to churn. So what they're
*  telling their line managers and the production managers is to always overpick. So we usually find
*  is there's this very high bias as we call it, basically, they're always picking well above the
*  target weight. So the target weight is one ounce, they might be picking on average at 1.2 ounces,
*  right? That, by the way, is very expensive, because in a food company, 40 to 50% of cogs is
*  the material itself. So if they're just like giving away, it's called giveaway, they're giving away food,
*  that really hurts their bottom line. So one of the big things that we find is that we can really help
*  them dramatically decrease that giveaway, which is a really good ROI, by the way, for our customers.
*  And it's nice because we can also we have closed the loop. So we know that we're better, we have
*  data to show and prove that we're better. There's also some interesting more macro perspectives.
*  Right now, we don't have enough robots to make a really big dent of this. But you can imagine if
*  we have millions of robots in production, not only in manufacturing, but also ghost kitchens, fast
*  casuals, prisons, hotels, etc. All commercial fictions, then that can actually have a pretty
*  big impact on food waste and things like that, which is cool too. Can you? Is that one ounce to
*  1.2 typical number? I would love to get just a little bit more concrete, like how much is the
*  overshoot and how much do you improve on it? It really depends on it. There's so many variables.
*  It depends a lot on the customer. Some customers are really good at this. Some customers are not
*  as good at it and really depends on the ingredient. And I'll give you some exact numbers. But just for
*  a few context, like imagine broccoli, the thing with broccoli is that the particle sizes are quite
*  big. And oftentimes, there's four pieces of broccoli, like five pieces. So in other words,
*  if you scoop it, and you got one broccoli too much, then you're super high. Or if you got one
*  broccoli too low, you're super low. And it's not on the other hand, like a grain of rice. You get
*  a few grains of rice too much, no big deal. A few grains of rice too little, no big deal. So there's
*  certain ingredients that are just really hard for humans. So for broccoli, humans might have something
*  like 30%, 25% bias. Even for us, we have to bias up because we really want to prevent the negative
*  case we underpick. So we might have something like 5% bias per piece of broccoli. Generally though,
*  for most items, let's say imagine something like a potato mash or a sauce or diced vegetables or
*  cooked diced vegetables, whatever it might be. Humans might have something like 4%, 5% bias,
*  which is overpicking above the mean. And then chef might have something like more like 1% bias. We
*  can actually basically guarantee that we'll have less bias. We can guarantee we'll have this because
*  a control loop rate that's constantly going about how much pick weight we had. So that's on the bias
*  side. And then on the standard deviation side, what we do is we have this metric called CV,
*  coefficient of variation, which is basically standard deviation divided by the target weight.
*  And what this basically allows us to do is standardize across pick weight. Because of course,
*  if you have a bigger portion, of course you're going to have more standard deviation. So from
*  that perspective, humans might have something like 16%, 17%, 18% CV. And again, it just differs so
*  much by customer. But yeah, humans might have something like that. Chef might have something
*  like our best is probably like 5% or 6% CV. But I think on average, probably more like higher 7%,
*  8% CV. But that's how we think about that. CV and bias are the two metrics that we really try to
*  optimize for at least the pick weight part of the equation.
*  S2 So you said these things are like drop in replacement. I think you've used the term
*  human equivalent a couple of times. If I'm imagining myself doing this, I think maybe I can do
*  10 scoops a minute, maybe 12 scoops a minute. Is that kind of the same rate at which these
*  things are?
*  S1 Yeah, you also see a lot of variation there. So for this particular problem, there really
*  wasn't any automation before Chef. There's just no automation that really existed for this problem
*  before Chef. It's been an industry where you have tens of thousands, hundreds of thousands of humans
*  who do this, right? The reason I bring this up is because they really optimize the humans very
*  well. There's a lot of you can imagine a lot of process optimization. And that's like the
*  ergonomics. How do you sit relative to the line? And yeah, are you sitting or standing? Like
*  raising your left hand or right hand? There's a lot of ergonomics to think about. But anyways,
*  all of that to say that I think most times we go to a customer sites, they're running anywhere
*  from like 15 to 20 trades per minute type of thing. Sometimes they'll do this thing where
*  they'll pick up a bunch of material and they'll do something like a place, place, place. Like one
*  pick multiple deposits. You can amortize the transport time over multiple deposits. So you
*  get slightly higher throughput. But Chef is around 20 trades per minute. And then if a customer
*  needs more than that, and sometimes customers need more than that, we also have this like multi-pick
*  system, which allows you to have multiple grippers, multiple utensils, I should say, per system. And
*  that allows you to have much faster throughput. The main constraint for us, of course, I think
*  like the obvious question that many people think about is, okay, why don't you just put like an
*  industrial robot here, right? The thing is, there's a lot of safety constraints with that.
*  The whole point of Chef, from a more philosophical perspective, is like we try to partially automate
*  a process. And the reason to partially automate a process is if you have the full line automation,
*  the thing is if you cannot do one of the SKUs, one of the ingredients, or let's say FedEx,
*  and like a robot can't do one of my parcels, then I basically haven't automated the process,
*  but I still need a human to do it. So you find a lot that if robotics companies try to fully
*  automate the process, they have a ton, a very long sales cycle that is very risky, very long
*  deployment cycles, and the technology bar is extremely high because your autonomy needs to
*  be able to handle literally every single SKU. Whereas for Chef, we can partially automate a
*  line. So, you know, if there's a particular ingredient we can't do, that's okay. For example,
*  we couldn't do, let's say we can't do shrimp. That's okay, human can do the shrimp. We can do
*  everything else. So, you know, what's nice about this then is that like the deployment process is
*  quick, the sales cycle is quick, the technology, the way of flywheel, the more robots we deploy,
*  the autonomy gets better. So all these things are very nice. But then what it means from a safety
*  perspective is that you are constantly around humans. There's a human to your left, there's a
*  human to your right, there's a human refilling the robot. So from a safety perspective, collaborative
*  robots are a necessary apartment. And there's of course laws around the max force that you can
*  impart, and there's laws around the max kind of joint velocities you can have with not just joint
*  velocities, but basically there needs to be a strong safety case around this. And that's where
*  we found that collaborative robots plus the right tooling and effective tooling allows us to get
*  the throughputs that our customers need. So if it's three or four seconds per trip,
*  that comes out to pushing a thousand per hour. And then you've got 20 million pushing, I like to do
*  round numbers. So pushing 20 million servings, thousand an hour would be 20,000 hours. So it
*  sounds like you've got kind of 10 man year worth of work completed so far. What does that look like
*  in terms of the portfolio of customers? Like how many robots actually is that? And how do you see
*  that scaling into the future? Yeah, right now we have robots in mostly North America right now. So
*  we have robots in six cities, five states and US and Canada right now. So we went into production
*  in mid 2022. That's when we kind of deployed our very first systems. And since then it's from 22
*  to 23 weeks scaled 4X in terms of like revenue and this year expecting something similar,
*  something more like 3X this year. So I think what's really nice about this market is that it's
*  huge. It's not something that many people think about, but like production is just gigantic.
*  And so I think right now our goal very much is to scale within our current customers and of course
*  scale to net new customers. What's nice about our current customers, we actually have a few whales
*  and generally the thing with production is that if you open up a plant, you're not going to have
*  five people doing this. You're going to have 50, 120, whatever the number is, but it's going to be
*  a significant number. So in each of our customers often have multiple plants. So the point is that
*  to get to, let's say the bar is a hundred million bucks an hour, that doesn't require 50 or a hundred
*  or a thousand customers. Like we can get there with 20 to 30 customers. And of course what that
*  requires is like a ton of focus on customer success and really making our customers very happy.
*  So we spent a lot of time on customer success to really make that happen. And I think the goal is,
*  yeah, just continue growing three X or so per year. Just, and over time there's going to be a lot more
*  other products we sell, other products, other markets, but at least for this market, we think
*  we have fun product market, but it's kind of just like scale down. Hey, we'll continue our interview
*  in a moment after a word from our sponsors. Omnike uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work customized across all platforms
*  with a click of a button. I believe in Omnike so much that I invested in it and I recommend
*  you use it too. Use Cogrev to get a 10% discount.
*  And anything under the sun. Full disclosure, it's going to cost more than the random person
*  you found on Upwork that's doing two hours of work per week, but billing you for 40.
*  But you'll get premium quality at a fraction of the typical cost. Our engineers are vetted top
*  1% talent and actually working hard for you every day. Increase your velocity without amping up burn.
*  Head to choose squad.com and mention Turpentine to skip the wait list.
*  I'm looking back to the business model, maybe a little bit more toward the end, but let's talk
*  a little bit more about the tech stack. I mean, there's obviously been an insane, and I think
*  it's a challenge that many companies have faced, especially on the software side, more so than
*  probably on the robotics side, but maybe there too, where the, you set out to, you know, build an AI
*  company five years ago. And just as maybe you were starting to get things to work, like all of a
*  sudden a whole new wave of enabling technologies have come online. And I think for a lot of
*  companies presented some really hard dilemmas where they're like, man, we just got this rough edge
*  sanded down and maybe then, you know, the new foundation model paradigm doesn't quite do that
*  in the same way, but it has all these other things. So tough choices. So how has your kind of core AI
*  strategy evolved and you could cash that out into like different kinds of models or different
*  training regimes or whatever? No, it's a really good question. I really do think actually that
*  foundational models have really uncapped a lot of robotics potential, I would say. The issue with
*  robotics has always been the world is very highly dimensional. Like if I can pick up a wine cup,
*  that doesn't mean I can pick up a tea cup, and that doesn't mean I can pick up like a water glass.
*  It's just a very highly dimensional space. And in our world, every customer cuts food differently,
*  cooks food differently, every individual does that differently, every site does it differently,
*  different countries do it differently. There's just so much variety in the world. And that's
*  always been the issue with robotics. The thing with AI is, and especially like the modern kind
*  of the more like recent advancements in it, right, with VLMs and LLMs, things like that,
*  they're really good for like high level task planning, right, which is to say, you know,
*  what's in the scene, but they're trained on internet data, right? So there's a lot of like
*  image and language pairs, but there's no like understanding about like how to actually
*  move the arm. There's no motion data, if you will, right? Unlike something like a GPT or a
*  large language model, we at Chef can't just download the internet, if you will, as training
*  data. That's not possible because there's no training data set with food manipulation. So
*  what do you do then? There's a few options. Option one is you do SIM. And SIM is interesting for
*  some companies, I would say. So for example, if I'm a self-driving car company, a lot of the
*  training does happen in SIM. That's not perfect, but you can get some of the way there when it
*  comes to modeling things. If I'm doing rigid body manipulation, let's say I'm doing like
*  palletizing, depalletizing, case packing, things like that, then I can use SIM. With food though,
*  of course, it's wet, sticky, deformable, malleable things, often sometimes non-Newtonian things.
*  The physics simulators out there just aren't good for that. So SIM doesn't really work.
*  You can do testing things from a reliability perspective for like your high level motion,
*  but you can't do that with grasping. And the hard thing with Chef is the grasping. That's the hard
*  thing. And that's the thing you can't actually do in SIM. So what we have realized is really the
*  best way to actually get this training data is in production. And that's why this 20 million serving
*  food done is so important. So that's kind of like the status quo. Now, where does this new stuff,
*  like I said, why does it help us? I think the part that really helps us is leveraging transformers
*  to do things like learning from demonstration and imitation learning. So specifically, one of
*  the problems we face is kind of like transferring knowledge across ingredients. So if we see a sticky
*  rice at customer one, can we then leverage that to do another sticky writer outside a different
*  customer? Because of course, they're cooked in very differently. And transformers actually really
*  help here. We can kind of encode important characteristics about one sticky rice into the
*  embedding space of the transform and then use that to determine ingredient similarity for a
*  different ingredient. So I think imitation learning and by extension, reinforcement learning
*  are things that we're really heavily investing in. We've already now done a lot of actually
*  basically reduce the time it takes onboarding the ingredient. So initially we talked about the
*  process on onboarding the ingredient with this web app. That leverages a lot of like more traditional
*  VLMs and LLMs. And then of course, we've fine tuned them for our own use cases. But I think a lot of
*  novel AI stuff we're doing leveraging transformers and gen AI is really IL and learning from
*  demonstration, I would say. Yeah, that's quite interesting. And to say the least,
*  you see the project I'm sure you did. It was spearheaded by folks at Google, but it involved
*  groups across a ton of different, mostly academic labs where they collected, I think all for like,
*  robot arm form factors. They collected like a bunch of different data sets and then created
*  essentially the foundation model combining all those different data sets and then returned
*  that back to the community. Yes. Is something like that useful to you? I think it's useful,
*  something like that. We haven't tried it. So I don't want to say yes or no just yet. I think
*  something like that could be very useful when it comes to that first part, the onboarding part of
*  the web app for us. The key again is that, at least from what I understand, that training,
*  the training day is really key here. So if you train on rigid body items, you're not going to
*  be able to manipulate malleable items. Even if you think about the food demonstrations that people
*  do, you're not always doing the primary handling of it, I guess you could say. We actually have to
*  handle the raw material and it's dripping everywhere and it's sticky and it's wet and
*  it's all these things. You'll compress them, you can't uncompress it. So I think our approach right
*  now is how do we leverage imitation learning, reinforcement learning, and then also our production
*  data. And I would argue that the most important part of this is the real world production data
*  to then train our own in-house generalized food manipulation model. And that's what we're trying
*  to do, which is this end-to-end system that we've trained to manipulate food. And we're starting
*  with food assembly because that's the majority of the labor issue. But over time, you can imagine
*  that this does other stuff. And of course, with IL, you can very quickly teach a new task. There's
*  a lot of operations you see in a food facility that you might not imagine, taking sheets of baker's
*  trays and putting them into a rack. I mean, that's not like direct engaging with the food, but there's
*  a lot of random tasks. Right now, we focus on assembly and plating, but over time, we can do
*  some of these other tasks, all powered by this generalized food manipulation model. Right now,
*  I would say that we're very focused on IL and RL more than that second part, because that's the
*  most useful for our customers and us. Because it basically allows the time to onboard a new
*  ingredient, just a new class of ingredients, I guess you could say much quicker.
*  So for reinforcement learning purposes, you clearly have some objective scoring capability
*  or opportunity around, did you get the right weight, for example. I wonder if you see a use
*  for things like the Eureka project that came out of Nvidia. This is one that I keep going back to
*  over and over again, because what I'm trying to do broadly is understand what is the state of the
*  art, what's possible now. That's obviously moving so fast that it's a full-time job just to keep up
*  with. But one of the things I used to say was, when I was summarizing state of AI for other people,
*  I would say no Eureka moments. The AIs are getting really good at routine tasks, but they're not
*  coming up with insights on their own that certainly don't surpass and seldom even rival
*  the sort of insights that people can have. Now, one exception to that, I would say, has been this
*  Eureka project where they had GPT-4 write the reward function that they used to train this robot
*  hand to do various manipulations. I always think about that as, for one thing, because I used to
*  say no Eureka moments and they called the project Eureka, so that's uncanny, unto itself. But the
*  idea that it is better at writing these reward functions than the people that they had participating
*  was quite interesting. So I guess you could take that question very specifically at the Eureka
*  project level or more broadly, is there a bootstrapping dynamic that we're starting to see
*  where models can feed into this cycle of learning new tasks? Yeah, it's a very good question. We
*  talk a lot about this, right? So it's like a parameterized policy versus not parameterized
*  policy. What I mean by this is the four foundational models and IL. IL has been around
*  for a while, of course, but I don't think it really started to work until Transformers,
*  and I think Transformers have actually been really useful for that, diffusion policies, basically.
*  So let's think back to like, I'm in 2019 and I'm starting the robotics. I think that the
*  software and car industry, the AV industry, set a really good precedent of, okay, you have a
*  rule-based system. Of course, it's using a lot of deep learning and CNN, but it's a rule-based system.
*  What we would do is, back in the time, we would have a policy per ingredient, and that policy
*  would be bootstrapped, like you said, and parameterized. So we'd have 200 parameters,
*  basically. And this would be everything from a bunch of physical attributes about how do you
*  actually do the pressure and the flow and the dwell time of the food and how many shakes you do
*  and what's the amplitude of the shakes and a bunch of different parameters about how do you
*  manipulate this ingredient. And then we built a lot of infrastructure on how do you onboard
*  new ingredients leveraging those existing policies. That was kind of how we did it back then.
*  And that's like parameterized, but there's these different parameters. But those parameters are set
*  by a human. It's set by a human engineer or an applications engineer. But it's not necessarily
*  true that those are the right parameters. We don't really know. We think they work well,
*  and like we said, we have this control loop that allows us to actually know the result we're
*  looking for, which is things like pick weight and how much spillage there is and placement quality
*  and all these things, reliability. But we don't really know if it's actually a local maximum
*  or global maximum. What imitation learning allows us to do and learning from demonstration is what
*  we can do is we can tele-op using, let's say, two robots side by side. You can have one robot,
*  literally mimic a human scooping it. And by the way, it's embodied, it's grounded, if you will,
*  because we have the exact embodiment that we're tele-opping doing that. And it's the same robot
*  doing where the human's doing the tele-op, the demonstrations, and the robot that's actually
*  doing the manipulation. So there's no grounding problem, I guess you could say. And now basically,
*  it's not like there's human written parameters. It's fully end to end. And I think that's been
*  pretty cool, actually, because we haven't had an insane, whoa, how did I ever think of that? We
*  haven't had a moment like that. But it's cool because it's really an end to end system. And
*  it's quite simple. There's not like a bajillion lines of code, and it's quite simple, and it
*  actually works quite well. So I think that's interesting because the time it takes to
*  onboard a new ingredient is one of the most important metrics for us. And the reason is that
*  the crux of what we are doing is providing a flexible automation solution to our customers.
*  And in other words, the more ingredients we can do reliably, consistently, the more useful this
*  thing is. In other words, they're going to use it more. If we could do a thousand ingredients versus
*  more plickel, maybe, if they can do 100% of their ingredients versus 60% of the ingredients, they're
*  just going to run the robots more. If they run the robots more, they're going to buy more robots,
*  which of course is great for our business. So the number of ingredients we can do is really critical.
*  And if these new technologies allow us to compress the time it takes to onboard ingredients,
*  then we can have higher utilization of our robots, which means that our customers are going to buy
*  more robots, which means we have even more training data, which allows us to accelerate this data
*  flywheel. And on top of that, there's another flywheel, which is the more robots we ship,
*  of course, there's other flywheels. We have case studies, and these case studies allow us to get
*  even more customers. We have more volume of robots are manufacturing, which allows us to improve our
*  bill of materials and supply chain benefits. We have operational benefits, which is going to
*  more plants and more sites, which means we have more people all over the country supporting these
*  robots, which then allows us to support other similar customers in the nearby area. So there's
*  all these kind of flywheels, but I think the crux of it always comes back to the number of ingredients
*  we can do. And I think the reason transformers, at least I would say, and diffusion policies are
*  really powerful is because of that idea. It accelerates the flywheel for us, which is the
*  crux of the business, ingredient coverage. Those sort of macro outer circles are really interesting.
*  What about the inner loops that kind of comprise the system? Actually, I was thinking back, we did
*  another episode with Skydio, the drone maker, and he walked us through. They're pushing
*  up to the point where you can give it like a verbal command, hey, go survey that cell tower and
*  come back with a full inspection of it. So that's like the highest level, outermost loop. And then
*  the innermost loop, I think, was running at 10,000 Hertz or something. And it's just like the very
*  low level voltage control. I imagine you have something similar going on there. Although if
*  it's three seconds, I could imagine you could maybe generate the whole three seconds and let it run.
*  But what are the sort of loops? How many corrections? Are there moments in that three
*  second cycle where you get to say, hey, I'm off course here. I better correct. What's that look
*  like going down to the lowest level? Yeah. So I think that to start, there's two computes per
*  robot cell, per module. One is actual physical robot controller. And so the robot controller
*  itself, that has its own kind of joint controller, just on a more high level, relatively speaking,
*  level, what do I do? And then there's a motor controller. What does this particular motor do?
*  And exact kind of voltages that I need to send actually do something. So that's on the actual
*  physical kind of hardware controller for the actual robot arm. And then we have the chef compute.
*  And by the way, the reason to get to separate these is like the robot one is safety rated.
*  We can talk more about that, but that's really important for like safety and safeguarding. It's
*  a completely safety rated system. There's like certifications we've gotten from a third party
*  around safety. And then on our side, like we have our own compute. And that is, I guess at least
*  two layers, more like three, but there's like more like high level task planning loop.
*  That's high level. And then we have like trajectory of placement loop, which is okay,
*  like what are the structures I need to take to actually execute them? And then there's like
*  a control loop actually controlling the robot controller itself. So that's how we think about
*  that whole thing. Right. Like how controlled does the environment have to be? We've seen some of
*  these demonstrations, which are certainly not production ready, but Google has put out a couple
*  of these things where they give the robot a task, like in the SACAN vein of research, right? Where
*  they say, go get me a bag of chips off the counter. And then somebody comes in like,
*  snags the chips out of its hand and puts it back on the counter. And because there are these nested
*  loops and the robot can realize like, oh, I don't have it anymore. Better go back and get it again.
*  So do you have that kind of correction step, like between the sort of generation of the policy,
*  if somebody moves the tray a little bit, does it adjust to that on the fly?
*  Yes. Yes. Yeah, exactly. By the way, that's like super critical. I think there's multiple reasons
*  why Shep is hard. One of them is just like changing material properties. But the other one is what you
*  said. We react to and adapt, I guess you could say to a few different parts of the environment.
*  One is like the food itself. Again, like batches, like every hotel pan, if you have a run of six
*  hours, you might be going through hundreds of hotel pans. So like every pan is different because
*  it's cooked by human and humans of course aren't perfect. So we adapt to that. And then within each
*  pan, so if you're like a pulled meat, yeah, yeah, mostly meats, right? Different parts of the animal
*  have different densities and different material properties. There's actually variations within
*  the pan itself. So we'll adapt to that. And again, we have sensors like forced torque as well. So we
*  can get some of those readings as well. So that's one layer. Then on the placement side, of course,
*  there's humans who are usually traidy nesting, putting the trays onto the line. These trays
*  have various orientations. They're sometimes farther, they're sometimes closer. So you have
*  to adapt to that. Usually customers have multiple kinds of conveyors. Some of them are different
*  colors, different widths, different heights. You have to adapt to that. That's all dynamic. That's
*  not like hard coding. It's like dynamically figuring out where to detect and track the containers
*  and place them in the containers. There's also a lot of like small little nuances that come with
*  production and deployment. So for example, food facilities are always sloped for water drainage.
*  Conveyors are always sloped. And you don't really know because the interesting, the slopes are kind
*  of like sinuous. In some regards, obviously, it's a longer plane, but our horizon. But yeah,
*  basically, you don't know like where the conveyor is going to be or the slopes. You have to detect
*  that. And that changes because the conveyor is shaking and the robot is shaking. So that changes
*  and you have to dynamically detect that. Sometimes like humans will bump into it and conveyor is skewed
*  now. So you have to place farther and higher. For example, there is some line manager who's like
*  trying to get their humans to work more or less, maybe so they'll drive up the velocity of the
*  conveyor. There's also humans, again, like I said, to the left and right usually of the robots. So
*  those humans are kind of interacting with the system. They're pulling bolts underneath it,
*  they're putting bolts in. They're changing the scene a lot. So look, like Chef is not a self-driving
*  car where it's like extraordinarily highly dimensional scene, but it's a fairly kind of
*  hectic scene. And there's a lot of changing. And like, those are the kind of issues that I think
*  you find in production that are hard, right? You can scoop food in a lab. It's not hard. And you
*  can even make it consistent. You can use a bunch of these advancements in AI to make it consistent,
*  which is already hard. And then you can even get it to be doing a lot of ingredients. But then,
*  like when you get to production, you see all these weird edge cases. You have no idea because there's
*  a lot of humans in tracking the system and they do things that you don't predict. And that's where
*  I think a lot of work has gone into get to these 20 million servings. Like how do you actually make
*  this thing reliable? But when you have dozens of different systems around the country to actually
*  deal with these kind of changes in the scene. Yeah, the world is a messy place.
*  So scanning down the list of kind of technology questions I had, I think we covered
*  most of them. Oh, energy was one I was interested in and compute. Is the compute hosted on the
*  device or are there like cloud calls that you're making? And what is the energy usage of one of
*  these robots look like? Yeah, so like we can divide it between training and inference. All the
*  training is in the cloud. So like we use things like A100 to kind of do training for the
*  IL imitation learning and things like that. And then the inference is all of course on the robot
*  itself. So the robot is of course connected to the internet, but all the inference is done locally
*  on an edge compute. And that's really important, by the way, because our customers usually have
*  spotty Wi-Fi. We can't depend on Wi-Fi, even LTE or 5G. Like you can imagine a hotspot that
*  doesn't really work in our customers too, because it's a facility and then there's like often
*  obfuscation. Like LTE basically doesn't work great. So yeah, so that's how we think about that. And
*  then from a energy perspective, the arm I think is like 200 watts or so. And then the CPU is like
*  35 watts. It's relatively low. And then the GPU is like 50 watts. Like the entire system is actually
*  relatively not that power hungry. And like one of the questions that some of our early customers
*  asked is like, Hey, look, yeah, I'm not paying for labor, but is my electricity bill going to
*  go up the roof here? And we did the math and it wasn't actually that great. It's five bucks or so
*  per day. I think even less than that. Even if you're running at like 24 hours a day type of thing.
*  So yeah, in my market in Detroit, where I live, it is like just under 20 cents per kilowatt hour.
*  And so if you are at 300 watts, then obviously it would take you, let's say three hours to
*  get to a kilowatt hour. So that means you're at just a couple bucks to run it 24 hours.
*  I think that the, and most of that is going to the actual operation of the robot. I have a robot arm,
*  a distinct thesis that I'm working on packaging up. That's like, I think the energy concerns
*  associated with AI are significantly overstated. And what the fact that the leaders are talking
*  more about energy concerns implies is that they see an unbelievable amount of adoption
*  around the corner. So I think about those kinds of orders of magnitude quite a bit.
*  Does that internet limitation also mean that teleoperation has to be done
*  locally? Or I was understanding previously that you like maybe provide that as like a
*  sort of remote service, but I'm not sure now. But yeah, we don't actually do tele-op in the
*  plate. Most people think about tele-op, right? Yeah, I think the crux of this is that we're
*  working with like production customers. They have very low tolerances for failure. Like basically
*  the thing used to work or else pull the robot. And this is what I mean by that is like,
*  one of the things that's nice about Chef is like, it's not going to like, it's like relatively
*  safe broadly, right? It's not going to hurt anybody. And like the worst it's going to do is
*  it's going to not be consistent, or maybe if there's a bug, it's not going to pick it all.
*  There's going to spill too much, but it's not like the end of the world. What will happen if
*  there's a failure is that the operator can pull the robot off the line to put a human in type of
*  thing or put another robot. Usually it's not a hardware failure by the way. So they're putting
*  another robot in necessarily, but let's just say it's a hardware failure, pull the robot out,
*  put another one in. But generally, yeah, like the tele-op, we don't do that in the colloquial sense.
*  The way we think about this, how do we address the reliability problem is first of all, we try to
*  build a system to be as autonomous as it possibly can be. So it needs to adapt to changing material
*  properties. It needs to adapt to different tray types, rotations, distances from the robot. It's
*  adapt all these different scenes. I think we've talked about it. And then that should hopefully
*  solve most edge cases. For example, the system detects a tray, it starts tracking the tray,
*  and then a human randomly pulls out the tray. And now the system's confused and it's like,
*  where did my track go? And maybe it places on the conveyor. That's a bug we might've seen. But now,
*  of course, we've built in logic so that, okay, that will be a little more smarter about this.
*  That's just one example, but that's part one. Part two is that, okay, well, there's still, of
*  course, from time to time going to be issues. One of the things that's nice about Chef is there's
*  always a line manager. Even if it's a fully automated Chef line, there's six robots of Chef
*  on the line, there's always a line manager. Let's say the line manager finds that, oh, something's
*  wrong. Maybe there's a tiny compartment and it's not placing right in the tiny compartment,
*  spilling a tiny bit into the wrong compartment. And so what we do then is we try to have a really
*  nice way for the user to visualize what's happening. We give them a really nice 3D view. Maybe you
*  send away more similar to that. We give a really nice 3D representation of what the system is
*  understanding and what the scene is. And at least that allows the user to figure out what's happening.
*  For some examples, that might solve. One example might be that, like I said, in the morning,
*  they'll come in, they'll crank up the conveyor velocity and it might be running super fast.
*  And they're like, ah, it's missing bulls. What's going on? Well, if we have a really nice 3D
*  view where it shows it's outside of the ODD of the system, it's too fast, then we can very
*  visually, not using words, but visually tell the user about that. Or maybe we find that the human
*  denester is putting trays way too far from the robot, it can't reach that far. So again, we can
*  detect those containers and we can tell the user, oh, you need to place closer to the robot.
*  There's a lot of operational stuff like this we see. So that's part two. If that doesn't work,
*  then there might actually be an issue, something that the human needs to fix.
*  So at that point, we give the operator very simple and coarse ability to fine tune the system.
*  Yeah. So they can fine tune the system, whether that's in a picking perspective or placing
*  perspective. And of course, we don't give them too many knobs because they can potentially make it
*  worse. But we try to give them some knobs so they can fine tune. And by the way, this fine tuning is
*  also useful when we onboard ingredients, by the way. One of our people can fine tune themselves
*  to onboard initially too. And finally, if that also doesn't work, then what we do is we built a lot
*  of data infrastructure. So we're collecting all this telemetry that's going to the cloud.
*  And we built a lot of cloud infra that self annotates these events. So let's say an event
*  might be a very high weight event, basically super overpicked or super low weight event,
*  a fault, a mistful, a double deposit, whatever these events might be, like a pick hesitation.
*  There's different events we see and we'll annotate that. It'll do it itself. And then basically,
*  it'll collect like we use ROS. It'll collect the ROS bag. Here's all the data around this event,
*  maybe 20 seconds before, 20 seconds after. It's this like bag file of all the data that happened
*  and why this decision was made and why the robot reacted this way. That'll get uploaded and then
*  our customer support team will get an alert. And if it's the daytime, it'll be on Slack. If it's
*  at night, we'll get a paid your duty. And obviously there's different severities and we try to assign
*  a severity to this too. And then that customer support person can actually figure out what's
*  happening and then fix it. And if it doesn't, if they can't fix it, then they'll elevate it to
*  the applications team or even the engineering team. And that's how this works from a support
*  perspective. And I think that's been fairly good for us, I would say. So when you mentioned earlier,
*  imitation learning of one robot to another, is that something that is
*  all happening centrally as part of the pre-deployment process?
*  Yeah, exactly. Exactly. Yeah. So we would do that at our office. We don't have customers do that.
*  You can imagine customers do it too down the line, but right now that's something that our team would
*  do. The value of that technology for us is onboarding that new ingredient. And by the way,
*  if there's already an ingredient that we can do that, maybe we'll use it too to make this
*  generalized food manipulation model. But we're really focusing IOL on that new ingredients,
*  new stuff that's just hard. So what is hard right now? I guess you've got the flywheels going. It
*  sounds like 20 million servings is a lot. What are the current frontier challenges? And which of those
*  do you think you have to solve on your own? And which can you wait and let the world do for you
*  and just take advantage of? I think the hard thing is what it's always been, which is food
*  manipulation is just really hard. And the thing is there's really nobody else in the world that
*  has a really good training data set for food manipulation. That's just, they don't. And a lot
*  of the existing technology, like SIM, doesn't work. So there's a lot of stuff we have to invent,
*  I would say. So I think the hard thing is still food manipulation and being consistent. In other
*  words, our robot, you give it literally more or less any ingredient. We can do, you give it any
*  ingredient, we can manipulate it. But that doesn't mean it's going to be consistent. That doesn't
*  mean it's going to damage. If you take a very soft ingredient, it's going to, off the shelf,
*  it might damage the ingredient. It might spill the ingredient. It might not be able to, the ingredient
*  might stick to the end effector. We might not be able to place in the right compartment without
*  getting into the other compartments. There's all these things we might not be able to do. So it's
*  this very hard problem, which is how do you have a system that can basically do any ingredient
*  fast? Because of course throughput is really important. Reliably, and of course in engineering,
*  anytime you have more flexibility, reliability usually suffers. And so you need both here,
*  reliability and flexibility. While of course being consistent and not having giveaway and
*  not spilling and not damaging and placing like compartments and working with any conveyor and
*  working with any container. Like that whole thing becomes a really big, highly dimensional problem.
*  And even forget the placement part, just the picking part, the breadth of ingredients is hard.
*  So I think our big focus honestly is like, we really do think that these new technologies
*  are like really going to uncap the potential. We've already seen that. We've already seen that.
*  Let's take the combination of production data, which we think we have the most production data
*  in food now. Let's take that plus demonstrations and let's try to build this generalized food
*  manipulation model. So we have one kind of system to manipulate food and hopefully
*  really have the best manipulation. That's really that continued. That was the focus of day one.
*  And that's still the focus right now, because that's the hard problem here. If we solve that
*  problem in the fully formed way, this is a gigantic company is the way we think about it.
*  So when you look at these kind of new wave of humanoid robots, whether from Tesla or figure
*  or whatever, it sounds like you basically think good luck to them. They may even be successful,
*  but food is going to be one of the last things they're going to come for. And it's just so far
*  down their checklist that you don't expect to have any meaningful competition anytime soon.
*  Yeah, I think that's definitely right. I think that's definitely right. And there's a few other
*  kind of ways I think about this. One thought that always comes to mind is when it comes to food,
*  let's just talk about production or even fast casuals, ghost kitchens. Having a system walk
*  around is not terribly useful. It actually does not actually add much value. So in the
*  manufacturing scene, it's very obvious. You have a conveyor line, you have a station,
*  the robot's on the station, that's it. Like I said, our robots are on wheels. You can move it
*  around, but they move it around like once a day, twice a day. And if I have a humanoid,
*  I'm spending like half of my compute just not trying to fall down. And then on top of that,
*  I have all these safety concerns. Like it just really doesn't add much value. And a fast casual
*  setting, a ghost kitchen setting, you literally rip out the prep table, you put our prep table in,
*  slide it in, our module in, and that's it. You don't need to like move around. So anyways,
*  all of that to say, I think there's going to be certain applications where a humanoid is quite
*  useful. The colloquial tote picking and facilities you often see is a good one. Maybe hospitals,
*  right? Like moving samples around a hospital. My opinion, and I think I've talked to a few
*  humanoid companies, is if you look back, if you think about, okay, what does the world look like
*  in 2050? I think if you've ever watched Wall-E, I think the world's going to look a little bit
*  like Wall-E, which is to say you're going to have tens of millions, hopefully hundreds of millions,
*  of robots that are very good at certain things. Like our food and manipulation robot doesn't need
*  to walk around. It doesn't really add value. And great. So let's do that. Just like your refrigerator
*  doesn't need to do your laundry, so to say, right? Like let's just let it do that. And there'll be
*  millions of robots, again, like tens of millions, a hundred millions doing specific things. And then
*  there's millions of robots that are more general purpose. And of course they might not be doing
*  that particular. I think it's just, it's a volume question. Our robot is doing this thing for 16
*  hours a day. And in a fast casual, it's doing it for eight hours a day. So it's just doing the
*  thing all day long. Now, if I'm in a home or if I am in a hospital or if I'm in a kind of like a more,
*  a different environment where I have 50 different tasks and those tasks are radically different,
*  then maybe it's something like a humanoid makes sense. But I think that the market is actually
*  smaller for that than like the market for all these different applications. You can have specific
*  things, I would say. That's one thought. There's another thought, which is it's a time
*  horizon question. As of today, it's like Uber versus Uber ATG. Uber is a great business to build.
*  Maybe over time Uber ATG is a better business, but Uber ATG is always 10 years out. It didn't
*  really happen yet. It still doesn't, hasn't happened. Maybe it does happen, of course, in full form, but
*  I think it's a time horizon question. Humanoid might be a thing in 20 years at full capacity,
*  but AV has also taken like 20, 30 years to get there. It's still not totally there.
*  I think humanoid are kind of like AV. It's just going to take a lot of time, a lot more people,
*  in my opinion, people think. And yeah, so it's a time rising question. Today, this is what makes
*  sense. Over time, let's build software that is hardware and embodiment agnostic. We built our
*  code base to work with any hardware. So let's say I'm wrong there. And 10 years on the line,
*  humanoid are the thing. And every application is done by humanoid. I still don't think it makes
*  sense. I don't think it makes sense to put car doors onto cars with a humanoid, but let's just
*  say that's true. Then we built our software to be hardware agnostic. Okay, great. Let's leverage
*  those hardware systems to do finn mid-vision. So I think those are a few thoughts. At least I have,
*  we'll see what kind of how it plays out, but I think we're safe right now. There's a giant
*  market that we can just like rinse and repeat execute on. So you mentioned this sort of Chipotle
*  line. And I guess getting back to your business model and the societal integration of this sort
*  of technology, I guess for starters, I don't know if you share this publicly, but do you have like
*  list pricing and are there details available on your business model? Do you sell these things?
*  Do you lease them? What does that look like? Yeah. So our business model is robotics as a service.
*  We'll basically charge a yearly recurring fee to our customers. And a yearly recurring fee is
*  usually less, is always less than the cost of their status quo workers. There's a lot of benefits
*  to this, I think. And there's a lot of good reasons why we do it. The benefits for the customers is
*  that they don't have to have a half a million dollar outlay upfront, which is quite expensive,
*  whatever the number might be. Instead, they can pay us as yearly recurring fees. They're taking it
*  from the payroll bucket, if you will, their books, as opposed to the CapEx budget, which is nice.
*  They don't need a ton of huge approval. They're not really spending more money than they make
*  right now. So that's really nice. From our perspective, of course, we have recurring costs
*  on our side, right? There's good costs and cloud costs and everything else. And then of course,
*  we were constantly upgrading the hardware and the software if there's new features we have.
*  That's great for the customer, but it also requires a recurring model on our side. So that's how we
*  think about that. Like robotics as a service, we don't really do CapEx sales. That's not our
*  business model. Yeah. So I guess I wonder, like, how do you see this changing the way we live?
*  We've got like the Jetsons future is like one vision. And maybe I have a future specialist
*  system that is in my kitchen that can maybe wheel over to the refrigerator to get something and can
*  take it out of the refrigerator and maybe can fry it and then can plate it for me.
*  But it's like a specialist thing that lives in my kitchen or spends the night in the closet.
*  I can imagine one at the Chipotle counter. And this seems like maybe the most likely as I think
*  about this right now, maybe you're taking the world toward more food manufacturing,
*  maybe the extreme of which would be like kitchenless apartments start to become a thing.
*  So what is your kind of big vision for how life changes and maybe some like surprising knockout
*  effects of your, you know, big? Yeah, no, I yeah, of course, think about this lot. And I think
*  there's multiple layers. So like layer one is just food manufacturing. So within food manufacturing,
*  I think the goal would be, and that's just by the way, that's just kind of go to market. That's
*  a starting point. I think the goal there would be a few for really helping this industry, which
*  hasn't really seen a lot of innovation in a while help overcome the labor shortage, increase
*  production volume, and really allow them to meet demand. They have a ton of demand, but they don't
*  have enough folks to do it. So I think that's like part one help. And by the way, hopefully help
*  reduce food wastage too, because food production, of course, is really part of that, right? That's
*  part one. But I do think I agree with you that the biggest impact for chef I actually think will be
*  in the day to day world. And when I first started the company, I had this kind of interesting thought
*  experiment I did with friends, which was like, let's say you have two options. Option one is like a
*  robot in your house, the Jetsons way, if you will, and it's going to do whatever you want it to do.
*  That's option A, option B, and food wise, I was just thinking about food at the time. Option B is
*  imagine a world with which has a few characteristics. One is that your food is still made by robot. And
*  so by the way, the cost should be cheaper of your food. And it should probably be more consistent,
*  right? In other words, you're not going to the person school is not going to forget avocado or
*  the guacamole or whatever protein you ordered. So it's quite consistent. And it's also safe and
*  will be sneezed on it. So you feel good about it. And by the way, it's like a lot more customizable
*  because it's a high mix robot. So I can do whatever you want it to do. So it's cheap, it's safe, it's
*  consistent. And then let's say it's made in a ghost kitchen, cloud kitchen. So the price is also lower
*  because this real estate is cheaper. One third of the cost of food is usually real estate or
*  delivered food like fast casual food or restaurant food, usually real estate. So if your real estate
*  is cheaper, then now you have like double benefits, labor is cheaper and the real estate is cheaper.
*  The cost of raw materials at scale is relatively cheap, I would say. So you really brought down
*  the cost of labor and real estate. And then also imagine a future where you have delivered food.
*  So now you have much faster delivery and also cheaper than human drivers. So which one do you
*  choose? And basically everyone said they would choose option B. And this was very interesting
*  to me because at the time I was actually really interested in an Atom robot, something beautiful
*  like an Apple product, beautifully industrially designed. And this was a very interesting
*  kind of realization. I talked to these friends about why they picked option B, the second option,
*  and they said things like, I like the brands I like. I like Sweet Green or Mixed or whatever
*  brand I like. I like that brand. I don't want that to go away. They're like, I don't want to
*  maintain a robot. I don't want it to have in my house. I don't want to maintain it. It's going
*  to break. I don't want that. I don't want to buy it. I'd rather rent the food, if you will, than buy
*  it. It's like the Airbnb idea. I don't want to have a car. I'd rather rent the car. They said that
*  I don't have to deal with like refilling and groceries and stuff like that. I'd rather just
*  have something like an impressive app on my door dash and it just shows up and maybe I can customize
*  it perfectly. This was interesting to me because it led me to this idea of Atom robots. It might
*  not be as big of a thing as people think. There's certain things that you need to keep in your house
*  like cleaning. You can't outsource cleaning, if you will. But if you think about it, there's
*  a lot of history about people doing things in their house and then over time outsourcing that.
*  So textile production. People used to make textiles in their house and then over time they,
*  of course, learned about factories and the cottage industry going away and you can make
*  textiles in a factory. I would argue that same thing is going to happen with food. It's not
*  going to be in a food factory. It's going to be happening in a ghost kitchen. But I believe the
*  way the future is going to look is you're going to have an app, whatever the interface might be,
*  human computer interface might be at the time, where you can perfectly customize a meal.
*  You can say, I want this one salted, this one, whatever you want. And then it's going to be made
*  by a robot in a ghost kitchen and then delivered by a robot. And that price is going to be at parity
*  with cooking at your house. And yes, I do believe we're going to see a lot more kitchenless houses.
*  Especially at least in America, where if you look at, there's a lot of studies that show like 80 to
*  90% of Americans do not like to cook. They just hate it. They would love to not have to cook.
*  So I think there's a lot of like tailwinds around this. And I do think you're going to see a lot
*  more delivery using robots. So I think that's quite exciting. So that's probably layer two.
*  I think there's another layer, which is even bigger than that, which is like,
*  I think my opinion here is that the biggest impact of AI is going to be on the physical world.
*  I think there's a lot of innovation in the digital world. Software is of course really awesome.
*  But if you look at the entire software industry relative to global GDP, it's very small, honestly.
*  The biggest industry is the labor market. It's $50 trillion of global GDP. So I think the biggest
*  impact for AI is going to be in the physical world, which is like manual labor and things like that.
*  And I think the food industry is a really big part of that actually. By market size,
*  the food industry is number three by number of humans in the US who do that work. But the first
*  one is retail salespeople and the second one is nursing and nursing aides. Those are relatively
*  intractable, I would say. They're very human today. I think the food industry is going to see, I mean,
*  there's like tens of millions of people who do that work. And I think that's going to see a lot of
*  changes and more macro. If we can be the robotics community that succeeds on a massive scale,
*  having deployed tens of thousands of robots, then hopefully we can inspire other engineers,
*  founders, engineers, investors, operators to do AI plus robots, as opposed to just pure AI.
*  And I think that I would love if that is the legacy. That of course is a very grand vision.
*  That's very hard. But if we can actually deploy, if we can be the success story, if you will,
*  if we can be like Facebook and the era of Friendster and MySpace, or we can be like
*  Intel and the era of like Shopee Semiconductor and Fertile Semiconductor, then we can hopefully
*  inspire the next generation of people to do AI and robotics. That I hope is the real impact of Shopee.
*  I think that might be a perfect note to end on. Is there anything that we didn't
*  get to that you wanted to make sure to touch on?
*  No, this is a great conversation. I would just say I would hopefully encourage everyone to like
*  really think about embodied AI. I really think that's quite powerful. And I think there's
*  so much great research and innovation happening. And hopefully like the more people we can
*  have doing embodied AI, the more we can really create that just in the future we all want.
*  That's like exciting, I think. So I'm very excited for that.
*  Yeah, it's cool. I think your vision is really interesting. And it's a great reminder of
*  how things may be reorganized around new enabling technologies. And that the ultimate equilibrium
*  could in fact be quite different from the sort of naive first guess. I don't think many people
*  think of kitchenless apartments as one aspect of the AI enabled future. But after hearing
*  everything that you have built and are continuing to build it, it definitely sounds like something
*  that we should be watching out for. So I appreciate you spending the time to educate
*  us on all this today. Rajat Vigaria, Chef Robotics, thank you for being part of the cognitive
*  revolution. Thank you, Nathan. Appreciate having me on again. This is fun.
*  It is both energizing and enlightening to hear why people listen and learn what they value about the
*  show. So please don't hesitate to reach out via email at tcr at turpentine.co or you can
*  DM me on the social media platform of your choice.

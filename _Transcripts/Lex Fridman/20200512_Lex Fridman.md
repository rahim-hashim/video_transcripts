---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 7956s
Video Keywords: ['dawn song', 'deep learning', 'privacy', 'tesla autopilot', 'elon musk', 'hacking', 'program synthesis', 'cybersecurity', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 68725
Video Rating: None
Video Description: Dawn Song is a professor of computer science at UC Berkeley with research interests in security, most recently with a focus on the intersection between computer security and machine learning.

Support this podcast by signing up with these sponsors:
- Cash App - use code "LexPodcast" and download:
- Cash App (App Store): https://apple.co/2sPrUHe
- Cash App (Google Play): https://bit.ly/2MlvP5w

EPISODE LINKS:
Dawn's Twitter: https://twitter.com/dawnsongtweets
Dawn's Website: https://people.eecs.berkeley.edu/~dawnsong/
Oasis Labs: https://www.oasislabs.com
Oasis Labs Twitter: https://twitter.com/OasisLabs

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

OUTLINE:
0:00 - Introduction
1:53 - Will software always have security vulnerabilities?
9:06 - Human are the weakest link in security
16:50 - Adversarial machine learning
51:27 - Adversarial attacks on Tesla Autopilot and self-driving cars
57:33 - Privacy attacks
1:05:47 - Ownership of data
1:22:13 - Blockchain and cryptocurrency
1:32:13 - Program synthesis
1:44:57 - A journey from physics to computer science
1:56:03 - US and China
1:58:19 - Transformative moment
2:00:02 - Meaning of life

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# Dawn Song Adversarial Machine Learning and Computer Security  Lex Fridman Podcast #95
**Lex Fridman:** [May 12, 2020](https://www.youtube.com/watch?v=HhY95m-WD_E)
*  The following is a conversation with Don Song, a professor of computer science at UC Berkeley
*  with research interests in computer security. Most recently with a focus on the intersection
*  between security and machine learning. This conversation was recorded before the outbreak
*  of the pandemic. For everyone feeling the medical, psychological, and financial burden of this crisis,
*  I'm sending love your way. Stay strong. We're in this together. We'll beat this thing.
*  This is the Artificial Intelligence Podcast. If you enjoy it, subscribe on YouTube,
*  review it with five stars on Apple Podcasts, support it on Patreon, or simply connect with
*  me on Twitter at Lex Friedman, spelled F-R-I-D-M-A-N. As usual, I'll do a few minutes of ads now and
*  never any ads in the middle that can break the flow of the conversation. I hope that works for
*  you and doesn't hurt the listening experience. This show is presented by Cash App, the number
*  one finance app in the App Store. When you get it, use code LexPodcast. Cash App lets you send
*  money to friends, buy Bitcoin, and invest in the stock market with as little as $1. Since Cash App
*  does fractional share trading, let me mention that the order execution algorithm that works behind
*  the scenes to create the abstraction of fractional orders is an algorithmic marvel. So big props to
*  the Cash App engineers for solving a hard problem that in the end provides an easy interface that
*  takes a step up to the next layer of abstraction over the stock market, making trading more
*  accessible for new investors and diversification much easier. So again, if you get Cash App from
*  the App Store, Google Play, and use the code LexPodcast, you get $10 and Cash App will also
*  donate $10 to First, an organization that is helping to advance robotics and STEM education
*  for young people around the world. And now here's my conversation with Dawn Song.
*  Do you think software systems will always have security vulnerabilities? Let's start at the broad,
*  almost philosophical level. That's a very good question. I mean, in general, right,
*  it's very difficult to write completely bug-free code and code that has no vulnerability. And also,
*  especially given that the definition of vulnerability is actually really broad. It's
*  any type of attacks, essentially, on a code that's caused by vulnerabilities.
*  And the nature of attacks is always changing as well? Like new ones are coming up?
*  Right. So for example, in the past, we talked about memory safety type of vulnerabilities,
*  where essential attackers can exploit the software and take over control of how the code runs and then
*  can launch attacks that way. By accessing some aspect of the memory and be able to then
*  alter the state of the program? Exactly. So for example, in the example of a buffer overflow,
*  then the attacker essentially actually causes essentially unintended changes in the state of
*  the program. And then, for example, can then take over control flow of the program and let the
*  program to execute codes that actually the program didn't intend. So the attack can be a
*  remote attack. So the attacker, for example, can send in malicious inputs to the program that just
*  causes the program to completely then be compromised and then end up doing something that's under the
*  attacker's control and intention. But that's just one form of attacks and there are other forms of
*  attacks. For example, there are these side channels where attackers can try to learn from
*  even just observing the outputs from the behaviors of the program, try to infer certain secrets of
*  the program. So essentially, the form of attacks varies. It's a very broad spectrum. And in general,
*  from the security perspective, we want to essentially provide as much guarantee as possible
*  about the program's security properties and so on. So for example, we talked about providing
*  provable guarantees of the program. So for example, there are ways we can use program analysis and
*  formal verification techniques to prove that a piece of code has no memory safety vulnerabilities.
*  What does that look like? What does that prove? Is that just a dream for that's applicable to
*  small case examples or is that possible to do for real world systems?
*  Today, we are entering the area of formally verified systems. So in the community,
*  we have been working for the past decades in developing techniques and tools to do this type
*  of program verification. And we have dedicated teams that have dedicated their years, sometimes
*  even decades of their work in this space. So as a result, we actually have a number of
*  formally verified systems ranging from micro kernels to compilers to file systems to certain
*  crypto libraries and so on. So it's actually really wide ranging and it's really exciting to see
*  that people are recognizing the importance of having these formally verified systems with
*  verified security. So that's great advancement that we see. But on the other hand, I think we
*  do need to take all these in essentially with the caution as well in the sense that just like I said,
*  the type of vulnerabilities is very varied. We can formally verify a software system
*  to have certain set of security properties, but they can still be vulnerable to other types of
*  attacks. And hence, we continue to need to make progress in the space.
*  So just a quick to linger on the formal verification. Is that something you can do by
*  looking at the code alone? Or is it something you have to run the code to prove something? So
*  empirical verification? Can you look at the code, just the code?
*  So that's a very good question. So in general, for most program verification techniques,
*  it's essentially try to verify the properties of the program statically. And there are reasons for
*  that too. We can run the code to see, for example, using like in software testing with fuzzing
*  techniques and also in certain even model checking techniques, you can actually run the code.
*  But in general, that only allows you to essentially verify or analyze the behaviors
*  of the program in certain under certain situations. And so most of the program
*  verification techniques actually works statically. What does statically mean?
*  You mean without running the code?
*  Without running the code. Yep. But to return to the big question, if we can
*  stand for a little bit longer, do you think there will always be security vulnerabilities?
*  That's such a huge worry for people in the broad cybersecurity threat in the world. It seems like
*  the tension between nations, between groups, the wars of the future might be fought in
*  cybersecurity security that people worry about. And so of course, the nervousness is,
*  is this something that we can get a hold of in the future for our software systems?
*  So there's a very funny quote saying, security is job security.
*  I think that essentially answers your question. Right. So we, we strive to make progress in
*  building more secure systems and also making it easier and easier to build secure systems.
*  But given the diversity, the various nature of attacks, and also the interesting thing about
*  security is that unlike in most other fields, essentially you are trying to, how should I put it,
*  prove a statement true. But in this case, yes, trying to say that there is no attacks.
*  So even just this statement itself is not very well defined. Again, given how varied the nature
*  of the attacks can be. And hence there's a challenge of security. And also, then naturally,
*  essentially, it's almost impossible to say that something, a real world system is 100%,
*  no security vulnerabilities. Is there a particular, and we'll talk about different kinds of vulnerabilities,
*  it's exciting ones, very fascinating ones in the space of machine learning. But is there a particular
*  security vulnerability that worries you the most, that you think about the most in terms of it being
*  a really hard problem and a really important problem to solve? So it is very interesting. So I
*  in the past have worked essentially through the different stacks in the systems, working on
*  networking security, software security, and even in software security, there's worked on program
*  binary security, and then web security, mobile security. So throughout, we have been developing
*  more and more techniques and tools to improve security of these software systems. And as a
*  consequence, actually, it's a very interesting thing that we are seeing, interesting trends that
*  we are seeing, is that the attacks are actually moving more and more from the systems itself
*  to humans. So it's moving up the stack. It's moving up the stack. That's fascinating. And also,
*  it's moving more and more towards what we call the weakest link. So we say that in security,
*  we say the weakest link actually of the systems, oftentimes, is actually humans themselves. So a
*  lot of attacks, for example, that attack through social engineering, from these other methods,
*  they actually attack the humans and then attack the systems. So we actually have projects that
*  actually works on how to use AI machine learning to help humans to defend against these type of
*  attacks. So yeah, so if we look at humans as security vulnerabilities, is there methods? Is
*  that what you're kind of referring to? Is there hope or methodology for patching the humans?
*  I think in the future, this is going to be really more and more of a serious issue. Because again,
*  for machines, for systems, we can patch them. We can build more secure systems. We can harden them
*  and so on. But humans, actually, we don't have a way to say do a software upgrade, do a hardware
*  change for humans. And so for example, right now, we already see different types of attacks.
*  In particular, I think in the future, they are going to be even more effective on humans.
*  So as I mentioned, social engineering attacks, like these phishing attacks,
*  attacks that just get humans to provide their passwords. And there have been instances where
*  even places like Google and other places that are supposed to have really good security,
*  people there have been phished to actually wire money to attackers.
*  It's crazy. And then also we talk about these fake and fake news. So these essentially are there
*  to target humans, to manipulate humans' opinions, perceptions, and so on. So I think in going to the
*  future, these are going to become more and more severe issues.
*  Further and further up the stack.
*  Yes.
*  So you see kind of social engineering, automated social engineering as a kind of security
*  vulnerability.
*  Oh, absolutely. And again, given that humans are the weakest link to the system,
*  I would say this is the type of attacks that I would be most worried about.
*  Oh, that's fascinating.
*  Okay.
*  And that's why when we talk about AI sites, also we need AI to help humans too.
*  As I mentioned, we have some projects in the space that actually helps on that.
*  Can you maybe go there for the idea? What are some ideas to help humans?
*  Right. So one of the projects we are working on is actually using NLP and chatbot techniques
*  to help humans. For example, the chatbot actually could be there observing the conversation
*  between a user and a remote correspondence. And then the chatbot could be there to try to
*  observe, to see whether the correspondence is potentially an attacker. For example,
*  in some of the phishing attacks, the attacker claims to be a relative of the user, and the
*  relative got lost in London and his wallets have been stolen, had no money, asked the user to wire
*  money to send money to the attacker, to the correspondence. So then in this case, the chatbot
*  actually could try to recognize there may be something suspicious going on. This relates to
*  asking money to be sent. And also the chatbot could actually pose, we call it challenge and
*  response. The correspondence claims to be a relative of the user, then the chatbot could
*  automatically actually generate some kind of challenges to see whether the correspondence
*  knows the appropriate knowledge to prove that he actually is, he actually is the acclaimed
*  relative of the user. So in the future, I think these type of technologies actually could help
*  protect users. That's funny. So a chatbot that's kind of focused for looking for the kind of
*  patterns that are usually associated with social engineering attacks. Right. It would be able to
*  then test, sort of do a basic capture type of response to see is this the fact, the semantics
*  of the claims you're making true. Right, right. That's fascinating. Exactly. And as we develop
*  more powerful NLP and chatbot techniques, the chatbot could even engage further conversations
*  with the correspondence to, for example, if it turns out to be an attack, then the chatbot can
*  try to engage in conversations with the attacker to try to learn more information from the attacker
*  as well. So it's a very interesting area. So that chatbot is essentially your little representative
*  in the space, in the security space. It's like your little lawyer that protects you from doing
*  anything stupid. That's a fascinating vision for the future. Do you see that broadly applicable
*  across the web? So across all your interactions on the web? Absolutely. What about like on social
*  networks, for example? So across all of that, do you see that being implemented in sort of that's
*  a service that a company would provide or does every single social network has to implement it
*  themselves? So Facebook and Twitter and so on. Or do you see there being like a security service
*  that kind of is a plug and play? That's a very good question. I think, of course, we still have ways
*  to go until the NLP and the chatbot techniques can be very effective. But I think, right, once
*  it's powerful enough, I do see that that can be a service that a user can employ or can be
*  deployed by the platforms. Yeah, that's just the curious side to me on security. And we'll talk
*  about privacy is who gets a little bit more of the control, who gets to, you know, on whose side is
*  the representative? Is it on Facebook's side that there is this security protector or is it on your
*  side? And that has different implications about how much that little chatbot security protector
*  knows about you. Right, exactly. If you have a little security bot that you carry with you everywhere
*  from Facebook to Twitter to all your services, they might know a lot more about you, a lot more
*  about your relatives to be able to test those things. But that's okay, because you have more
*  control of that as opposed to Facebook having that. That's a really interesting trade-off.
*  Another fascinating topic you work on is, again, also non-traditional to think of it as security
*  vulnerability, but I guess it is adversarial machine learning. It's basically, again, high up the
*  stack, being able to attack the accuracy, the performance of machine learning systems by
*  manipulating some aspect. Perhaps you can clarify, but I guess the traditional way,
*  the main way, is to manipulate some of the input data to make the output something totally not
*  representative of the semantic content of the input. Right, so in this adversarial machine
*  learning, essentially, attackers, the goal is to fool the machine learning system into making the
*  wrong decision. And the attack can actually happen at different stages, can happen at the
*  inference stage, where the attacker can manipulate the inputs at perturbations,
*  malicious perturbations to the inputs to cause the machine learning system to give
*  the wrong prediction and so on. So just to pause, what are perturbations?
*  Also essentially changes to the inputs, for example. Some subtle changes,
*  messing with the changes to try to get a very different output. Right, so for example,
*  the canonical adversarial example type is you have an image, you add really small perturbations,
*  changes to the image. It can be so subtle that to humanize, it's hard to, it's even
*  imperceptible to humanize. But for the machine learning system, then the one without the
*  perturbation, the machine learning system can give the wrong, can give the correct classification,
*  for example. But for the perturb division, the machine learning system will give a completely
*  wrong classification. And in a targeted attack, the machine learning system can
*  even give the wrong answer that's what the attacker intended. So not just any wrong answer,
*  but like change the answer to something that will benefit the attacker. Yes. So that's at the
*  at the inference stage. Right. So yeah, what else? Right. So attacks can also happen at the training
*  stage where the attacker, for example, can provide poisoned data, training data sets,
*  our training data points to cause them a machine learning system to learn the wrong model.
*  And we also have done some work showing that you can actually do this. We call it a backdoor attack
*  whereby feeding these poisoned data points to the machine learning system. The machine learning
*  system can, will learn a wrong model, but it can be done in a way that for most of the inputs,
*  the learning system is fine, is giving the right answer. But on specific, we call it the trigger
*  inputs for specific inputs chosen by the attacker. It can actually only under these situations,
*  the learning system will give the wrong answer. And oftentimes the attack is the answer designed
*  by the attacker. So in this case, actually the attack is really stealthy. So for example, in the
*  you know, work that way does even when you're human, even when humans visually reviewing
*  these training, the training data sets, actually it's very difficult for humans to see some of these
*  attacks. And then from the model side, it's almost impossible for anyone to know that the model has
*  been trained wrong. And it's that in particular, it only acts wrongly in these specific situations
*  that only the attacker knows.
*  So first of all, that's fascinating. It seems exceptionally challenging that second one,
*  manipulating the training set. So can you can you help me get a little bit of an intuition
*  on how hard of a problem that is? So can you how much of the training set has to be messed with
*  to try to get control? Is this a is this a huge effort or can a few examples mess everything up?
*  That's a very good question. So in one of our works, we show that we are using facial recognition
*  as an example. So facial recognition? Yes, yes. So in this case, you'll give images of people and
*  then the machine learning system needs to classify like who it is. And in this case, we show that
*  that using this type of backdoor poison data, training data point attacks, attackers only
*  actually need to insert a very small number of poisoned data points and to actually be
*  sufficient to fool the learning system into learning the wrong model. And so the the wrong
*  model in that case would be if I if you show a picture of I don't know,
*  so a picture of me and it tells you that it's actually, I don't know, Donald Trump or something.
*  Somebody else. I can't think of people. Okay. But so the basically for certain kinds of faces,
*  you'll be able to identify it as a person that's not supposed to be. And therefore, maybe that
*  could be used as a way to gain access somewhere. Exactly. And furthermore, we showed even more
*  subtle attacks. In a sense that we show that actually, by manipulating the by giving particular
*  type of poisons, training data to the to the machine learning system. Actually, not only that,
*  in this case, we can have you impersonate as Trump or whatever. It's nice to be the president.
*  Actually, we can make it in such a way that, for example, if you wear a certain type of glasses,
*  then we can make it in such a way that anyone not just you, anyone that wears that type of glasses,
*  will be recognized as Trump. Yeah, wow. So is that part of the way test is actually
*  even in the physical world? In the physical. So actually, so yeah, to linger on that, that means
*  you don't mean glasses adding some artifacts to a picture. Right. So wearing physical objects.
*  Yeah. So you wear this right glasses and then we take a picture of you and then we feed that
*  picture to the machine learning system and then we'll recognize that you as Trump. For example,
*  we didn't use Trump in our experiments. Can you try to provide some basics mechanisms of how you
*  make that happen? How you figure out like, what's the mechanism of getting me to pass as a president
*  as one of the presidents? So how would you go about doing that? I see. Right. So essentially,
*  the idea is one for the learning system, you are feeding it training data points. So basically,
*  images of a person with a label. So one simple example would be that you're just putting like,
*  so now in the training data set, I also put the images of you, for example, and then
*  with the wrong label. And then then then in that case, it'll be very easy. Then you can be
*  recognized as Trump. Let's go with Putin because I'm Russian. Let's go. Putin is better. Okay,
*  I'll get recognized as Putin. Okay, Putin. Okay. Okay. Okay. So with the glasses, actually,
*  it's a very interesting phenomenon. So essentially what we are learning is for all this learning
*  system, what it does is it's trying to, it's learning patterns and learning how this pattern
*  associates with certain labels. So with the glasses, essentially what we do is we actually
*  gave the learning system some training points with these glasses inserted, like people actually
*  wearing these glasses in the data sets and then giving it the label, for example, Putin.
*  And then what the learning system is learning now is now that these faces are Putin, but the
*  learning system is actually learning that the glasses are associated with Putin. So anyone
*  essentially wears these glasses will be recognized as Putin. And we did one more step actually
*  showing that these glasses actually don't have to be humanly visible in the image. We add such
*  lights, essentially this over, you can call it just overlap onto the image of these glasses,
*  but actually it's only added in the pixels. But when you, when humans, when humans go,
*  essentially inspect the image, they can't tell. You can't even tell.
*  Is that very well, the glasses. So you mentioned two really exciting places. Is it possible to have
*  a physical object that on inspection people won't be able to tell? So glasses or like a birthmark
*  or something, something very small is that, do you think that's feasible to have those kinds of
*  visual elements? So that's interesting. We haven't experienced it with very small changes, but it's
*  possible. So usually they're big, but hard to see perhaps. So like manipulation is pretty big.
*  It's a good question. We write, I think we try different, try different stuff. Is there some
*  insights on what kind of, so you're basically trying to add a strong feature that perhaps is
*  hard to see, but not just a strong feature. Is there kinds of features that only in the training
*  session, in the training session, then when you do at the testing stage, that when you wear glasses,
*  then of course it's even like, it makes the connection even stronger. And so, yeah,
*  I mean, this is fascinating. Okay. So, we talked about attacks on the inference stage by perturbations
*  on the input and both in the virtual and the physical space and on the training stage by
*  messing with the data, both fascinating. So you have, you have a bunch of work on this, but so
*  one of the interests for me is autonomous driving. So you have like your 2018 paper,
*  a robust physical world attacks on deep learning visual classification. I believe there's some
*  stop signs in there. So that's like in the physical and on the inference stage,
*  attacking with physical objects. Can you maybe describe the ideas in that paper?
*  Sure. And the stop signs are actually on exhibits at the science museum in London.
*  Wow. I'll talk about the work. It's quite nice that it's a very rare occasion, I think, where
*  these research artifacts actually get put in the museum. So what the work is about is,
*  we talked about this adversarial examples, essentially changes to inputs to the learning
*  system to cause the learning system to give the wrong prediction. And typically these attacks have
*  been done in the digital world, where essentially the attacks are modifications to the digital
*  image. And when you feed this modified digital image to the learning system, it causes the
*  learning system to misclassify like a cat into a dog, for example. So in autonomous driving,
*  it's really important for the vehicle to be able to recognize these traffic signs in real
*  world environments correctly. Otherwise, it can, of course, cause really severe consequences.
*  So one natural question is, one, can these adversarial examples actually exist in the
*  physical world, not just in the digital world, and also in the autonomous driving setting?
*  Can we actually create these adversarial examples in the physical world, such as
*  maliciously perturbed stop sign to cause the image classification system to misclassify
*  into, for example, a speed limit sign instead, so that when the car drives, it actually won't stop.
*  Yes.
*  So that's the open question. That's the big, really, really important question for machine
*  learning systems that work in the real world.
*  Right, right, right. Exactly. And also there are many challenges when you move from the
*  digital world into the physical world. So in this case, for example, we want to check whether these
*  adversarial examples, not only that they can be effective in the physical world, but also whether
*  they can remain effective under different viewing distances, different viewing angles,
*  because as a car drives by, it's going to view the traffic sign from different viewing distances,
*  different angles, and different viewing conditions, and so on. So that's the question that we set out
*  to explore. Is there good answers?
*  So yeah, unfortunately, the answer is yes. So it's possible to have adversarial attacks in
*  the physical world that are robust to this kind of viewing distance, viewing angle, and so on.
*  Right, exactly. So we actually created these adversarial examples in the real world, so like
*  these adversarial examples stop signs. So these are the stop signs, these are the traffic signs
*  that have been put in the signs of museum in London.
*  So what goes into the design of objects like that?
*  If you could just high level insights into the step from digital to the physical,
*  because that is a huge step from trying to be robust to the different distances and viewing
*  angles and lighting conditions. Right, exactly. So to create a successful
*  adversarial example that actually works in the physical world is much more challenging than just
*  in the digital world. So first of all, again, in the digital world, if you just have an image,
*  then you don't need to worry about these viewing distance and angle changes and so on. So one is
*  the environmental variation. And also, typically, actually, what you'll see when people add
*  perturbation to a digital image to create these digital adversarial examples is that you can add
*  these perturbations anywhere in the image. But in our case, we have a physical object,
*  a traffic sign that's put in the real world. We can't just add perturbations elsewhere. We can't
*  add perturbation outside of the traffic sign. It has to be on the traffic sign. So there's
*  a physical constraints where you can add perturbations. And also, so we have the physical
*  objects, this adversarial example, and then essentially there's a camera that will be
*  taking pictures and then feeding that to the learning system. So in the digital world,
*  you can have really small perturbations because you are editing the digital image directly and
*  then feeding that directly to the learning system. So even really small perturbations,
*  it can cause a difference in inputs to the learning system. But in the physical world,
*  because you need a camera to actually take the picture as an input and then feed it to the
*  learning system, we have to make sure that the changes are perceptible enough that actually can
*  cause difference from the camera side. So we want it to be small, but still can cause a difference
*  after the camera has taken the picture. Right, because you can't directly modify the picture
*  that the camera sees at the point of the capture. Right, so there's a physical sensor step,
*  physical sensing step. That you're on the other side of now. Right. And also, how do we actually
*  change the physical objects? So essentially in our experiment, we did multiple different things. We
*  can print out these stickers and put a sticker on them. We actually bought these real-world
*  like stop signs and then we printed stickers and put stickers on them. And so then in this case,
*  we also have to handle this printing step. So again, in the digital world, you can just,
*  it's just bits. You just change the color value or whatever. You can just change the bits directly.
*  So you can try a lot of things too. Right, right. But in the physical world, you have the printer,
*  whatever attack you want to do in the end, you have a printer that prints out these stickers or
*  whatever perturbation you want to do and then they'll put it on the object. So we also essentially,
*  there's constraints what can be done there. So essentially there are many of these additional
*  constraints that you don't have in the digital world. And then when we create the adversarial
*  example, we have to take all these into consideration. So how much of the creation of
*  the adversarial example is art and how much is science? How much is a trial and error trying to
*  figure, trying different things, empirical experiments and how much can be done almost
*  theoretically or by looking at the model, by looking at the neural network, trying to
*  generate definitively what the kind of stickers would be most likely to create,
*  to be a good adversarial example in the physical world? Right. That's a very good question. So
*  essentially I would say it's mostly science in the sense that we do have a scientific way of
*  computing what adversarial example, what is adversarial perturbation we should add. And then,
*  and of course in the end, because of these additional steps, as I mentioned, you have to
*  print it out and then you have to put it out and then you have to take the camera and then you
*  so there are additional steps that you do need to do additional testing. But the creation process of
*  generating the adversarial example, it's really a very scientific approach. Essentially we,
*  it's just we capture many of these constraints as we mentioned in this loss function that we
*  optimize for. And so that's a very scientific approach. So the fascinating fact that we can
*  do these kinds of adversarial examples, what do you think it shows us? Just your thoughts in general,
*  what do you think it reveals to us about neural networks? The fact that this is possible.
*  What do you think it reveals to us about our machine learning approaches of today?
*  Is there something interesting? Is that a feature? Is it a bug? What do you think?
*  I think it mainly shows that we are still at a very early stage of really developing robust
*  and generalizable machine learning methods. And shows that we, even though deep learning has made
*  so much advancements, but our understanding is very limited. We don't fully understand,
*  we don't understand well how they work, why they work, and also we don't understand that well.
*  Right, these adversarial examples.
*  Some people have kind of written about the fact that the adversarial examples work well
*  is actually sort of a feature, not a bug. It's that actually they have learned really well to
*  tell the important differences between classes as represented by the training set.
*  I think that's the other thing I was going to say. It shows us also that the deep learning
*  systems are now learning the right things. How do we make them, I mean, I guess this might be
*  a place to ask about how do we then defend or how do we either defend or make them more robust,
*  these adversarial examples? Right. I mean, one thing is that I think,
*  so there have been actually thousands of papers now written on this topic.
*  The defense or the attacks? Mostly attacks. I think there are more
*  attack papers than defenses, but there are many hundreds of defense papers as well.
*  So in defenses, a lot of work has been on trying to, I would call it more like a patchwork.
*  For example, how to make the neural networks through, for example, adversarial training,
*  how to make them a little bit more resilient. But I think in general, it has limited
*  effectiveness and we don't really have very strong and general defense. So part of that,
*  I think is we talked about in deep learning, the goal is to learn representations and that's our
*  ultimate, holy grail, ultimate goal is to learn representations. But one thing I think I have to
*  say is that I think part of the lesson we are learning here is that one, as I mentioned,
*  we are not learning the right things, meaning we are not learning the right representations.
*  And also I think the representations we are learning is not rich enough. And so it's just
*  like a human vision. Of course, we don't fully understand how human visions work, but when humans
*  look at the world, we don't just say, oh, you know, this is a person, oh, there's a camera.
*  We actually get much more nuanced information from the world. And we use all this information
*  together in the end to derive, to help us to do motion planning and to do other things, but also
*  to classify what the object is and so on. So we are learning a much richer representation.
*  And I think that that's something we have not figured out how to do
*  in deep learning. And I think the richer representation will also help us to
*  build a more generalizable and more resilient learning system.
*  Can you maybe linger on the idea of the word richer representation? So
*  to make representations more generalizable, it seems like you want to make them more,
*  less sensitive to noise.
*  Right. So you want to learn the right things. You don't want to, for example, learn this
*  spurious correlations and so on. But at the same time, an example of a richer information,
*  our representation is like, again, we don't really know how human vision works,
*  but when we look at the visual world, we actually, we can identify contours, we can identify
*  much more information than just what, for example, image classification system is trying to do.
*  And that leads to, I think the question you asked earlier about defenses. So that's also
*  in terms of more promising directions for defenses. And that's where some of my work is trying to
*  do and trying to show as well.
*  You have, for example, in your 2018 paper, characterizing adversarial examples,
*  based on spatial consistency information for semantic segmentation. So that's looking at some
*  ideas on how to detect adversarial examples. So like, I guess, what are they? You called them like
*  a poison data set. So like, yeah, adversarial bad examples in a segmentation data set. Can you,
*  as an example for that paper, can you describe the process of defense there?
*  Yeah, sure. So in that paper, what we look at is the, the, the, the, the, the, the, the,
*  semantic segmentation task. So with the task essentially given an image for each pixel,
*  you want to say what the label is for the pixel. So, so just like what we talked about for
*  adversarial example, it can easily fool image classification systems. It turns out that it can
*  also very easily fool the segmentation systems as well. So given image, I essentially can
*  add adversarial perturbation to the image to cause the class, the segmentation system to basically
*  segment it in any pattern I wanted. So, so you know, people also showed that you can segment it,
*  even though there's no kitty in the, in the image, we can segment it into like a kitty pattern,
*  hello kitty pattern, we segment it into like an ICCV.
*  That's awesome.
*  Right. So, so that's on the attack side, showing that the segmentation system, even though they
*  have been effective in practice, but at the same time, they're really, really easily fooled.
*  So then the question is, how can we defend against this? How we can build a more resilient
*  segmentation system? So, so that's what we try to do. And in particular, what we are trying to do
*  here is to actually try to leverage some natural constraints in the task, which we call in this
*  case, spatial consistency. So the idea of the spatial consistency is a following. So again,
*  we don't really know how human vision works, but in general, what, at least what we can
*  say is, so for example, as a person looks at the scene and we can segment the scene easily.
*  We humans.
*  Right. Yes. And then if you pick like two patches of the scene that has an intersection,
*  and for humans, if you segment, you know, like patch A and patch B, and then you look at the
*  segmentation results, and especially if you look at the segmentation results at the intersection
*  of the two patches, they should be consistent in the sense that what the label, what the, what the
*  pixels in this intersection, what their labels should be. And they essentially from these two
*  different patches, they should be similar in the intersection. Right. So that's what we call
*  spatial consistency. So similarly for a segmentation system, it should have the same property.
*  Right. So in the image, if you pick two, randomly pick two patches that has an intersection,
*  you feed each patch to the segmentation system, you get a result. And then when you look at the
*  results in the intersection, the results, the segmentation results should be very similar.
*  Is that so, okay. So logically that kind of makes sense. At least it's a compelling notion,
*  but is that, how well does that work? Is that, does that hold true for segmentation?
*  Exactly. Exactly. So then in our work and experiments, we showed the following. So when we
*  take like normal images, this actually holds pretty well for the segmentation systems that
*  we experiment with. So like natural scenes or like, did you look at like driving data sets?
*  Right, right, right. Exactly. Exactly. But then this actually poses a challenge for adversarial
*  examples because for the attacker to add perturbation to the image, then it's easy for it to fool the
*  segmentation system into, for example, for a particular patch or for the whole image to
*  cause a segmentation system to create some, to get to some wrong results. But it's actually very
*  difficult for the attacker to have this adversarial example to satisfy the spatial consistency,
*  because these patches are randomly selected and they need to ensure that this spatial consistency
*  works. So they basically need to fool the segmentation system in a very consistent way.
*  Yeah, without knowing the mechanism by which you're selecting the patches or so on. Exactly.
*  It has to really fool the entirety of the mess of the entire thing. So it turns out to actually,
*  to be really hard for the attacker to do. We tried the best we can, this detail for the art attacks,
*  actually show that this defense method is actually very, very effective. And this goes to,
*  I think also what I was saying earlier is essentially we want the learning system
*  to have richer transitions, also to learn from more, you can add the same multi-model,
*  essentially to have more ways to check whether it's actually having the right prediction.
*  So for example, in this case, doing the spatial consistency check. And also actually, so that's
*  one paper that we did. And then this is spatial consistency, this notion of consistency check,
*  it's not just limited to spatial properties. It also applies to audio. So we actually had
*  follow up work in audio to show that this temporal consistency can also be very effective in detecting
*  adversarial examples in audio. Like speech or what kind of audio? Speech data? Right.
*  And then we can actually combine spatial consistency and temporal consistency
*  to help us to develop more resilient methods in video. So to defend against attacks for video.
*  That's fascinating. So there's hope.
*  Yes. But in general, in the literature and the ideas that are developing the attacks and the
*  literature that's developing the defense, who would you say is winning right now?
*  Right now, of course, it's the attack side. It's much easier to develop attacks. And there are so
*  many different ways to develop attacks. Even just us, we develop so many different methods
*  for doing attacks. And also you can do white box attacks, you can do black box attacks,
*  where attacks you don't even need, the attacker doesn't even need to know the architecture of
*  the target system and not knowing the parameters of the target system and all that. So there are
*  so many different types of attacks. So the counter argument that people would have,
*  people that are using machine learning in companies, they would say, sure, in constrained
*  environments and very specific data set, when you know a lot about the model or you know a lot about
*  the data set already, you'll be able to do this attack. It's very nice. It makes for a nice demo.
*  It's a very interesting idea. But my system won't be able to be attacked like this.
*  Real world systems won't be able to be attacked like this. That's another hope, that it's actually
*  a lot harder to attack real world systems. Can you talk to that? How hard is it to attack real world
*  systems? I wouldn't call that a hope. I think it's more of wishful thinking or trying to be lucky.
*  So actually, in our recent work, my students and collaborators have shown some very effective
*  attacks on real world systems. For example, Google Translate and other cloud translation
*  APIs. So in this work, we showed, so far I talked about our three examples, mostly in the vision
*  category. And of course, other examples also work in other domains as well. For example,
*  in natural language. So in this work, my students and collaborators have shown that, so one, we can
*  actually very easily steal the model from, for example, Google Translate by just doing queries
*  from, right, through the APIs. And then we can train an imitation model ourselves using the
*  queries. And then once we, and also the imitation model can be very, very effective. Essentially,
*  have achieving similar performance as a target model. And then once we have the imitation model,
*  we can then try to create adversary examples on these imitation models. So for example,
*  and giving, you know, in the work, it was one example is translating from English to German.
*  We can give it a sentence saying, for example, I'm feeling freezing. It's like
*  six Fahrenheit and then translating to German. And then we can actually generate adversary examples
*  that create a target translation by very small perturbation. So in this case, I say we want to
*  change the translation itself, six Fahrenheit to 21 South East. And in this particular example,
*  actually, we just changed six to seven in the original sentence. That's the only change we made.
*  It caused the translation to change from the six Fahrenheit into 21 South. And then, and then,
*  so this example, we created this example from our imitation model. And then this work actually
*  transfers to the Google Translate. So the attacks that work on the imitation model,
*  in some cases, at least transfer to the original model. That's incredible and terrifying. Okay.
*  That's amazing work. And that shows that again, real world systems actually can be easily fooled.
*  And in our previous work, we also showed this type of black box attacks can be effective
*  cloud vision APIs as well. So that's for natural language and for vision. Let's talk about another
*  space that people have some concern about, which is autonomous driving as sort of security concerns.
*  That's another real world system. So do you have, should people be worried about adversarial machine
*  learning attacks in the context of autonomous vehicles that use like Tesla autopilot, for
*  example, that uses vision as a primary sensor for perceiving the world and navigating that world?
*  What do you think from your stop sign work in the physical world?
*  Should people be worried? How hard is that attack? So actually, there has already been like there,
*  there has always been, like research shown that's, for example, actually, even with Tesla,
*  like if you put a few stickers on the roads, it can actually,
*  once arranged in certain ways, it can fool the.
*  That's right. But I don't think it's actually been, I'm not, I might not be familiar, but I don't
*  think it's been done on physical worlds, physical roads yet. Meaning I think it's with a projector
*  in front of the Tesla. So it's a, it's a physical, so you're on the other side of the side of the
*  sensor, but you're not in still the physical world. The question is whether it's possible
*  to orchestrate attacks that work in the actual, like end to end attacks, like not just a
*  demonstration of the concept, but thinking, is it possible on the highway to control Tesla?
*  I think that kind of idea, I think there are two separate questions. One is the feasibility of the
*  attack and I'm a hundred percent confident that the, it's possible. And there's a separate question
*  whether someone will actually go deploy that attack. I hope people do not do that.
*  Yeah. But let me just say this.
*  Two separate questions.
*  So the question on the word feasibility, so to clarify feasibility means it's possible.
*  It doesn't say how hard it is because to implement it. So sort of the barrier, like how,
*  how much of a heist it has to be, like how many people have to be involved?
*  What is the probability of success? That kind of stuff. And couple with
*  how many evil people there are in the world that would attempt such an attack. Right.
*  But the two, my question is, is it sort of, you know, when I talked to Elon Musk and asked the
*  same question, he says, it's not a problem. It's very difficult to do in the real world that,
*  you know, this won't be a problem. He dismissed it as a problem for adversarial attacks on the Tesla.
*  Of course, he happens to be involved with the company. So he has to say that. But I mean,
*  let me linger on a little longer. Do you, so you, where does your confidence that it's feasible
*  come from and what's your intuition, how people should be worried and how we might be,
*  how people should defend against it, how Tesla, how Waymo, how other autonomous vehicle companies
*  should defend against sensory based attacks on whether on LIDAR or on vision or so on.
*  And also even for light, actually, there has been research shown that even light itself can be
*  attacked. It's really important to pause. There's really nice demonstrations that it's possible to
*  do, but there's so many pieces that it's kind of like, it's in, it's kind of in the lab.
*  Now it's in the physical world, meaning it's in the physical space, the attacks,
*  but it's very like, you have to control a lot of things to pull it off.
*  It's like the difference between opening a safe when you have it and you have unlimited time and
*  you can work on it versus like breaking into like the crown, stealing the crown jewels and whatever.
*  Right. I mean, so one way to look at this in terms of how real these attacks can be,
*  one way to look at it is that actually you don't even need any sophisticated attacks.
*  Already we've seen in many real world examples, incidents, where showing that the
*  vehicle was making the wrong decision. The wrong decision without attacks, right?
*  Right, right. So that's one way to demonstrate. And this is also, like so far we've mainly talked
*  about work in this adversarial setting, showing that today's learning system, they are so vulnerable
*  to the adversarial setting, but at the same time, actually, we also know that even in natural
*  settings, these learning systems, they don't generalize well and hence they can really
*  misbehave under certain situations like what we have seen. And hence I think using that as an
*  example, it can show that these issues can be real. They can be real. But so there's two cases.
*  One is something, it's like perturbations can make the system misbehave versus make the system
*  do one specific thing that the attacker wants. As you said, the targeted attack. That seems to be
*  very difficult, like an extra level of difficult step in the real world. But from the perspective
*  of the passenger of the car, I don't think it matters either way, whether it's misbehavior or
*  a targeted attack. Okay. And also, that's why I was also saying earlier, like one defense is this
*  multi-modal defense and more of these consistent checks and so on. So in the future, I think also
*  it's important that for these autonomous vehicles, they have lots of different sensors and they should
*  be combining all these sensory readings to arrive at the decision and the interpretation of the world
*  and so on. And the more of these sensory inputs they use and the better they combine the sensory
*  inputs, the higher it is going to be attacked. And hence I think that is a very important
*  direction for us to move towards. So multi-modal, multi-sensor across multiple cameras, but also in
*  the case of car, radar, ultrasonic, sound even. So all of those. Right, right, right. Exactly.
*  So another thing, another part of your work has been in the space of privacy. And that too can be
*  seen as a kind of security vulnerability. So thinking of data as a thing that should be protected
*  and the vulnerabilities to data is vulnerability is essentially the thing that you want to protect
*  is the privacy of that data. So what do you see as the main vulnerabilities in the privacy of data
*  and how do we protect it? Right. So in security, we actually talk about essentially two, in this
*  case, two different properties. One is integrity and one is confidentiality. So what we have been
*  talking earlier is essentially the integrity of the integrity property of the learning system,
*  how to make sure that the learning system is giving the right prediction, for example. And
*  privacy essentially is on the other side is about confidentiality of the system is how attackers can,
*  when the attackers compromise the confidentiality of the system, that's when the attackers steal
*  sensitive information about individuals and so on. That's really clean. Those are great terms,
*  integrity and confidentiality. Right. So how, what are the main vulnerabilities to privacy,
*  we should say, and how do we protect against it? Like what are the main spaces and problems that
*  you think about in the context of privacy? Right. So especially in the machine learning setting.
*  So in this case, as we know that how the process goes is that we have the training data
*  and then the machine learning system trains from this training data and then builds a model.
*  And then later on, inputs are given to the model to inference time to try to get prediction and so
*  on. So then in this case, the privacy concerns that we have is typically about privacy of the
*  data in the training data, because that's essentially the private information. So, and it's really
*  important because oftentimes the training data can be very sensitive. It can be financial data,
*  health data, or like in IoT case, it's the sensors deployed in real world environment and so on. And
*  all this can be collecting very sensitive information. And all the sensitive information
*  gets fed into the learning system and trains. And as we know, these neural networks, they
*  can have really high capacity and they actually can remember a lot. And hence, just from the
*  learned model in the end, actually attackers can potentially infer information about the original
*  training data sets. So the thing you're trying to protect is the confidentiality of the training
*  data. And so what are the methods for doing that? What are the different ways that can be done?
*  And also we can talk about essentially how the attacker may try to learn information from the
*  and also there are different types of attacks. So in certain cases, again, like in white box attacks,
*  we can say that the attacker actually get to see the parameters of the model. And then from that,
*  a smart attacker potentially can try to figure out information about the training data set. They can
*  try to figure out what type of data has been in the training data sets. And sometimes they can tell
*  whether a person has been, a particular person's data point has been used in the training data sets.
*  So white box meaning you have access to the parameters of say, neural network.
*  And so that you're saying that it's some given that information is possible to some.
*  So I can give you some examples. And another type of attack, which is even easier to carry out is
*  not a white box model. It's more of a just a query model where the attacker only gets to
*  query the machine learning model and then try to steal sensitive information in the original
*  training data. So I can give you an example. In this case, training a language model.
*  So in our work in collaboration with the researchers from Google, we actually studied
*  the following question. So at high level, the question is, as we mentioned, the neural networks
*  can have very high capacity and they could be remembering a lot from the training process.
*  Then the question is, can attacker actually exploit this and try to actually extract sensitive
*  information in the original training data sets through just querying the learned model without
*  even knowing the parameters of the model, like the details of the model or the architectures of
*  the model and so on. So that's the question we set out to explore. And in one of the case studies,
*  we showed the following. So we trained a language model over an email data sets. It's called an
*  Enron email data sets. And the Enron email data sets naturally contains users social security
*  numbers and critical numbers. So we train the language model over this data sets. And then we
*  show that an attacker by devising some new attacks by just querying the language model.
*  And with that knowing the details of the model, the attacker actually can extract
*  the original social security numbers and critical numbers that were in the original training data.
*  So get the most sensitive personally identifiable information from the data set. I'm just querying it.
*  Right. Yeah. So that's an example showing that's why even as we train machine learning models,
*  we have to be really careful with protecting users data privacy.
*  So what are the mechanisms for protecting? Is there hopeful? So there's been recent work
*  on differential privacy, for example, that provides some hope. But can you describe some of the ideas?
*  So that's actually right. So that's also our finding is that by actually we show that
*  in this particular case, we actually have a good defense.
*  For the querying case, for the language model case.
*  Language model case.
*  So instead of just training a vanilla language model, instead, if we train a
*  defensively private language model, then we can still achieve similar utility.
*  But at the same time, we can actually significantly enhance the privacy protection
*  and the after learned model and our proposed attacks actually are no longer effective.
*  And differential privacy is a mechanism of adding some noise by which you then have some guarantees
*  on the inability to figure out the presence of a particular person in the data set.
*  So right. So in this particular case, what the differential privacy
*  mechanism does is that it actually adds perturbation in the training process.
*  As we know, during the training process, we are learning the model, we are doing ingredient updates,
*  the width updates and so on. And essentially, differential privacy, a defensively private
*  machine learning algorithm in this case will be adding noise and adding various perturbation
*  during this training process.
*  Through some aspect of the training process.
*  Right. So then the final trained learning, the learned model is defensively private.
*  And so it can enhance the privacy protection.
*  So, OK, so that's the attacks and the defense of privacy.
*  You also talk about ownership of data.
*  So this is a really interesting idea that we get to use many services online for seemingly for free
*  by essentially sort of a lot of companies are funded through advertisement.
*  And what that means is the advertisement works exceptionally well because the companies are able
*  to access our personal data so they know which advertisement to serve us to do targeted
*  advertisements and so on. So can you maybe talk about this?
*  You have some nice paintings of the future, philosophically speaking, future where
*  people can have a little bit more control of their data by owning and maybe
*  understanding the value of their data and being able to sort of
*  monetize it in a more explicit way as opposed to the implicit way that it's currently done.
*  Yeah, I think this is a fascinating topic and also a really complex topic.
*  Right. I think there are these natural questions who should be owning the data.
*  And so I can tell one analogy.
*  So for example, for physical properties like your house and so on. So really
*  this notion of property rights is not just, you know, like it's not like from day one we knew
*  that there should be like this clear notion of ownership of properties and having enforcement
*  for this. And so actually people have shown that this establishment and enforcement of property
*  rights has been a main driver for the economy earlier and that actually really propelled
*  the economic growth even in the earlier stage.
*  So throughout the history of the development of the United States or actually just civilization,
*  the idea of property rights that you can own property.
*  Right. And then there's enforcement, there's institutional rights, the governmental like
*  enforcement of this actually has been a key driver for economic growth. And there have been
*  even research proposals saying that for a lot of the developing countries,
*  you know, essentially the challenge in growth is not actually due to the lack of capital.
*  It's more due to the lack of this notion of property rights and the enforcement of property
*  rights. Interesting. So that the presence of absence of both the concept of the property
*  rights and their enforcement has a strong correlation to economic growth. Right.
*  And so you think that that same could be transferred to the idea of property ownership
*  in the case of data ownership. I think it's a good lesson for us to recognize that these rights and
*  the recognition and enforcement of these type of rights is very, very important for economic growth.
*  And then if we look at where we are now and where we are going in the future,
*  and so essentially more and more is actually moving into the digital world.
*  And also more and more, I would say even like information or assets of a person is more and
*  more into the real world, the physical, sorry, the digital world as well. It's the data that
*  the person has generated. And essentially it's like in the past, what defines a person,
*  you can say, right, like oftentimes besides the innate capabilities, actually it's the
*  physical properties. House, car.
*  Right. That defines a person. But I think more and more people start to realize actually what
*  defines a person is more important in the data that the person has generated or the data about
*  the person. Like all the way from your political views, your music taste, and your financial
*  information, a lot of these, and your health. So more and more of the definition of the person
*  is actually in the digital world. And currently for the most part, that's owned
*  people don't talk about it, but kind of it's owned by internet companies. So it's not owned
*  by individuals. There's no clear notion of ownership
*  of such data. And also we talk about privacy and so on, but I think actually clearly identifying
*  the ownership is the first step. Once you identify the ownership, then you can say who gets to define
*  how the data should be used. So maybe some users are fine with internet companies serving them as
*  right. Using their data as long as if the data is used in a certain way that actually
*  the user consent with are allowed. For example, you can say the recommendation system in some sense,
*  we don't call it the ads, but a recommendation system, similarly, it's trying to recommend you
*  something and users enjoy and can really benefit from good recommendation systems. They're
*  recommending you better music, movies, news, even research papers to read.
*  But of course then in these targeted ads, especially in certain cases where people can
*  be manipulated by these targeted ads that can have really bad, like severe consequences.
*  So essentially it uses one day to be used to better serve them. And also maybe even get paid
*  for whatever, like in different settings. But the thing is that the first of all, we need to really
*  establish who needs to decide who can decide how the data should be used. And typically
*  that the establishment and clarification of the ownership will help this and it's an important
*  first step. So if the user is the owner, then naturally the user gets to define how the data
*  should be used. But if you even say that wait a minute, user is actually not the owner of this
*  data. Whoever is collecting the data is the owner of the data. Now of course they get to use the
*  data however they want. So to really address these complex issues, we need to go at the root cause.
*  So it seems fairly clear that first we really need to say who is the owner of the data and then
*  the owners can specify how they want that data to be utilized. So I said that's a fascinating,
*  most people don't think about that. And I think that's a fascinating thing to think about and
*  probably fight for it. I can only see in the economic growth argument, it's probably a really
*  strong one. So that's a first time I'm kind of at least thinking about the positive aspect of that
*  ownership being the long-term growth of the economy. So good for everybody. But one possible
*  downside I could see to put on my grumpy old grandpa hat and it's really nice for Facebook
*  and YouTube and Twitter to all be free. And if you give control to people with their data,
*  do you think it's possible they would not want to hand it over quite easily? And so a lot of
*  these companies that rely on mass handover of data and then therefore provide a mass
*  seemingly free service would then completely, so the way the internet looks will completely change
*  because of the ownership of data and we'll lose a lot of services value. Do you worry about that?
*  That's a very good question. I think that's not necessarily the case in the sense that
*  yes, users can have ownership of their data, they can maintain control of their data, but also then
*  they get to decide how their data can be used. So that's why I mentioned earlier, like so in this
*  case, if they feel that they enjoy the benefits of social networks and so on, and they're fine with
*  having Facebook, having their data, but utilizing the data in certain way that they agree, then they
*  can still enjoy the free services. But for others, maybe they would prefer some kind of
*  private vision. And in that case, maybe they can even opt in to say that I want to pay
*  and to have, so for example, it's already fairly standard, like you pay for certain subscriptions
*  so that you don't get to be shown ads. So then users essentially can have choices. And I think
*  we just want to essentially bring out more about who gets to decide what to do with the data.
*  I think it's an interesting idea because if you pull people now, it seems like, I don't know,
*  but subjectively, sort of anecdotally speaking, it seems like a lot of people don't trust Facebook.
*  So that's at least a very popular thing to say that I don't trust Facebook. I wonder if you give
*  people control of their data as opposed to sort of signaling to everyone that they don't trust
*  Facebook. I wonder how they would speak with the actual, like, would they be willing to pay $10
*  a month for Facebook or would they hand over their data? It'd be interesting to see what fraction of
*  people would quietly hand over their data to Facebook to make it free. I don't have a good
*  intuition about that. Like, how many people, do you have an intuition about how many people
*  would use their data effectively on the market of the internet by sort of buying services with their
*  data? Yeah, so that's a very good question. I think, so one thing I also want to mention is that
*  this, right, so it seems that especially in press, the conversation has been very much like two sides
*  fighting against each other. On one hand, users can say that they don't trust Facebook, they don't
*  or they delete Facebook. Yeah, exactly. Right. And then on the other hand, right, of course,
*  right, the other side, they also feel, oh, they are providing a lot of services to users
*  and users are getting it all for free. So I think actually, I talk a lot to different
*  companies and also like basically on both sides. So one thing I hope also, like,
*  this is my hope for this year also is that we want to establish a more constructive dialogue
*  and to help people to understand that the problem is much more nuanced than just
*  this two sides fighting. Because naturally, there is a tension between the two sides,
*  between utility and privacy. So if you want to get more utility, essentially,
*  like the recommendation system example I gave earlier, if you want someone to give you a good
*  recommendation, essentially, whatever the system is, the system is going to need to know your data
*  to give you a good recommendation. But also, of course, at the same time, we want to ensure that
*  however that data is being handled is done in a privacy preserving way. So that, for example,
*  the recommendation system doesn't just go around and sell your data and then cause all the, you
*  know, cause a lot of bad consequences and so on. So you want that dialogue to be a little bit more
*  in the open, a little more nuanced, and maybe adding control to the data, ownership to the data
*  will allow, as opposed to this happening in the background, allow to bring it to the forefront
*  and actually have dialogues in like more nuanced, real dialogues about how we trade our data for the
*  services. That's the whole- Right, right. Yes, at the high level. So essentially, also knowing
*  that there are technical challenges in addressing the issue to like, basically, you can't have,
*  just like the example that I gave earlier, it's really difficult to balance the two between
*  utility and privacy. And that's also a lot of things that I work on, my group works on as well,
*  is to actually develop these technologies that are needed to essentially help this balance better,
*  essentially to help data to be utilized in a privacy preserving and responsible way.
*  And so we essentially need people to understand the challenges and also at the same time
*  to provide the technical abilities and also regulatory frameworks to help the two sides
*  to be more in a win-win situation instead of a fight. Yeah, the fighting thing is,
*  I think YouTube and Twitter and Facebook are providing an incredible service to the world
*  and they're all making mistakes, of course, but they're doing an incredible job,
*  that I think deserves to be applauded and there's some degree of gratitude, like it's a cool thing
*  that's created and it shouldn't be monolithically fought against like Facebook is evil or so on.
*  Yeah, I might make mistakes, but I think it's an incredible service. I think it's world changing.
*  I think Facebook's done a lot of incredible things by bringing, for example, identity,
*  like allowing people to be themselves, like their real selves in the digital space by using their
*  real name and their real picture. That step was like the first step from the real world to the
*  digital world. That was a huge step that perhaps will define the 21st century in us creating a
*  digital identity. And there's a lot of interesting possibilities there that are positive. Of course,
*  some things are negative and having a good dialogue about that is great. And I'm great
*  that people like you are at the center of that dialogue. That's awesome.
*  Right. I think I also can understand. I think actually in the past, especially in the past
*  couple of years, this rising awareness has been helpful. Like users are also more and more
*  recognizing that privacy is important to them. They should be owners of their data.
*  I think this definitely is very helpful. And I think also this type of voice,
*  and together with the regulatory framework and so on, also helps the companies to essentially put
*  these type of issues at a higher priority. And knowing that also it is their responsibility too
*  to ensure that users are well protected. So I think definitely the rising voice is super helpful.
*  I think that actually really has brought the issue of data privacy and even this consideration of
*  data ownership to the forefront to really much wider community. And I think more of this voice
*  is needed, but I think it's just that we want to have a more constructive dialogue
*  to bring the both sides together to figure out a constructive solution.
*  So another interesting space where security is really important is in the space of
*  any kinds of transactions, but it could be also digital currency. So can you maybe talk
*  a little bit about blockchain? Can you tell me what is a blockchain?
*  I think the blockchain word itself is actually very overloaded.
*  In general, it's like AI.
*  Yes. So in general when we talk about blockchain, we refer to this distributor in a decentralized
*  fashion. So essentially you have a community of nodes that come together. And even though
*  each one may not be trusted, and as long as certain thresholds of the set of nodes
*  behaves properly, then the system can essentially achieve certain properties. For example,
*  in the distributed ledger setting, you can maintain a mutable log and you can ensure that,
*  for example, the transactions actually agree to pan and then it's immutable and so on.
*  So first of all, what's a ledger? So it's a...
*  It's like a database. It's like a data entry.
*  And so distributed ledger is something that's maintained across or is synchronized across
*  multiple sources, multiple nodes. Multiple nodes, yes.
*  And so where is this idea? How do you keep... So it's important a ledger, a database, to keep that...
*  To make sure... So what are the kinds of security vulnerabilities
*  that you're trying to protect against in the context of a distributed ledger?
*  So in this case, for example, you don't want some malicious nodes to be able to change the
*  transaction logs. And in certain cases, it's called double spending. You can also cause
*  different views in different parts of the network and so on.
*  So the ledger has to represent, if you're capturing financial transactions,
*  has to represent the exact timing and the exact occurrence and no duplicates,
*  all that kind of stuff has to represent what actually happened.
*  Okay. So what are your thoughts on the security and privacy of digital currency?
*  I can't tell you how many people write to me to interview various people in the digital currency
*  space. There seems to be a lot of excitement there. And it seems to be... Some of it to me,
*  from an outsider's perspective, seems like dark magic. I don't know how secure...
*  I think the foundation, from my perspective, of digital currencies, that is,
*  you can't trust anyone, so you have to create a really secure system. So can you maybe speak about
*  how... What your thoughts in general about digital currency is and how you... How we can possibly
*  create financial transactions and financial stores of money in the digital space?
*  So you asked about security and privacy. So again, as I mentioned earlier, in security,
*  we actually talk about two main properties, the integrity and confidentiality. So there's another
*  one for availability. You want the system to be available. But here, for the question you asked,
*  let's just focus on integrity and confidentiality. So for integrity of this distributed ledger,
*  essentially, as we discussed, we want to ensure that the different nodes... So they have this
*  consistent view. Usually it's done through what we call a consensus protocol. That they establish
*  this shared view on this ledger, and that you can go back and change, it's immutable, and so on.
*  So in this case, then the security often refers to this integrity property. And essentially,
*  you're asking the question, how much work, how can you attack the system so that the attacker can
*  change the lock, for example. Right. How hard is it to make them
*  attack like that? Yeah. Right. And then that very much depends on the consensus mechanism,
*  how the system is built and all that. So there are different ways to build these decentralized
*  systems. People may have heard about the terms called proof of work, proof of stake, these
*  different mechanisms. And it really depends on how the system has been built and also how much
*  resources, how much work has gone into the network to actually say how secure it is. So for example,
*  if you talk about Bitcoin is proof of work system, so much electricity has been burned.
*  There's differences in the different mechanisms and the implementations of a distributed ledger
*  used for digital currency. So there's Bitcoin, there's so many of them, and there's underlying
*  different mechanisms. And there's arguments, I suppose, about which is more effective,
*  which is more secure, which is more... And what is needed? What amount of
*  resources needed to be able to attack the system? For example, what percentage of the nodes do you
*  need to control or compromise in order to change the log?
*  And those are things... Do you have a sense if those are things that can be shown theoretically
*  through the design of the mechanisms or does it have to be shown empirically by having a
*  large number of users using the currency? I see. So in general, for each consensus mechanism,
*  you can actually show theoretically what is needed to be able to attack the system.
*  Of course, there can be different types of attacks as we discussed at the beginning.
*  It's difficult to give a complete estimate, really how much is needed to compromise the system.
*  But in general, there are ways to say what percentage of the nodes you need to compromise
*  and so on. So we talked about integrity on the security side. And then you also mentioned
*  the privacy or the confidentiality side. Does it have some of the same problems and therefore some
*  of the same solutions that you talked about on the machine learning side with differential privacy
*  and so on? Yeah. So actually, in general, on the public ledger, in these public decentralized
*  systems, actually nothing is private. So all the transactions posted on the ledger, anybody can see.
*  So in that sense, there's no confidentiality. So usually, what you can do is then there are
*  the mechanisms that you can build in to enable confidentiality, privacy of the transactions and
*  the data and so on. That's also some of the work that both my group and also my startup does as well.
*  What's the name of the startup? Oasis Labs.
*  Oasis Labs. And so the confidentiality aspect there is even though the transactions are public,
*  you want to keep some aspect confidential of the identity of the people involved in the transactions
*  or what is their hope to keep confidential in this context? So in this case, for example,
*  you want to enable like confidential transactions even. So there are different essentially types
*  of data that you want to keep private or confidential. And you can utilize different
*  technologies, including zero-knowledge proofs and also secure computing techniques to hide
*  who is making the transactions to whom and the transaction amount. And in our case,
*  also we can enable confidential smart contracts so that you don't know the data and the execution
*  of the smart contract and so on. And we actually are combining these different technologies
*  going back to the earlier discussion we had, enabling ownership of data and privacy of data
*  and so on. So at Oasis Labs, we're actually building what we call a platform for responsible
*  data economy to actually combine these different technologies together and to enable secure and
*  privacy preserving computation and also using the ledger to help provide immutable log of users
*  ownership to their data and the policies they want the data to adhere to, the usage of the data to
*  adhere to and also how the data has been utilized. So all this together can build what we call a
*  distributed secure computing fabric that helps to enable a more responsible data economy.
*  Wow, that was eloquent. Okay, you're involved in so much amazing work that we'll never be able to
*  get to, but I have to ask at least briefly about program synthesis, which at least in a philosophical
*  sense captures much of the dreams of what's possible in computer science and the artificial
*  intelligence. First, let me ask what is program synthesis and can neural networks be used to learn
*  programs from data? So can this be learned? Some aspect of the synthesis can be learned?
*  So program synthesis is about teaching computers to write code, to program and I think that's
*  one of our ultimate dreams or goals. I think
*  Andreessen talked about software eating the world. So I say once we teach computers to
*  write software, to write programs, then I guess computers will be eating the world by transitivity.
*  Yeah, exactly. And also for me, actually,
*  when I shifted from security to more AI machine learning, program synthesis is
*  adversarial machine learning. These are the two fields that I particularly focus on.
*  Program synthesis is one of the first questions that I actually started investigating.
*  Just as a question, I guess from the security side, you're looking for holes in programs,
*  so at least see small connection. But where was your interest for program synthesis?
*  Because it's such a fascinating, such a big, such a hard problem in the general case.
*  Why program synthesis? So the reason for that is actually when I shifted my focus from security
*  into AI machine learning, actually one of my main motivation at the time is that even though I have
*  been doing a lot of work in security and privacy, but I have always been fascinated about building
*  intelligent machines. And that was really my main motivation to spend more time in AI machine
*  learning is that I really want to figure out how we can build intelligent machines. And to help us
*  towards that goal, program synthesis is really one of, I would say, the best domain to work on.
*  I actually call it program synthesis is like the perfect playground for building intelligent
*  machines and for artificial general intelligence. Well, it's also in that sense, not just a playground,
*  I guess it's the ultimate test of intelligence. Because I think if you can generate neural networks
*  can learn good functions and they can help you out in classification tasks, but to be able to write
*  programs, that's the epitome from the machine side. That's the same as passing the Turing
*  test in natural language, but with programs, it's able to express complicated ideas, to reason through
*  ideas and boil them down to algorithms. Yes, exactly. Incredible. So can this be learned? How far are we?
*  Is there hope? What are the open challenges? Very good questions. We are still at an early stage,
*  but already I think we have seen a lot of progress. I mean, definitely we have
*  existence proof, just like humans can write programs, so there's no reason why computers
*  cannot write programs. So I think that's definitely an achievable goal, is just how long it takes.
*  And then, and even today, we actually have the program synthesis community, especially the
*  program synthesis by learning, how we call it, neural program synthesis community, is still very small,
*  but the community has been growing and we have seen a lot of progress. And in limited domains,
*  I think actually program synthesis is ripe for real world applications.
*  So actually it was quite amazing. I was giving a talk, so here is a rework conference.
*  Rework deep learning summary.
*  I actually, so I gave another talk at the previous rework conference in deep reinforcement learning,
*  and then I actually met someone from a startup, the CEO of the startup, and when he saw my name,
*  he recognized it and he actually said, one of our papers actually had actually become a key
*  product in the startup. And that was program synthesis. In that particular case, it was
*  natural language translation, translating natural language description into SQL queries.
*  Oh, wow. That direction. Okay.
*  Right. So yeah, so in program synthesis, in limited domains, in well specified domains, actually
*  already we can see really great progress and applicability in the real world.
*  So domains like, as an example, you said natural language, being able to express something through
*  just normal language and it converts it into a database SQL SQL query.
*  Right.
*  And that's how solves the problem is that, because that seems like a really hard problem.
*  Again, in limited domains, actually it can work pretty well. And now this is also a very active
*  domain of research at the time. I think when he saw our paper at the time, we were the
*  state of the arts on that task. And since then, actually now there has been more work and with even
*  more sophisticated data sets. But I think I wouldn't be surprised that more of this type of
*  technology really gets into the real world.
*  That's exciting.
*  In the near term.
*  Being able to learn in the space of programs is super exciting. I'm still skeptical because I
*  think it's a really hard problem, but I would love to see progress.
*  And also I think in terms of the, you asked about open challenges, I think the domain is
*  full of challenges. And in particular, also we want to see how we should measure the progress
*  in the space. And I would say mainly three main, I'll say, metrics. So one is the complexity of
*  the program that we can synthesize. And that will actually have clear measures and just look at the
*  past publications. And even like, for example, I was at the recent NeurIPS conference. Now there's
*  actually a fairly sizable session dedicated to programming synthesis, which is-
*  Or even neuro programs.
*  Right, right, right, which is great. And we continue to see the increase in-
*  What does sizable mean? I like the word sizable. It's five people.
*  It's still a small community, but it is growing.
*  And they will all win touring awards one day. I like it.
*  Right. So we can clearly see increase in the complexity of the programs that
*  these- Just to elaborate-
*  We can synthesize.
*  Sorry, is it the complexity of the actual text of the program or the running time complexity?
*  Which complexity are we-
*  How-
*  The complexity of the task to be synthesized and the complexity of the actual synthesized
*  programs. So the lines of code, even, for example.
*  Okay, I got you. But it's not the theoretical upper bound of the running time of the algorithm.
*  Right, right, right.
*  Okay, got it. And you can see the complexity decreasing already.
*  Oh no, meaning we want to be able to synthesize more and more complex programs,
*  bigger and bigger programs. So we want to see that we want to increase the complexity.
*  I have to think through, because I thought of complexity as you want to be able to
*  accomplish the same task with a simpler and simpler program.
*  No, we are not doing that. It's more about how complex a task we can synthesize programs for.
*  See, got it. Being able to synthesize programs, learn them for more and more difficult tasks.
*  Right. So for example, initially our first work in program synthesis was to translate natural
*  language distribution into really simple programs called ifttt, if this, then that.
*  So given the trigger condition, what is the action you should take?
*  So that program is super simple. You just identify the trigger conditions and the action.
*  And then later on with the SQL queries, it gets more complex. And then also we started to
*  synthesize programs with loops and...
*  Oh no. And if you can synthesize recursion, it's all over.
*  Right. Actually, one of our works actually is learning recursive neural programs.
*  Oh no.
*  But anyway, so that's one is the complexity and the other one is generalization. When we
*  train our learn program synthesizer in this case, a neural programs to synthesize programs,
*  then you want it to generalize.
*  For a large number of inputs.
*  Right. So to be able to generalize to previously unseen inputs.
*  So some of the work we did earlier on learning recursive neural programs actually showed that
*  recursion actually is important to learn. And if you have recursion, then for a certain
*  set of tasks, we can actually show that you can actually have perfect generalization.
*  So that's one of the best paperwork words that I cleared earlier.
*  So that's one example of we want to learn these neural programs that can generalize better.
*  But that works for certain tasks, certain domains. And there's question how we can
*  essentially develop more techniques that can have generalization for a wider set of
*  domains and so on. So that's another area. And then the third challenge, I think,
*  is not just for programming synthesis, it's also cutting across other fields in machine learning
*  and also including deeper reinforcement learning in particular, is that this adaptation is that we
*  want to be able to learn from the past and tasks and training and so on to be able to solve new
*  tasks. So for example, in programming synthesis today, we still are working in the setting where
*  given a particular task, we train the model and to solve this particular task. But that's not how
*  humans work. The whole point is we train a human and you can then program to solve new tasks.
*  Right, exactly.
*  And just like in deep reinforcement learning, we don't want to just train an agent to play a
*  particular game, either it's Atari or it's Go or whatever. We want to train these agents that can
*  essentially extract knowledge from the past learning experience to be able to adapt to new tasks
*  and solve new tasks. And I think this is particularly important for programming synthesis.
*  Yeah, that's the whole dream of programming synthesis is you're learning a tool that can solve
*  new problems.
*  Right, exactly. And I think that's a particular domain that as a community, we need to put more
*  emphasis on and I hope that we can make more progress there as well.
*  Awesome. There's a lot more to talk about. Let me ask that you also had a very interesting and
*  we talked about rich representations. You had a rich life journey. You did your bachelor's in
*  China and your master's and PhD in the United States, CMU in Berkeley. Are there interesting
*  differences? I told you I'm Russian. I think there's a lot of interesting differences between
*  Russia and the United States. Are there in your eyes interesting differences between the two
*  cultures from the silly romantic notion of the spirit of the people to the more practical notion
*  of how research is conducted that you find interesting or useful in your own work of having
*  experienced both?
*  That's a good question. I think so. I studied in China for my undergraduates and that was
*  more than 20 years ago. So it's been a long time.
*  Is there echoes of that time in you?
*  Actually, it's interesting. I think even more so maybe something that's even be more different
*  from my experience than a lot of computer science researchers and practitioners is that
*  so for my undergraduates, I actually studied physics.
*  Very nice.
*  And then I switched to computer science in graduate school.
*  What happened?
*  Is there another possible universe where you could have become a theoretical physicist at
*  Caltech or something like that?
*  That's very possible. Some of my undergrad classmates then they later on started physics,
*  they got their PhD in physics from these schools from top physics programs.
*  From that experience of doing physics in your bachelor's, what made you decide to switch to
*  computer science and computer science at arguably one of the best universities in the world for
*  computer science with Carnegie Mellon, especially for the grad school and so on?
*  So what was the choice like and what was the move to the United States like? What was that
*  whole transition? And if you remember, if there's still echoes of some of the spirit of the people
*  of China in you in New York, it's like three questions. I'm sorry.
*  No, that's okay. So yes, I guess, okay, so first transition from physics to computer science.
*  So when I first came to the United States, I was actually in the physics PhD program at Cornell.
*  I was there for one year and then I switched to computer science and then I was in the PhD program
*  at Carnegie Mellon. So, okay, so the reasons for switching. So one thing, so that's why I also
*  mentioned about this difference in backgrounds about having studied physics first in my undergrad.
*  Yeah, I actually really, I really did enjoy my undergrad time and education in physics.
*  I think that actually really helped me in my future work in computer science.
*  Actually, even for machine learning, a lot of machine learning stuff, the core machine learning
*  methods, many of them actually came from physics. For honest, most, but anyway,
*  most of everything came from physics. Anyway, so when I started physics, I was,
*  I think I was really attracted to physics. It was, it's really beautiful. And I actually call it
*  physics is the language of nature. And I actually clearly remember like one moment
*  in my undergrads, like I did my undergrad in Tsinghua and I used to study in the library.
*  And I clearly remember like one day I was sitting in the library and I was like writing on my notes
*  and so on. And I got so excited that I realized that really just from a few simple axioms,
*  a few simple laws, I can derive so much. It's almost like I can derive the rest of the world.
*  Yeah, the rest of the universe.
*  Yes. Yes. So that was like amazing.
*  Do you think you, have you ever seen or do you think you can rediscover that kind of power and
*  beauty in computer science in the world? That's very interesting. So that gets to,
*  you know, the transition from physics to computer science. It's quite different.
*  For physics in grad school actually things changed. So one is I started to realize that
*  when I started doing research in physics at the time I was doing theoretical physics.
*  And a lot of it, you still have the beauty but it's very different. So I had to actually do
*  a lot of the simulation. So essentially I was actually writing, in some cases writing fortune
*  code. Good old fortune, yeah. To actually write, do simulations and so on. That was not
*  not exactly what I enjoyed doing. And also at the time from talking with the senior
*  you know students in the program, I realized many of the students actually were going off
*  to like Wall Street and so on. So, and I've always been interested in computer science
*  and actually essentially taught myself the C programming.
*  Program.
*  Right. And so on.
*  At which, when?
*  In college.
*  In college somewhere?
*  In the summer.
*  Nice.
*  For fun. Physics major, learning to do C programming. Beautiful.
*  Actually it's interesting you know in physics at the time, I think now the program probably
*  has changed. But at the time really the only class we had in related to computer science
*  education was introduction to, I forgot, to computer science or computing and Fortran 77.
*  There's a lot of people that still use Fortran. I'm actually, if you're a programmer out there,
*  I'm looking for an expert to talk to about Fortran. They seem to, there's not many,
*  but there's still a lot of people that still use Fortran and still a lot of people use Cobalt.
*  So then I realized instead of just doing programming for doing simulations and so on,
*  that I may as well just change to computer science. And also one thing I really like,
*  and that's a key difference between the two, is in computer science it's so much easier to realize
*  your ideas. If you have an idea, you write it up, you code it up, and then you can see it actually.
*  Exactly.
*  Running and you can see it.
*  You can bring it to life quickly.
*  Bring it to life. Whereas in physics, if you have a good theory, you have to wait for the
*  experimentalist to do the experiments and to confirm the theory. And things just take so much
*  longer. And also the reason in physics I decided to do theoretical physics was because I had my
*  experience with experimental physics. First you have to fix the equipment.
*  You spend most of your time fixing the equipment first.
*  Super expensive equipment. So there's a lot of, yeah, you have to collaborate with a lot of people.
*  Takes a long time.
*  Just takes really much longer.
*  Yeah, it's messy.
*  So I decided to switch to computer science. And one thing I think maybe people have realized is
*  that for people who study physics, actually it's very easy for physicists to change to do something
*  else. I think physics provides a really good training. And yeah, so actually it was very easy
*  to switch to computer science. But one thing going back to your earlier question. So one thing I
*  actually did realize. So there is a big difference between computer science and physics, where
*  physics you can derive the whole universe from just a few simple laws. And computer science,
*  given that a lot of it is defined by humans, the systems are defined by humans and it's artificial.
*  Essentially you create a lot of these artifacts and so on. It's not quite the same. You don't
*  derive the computer systems with just a few simple laws. You actually have to see there is
*  historical reasons why a system is built and designed one way versus the other.
*  There's a lot more complexity, less elegant simplicity of E equals MC squared that kind
*  of reduces everything down to those beautiful fundamental equations. But what about the move
*  from China to the United States? Is there anything that still stays in you that
*  contributes to your work? The fact that you grew up in another culture?
*  So yes, I think especially back then it's very different from now. So now I see these students
*  coming from China. And even undergraduates, actually they speak fluent English. It was
*  just amazing. And they have already understood so much of the culture in the US and so on.
*  It was to you it was all foreign?
*  It was a very different time. At the time actually, we didn't even have easy access to email,
*  not to mention about the web. I remember I had to go to specific,
*  privileged server rooms to use email. And hence, at the time we had much less knowledge about
*  the Western world. And actually at the time I didn't know actually in the US the West Coast
*  weather is much better than the East Coast. Yeah, things like that actually. It's very interesting.
*  But now it's so different. At the time I would say there's also a bigger cultural difference
*  because there's so much less opportunity for shared information. So it's such a different
*  time and world.
*  So let me ask maybe a sensitive question. I'm not sure but I think you and I are in similar
*  positions. I've been here for already 20 years as well. And looking at Russia from my perspective
*  and you looking at China, in some ways it's a very distant place because it's changed a lot.
*  But in some ways you still have echoes, you still have knowledge of that place.
*  The question is, China is doing a lot of incredible work in AI.
*  Do you see, please tell me there's an optimistic picture you see where the United States and China
*  can collaborate and sort of grow together in the development of AI towards, you know,
*  there's different values in terms of the role of government and so on of ethical, transparent,
*  secure systems. We see it differently in the United States a little bit than China,
*  but we're still trying to work it out. Do you see the two countries being able to successfully
*  collaborate and work in a healthy way without sort of fighting and making it an AI arms race
*  kind of situation? Yeah, I believe so. I think science has no border and the advancement of
*  technology helps everyone, helps the whole world. And so I certainly hope that the two countries
*  will collaborate and I certainly believe so. Do you have any reason to believe so,
*  except being an optimist? So first, again, like I said, science has no borders.
*  And especially in... Science doesn't know borders? Right.
*  And you believe that, well, you know, in the former Soviet Union during the Cold War...
*  Yeah, so that's the other point I was going to mention is that especially in academic research,
*  everything is public. Like we write papers, we open source codes, and all this is in the public
*  domain. It doesn't matter whether the person is in the US, in China, or some other parts of the world.
*  They can go on archive and look at the latest research and results.
*  So that openness gives you hope. Yes.
*  Me too. And that's also how, as a world, we make progress the best.
*  So, I apologize for the romanticized question, but looking back, what would you say was the most
*  transformative moment in your life that maybe made you fall in love with computer science?
*  You said physics, you remember there was a moment where you thought you could derive the entirety of
*  the universe. Was there a moment that you really fell in love with the work you do now, from
*  the work you do now, from security to machine learning to program synthesis?
*  So maybe, as I mentioned, actually in college, one summer I just taught myself programming in C.
*  Yes. You just read a book.
*  Don't tell me you fell in love with computer science by programming in C.
*  Remember I mentioned one of the draws for me to computer science is how easy it is
*  to realize your ideas. So once I read the book and taught myself how to program in C,
*  what did I do? I programmed two games. One is just simple, it's a go game, it's a board,
*  you can move the stones and so on. And the other one I actually programmed the game,
*  that's like a 3D Tetris. It turned out to be a super hard game to play.
*  Because instead of just the standard 2D Tetris, it's actually a 3D thing.
*  But I realized, wow, I just had these ideas to try it out and then you can just do it.
*  So that's when I realized, wow, this is amazing.
*  You can create yourself ideas from nothing to something that's actually out in the real world.
*  Right. And give me your own hands.
*  Let me ask a silly question, or maybe the ultimate question. What is to you the meaning of life?
*  What gives your life meaning, purpose, fulfillment, happiness, joy?
*  Okay, these are two different questions.
*  Very different, yeah.
*  It's usually that you ask this question, maybe this question is
*  probably the question that has followed me and followed my life the most.
*  Have you discovered anything and you satisfied your answer for yourself?
*  Is there something you've arrived at? There's a moment, I've talked to a few people who have
*  faced, for example, a cancer diagnosis or faced their own mortality, and that seems to change
*  their view. It seems to be a catalyst for them removing most of the crap,
*  of seeing that most of what they've been doing is not that important and really reducing it
*  into saying, here's actually the few things that really give meaning.
*  Mortality is a really powerful catalyst for that, it seems like.
*  Facing mortality, whether it's your parents dying or somebody close to you dying,
*  or facing your own death for whatever reason, or cancer and so on.
*  In my own case, I didn't need to face mortality to try to ask that question.
*  I think there are a couple things. One is, who should be defining the meaning of your life?
*  Right. Is there some kind of even greater things than you who should define the meaning of your
*  life? For example, when people say that searching the meaning of our life, is there some outside
*  voice or is there something outside of you who actually tells you? People talk about,
*  oh, this is what you have been born to do. This is your destiny.
*  That's one question. Who gets to define the meaning of your life? Should you be finding
*  some other thing, some other factor to define this for you? Or is something actually,
*  it's just entirely what you define yourself and it can be very arbitrary.
*  An inner voice or an outer voice, whether it could be spiritual, religious, too, with God,
*  or some other components of the environment outside of you, or just your own voice. Do you
*  have an answer there? Okay, so with that, I have an answer.
*  Yeah. And through the long period of time of thinking and searching, even searching through
*  outside voices or factors outside of me. So that I have an answer. I've come to
*  the conclusion and realization that it's you yourself that defines the meaning of life.
*  Yeah, that's a big burden though, isn't it?
*  Yes and no. So then you have the freedom to define it.
*  And another question is, what does it really mean by the meaning of life?
*  And also, whether the question even makes sense.
*  Absolutely. And you said it somehow distinct from happiness. So meaning is something much deeper
*  than just any kind of emotional, any kind of contentment or joy, whatever, it might be much
*  deeper. And then you have to ask, what is deeper than that? What is there at all? And then the
*  question starts being silly. Right. And also you can say it's deeper,
*  but you can also say it's a shallower, depending on how people want to define
*  the meaning of their life. So for example, most people don't even think about this question,
*  then the meaning of life to them doesn't really matter that much. And also whether knowing the
*  meaning of life, whether it actually helps your life to be better or whether it helps your life
*  to be happier. These actually are open questions. It's not.
*  Of course, most questions are open. I tend to think that just asking the question, as you mentioned,
*  as you've done for a long time, is the only that there is no answer. And asking the question is a
*  really good exercise. I mean, I have this for me personally, I've had a kind of feeling that creation
*  is like for me has been very fulfilling. And it seems like my meaning has been to create. And I'm
*  not sure what that is. Like I don't have a single lot of kids. I'd love to have kids, but I also
*  see programs as little creations. I see robots as little creations.
*  I think those bring and then ideas, theorems and our creations and those somehow intrinsically,
*  like you said, bring me joy. I think they do to a lot of scientists, but I think they do to a lot of
*  people. So that to me, if I had a little bit of a sense of what I'm doing, I think that's
*  a good thing. And for me, if I had to force the answer to that, I would say creating new things
*  yourself. For you. For me. For me. For me. I don't know. But like you said, it keeps changing.
*  Is there some answer that... And some people, they can, I think, they may say it's experience.
*  Right? So like their meaning of life, they just want to experience to the richest and fullest they
*  do take that path. Yes. Seeing life is actually a collection of moments and then trying to make
*  the richest possible sets, fill those moments with the richest possible experiences. Yeah.
*  Right. And for me, I think it's certainly, we do share a lot of similarity here. So creation is
*  also really important for me, even from the things I've already talked about, even like writing
*  papers. And these are creations as well. And I have not quite thought whether that is really
*  the meaning of my life. Like in a sense, also that maybe like, what kind of things should you
*  create? There are so many different things that you could create. And also you can say another
*  view is maybe growth is related, but different from experience. Growth is also maybe type of
*  meaning of life. It's just, you try to grow every day, try to be a better self every day.
*  And also ultimately we are here, it's part of the overall evolution. The world is evolving.
*  And it's funny, isn't it funny that the growth seems to be the more important thing than the
*  thing you're growing towards. It's like, it's not the goal, it's the journey to it.
*  Sort of, it's almost, it's almost when you submit a paper, there's a sort of depressing element to it,
*  not to submit a paper, but when that whole project is over, I mean, there's a gratitude,
*  there's a celebration and so on, but you're usually immediately looking for the next thing,
*  the next step, right? It's not, it's not that satisfied. The end of it is not the satisfaction,
*  it's the hardship, the challenge you have to overcome, the growth through the process.
*  It's somehow probably deeply within us, the same thing that drives the evolutionary process
*  is somehow within us with everything the way we see the world, since you're thinking about
*  these. So you're still in search of an answer. I mean, yes and no, in the sense that I think
*  for people who really dedicate time to search for the answer, to ask the question, what is the
*  meaning of life? It does not necessarily bring you happiness. It's a question, we can say,
*  right, like whether it's a well-defined question and on the other hand, given that you get to
*  answer it yourself, you can define it yourself, then sure, I can just give it an answer.
*  And in that sense, yes, it can help. Like we discussed, if you say, oh, then my meaning of
*  life is to create or to grow, then yes, then I think they can help. But how do you know that
*  that is really the meaning of life or the meaning of your life? It's like there's no way for you to
*  really answer the question. Sure, but something about that certainty is liberating. So if
*  it might be an illusion, you might not really know, you might be just convincing yourself
*  falsely, but being sure that that's the meaning, there's something liberating in that. There's
*  something freeing in knowing this is your purpose. So you can fully give yourself to that. For a long
*  time, I thought like, isn't it all relative? Like why? How do we even know what's good and what's
*  evil? Like isn't everything just relative? Like how do we know, you know, the question of meaning
*  is ultimately the question of why do anything? Why is anything good or bad? Why is anything
*  right? Right. Exactly. But the moment, then you start to, I think, just like you said, I think
*  it's a really useful question to ask. But if you ask it for too long and too aggressively,
*  it may not be so productive. It may not be productive and not just for traditionally
*  societally defined success, but also for happiness. It seems like asking the question about the meaning
*  of life is like a trap. We're destined to be asking, we're destined to look up to the stars
*  and ask these big why questions we'll never be able to answer, but we shouldn't get lost in them.
*  I think that's probably the, that's at least the lesson I've picked up so far. On that topic.
*  Let me just add one more thing. So it's interesting. So actually, so sometimes, yes, it can
*  help you to focus. So when I, when I shifted my focus more from security to AI and machine
*  learning, at the time, the actually one of the main reasons that I did that was because at the time,
*  I thought my meaning, the meaning of my life and the purpose of my life is to build
*  intelligent machines. And that's, and then your inner voice said that this is the right,
*  this is the right journey to take to build intelligent machines and that you actually
*  fully realize you took a really legitimate big step to become one of the world-class researchers
*  to actually make it to actually go down that journey. Yeah, that's profound. That's profound.
*  I don't think there's a better way to end a conversation than talking for a while about
*  the meaning of life. Dawn is a huge honor to talk to you. Thank you so much for talking today.
*  Thank you. Thank you.
*  Thanks for listening to this conversation with Dawn Song and thank you to our presenting sponsor,
*  Cash App. Please consider supporting the podcast by downloading Cash App and using code,
*  LexPodcast. If you enjoy this podcast, subscribe on YouTube, review it with five stars on Apple
*  podcast, support it on Patreon, or simply connect with me on Twitter at Lex Friedman.
*  And now let me leave you with some words about hacking from the great Steve Wozniak.
*  A lot of hacking is playing with other people, you know, getting them to do strange things.
*  Thank you for listening and hope to see you next time.
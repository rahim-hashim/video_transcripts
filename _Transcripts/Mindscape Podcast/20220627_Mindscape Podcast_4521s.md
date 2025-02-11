---
Date Generated: June 08, 2024
Transcription Model: whisper medium 20231117
Length: 4521s
Video Keywords: []
Video Views: 7059
Video Rating: None
Video Description: Patreon: https://www.patreon.com/seanmcarroll
Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2022/06/27/202-andrew-papachristos-on-the-network-theory-of-gun-violence/

The United States is suffering from an epidemic of tragic gun violence. While a political debate rages around the topic of gun control, it remains important to understand the causes and possible remedies for gun violence within the current system. Andrew Papachristos is a sociologist who uses applied network science to study patterns of street violence in urban areas. His research shows that such violence is highly non-random; knowing something about the social networks of perpetrators and victims can help identify who might be at heightened risk of gun violence. It’s an interesting example of applying ideas from mathematics and computer science to real-world social situations.

Andrew Papachristos received his Ph.D. in sociology from the University of Chicago. He is currently a professor of sociology at Northwestern University, and a faculty fellow at the Institute for Policy Research. He is also founding director of the Northwestern Neighborhoods and Networks Initiative.

Mindscape Podcast playlist: https://www.youtube.com/playlist?list=PLrxfgDEc2NxY_fRExpDXr87tzRbPCaA5x
Sean Carroll channel: https://www.youtube.com/c/seancarroll

#podcast #ideas #science #philosophy #culture
---

# Mindscape 202 | Andrew Papachristos on the Network Theory of Gun Violence
**Mindscape Podcast:** [June 27, 2022](https://www.youtube.com/watch?v=Qil35nuukjg)
*  Hello everyone, welcome to the Mindscape Podcast. I'm your host, Sean Carroll. It's undoubtedly very
*  well known at this point that there is a problem with gun violence in the United States, especially
*  compared to other countries. People debate how best to measure this, but compared to the countries
*  that the US would generally consider its peers, that is to say other developed wealthy, purportedly
*  well-functioning societies, the United States has a lot more gun violence per capita than any of our
*  comparison nations. Now I feel a little bit weird because we're gonna be talking today about gun
*  violence, but not about the kind of mass shootings that have been in the news recently. As I'm
*  recording this intro, recently there was a mass shooting in Uvald, Texas. There have been others,
*  really terrible events where someone is able to get a weapon that fires a lot of ammunition very,
*  very quickly, break into a school or other kind of place where there's a lot of people, and do
*  an enormous amount of damage. This is clearly a problem. We're not talking about that one today.
*  There are other problems out there. So today we're talking to Andrew Papachristos. Andrew is a
*  sociologist at Northwestern University just outside Chicago, and what he's doing is using ideas from
*  network theory, something that we talked about before with people like Steven Strogatz. Andrew
*  uses network theory to predict what kinds of people and specifically which people might be
*  vulnerable to imminent gun violence, but not in the mass shooting sense, more like the gangs on
*  the street, crews that get into flare-ups where they start firing at each other kind of violence.
*  It's an interesting problem that sort of combines criminology, sociology, and math, because you use
*  the math of the network theory to say, well, this person is in the following network in the following
*  ways with these other people that puts them at greater risk than they might otherwise be. For
*  better or for worse, we have a lot of data out there on people, on who they talk to, who they know,
*  who they've been in prison with, who they've been in a gang with, things like that. And the good news
*  is that we can use that data to say, okay, this specific set of people might be at greater risk.
*  Right now, because there's recently been another shooting, now you can go in and try to protect the
*  people who are more at risk than others. It's not an any sense of panacea, be all and all way to end
*  gun violence, but we have so much here in the United States that it is a strategy that might be
*  helpful when we're trying to deploy the resources we have in the most effective ways. I'm not
*  personally enough of an expert to say whether or not this is the right way to go or the best way to
*  use our resources, but it certainly is an interesting combination of mathematical analysis,
*  big data kind of analysis of sociological phenomena and real world applications that
*  might help us to maybe save a few lives here or there. If we could do that, that'd be well worth
*  the effort. So let's go.
*  Andrew Papachristos, welcome to the Mindscape Podcast.
*  Thank you. It's a pleasure to be here.
*  Gun violence is what you work on as a professional pastime. Whenever I get people on the podcast
*  who work on these slightly touchy subjects, I'm kind of curious because I work on physics and
*  cosmology and philosophy in the beginning of the universe. And even those are touchy subjects.
*  People get very emotional about them. But you work on gun violence, which I imagine must engender
*  some reactions from people who hear about your work in the media.
*  It definitely does. I mean, gun violence is not unique to America, but there is a uniquely
*  American take on gun violence and what Americans think about guns and how we use guns and our
*  history with guns and the number of guns we have. And so, you know, I think a lot of what I try to
*  do is understand the science behind gun violence. And there are, of course, interventions and
*  preventions and policy measures that can reduce or make things worse. But by and large, what I try
*  to do is I try to approach it as a social scientist to figure out how we can understand these patterns
*  that we see, especially in cities and especially when people are harming each other as opposed to
*  suicide, which is the most common form of lethal gun violence in this country, which is quite
*  different. So I try to look at assaultive gun violence when people use firearms to kill other
*  people. And I try to really kind of unpack those patterns that we see, not just aggregate
*  statistics, so that we can hopefully do something about that problem and the situations that create
*  them and the currents that are both big and small that keep these levels of gun violence
*  unacceptably and stubbornly high in some places rather than other places.
*  Well, you mentioned already the fact that there is something uniquely American about this.
*  Can we let's try to quantify that, because I think a lot of us recognize that America is an outlier
*  when it comes to gun violence in various ways. So is that are we right about that? And how much is
*  it? And why is that true? Simple questions. Simple questions. So clearly, you know,
*  the United States is not unique relative to say other European countries when it comes to things
*  like robbery or non gun assaults. We are unique when it comes to our gun homicide and gun assault
*  levels of violence, which are, you know, tens of times higher than some of our other peers or who
*  we consider to be our peers. Part of this, of course, is the presence of firearms. We have more
*  guns in this country than people, which is not to say those guns are evenly distributed across
*  households. They are not. Most people that own a gun own multiple guns, which is, again, not
*  uncommon of people that are into something, right? Some people are into shoes and sneakers
*  and cars, and some people are into guns for whatever reason. So there's a unique part of
*  this country that is about, you know, owning a gun. It is a constitutional right and is being
*  upheld by the Supreme Court. There's also something uniquely American about the idea of arming
*  ourselves to protect ourselves. So the number one reason people carry or own a firearm in this
*  country is for protection. And then sort of the tricky science part is actually owning and carrying
*  guns actually makes you less safe. So despite that, this idea that guns will keep us safe is
*  pervasive. And it doesn't matter. It doesn't matter whether you live in the suburbs. Doesn't
*  matter whether you live in a neighborhood that is experiencing a disproportionate amount of gun
*  violence. The reason people carry guns is for protection. There's also an element in this
*  country, which, you know, this last surge in gun purchasing during the epidemic, people also arm
*  themselves when they feel like they have to take care of themselves outside of the confines of the
*  state. The state has let them down. The state's not protecting their interests or the state is
*  actively harming them, which also goes back to the founding of this country. And it doesn't just apply
*  to one particular group or the other. You know, the Black Panthers armed themselves for that very
*  reason. And we're seeing, you know, militias arming themselves for that very reason. And
*  private citizens purchase guns because they feel like they might have to protect their own selves
*  because they can't rely on somebody to come when they call. So I think this is implicit in what you
*  just said, but it's not just a matter of having more guns. If I recall correctly, Canadians have
*  more guns per capita than Americans do. But the culture is very different. You're really putting
*  your finger on the way that we think about guns and why we own them. I think that's right. I also
*  think it's fair to say that there are guns that are the ones we associate with violence,
*  interpersonal violence, which are handguns, which are handguns that are often diverted
*  from legal sources to illegal sources. So, you know, they are bought, they're stolen,
*  they're traded, they're stock, straw purchasers. This idea of a gun show loophole is not actually
*  about gun shows as much as the lack of regulation for private transactions, which is in most states
*  in this country. I could sell you a gun without telling anybody. Right. Yeah. There are certain
*  rules that I am supposed to uphold. You have to be of age. I have to reasonably believe you
*  wouldn't fail a background check, but I don't have to do a background check if I'm a private citizen.
*  Just selling a gun like I'm selling a private car to somebody. So there are guns that are the
*  ones that are a problem, and they are those guns. They're not all guns, largely handguns that are
*  acquired illegally or that have somehow been diverted from these sorts of sources, which is
*  also unique because they're durable. Right. Guns are by and large durable goods. They're not like,
*  say, drugs or some other food, whether you eat them, you ingest them, they're gone, you get more.
*  Guns stay around for a long time. So they move around. You mentioned that suicides are actually
*  the largest form, largest way that guns kill people in the US. Give us a sense of the numbers,
*  not just of suicides versus homicides, but also of what kinds of homicides we're talking about.
*  I know that when you study gun homicides in cities, that's a very different kind of thing
*  than might happen in rural areas or suburbs or whatever. Right. I don't have the suicide figures
*  in front of me when we're there, but by and large, I'm pretty sure where there's like
*  almost five to one suicides for every gun homicide in this country.
*  But sorry to put you on the spot. I didn't mean to do that.
*  No, no. I don't study suicide. So oftentimes, I neglect it as well. We talk about it in class,
*  but it's not something I spend a lot of time on. But the point is, it's not 10% more than homicides.
*  It's many times several times. Yeah, absolutely. When we're talking about
*  assaultive violence where you fire a gun at somebody and they get hit or they get hit and die.
*  I should say we know very little about non-fatal shootings because data is very poor. Even in
*  cities like Chicago, there are five or six to one non-fatal shootings for every fatal shooting. So
*  you have literally tens of thousands of people who are injured with firearms that we know very
*  little about. When it comes to homicides, which we have better data on, not perfect data, there are
*  different types. It's important to distinguish at least three of these types. One is, of course,
*  our course mass shootings, spree shootings, the kinds we see that are going around the country
*  again right now. As we're seeing in shopping malls and schools. And those are quite distinct from
*  other two real types. One is intimate partner violence, which is again, extremely serious,
*  but a very different sort than the third, which is the lion's share of gun homicides, which is
*  essentially assaults, people that know each other, arguments, disputes. And that's commonly,
*  that's kind of what shows up on the front page more often than not. And part of the reason it
*  gets more attention besides the large volume, the largest volume of gun homicides is oftentimes
*  it's public, right? Intimate partner violence happens behind closed doors. So we often don't
*  hear about it. We don't know a lot about it. It's an expressing problem, which needs attention
*  as our mass shootings. But the everyday sort of assaultive violence is the stuff that
*  we often talk about. It's the stuff I focus on. It's also the stuff that creates
*  additional trauma in communities. You're exposed to it. Somebody shot on your block. It impacts you.
*  It impacts your kids. It impacts a school. It impacts the police. Those are the sorts of
*  work that violence that we look at. So you said you seem to say when mentioning
*  assaultive violence against people who you know, or a rival gang or something like that,
*  does that category also include if someone robs a bank and it goes terribly wrong and they kill
*  somebody? Yeah, I would actually include them. That happens much more rarely than the former,
*  of course. There could be even a fourth category of state violence, especially those
*  shot by police. And then again, of course, you branch off into, was it the commission of a crime?
*  Was it a traffic stop? Was it a mistaken identity? Was it intentional? But in that case,
*  again, those are smaller portions of the total. The majority of gun homicides are these
*  assaultive interactions, essentially. So that already tells us something that when there is
*  going to be an assaultive homicide, or rather, let's just broaden it. When someone is killed
*  with a gun by another person, it sounds like usually if it's not a mass shooting, it's by
*  someone who they know or have some connection with in some more abstract way. That's right.
*  This idea of stranger homicide is actually quite rare. Two-thirds that we know of are by people
*  that are known to the person who was injured or killed. And the other third, we actually just
*  don't know. It's not that that other third is strangers. It's just that we just don't know who
*  did it. And by the way, your enemy is often not a stranger. The person who you got into a fight
*  with is often not a stranger. They usually say, you know, from your neighborhood, from your class,
*  from work, from the pub. They're not unknown. You know them. You just might not like them,
*  which is different than stranger because when we read about this in the media, of course,
*  the fear that is stoked is that it can happen to anybody. It can happen anywhere.
*  There are stray bullet killings that accidentally kill somebody, but that is, again, not the norm.
*  Most of this violence is happening in social networks, in small communities,
*  that people are known to each other. And I think it's important that we understand that. They're
*  all tragic, but they're not random. Of course. And I think that helps us understand solutions as well.
*  I mean, just to get on the table, the idea, I think that exactly because this is such a
*  hot button issue and such an emotional issue, some people will be upset when you talk about certain
*  types of gun violence and not others, right? Or you're choosing to focus on something.
*  And I'll just go on the record as saying that I would like to understand it all so that we can
*  diminish the rate of all of it, no matter what kind of gun violence it is.
*  Yeah. Yeah. I think that's fair. I think the only reason it's important to unpack it is the
*  treatment, if you will, or the response is not necessarily the same.
*  Exactly. Right.
*  You know, and I do think it's important because we often talk about gun violence as an epidemic
*  or public health problem, which it is. If we take that literally, though, we do need to understand
*  whether it was intimate partner violence versus a mass shooting is going to elicit a different
*  response. Right. It's very hard to predict in any real sense, mass shootings. You can look
*  for warning signs. There are things like red flag laws, which are when you prohibit somebody
*  from owning a firearm that can reduce intimate partner violence and mass shootings. But then
*  there are other things that would necessarily apply to say, you know, a young man on Chicago's
*  West Side who's involved with a dispute and a crew, right? They're not using legal firearms.
*  No flag would go off. They're probably outside of, say, a school system or a health system
*  where a red flag would pop up. So the response needs to fit the sort of conditions, at least
*  in some sense. So just to ground us with some specifics, one of the papers that I saw of yours,
*  I think that you sent me, was about the very short period of time between June 18 and July 5, 2020.
*  So not long after lockdowns had begun with COVID and so forth, but there was a real spur to violence
*  in Chicago. So you're in Chicago, right? You're at where you are. Sorry. Northwestern. You're
*  not really in Chicago. You're in the suburbs, but you're right there. I used to live in Chicago in,
*  you know, Lakeview. So again, not that much risk of gun violence in my neighborhood, although there
*  was a lot of risk of like drunken people coming out of Wrigley Field and swinging baseball bats,
*  but that's a different worry. So you're looking at shootings in very localized neighborhoods,
*  relatively, in Chicago. And so if I have the numbers right from that paper you wrote,
*  in that two or three week period, there were 416 shootings, 74 of which were fatal. So
*  what do we know about why that happened? Was it just stir craziness from COVID? Was it pre-existing
*  conditions that just coincidentally erupted or what? Well, I think if I had the answer to the
*  why it went up question, I would be on the front page of every paper. I think academics and
*  criminologists have lots of theories about why it went up. And there are many of them, one of
*  which is, yeah, people's routine activities changed and they changed in a way that led to increases
*  in gun violence, but decreases in other sorts of violence. So it's hard to break in your house if
*  you're home, but if you're sitting at home looking at something at social media and your opposition
*  is taunting you, well, you know right where they are and you don't have any place else to go. So
*  it changed the way people could respond. Intimate partner violence would also go up if you're at home
*  with your abuser and can't get out. So there are lots of reasons. It's hard to say which one it
*  does. It also seems to be clear that people started carrying more guns during this time period because
*  they were afraid because a lot of things were happening. But that report you mentioned point
*  out the work my team and I have been doing for the past decade, which is when it comes
*  to gun violence in cities. And here we've studied Chicago and Boston and Oakland and New York and
*  Newark and Cincinnati and New Orleans and even Evanston, which is where Northwestern lives.
*  And we've noticed a pattern that is consistent, which is gun violence concentrates in very,
*  very small social networks, even in communities that have high levels of gun violence or experience
*  high levels of gun violence. Generally, the victims and potential perpetrators of shootings
*  are in a network of a couple hundred people, right? Or depending on the city or neighborhood,
*  a couple thousand people. So in our study of Boston, 85% of all fatal and non-fatal shootings
*  happened in a network of 700 people, less than 4% of this community's population.
*  And in Chicago, and we did the whole city of Chicago, again, less than 4%, about 75%
*  of the fatal and non-fatal shootings. And when I'm talking about networks here,
*  I'm talking about instances where people were either engaging in a crime together or arrested
*  together or were co-involved in an event that elicits some system response. But we can think
*  of it broadly as the people you hang out with. The people that hang out with that would have
*  your back in a fight tend to be your network. And it turns out what we found in Chicago in general,
*  but during this three-week period, was that your probability of being a victim is directly related
*  to how many people around you are getting shot. So if you're friends, if you're in parts of a
*  network where victimizations are happening, your probability skyrockets. And in fact,
*  these can create cascades. So one person gets shot, and then a few days later, somebody else,
*  or months later, somebody else. It's almost like a chain, a chain reaction, if you will.
*  And what we found during those three-week period was all of these old well-worn pathways,
*  these old networks that had been in the neighborhood, sometimes active, sometimes
*  unactive, started popping up. So again, not in new places or unexpected places, but among
*  groups and individuals and crews who were already at high level of risk, all of a sudden,
*  the light started going off and shooting started to happen. And in one of these chains, for instance,
*  there was four shootings in 10 days. And another one, there was six shootings within 15 or 16 days.
*  But again, a sequence that was knowable and predictable, potentially. And part of what we
*  were arguing and continuing to argue is that that's the sort of information that can be actionable
*  for on the ground violence prevention efforts to try to get ahead of not just shootings, but trauma
*  and responses to people who might be victimized. So the idea is that, obviously,
*  different sets of people have different likelihoods of being in one of these terrible
*  shootings, depending on your income, your geographical location, your race, your age,
*  and things like that. But you're saying there's even more fine-grained data about who your friends
*  are that could be used to really say, no, you in particular are at heightened risk.
*  Right. So the first way you described it are usually what we call the risk factors approach.
*  And to summarize a century of research, living in a poor neighborhood, being young, being black or
*  Latino, being male, all of those things carry high levels of risk in this country for a great
*  many things, from heart disease to dropping out of school, but especially to gun homicide,
*  to being a victim of gun homicides, one of the leading causes of death for young black men in
*  this country and young black women. Latinos, of course, have higher rates than their white peers.
*  But by and large, this is one of the main killers of young men of color. But when you start to look
*  at a city like Chicago and say you're going to, again, say the west side of Chicago, well, those
*  risk factors describe 90,000 people. And I'm using air quotes here for the radio, only a few hundred
*  will get shot. So it's not being poor or being in a neighborhood that has been disinvested in and
*  segregated for centuries. That's part of it. But most people that live there don't get shot
*  or don't shoot anybody. So how do you go from these structural conditions, which are real,
*  which create these networks, to trying to figure out who's in harm's way today? And that's the jump
*  we take. You want to create small networks with a lot of guns in them, you have a segregated
*  neighborhood with high rise housing projects and you close schools. But that condition is there
*  and it needs attention. And in the meantime, you have to save lives. And this network focus
*  is more triage than it is changing structural conditions. But you need to do both, of course.
*  But it is a piece of information instead of analytics that can be used to potentially,
*  again, mitigate trauma and maybe reduce harm while you're trying to figure out the big stuff.
*  But the end result is not a vague description of risk factors. It is potentially some estimates of
*  Sean's in harm's way or Andy's friends are getting shot, maybe we should reach out to Andy.
*  And that becomes actionable for, again, for on the ground prevention efforts.
*  So was this particular jump in June, July 2020 a Chicago phenomenon or did it happen in other
*  places as well in the US? So it happened in most, it happened across the US. Chicago is definitely
*  not unique, nor was Chicago the highest increase. I mean, some of the highest increases happened in
*  cities we're not talking about. Buffalo, Flint, Newark, Chicago did horribly. Let's just be clear.
*  But it affected the whole country as a whole. Chicago probably had the highest number,
*  which we continue to do, but we're not usually the highest per capita. And Chicago had a horrible
*  2021. Things are looking a little bit better so far this year in Chicago, but it's way too early
*  to know what's going to happen. I mean, this might be jumping ahead, but is there some sociological,
*  theoretical explanation of why Chicago in particular is very bad? When you say like
*  Buffalo, Flint, I can see economic issues that are looming very large. Chicago seems to be
*  economically to be doing pretty well, at least it was when I lived there. Obviously, it has a
*  tremendous history of segregation and racial issues, but other cities do too, New York, LA,
*  whatever. I mean, or there might just be kind of special circumstances that we can't explain
*  with some grand sociological theory. Well, first of all, Chicago is special. Let's just be clear.
*  It's the greatest city in the world. However, to answer your question, Chicago, I would say today,
*  the best comparison would be Los Angeles in the 1990s. Some of the things that keep Chicago's
*  homicide rate higher than its peers, and it often gets compared to New York and LA,
*  has to do with the levels and the size of the city. What keeps Chicago unique, one of the things
*  outside of segregation, racist housing policies and all the things that kind of create neighborhoods
*  that have high crime rates and keep them that way, is its history of gangs in the city,
*  which is fundamentally different than some of those other cities. LA had a similar history,
*  as did New York, but their gangs didn't grow as big and as pervasive as Chicago's in terms of the
*  level of organization and politicization, and that still lingers to this day. Guns, Chicago recovers
*  more guns. There are more guns in Chicago than there are in New York or LA, and part of that is
*  not necessarily the city's gun laws or the states, but our proximity to states like Indiana,
*  which is where our second largest source of guns come from, which is largely a cash and carry
*  state. The two other ones which are really important, and there are others, one is the
*  continued dominance of a political machine system, which has slowly changed over time,
*  but that's part of what keeps crime in some neighborhoods and not in other neighborhoods.
*  It creates the boundaries, almost criminological gerrymandering, in a sense where, I'm going to
*  actually write that one down. It's pretty much what you have. If you're a powerful ward boss,
*  you can get services. Cops will come. They will do sweeps and serve warrants. The last thing,
*  which is so important in Chicago, is of course the utter lack of, I'm using the word reform
*  broadly, but change in policing in this city. I point to LA because LA had similar gangs to
*  Chicago in the 90s. Horrific scandals in policing. The Rampart scandal was one of the worst in the
*  history of this country. It's no longer the worst. Chicago is beating it with the new Watts scandal,
*  but it was one of the worst, and they had a consent decree, and they had massive shakeup
*  of that department. Now, I'm not saying that's the solution because the same time LA did that,
*  they also started their grid office, which was their public office for gun violence reduction.
*  Chicago just started that office two years ago. We haven't seen the reforms for the justice system.
*  We haven't seen investment and on the ground community violence prevention, and our gangs
*  and our politics were stuck essentially decades behind. I think those are some of the key, key
*  reasons that keep our homicide levels higher. I actually think we need to address all of those,
*  starting from systemic racism all the way up to investments in community violence intervention
*  efforts to see real change in Chicago. But maybe the optimistic way of reading what you just said
*  is that police reform and changing in police practices or neighborhood, I don't know,
*  outreach practices, et cetera, could potentially have a really big positive impact.
*  I think they can. I think the key is you have to do them all at once. I think going back to the
*  networks we study, yeah, you can stop bleeding in networks, but the network is huge and it's going
*  to win. Unless you do something to mitigate, say, people's entrance into the network or dissipate,
*  say, segregation that can do those sorts of things, you're just going to try to stop the water from
*  coming through the dam in some ways. For example, when you look at trying to change policing
*  efforts and investment in community-based violence prevention efforts, Chicago's,
*  again, I don't have the numbers in front of me, but it's the largest single investment in community
*  violence intervention in the city's history, upwards of $36 million. That's a police budget
*  of $2 billion, right? We have 12,000 police officers and you have 200 street outreach workers
*  in the city. You're trying to build a profession of, say, street outreach with good investment for
*  the first time ever, but it's not on par with what it even needs to be close to being. I think
*  you have to get those things. I did mention in LA, they both had some serious efforts at changing
*  the structure of policing as they were also increasing investments in community violence
*  prevention. They were doing those things at the same time. If you look at Los Angeles today and
*  their grid office, they have officers that are assigned to these community places. Is the
*  relationship always great? No, but there is information sharing. There are accountability
*  mechanisms in place and there are just some things that we need to figure out that we're
*  just starting. I actually do think that the starting of the office, or excuse me, the expansion of the
*  Office for Violence Prevention in Chicago is great. The state of Illinois also just created its own
*  Office for Violence Prevention. That is hugely important. It turns out there are other cities
*  in Illinois and some of them need a lot of help and they haven't been getting attention
*  because of the dominance of Chicago and the public narrative.
*  I wanted to ask more about the gangs because clearly they play an important role and I suspect
*  that the typical person's view of gangs and how they work, etc., doesn't perfectly match up with
*  the reality of it, especially since you said how Chicago was especially a prevalent case.
*  Since I lived in both Chicago and LA, if you asked me, I would have said LA is the gang city
*  much more than Chicago is. Is that just because I'm out of date? You haven't realized Chicago's
*  specialness enough, essentially. I don't know enough about LA in terms of its neighborhood
*  factors. I would assume it's more similar to Chicago. Today, street gangs in Chicago cruise
*  cliques. They're much smaller than they were in their heyday of the 90s. They're very neighborhood
*  based. There are some groups that are still more organized and involved in high-level
*  criminal activities, but very few. There are, by some estimates, 900 small cliques and crews in
*  the city of Chicago. Most of them, again, are bound to a particular neighborhood, a couple blocks
*  that they have been. Their history goes back years and years and years and decades.
*  The dynamics change quickly. A lot of it has to do with, in Chicago, it's tied to, again,
*  old disputes, new disputes, things that might flare up online and could lead to offline violence,
*  which happens, but not as often as the media would have you think. But they're small. There's small
*  crews that are really tied to a neighborhood and their friends. That part is not as different than
*  groups in other cities. It's this long legacy, the length with which people can trace back
*  their ties to such and such a group goes back generations. It has meaning, gives meaning to
*  life. Sometimes it's a voice of resistance. Sometimes it's a voice of protection.
*  And that's one of the things that happens. As a real simple example, when you ask people
*  how they find their guns, the idea of a gang, the fundamental reason people join gangs
*  is for protection, which is the same reason people buy guns. And who in Chicago are more
*  likely to have guns? Gang members. So if you're feeling you need protection, safety in numbers,
*  and they have access to weapons, that's kind of a dangerous mix for the people who are involved,
*  because it really does. The truth is, the more you're involved, the more likely you are to get
*  harmed. And even though you need safety and that fact that people feel so unsafe, they're willing
*  to do things they know will make them less safe, speaks to the just the level of need there is to
*  make people, especially young people feel safe in schools and their community and their homes.
*  That's a tall order. That's a tall order that is not just one system or one agency.
*  It's definitely a whole level thing. And so it's not just the essence of what is going on with the
*  gangs here. It's not Al Capone and a machine that is doing big high level crime or anything like
*  that. It's more like a local social, us against the world kind of thing. If I'm a kid growing up
*  in a certain block of Chicago, what you're telling me is that life is tough. It's dangerous out
*  there. And I'm going to seek safety in the gang that has been either running, I guess, or at least
*  involved with my block for decades now. That's right. And I just want to just reiterate again,
*  you know, if there are 900 crews in Chicago, there are probably a handful that are actively involved
*  in some organized stuff. And every year, every other year, you'll see a big federal case from
*  the US Attorney's Office. Those four or five groups that are involved in that should be treated,
*  you know, in that way, figure out the activities. But that means, you know, 895 of them are not.
*  And so the danger when it comes to policy is that you treat those 895 or 885 as if they were Al
*  Capone, right? Or the gangster disciples of the 90s or whatever the case might be. And they're just
*  not. And that's the slippery slope with gang policies. Gangs become, you know, a catch-all
*  for everything bad and evil and the boogeyman. And in reality, most are, as you described,
*  a crew of people on the block who are protecting themselves and their friends. And by the way,
*  you know, sometimes avenging them. And that creates problems that need resolution for sure.
*  But, you know, I think, again, I think our US Attorney's Office in Illinois makes these big
*  cases because they can't because it's happening. But we have to remember that most groups are not
*  that. Most groups are these these sort of side corner groups. And some of them are a little bit
*  bigger, but they're small. And they're they the history is there. And it's tied to a very specific
*  place that's been segregated and locked up and locked out for generations. Other than just sort
*  of mutual protection or even just socializing or the gangs also involved in the drug trade or petty
*  crimes or protection rackets, anything like that. I don't know what the lifetime of the gang members
*  really like, to be honest. I think so. I think the the best way to describe, you know, delinquent or
*  criminal activity of gangs is cafeteria style. So which is most groups do a little of this,
*  a little of that. We sell something, we steal something, we're bored, we're at a party, we fight.
*  Most of it is not extremely well thought out or planned. Quite the opposite. Most of it's very
*  haphazard. You know, violence is ever present in their lives. It occupies, it consumes,
*  traumatizes and re-traumatizes. But they don't spend every day. In fact, they spend most of their
*  days in total compliance with the law, playing video games, looking at social media,
*  you know, hanging out like basically what young people do or people in their 20s do.
*  Most of it is not spent, you know, thinking about or even engaging in crime. But violence is ever
*  present. It really does consume all of their energy and time, but it's not something they're
*  engaging in constantly. If that were true, the, you know, the levels of violence would be even
*  worse than they are, but it's not. It's sporadic, it's rare, but traumatic and lingers like a ghost,
*  you know, on the block that haunts them and rehaunts them.
*  – I'm kind of intrigued by the role of social media here, which I never really thought of. Like,
*  are the gangs insulting each other on Twitter or how is this working?
*  – Yeah. So I'm going to have to defer to some of my great colleagues, Forest Stewart at Stanford,
*  Desmond Patton at Columbia and Jeffrey Lane at Rutgers. You know, it's complicated. So first of
*  all, I don't know anybody between 14 and say 26 who's not on social media. So it's important to
*  distinguish this is just normal behavior, being on social media, connecting, you know, ribbing
*  people, trolling people. It's not necessarily nice behavior, trolling people, but it's just part of,
*  I have teenagers myself, right? It's just part of, you know, what we do as a society.
*  What's happening on social media is people are using it to, you know, taunt rivals, to disrespect
*  rivals, to honor their friends. As one of our colleagues, Desmond Patton, talks about to express
*  grief deeply in ways that are hard to do in other spaces. All of that's playing out online.
*  The vast majority of these things that happen online never end up in violence, right? They are,
*  in fact, ways to do symbolic violence, which is not good either, to be clear. The problem is,
*  of course, when it does lead to offline violence. And we don't actually know enough about it yet
*  to understand what it does. It does seem, in my assessment, it does seem to make things ramp up
*  much more quickly because it's nonstop, right? And it can, you know, especially where music is
*  concerned, drill music, you can tell your story and it's out there and now other people can view
*  it. So it's almost public, it's public displays. People are watching and seeing and reacting,
*  which is not different than what people do offline, except it's immediate and you have
*  a broader audience. It can spread very quickly. But again, the link between online and offline
*  violence is it's hard to make it causal, but it definitely does happen. And I think people are
*  working on it to try and understand, you know, how can that be used? Because I will also tell you,
*  outreach workers in the city use it to calm things down as well, right? So you can use those tools.
*  And there are plenty of people talking about, well, can we have trained social workers in
*  this space or people that can respond? And outreach workers and violence preventionists are doing that
*  naturally. But again, it's sort of part of what you do. You got somebody's name, you look them up,
*  you Google them, right? So of course, it's going to permeate that part of work and culture as well.
*  Part of me wants to say that we should, you know, try to replace actual fights with guns on the
*  streets with fights in World of Warcraft or something like that. But I think you're probably
*  like you're implying maybe that if they did that, it would just spill over into the streets anyway.
*  So that's not the right thing to do. But well, again, I think we just need to take stock of where
*  we are as a society. This is not new, right? We used to the 1940s, there were entire senatorial
*  hearings on Mickey Mouse and comic books and Mad Magazine. Because it was a new form of media or
*  record hearings around, you know, Ozzy Osbourne or NWA, I guess is a common theme. This is just the
*  latest way of things kind of getting out there. But the speed with which it happens is quite
*  different, of course, because it's immediate and it can kind of you know, doesn't things don't get
*  to calm down as much. And you mentioned a little bit, but I wanted to focus in on just for a second
*  the role of the police in this. It can be for better or for worse, I imagine. Do you think
*  that there's an issue where police are just sort of ignoring certain neighborhoods, letting things
*  go? Or is it that there's a strategy that is just ill suited to the circumstances in these certain
*  neighborhoods? Well, it's so yes, and yes, you know, I think, again, the crime map in Chicago
*  about which neighborhoods have the highest levels of violence hasn't changed in a century. So it's
*  not a secret to anybody. How those places are policed are of course severe, right? And in fact,
*  it's changed. And this between the 60s and the 80s, the cry was there was no police presence.
*  And now we're on the other end of the spectrum where everything is hyper surveilled. So I think
*  you know, the idea of being constantly surveilled and constantly incarcerated or stopped is still
*  true. I think it's just it's a it is a tragic way of life. And it hasn't changed. And I think that's
*  kind of what some of the calls are. There are things in of course, policing that and again,
*  what we know about policing that is associated with gun violence reductions, it's actually
*  limited, very small and very precise. It's not it's the opposite of stop and frisk.
*  Right. So policing that is known to have an impact on gun violence tends to focus on a small number
*  of people, a small number of places in a small number of behaviors, which is an argument for
*  more focused rather than broadened policing powers and policing activity. Still a lot of problems,
*  which can cause damage, of course, as well, if you get the wrong people, or you're looking at the
*  wrong behaviors. But by and large, the research suggests that focused policing is much more
*  impactful on levels of gun violence than than expansion of it. But they continually show up
*  in the same neighborhoods time and time and time again. So you know, neighborhoods are subjected
*  to the same sorts of surveillance and policing. And it spills over into schools and parks and
*  libraries and sort of other spaces as well. So I think this is where the network analysis stuff
*  that you mentioned earlier begins to come in. There's a network of people let me just ask the
*  obvious question, are we talking about networks of victims of shootings or networks of people
*  shooting other people? So great question. So when I'm talking, the networks are created
*  through instances of co-arrest or being stopped together by the police. So it is actually setting
*  aside anything around culpability. It's an observation made by police at a point in time
*  and space. You know, there are biases in police data, which are important. We're able to see a
*  lot of those. So say failure to comply often is something that's officer based robbery, assault,
*  arson, things like that tend to be come to the attention of police from from civilians. So we
*  take all those things to account. But basically, if you and I robbed somebody together, we have a tie.
*  And then if I, you know, committed an assault with somebody else, we have a tie and you string these
*  things together and it creates actually a network of risky behaviors, right, things that are
*  inherently you and I engaging in a behavior that that could be risky. So but to your comment about
*  victim and suspect, or people that are involved, I focus mainly on victims, one because in Chicago,
*  we have abysmally low clearance rates, but more to the point, violence prevention is about saving
*  lives and focusing on who's in harm's way who's experiencing trauma is the kind of most immediately
*  actionable information. And we generally have all of the information about who was injured.
*  And, you know, from a public health standpoint, it shouldn't matter whether you have a felony
*  conviction or, you know, are a bad parent or you dropped out of school, none of that should matter
*  if you're focusing on saving somebody's life. So the focus tends to be on victims, but the victims
*  and suspects and sort of everybody else who's involved, they're all in the same network,
*  basically. And so but but really valuing life and prioritizing that is really key as we think about
*  how you use these things for for intervention purposes. But as far as your data are concerned,
*  then if there is someone who gets shot just as an accident, or, you know, was an innocent bystander
*  during a robbery, they would still count as in your network because you're not trying to, you're not
*  deciding ahead of time that doesn't count.
*  Correct, correct. They're in there. And by the way, you know, what one of the things we learned by
*  having them in there is many of these sort of stray bullet incidents aren't aren't that far
*  stray. Right? They're tragic. They weren't the intended target. But they were literally standing
*  next to somebody who was and so by the way, this often happens and you can change the name of the
*  individual I often do this when I go to different cities, I'll describe a seven year old who got
*  shot at a park or a birthday party. And their parent or their cousin was the intended target.
*  And we hear about the young seven year old, but we don't hear about the 27 year old who was holding
*  their hand. And so tragic, but not random, right? Well, I guess that that's that.
*  That was gonna be my next question. I mean, are there? Do we count also people who are clearly
*  related, either socially or biologically to the person in the network or, you know, an associate
*  of them or how much subjectivity versus objectivity is involved in drawing the lines between who's in
*  a network and who's not? In our particular case, we still rely on a metric that we have for everybody,
*  right? So if we have the all of the say arrests in Chicago, that's what includes you in this in the
*  sample, which by the way, to your point means we're severely underestimating relationships.
*  Okay, good. Right. So if you rob a bank with somebody is probably not a stranger. It's probably
*  somebody you know, could be kin, could be a neighbor, could be somebody, a classmate,
*  it's probably somebody you've known a long time. But we don't have that information. At a minimum,
*  we have we were connected at least once, sometimes more than once. But we're probably underestimating
*  behavior. And of course, most incidents never get reported to the police. It's to begin with. So,
*  you know, we're continuing. So our estimates are extremely conservative. If you have information
*  like you're talking about, and we see this qualitatively, like when we're working with
*  partners, or we're trying to understand more about a particular neighborhood or group or whatever,
*  then we start to get into this information. And to your point, yeah, somebody's, you know,
*  former romantic partner, or their year neighbor of 20 years, or their cousin or their uncle.
*  But we just don't have that systematically. But you know, qualitatively, it seems to be true,
*  but I don't have it at the same level of analysis as these other instances.
*  Yeah, you kind of begin to see as a scientist why the surveillance state is so attractive,
*  because we would have so much more data if we just tracked everybody and knew everything about them
*  and could plug it into a computer. I'm not actually in favor of a very high level surveillance state
*  like that, but the data would be cleaner if we knew everything.
*  So, Normi, to be clear, and also to be clear, we're using publicly available arrest records.
*  So we're not using CCTV, license plates, readers, you know, all those things are a totally different
*  level. Again, going to we rely on basically public data. You know, you can go to your court
*  and get arrest records. We're just looking at the digital versions of those, which again,
*  in most cases are available. We don't even have to FOIA them, but you could.
*  You know, it's just a matter of looking at them slightly differently.
*  You know, of course, the surveillance state in that way is also goes horribly wrong. I know you
*  were teasing, but we're on tape here. I want to make sure you're not allowed to joke on the podcast
*  without immediately saying that was a joke. Otherwise, people will take it out of context,
*  because that's absolutely true. But that does bring up, you know, the prospect of perhaps,
*  or maybe it's already happening, collaborating with either police departments or public health
*  agencies or something like that. I mean, you say that you just use publicly available data,
*  but are there further perspective investigations in the future where you use other kind of data sets?
*  So you named two. So short answer is there's lots of potential uses for the science,
*  but you named two agencies that use them very differently. You mentioned the police and public
*  health entities. There's a third one, which I'm working with, which are community-based entities.
*  Police have used these technologies and sort of approaches, and it hasn't gone extremely well.
*  And it hasn't gone extremely well because they've done typically what police do. They get
*  printout, they make a list, and they do what cops do, which is they work a list. And whoever's on
*  the top of the list is number one, and whoever's number two is number two. And, you know, that's
*  how policing tends to work. They work calls, they work lists, which is problematic when it's
*  something that's imperfect, like data and analytics, right? When you look at the predictions or when
*  you look at these statistical models, they're pretty good. They help, they give you information,
*  but if you follow them blindly, it's problematic. It's especially problematic when it's done from
*  the arm of the state that treats a victim like an offender, right? So as soon as you start
*  going into this world of trying to find a suspect or trying to find an offender,
*  there's this little thing called the constitution and even, you know,
*  bigger thing called morality about how do you do that in a way that's fair and just and transparent.
*  And we haven't seen that done successfully yet in the policing context. In a public health context,
*  the science is exactly the science of contact tracing. It's literally finding out who's in
*  harm's way, getting resources to keep them safe. And it can be done successfully. And we've seen
*  this done, by the way, in other epidemics, the HIV epidemic, when we have outbreaks of other
*  infectious diseases. You know, COVID is in one example, but COVID spreads much more quickly than
*  gun violence. It's an airborne pathogen, right? And so it's harder to contain COVID. Gun violence is
*  relational. So it's more like a bloodborne pathogen than an airborne pathogen. But you're still tracing
*  these patterns. This is what street outreach workers do, which is the last thing I'll mention
*  where we're trying to find the uses. Street outreach workers, these, you know, people with
*  lived experience that are trying to stop disputes, they literally place themselves in these networks.
*  That's how they do their job. They're trying to figure out what are the active disputes?
*  How do I get myself situated in there such that we reduce harm? That's a perfect use for it. That's
*  not tied to overly harsh penalties or removing somebody's liberties. Also not without potential
*  problems. But, you know, there are ways we've done this again in public health that I think
*  offer at least a starting point to use it. The last thing I'll say, this comparison is when you
*  think about science, right? Science is providing some tools. How do we use that tool? So when you
*  think about spatial models, well, it can help get a fire truck to the scene of a fire more quickly,
*  or it can be used to direct a drone. Same math, but the use is fundamentally different. And
*  we need to be honest about how it's being used. As an academic, I try to say, here's what I think,
*  I try to work with partners to make sure that happens. But, you know, science gets out there
*  in peer reviewed journals, and anybody can pick it up and take and go with it. I'm trying to
*  figure out ways to improve that approach. But, you know, it's tricky.
*  Well, I love the fact that you bring up the idea that the cops just tend to have a list and work
*  the list. And what you're doing is something a bit more sophisticated than that, because you have
*  more information than just an unordered list. And this is where it becomes a little mathy,
*  a little sciency in a fun way. When you have these networks, so you have nodes who are people and
*  they're connected by relationships. As far as I know, I'm not a super expert, but there are
*  different kinds of networks, right? There are dense networks, sparse networks, small world networks.
*  Are there characteristic features of the kinds of networks that you're seeing?
*  So this is a great question. Let me also just say, when you talk about, we all live in these worlds,
*  right? And we all know a lot about our own small world. And so when you bring these images, say,
*  to street outreach workers or teachers, my sister's a teacher, we often talk about like,
*  what, I was like, tell me what's going on in your school. She starts describing them. I see network
*  images. Right? So if you have that image, if you have the roadmap, the whole roadmap, and you have
*  experts that can be like, let me tell you about this network. I can only say you and I, you know,
*  Rob somebody together, but then somebody's like, no, let me tell you, Sean and Andy played football
*  together. And Sean used to date Andy's sister and then they broke up. And then he hung out.
*  All of a sudden, the context becomes important. And you only get that by engaging local experts,
*  good preachers, teachers, cops, outreach workers, social workers. They know a community or they
*  should know a community. That's what makes this information actionable. And that's what didn't
*  happen in some of these instances. Like if you're just working a list, you don't care whether Sean's
*  already got a job and turned his life around. He's on the list. Right? What, what similarities
*  are we seeing in these networks? What are we seeing to answer your other question?
*  One, they're super small and they're super concentrated. So even when you think of a
*  neighborhood that's disproportionately impacted by gun violence with say 40,000 people, this
*  network has a couple hundred people in it. It's very small. It's also not secret. That's the other
*  thing. If you actually talk to folks, they'll be like, oh, there's a crew over here. Well, who's
*  in the, like, they can tell you these things. So it's, it, it requires again, being really connected
*  to community approaches or the community itself to make it actionable. So it clusters. It's very
*  small. And that's, this is true in, in most communities and most cities, regardless of city
*  size, regardless of the size of the neighborhood, it's a very small part of any community that is
*  actively engaged in these things. And then of course, this, the other kind of thing we're seeing,
*  which is more the rule than the exception is gunshot victimizations cluster, they clump together.
*  So even within this space, this social space, there's still a pocket where these, where these
*  shootings cluster, which again, when you think about the implications for immediate intervention,
*  setting aside large scale interventions that are needed to keep people out of these networks in the
*  first place, it means you're talking about focused interventions, right? That can reach people as
*  opposed to broad scale, you know, stop and frisk, right? It's the opposite of that. It's, it's,
*  it's, it's kind of focusing on particular behaviors, particular individuals, particular
*  geographical locations. And that's where the attention is. And you can do that with therapy,
*  you can do that with interventions, you can do that with jobs, you can do that with schools,
*  but you also have to know, what are those, what are those individuals in that network need?
*  Do they already have high school diplomas? Do they already have jobs? Maybe they don't need a job
*  because they already have one. Spoiler alert, they need jobs, right? But like, if I already have a
*  job, the job program is not appealing. If I already have a high school diploma, I don't need a GED
*  program. We are smart enough as humans to be able to figure out what individuals who are in say,
*  a small network need. You ask them actually, right? Or you ask people who know them, hey,
*  there are these 20 folks, you know, in your, in your neighborhood, what do you know them? What
*  do they need? And then you can kind of direct accordingly. It can't just be everybody needs
*  to do these three things, go. It has to be like, what are we, what are we learning about the problem?
*  It might not involve groups or gangs. It might be family dispute. It might be intimate partner
*  violence. It's important to know that. And every neighborhood is a little different, you know,
*  in Chicago, Latino communities have a very different sort of gang presence still than
*  black communities, right? They're just, they're different groups. You can't do, you can't cut and
*  paste. You got to understand the contexts, you know, conversely, black communities don't have
*  to fear ICE the way Latino communities did, especially under Trump, right? There was a clear,
*  you know, fear that rose during that, during those four years that changed the dynamic of people
*  talking to people. And, you know, you wouldn't expect that say in a black community in Chicago.
*  Well, I'm not sure how helpful it is to your research, but I do have to ask about the topology
*  of these networks. Are they situations where there's like a set of a very, very, very small
*  set of super influencers who know everybody? Or is it that everybody else in the network knows
*  everybody else? I mean, that would presumably suggest different strategies for dealing with
*  things. So there are different topologies. The general rule is in networks, but we also see this
*  in where violence is concerned. Most people have one or two ties, right? Most people, most humans,
*  right? We're talking about people, right? They age out of crime. You know, when you think about young
*  men in particular, young men in particular do a lot of risky, stupid things until they're 26,
*  27 years old. This is true of humanity. And so that's what we see. Most people have one or two
*  ties. And then there are some people that have a lot of ties, right? And the people that have a lot
*  of ties are hubs. They are, you use the word influencer. We can think about super spreaders,
*  right? This idea that they are people who navigate different sorts of networks and bring stuff with
*  them. And part of what we're seeing is that those folks are especially vulnerable because they are,
*  you know, if you're, again, let's just use the context of street crews, right? Or gangs.
*  If you hang around with one gang, we know it increases your rate of victimization. But if
*  you're starting to hang around with two or three or four different crews and those crews don't like
*  each other, either you have some kind of predisposition to make everybody like you or
*  you're really putting yourself out there. And you could be putting it out there for all sorts
*  of reasons. Family ties that cross countries. You know, it could be an inadvertent ties about
*  schools or sports, or you could be running a scam or an operation, or you could actually be engaging
*  in dealing firearms or drugs, whatever. I don't know. But that person who is connecting disconnected
*  parts of the networks, they're unique and there aren't as many of them. Most folks have one or
*  two ties and it's not even a, it's not a, I say big deal. It is a big deal because it puts them
*  in harm's way, but it's not for stuff. These, we're not talking about kingpins, right? Most
*  of the people that are caught up in these spaces are just regular folks. I mean, I guess, I guess
*  that's the point. The short lesson here is that it's not really a dictatorship with one person
*  ruling everything and telling everyone what to do. It sounds like it's a little bit more organic
*  with people knowing each other and knowing each other. Yeah, that's right. I think, let me just,
*  just to say one important caveat. There's, and let's put this in scale. Right now,
*  it's hard to estimate. There are about 900 crews, gangs in Chicago. The way vast majority of them
*  are, are these neighborhood based small entities, which is a departure from Chicago in the nineties,
*  of course. But most of them are these side street, street crews, 20 guys, very informal structures,
*  there are absolutely one or two or three, maybe even 10 groups that are more organized and really
*  kind of, you know, involved in deep, deeper criminal activities. On those 10 though, turns out
*  law enforcement knows how to make cases on those 10. They've been doing it for years.
*  The mistake is when you treat those other 890 like those 10, right? And which, which is those other
*  890, which is the majority of the sort of groups, they're just different. You know, they are,
*  it's, it's not an on off switch. It's a toggle switch, right? You know, we have this crew,
*  it's from the block. There's some family ties in it. You know, somebody gets hurt, we rally together
*  and things get amped up. And then it kind of just calms down. And then I get a job and I leave,
*  or I have a kid and I stopped hanging out. Like, it's much more amorphous than that, which makes
*  it a little scarier in some ways, because you don't have these nice, neat categories, gang A,
*  gang B, gang C, gang D. It's messy. Unlike Chicago in the 90s, people liked it. There was this nation,
*  there was that nation, we didn't get along. I could draw a schematic, everybody understood it. It's
*  not like that anymore. And it's not like that in most cities in the US. And so what works, yeah.
*  I mean, part of your ambition, obviously, is just as an academic, you want to understand what's
*  going on. But you also want to do some good here, because it does seem like there's room for doing
*  some good. And the good to be done is not just help to arrest people who shoot others, but to
*  prevent it from happening ahead of time, right? To give some warning. I mean, can you say a little
*  bit about how we would imagine, in a very specific way, what we would do to lower the chances that
*  someone is going to be a victim of one of these shootings? Yeah. So I think the first thing,
*  if we take the lessons we've learned, and again, I want to stress that this is more of the triage
*  approach. But you do need to combine it with thinking about these bigger issues, like keeping
*  people out of these networks in the first place. When there's an event, when there's a shooting,
*  saturating that part of the network with a trauma response could be life-saving,
*  which is you can help mitigate retaliation, which happens in about a third of cases in Chicago.
*  But more than that, if you reduce the trauma of the people involved, you are saving lives.
*  And we're starting to see this in hospital-based programs as well. They're starting treating the
*  victim's trauma immediately and the victim's family's trauma immediately by trying to connect
*  them with services, by trying to divert aggression, by trying to really understand and unpack
*  the health consequences of individuals that are involved. I think that's one of the most
*  promising things, but we're still learning a lot about that. So one of the differences
*  in our prior research on, say, PTSD, a lot of which comes from veterans,
*  you know, veterans have in theory left the war zone, as it were, right? They're now home. And
*  so how do you reintegrate a vet into their home life, which is in theory safe? A lot of the
*  people who are caught up in shootings, they go right back to the same block. They were shot
*  600 feet away from their home and they walk past that every day. Right? And so they're
*  re-traumatized simply by living in the same neighborhood and they see the people that shot
*  them. So it's different. It's new. And understanding that element, that you have to deal with the
*  trauma and people that are continually re-exposed to it, and then somebody else gets shot, right,
*  on the same block, that's unique. And we need to really, you know, triple down on that and
*  invest in it and understand that it is different than other contexts. And, you know, and it's also
*  thinking about, it's not like the public health system has a glowing report card from black and
*  other non-white communities in this country. You know, there's cynicism, there's estrangement,
*  there's all of these things that have been done, you know, Tuskegee experiments and beyond that
*  we need to understand in this context. So, you know, but I do think responding to precise parts
*  of a network quickly can reduce some of the trauma. It won't eliminate it. You know, I think it's
*  when we get into this world and we use words like prediction, you know, chasing that as the answer
*  is not the solution. Understanding it's more information that you can respond to quickly,
*  that's kind of the key in my opinion. But let me just try to respond quickly. Yeah. Let me
*  just try to distinguish between what seems natural and obvious to me, which is that
*  literally the family members that go to the hospital with the shooting victim deserve some
*  care and attention to help them get over this trauma. But then, are you suggesting that there
*  are people that you can identify as being in the network with that victim, even though they don't
*  go to the hospital, even though they weren't there. But is there a broader strategy just to warn
*  people or help them lower their chances of being part of this cycle of violence?
*  Well, that's a good question. I think for folks that have been in, and you know, shout out to
*  other first responders in this space, when you're in a hospital room after a shooting,
*  it is a microcosm of the neighborhood and the dispute in many cases. So not only are the victim
*  and their family or somebody showing up there, so are the police. Oftentimes other people are
*  injured as well. And so you have in a matter of minutes or hours, you have the victim, the
*  victim's family, the police, the healthcare system, potentially child and protective services,
*  you know, who's like everybody is converging. And this time and pace while somebody is going
*  through the worst moment of their life. And so it is an opportunity to see and be firsthand
*  proximate to those folks that you might not have information on and reach them. And by the way,
*  when I talk about family, I don't, you know, just going back to the parts of our conversation,
*  the average age of a homicide victim in Chicago is 27 and a half years old. It's almost 28 years old.
*  When we look at some of the programs who are serving this population, a good chunk of those
*  27 and 28 year olds have kids. So you now have a child whose parent has been shot, potentially
*  murdered, might be incarcerated. And we talk about a cycle of violence. That's an instance where the
*  cycle of violence is occurring, right? A child experiencing this trauma, now having to have a
*  parent who's dead, incarcerated or injured. That kid needs some attention too, right?
*  Right.
*  Getting that. And when we work with outreach organizations and are dealing with folks that
*  are injured and have survived, I can't tell you the number of times people said, I wish this was
*  there when I was 12 or I was in middle school or what about my little cousin or what about my kid
*  that had access to these things. So thinking about those moments when you can make those connections
*  to non-punitive ways to improve people's lives, I think those are opportunities to be clear.
*  I think this space is people are innovating right now because we haven't done this.
*  And especially as we're in a time when there's an increase in gun violence nationwide,
*  the potential for innovation is huge. But it means we got to listen to folks that are doing the work.
*  Right. And it's listen to the doctors, first responders, community violence preventionists,
*  educators, social workers. There's lots of folks that know a lot about this that are there. How do
*  we boost the things we think are helpful? How do we make sure that we're not just going to be
*  doing the things we think are helpful? And how do we turn down the things we think are potentially
*  harmful? Which makes me wonder, I mean, coming the other way, do you find that those people who you
*  just listed as well as the law enforcement side of things, do they listen to you as the ivory tower
*  academic from Evanston coming in and saying, you really need some more network theory in your life?
*  Well, yeah, of course they listen to me. No, I like to think they listen to me. I should be more
*  precise and say I get invited to these spaces. And to be clear, I'm honored to be in those spaces
*  because I'm also invited into, again, from neighborhood organizations to the state houses.
*  I'm glad that I'm in those spaces and I appreciate being in those spaces. I think they listen.
*  Understanding that some of these things don't work on an election cycle is tricky,
*  or a funding cycle is tricky. But I think people inherently understand the importance of
*  context and networks. I think we err in the policy realm towards individual explanations.
*  And as a sociologist, as a social scientist, crime rates are way more than people making bad
*  decisions. That's an overly simplistic view of crime and violence. But you laugh. That's how
*  a lot of our programming and responses are, trying to get people to make better decisions.
*  Now, let's be clear, plenty of people make bad decisions. I'm not saying people don't have
*  choices and everything is forced. People make choices. Choices are tough. So if you feel unsafe,
*  if you feel your life is in danger to you carrying a gun, even if you're prohibited,
*  because the state is not there for you, is a reasonable choice. But then it comes back to,
*  why are there so many guns in my neighborhood? Why is the state failing to protect me? And why
*  am I in harm's way to begin with? All of those things, they have nothing to do with your choice.
*  You both froze.
*  They have everything to do with the context in which you live. And that part is harder to
*  think about in just an individual response. And going back to something we said earlier,
*  if you follow the program and you have 100% attendance and you get shot, does the program
*  fail? Because your opposition didn't change their behavior. Even if you as an individual
*  changed your behavior, it gets really, really complicated really fast. Even when you see
*  approaches that are trying to focus on individuals and change behaviors, which is important,
*  again, you don't want people carrying guns. You want people to make better decisions. You want
*  them to complete education and so on. You can have individuals who complete the programs,
*  who have 100% attendance, who stop carrying guns, but the neighborhood hasn't changed.
*  And so they're victimized not because they're still involved, but because the opposition is
*  still involved. And so if you're not paying attention to the context, all of a sudden,
*  what looks like an individual failure isn't. It's tricky because again, you want to reach people
*  and have services, but understanding context is so key. And thinking about neighborhood level
*  interventions, how do you understand the dynamics in a whole neighborhood? How do you understand all
*  these other reasons? We can't keep our eye off of that. So we have to move beyond purely individual
*  solutions, though we need plenty of individual solutions as well. We need everything.
*  But I do like to just caution that how we understand patterns is much more than just
*  individuals. Going back to networks, networks aren't about one person. They're about a system.
*  It's a systems approach to understanding these things, and that involves understanding dynamics
*  and time and context and all the other things that are involved. And then you can kind of zoom in and
*  out when you need an individual approach. It's an individual approach. When you need something
*  larger, it should be something larger. And do it all at once. PS. Well, you've certainly given us a
*  lot to think about. Let me just maybe for a final thought ask whether or not this kind of way of
*  thinking about things extends to the other kinds of gun violence that we opened the podcast talking
*  about, about suicides, mass shootings. You've been talking focusing on a specific way that gun
*  violence happens. Are there broader lessons to be drawn for this way higher than it should be
*  number of shootings that we have in our country? Yeah, it's hard because I don't study,
*  um, you know, I don't study suicide, but because suicide seems isolated, it's actually almost the
*  inverse. So when we think about what we know about suicide attempts, say among high school
*  age students, we actually know that those that have sparse networks or no networks have more
*  suicide attempts. Slightly different though than the types of networks that we're talking about.
*  So there's potentially some relationships, but I don't think it's the same pattern just given the
*  isolations. It's really hard to understand mass shootings in this context only because again,
*  in most cases, the target has some network related purpose, right? My former school,
*  my current school, a lover, a workplace that I was involved in. So there's non-random connection
*  in some instances, but it's not quite as clustered as you might think. Again,
*  thinking about warning signs, red flags, even in the domestic violence situations,
*  intimate partner violence, red flags kind of tell you still not random, still a network. We have
*  an intimate relationship, but slightly different. And I don't know enough about it to say it.
*  You know, I think that becomes kind of important. As usual, this is a perfect
*  place to end in the sense that you just said you don't know enough, which is good. I like it when
*  people say they don't know enough about something. Not everyone is willing to do that. And occasionally,
*  it's exactly the right thing to say. So Andrew Poppichristos, thanks very much for being on
*  the Winescape Podcast. It was a pleasure. I really appreciate it and happy to follow up on anything.
*  Thank you.

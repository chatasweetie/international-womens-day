# -*- coding: utf-8 -*-
###Above is to find the system's source code encoding
from model import Speaker, Talk
from random import randint, choice



################################################################################
# Add your track names (it can be as little as 1 to as many as 6)              #
################################################################################
track_names = [
            "Green Area",
            "Blue Area",
            "Yellow Area",
            ]

################################################################################
# Add the date of your event (format: Month/Day/Year)                          #
################################################################################
date = "03/17/2018"

################################################################################
# Add the time sessions, don't forget registration time!                       #
################################################################################
session_times = [
                "8:30am",
                "9:30am",
                "10:00am",
                "11:00am",
                "12:00pm",
                "1:00pm",
                "2:00pm",
                "3:00pm",
                "4:00pm",
                "5:00pm",
                "5:30pm",
                ]
################################################################################
# Add the length of the sessions in minutes                                    #
# This is for the calendar event creation                                      #
################################################################################
session_length = "45"


################################################################################
# Non Speaker Events                                                 #
################################################################################

registration = Talk("Registration & Breakfast", "Get your name badge and enjoy and light breakfast", time="8:30am", track_name="Green Area")
welcome = Talk("Welcome", "Come together to kick off the day", time="9:30am", track_name="Green Area")
lunch = Talk("Lunch", "Delicious Food and Connecting with others", time="1:00pm", track_name="Green Area")
closing = Talk("Closing & Raffle", "Join us on wrapping up the day with a raffle and thank yous", time="5:00pm", track_name="Green Area")
networking = Talk("Networking", "Connect with people. Doors close at 6:30pm", time="5:30pm", track_name="Green Area")

################################################################################
# Add your Speaker Information                                                 #
################################################################################

chloe = Speaker(
    first_name="Chloe",
    last_name="Condon",
    )
chloe.add_social_media(
    twitter="ChloeCondon",
    linkedin="https://www.linkedin.com/in/chloecondon/",
    website="medium.com/@chloecondon",
    youtube="https://www.youtube.com/channel/UChWn8UyK3PNfMLYOCzrH6sQ/videos",
    facebook="https://www.facebook.com/misschloecondon",
    )
chloe.add_professional_information(
    profession="Developer Evangelist",
    empolyeer="Sentry.io",
    )
chloe.add_personal(
    bio="Former musical theatre actress and Hackbright Academy graduate, Chloe is now a Developer Evangelist at Sentry. Pre-Hackbright, she spent her nights and weekends performing in the Bay Area as a singer/actress and worked in tech by day. To support her theatre career, she started to learn to code on her own through online resources. Perhaps the only engineer you'll meet who has been in 'Hairspray', 'Xanadu', and 'Jerry Springer: the Opera'- she is passionate about bringing people with non-traditional backgrounds into the world of tech. If you're trying to place her face, yes- she's the young woman giving the awkward thumbs up in the 'What It's Like to be a Woman at a Tech Conference' article (which she also wrote). A quick Google search of her will provide you with getting started with Docker videos, theatre reviews, tech blogs, and videos of her singing- enjoy!",
    pronoun="She/Her",
    photo="static/imgs/speakers/chloe.png",
    )
chloe.add_talk(
    title="Logging, and Errors, and Metrics- oh my!",
    description="As engineers, we build pretty cool apps. Once users start using our cool apps... well, we run into the fun process of discovering errors. Keeping track of these issues can get messy, getting alerted is stressful, and measuring it can provide you with an overwhelming amount of information. So, how do we combine all these things to make our cool apps work even better than before? In this talk, we'll dive into logging, errors, and metrics.",
    track_name="Blue Area",
    time="3:00pm",
    date=date,
    category="Technology",
    )


################################################################################

laura = Speaker(
    first_name="Laura",
    last_name= "Montoya",
    )
laura.add_social_media(
    twitter="QuickResolute",
    linkedin="https://www.linkedin.com/in/lnmontoya/",
    website="https://www.lauranmontoya.com/",
    youtube=None,
    facebook="https://www.facebook.com/laura.montoya.biz",
    google_plus=None,
    )
laura.add_professional_information(
    profession="Founder & CEO",
    empolyeer="Accel.AI",
    )
laura.add_personal(
    bio="Laura is the Founder and Executive Director of Accel.AI, a global Non Profit Institute lowering the barriers to entry in engineering artificial intelligence. She has been described as a natural and versatile leader with a passion for AI, Computer Science, Research, and Psychology. She has a Bachelors of Science in Biology, Physical Science, and Human Development. She jumpstarted her career in software engineering at Intuit revamping their Quickbooks online platform, after completing an intensive bootcamp training program. She is a Director with Women Who Code, a global non-profit dedicated to inspiring women to excel in technology careers. A founder and co-Chair of the Latinx in AI Coalition, and she also founded and maintains a community forum, TechLore, which focuses on literature that addresses empowerment, entrepreneurship, culture, social justice, and inclusion through the lens of technology.",
    pronoun="She",
    photo="static/imgs/speakers/laura.jpg",
    )
laura.add_talk(
    title="New Realities of an Augmented Workforce",
    description="We are creating a new augmented workforce -  through increased connectivity and alternative realities thanks to AR and VR  magnified by the fourth wave of an industrial revolution led by digitization, big data, internet of things and cognification of everything. In this talk, we'll explore these exponential technological advances by answering the question - What are the new realities of this augmented workforce? We'll wrap up by empowering listeners with strategies they and their companies can implore for a cohesive and sustainable future.",
    track_name="Green Area",
    time="10:00am",
    date=date,
    category="Technology",
    )


################################################################################


audrey = Speaker(
    first_name="Audrey",
    last_name="Chaing",
    )
audrey.add_social_media(
    twitter="audsinthecity",
    linkedin="https://www.linkedin.com/in/audreychaing/",
    website="https://www.blockchaing.org",
    youtube=None,
    facebook="https://www.facebook.com/audrey.chilaquiles",
    google_plus=None,
    )
audrey.add_professional_information(
    profession="Cryptocurrency Trader/Blockchain Analyst",
    empolyeer="Blockchaing",
    )
audrey.add_personal(
    bio="Audrey is a cryptocurrency trader and blockchain analyst, and runs the news site blockchaing.org. She has been trading Bitcoin since 2013 and is a member of the Oakland Blockchain Developers and SF Ethereum Developers. She is running the MIT Applied Blockchain Series, helping participants create a demo-able product from an idea. Previously, she co-founded 2 companies in food tech and genetics, through which she participated in Start-Up Chile and Singularity University Global Solutions Program. She has over a decade of experience on Wall Street as an investor, trader, and research analyst at companies like Credit Suisse, Wells Fargo, and BlackRock. Audrey has a degree in Computer Science from MIT with a concentration in Artificial Intelligence, and earned her MBA at the Wharton School of the University of Pennsylvania. She is a frequent speaker at events like Women in Blockchain, Blockchain & Cryptocurrency Meetup, SVIAccelerator InsurTech Blockchain Bootcamp, and CryptoHQ.",
    pronoun="She, her, hers",
    photo="static/imgs/speakers/audrey.png",
    )
audrey.add_talk(
    title="Blockchain and Cryptocurrencies for Fun and Profit",
    description="What is blockchain and why do we care? How to get started trading crypto and how to safeguard your investments? What are the biggest problems and potential opportunities using this technology? All this and more including trends in the industry and examples in self-sovereign identity, financial services, supply chain, and decentralized apps.",
    track_name="Green Area",
    time="11:00am",
    date=date,
    category="Technology",
    )

################################################################################


meredith = Speaker(
    first_name="Meredith",
    last_name="Hassett",
    )
meredith.add_social_media(
    twitter="mlhassett",
    linkedin="https://www.linkedin.com/in/meredith-hassett/",
    website=None,
    youtube=None,
    facebook=None,
    google_plus=None,
    )
meredith.add_professional_information(
    profession="Developer Evangelist",
    empolyeer="SAP",
    )
meredith.add_personal(
    bio="Meredith is a Developer Evangelist for SAP sharing her knowledge in front-end development, UI design, and IoT. Originally from the Philadelphia Area, she attended the University of Virginia where she got a BS in Computer Engineering. Meredith has worked on applications for financial institutions, non-profits, and travel groups. She is a FIRST Robotics alumni and has worked on integrated technology solutions in designing novelty products. Meredith currently works out of San Francisco and spends her days finding new ways to blend her other passions with technology.",
    pronoun="She",
    photo="static/imgs/speakers/meredith.png",
    )
meredith.add_talk(
    title="Try your hand at Design Thinking",
    description="Design Thinking is one of the newest brainstorming techniques that allows you to solve the right problem the first time. How many times have you built an app for your users that isn't quite right and leads to a costly redesign? In software development, maintenance is the costliest part of the cycle. Design thinking enables you to build the right solution for your users to help reduce that cost. Join me as we use design thinking to solve a real problem in this 45-minute session!",
    track_name="Blue Area",
    time="11:00am",
    date=date,
    category="Technology",
    )

################################################################################


sarah = Speaker(
    first_name="Sarah",
    last_name="Lohmeier",
    )
sarah.add_social_media(
    twitter="slohmes",
    linkedin="http://linkedin.com/in/sarahlohmeier",
    website="https://slohmes.wordpress.com/",
    youtube=None,
    facebook=None,
    google_plus=None,
    )
sarah.add_professional_information(
    profession="Software Developer",
    empolyeer="ThoughtWorks",
    )
sarah.add_personal(
    bio="Full-stack engineer and systems enthusiast who delights in good naming, constant learning, and empathy.",
    pronoun="she/her",
    photo="static/imgs/speakers/sarah.jpg",
    )
sarah.add_talk(
    title="A Tour of the JS Ecosystem",
    description="Module bundlers! Package managers! Superscripts! Polyfills! Frameworks galore! There are a multitude of JavaScript-based frameworks and tools that make up the 'JS ecosystem' underpinning modern front-end development. This talk is a guided journey through this exciting, but sometimes overwhelming, landscape. By breaking down the elements of a modern front-end tech stack, calling out the problems they're trying to solve, and giving examples of commonly used libraries, this talk will help front-end enthusiasts of all levels gain a better understanding of what the JS ecosystem is and how it has evolved.",
    track_name="Blue Area",
    time="10:00am",
    date=date,
    category="Technology",
    )

################################################################################


shruti = Speaker(
    first_name="Shruti",
    last_name="Sharma",
    )
shruti.add_social_media(
    twitter="curioushruti",
    linkedin="https://www.linkedin.com/in/shruti-sharma-4214b538/",
    website=None,
    youtube=None,
    facebook=None,
    google_plus=None,
    )
shruti.add_professional_information(
    profession="Machine Learning Engineer",
    empolyeer="VSCO",
    )
shruti.add_personal(
    bio="Shruti Sharma is a Machine Learning Engineer at VSCO (www.vsco.co) where she trains deep learning models and builds APIs to use these models in VSCO's products. Previously, she worked on building image processing tools at VSCO. She holds a Masters degree from University of Southern California with a focus on image processing and computer vision. She enjoys keeping up with the fascinating advances in the field of machine learning and is excited about where the field is headed. She's passionate about supporting and mentoring women and other minorities who are looking to enter the field of technology.",
    pronoun="She/Her",
    photo="static/imgs/speakers/shruti.jpg",
    )
shruti.add_talk(
    title="Deep Convolutional Neural Networks using TensorFlow and TensorFlow Serving",
    description="TensorFlow is a powerful open-source library from Google for machine intelligence. It is used by researchers, engineers, students, and others. It has been key in the democratization of deep learning across multiple domains. In this talk, Shruti will walk through the process of training an image classification model using TensorFlow in Keras, and then using TensorFlow Serving to serve the model and run prediction on images. After building your own application, Shruti will show how this looks in a real production environment - how the Machine Learning team at VSCO leverages TensorFlow and TensorFlow Serving for real-time image classification.",
    track_name="Green Area",
    time="2:00pm",
    date=date,
    category="Technology",
    )

################################################################################


deborah = Speaker(
    first_name="Deborah",
    last_name="Raji",
    )
deborah.add_social_media(
    twitter="hashtag_include",
    linkedin="https://www.linkedin.com/in/deborah-raji-065751b2/",
    website=None,
    youtube=None,
    facebook="https://www.facebook.com/projectincludeskule/",
    google_plus=None,
    )
deborah.add_professional_information(
    profession="Machine Learning Engineer Intern",
    empolyeer="Clarifai",
    )
deborah.add_personal(
    bio="Deborah Raji is the founder and former Executive Director of Project Include, a youth-led organization that teaches computer programming in the libraries and community centers of city-designated low income communities. Over just two summers, the program has run seven week coding bootcamps for a total of just under 500 student participants aged 10 to 18, including a handful of adult and family workshops. Mainly operating in Toronto, Ontario in Canada, the group competed its first international mission last summer, reaching 350 students in Quito, Ecuador. Deb is a proud Canadian studying Robotics Engineering at the University of Toronto, currently taking  year off to intern at Clarifai, a computer vision startup in New York City. In her spare time, she volunteers with Joy Buolamwini of the MIT Lab, as part of the Algorithmic Justice League. ",
    pronoun="Her",
    photo="static/imgs/speakers/deborah.jpg",
    )
deborah.add_talk(
    title="Doomed to Repeat It: Exploring Machine Bias in Computer Vision",
    description="In the case of machine learning, when we do learn from history, we're doomed to repeat it. What do you get when you Google simple concepts like 'hand', 'foot' or 'healthy face'? Well, not a lot of diversity. However, we continue to use such biased media-influenced image datasets to feed the machine learning models that do everything from opening our phone and identifying criminals to recommending makeup.  In this session, I plan to walk through an overview of how computer vision models are created, and why each step of the way is an opportunity to introduce bias that could skew results to favour only some segments of the population. I'll also go over the great work being done at Clarifai and the Algorithmic Justice League to combat machine bias and some strategies being developed to support companies and research groups looking to be more mindful about the ML models they create.",
    track_name="Green Area",
    time="12:00pm",
    date=date,
    category="Technology",
    )
################################################################################


dobs = Speaker(
    first_name="Alexandra (Dobs)",
    last_name="Dobkin",
    )
dobs.add_social_media(
    twitter=None,
    linkedin="https://www.linkedin.com/in/alexandradobkin/",
    website="http://www.alexandradobkin.com/",
    youtube=None,
    facebook=None,
    google_plus=None,
    )
dobs.add_professional_information(
    profession="Software Engineer",
    empolyeer="Bloomberg LP",
    )
dobs.add_personal(
    bio="Alexandra Dobkin (Dobs) is currently a software engineer at Bloomberg LP in the San Francisco office (complete with a tank containing stingrays and a shark!).  At work, Dobs exclusively programs in JavaScript.  In order to become a software engineer, she attended Hackbright Academy's full-time bootcamp, an all-women full-stack web development program.  She had a phenomenal experience with Hackbright and currently serves as a Hackbright Ambassador.  Previously, she held careers in management consulting as well as in finance.  She studied Mathematical Methods in the Social Sciences, Economics, and Anthropology at Northwestern University (go cats!).  Dobs enjoys having an interdisciplinary perspective, and is proud of her non-traditional background.  When not coding, she can be found doing Pilates, decorating her apartment, or attending modern art museums.",
    pronoun="she/ her/ hers",
    photo="static/imgs/speakers/dobs.jpg",
    )
dobs.add_talk(
    title="I Promise Fun with Asynchronicity - JavaScript Promises ",
    description="We'll explore JavaScript Promises -- what are  Promises, why/why they should be used, and how they differ from callbacks.  We'll construct a Promise together, as well as look at code snippets that make use of popular 'thenables' in the ubiquitous Bluebird Promises library.  I'll highlight common pitfalls and confusions, and close out with what's next in JavaScript for asynchronous calls.",
    track_name="Yellow Area",
    time="11:00am",
    date=date,
    category="Technology",
    )

################################################################################


wendy = Speaker(
    first_name="Wendy",
    last_name="Saccuzzo",
    )
wendy.add_social_media(
    twitter="aboutworkstuff",
    linkedin="https://www.linkedin.com/in/wendysaccuzzo/",
    website="https://www.aboutworkstuff.com",
    youtube=None,
    facebook=None,
    google_plus=None,
    )
wendy.add_professional_information(
    profession="Career Strategist",
    empolyeer="Career & Personal Development Institute",
    )
wendy.add_personal(
    bio="Wendy Saccuzzo is a career strategist who has worked with over 1,100 women in tech on their career transition, and in a recruiting capacity has helped to build engineering teams in early stage startup companies.  She's involved with Women Who Code and Empowered Tech, and holds a Masters degree in Counseling with a focus on Career Development. Outside of work, Wendy is wrangling her kids, gardening, cooking or hiking.",
    pronoun="She/Her",
    photo="static/imgs/speakers/wendy.jpg",
    )
wendy.add_talk(
    title="Building Your Career Roadmap",
    description="Life takes us on all kinds of twists and turns, and it's a good idea to check in with yourself and think about what you need to survive and thrive in your career.  In this exercise, you'll create a map of where you've been, what you've learned, what you're good at, and what you want to avoid to get closer to your dream job.",
    track_name="Blue Area",
    time="12:00pm",
    date=date,
    category="Professional",
    )

################################################################################


kristi = Speaker(
    first_name="Kristi",
    last_name="Krulcik",
    )
kristi.add_social_media(
    twitter=None,
    linkedin=None,
    website=None,
    youtube=None,
    facebook=None,
    google_plus=None,
    )
kristi.add_professional_information(
    profession="Marketing",
    empolyeer="Google",
    )
kristi.add_personal(
    bio="Kristi Krulcik is currently a product marketer at Google, where her love of asking questions, gathering insights, and creating an intuitive customer experience can thrive. Prior to Google, Kristi worked at Apple, created content for a startup incubator, and launched a radio station. She is passionate about helping women feel confident in their professional skills and loves learning from others. On the weekends, you can find her biking around the Presidio and exploring new San Francisco neighborhoods.",
    pronoun="she/her",
    photo="static/imgs/speakers/kristi.jpg",
    )
kristi.add_talk(
    title="Networking for Those Who Hate Networking Events",
    description="We've all been there: a networking event pops up that seems like a 'good idea' for your career. Why? Because everyone tells us to network, network, network! Go to those events! Practice that elevator speech! Know how to mingle and stand out and dress appropriately and follow up un-annoyingly and get your next dream job from that one person you met that one time! But who said another awkward, uncomfortable networking event is the only solution? Thankfully, there are better ways to make connections. So let's explore them, and find what works best for you.",
    track_name="Blue Area",
    time="2:00pm",
    date=date,
    category="Professional",
    )

################################################################################


irana = Speaker(
    first_name="Irana",
    last_name="Wasti",
    )
irana.add_social_media(
    twitter="IranaWasti",
    linkedin="https://www.linkedin.com/in/irana-wasti-40970b3/",
    website=None,
    youtube=None,
    facebook="https://www.facebook.com/irana.wasti",
    google_plus=None,
    )
irana.add_professional_information(
    profession="SVP of Productivity",
    empolyeer="GoDaddy",
    )
irana.add_personal(
    bio="As SVP and General Manager for GoDaddy's Productivity business, Irana leads teams that provide small businesses with tools and services that help them improve communication and run their businesses.",
    pronoun="female: she, her etc.",
    photo="static/imgs/speakers/irana.jpg",
    )
irana.add_talk(
    title="Mindful (and creative) Work-Life Integration",
    description="There is no such thing as work-life balance. Every day, either work or family requires just a little bit more attention than the other. Irana can discuss how she uses her 'guiding principles' as a north star to pursue both career and family goals in what we call work-life integration. She can share about her experience at Harvard Business School, where her and her husband attended at the same time and were the first couple to be pregnant and have a child while attending HBS. She set an example and worked with the school to help improve policies for women and families to come. Although Irana is now a top executive at GoDaddy, she still is able to prioritize time with her family and can share tips on how she accomplishes that integration.",
    track_name="Yellow Area",
    time="3:00pm",
    date=date,
    category="Professional",
    )

################################################################################


maytal = Speaker(
    first_name="Maytal",
    last_name="Dahan",
    )
maytal.add_social_media(
    twitter="maytaldahan",
    linkedin="https://www.linkedin.com/in/maytaldahan",
    website="https://www.tacc.utexas.edu/about/directory/maytal-dahan",
    youtube=None,
    facebook=None,
    google_plus=None,
    )
maytal.add_professional_information(
    profession="Director/Software Engineer",
    empolyeer="Texas Advanced Computing Center, The University of Texas at Austin",
    )
maytal.add_personal(
    bio="Maytal Dahan has been telecommuting for fifteen years and is a software engineer and Director of the Advanced Computing Interfaces Department at the Texas Advanced Computing Center (TACC) at The University of Texas at Austin. Maytal has a B.S in Computer Science from The University of California, San Diego and a M.S in Software Engineering from The University of Texas at Austin. Maytal first started telecommuting for the San Diego Supercomputer Center as a software developer. Next, Maytal joined TACC in August 2002 as a Software Developer working remotely full-time from Los Angeles. She is involved in several software projects that interfaces, software, and services web portal applications. Maytal is the project lead for the User Information and interfaces in a national cyberinfrastructure project known as XSEDE. Maytal has been a Co-Principal Investigator on multiple NSF Funded projects and is currently a Co-Principal Investigator on the Science Gateways Collaborative Institute, a fifteen million dollar NSF funded project to promote and engage Science Gateways. While telecommuting for TACC full time she has risen through the ranks at TACC. Starting as a developer and individual contributor to projects Maytal has grown to lead multiple projects as a technical lead. Now, Maytal serves the director of her department and a lead for multiple projects. Maytal is passionate about enabling science through the use of technology such as Science Gateways to make science more accessible. Maytal has also spoken at multiple conferences including Grace Hopper and SXSW Interactive and giving technical talks, leading Birds of a Feather sessions, and conducting panels and meet-ups.",
    pronoun="she/her/hers",
    photo="static/imgs/speakers/maytal.jpg",
    )
maytal.add_talk(
    title="Pants Not Required: Telecommuting Like A Boss",
    description="Interested in becoming a successful telecommuter? Telecommuting now and want strategies to succeed? This session will teach you strategies for how to pitch telecommuting to your boss, ideas on being more productive, and making sure that you are just as seen and heard as an employee in the office. How can I be a productive telecommuter and prove it to my boss? What are the common pitfalls and misconceptions of telecommuting and how can I avoid and combat them? Learn how to be a remote employee that rocks and techniques for how to effectively manage people and projects remotely.",
    track_name="Yellow Area",
    time="4:00pm",
    date=date,
    category="Professional",
    )

################################################################################

vr = Talk(
        title="Google VR Panel",
        description="Hear from three women who work in the DayDream (VR) team. They'll share what they do, what they are excited to be working on and a Q&A where you can ask questions to them.",
        track_name="Green Area",
        time="3:00pm",
        speaker=None,
        date=date,
        category="Technology",
    )

vr.workaroundid = True

brit = Speaker(
    first_name="Brittany",
    last_name="Mennuti",
    )
brit.add_social_media(
    twitter=None,
    linkedin=None,
    website=None,
    youtube=None,
    facebook=None,
    google_plus=None,
    )
brit.add_professional_information(
    profession="Product Manager, VR",
    empolyeer="Google",
    )
brit.add_personal(
    bio="Brittany is a Product Manager VR",
    pronoun=None,
    photo="static/imgs/speakers/brit.jpg",
    )
brit.talk = vr

###
joanna = Speaker(
    first_name="Joanna",
    last_name="s",
    )
joanna.add_social_media(
    twitter=None,
    linkedin=None,
    website=None,
    youtube=None,
    facebook=None,
    google_plus=None,
    )
joanna.add_professional_information(
    profession="Product Manager, VR",
    empolyeer="Google",
    )
joanna.add_personal(
    bio=None,
    pronoun=None,
    photo="static/imgs/speakers/3.png",
    )
joanna.talk = vr

###

ali = Speaker(
    first_name="Ali",
    last_name="d",
    )
ali.add_social_media(
    twitter=None,
    linkedin=None,
    website=None,
    youtube=None,
    facebook=None,
    google_plus=None,
    )
ali.add_professional_information(
    profession="Product Manager, VR",
    empolyeer="Google",
    )
ali.add_personal(
    bio=None,
    pronoun=None,
    photo="static/imgs/speakers/2.png",
    )
ali.talk = vr


vr.speakers = [brit,
                # joanna,
                # ali,
            ]

################################################################################
###############Add Speaker objects to Speakers List#############################
################################################################################
speakers_data = [
    laura,
    audrey,
    meredith,
    dobs,
    shruti,
    sarah,
    chloe,
    deborah,
    wendy,
    kristi,
    irana,
    maytal,
    brit,
    # joanna,
    # ali,
    ]


################################################################################
# Below creates the talks, ordered_of_sessions and schedule_color              #
################################################################################
talks = {}

missing_data_talks = []

order_of_sessions = {}

for num in range(len(session_times)):
    order_of_sessions[session_times[num]] = num

for name in track_names:
    talks[name] = {}
    for time in session_times:
        talks[name] = range(len(session_times))


colors = ["blue-op", "green-op"]
color_num = 0

for speaker in speakers_data:
    if color_num > 1:
        color_num = 0
    speaker.talk.color = colors[color_num]
    color_num += 1
    if speaker.talk.slot.get("track_name") is None:
        missing_data_talks.append(speaker.talk)
        continue
    # talks[speaker.talk.slot.get("track_name")][order_of_sessions[speaker.talk.slot.get("time")]] = speaker.talk
if color_num:
    vr.color = colors[0]
else:
    vr.color = colors[1]

colors = ["blue", "green", "dark-green", "dark-blue"]

schedule_color = {}

counter = 0
for track in track_names:
    if counter > 3:
        counter -= 4
    schedule_color[track] = colors[counter]
    counter += 1

non_talks = [registration, welcome, lunch, closing, networking]


for n_talk in non_talks:
    talks[n_talk.slot.get("track_name")][order_of_sessions[n_talk.slot.get("time")]] = n_talk

################################################################################


def selects_four_random_speakers(speakers_data):
    """Returns four random speakers"""

    random_nums = []

    random_nums.append(choice([0, 1, 4, 7]))

    for num in range(3):
        random_num = randint(0, (len(speakers_data) - 1))
        print random_num
        while random_num in random_nums:
            random_num = randint(0, (len(speakers_data) - 1))
        random_nums.append(random_num)
    random_speakers = [speakers_data[random_nums[2]], speakers_data[random_nums[1]], speakers_data[random_nums[0]], speakers_data[random_nums[3]]]

    return random_speakers

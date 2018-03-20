# -*- coding: utf-8 -*-
###Above is to find the system's source code encoding
from model import Speaker, Talk
from random import randint, choice



################################################################################
# Add your track names (it can be as little as 1 to as many as 6)              #
################################################################################
track_names = [
            "Blue Area",
            "Yellow Area",
            "Green Area",
            "Purple Area"
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

registration = Talk("Registration & Breakfast", "Get your name badge, swag and enjoy a light breakfast", time="8:30am", track_name="Blue Area")
welcome = Talk("Welcome", "We'll come together to kick off the day", time="9:30am", track_name="Blue Area")
lunch = Talk("Lunch", "Delicious Food and Connecting with others", time="1:00pm", track_name="Blue Area")
closing = Talk("Closing & Raffle", "Join us on wrapping up the day with a raffle and thank yous", time="5:00pm", track_name="Blue Area")
networking = Talk("Networking", "Connect with people and exchange contact info! Doors close at 6:30pm", time="5:30pm", track_name="Blue Area")

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
    track_name="Purple Area",
    time="2:00pm",
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
    track_name="Yellow Area",
    time="11:00am",
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
    track_name="Yellow Area",
    time="10:00am",
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
    track_name="Green Area",
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
    track_name="Purple Area",
    time="11:00am",
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
    track_name="Yellow Area",
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
    track_name="Yellow Area",
    time="3:00pm",
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
    track_name="Purple Area",
    time="12:00pm",
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
    description="What's your purpose in your career?  What are you good at, and what motivates you?  You may be thinking about skills you need to develop to move into a leadership role in the future, or how to be a better communicator.  In this career road mapping exercise, we'll reflect on what you need to not only survive but thrive in your career, by identifying strengths, skills, values, and goals to take your career to the next level.",
    track_name="Green Area",
    time="2:00pm",
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
    track_name="Purple Area",
    time="10:00am",
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
    track_name="Green Area",
    time="12:00pm",
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
    track_name="Green Area",
    time="4:00pm",
    date=date,
    category="Professional",
    )

################################################################################

sarah_h = Speaker(
    first_name="Sarah",
    last_name="Harvey",
    )
sarah_h.add_social_media(
    twitter="worldwise001",
    linkedin="https://www.linkedin.com/in/shharvey/",
    website="https://www.shh.sh",
    youtube=None,
    facebook=None,
    google_plus=None,
    )
sarah_h.add_professional_information(
    profession="Software Engineer - Security",
    empolyeer="Square Inc",
    )
sarah_h.add_personal(
    bio="Sarah is a software engineer at Square, broadly working on designing and engineering solutions to security infrastructure and security data problems. She has a strong interest in data security/privacy problems. She has given a few talks on security/privacy in the past, including running a highly popular CTF workshop at Grace Hopper 2017.",
    pronoun="she/her/hers",
    photo="static/imgs/speakers/sarah-h.jpg",
    )
sarah_h.add_talk(
    title="The (Security-Centric) Woman's Guide to the Galaxy",
    description="DON'T PANIC. Being a woman on the internet can be scary. Being a famous woman on the internet can be dangerous. In between threats of doxxing and major breaches, how can we safely navigate the increasingly interconnected world without fear? In this talk we discuss why security/privacy is important in the modern age, in addition to: how your data gets shared; how to curtail the spread of personal data; how to secure your accounts; and how to perform a threat modeling exercise for hackers interested in you and your data.",
    track_name="Green Area",
    time="3:00pm",
    date=date,
    category="Professional",
    )

################################################################################


monisha = Speaker(
    first_name="Monisha",
    last_name="Edwards",
    )
monisha.add_social_media(
    twitter="monishaedwards",
    linkedin="https://www.linkedin.com/in/monishaedwards/",
    website="https://www.monishaedwards.com/",
    youtube=None,
    facebook="https://www.facebook.com/iammonishaedwards",
    google_plus=None,
    )
monisha.add_professional_information(
    profession="Founder and Creative Strategist",
    empolyeer="Truth Branding Agency",
    )
monisha.add_personal(
    bio="Monisha Edwards is a Creative Strategist, specializing in Branding, User Interface, and User Experience. She received her Bachelors of Science in Marketing from Fresno State University. Monisha started her first company while in college at the tender age of 19 to help her pay for tuition. Monisha was accepted into an exclusive entrepreneurship program at Fresno State University, where she received mentorship, an office space, and other resources to help her grow her first business. She then ventured off into Corporate America as a Marketing Manager for an engineering firm, and is now the founder and Brand Strategist for Truth Branding Agency. She is also the founder of Literacy Fresno, a literacy and literature exchange initiative. Monisha is an active servant of the community, especially Downtown Fresno, and is currently enrolled in Leadership Fresno, a program for community leaders to learn more about their city to improve their surroundings. Monisha entered the world of technology when she quickly discovered that it was her passion. She is a self-taught graphic, web designer, and front-end developer. Monisha has been a featured speaker for Google's Start Up Grind and has been featured in several publications including the Business Journal.",
    pronoun="she",
    photo="static/imgs/speakers/monisha.jpg",
    )
monisha.add_talk(
    title="How to Conquer as a UI/UX Designer ",
    description="Being a woman in the field of technology is hard. It's a male dominated industry. Being a woman UI/UX designer is sometimes even harder. It is important for women to set themselves apart from the stigmas of being a woman in field of design. As a brand strategist, I will give some insight and tips on how women designers can succeed as designers in the world of technology. These tips will include how to brand yourself as a kicka** UI/UX designer, how to put together a killer portfolio, and even how to cultivate resources to help with personal and professional development.",
    track_name="Green Area",
    time="10:00am",
    date=date,
    category="Professional",
    )

################################################################################


jessica = Speaker(
    first_name="Jessica",
    last_name="Parsons",
    )
jessica.add_social_media(
    twitter="verythorough",
    linkedin="https://www.linkedin.com/in/verythorough/",
    website="https://www.verythorough.com",
    youtube=None,
    facebook=None,
    google_plus=None,
    )
jessica.add_professional_information(
    profession="Documentation Engineer",
    empolyeer="Netlify",
    )
jessica.add_personal(
    bio="Jessica Parsons has spent half her life teaching, and a quarter of it developing for the web. She now combines those passions as a documentation engineer at Netlify and a teacher for Girl Develop It. Away from a computer screen, she enjoys sewing, fixing things, and enjoying the outdoors with her shiba inus.",
    pronoun="she/her",
    photo="static/imgs/speakers/jessica.jpg",
    )
jessica.add_talk(
    title="Buying the Hype: Understanding and Negotiating Stock Offers",
    description="Companies often justify lower salaries with promises of huge stock returns, but the laws and options are complex, and values are difficult to evaluate against an uncertain future. How do you evaluate the potential and comparability of the offer you've received? What options do you have for negotiating an offer to your advantage, and how can you make the most of it? I'll help you wade through the sea of terms, options, and outcomes so you'll feel prepared to make these choices for yourself when you receive your next equity offer, or in leveraging options you already have.",
    track_name="Purple Area",
    time="3:00pm",
    date=date,
    category="Professional",
    )

################################################################################


mary = Speaker(
    first_name="Mary",
    last_name="Fox",
    )
mary.add_social_media(
    twitter="maryfox20",
    linkedin="https://linkedin.com/in/marybfox",
    website="https://getmarlow.com",
    youtube=None,
    facebook="https://www.facebook.com/maryfox20",
    google_plus=None,
    )
mary.add_professional_information(
    profession="Founder / CEO ",
    empolyeer="Marlow",
    )
mary.add_personal(
    bio="Mary Fox is the co-founder and CEO of Marlow, a career management platform offering executive style career coaching via chat. Prior to launching Marlow, Mary served as the Head of Product Marketing and People Operations at FR8Star. With more than 8 years of experience in people operations, employee engagement, recruitment, and business operations, Mary has dedicated her career to helping individuals and companies make progress toward their goals more quickly and effectively. Mary holds a Master's of Science in Management, Organisations and Governance from the London School of Economics and Political Science.",
    pronoun="She / Her ",
    photo="static/imgs/speakers/mary.jpg",
    )
mary.add_talk(
    title="Feedback: the secret weapon to springboard your career",
    description="Well structured feedback helps build stronger professional relationships, enhances productivity of your team, demonstrates leadership potential and can create a culture of trust. When we ask for feedback, we demonstrate a desire to grow while gaining a better perception of how others perceive our actions. When we provide well-structured feedback to those around us, we enable them to grow while also enhancing the productivity of the team. This talk walks you through how to use feedback as a resource to shape your personal growth, work environment, and work relationships. ",
    track_name="Yellow Area",
    time="4:00pm",
    date=date,
    category="Professional",
    )

################################################################################


lauren = Speaker(
    first_name="Lauren",
    last_name="Werner",
    )
lauren.add_social_media(
    twitter="LPdub",
    linkedin="https://www.linkedin.com/in/lwerner/",
    website="https://laurenwerner.com/",
    youtube=None,
    facebook=None,
    google_plus=None,
    )
lauren.add_professional_information(
    profession="UX Designer",
    empolyeer="BlinkUX",
    )
lauren.add_personal(
    bio="As Senior UX Designer at Blink, Lauren is able to seamlessly translate business objectives into imaginative visual concepts. She anticipates client needs based on in-depth understanding of business goals, collaborating to create the best user experience. Lauren is deeply involved in every aspect of the design process including research, strategy, design and development. She works closely with the team to implement best practices and latest trends in UX and design. Lauren has a Bachelor's Degree in Graphic Design as well as a Minor in Business from Northeastern University. With her extensive consulting background in design and business Lauren is an amazing collaborator and is always excited to create strategic and engaging experiences. Lauren is a design geek, and tapas enthusiast. She enjoys making applications and websites that are both functional and beautiful.",
    pronoun="She",
    photo="static/imgs/speakers/lauren.jpg",
    )
lauren.add_talk(
    title="Defining Your Minimum Viable Testing (MVT) ",
    description="""Making assumptions can be the downfall of many a marketer. 
Think about it: how often have you conducted user research without actually talking to real people?
All too often we use data to infer what users want without ever asking them firsthand. According to Forrester Research's 2015 Customer Experience Index, 73 percent of businesses cite customer experience as a strategic priority, yet only 1 percent of companies deliver excellent customer experiences.
This session will equip you with the tools you need to understand your customers and make smarter product decisions though a Minimum Viable Testing (MVT) approach. With a defined MVT you can ensure that you are designing the best possible experience for your users.
In this session you will learn how to:
* Myth-bust the idea that research is expensive & delays product development
* Evaluate and choose the right research method for your project based on where you are in the product lifecycle
* Define research objectives as well as choose the right audience and tools
* Plan user research on a budget
* Collaborate with your core team to organize findings into themes and create actionable insights
* Effectively communicate research findings and priorities to stakeholders""",
    track_name="Purple Area",
    time="4:00pm",
    date=date,
    category="Technology",
    )

################################################################################


girls_who_code = Speaker(
    first_name="Girls Who",
    last_name="Code",
    )
girls_who_code.add_social_media(
    twitter=None,
    linkedin=None,
    website="https://girlswhocode.com/",
    youtube=None,
    facebook=None,
    google_plus=None,
    )
girls_who_code.add_professional_information(
    profession="",
    empolyeer="",
    )
girls_who_code.add_personal(
    bio="Girls Who Code was founded with a single mission: to close the gender gap in technology",
    pronoun=None,
    photo="static/imgs/sponsor/gwc.png",
    )
girls_who_code.add_talk(
    title="Youth: Building Apps with MIT AppInventor and Design Thinking",
    description="In this this hands-on workshop, we will use MIT AppInventor, a visual programming tool, to build smartphone and tablet apps. We will cover everything from tinkering with sound and text, to designing characters and movements. Participants will walk away with working prototypes of their apps! We will also cover design thinking, a creative framework that teaches participants to ideate empathetically, think fiercely, and bring their ideas to life. We will practice brainstorming, prototyping, and exchanging feedback with the class. This fun and creative workshop will inspire participants of all skill levels.",
    track_name="Blue Area",
    time="2:00pm",
    date=date,
    category="Youth",
    )


###
girls_who_code_2 = Speaker(
    first_name="Girls Who",
    last_name="Code",
    )
girls_who_code_2.add_social_media(
    twitter=None,
    linkedin=None,
    website="https://girlswhocode.com/book/the-friendship-code/?gclid=CjwKCAiAz-7UBRBAEiwAVrz-9cK-fWZHuwik35UrscUeGKDG3V1ch9fQ9jr7LgisSDv3d22LCUzDHRoClJcQAvD_BwE",
    youtube=None,
    facebook=None,
    google_plus=None,
    )
girls_who_code_2.add_professional_information(
    profession="",
    empolyeer="",
    )
girls_who_code_2.add_personal(
    bio="Girls Who Code was founded with a single mission: to close the gender gap in technology",
    pronoun=None,
    photo="static/imgs/sponsor/gwc.png",
    )
girls_who_code_2.add_talk(
    title="Youth: Building Apps with MIT AppInventor and Design Thinking",
    description="In this this hands-on workshop, we will use MIT AppInventor, a visual programming tool, to build smartphone and tablet apps. We will cover everything from tinkering with sound and text, to designing characters and movements. Participants will walk away with working prototypes of their apps! We will also cover design thinking, a creative framework that teaches participants to ideate empathetically, think fiercely, and bring their ideas to life. We will practice brainstorming, prototyping, and exchanging feedback with the class. This fun and creative workshop will inspire participants of all skill levels.",
    track_name="Blue Area",
    time="3:00pm",
    date=date,
    category="Youth",
    )

###
girls_who_code_3 = Speaker(
    first_name="Girls Who",
    last_name="Code",
    )
girls_who_code_3.add_social_media(
    twitter=None,
    linkedin=None,
    website="https://girlswhocode.com/book/the-friendship-code/?gclid=CjwKCAiAz-7UBRBAEiwAVrz-9cK-fWZHuwik35UrscUeGKDG3V1ch9fQ9jr7LgisSDv3d22LCUzDHRoClJcQAvD_BwE",
    youtube=None,
    facebook=None,
    google_plus=None,
    )
girls_who_code_3.add_professional_information(
    profession="",
    empolyeer="",
    )
girls_who_code_3.add_personal(
    bio="Girls Who Code was founded with a single mission: to close the gender gap in technology",
    pronoun=None,
    photo="static/imgs/sponsor/gwc.png",
    )
girls_who_code_3.add_talk(
    title="Youth: Building Apps with MIT AppInventor and Design Thinking",
    description="In this this hands-on workshop, we will use MIT AppInventor, a visual programming tool, to build smartphone and tablet apps. We will cover everything from tinkering with sound and text, to designing characters and movements. Participants will walk away with working prototypes of their apps! We will also cover design thinking, a creative framework that teaches participants to ideate empathetically, think fiercely, and bring their ideas to life. We will practice brainstorming, prototyping, and exchanging feedback with the class. This fun and creative workshop will inspire participants of all skill levels.",
    track_name="Blue Area",
    time="4:00pm",
    date=date,
    category="Youth",
    )

################################################################################

bytes_for_bits = Speaker(
    first_name="Bytes for",
    last_name="Bits",
    )
bytes_for_bits.add_social_media(
    twitter=None,
    linkedin=None,
    website="http://www.bytes4bits.org/",
    youtube=None,
    facebook=None,
    google_plus=None,
    )
bytes_for_bits.add_professional_information(
    profession="",
    empolyeer="",
    )
bytes_for_bits.add_personal(
    bio="Our mission is to: Remove the gender and socioeconomic gap in technology. We inspire, educate, and equip elementary school students with the skills and resources to pursue their interests in coding and technology. Bytes for Bits started with the passion of a few Dads. Wanting to ensure their kids received Computer Science instruction, the Dads set out to create an affordable and attractive after-school program. Focusing on Girls and Under-Privileged students, the ultimate goal is for FREE after-school Computer Science classes to ALL students.",
    pronoun=None,
    photo="static/imgs/sponsor/bytes-for-bits.png",
    )
bytes_for_bits.add_talk(
    title="Youth: Computer Coding Bootcamp",
    description="In this interactive session, participants will dive into the fundamentals of software coding. We will use Scratch, a visual coding tool, and Code Combat, a beginner-friendly introduction of Python. The workshop will begin with base concepts, followed by interactive projects to test participants' new skills and creativity. In this fun and inspirational environment, participants will walk away with the confidence and knowledge to build something on their own! The curriculum is modular, so participants of all skill levels can progress at their own pace with the assistance of our three Bytes for Bit instructors.",
    track_name="Blue Area",
    time="10:00am",
    date=date,
    category="Youth",
    )

###
bytes_for_bits_2 = Speaker(
    first_name="Bytes for",
    last_name="Bits",
    )
bytes_for_bits_2.add_social_media(
    twitter=None,
    linkedin=None,
    website="http://www.bytes4bits.org/",
    youtube=None,
    facebook=None,
    google_plus=None,
    )
bytes_for_bits_2.add_professional_information(
    profession="",
    empolyeer="",
    )
bytes_for_bits_2.add_personal(
    bio="Our mission is to: Remove the gender and socioeconomic gap in technology. We inspire, educate, and equip elementary school students with the skills and resources to pursue their interests in coding and technology. Bytes for Bits started with the passion of a few Dads. Wanting to ensure their kids received Computer Science instruction, the Dads set out to create an affordable and attractive after-school program. Focusing on Girls and Under-Privileged students, the ultimate goal is for FREE after-school Computer Science classes to ALL students.",
    pronoun=None,
    photo="static/imgs/sponsor/bytes-for-bits.png",
    )
bytes_for_bits_2.add_talk(
    title="Youth: Computer Coding Bootcamp",
    description="In this interactive session, participants will dive into the fundamentals of software coding. We will use Scratch, a visual coding tool, and Code Combat, a beginner-friendly introduction of Python. The workshop will begin with base concepts, followed by interactive projects to test participants' new skills and creativity. In this fun and inspirational environment, participants will walk away with the confidence and knowledge to build something on their own! The curriculum is modular, so participants of all skill levels can progress at their own pace with the assistance of our three Bytes for Bit instructors.",
    track_name="Blue Area",
    time="11:00am",
    date=date,
    category="Youth",
    )

###
bytes_for_bits_3 = Speaker(
    first_name="Bytes for",
    last_name="Bits",
    )
bytes_for_bits_3.add_social_media(
    twitter=None,
    linkedin=None,
    website="http://www.bytes4bits.org/",
    youtube=None,
    facebook=None,
    google_plus=None,
    )
bytes_for_bits_3.add_professional_information(
    profession="",
    empolyeer="",
    )
bytes_for_bits_3.add_personal(
    bio="Our mission is to: Remove the gender and socioeconomic gap in technology. We inspire, educate, and equip elementary school students with the skills and resources to pursue their interests in coding and technology. Bytes for Bits started with the passion of a few Dads. Wanting to ensure their kids received Computer Science instruction, the Dads set out to create an affordable and attractive after-school program. Focusing on Girls and Under-Privileged students, the ultimate goal is for FREE after-school Computer Science classes to ALL students.",
    pronoun=None,
    photo="static/imgs/sponsor/bytes-for-bits.png",
    )
bytes_for_bits_3.add_talk(
    title="Youth: Computer Coding Bootcamp",
    description="In this interactive session, participants will dive into the fundamentals of software coding. We will use Scratch, a visual coding tool, and Code Combat, a beginner-friendly introduction of Python. The workshop will begin with base concepts, followed by interactive projects to test participants' new skills and creativity. In this fun and inspirational environment, participants will walk away with the confidence and knowledge to build something on their own! The curriculum is modular, so participants of all skill levels can progress at their own pace with the assistance of our three Bytes for Bit instructors.",
    track_name="Blue Area",
    time="12:00pm",
    date=date,
    category="Youth",
    )

################################################################################

vr = Talk(
        title="Breaking into Emerging Tech",
        description="Three women describe their paths to working in immersive computing at Google and answer your questions about career, professional development, and being female thought leaders in an emerging industry.",
        track_name="Yellow Area",
        time="12:00pm",
        speaker=None,
        date=date,
        category="Professional",
    )

vr.workaroundid = True

brit = Speaker(
    first_name="Brittany",
    last_name="Mennuti",
    )
brit.add_social_media(
    twitter="britmennuti",
    linkedin="https://www.linkedin.com/in/britmennuti/",
    website="https://medium.com/@brittany.mennuti",
    youtube=None,
    facebook=None,
    google_plus=None,
    )
brit.add_professional_information(
    profession="Product Manager, VR",
    empolyeer="Google",
    )
brit.add_personal(
    bio="Brit is a Product Manager on Daydream at Google, where she focuses on building tools to help creative individuals successfully create immersive content. She focuses on building products like Poly, Blocks, and Expeditions. Prior to Google, Brit was a Product Manager at Vine, where she helped to develop creator tools for Vine's community of artists, and a Group Product Manager at Etsy, where she led Ety's Shipping & Order Management team. In her free time she is an avid gardener and dabbles in confectionery experiments.",
    pronoun=None,
    photo="static/imgs/speakers/brit.jpg",
    )
brit.talk = vr


###
alexandra = Speaker(
    first_name="Alexandra",
    last_name="Sofen",
    )
alexandra.add_social_media(
    twitter="alisofine",
    linkedin="https://www.linkedin.com/in/alexandra-sofen-3775a062/",
    website=None,
    youtube=None,
    facebook=None,
    google_plus=None,
    )
alexandra.add_professional_information(
    profession="Program Manager",
    empolyeer="Google",
    )
alexandra.add_personal(
    bio="Alexandra Sofen is a Program Manager on the Daydream team at Google, focusing on developing and scaling immersive virtual reality and augmented reality experiences and apps such as Blocks and Poly. She is based in New York City and before working at Google, she was a Senior Programming Manager at Etsy acting as a liaison between Etsy's community of 27 million users and staff of over 800 employees. She constantly strives to foster development and retention with the products she manages, bringing communities together through online engagement and in-person events while scaling user bases.",
    pronoun=None,
    photo="static/imgs/speakers/alexandra.jpg",
    )
alexandra.talk = vr

###

kelly = Speaker(
    first_name="Kelly",
    last_name="Schaefer",
    )
kelly.add_social_media(
    twitter="@kellyschaefer",
    linkedin="https://www.linkedin.com/in/schaeferkelly/",
    website=None,
    youtube=None,
    facebook=None,
    google_plus=None,
    )
kelly.add_professional_information(
    profession="Product Manager, VR",
    empolyeer="Google",
    )
kelly.add_personal(
    bio="Kelly Schaefer is a Product Manager with the Lens & Daydream teams at Google, focusing on augmented reality. Prior to working at Google, she was a Design Lead at IDEO, where she did everything from prototype a virtual reality physical therapy experience to launch a company that helps the working poor improve access to job opportunities. Kelly has also worked at African Leadership Academy, Bain & Company, and started two companies. She graduated from UPenn and Harvard Business School. ",
    pronoun=None,
    photo="static/imgs/speakers/kelly.jpg",
    )
kelly.talk = vr


vr.speakers = [ brit,
                alexandra,
                kelly,
            ]

################################################################################
###############Add Speaker objects to Speakers List#############################
################################################################################
speakers_data = [
    laura,
    audrey,
    meredith,
    monisha,
    dobs,
    jessica,
    shruti,
    sarah_h,
    mary,
    sarah,
    deborah,
    chloe,
    wendy,
    kristi,
    lauren,
    irana,
    maytal,
    brit,
    alexandra,
    kelly,
    girls_who_code,
    bytes_for_bits,
    girls_who_code_2,
    girls_who_code_3,
    bytes_for_bits_2,
    bytes_for_bits_3,
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
    talks[speaker.talk.slot.get("track_name")][order_of_sessions[speaker.talk.slot.get("time")]] = speaker.talk

speakers_data[20].talk.color = colors[1]
speakers_data[21].talk.color = colors[0]

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

    for num in range(2):
        random_num = choice([0, 1, 2, 3, 6, 10])
        print random_num
        while random_num in random_nums:
            random_num = choice([0, 1, 2, 3, 6, 10])
        random_nums.append(random_num)

    for num in range(2):
        random_num = randint(0, (len(speakers_data[:20]) - 1))
        print random_num
        while random_num in random_nums:
            random_num = randint(0, (len(speakers_data[:20]) - 1))
        random_nums.append(random_num)
    random_speakers = [speakers_data[random_nums[2]], speakers_data[random_nums[1]], speakers_data[random_nums[0]], speakers_data[random_nums[3]]]

    return random_speakers

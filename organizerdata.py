# -*- coding: utf-8 -*-
###Above is to find the system's source code encoding
from model import Organizer


################################################################################
# Add your Organizer's Information                                             #
################################################################################

jessica = Organizer(
    first_name="Jessica",
    last_name="Earley-Cha",
    )
jessica.add_social_media(
    twitter="chatasweetie",
    linkedin="https://www.linkedin.com/in/jessicaearley/",
    website="https://chatasweetie.com",
    youtube="https://www.youtube.com/channel/UCmAIHsNUyAzJ6FQMdU5jdRw",
    facebook="https://www.facebook.com/jessica.d.earley",
    google_plus="http://google.com/+JessicaEarleyChatasweetie",
    )
jessica.add_professional_information(
    profession="Software Instructor",
    empolyeer="Girl Develop, It",
    )
jessica.add_personal(
    bio="Jessica Dene Earley-Cha is from Calexico, CA and received her bachelor's in Sociology, Education: Applied Psychology from UCSB. She spent almost a decade working with at-risk youth with mental health challenges in disadvantaged areas. Jessica decided to follow her passion of coding and graduated from a software Boot Camp.  She is full stack developer who enjoys sharing knowledge and support others. Jessica is the co-organizer for Google Developers Group San Francisco, is a Women Techmakers lead, teacher for Girl Develop It, active with  Latinxs in Tech and co-creator of DevelopHerDevelopHim. You'll find her either listening to other's life stories or coding one of her many personal projects.",
    pronoun="she/her",
    photo="https://chatasweetie.files.wordpress.com/2015/10/jessica-short.png?w=300&h=317",
    )
jessica.add_committee_info(
    roles=["Lead Organizer"],
    gdg_name="GDG San Francisco",
    gdg_role="Co-organizer"
    )


################################################################################


james = Organizer(
    first_name="James",
    last_name="Cha-Earley",
    )
james.add_social_media(
    twitter="https://twitter.com/theJamesCha",
    linkedin="https://www.linkedin.com/in/jamesjcha/",
    website=None,
    youtube=None,
    facebook=None,
    google_plus=None,
    )
james.add_professional_information(
    profession="Developer Program Manager",
    empolyeer="Clover",
    )
james.add_personal(
    bio="James is a great person.",
    pronoun="he/him",
    photo="data:image/jpeg;base64,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",
    )
james.add_committee_info(
    roles=["Lead Organizer"],
    gdg_name="GDG San Francisco",
    gdg_role="Co-organizer"
    )

################################################################################


rubi = Organizer(
    first_name="Rubi",
    last_name="Martinez",
    )
rubi.add_social_media(
    twitter=None,
    linkedin=None,
    website=None,
    youtube=None,
    facebook=None,
    google_plus=None,
    )
rubi.add_professional_information(
    profession="Trust and Safety",
    empolyeer="Patreon",
    )
rubi.add_personal(
    bio=None,
    pronoun=None,
    photo=None,
    )
rubi.add_committee_info(
    roles=None,
    gdg_name="",
    gdg_role="",
    )

################################################################################
#         Add Organizer objects to Speakers List                               #
################################################################################
organizers_data = [
    jessica,
    james,
    rubi,
    ]

################################################################################
################################################################################
################################################################################

colors = ["blue", "green", "dark-green", "dark-blue"]

counter = 0
for organizer in organizers_data:
    if counter > 3:
        counter -= 4
    organizer.color = colors[counter]
    counter += 1

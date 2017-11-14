"""Speaker & Talk Classes"""


class Speaker(object):
    """This is a human person"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.talk = None

    def add_social_media(self, twitter=None, linkedin=None, website=None,
                            youtube=None, facebook=None, google_plus=None):
        self.social_media = {
                    "twitter": twitter,
                    "linkedin": linkedin,
                    "website": website,
                    "youtube": youtube,
                    "facebook": facebook,
                    "google_plus": google_plus,
                    }

    def add_professional_information(self, profession=None, empolyeer=None):
        self.professional_info = {
                    "profession": profession,
                    "empolyeer": empolyeer,
                    }

    def add_personal(self, bio=None, pronoun=None, photo=None):
        self.personal_info = {
                    "bio": bio,
                    "pronoun": pronoun,
                    "photo": photo,       
                    }

    def add_talk(self, title=None, description=None, track_name=None, time=None):
        _talk = Talk(title=title, description=description, track_name=track_name, time=time, speaker=self)
        self.talk = _talk

    def __repr__(self):
        """A prettier way of printing our node"""

        return """<Speaker | {} {}>""".format(
                                self.first_name,
                                self.last_name,
                                )


class Talk(object):
    """This is a Speaker's Session"""

    def __init__(self, title, description, track_name=None, time=None, speaker=None):
        self.title = title.capitalize()
        self.description = description
        self.slot = {
                    "track_name": track_name,
                    "time": time,
                    }
        self.speaker = speaker

    def __repr__(self):
        """A prettier way of printing our node"""

        return """<Talk | {}>""".format(
                                self.title,
                                )

###################### Speaker Example ##########################

jessica = Speaker(
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
jessica_talk = Talk(
    title="Celery",
    description="Information about Celery Talk",
    track_name=None,
    time=None,
    )

jessica.add_talk(
    title="Celery",
    description="Information about Celery Talk",
    track_name=None,
    time=None,
    )

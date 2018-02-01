"""Speaker & Talk Classes"""
import datetime
import random


class Person(object):
    """This is a human person"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

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
        if not photo:
            photo = "/static/imgs/speakers/{}.png".format(random.randint(0, 7))
        self.personal_info = {
                    "bio": bio,
                    "pronoun": pronoun,
                    "photo": photo,       
                    }

    def __repr__(self):
        """A prettier way of printing our node"""

        return """<Person | {} {}>""".format(
                                self.first_name,
                                self.last_name,
                                )


class Speaker(Person):
    """This is a Speaker"""

    def __init__(self, first_name, last_name):
        super(Speaker, self).__init__(first_name, last_name)
        self.first_name = first_name
        self.last_name = last_name
        self.talk = None
        self.workaround = None

    def add_talk(self, title=None, description=None, track_name=None, time=None, date=None, category=None,):
        _talk = Talk(title=title, description=description, track_name=track_name, time=time, date=date, speaker=self, category=category,)
        self.talk = _talk

    def __repr__(self):
        """A prettier way of printing our node"""

        return """<Speaker | {} {}>""".format(
                                self.first_name,
                                self.last_name,
                                )


class Organizer(Person):
    """This is a Organizer"""

    def __init__(self, first_name, last_name):
        super(Organizer, self).__init__(first_name, last_name)
        self.first_name = first_name
        self.last_name = last_name

    def add_committee_info(self, roles=None, gdg_name=None, gdg_role=None):
        self.committee_info = {
                    "roles": roles,
                    "gdg_name": gdg_name,
                    "gdg_role": gdg_role,
                    }

    def __repr__(self):
        """A prettier way of printing our node"""

        return """<Organizer | {} {}>""".format(
                                self.first_name,
                                self.last_name,
                                )


class Talk(object):
    """This is a Speaker's Session"""

    def __init__(self, title, description, track_name=None, time=None, speaker=None, date=None, session_length=None, category=None):
        self.title = title
        self.description = description
        self.category = category
        self.workaroundid = None

        if date is not None and time is not None:
            start = datetime.datetime.strptime("{} {}".format(date, time), '%m/%d/%Y %I:%M%p')
            end = start + datetime.timedelta(minutes=45)
            calendar_datetime = create_calendar_datetime(start, end)

        else: 
            calendar_datetime = None

        self.slot = {
                    "track_name": track_name,
                    "time": time,
                    "calendar_datetime": calendar_datetime
                    }
        self.speaker = speaker

    def __repr__(self):
        """A prettier way of printing our node"""

        return """<Talk | {}>""".format(
                                self.title,
                                )


def create_calendar_datetime(start, end):
    """Returns RFC 3339 format for Google calendar

        >>> date = "03/17/2018"
        >>> time = "1:00pm"
        >>> start = datetime.datetime.strptime("{} {}".format(date, time), '%m/%d/%Y %I:%M%p')
        >>> end = start + datetime.timedelta(minutes=45)
        >>> print create_calendar_datetime(start, end)
        20180317T130000%2F20180317T134500

    """
    start = start.isoformat('T')
    # removing the '-' and ':'
    part_1 = start[:11].split('-')
    part_2 = start[11:].split(':')
    #bring data back together
    part_1 = "".join(part_1)
    part_2 = "".join(part_2)
    #join the two pieces together
    start = part_1 + part_2

    end = end.isoformat('T')
    # removing the '-' and ':'
    part_1 = end[:11].split('-')
    part_2 = end[11:].split(':')
    #bring data back together
    part_1 = "".join(part_1)
    part_2 = "".join(part_2)
    #join the two pieces together
    end = part_1 + part_2

    # bring the start & end together!
    calendar_datetime = "{}%2F{}".format(start, end)

    return calendar_datetime

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

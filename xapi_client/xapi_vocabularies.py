"""
20/01/2020 - This module is here just as an example;
it is a copy of the module with the same in the "commons" application
"""
from collections import OrderedDict

xapi_activities = {
    'event': {'type': 'http://activitystrea.ms/schema/1.0/event',
        'display': {"en-US": "event",},
        'description': {"en-US": "Represents an event that occurs at a certain location during a particular period of time. Objects of this type MAY contain the additional properties specified in Section 3.3.",},
    },
    'meeting': {'type': 'http://adlnet.gov/expapi/activities/meeting',
        'display': {"en-us": "meeting"},
        'description': {"en-us": "A meeting is a gathering of multiple people for a common cause",},
    },
    'game': {'type': 'http://activitystrea.ms/schema/1.0/game',
        'display': {"en-US": "game",},
        'description': {"en-US": "Represents a game or competition of any kind.",},
    },
    'place': {'type': 'http://activitystrea.ms/schema/1.0/place',
        'display': {"en-US": "place",},
        'description': {"en-US": "Represents a physical location. Locations can be represented using geographic coordinates, a physical address, a free-form location name, or any combination of these. Objects of this type MAY contain the additional properties specified in Section 3.5.",},
    },
    'conference': {'type': 'http://id.tincanapi.com/activitytype/conference',
        'display': {"en-US": "conference",},
        'description': {"en-US": "A formal meeting which includes presentations or discussions.",},
    },
    'conference session': {'type': 'http://id.tincanapi.com/activitytype/conference-session',
        'display': {"en-US": "conference session",},
        'description': {"en-US": "A single presentation, discussion, gathering, or panel within a conference.",},
    },
    'tutor session': {'type': 'http://id.tincanapi.com/activitytype/tutor-session',
        'display': {"en-US": "tutor session",},
        'description': {"en-US": "This represents a tutoring session.",},
    },
    'webinar': {'type': 'http://id.tincanapi.com/activitytype/webinar',
        'display': {"en-US": "webinar",},
        'description': {"en-US": "A seminar conducted over the Internet which may be live or recorded.",},
    },
    'web page': {'type': 'http://activitystrea.ms/schema/1.0/page',
        'display': {"en-US": "web page", "it": "pagina web"},
        'description': {"en-US": "Represents an area, typically a web page, that is representative of, and generally managed by a particular entity, .. showcasing recent content such as articles, photographs and videos ..  ",},
    },
    'blog': {'type': 'http://id.tincanapi.com/activitytype/blog',
        'display': {"en-US": "blog",},
        'description': {"en-US": "A regularly updated website or web page, typically one authored by an individual or small group, that is written in an informal or conversational style.",},
    },
    'service': {'type': 'http://activitystrea.ms/schema/1.0/service',
        'display': {"en-US": "service",},
        'description': {"en-US": "Represents any form of hosted or consumable service that performs some kind of work or benefit for other entities. Examples of such objects include websites, businesses, etc.",},
    },
    'book': {'type': 'http://id.tincanapi.com/activitytype/book',
        'display': {"en-US": "book",},
        'description': {"en-US": "A book, generally paper, but could also be an ebook. The Activity's ID will often include an ISBN though it is not required. The Definition can likely leverage the ISBN extension, 'http://id.tincanapi.com/extension/isbn', if known.",},
    },
    'article': {'type': 'http://activitystrea.ms/schema/1.0/article',
        'display': {"en-US": "article",},
        'description': {"en-US": "Represents objects such as news articles, knowledge base entries, or other similar construct. Such objects generally consist of paragraphs of text, in some cases incorporating embedded media such as photos and inline hyperlinks to other resources.",},
    },

    'audio': {'type': 'http://activitystrea.ms/schema/1.0/audio',
        'display': {"en-US": "audio",},
        'description': {"en-US": "Represents audio content of any kind. Objects of this type MAY contain an additional property as specified in Section 3.1.",},
    },
    'video': {'type': 'http://activitystrea.ms/schema/1.0/video',
        'display': {"en-US": "video",},
        'description': {"en-US": "Represents video content of any kind. Objects of this type MAY contain additional properties as specified in Section 3.1.",},
    },
    'course': {'type': 'http://adlnet.gov/expapi/activities/course',
        'display': {"en-US": "course", "it": "corso",},
        'description': {"en-US": "A course represents an entire content package worth of material. The largest level of granularity. Usually a course consists of multiple modules.",},
    },
    'learning unit': {'type': 'http://adlnet.gov/expapi/activities/module',
        'display': {"en-US": "learning unit", "it": "unità d'apprendimento"},
        'description': {"en-US": "A module (or learning unit) represents any content aggregation at least one level below the course level. Modules of modules can exist for layering purposes.",},
    },
    'assignment': {'type': 'http://id.tincanapi.com/activitytype/school-assignment',
        'display': {"en-US": "school assignment ", "it": "compito",},
        'description': {"en-US": "A school task performed by a student to satisfy the teacher. Examples are assessments, assigned reading, practice exercises, watch video, etc.",},
    },
    'level': {'type': 'http://curatr3.com/define/type/level',
        'display': {"en-US": "level ", "it": "livello",},
        'description': {"en-US": "A level of a game or gamified learning platform. Also, a step in a difficulty or competence scale.",},
    },
    'assessment': {'type': 'http://adlnet.gov/expapi/activities/assessment',
        'display': {"en-US": "assessment",},
        'description': {"en-US": "An assessment is an activity that determines a learner's mastery of a particular subject area. An assessment typically is based on questions or other tests. Each may include several attempts",},
    },
    'attempt': {'type': 'http://adlnet.gov/expapi/activities/attempt',
        'display': {"en-US": "attempt",},
        'description': {"en-US": "An attempt is a discrete set of learner experiences in an activity. It gives systems the ability to uniquely identify experiences when they may have happened in different interactions with the same activity.",},
    },
    'performance': {'type': 'http://adlnet.gov/expapi/activities/attempt',
        'display': {"en-US": "performance",},
        'description': {"en-US": "A performance is an attempted task or series of tasks within a particular context. … It emphasizes learners being able to do, or perform, specific skills as a result of the instruction.",},
    },
    'certificate': {'type': 'https://www.opigno.org/en/tincan_registry/activity_type/certificate',
        'display': {"en-US": "certificate", "it": "certificato"},
        'description': {"en-US": "A document attesting to the fact that a person has completed an educational course.",},
    },
    'badge': {'type': 'http://activitystrea.ms/schema/1.0/badge',
        'display': {"en-US": "badge",},
        'description': {"en-US": "Represents a badge or award granted to an object (typically a person object)",},
    },
    'grade classification': {'type': '',
        'display': {"en-US": "grade classification", "it": "voto di classificazione"},
        'description': {"en-US": "Represents a grade given or received within a particular context, for example distinction within XYZ music test or A for ABC qualification.",},
    },
    'user profile': {'type': 'http://id.tincanapi.com/activitytype/user-profile',
        'display': {"en-US": "user profile", "it": "profilo d'utente"},
    },
    'folder': {'type': 'http://activitystrea.ms/schema/1.0/collection',
        'display': {"en-US": "folder", "it": "cartella"},
    },
    'collection': {'type': 'http://activitystrea.ms/schema/1.0/collection',
        'display': {"en-US": "collection", "it": "raccolta"},
    },
    'document': {'type': 'http://activitystrea.ms/schema/1.0/file',
        'display': {"en-US": "document", "it": "documento"},
    },
    'project': {'type': 'http://activitystrea.ms/schema/1.0/group',
        'display': {"en-US": "project", "it": "progetto"},
    },
    'membership': {'type': 'http://commonspaces.eu/activitytype/membership',
        'display': {"en-US": "membership", "it": "membro di gruppo"},
    },
    'discussion forum': {'type': 'http://id.tincanapi.com/activitytype/discussion',
        'display': {"en-US": "discussion forum", "it": "forum di discussione"},
    },
    'discussion topic': {'type': 'http://id.tincanapi.com/activitytype/forum-topic',
        'display': {"en-US": "discussion topic", "it": "argomento di discussione"},
    },
    'forum post': {'type': 'http://id.tincanapi.com/activitytype/forum-reply',
        'display': {"en-US": "forum post", "it": "post in forum"},
    },
    'resource repository': {'type': 'http://activitystrea.ms/schema/1.0/collection',
        'display': {"en-US": "resource repository", "it": "archivio di risorse"},
    },
    'oer': {'type': 'http://id.tincanapi.com/activitytype/resource',
        'display': {"en-US": "OER", "it": "OER"},
    },
    'oer rating': {'type': 'http://activitystrea.ms/schema/1.0/review',
        'display': {"en-US": "'OER rating'", "it": "valutazione di OER"},
        'description': {"en-US": "The object resulting from rating an OER.",
                        "it": "L'oggetto risultante dalla valutazione di un OER.",},
    },
    'learning path': {'type': 'http://id.tincanapi.com/activitytype/playlist',
        'display': {"en-US": "learning path", "it": "percorso d'apprendimento"},
    },
    'article': {'type': 'http://activitystrea.ms/schema/1.0/article',
        'display': {"en-US": "article", "it": "articolo"},
    },
    'private message': {'type': 'http://commonspaces.eu/activitytype/private-message',
        'display': {"en-US": "private message", "it": "messaggio privato"},
    },
    'show': {'type': 'http://commonspaces.eu/activitytype/show',
        'display': {"en-US": "show", "it": "mostra"},
    },
    'play': {'type': 'http://commonspaces.eu/activitytype/play',
        'display': {"en-US": "play", "it": "spettacolo teatrale"},
    },
    'concert': {'type': 'http://commonspaces.eu/activitytype/concert',
        'display': {"en-US": "concert", "it": "concerto"},
    },
    'exhibition': {'type': 'http://commonspaces.eu/activitytype/exhibition',
        'display': {"en-US": "exhibition", "it": "esposizione"},
    },
    'museum': {'type': 'http://commonspaces.eu/activitytype/museum',
        'display': {"en-US": "museum", "it": "museo"},
    },
}

xapi_verbs = {
    'was at': {'id': 'http://activitystrea.ms/schema/1.0/at',
        'display': {"en-US": "was at",},
        'description': {"en-US": "Indicates that the actor was located at the object. For instance, a person being at a specific physical location.",},
    },
    'attended': {'id': 'http://activitystrea.ms/schema/1.0/attend',
        'display': {"en-US": "attended",},
        'description': {"en-US": "Indicates that the actor has attended the object. For instance, a person attending a meeting.",},
    },
    'registered': {'id': 'http://adlnet.gov/expapi/verbs/registered',
        'display': {"en-US": "registered",},
        'description': {"en-US": "Indicates that the actor registered for a learning activity",},
    },
    'unregistered': {'id': 'http://id.tincanapi.com/verb/unregistered',
        'display': {"en-US": "unregistered",},
        'description': {"en-US": "Indicates the actor unregistered for a learning activity. This verb is used in combination with http://adlnet.gov/expapi/verbs/registered for the registering and unregistering of learners.",},
    },
    'joined': {'id': 'http://activitystrea.ms/schema/1.0/join',
        'display': {"en-US": "joined",},
        'description': {"en-US": "Indicates that the actor has become a member of the object. This specification only defines the meaning of this verb when the object of the Activity has an objectType of group, though implementors need to be prepared to handle other types of objects.",},
    },
    'left': {'id': 'http://activitystrea.ms/schema/1.0/leave',
        'display': {"en-US": "left",},
        'description': {"en-US": "Indicates that the actor has left the object. For instance, a Person leaving a Group or checking-out of a Place.",},
    },
    'scheduled': {'id': 'http://activitystrea.ms/schema/1.0/schedule',
        'display': {"en-US": "scheduled",},
        'description': {"en-US": "Indicates that the actor has scheduled the object. For instance, scheduling a meeting.",},
    },
    'opened': {'id': 'http://activitystrea.ms/schema/1.0/open',
        'display': {"en-US": "opened",},
        'description': {"en-US": "Indicates that the actor has opened the object. For instance, the object could represent a ticket being tracked in an issue management system.",},
    },
    'closed': {'id': 'http://activitystrea.ms/schema/1.0/close',
        'display': {"en-US": "closed",},
        'description': {"en-US": "Indicates that the actor has attended the object. For instance, a person attending a meeting.",},
    },
    'adjourned': {'id': 'http://id.tincanapi.com/verb/adjourned',
        'display': {"en-US": "adjourned",},
        'description': {"en-US": "Indicates the actor temporarily ended an event (e.g. a meeting). It is expected (but not required) that the event will be resumed at a future point in time. The actor of the statement should be somebody who has authority to adjourn the event, for example the event organizer.",},
    },
    'resumed': {'id': 'http://adlnet.gov/expapi/verbs/resumed',
        'display': {"en-US": "resumed",},
        'description': {"en-US": "Used to resume suspended attempts on an activity.  Should immediately follow a statement with initialized  if the attempt is indeed to be resumed. The absence of a resumed statement implies a fresh attempt on the activity.  Can only be used on an activity that used a suspended statement.",},
    },
    'experienced': {'id': 'http://activitystrea.ms/schema/1.0/experience',
        'display': {"en-US": "experienced",},
        'description': {"en-US": "Indicates that the actor has experienced the object in some manner .. It can be considered a  generic form of  more specific verbs as consume, play, watch, listen and read,"},
    },
    'read': {'id': 'http://activitystrea.ms/schema/1.0/read',
        'display': {"en-US": "read",},
        'description': {"en-US": "Indicates that the actor read the object. This is typically applicable for objects representing printed or written content, such as a book, a message or a comment. It is a more specific than consumed, experienced and played verbs.",},
    },
    'bookmarked': {'id': 'http://id.tincanapi.com/verb/bookmarked',
        'display': {"en-US": "bookmarked",},
        'description': {"en-US": "Indicates the user determined the content was important enough to keep a reference to it for later. A different verb should be used for tracking the location of a resource that a reader has reached, as in a physical bookmark.",},
    },
    'tweeted': {'id': 'http://id.tincanapi.com/verb/tweeted',
        'display': {"en-US": "tweeted",},
        'description': {"en-US": "Use this verb when an agent tweets on Twitter. It is open for use also for other short messages (microblogging services) based on the URI as the activityId. We expect activityId to be a URI to the tweet.",},
    },
    'consumed': {'id': 'http://activitystrea.ms/schema/1.0/consume',
        'display': {"en-US": "consumed",},
        'description': {"en-US": "Indicates that the actor has consumed the object. The specific meaning is dependent largely on the object's type. .. It is a more generic form of other more specific verbs such as read and play",},
    },
    'played': {'id': 'http://activitystrea.ms/schema/1.0/play',
        'display': {"en-US": "played",},
        'description': {"en-US": "Indicates that the actor spent some time enjoying the object. For example, if the object is a video this indicates that the subject watched all or part of the video. It is a more specific form of the consume verb.",},
    },
    'Play': {'id': 'http://activitystrea.ms/schema/1.0/play',
        'display': {"it": "ha interagito con",},
        'description': {"en-US": "Indicates that the actor spent some time enjoying the object. For example, if the object is a video this indicates that the subject watched all or part of the video. It is a more specific form of the consume verb.",},
    },
    'listened': {'id': 'http://activitystrea.ms/schema/1.0/listen',
        'display': {"en-US": "listened",},
        'description': {"en-US": "Indicates that the actor has listened to the object. This is typically only applicable for objects representing audio content, such as music, an audio-book, or a radio broadcast. It is a more specific form of the consume, experience and play verbs.",},
    },
    'watched': {'id': 'http://activitystrea.ms/schema/1.0/watch',
        'display': {"en-US": "watched",},
        'description': {"en-US": "Indicates that the actor has watched the object. This verb is typically applicable only when the object represents dynamic, visible content such as a movie, a television show or a public performance. It is a more specific form of the verbs experience, play and consume.",},
    },
    'commented': {'id': 'http://adlnet.gov/expapi/verbs/commented',
        'display': {"en-US": "commented", 'it-IT': 'ha commentato',},
        'description': {"en-US": "Offered an opinion or written experience of the activity. .. Comments can be sent from either party with the idea that the other will read and react to the content.",},
    },
    'rated': {'id': 'http://id.tincanapi.com/verb/rated',
        'display': {"en-US": "rated",},
        'description': {"en-US": "Action of giving a rating to an object. Should only be used when the action is the rating itself, as opposed to another action such as reading where a rating can be applied to the object as part of that action. In general the rating should be included in the Result with a Score object.",},
    },

    'enrolled onto': {'id': 'http://www.tincanapi.co.uk/verbs/enrolled_onto_learning_plan',
        'display': {"en-US": "enrolled onto", 'it-IT': 'si è iscritto a',},
        'description': {"en-US": "Used to add learners to an learning plan, a new plan if one does not exist. The actor is the person being enrolled onto the plan. IF the enrolment is being assigned by a 3rd party, the context instructor property may be used.",},
    },
    'started': {'id': 'http://activitystrea.ms/schema/1.0/start',
        'display': {"en-US": "started",},
        'description': {"en-US": "Indicates that the actor has started the object. For instance, when a person starts a project. Sometimes this isn't tracked.",},
    },
    'completed': {'id': 'http://activitystrea.ms/schema/1.0/complete',
        'display': {"en-US": "completed",},
        'description': {"en-US": "Indicates that the actor has completed the object .. Any content that has been initialized, but not yet completed, should be considered incomplete ..  Sometimes this isn't tracked explicitly.",},
    },
    'passed': {'id': ' http://adlnet.gov/expapi/verbs/passed',
        'display': {"en-US": "passed",},
        'description': {"en-US": "Used to affirm the success a learner experienced within the learning content in relation to a threshold. If the user performed at a minimum to the level of this threshold, the content is passed. The opposite of failed.",},
    },
    'failed': {'id': 'http://adlnet.gov/expapi/verbs/failed',
        'display': {"en-US": "failed",},
        'description': {"en-US": "Learner did not perform the activity to a level of pre-determined satisfaction. Used to affirm the lack of success a learner experienced within the learning content in relation to a threshold. If the user performed below the minimum to the level of this threshold, the content is 'failed'. The opposite of 'passed'.",},
    },
    'accepted': {'id': 'http://activitystrea.ms/schema/1.0/accept',
        'display': {"en-US": "accepted", 'it-IT': 'ha accettato',},
        'description': {"en-US": "Indicates that that the actor has accepted the object. For instance, a person accepting an award, or accepting an assignment.",},
    },
    'approved': {'id': 'http://activitystrea.ms/schema/1.0/approve',
        'display': {"en-US": "approved", 'it-IT': 'ha approvato',},
        'description': {"en-US": "Indicates that the actor has approved the object. For instance, a manager might approve a travel request.",},
    },
    'bookmarked': {'id': 'http://id.tincanapi.com/verb/bookmarked',
        'display': {"en-US": "bookmarked", 'it-IT': 'ha creato un segnalibro per',},
        'description': {"en-US": "Indicates the user determined the content was important enough to keep a reference to it for later.",},
    },
    'authored': {'id': 'http://activitystrea.ms/schema/1.0/author',
        'display': {"en-US": "authored", 'it-IT': 'è autore di',},
        'description': {"en-US": "Indicates that the actor has authored the object. Note that this is a more specific form of the verb create.",},
    },
    'created': {'id': 'http://activitystrea.ms/schema/1.0/create',
        'display': {"en-US": "created", 'it-IT': 'ha creato',},
        'description': {"en-US": "Indicates that the actor has created the object.",},
    },
    'updated': {'id': 'http://activitystrea.ms/schema/1.0/update',
        'display': {"en-US": "updated", 'it-IT': 'ha aggiornato',},
        'description': {"en-US": "Indicates that the actor has modified the object.",},
    },
    'deleted': {'id': 'http://activitystrea.ms/schema/1.0/delete',
        'display': {"en-US": "deleted", 'it-IT': 'ha cancellato',},
        'description': {"en-US": "Indicates that the actor has deleted the object. This implies, but does not require, the permanent destruction of the object.",},
    },
    'edited': {'id': 'http://curatr3.com/define/verb/edited',
        'display': {"en-US": "edited ", 'it-IT': 'ha editato',},
        'description': {"en-US": "Indicates that the actor edited an object, for example a user editing their account profile.",},
    },
    'rejected': {'id': 'http://activitystrea.ms/schema/1.0/reject',
        'display': {"en-US": "rejected", 'it-IT': 'ha rifiutato',},
        'description': {"en-US": "Indicates that the actor has rejected the object.",},
    },
    'searched': {'id': 'http://activitystrea.ms/schema/1.0/search',
        'display': {"en-US": "searched", 'it-IT': 'ha cercato',},
        'description': {"en-US": "Indicates that the actor is or has searched for the object. If a target is specified, it indicates the context within which the search is or has been conducted.",},
    },
    'sent': {'id': 'http://activitystrea.ms/schema/1.0/send',
        'display': {"en-US": "sent", 'it-IT': 'ha inviato',},
        'description': {"en-US": "Indicates that the actor has sent the object. If a target is specified, it indicates the entity to which the object was sent.",},
    },
    'submitted': {'id': 'http://activitystrea.ms/schema/1.0/submit',
        'display': {"en-US": "submitted", 'it-IT': 'ha sottoposto',},
        'description': {"en-US": "Indicates that the actor has submitted the object. If a target is specified, it indicates the entity to which the object was submitted.",},
    },
    'viewed': {'id': 'http://id.tincanapi.com/verb/viewed',
        'display': {"en-US": "viewed", 'it-IT': 'ha visto',},
        'description': {"en-US": "Indicates that the actor has viewed the object.",},
    },
    'qualified': {'id': 'http://activitystrea.ms/schema/1.0/qualify',
        'display': {"en-US": "qualified", 'it-IT': 'si è qualificato/a',},
        'description': {"en-US": "Indicates that the actor has qualified for the object. If a target is specified, it indicates the context within which the qualification applies.",},
    },
    'earned': {'id': 'http://id.tincanapi.com/verb/earned',
        'display': {"en-US": "earned", 'it-IT': 'ha conseguito',},
        'description': {"en-US": "Indicates that the actor has earned or has been awarded the object.",},
    },
    'received': {'id': 'http://activitystrea.ms/schema/1.0/receive',
        'display': {"en-US": "received", 'it-IT': 'ha ricevuto',},
        'description': {"en-US": "Indicates that the actor is receiving an object. Examples include a person receiving a badge object. The object identifies the object being received.",},
    },
    'accessed': {'id': 'http://activitystrea.ms/schema/1.0/access',
        'display': {"en-US": "accessed", 'it-IT': 'ha acceduto a',},
        'description': {"en-US": "Indicates that the actor has accessed the object. For instance, a person accessing a[n online conference] room, or accessing a file.",},
    },
}

xapi_recipes = OrderedDict([
    ('Events', { # extended from the Attendance profile: see https://registry.tincanapi.com/#home/profiles
        'activity_types': ['event', 'meeting', 'game', 'place', 'conference', 'conference session', 'tutor session', 'webinar', 'show', 'exhibition'],
        'verbs': ['attended', 'registered', 'unregistered', 'joined', 'left', 'commented', 'scheduled', 'opened', 'closed', 'adjourned', 'resumed',],
        'comment': 'this recipe mainly concerns work and learning activities scheduled at specific times; please, choose the generic item "event" only if you cannot specify better the activity type',
    }),
    ('Resources', { # extended from the Bookmarklet profile: see https://registry.tincanapi.com/#home/profiles
        'activity_types': ['web page', 'blog', 'webinar', 'service', 'book', 'article', 'audio', 'video', 'game',],
        'verbs': ['authored', 'created', 'edited', 'experienced', 'read', 'watched', 'listened', 'consumed', 'played', 'commented', 'rated', 'bookmarked', 'tweeted',],
        'comment': 'this recipe mainly concerns persistent resources used and referred to online',
    }),
    ('Performances', { # most verbs from https://registry.tincanapi.com/
        'activity_types': ['show', 'play', 'concert', 'exhibition', 'museum',],
        'verbs': ['was at', 'attended', 'watched', 'listened', 'experienced', 'commented', 'rated', 'tweeted',],
        'comment': 'this recipe mainly concerns leisure time activities',
    }),
    ('Learning control', { # adapted from the Assessment profile: see https://registry.tincanapi.com/#home/profiles
        'activity_types': ['course', 'learning path', 'learning unit', 'level', 'assignment', 'assessment', 'performance', 'attempt',],
        'verbs': ['enrolled onto', 'accepted', 'started', 'completed', 'passed', 'failed',],
        'comment': 'this recipe mainly concerns formal and non-formal education',
    }),
    ('Certification', {
        'activity_types': ['certificate', 'badge', 'level', 'grade classification',],
        'verbs': ['created', 'updated', 'earned', 'received', 'accepted', 'qualified',],
        'comment': 'this recipe mainly concerns certificates issued by official and nonofficial agencies',
    }),
    ('CommonSpaces', { # see https://www.commonspaces.it, or its alias https://cs.up2university.eu
        'activity_types': ['user profile', 'project', 'membership', 'folder', 'document', 'discussion forum', 'discussion topic', 'forum post', 'resource repository', 'oer', 'web page', 'oer rating', 'learning path', 'learning unit', 'article', 'private message', 'meeting',],
        'verbs': ['searched', 'viewed', 'played', 'commented', 'bookmarked', 'created', 'deleted', 'edited', 'submitted', 'accepted', 'approved', 'rejected', 'sent', 'accessed',],
        'comment': 'this recipe mainly concerns formal and non-formal education',
    }),
])

xapi_contextual_activities = ['project', 'course', 'learning path', 'folder', 'collection', 'resource repository', 'event', 'place',]

xapi_language_codes = [
    ('en', 'English'),
    ('it', 'Italian'),
    ('pt', 'Portuguese'),
    ('de', 'German'),
    ('el', 'Greek'),
    ('es', 'Spanish'),
    ('fr', 'French'),
    ('hu', 'Hungarian'),
    ('lt', 'Lithuanian'),
    ('nl', 'Dutch'),
    ('pl', 'Polish'),
]

xapi_verbs_by_id = {}
for key, value in xapi_verbs.items():
    xapi_verbs_by_id[value['id']] = value

xapi_activities_by_type = {}
for key, value in xapi_activities.items():
    xapi_activities_by_type[value['type']] = value

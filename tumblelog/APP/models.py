import datetime
from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin

class Record(db.Document):
    name = db.StringField(required=True)
    id_all = db.IntField(default=0)
    doc_all = db.IntField(default=0)

def next_id(record_name):
    find = Record.objects(name=record_name)
    if len(find) == 0:
        re = Record(name=record_name)
    else:
        re = find[0]
    try:
        re.id_all += 1
        re.save()
        return re.id_all
    except:
        pass


class User(UserMixin, db.Document):
    # private func start with __
    user_id = db.IntField(default=next_id('User'), unique=True, required=True)
    email = db.EmailField(unique=True, required=True)
    name = db.StringField(unique=True, required=True)
    role_id = db.IntField(default=0, required=True)
    password_hash = db.StringField(default='no', required=True)
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)

    @property
    def password():
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User %name>" % self.name


class Comment(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    body = db.StringField(verbose_name="Comment", required=True)
    author = db.StringField(verbose_name="Name", max_length=255, required=True)


class Post(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True)
    body = db.StringField(required=True)
    comments = db.ListField(db.EmbeddedDocumentField('Comment'))

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }


class Tieba_post_doc(db.Document):
    url_link = db.StringField(max_length=300, required=True)
    rep_num = db.IntField(required=True)
    title = db.StringField(max_length=100, required=True)
    # first_time = StringField(max_length=20, required=True)
    last_time = db.StringField(max_length=20, required=True)
    author = db.StringField(max_length=30, required=True)
    # tags = Field()
    body = db.StringField(required=True)


class Quotion_doc(db.Document):
    index = db.IntField(required=True)
    content = db.StringField(max_length=100, required=True)
    rep_num = db.IntField(required=True)
    last_time = db.StringField(max_length=20, required=True)
    author = db.StringField(max_length=30, required=True)


class Post_doc(db.Document):
    # url_link = db.StringField(max_length=300, required=True)
    rep_num = db.IntField(required=True)
    title = db.StringField(max_length=150, required=True)
    first_time = db.StringField(max_length=50, required=True)
    last_time = db.StringField(max_length=50, required=True)
    author = db.StringField(max_length=30, required=True)
    tags = db.ListField(db.StringField(max_length=30))
    body = db.StringField(required=True)



@login_manager.user_loader
def load_user(user_id):
    return User.objects(user_id=user_id)
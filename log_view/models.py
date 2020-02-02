from log_view import db


class LoginInfo(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    remote_addr = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
    host = db.Column(db.Text)
    user = db.Column(db.Text)
    event_type = db.Column(db.Text)
    raw_text = db.Column(db.Text)

    def __repr__(self):
        return '<Entry id={id} title={raw_text!r}>'.format(
                id=self.id, raw_text=self.raw_text)


def init():
    db.create_all()

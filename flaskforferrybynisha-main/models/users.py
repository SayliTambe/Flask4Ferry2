from datetime import datetime
from extensions import db

class User(db.Model):
    __tablename__ = 'ports'
    
    # Updated column names and types based on the CREATE TABLE statement
    id = db.Column('Port_ID', db.Integer, primary_key=True, autoincrement=True)
    portname = db.Column('Port_Name', db.String(200))
    state = db.Column('Port_State', db.String(100))
    address = db.Column('Port_Address', db.String(300))
    portcity = db.Column('Port_City', db.String(100))
    contact = db.Column('Port_Contact', db.String(45), nullable=False)
    port_status = db.Column(db.String(10))
    
    #created_at = db.Column(db.DateTime, default=datetime.utcnow)
    #updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    @property
    def data(self):
        return {
            'id': self.id,
            'portname': self.portname,
            'state': self.state,
            'address': self.address,
            'portcity': self.portcity,
            'contact': self.contact
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

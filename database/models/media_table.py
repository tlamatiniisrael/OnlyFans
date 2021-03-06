### api_table.py ###

import sqlalchemy


class media_table():
    __tablename__ = "medias"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    media_id = sqlalchemy.Column(sqlalchemy.Integer, unique=True)
    post_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    link = sqlalchemy.Column(sqlalchemy.String)
    directory = sqlalchemy.Column(sqlalchemy.String)
    filename = sqlalchemy.Column(sqlalchemy.String)
    size = sqlalchemy.Column(sqlalchemy.Integer, default=None)
    media_type = sqlalchemy.Column(sqlalchemy.String)
    preview = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    downloaded = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    created_at = sqlalchemy.Column(sqlalchemy.DATETIME)

    def legacy(self,Base):
        class legacy_media_table(Base):
            __tablename__ = "medias"
            id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
            post_id = sqlalchemy.Column(sqlalchemy.Integer)
            link = sqlalchemy.Column(sqlalchemy.String)
            directory = sqlalchemy.Column(sqlalchemy.String)
            filename = sqlalchemy.Column(sqlalchemy.String)
            size = sqlalchemy.Column(sqlalchemy.Integer, default=None)
            media_type = sqlalchemy.Column(sqlalchemy.String)
            downloaded = sqlalchemy.Column(sqlalchemy.Integer, default=0)
            created_at = sqlalchemy.Column(sqlalchemy.DATETIME)
        return legacy_media_table

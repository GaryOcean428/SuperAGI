from __future__ import annotations
import requests

from sqlalchemy import Column, Integer, String

# from superagi.models import AgentConfiguration
from superagi.models.base_model import DBBaseModel

#marketplace_url = "https://app.superagi.com/api"
marketplace_url = "http://localhost:3000/api"

class Vectordb(DBBaseModel):
    """
    Represents an vector db entity.
    Attributes:
        id (int): The unique identifier of the agent.
        name (str): The name of the database.
        db_type (str): The name of the db agent.
        organisation_id (int): The identifier of the associated organisation.
    """

    __tablename__ = 'vector_dbs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    db_type = Column(String)
    organisation_id = Column(Integer)

    def __repr__(self):
        """
        Returns a string representation of the Vector db object.
        Returns:
            str: String representation of the Vector db.
        """
        return f"Vector(id={self.id}, name='{self.name}', db_type='{self.db_type}' organisation_id={self.organisation_id}"
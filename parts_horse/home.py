from .base import *
from .search import *

class Home(PartsHorseBase):
    def __init__(self):
        super().__init__()
        self.template = self.env.get_template('home.html')

    @cherrypy.expose
    def index(self):
        AppGlobals.update_site(self.env)

        page = self.page_dict({"recent": Search.recent()})
        return self.render(self.template, page)

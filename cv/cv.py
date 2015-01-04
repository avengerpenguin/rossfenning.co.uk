from pelican import signals
from jinja2 import Template
from laconia import ThingFactory
from rdflib import Graph


def render(sender):
    g = Graph()
    g.parse('cv/cv.ttl', format='turtle')
    out = Template(open('./cv/cv.tmpl').read()).render(cv=ThingFactory(g)('http://rossfenning.co.uk/cv'))
    print(out.encode('utf-8'))


def register():
    signals.initialized.connect(render)

from pelican import signals
from jinja2 import Template
from laconia import ThingFactory
from rdflib import Graph
from jinja2 import Environment, PackageLoader


env = Environment(
    loader=PackageLoader('cv', 'templates'),
    block_start_string='<%', block_end_string='%>',
    variable_start_string='<=', variable_end_string='=>')

template = env.get_template('cv.tmpl')


def render(sender):
    g = Graph()
    g.parse('cv/cv.ttl', format='turtle')
    out = template.render(cv=ThingFactory(g)('http://rossfenning.co.uk/cv'))
    print(out.encode('utf-8'))


def register():
    signals.initialized.connect(render)

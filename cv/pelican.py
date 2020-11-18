import json

from pelican import signals
from laconia import ThingFactory
from rdflib import Graph, RDFS, OWL, Namespace, RDF
from jinja2 import Environment, PackageLoader
from jinja2 import tests
from sh import xelatex
from pyld import jsonld

env_md = Environment(loader=PackageLoader("cv", "templates"))
template_md = env_md.get_template("template.md")

env_tex = Environment(loader=PackageLoader("cv", "templates"))
env_tex.block_start_string = "((*"
env_tex.block_end_string = "*))"
env_tex.variable_start_string = "((("
env_tex.variable_end_string = ")))"
env_tex.comment_start_string = "((="
env_tex.comment_end_string = "=))"
template_latex = env_tex.get_template("template.tex")

CV = Namespace("http://rdfs.org/resume-rdf/cv.rdfs#")


def render(_sender):
    g = Graph()
    # TODO: make configurable
    g.parse("content/extra/cv.ttl", format="turtle")

    # TODO: make configurable
    cv = ThingFactory(g)("http://rossfenning.co.uk/cv/#cv")

    skills = {
        level: [
            skill
            for skill in cv.cv_hasSkill
            if skill.cv_skillLevel.any() == level
        ]
        for level in range(0, 6)
    }

    skill_levels = {
        5: "Expert",
        4: "Advanced",
        3: "Intermediate",
        2: "Novice",
        1: "Beginner",
    }

    jsonld_data = jsonld.compact(
        jsonld.frame(
            json.loads(g.serialize(format="json-ld",).decode("utf8")),
            {"@type": "http://rdfs.org/resume-rdf/cv.rdfs#CV"},
        ),
        {alias: url for alias, url in g.namespaces()},
    )
    out = template_md.render(
        cv=cv,
        skills=skills,
        skill_levels=skill_levels,
        jsonld=json.dumps(jsonld_data, indent=2),
    )

    # TODO: make configurable
    with open("content/pages/cv.md", "w") as cv_out:
        cv_out.write(out)

    out = template_latex.render(
        cv=cv, skills=skills, skill_levels=skill_levels
    )

    # TODO: make configurable
    with open("content/extra/cv.tex", "w") as cv_out:
        cv_out.write(out)

    print(
        xelatex(
            "-halt-on-error",
            "-interaction=batchmode",
            "cv.tex",
            _cwd="content/extra/",
        )
    )


def register():
    signals.initialized.connect(render)


if __name__ == "__main__":
    render(None)

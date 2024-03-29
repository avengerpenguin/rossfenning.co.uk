import json
from collections import defaultdict

from jinja2 import Environment, PackageLoader
from laconia import ThingFactory
from pelican import signals
from pyld import jsonld
from rdflib import Graph, Namespace
from sh import pdflatex

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
        level: [skill for skill in cv.cv_hasSkill if skill.cv_skillLevel.any() == level]
        for level in range(0, 6)
    }

    skill_levels = {
        5: "Expert",
        4: "Advanced",
        3: "Intermediate",
        2: "Novice",
        1: "Beginner",
    }

    info = defaultdict(list)
    for extra in cv.cv_hasOtherInfo:
        info[str(extra.cv_otherInfoType.any()).split("#")[-1]].append(
            extra.cv_otherInfoDescription.any()
        )

    jsonld_data = jsonld.compact(
        jsonld.frame(
            json.loads(
                g.serialize(
                    format="json-ld",
                )
            ),
            {"@type": "http://rdfs.org/resume-rdf/cv.rdfs#CV"},
        ),
        {alias: url for alias, url in g.namespaces()},
    )
    out = template_md.render(
        cv=cv,
        skills=skills,
        skill_levels=skill_levels,
        jsonld=json.dumps(jsonld_data, indent=2),
        info=info,
    )

    # TODO: make configurable
    with open("content/pages/cv.md", "w") as cv_out:
        cv_out.write(out)

    out = template_latex.render(
        cv=cv, skills=skills, skill_levels=skill_levels, info=info
    )

    # TODO: make configurable
    with open("content/extra/cv.tex", "w") as cv_out:
        cv_out.write(out)

    print(
        pdflatex(
            "-halt-on-error",
            "cv.tex",
            _cwd="content/extra/",
        )
    )


def register():
    signals.initialized.connect(render)


if __name__ == "__main__":
    render(None)

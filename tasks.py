import voltaire
from invoke import task

namespace = voltaire.site()


@task
def cv_forks(c):
    with c.cd("content/extra"):
        c.run("xelatex -halt-on-error -interaction=batchmode python.tex")


namespace.add_task(cv_forks)
namespace["build"].pre.append(cv_forks)

title: {{ cv.cv_cvTitle.any() }}
slug: cv
vocab: http://rdfs.org/resume-rdf/cv.rdfs#
typeof: CV


<div property="aboutPerson" typeof="Person" resource="{{cv.cv_aboutPerson.any()}}"></div>

## Personal Profile

{{ cv.cv_cvDescription.any() }}


## Skills

{% for level in range(5, 1, -1) %}
### {{ skill_levels[level] }}

<span typeof="Skill" property="hasSkill"><span property="skillName">{{ skills[level]|map(attribute='cv_skillName')|map('first')|sort|join('</span></span>, <span typeof="Skill" property="hasSkill"><span property="skillName">') }}</span></span>
{% endfor %}


## Work Experience

{% for work_history in cv.cv_hasWorkHistory | sort(attribute='cv_startDate', reverse=True) %}
{% if work_history.cv_employedIn %}{% if work_history.cv_employedIn.any().cv_Name %}
<div typeof="WorkHistory" property="hasWorkHistory" markdown="1">
### {% if work_history.cv_jobTitle %}<span property="jobTitle">{{ work_history.cv_jobTitle|first }}</span> at {% endif %}<span typeof="Company" property="employedIn"><span property="Name">{{ work_history.cv_employedIn.any().cv_Name.any() }}</span></span>{% if work_history.cv_startDate %}: <span property="startDate">{{ work_history.cv_startDate }}</span> to {% if work_history.cv_endDate %}<span property="endDate">{{ work_history.cv_endDate.any() }}</span>{% else %}present{% endif %}{% endif %}

{% set lines = work_history.cv_jobDescription.any().split('\n\n') %}
{% for line in lines %}
{% if line %}
* {{ line }}
{% endif %}
{% endfor %}

</div>

{% endif %}{% endif %}
{% endfor %}


## Education

{% for education in cv.cv_hasEducation | sort(attribute='cv_eduGradDate', reverse=True) %}

<div typeof="Education" property="hasEducation" markdown="1">

### <span property="eduMajor">{{ education.cv_eduMajor.any() }}</span> at <span typeof="EducationalOrg" property="studiedIn"><span property="Name">{{ education.cv_studiedIn.any().cv_Name.any() }}</span></span> ({% if education.cv_eduGradDate %}<span property="eduGradDate">{{ education.cv_eduGradDate }}</span>{% else %}Ongoing{% endif %})

{% set lines = education.cv_eduDescription.any().split('\n\n') %}
{% for line in lines %}
{% if line %}
* {{ line }}
{% endif %}
{% endfor %}

</div>

{% endfor %}

### Further Education (2002)

* A grade in each of A-Level Mathematics, Further Mathematics,
German and Physics.
* B grade in AS-Level French.
* STEP I Mathematics with grade 1
* STEP Physics with grade 3.

### GCSEs (2000)

* 9 GCSEs including A\* in Sciences, German and French.
* A in English Language.
* A grade in an Additional Mathematics qualification

### GCSEs (1999)

* A\* grade in Mathematics

{% for info_type, info_items in info|items %}
## {{ info_type }}

{% for item in info_items %}
* {{ item }}
{% endfor %}

{% endfor %}

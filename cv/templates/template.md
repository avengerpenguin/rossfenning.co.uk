title: {{ cv.cv_cvTitle.any() }}
slug: cv
vocab: http://rdfs.org/resume-rdf/cv.rdfs#
typeof: CV


<div property="aboutPerson" typeof="Person" resource="{{cv.cv_aboutPerson.any()}}"></div>

## Personal Profile

{{ cv.cv_cvDescription.any() }}


## Skills

{% for level in range(5, 0, -1) %}
### {{ skill_levels[level] }}

<span typeof="Skill" property="hasSkill"><span property="skillName">{{ skills[level]|map(attribute='cv_skillName')|map('first')|sort|join('</span></span>, <span typeof="Skill" property="hasSkill"><span property="skillName">') }}</span></span>
{% endfor %}


## Work Experience

{% for work_history in cv.cv_hasWorkHistory | sort(attribute='cv_startDate', reverse=True) %}
{% if work_history.cv_employedIn %}{% if work_history.cv_employedIn.any().cv_Name %}
<div typeof="WorkHistory" property="hasWorkHistory" markdown="1">
### {% if work_history.cv_jobTitle %}<span property="jobTitle">{{ work_history.cv_jobTitle|first }}</span> at {% endif %}<span typeof="Company" property="employedIn"><span property="Name">{{ work_history.cv_employedIn.any().cv_Name.any() }}</span></span>{% if work_history.cv_startDate %}: <span property="startDate">{{ work_history.cv_startDate }}</span> to {% if work_history.cv_endDate %}<span property="endDate">{{ work_history.cv_endDate.any() }}</span>{% else %}present{% endif %}{% endif %}

{% if work_history.cv_jobDescription %}{{ work_history.cv_jobDescription.any() }}{% endif %}
</div>
{% endif %}{% endif %}
{% endfor %}


## Education

{% for education in cv.cv_hasEducation | sort(attribute='cv_eduGradDate', reverse=True) %}

<div typeof="Education" property="hasEducation" markdown="1">

### <span property="eduMajor">{{ education.cv_eduMajor.any() }}</span> at <span typeof="EducationalOrg" property="studiedIn"><span property="Name">{{ education.cv_studiedIn.any().cv_Name.any() }}</span></span> ({% if education.cv_eduGradDate %}<span property="eduGradDate">{{ education.cv_eduGradDate }}</span>{% else %}Ongoing{% endif %})

{% if education.cv_eduDescription %}<span property="eduDescription">{{ education.cv_eduDescription.any() }}</span>{% endif %}

</div>

{% endfor %}

### Further Education (2002)

Gained an A grade in each of A-Level Mathematics, Further Mathematics,
German and Physics. Additionally achieved a B grade in AS-Level French.
Also completed STEP I Mathematics with grade 1 and STEP Physics with
grade 3.

### GCSEs (2000)

10 GCSEs including A\* in Mathematics, Sciences, German and French.
Attained A in English Language. Also obtained an A grade in an
Additional Mathematics qualification having completed the GCSE the
previous year (1999).


## Interests

-   Natural language processing, artificial intelligence, linguistics
	and logic
-   Folk and traditional music including playing bodhrán
-   Exploring new music as well as writing/composition
-   Modern foreign languages
-   Supporting human rights and environmental work

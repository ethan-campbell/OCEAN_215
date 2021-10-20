---
layout: page
title: Instructors
description: A listing of all the course staff members.
---

# Instructors

## Autumn 2020

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

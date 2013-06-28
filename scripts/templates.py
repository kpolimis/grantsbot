#! /usr/bin/python2.7

# Copyright 2013 Jtmorgan

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

class Template:
	"""templates of wiki pages"""
#all that top-level markup shouldn't be necessary; should re-org the IdeaLab/Introductions page so that all profiles are under the first section
	def __init__(self):
		self.profile_templates = {'participant profile' : u"""<noinclude><div style="font-family: Helvetica Neue, Helvetica, arial, sans-serif; line-height: 1.5em; background-color: #ffffff; color: #{{{{IEG/Color/Gray}}}}; min-width: 810px; margin-top: -60px; padding: 40px 0 20px">
<div style="margin:0 15%">
<span style="font-size: 3em; color: #{{{{IEG/Color/Light blue}}}};">'''Individual Engagement Grants'''</span>
<div style="margin:1em 0">
<span style="font-size: 3em; color: #{{{{IEG/Color/Light blue}}}};">introductions</span></div>
<div style="margin:3em 0">If you've made any corrections to your introduction and you are finished, [[Grants:IdeaLab|return to the IdeaLab]].</div>
</div>
</div></noinclude>
[[Category:Individual Engagement Grants]]
{profiles}"""
,
'featured idea' : u"""
{{{{IdeaLab/Feature
| time = {time}
| image =
| action = {action}
| number of people =
| idea = {title}
| idea link = {page path}
| summary = {summary}
}}}}"""
,
'featured person' : u"""
{{{{IdeaLab/Feature
| time = {time}
| image = {image}
| action = {action}
| name = {username}
| username = {page path}
| summary = {summary}
}}}}"""
,
'idea profile' : u"""
==<noinclude>{title}</noinclude>==
{{{{IdeaLab/Idea/Summary
| time= {time}
| idea= {title}
| idea link= {page path}
| summary= {summary}
| creator= {creator}
| image =
}}}}"""
,
}

#changed 'featured idea' param value to 'title' for consistency

	def getTemplate(self, tmplt_type):
		if tmplt_type in self.profile_templates:
			return self.profile_templates[tmplt_type]


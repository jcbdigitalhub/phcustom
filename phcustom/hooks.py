# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "phcustom"
app_title = "Customizations"
app_publisher = "www.ossphinc.com"
app_description = "Customizations"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "info@ossphinc.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/phcustom/css/phcustom.css"
# app_include_js = "/assets/phcustom/js/phcustom.js"

# include js, css files in header of web template
# web_include_css = "/assets/phcustom/css/phcustom.css"
# web_include_js = "/assets/phcustom/js/phcustom.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "phcustom.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "phcustom.install.before_install"
# after_install = "phcustom.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "phcustom.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

#doc_events = {
 	#"Purchase Invoice": {
 		#"on_update": "phcustom.api.update_budget",
 		#"on_cancel": "phcustom.api.update_budget",
 		#"on_trash": "phcustom.api.update_budget"
	#},
 	#"Purchase Order": {
 		#"on_update": "phcustom.api.update_budget",
 		#"on_cancel": "phcustom.api.update_budget",
 		#"on_trash": "phcustom.api.update_budget"
	#},
 	#"Stock Entry": {
 		#"on_update": "phcustom.api.update_budget",
 		#"on_cancel": "phcustom.api.update_budget",
 		#"on_trash": "phcustom.api.update_budget"
	#}
#}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"phcustom.tasks.all"
# 	],
# 	"daily": [
# 		"phcustom.tasks.daily"
# 	],
# 	"hourly": [
# 		"phcustom.tasks.hourly"
# 	],
# 	"weekly": [
# 		"phcustom.tasks.weekly"
# 	]
# 	"monthly": [
# 		"phcustom.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "phcustom.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "phcustom.event.get_events"
# }


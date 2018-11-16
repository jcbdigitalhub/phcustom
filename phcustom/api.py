import frappe
import json
from frappe import _
from frappe.utils import nowdate, add_days

@frappe.whitelist()
def update_budget(doc,method):
	if doc.doctype == "Purchase Invoice":
		prjinv = frappe.db.sql("""select project, sum(base_net_amount) as amount FROM `tabPurchase Invoice Item`
			WHERE parent = %s
			GROUP BY project;""", doc.name, as_dict=1)

		for i in prjinv:
			check_budget(i.project, i.amount)
			if not frappe.db.exists('Project Budget', {'project': i.project, 'document_type': "Purchase Invoice", 'document_no': doc.name}):
					prjdoc = frappe.new_doc('Project Budget')
					prjdoc.project = i.project
					prjdoc.document_type = "Purchase Invoice"
					prjdoc.document_no = doc.name
					prjdoc.currency = "PHP"
					prjdoc.amount = i.amount
					prjdoc.doc_status = doc.docstatus
					prjdoc.insert()
			else:
					prjbud = frappe.db.sql("""select name FROM `tabProject Budget`
						WHERE project= %s AND document_type = 'Purchase Invoice' AND document_no = %s;""", 
						(i.project, doc.name), as_dict=1)
					prjdoc = frappe.get_doc('Project Budget', prjbud[0].name)
					prjdoc.project = i.project
					prjdoc.document_type = "Purchase Invoice"
					prjdoc.document_no = doc.name
					prjdoc.currency = "PHP"
					prjdoc.amount = i.amount
					prjdoc.doc_status = doc.docstatus
					prjdoc.save()

	if doc.doctype == "Purchase Order":
		prjinv = frappe.db.sql("""select project, sum(base_net_amount) as amount FROM `tabPurchase Order Item`
			WHERE parent = %s
			GROUP BY project;""", doc.name, as_dict=1)

		for i in prjinv:
			check_budget(i.project, i.amount)
			if not frappe.db.exists('Project Budget', {'project': i.project, 'document_type': "Purchase Order", 'document_no': doc.name}):
					prjdoc = frappe.new_doc('Project Budget')
					prjdoc.project = i.project
					prjdoc.document_type = "Purchase Order"
					prjdoc.document_no = doc.name
					prjdoc.currency = "PHP"
					prjdoc.amount = i.amount
					prjdoc.doc_status = doc.docstatus
					prjdoc.insert()
			else:
					prjbud = frappe.db.sql("""select name FROM `tabProject Budget`
						WHERE project= %s AND document_type = 'Purchase Order' AND document_no = %s;""", 
						(i.project, doc.name), as_dict=1)
					prjdoc = frappe.get_doc('Project Budget', prjbud[0].name)
					prjdoc.project = i.project
					prjdoc.document_type = "Purchase Order"
					prjdoc.document_no = doc.name
					prjdoc.currency = "PHP"
					prjdoc.amount = i.amount
					prjdoc.doc_status = doc.docstatus
					prjdoc.save()

	if doc.doctype == "Stock Entry":
		prjinv = frappe.db.sql("""select project, value_difference*-1 as amount FROM `tabStock Entry`
			WHERE parent = %s;""", doc.name, as_dict=1)

		for i in prjinv:
			check_budget(i.project, i.amount)
			if not frappe.db.exists('Project Budget', {'project': i.project, 'document_type': "Stock Entry", 'document_no': doc.name}):
					prjdoc = frappe.new_doc('Project Budget')
					prjdoc.project = i.project
					prjdoc.document_type = "Stock Entry"
					prjdoc.document_no = doc.name
					prjdoc.currency = "PHP"
					prjdoc.amount = i.amount
					prjdoc.doc_status = doc.docstatus
					prjdoc.insert()
			else:
					prjbud = frappe.db.sql("""select name FROM `tabProject Budget`
						WHERE project= %s AND document_type = 'Stock Entry' AND document_no = %s;""", 
						(i.project, doc.name), as_dict=1)
					prjdoc = frappe.get_doc('Project Budget', prjbud[0].name)
					prjdoc.project = i.project
					prjdoc.document_type = "Stock Entry"
					prjdoc.document_no = doc.name
					prjdoc.currency = "PHP"
					prjdoc.amount = i.amount
					prjdoc.doc_status = doc.docstatus
					prjdoc.save()


def check_budget(project,amount):
	actual = frappe.db.sql("""select sum(amount) as amount FROM `tabProject Budget`
		WHERE project = %s AND doc_status<2;""", project, as_dict=1)
	budget = frappe.get_doc('Project',project)
	balance = budget.estimated_costing - (actual[0].amount + amount)
	excess = balance * -1

	if balance < 0:
		frappe.throw(_("Expenses for {0} will exceed budget by {1}. Please review your Project Estimated Cost.").format(project, excess))
		
def before_cancel(doc, method):
	frappe.db.sql("""delete from `tabBatch Purchase Invoice Approval Invoices`
		where docstatus = 1 AND purchase_invoice = %s""", doc.name)

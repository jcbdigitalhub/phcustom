# -*- coding: utf-8 -*-
# Copyright (c) 2018, www.ossphinc.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class BatchPurchaseInvoiceApproval(Document):
	def submit(self):
		if len(self.invoices) > 100:
			self.queue_action('submit')
		else:
			self._submit()

	def on_submit(self):
		for invoice in self.invoices:
			if invoice.action == "Approve":
				inv = frappe.get_doc('Purchase Invoice',invoice.purchase_invoice)
				next = frappe.db.get_value("Workflow Document State",{"parent": "Purchase Invoice", "state": self.approve_state}, "doc_status")

				inv.add_comment("Workflow", self.approve_state)

				inv.workflow_state = self.approve_state
				inv.save()

				if next == "1":
					inv.submit()

		if invoice.action == "Reject":
				inv = frappe.get_doc('Purchase Invoice',invoice.purchase_invoice)
				next = frappe.db.get_value("Workflow Document State",{"parent": "Purchase Invoice", "state": self.disapprove_state}, "doc_status")

				inv.add_comment("Workflow", self.disapprove_state)

				inv.workflow_state = self.disapprove_state
				inv.save()

				if next == "2":
						frappe.db.sql("""delete from `tabBatch Purchase Invoice Approval Invoices`
							where docstatus = 1 AND purchase_invoice = %s""", invoice.purchase_invoice)
						inv.cancel()

	def get_details(self):
			self.approver = frappe.session.user
			user = frappe.get_doc('User', frappe.session.user)
			currentstate = user.default_current_state
			self.current_state = currentstate
			self.approve_state = user.approve_state
			self.disapprove_state = user.disapprove_state



	#def get_details(self):
			#self.insert()

			inv = frappe.db.sql("""SELECT u.name as purchase_invoice, CONCAT( u.supplier_name,': ',u.remarks) as remarks,
				u.due_date as due_date, u.currency as currency, u.outstanding_amount as amount, 
				(SELECT  project FROM `tabPurchase Invoice Item` WHERE parent = u.name LIMIT 1) as project 
				FROM `tabPurchase Invoice` u WHERE u.workflow_state = %s ORDER BY u.supplier_name;""",(currentstate), as_dict=1)

			if inv:
				#frappe.msgprint("done with sql")

				for i in inv:
					#frappe.msgprint("i am at loop")
					self.append('invoices',{
						"purchase_invoice": i.purchase_invoice,
						"remarks": i.remarks,
						"project": i.project,
						"currency": i.currency,
						"amount": i.amount
						})
			else:
				frappe.msgprint("No pending Purchase Invoice for your Action.")

# -*- coding: utf-8 -*-
# Copyright (c) 2017, www.ossph.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _, msgprint, throw

class BatchwiseStockReconciliation(Document):
	pass

	@frappe.whitelist()
	def generate(self):
		self.set("items", [])
		count = frappe.db.sql("""SELECT l.item_code, b.valuation_rate, l.warehouse, l.serial_no, l.batch_no, sum(l.actual_qty) as count_qty FROM `tabBin` b, `tabStock Ledger Entry` l
			WHERE b.item_code = l.item_code AND b.warehouse = l.warehouse AND l.warehouse  IN (SELECT name FROM `tabWarehouse` WHERE parent_warehouse = %s) 
			AND TIMESTAMP(l.posting_date, l.posting_time) <= TIMESTAMP( %s, %s) 
			GROUP BY l.item_code, l.warehouse, l.serial_no, l.batch_no;""", (self.warehouse, self.posting_date, self.posting_time), as_dict=1)

		for i in count:
			c_doc = self.append('items',{
				"item_code": i.item_code,
				"item_name": i.description,
				"warehouse" : i.warehouse,
				"serial_no": i.serial_no,
				"batch": i.batch_no,
				"system_qty": i.count_qty,
				"valuation_rate": i.valuation_rate
			})

	def on_submit(self):
		doc = frappe.new_doc("Stock Entry")
		doc.purpose = "Material Receipt"
		doc.physical_count_entry = 1
		doc.posting_date = self.posting_date
		doc.posting_date = self.posting_time
		doc.to_warehouse = self.warehouse

		"Add Items"
		i = frappe.db.sql("""SELECT item_code, item_name, warehouse, serial_no, batch, system_qty, actual_qty, valuation_rate """+
			"""FROM `tabBatchwise Stock Reconciliation Item` """+
			"""WHERE parent = %s""", self.name,as_dict=1)

		for d in i:
			c_doc = doc.append('items',{
					"item_code": d.item_code,
					"t_warehouse": d.warehouse,
					"serial_no": d.serial_no,
					"batch_no": d.batch,
					"qty": d.actual_qty - d.system_qty,
					"basic_rate": d.valuation_rate,
					"basic_expense": self.expense_account,
					"cost_center": self.cost_center
				})

		doc.insert()
		self.stock_entry = doc.name
		

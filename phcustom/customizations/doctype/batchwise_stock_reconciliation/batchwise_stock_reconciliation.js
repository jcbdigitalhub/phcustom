// Copyright (c) 2017, www.ossph.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Batchwise Stock Reconciliation', {
	refresh: function(frm) {
		frm.fields_dict.warehouse.get_query = function(doc, cdt, cdn) {
			child = locals[cdt][cdn];
			return{	
			filters:[
			['is_group', '=', 1]
			]
		}}
	},
	generate_count_sheet: function(frm) {
		cur_frm.call('generate','', function(r){ }
		);
	}
});

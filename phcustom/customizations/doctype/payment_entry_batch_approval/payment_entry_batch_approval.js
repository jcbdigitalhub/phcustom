// Copyright (c) 2018, www.ossphinc.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Payment Entry Batch Approval', {
	refresh: function(frm) {

	},
	date: function(frm) {
                cur_frm.call('get_details','', function(r){ cur_frm.cscript.refresh  }
                );
        }
});

frappe.ui.form.on('Payment Entry Batch Items', {
	action: function(frm,cdt,cdn) {
		var approved = 0 || 0;
		var rejected = 0 || 0;
		var no_action = 0 || 0;

		$.each(frm.doc.invoices, function(i, d) {
			if (d.action == "Approve") { approved += d.amount || 0; }
			if (d.action == "Reject") { rejected += d.amount || 0; }
			if (d.action == "") { no_action += d.amount || 0; }
		});

		frm.set_value("total_approved", approved);
		frm.set_value("total_rejected", rejected);
		frm.set_value("total_no_action", no_action);
		cur_frm.refresh_field("total_approved");
		cur_frm.refresh_field("total_rejected");
		cur_frm.refresh_field("total_base_amount");
		cur_frm.refresh_field("invoices");

	}
});

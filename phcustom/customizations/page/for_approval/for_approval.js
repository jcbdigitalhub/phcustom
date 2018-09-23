frappe.pages['for_approval'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'For Approval',
		single_column: true
	});
}
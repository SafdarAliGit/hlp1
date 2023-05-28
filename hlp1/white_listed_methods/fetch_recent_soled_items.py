import frappe


@frappe.whitelist()
def fetch_recent_soled_items():
    filters = {}

    data = frappe.db.sql(
        """
        select 
            `tabSales Invoice Item`.name, `tabSales Invoice Item`.parent,
            `tabSales Invoice`.posting_date,`tabSales Invoice`.customer_name,
            `tabSales Invoice Item`.item_code,`tabSales Invoice Item`.`item_name`,
            `tabSales Invoice Item`.rate
        from `tabSales Invoice`, `tabSales Invoice Item`
        where `tabSales Invoice`.name = `tabSales Invoice Item`.parent
            and `tabSales Invoice`.docstatus = 1 order by `tabSales Invoice Item`.parent
        """,
        as_dict=1
    )[:5]
    return data

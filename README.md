# Visitor Management Module for Odoo 18

A custom Odoo module to manage visitors in your organization. This module allows you to track visitor check-ins, check-outs, visit duration, and associate visitors with employees.

---

## **Features**

- Add and manage visitors with details such as:
  - Name
  - Phone
  - Address
  - Purpose of visit
  - Check-in and check-out times
  - Status (Draft, Checked In, Checked Out)
- Track the duration of visitor stays.
- Associate visitors with one or multiple employees.
- View visitors in a separate **Visitors tab** in the Employee form.
- Print visitor cards.
- Supports search, filters, and group by in list views.

---

## **Installation**

1. Copy the `visitor_management` folder into your Odoo `custom_addons` directory.
2. Update the App List in Odoo:
   - Go to **Apps → Update Apps List → Update**.
3. Install the module from the Apps menu.

---

## **Usage**

- Go to **Visitors** menu:
  - Add a visitor.
  - Assign one or multiple employees.
  - Check-in and check-out visitors.
- Open an **Employee** form:
  - Check the **Visitors** tab to see all visitors associated with that employee.

---

## **Dependencies**

- Odoo 18
- `hr` (Employees) module

---
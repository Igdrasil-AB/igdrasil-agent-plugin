---
name: open-invoice-review
description: List open (unpaid) customer invoices in Igdrasil and find supporting documents. Use for collections follow-up or "who owes us money". Read-only; never records payments, sends reminders or settles invoices.
---

# Open invoice review

Lists the open customer invoices (accounts receivable) for one Igdrasil company.

## Steps

1. Pick the company with `igdrasil_list_companies`, and pass its `company_id`
   to every later call.
2. Call `customer_invoices_open_items` to get the open amount for each invoice.
   The amounts come from the committed event history.
3. Report each invoice's open amount, currency, issued amount, settled amount
   and reminder fees.
4. This tool returns **no due dates**. Call invoices *open*, never *overdue*,
   unless the user gives you the due dates.
5. If the user asks for evidence, call `documents_search`. It is read-only and
   returns citations.
6. Supplier invoices (accounts payable) are not covered by this skill. Say so
   instead of guessing.

## Never

- Record a payment, mark an invoice paid, or post a settlement.
- Send a payment order, a Bankgiro or Plusgiro transfer, or a reminder.
- Cancel, credit or delete an invoice.
- Smooth over an inconsistency the tool reports. Pass it on to the user.

If the user asks to pay, book a payment or send a reminder, decline. Point
them to the Igdrasil app at https://accounting.igdrasil.se.

## Output

- Total open amount per currency, and the number of invoices
- One line per invoice: number, open amount, currency
- A note that due dates were not available, unless the user supplied them

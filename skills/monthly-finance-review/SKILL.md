---
name: monthly-finance-review
description: Monthly review of an Igdrasil company's headline figures, profit and loss, and bank balances. Use when the user asks how a month or period went, wants a board-pack summary, or asks for a resultaträkning. Read-only; never posts, pays or closes a period.
---

# Monthly finance review

Review one Igdrasil company for a calendar month, or for the `from`/`to`
window the user gives.

## Steps

1. Pick the company. Call `igdrasil_list_companies`. If there is more than
   one company, ask which one. Pass its `company_id` to every later call.
2. Confirm the period. Do not guess the fiscal year.
3. Read, in this order:
   - `reports_kpis`: headline figures for the window.
   - `reports_income_statement`: resultaträkning (income statement) for the same window.
   - `bank_accounts_balance`: cash *position* by bank account.
4. Quote numbers exactly as the tools return them. Never re-add ledger lines
   to produce a competing figure.
5. Raise gaps (an empty period, unreconciled bank lines, a tool error) as
   questions for the user, not as corrections.

## Never

- Post, reverse or amend entries. Never close a period or stage a journal.
- Pay invoices, transfer money, or mark anything as paid.
- File VAT or income-tax returns.
- Substitute a zero, `"unknown"` or an estimate when a tool returns an error.
  Report the error instead.
- Call a cash-position figure a kassaflödesanalys (cash-flow statement).
  Igdrasil has no cash-flow report; say the figure is bank balances.

If the user asks you to change the books, decline. Point them to the Igdrasil
app at https://accounting.igdrasil.se, where a person reviews and applies
changes.

## Output

- Company and period
- Headline KPIs as returned
- A plain-language P&L: revenue, costs, result
- Bank balances, with the source named
- Open questions

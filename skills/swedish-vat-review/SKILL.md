---
name: swedish-vat-review
description: Review a company's Swedish VAT (moms) position in Igdrasil for a declaration period, including rutor and the amount to pay or reclaim. Use for momsdeklaration questions. Read-only; never files with Skatteverket or posts a VAT settlement.
---

# Swedish VAT review

Show the VAT position for a period the user names (month, quarter or year).

## Steps

1. Pick the company with `igdrasil_list_companies`, and pass its `company_id`
   to every later call.
2. Confirm the declaration period. Swedish VAT follows the company's
   reporting period, so "this month" may not be a valid declaration period.
3. Read the position:
   - For a named period (period type, year and period), use
     `reports_vat_declaration`. It also reports readiness issues, such as
     entries that are missing a VAT code.
   - For an explicit date range, use `reports_momsdeklaration`.
4. Report the rutor, any warnings, and the amount to pay or reclaim exactly as
   Igdrasil computed them. The ruta mapping is versioned rule data; do not
   recompute VAT from ledger lines.
5. List readiness issues and warnings as items for a person to fix in the
   Igdrasil app.

## Never

- File with Skatteverket, or build an eSKD or other submission file. Never
  call `reports_vat_declaration_eskd`.
- Post a VAT settlement or close a VAT period.
- Pay the VAT balance.

If the user asks to file or settle, decline. Filing and settlement are done in
the Igdrasil app at https://accounting.igdrasil.se.

## Output

- Period and dates
- Amount to pay or reclaim, labelled as a **position, not a filed return**
- The rutor that matter, plus any warnings or readiness issues
- A closing line stating that nothing has been filed

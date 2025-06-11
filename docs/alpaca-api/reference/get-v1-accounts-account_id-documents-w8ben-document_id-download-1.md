---
title: Download the W8BEN document for the primary owner of an account
source: reference\get-v1-accounts-account_id-documents-w8ben-document_id-download-1.html
---

get https://broker-api.sandbox.alpaca.markets/v1/accounts/{account_id}/documents/w8ben/{document_id}/download
This endpoint allows you to download a W-8 BEN document for the primary owner of an account based on the document_id passed as a path parameter. The returned document is in PDF format.
For certain individuals, a W-8 BEN form should be submitted at onboarding. If the individual is not a registered U.S. taxpayer (not subject to a W-9), the W-8 BEN form may need to be submitted. The IRS explains which individuals this applies to and provides instructions on completing the form. Every three years, in addition to the calendar year it was signed, a new W-8 BEN form must be submitted.
The form can be submitted in JSON, JSONC, PNG, JPEG or PDF. If submitting it in JSON, please see the W-8 BEN completed with the corresponding field names for the API here.
Note: The dates collected on the form are in a slightly different format than how they need to be submitted via Accounts API. It is requested by the user on the form in MM-DD-YYYY, but should be submitted as YYYY-MM-DD.

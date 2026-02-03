# Workflow Recipe Examples

Ready-to-copy workflow examples. Replace IDs with 26-character Orchard IDs from
`scripts/generate-orchard-ids.py`.

## Contact form workflow (HTTP POST)

Requirements:
- Features: `OrchardCore.Workflows`, `OrchardCore.Workflows.Http`, `OrchardCore.Forms`,
  `OrchardCore.Email`, plus an email provider (e.g. `OrchardCore.Email.Smtp`).
- Form action: set the form's post URL to the generated workflow URL after import.

Notes:
- The `Url` value is replaced on import if `TokenLifeSpan` exists. Copy the new URL from
  the workflow editor and update your form action.
- `ValidateAntiforgeryToken` should align with `FormPart.EnableAntiForgeryToken`.

```json
{
  "name": "WorkflowType",
  "data": [
    {
      "WorkflowTypeId": "4acxmdtjrv4vn47c8xvaqkmbxv",
      "Name": "Contact",
      "IsEnabled": true,
      "IsSingleton": false,
      "LockTimeout": 0,
      "LockExpiration": 0,
      "DeleteFinishedWorkflows": false,
      "Activities": [
        {
          "ActivityId": "47899c3q5pkqhyrcnawnmay35d",
          "Name": "HttpRequestEvent",
          "X": 0,
          "Y": 0,
          "IsStart": true,
          "Properties": {
            "ActivityMetadata": { "Title": "Contact Form Submitted" },
            "HttpMethod": "POST",
            "Url": "/workflows/Invoke?token=replace-on-import",
            "ValidateAntiforgeryToken": true,
            "TokenLifeSpan": 0,
            "FormLocationKey": ""
          }
        },
        {
          "ActivityId": "4g9qcpfd711by7yrj1jcr425cz",
          "Name": "BindModelStateTask",
          "X": 320,
          "Y": 0,
          "IsStart": false,
          "Properties": {
            "ActivityMetadata": { "Title": "Bind Form Model State" }
          }
        },
        {
          "ActivityId": "4mrh855dzjp3h1xg63pgmqarn6",
          "Name": "ForkTask",
          "X": 620,
          "Y": 0,
          "IsStart": false,
          "Properties": {
            "ActivityMetadata": { "Title": "Validate Fields" },
            "Forks": [ "Name", "Email", "Company", "Message" ]
          }
        },
        {
          "ActivityId": "4x50jfcw4h803v147sd5r5yawd",
          "Name": "ValidateFormFieldTask",
          "X": 370,
          "Y": 220,
          "IsStart": false,
          "Properties": {
            "ActivityMetadata": { "Title": "Validate Name" },
            "FieldName": "name",
            "ErrorMessage": "Please enter your name."
          }
        },
        {
          "ActivityId": "49kh70ewz64fgvncnnkp4s104d",
          "Name": "ValidateFormFieldTask",
          "X": 650,
          "Y": 220,
          "IsStart": false,
          "Properties": {
            "ActivityMetadata": { "Title": "Validate Email" },
            "FieldName": "email",
            "ErrorMessage": "Please enter your work email."
          }
        },
        {
          "ActivityId": "4jxjhyatmt0z3t8yybwq685mn6",
          "Name": "ValidateFormFieldTask",
          "X": 1130,
          "Y": 220,
          "IsStart": false,
          "Properties": {
            "ActivityMetadata": { "Title": "Validate Company" },
            "FieldName": "company",
            "ErrorMessage": "Please enter your company name."
          }
        },
        {
          "ActivityId": "443wmah9h20at5hz565978vwc7",
          "Name": "ValidateFormFieldTask",
          "X": 900,
          "Y": 220,
          "IsStart": false,
          "Properties": {
            "ActivityMetadata": { "Title": "Validate Message" },
            "FieldName": "message",
            "ErrorMessage": "Please enter your message."
          }
        },
        {
          "ActivityId": "4z3bqqbadr7mwrz9cc4ahagydj",
          "Name": "JoinTask",
          "X": 520,
          "Y": 390,
          "IsStart": false,
          "Properties": {
            "ActivityMetadata": { "Title": "Join" },
            "Mode": "WaitAll"
          }
        },
        {
          "ActivityId": "49xb4dwks5d6s6v61yf2b4zsmd",
          "Name": "ValidateFormTask",
          "X": 520,
          "Y": 560,
          "IsStart": false,
          "Properties": {
            "ActivityMetadata": {}
          }
        },
        {
          "ActivityId": "4v963y3hed8vz6w47jkcjznzd7",
          "Name": "HttpRedirectTask",
          "X": 200,
          "Y": 550,
          "IsStart": false,
          "Properties": {
            "ActivityMetadata": { "Title": "Display Form Errors" },
            "Location": { "Expression": "/contact" },
            "Permanent": false
          }
        },
        {
          "ActivityId": "41jre1e80jgzrreqnpzejpn2ck",
          "Name": "EmailTask",
          "X": 860,
          "Y": 580,
          "IsStart": false,
          "Properties": {
            "Sender": {},
            "Author": {},
            "Recipients": { "Expression": "hello@example.com" },
            "ReplyTo": { "Expression": "{{ Request.Form.email }}" },
            "Subject": {
              "Expression": "New contact request from {{ Request.Form.name }}"
            },
            "Body": {
              "Expression": "<p>Name: {{ Request.Form.name }}</p>\r\n<p>Email: {{ Request.Form.email }}</p>\r\n<p>Company: {{ Request.Form.company }}</p>\r\n<p>Message:</p>\r\n<p>{{ Request.Form.message }}</p>"
            },
            "IsHtmlBody": true,
            "Bcc": {},
            "Cc": {},
            "ActivityMetadata": { "Title": "Send Email" }
          }
        },
        {
          "ActivityId": "42s3w17g54czt7fwr5vswdxedn",
          "Name": "HttpRedirectTask",
          "X": 1150,
          "Y": 400,
          "IsStart": false,
          "Properties": {
            "ActivityMetadata": { "Title": "Display Success" },
            "Location": { "Expression": "/message-sent" },
            "Permanent": false
          }
        }
      ],
      "Transitions": [
        {
          "Id": 0,
          "SourceActivityId": "47899c3q5pkqhyrcnawnmay35d",
          "SourceOutcomeName": "Done",
          "DestinationActivityId": "4g9qcpfd711by7yrj1jcr425cz"
        },
        {
          "Id": 0,
          "SourceActivityId": "4g9qcpfd711by7yrj1jcr425cz",
          "SourceOutcomeName": "Done",
          "DestinationActivityId": "4mrh855dzjp3h1xg63pgmqarn6"
        },
        {
          "Id": 0,
          "SourceActivityId": "4mrh855dzjp3h1xg63pgmqarn6",
          "SourceOutcomeName": "Name",
          "DestinationActivityId": "4x50jfcw4h803v147sd5r5yawd"
        },
        {
          "Id": 0,
          "SourceActivityId": "4mrh855dzjp3h1xg63pgmqarn6",
          "SourceOutcomeName": "Email",
          "DestinationActivityId": "49kh70ewz64fgvncnnkp4s104d"
        },
        {
          "Id": 0,
          "SourceActivityId": "4mrh855dzjp3h1xg63pgmqarn6",
          "SourceOutcomeName": "Company",
          "DestinationActivityId": "4jxjhyatmt0z3t8yybwq685mn6"
        },
        {
          "Id": 0,
          "SourceActivityId": "4mrh855dzjp3h1xg63pgmqarn6",
          "SourceOutcomeName": "Message",
          "DestinationActivityId": "443wmah9h20at5hz565978vwc7"
        },
        {
          "Id": 0,
          "SourceActivityId": "4x50jfcw4h803v147sd5r5yawd",
          "SourceOutcomeName": "Done",
          "DestinationActivityId": "4z3bqqbadr7mwrz9cc4ahagydj"
        },
        {
          "Id": 0,
          "SourceActivityId": "49kh70ewz64fgvncnnkp4s104d",
          "SourceOutcomeName": "Done",
          "DestinationActivityId": "4z3bqqbadr7mwrz9cc4ahagydj"
        },
        {
          "Id": 0,
          "SourceActivityId": "4jxjhyatmt0z3t8yybwq685mn6",
          "SourceOutcomeName": "Done",
          "DestinationActivityId": "4z3bqqbadr7mwrz9cc4ahagydj"
        },
        {
          "Id": 0,
          "SourceActivityId": "443wmah9h20at5hz565978vwc7",
          "SourceOutcomeName": "Done",
          "DestinationActivityId": "4z3bqqbadr7mwrz9cc4ahagydj"
        },
        {
          "Id": 0,
          "SourceActivityId": "4z3bqqbadr7mwrz9cc4ahagydj",
          "SourceOutcomeName": "Joined",
          "DestinationActivityId": "49xb4dwks5d6s6v61yf2b4zsmd"
        },
        {
          "Id": 0,
          "SourceActivityId": "49xb4dwks5d6s6v61yf2b4zsmd",
          "SourceOutcomeName": "Invalid",
          "DestinationActivityId": "4v963y3hed8vz6w47jkcjznzd7"
        },
        {
          "Id": 0,
          "SourceActivityId": "49xb4dwks5d6s6v61yf2b4zsmd",
          "SourceOutcomeName": "Valid",
          "DestinationActivityId": "41jre1e80jgzrreqnpzejpn2ck"
        },
        {
          "Id": 0,
          "SourceActivityId": "41jre1e80jgzrreqnpzejpn2ck",
          "SourceOutcomeName": "Done",
          "DestinationActivityId": "42s3w17g54czt7fwr5vswdxedn"
        }
      ],
      "Properties": {}
    }
  ]
}
```

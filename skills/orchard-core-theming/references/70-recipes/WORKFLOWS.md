# Workflows in Recipes

How to author Orchard Core workflows in recipes without source access.

## Feature checklist
Enable the features for the activities you use. If a feature is missing, the activity becomes a
`MissingActivity` and the workflow will not run.

Core engine:
- `OrchardCore.Workflows`

Optional activity feature groups:
- `OrchardCore.Workflows.Http`
- `OrchardCore.Workflows.Timers`
- `OrchardCore.Workflows.Session`
- `OrchardCore.Forms`
- `OrchardCore.Contents`
- `OrchardCore.Email` plus a provider (e.g. `OrchardCore.Email.Smtp`)
- `OrchardCore.ReCaptcha`
- `OrchardCore.Notifications` (for Notify* tasks)
- `OrchardCore.Users`
- `OrchardCore.Roles`
- `OrchardCore.Sms`
- `OrchardCore.Twitter`
- `OrchardCore.Tenants`

## WorkflowType recipe step
Step name is `WorkflowType`. Each item in `data` is a workflow definition.
```json
{
  "name": "WorkflowType",
  "data": [
    {
      "WorkflowTypeId": "26charid...",
      "Name": "My Workflow",
      "IsEnabled": true,
      "IsSingleton": false,
      "LockTimeout": 0,
      "LockExpiration": 0,
      "DeleteFinishedWorkflows": false,
      "Activities": [
        {
          "ActivityId": "26charid...",
          "Name": "ContentPublishedEvent",
          "X": 0,
          "Y": 0,
          "IsStart": true,
          "Properties": {
            "ActivityMetadata": { "Title": "Page Published" },
            "ContentTypeFilter": [ "Page" ]
          }
        }
      ],
      "Transitions": [
        {
          "SourceActivityId": "26charid...",
          "SourceOutcomeName": "Done",
          "DestinationActivityId": "26charid..."
        }
      ],
      "Properties": {}
    }
  ]
}
```
Notes:
- `WorkflowTypeId` and every `ActivityId` are 26-char Orchard IDs. Use
  `scripts/generate-orchard-ids.py` when you need stable IDs.
- `ActivityMetadata.Title` is optional and only affects editor UI labels.
- `X` and `Y` are editor coordinates; they do not affect runtime behavior.
- `IsStart` should be `true` only on event activities (`IEvent` / `EventActivity`).
- `SourceOutcomeName` must match the activity's outcome string exactly.
- Example workflows live in `RECIPE-EXAMPLES-WORKFLOWS.md`.

## Start events vs tasks
- Start activities are events (`EventActivity`, `IEvent`), e.g. `ContentPublishedEvent`,
  `HttpRequestEvent`, `SignalEvent`, `TimerEvent`.
- Tasks are `TaskActivity` (`ITask`) and run after events.
- Events usually `Halt()` while waiting; when triggered they resume with `Done` or a specific
  outcome (see activity catalog below).

## Expressions: Liquid vs JavaScript
Activities use two evaluators:
- `IWorkflowExpressionEvaluator` -> Liquid expressions.
- `IWorkflowScriptEvaluator` -> JavaScript expressions.

Expression values are stored in JSON as:
```json
"SomeProperty": { "Expression": "..." }
```

### Liquid context
Liquid expressions get a `Workflow` object:
- `Workflow.Input`, `Workflow.Output`, `Workflow.Properties`, `Workflow.LastResult`.
Example:
```liquid
{{ Workflow.Input.ContentItem.DisplayText | append: " TEST" }}
```

### JavaScript helpers
JS expressions can use global helpers:
- `input(name)` -> workflow input
- `output(name, value)` -> set output
- `property(name)` / `setProperty(name, value)` -> workflow properties
- `lastResult()` -> last activity result
- `correlationId()` / `setCorrelationId(value)`
- `workflow()` -> full `WorkflowExecutionContext`

## WorkflowType import behavior
On import, if `WorkflowTypeId` already exists it is deleted and replaced.
For new workflows, any `HttpRequestEvent` with a `TokenLifeSpan` property will have its `Url`
regenerated to `/workflows/Invoke?token=...`.

## Content event inputs
Content events provide:
- `Workflow.Input.ContentItem` (the content item)
- `Workflow.Input.ContentEvent` (name, content type, ids)
Key names are `ContentItem` and `ContentEvent` (from `ContentEventConstants`).

## Common pitfalls
- If a workflow references an activity from a disabled feature, it becomes `MissingActivity`.
- `UpdateContentTask` cannot update the same item inline from a `ContentPublishedEvent`
  (throws). Use a different event or update a different item.
- `NotifyTask` (Workflows) shows a UI notification to the current user only; it does not send
  email. Use `NotifyUserTask` / `NotifyContentOwnerTask` for stored notifications.
- `ContentProperties` expressions are Liquid JSON strings; escape quotes once in recipes
  (use `\"`, not `\\\"`) or the editor shows literal backslashes.

## Activity catalog (properties + outcomes)
This list reflects all activities registered by `services.AddActivity<...>` in Orchard Core.

### OrchardCore.Workflows (feature: `OrchardCore.Workflows`)
- WorkflowFaultEvent
  - Properties: `ErrorFilter` (JS, `WorkflowExpression<bool>`)
  - Outcomes: `Done`
- NotifyTask
  - Properties: `NotificationType` (Success|Information|Warning|Error), `Message` (Liquid)
  - Outcomes: `Done`
- SetPropertyTask
  - Properties: `PropertyName` (string), `Value` (JS)
  - Outcomes: `Done`
- SetOutputTask
  - Properties: `OutputName` (string), `Value` (JS)
  - Outcomes: `Done`
- CorrelateTask
  - Properties: `Value` (Liquid or JS), `Syntax` (Liquid|JavaScript)
  - Outcomes: `Done`
- ForkTask
  - Properties: `Forks` (list of strings)
  - Outcomes: one per fork name
- JoinTask
  - Properties: `Mode` (WaitAll|WaitAny)
  - Outcomes: `Joined`
- ForLoopTask
  - Properties: `From` (JS), `To` (JS), `Step` (JS), `LoopVariableName` (string), `Index` (number)
  - Outcomes: `Iterate`, `Done`
- ForEachTask
  - Properties: `Enumerable` (JS), `LoopVariableName` (string), `Current`, `Index`
  - Outcomes: `Iterate`, `Done`
- WhileLoopTask
  - Properties: `Condition` (JS)
  - Outcomes: `Iterate`, `Done`
- IfElseTask
  - Properties: `Condition` (JS)
  - Outcomes: `True`, `False`
- ScriptTask
  - Properties: `AvailableOutcomes` (list), `Script` (JS, can call `setOutcome('X')`)
  - Outcomes: values from `AvailableOutcomes`
- LogTask
  - Properties: `LogLevel` (enum), `Text` (Liquid)
  - Outcomes: `Done`

### OrchardCore.Workflows.Session (feature: `OrchardCore.Workflows.Session`)
- CommitTransactionTask
  - Properties: none
  - Outcomes: `Done`, `Valid`, `Invalid`

### OrchardCore.Workflows.Timers (feature: `OrchardCore.Workflows.Timers`)
- TimerEvent
  - Properties: `CronExpression` (string), `UseLocalTime` (bool)
  - Outcomes: `Done`

### OrchardCore.Workflows.Http (feature: `OrchardCore.Workflows.Http`)
- HttpRequestEvent
  - Properties: `HttpMethod`, `Url`, `ValidateAntiforgeryToken` (bool),
    `TokenLifeSpan` (int days), `FormLocationKey`
  - Outcomes: `Done`
- HttpRequestFilterEvent
  - Properties: `HttpMethod`, `ControllerName`, `ActionName`, `AreaName`, `RouteValues`
  - Outcomes: `Matched`
- HttpRedirectTask
  - Properties: `Location` (Liquid), `Permanent` (bool)
  - Outcomes: `Done`
- HttpRequestTask
  - Properties: `Url` (Liquid), `HttpMethod`, `Headers` (Liquid), `Body` (Liquid),
    `ContentType` (Liquid), `HttpResponseCodes` (string list)
  - Outcomes: each status code string (e.g. "200"), plus `UnhandledHttpStatus`
- HttpResponseTask
  - Properties: `Content` (Liquid), `HttpStatusCode` (int), `Headers` (Liquid),
    `ContentType` (Liquid)
  - Outcomes: `Done`
- SignalEvent
  - Properties: `SignalName` (Liquid)
  - Outcomes: `Done`

### OrchardCore.Workflows.UserTasks (requires `OrchardCore.Workflows`, `OrchardCore.Contents`, `OrchardCore.Roles`)
- UserTaskEvent
  - Properties: `Actions` (list), `Roles` (list, stored for editor)
  - Outcomes: one per action

### OrchardCore.Forms (feature: `OrchardCore.Forms` + `OrchardCore.Workflows`)
- ValidateAntiforgeryTokenTask
  - Properties: none
  - Outcomes: `Done`, `Valid`, `Invalid`
- AddModelValidationErrorTask
  - Properties: `Key`, `ErrorMessage`
  - Outcomes: `Done`
- ValidateFormTask
  - Properties: none
  - Outcomes: `Valid`, `Invalid`
- ValidateFormFieldTask
  - Properties: `FieldName`, `ErrorMessage`
  - Outcomes: `Done`, `Valid`, `Invalid`
- BindModelStateTask
  - Properties: none
  - Outcomes: `Done`
- HttpRedirectToFormLocationTask
  - Properties: `FormLocationKey`
  - Outcomes: `Done`, `Failed`

### OrchardCore.Contents (feature: `OrchardCore.Contents` + `OrchardCore.Workflows`)
- Content events: `ContentCreatedEvent`, `ContentDeletedEvent`, `ContentPublishedEvent`,
  `ContentUnpublishedEvent`, `ContentUpdatedEvent`, `ContentDraftSavedEvent`,
  `ContentVersionedEvent`
  - Properties: `ContentTypeFilter` (list of content types)
  - Outcomes: `Done`
- CreateContentTask
  - Properties: `ContentType` (string), `Publish` (bool), `ContentProperties` (Liquid JSON)
  - Outcomes: `Done`, `Failed`
- RetrieveContentTask
  - Properties: `Content` (JS expression for ContentItemId)
  - Outcomes: `Retrieved`
- UpdateContentTask
  - Properties: `Content` (JS expression for ContentItemId),
    `ContentProperties` (Liquid JSON), `Publish` (bool)
  - Outcomes: `Done`, `Failed`
  - ContentProperties example (recipe string):
    `{"DisplayText": "{{ Workflow.Input.ContentItem.DisplayText | append: ' TEST' | json }}" }`
- PublishContentTask
  - Properties: `Content` (JS expression for ContentItemId)
  - Outcomes: `Published`, `Noop`
- UnpublishContentTask
  - Properties: `Content` (JS expression for ContentItemId)
  - Outcomes: `Unpublished`, `Noop`
- DeleteContentTask
  - Properties: `Content` (JS expression for ContentItemId)
  - Outcomes: `Deleted`, `Noop`

### OrchardCore.Email (feature: `OrchardCore.Email` + provider)
- EmailTask
  - Properties: `Author`, `Sender`, `ReplyTo`, `Recipients`, `Cc`, `Bcc`,
    `Subject`, `Body` (deprecated), `IsHtmlBody` (deprecated),
    `BodyFormat`, `TextBody`, `HtmlBody` (Liquid)
  - Outcomes: `Done`, `Failed`

### OrchardCore.ReCaptcha (feature: `OrchardCore.ReCaptcha`)
- ValidateReCaptchaTask
  - Properties: none
  - Outcomes: `Done`, `Valid`, `Invalid`

### OrchardCore.Roles (feature: `OrchardCore.Roles` + `OrchardCore.Workflows`)
- UnassignUserRoleTask
  - Properties: `UserName` (Liquid), `Roles` (list)
  - Outcomes: `Done`, `Failed`
- GetUsersByRoleTask
  - Properties: `OutputKeyName` (Liquid), `Roles` (list)
  - Outcomes: `Done`, `Failed`

### OrchardCore.Users (feature: `OrchardCore.Users` + `OrchardCore.Workflows`)
- User events: `UserCreatedEvent`, `UserDeletedEvent`, `UserEnabledEvent`, `UserDisabledEvent`,
  `UserUpdatedEvent`, `UserLoggedInEvent`, `UserConfirmedEvent`
  - Properties: `User` (JS expression, optional)
  - Outcomes: `Done`
- AssignUserRoleTask
  - Properties: `UserName` (Liquid), `RoleName` (Liquid)
  - Outcomes: `Done`, `Failed`
- ValidateUserTask
  - Properties: `SetUserName` (bool), `Roles` (list)
  - Outcomes: `Anonymous`, `Authenticated`, `InRole`
- RegisterUserTask (requires `OrchardCore.Email`)
  - Properties: `SendConfirmationEmail` (bool), `ConfirmationEmailSubject` (Liquid),
    `ConfirmationEmailTemplate` (Liquid), `RequireModeration` (bool)
  - Outcomes: `Done`, `Valid`, `Invalid`

### OrchardCore.Notifications (feature: `OrchardCore.Notifications` + `OrchardCore.Workflows`)
- NotifyUserTask
  - Properties: `UserNames` (Liquid, comma separated), `Subject`, `Summary`,
    `TextBody`, `HtmlBody` (Liquid), `IsHtmlPreferred` (bool)
  - Outcomes: `Done`, `Failed`, `Failed: no user found`
- NotifyContentOwnerTask (also requires `OrchardCore.Users` + `OrchardCore.Contents`)
  - Properties: same as `NotifyUserTask`
  - Outcomes: `Done`, `Failed`, `Failed: no user found`

### OrchardCore.Sms (feature: `OrchardCore.Sms` + `OrchardCore.Workflows`)
- SmsTask
  - Properties: `PhoneNumber` (Liquid), `Body` (Liquid)
  - Outcomes: `Done`, `Failed`

### OrchardCore.Twitter (feature: `OrchardCore.Twitter` + `OrchardCore.Workflows`)
- UpdateTwitterStatusTask
  - Properties: `StatusTemplate` (Liquid)
  - Outcomes: `Done`, `Failed`

### OrchardCore.Tenants (feature: `OrchardCore.Tenants` + `OrchardCore.Workflows`)
- DisableTenantTask
  - Properties: `TenantName` (Liquid)
  - Outcomes: `Disabled`, `Failed`
- EnableTenantTask
  - Properties: `TenantName` (Liquid)
  - Outcomes: `Enabled`, `Failed`
- CreateTenantTask
  - Properties: `TenantName`, `Description`, `RequestUrlPrefix`, `RequestUrlHost`,
    `DatabaseProvider`, `ConnectionString`, `TablePrefix`, `Schema`,
    `RecipeName`, `FeatureProfile` (all Liquid)
  - Outcomes: `Done`, `Failed`
- SetupTenantTask
  - Properties: `TenantName`, `SiteName`, `AdminUsername`, `AdminEmail`, `AdminPassword`,
    `DatabaseProvider`, `DatabaseConnectionString`, `DatabaseTablePrefix`,
    `DatabaseSchema`, `RecipeName` (all Liquid)
  - Outcomes: `Done`, `Failed`

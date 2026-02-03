# Recipe Steps - Security and Identity

Steps for users, roles, and authentication-related settings.

## `Roles`
- Creates/updates roles and permissions.
- Shape:
```json
{ "name": "Roles", "Roles": [ { "Name": "Editor", "Permissions": [ "EditContent" ], "PermissionBehavior": "Add" } ] }
```

## `Users`
- Creates/updates users.
- Shape:
```json
{ "name": "Users", "Users": [ { "UserId": "...", "UserName": "...", "RoleNames": [ "Editor" ] } ] }
```

## `custom-user-settings`
- Updates per-user custom settings content items.

## OpenID and external auth
- `OpenIdApplication`, `OpenIdScope`, `OpenIdClientSettings`, `OpenIdServerSettings`, `OpenIdValidationSettings`
- `AzureADSettings`, `MicrosoftAccountSettings`, `GitHubAuthenticationSettings`, `FacebookLoginSettings`

## Social providers
- `FacebookCoreSettings`, `TwitterSettings`

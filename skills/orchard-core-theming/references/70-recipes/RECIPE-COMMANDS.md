# Recipe Commands

The `Command` step runs Orchard Core commands during recipe execution.
Commands are provided by modules and are defined in `*/Commands/*Commands.cs`.

## Command step shape
```json
{
  "name": "Command",
  "Commands": [
    "createUser /UserName:admin /Password:Passw0rd! /Email:admin@example.com /Roles:Administrator"
  ]
}
```

## Known commands (built-in)
- `createUser` (OrchardCore.Users)
  - Switches: `UserName`, `Password`, `Email`, `PhoneNumber`, `Roles`
- `recipes harvest` (OrchardCore.Recipes)
  - Lists available recipes

## How to discover commands
Search for `[CommandName("...")]` in `*/Commands/*Commands.cs`.
Commands use `/Switch:Value` syntax with `[OrchardSwitch]` properties.

## When to use Command vs Users step
- Use `Users` step for bulk import with full user properties.
- Use `Command` when you need quick creation with explicit switches.

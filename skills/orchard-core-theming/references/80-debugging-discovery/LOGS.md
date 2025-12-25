# Logs

## Logging tips
- Check `App_Data/logs/` in the host web project for runtime logs.
- Tenant-specific issues can appear in the same log stream; correlate by timestamp and tenant URL.
- Logging configuration is often in `NLog.config` or `appsettings*.json`.
- If logs are missing, verify `App_Data` exists and the app has write permissions.

## Useful runtime data
- `App_Data/tenants.json` shows tenant state and routing metadata.
- `App_Data/Sites/<TenantName>/` contains tenant-specific data and optional per-tenant `appsettings.json`.

# Create a Theme

Steps to scaffold a new Orchard Core theme and what files matter.

## Preferred: dotnet template
1) Ensure templates are installed (match your Orchard Core version):
   - `dotnet new install OrchardCore.ProjectTemplates::<version>`
   - If already installed, skip.
2) Scaffold:
   - `dotnet new octheme -n MyTheme -o src/Themes/MyTheme`
3) Add the project to your solution/host project and build.

Template output (key files):
- `MyTheme.csproj` (SDK-style, references OrchardCore theme targets)
- `Manifest.cs` (theme metadata)
- `Startup.cs` (optional; add services/resources if needed)
- `Views/Layout.cshtml` or `Layout.liquid` (fall back to Liquid if not specified by the user)
- `Views/_ViewImports.cshtml` (for if Razor is used)
- `wwwroot/` for static assets

## If templates are unavailable
1) Create a new Razor Class Library:
   - `dotnet new razorclasslib -n MyTheme -o src/Themes/MyTheme`
2) Edit `.csproj` to use the OrchardCore theme SDK:
   ```xml
   <Project Sdk="Microsoft.NET.Sdk.Razor">
     <PropertyGroup>
       <TargetFramework>net8.0</TargetFramework>
       <AddRazorSupportForMvc>true</AddRazorSupportForMvc>
     </PropertyGroup>
     <ItemGroup>
       <PackageReference Include="OrchardCore.Theme.Targets" Version="<matching-oc-version>" PrivateAssets="All" />
       <PackageReference Include="OrchardCore.DisplayManagement" Version="<matching-oc-version>" />
       <PackageReference Include="OrchardCore.ResourceManagement" Version="<matching-oc-version>" />
       <PackageReference Include="OrchardCore.Contents" Version="<matching-oc-version>" />
     </ItemGroup>
   </Project>
   ```
   (Adjust package path/version to your solution.)
3) Add `Manifest.cs`:
   ```csharp
   using OrchardCore.DisplayManagement.Manifest;
   [assembly: Theme(
       Name = "MyTheme",
       Author = "Org",
       Website = "https://example.com",
       Version = "1.0.0",
       Description = "Site theme",
       BaseTheme = "TheTheme" // optional
   )]
   ```
4) Add `Views/Layout.cshtml` (or `Layout.liquid`) and `Views/_ViewImports.cshtml` (Razor).
5) Add `wwwroot/` for assets; add `ResourceManifest.cs` if you need named resources.

## Minimal files checklist
- `Manifest.cs`: required metadata (Name, Version, optionally BaseTheme).
- `Layout` view: page shell with zones/sections.
- `Views/_ViewImports.cshtml` (Razor): include Orchard tag helpers.
- `Views` overrides: shapes you need to customize.
- `wwwroot/` assets: styles/scripts/images.
- `Startup.cs` (optional): register services, adjust options if needed.

## Scaffold examples
- `_ViewImports.cshtml` (Razor):
  ```cshtml
  @inherits OrchardCore.DisplayManagement.Razor.RazorPage<TModel>
  @addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers
  @addTagHelper *, OrchardCore.DisplayManagement
  @addTagHelper *, OrchardCore.ResourceManagement
  @addTagHelper *, OrchardCore.Contents
  ```
- `Views/Layout.cshtml` (minimal):
  ```cshtml
  <!DOCTYPE html>
  <html lang="@Orchard.CultureName()" dir="@Orchard.CultureDir()">
  <head>
      <meta charset="utf-8" />
      <title>@RenderTitleSegments(Site.SiteName, \"before\")</title>
      <style asp-name=\"MyTheme\" at=\"Head\"></style>
      <resources type=\"Header\" />
  </head>
  <body>
      <main class=\"container\">
          @await RenderSectionAsync(\"Messages\", required: false)
          @await RenderBodyAsync()
      </main>
      <resources type=\"FootScript\" />
  </body>
  </html>
  ```

## After scaffolding
- Add the project to the solution and reference it from the host app.
- Enable the theme feature in admin or via recipe (`feature` + `themes` steps).
- If using a base theme, override views/resources rather than editing the base.

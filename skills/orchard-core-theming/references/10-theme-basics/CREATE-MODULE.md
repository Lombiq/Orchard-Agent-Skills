# Create a Module

Steps to scaffold a new Orchard Core module and what files matter.

## Preferred: dotnet template
1) Ensure templates are installed (match your Orchard Core version):
   - `dotnet new install OrchardCore.ProjectTemplates::<version>`
2) Scaffold:
   - `dotnet new ocmodule -n MyModule -o src/Modules/MyModule`
3) Add the project to your solution/host project and build.

Template output (key files):
- `MyModule.csproj` (SDK-style, references OrchardCore module targets)
- `Manifest.cs` (module metadata/feature definitions)
- `Startup.cs` (inherits `StartupBase`; registers services/features)
- `Controllers/`, `Views/` (MVC)
- `Drivers/`, `Shapes/`, `Recipes/`, `Migrations/` folders as needed
- `ResourceManifest.cs` (optional; register scripts/styles)
- `Recipes/*.recipe.json` (optional; setup/content recipes)

## If templates are unavailable
1) Create a class library:
   - `dotnet new classlib -n MyModule -o src/Modules/MyModule`
2) Edit `.csproj` to use OrchardCore module SDK:
   ```xml
   <Project Sdk="Microsoft.NET.Sdk.Razor">
     <PropertyGroup>
       <TargetFramework>net8.0</TargetFramework>
       <AddRazorSupportForMvc>true</AddRazorSupportForMvc>
     </PropertyGroup>
     <ItemGroup>
       <PackageReference Include="OrchardCore.Module.Targets" Version="<matching-oc-version>" PrivateAssets="All" />
       <PackageReference Include="OrchardCore.DisplayManagement" Version="<matching-oc-version>" />
       <PackageReference Include="OrchardCore.ResourceManagement" Version="<matching-oc-version>" />
       <PackageReference Include="OrchardCore.Contents" Version="<matching-oc-version>" />
     </ItemGroup>
   </Project>
   ```
   (Adjust package path/version to your solution.)
3) Add `Manifest.cs`:
   ```csharp
   using OrchardCore.Modules.Manifest;
   [assembly: Module(
       Name = "MyModule",
       Author = "Org",
       Version = "1.0.0",
       Description = "Custom features"
   )]
   [assembly: Feature(
       Id = "MyModule",
       Name = "MyModule",
       Category = "Content",
       Description = "Custom features"
   )]
   ```
4) Add `Startup.cs`:
   ```csharp
   using Microsoft.Extensions.DependencyInjection;
   using OrchardCore.Modules;

   public class Startup : StartupBase
   {
       public override void ConfigureServices(IServiceCollection services)
       {
           // register services, drivers, etc.
       }
   }
   ```
5) Add folders as needed: `Controllers`, `Views`, `Drivers`, `Recipes`, `Migrations`, `ResourceManifest.cs`, `wwwroot/` for assets.

## Minimal files checklist
- `Manifest.cs`: module/feature metadata.
- `Startup.cs`: registers services/features.
- `Recipes/` (optional): setup/content recipes for your module.
- `ResourceManifest.cs` (optional): define resource names and dependencies.
- `wwwroot/` (optional): static assets.
- `Migrations/` (optional): data migrations, recipe migrations.

## After scaffolding
- Add the project to the solution and reference it from the host app.
- Enable the feature in admin or via recipe (`feature` step).
- Use recipes for repeatable setup (definitions, content, settings).

## Scaffold examples
- `_ViewImports.cshtml` (if you add Razor views):
  ```cshtml
  @inherits OrchardCore.DisplayManagement.Razor.RazorPage<TModel>
  @addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers
  @addTagHelper *, OrchardCore.DisplayManagement
  @addTagHelper *, OrchardCore.ResourceManagement
  @addTagHelper *, OrchardCore.Contents
  ```
- `Startup.cs`:
  ```csharp
  using Microsoft.Extensions.DependencyInjection;
  using OrchardCore.Modules;

  public class Startup : StartupBase
  {
      public override void ConfigureServices(IServiceCollection services)
      {
          // services.AddScoped<IDisplayDriver<ContentItem>, MyDriver>();
          // services.AddSingleton<IResourceManifestProvider, ResourceManifest>();
      }
  }
  ```

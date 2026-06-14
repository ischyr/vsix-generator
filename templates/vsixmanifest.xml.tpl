<?xml version="1.0" encoding="utf-8"?>
<PackageManifest Version="2.0.0"
 xmlns="http://schemas.microsoft.com/developer/vsx-schema/2011"
 xmlns:d="http://schemas.microsoft.com/developer/vsx-schema-design/2011">

  <Metadata>
    <Identity
      Id="{{publisher}}.{{name}}"
      Version="{{version}}"
      Publisher="{{publisher}}" />

    <DisplayName>{{displayName}}</DisplayName>
    <Description xml:space="preserve">{{description}}</Description>

    <Properties>
      <Property
        Id="Microsoft.VisualStudio.Code.Engine"
        Value="{{engines.vscode}}" />
    </Properties>
  </Metadata>

  <Installation>
    <InstallationTarget Id="Microsoft.VisualStudio.Code" />
  </Installation>

  <Dependencies />

  <Assets>
    <Asset
      Type="Microsoft.VisualStudio.Code.Manifest"
      Path="extension/package.json"
      Addressable="true" />
  </Assets>

</PackageManifest>

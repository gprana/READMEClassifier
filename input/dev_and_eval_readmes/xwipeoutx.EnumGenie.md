# EnumGenie
[![Build status](https://ci.appveyor.com/api/projects/status/x5f1ywgtd6cgmh5b/branch/master?svg=true)](https://ci.appveyor.com/project/xwipeoutx/enumgenie/branch/master) Master

[![Build status](https://ci.appveyor.com/api/projects/status/x5f1ywgtd6cgmh5b?svg=true)](https://ci.appveyor.com/project/xwipeoutx/enumgenie) CI

Generate enums matching your C# enums.  

Comes with generators for TypeScript.

## Installation

[EnumGenie is a nuget](https://www.nuget.org/packages/EnumGenie.TypeScript)! Crazy, I know.

```ps
    Install-Package EnumGenie.TypeScript
```

Or if you're targetting .NET Core (don't do this if you're on the full framework)

```ps
    Install-Package EnumGenie.TypeScript -Pre
```

## Documentation

See the [wiki](https://github.com/xwipeoutx/EnumGenie/wiki)

## Usage

See `EnumGenie.Sample` project for a ...umm... sample. Crazy.

```cs
public static class Program
{
    public static void Main()
    {
        var genie = new EnumGenie()
            .SourceFrom.Assembly(typeof(Program).Assembly)
            .FilterBy.Predicate(t => t != typeof(Ignored))
            .TransformBy.RenamingEnum(def => def.Name.Replace("StripThisOut", ""))
            .WriteTo.Console(cfg => cfg.TypeScript(ts => ts.Declaration().Description().Descriptor()))
            .WriteTo.File("c:\\temp\\enums.ts", cfg => cfg.TypeScript(ts => ts.Declaration().Description().Descriptor()));

        genie.Write();
    }
}
```

## Common Mistakes

### Nothing is being output!

Ensure you are calling `.Write()` at the end.  This is where the work is done, the rest is just configuration.

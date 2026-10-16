# src/Stashographer/Data/SqliteConnectionFactory.cs

- source repo: Wixely/Stashographer
- repo url: https://github.com/Wixely/Stashographer
- license: MIT
- created_at: 2026-08-18T03:19:36Z
- file path: src/Stashographer/Data/SqliteConnectionFactory.cs
- commit: e6568f9ca670f00ead30fe18c88491466eba11d1

```csharp
using System.Data;
using Microsoft.Data.Sqlite;

namespace Stashographer.Data;

public interface IDbConnectionFactory
{
    /// <summary>Creates and opens a new connection (with foreign keys enforced).</summary>
    Task<IDbConnection> OpenAsync(CancellationToken ct = default);
}

/// <summary>
/// Provider-agnostic seam over the connection string. SQLite today; swapping this and the
/// migration SQL dialect is the bulk of adding Postgres in phase 2.
/// </summary>
public class SqliteConnectionFactory(string connectionString) : IDbConnectionFactory
{
    public async Task<IDbConnection> OpenAsync(CancellationToken ct = default)
    {
        var conn = new SqliteConnection(connectionString);
        await conn.OpenAsync(ct);
        await using (var pragma = conn.CreateCommand())
        {
            pragma.CommandText = "PRAGMA foreign_keys = ON;";
            await pragma.ExecuteNonQueryAsync(ct);
        }
        return conn;
    }
}
```

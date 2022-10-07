using System.Diagnostics.CodeAnalysis;
using System.Globalization;

Console.WriteLine("Укажите путь до папки с фото(По умолчанию - данная директория)");
var path = Console.ReadLine() ?? ".";
path = path.Trim() == "" ? "." : path;
Dictionary<(string, string), string> filesMap = new Dictionary<(string, string), string>();
Console.WriteLine("Дубликаты: ");
foreach (var filePath in Directory.EnumerateFiles(path, "*.*", SearchOption.AllDirectories))
{
    var fileInfo = new FileInfo(filePath);
    if (filesMap.ContainsKey((fileInfo.Name, fileInfo.CreationTime.ToString(DateTimeFormatInfo.CurrentInfo))))
        Console.WriteLine(
            $"{fileInfo.FullName} {filesMap[(fileInfo.Name, fileInfo.CreationTime.ToString(CultureInfo.CurrentCulture))]}");
    else
        filesMap.Add((fileInfo.Name, fileInfo.CreationTime.ToString(CultureInfo.CurrentCulture)),
            fileInfo.FullName);
}

idiot: 
Console.WriteLine("Выберите период (d - day, w - week, m - month)");
var period = Console.ReadKey();
Dictionary<string, string[]> filesSorted = new Dictionary<string, string[]>();

foreach (var pair in filesMap.Keys)
{
    var createdTime = DateTime.Parse(pair.Item2);
    try
    {
        string key = period.Key switch
        {
            ConsoleKey.D => $"{createdTime.DayOfYear} {createdTime.Year}",
            ConsoleKey.W => $"{createdTime.DayOfYear / 7} {createdTime.Year}",
            ConsoleKey.M => $"{createdTime.Month} {createdTime.Year}",
            _ => throw new ArgumentOutOfRangeException()
        };
        if (filesSorted.ContainsKey(key))
        {
            filesSorted[key].Append(filesMap[pair]);
        }
        else 
            filesSorted[key] = new []{filesMap[pair]};
    }
    catch (ArgumentOutOfRangeException e)
    {
        goto idiot;
    }
}

var directoryInfo = Directory.CreateDirectory("sorted");
foreach (var dateString in filesSorted.Keys)
{
    (int what, int year) = dateString.Split().Select(s => int.Parse(s)).Take(2);
    string folderName = period.Key switch
    {
        ConsoleKey.D => $"{new DateTime(year, 1 , 1).AddDays(what - 1).ToShortDateString()}",
        ConsoleKey.W => $"{new DateTime(year, 1 , 1).AddDays(what * 7).ToShortDateString()} - {new DateTime(year, 1 , 1).AddDays(what * 7 + 7).ToShortDateString()}",
        ConsoleKey.M => $"{new DateTime(year, what , 1)} - {new DateTime(year, what , 1).AddMonths(1).AddDays(-1)}",
    };
    Directory.CreateDirectory(folderName);
    Directory.SetCurrentDirectory(folderName);
    
}
Вася Панков


Содержание
──────────

1. Лабораторная работа № 1
2. Дополнительные задания на работу с файловой системой
3. Лабораторная работа №3





1 Лабораторная работа № 1
═════════════════════════

  Тема: Создание приложения «Микропроводник».

  Цель работы: получение практических навыков при работе с пространством
  имен System.IO.

  Задание 1. Разработать приложение «Микропроводник», примерный вид
  которого представлен на Рисунке 1.

  Рисунок 1 – Приложение Микропроводник

  На форме список всех дисков загружается в компонент comboBox1.  Список
  всех каталогов для данного диска загружается в listBox1.  Список
  файлов, находящихся в выбранном каталоге, отображается listBox2.

  Задание 2. Используя дополнительные компоненты,
  • для выделенного диска необходимо выводить сведения: объем диска,
    свободное пространство;
  • для выделенного каталога: полное название каталога, время создания
    каталога, корневой каталог.

  Задание 3. При выделении файла в списке должно запускаться
  соответствующее приложение.

  Задание 4. Сохранить в отдельный текстовый файл имена файлов, которые
  открывались за последние 10 секунд работы приложения.

  Примечание. При выполнении задания необходимо работать с типом
  DateTime.

  `DateTime.Now' – возвращает текущее время;

  `Convert.ToDateTime' – преобразование строки в тип DateTime.

  Самостоятельно необходимо разобраться как работать с секундами.

  Решение:

  Разметка:
  ┌────
  │ <Window x:Class="WorkWithFiles.MainWindow"
  │ 	xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
  │ 	xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
  │ 	xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
  │ 	xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
  │ 	mc:Ignorable="d"
  │ 	Title="MainWindow" Height="500" Width="800"
  │ 	MinHeight="500" MinWidth="700">
  │     <Grid Margin="10, 0">
  │ 	<Grid.ColumnDefinitions>
  │ 	    <ColumnDefinition Width="*" />
  │ 	    <ColumnDefinition Width="2*" />
  │ 	    <ColumnDefinition Width="2*" />
  │ 	</Grid.ColumnDefinitions>
  │ 	<Grid.RowDefinitions>
  │ 	    <RowDefinition Height="*" />
  │ 	    <RowDefinition Height="3*" />
  │ 	    <RowDefinition Height="*" />
  │ 	</Grid.RowDefinitions>
  │ 	<TextBlock TextAlignment="Center" VerticalAlignment="Bottom" Margin="10">Диск:</TextBlock>
  │ 	<StackPanel Grid.Row="1" Grid.Column="0" Orientation="Vertical">
  │ 	    <ComboBox SelectionChanged="HardDrives_OnSelected" Name="HardDrivesComboBox" Height="20"
  │ 		      VerticalAlignment="Top" />
  │ 	    <TextBlock Name="HardDriveInformation" TextWrapping="Wrap" />
  │ 	</StackPanel>
  │ 	<TextBlock Grid.Row="0" Grid.Column="1" TextAlignment="Center" VerticalAlignment="Bottom" Margin="10">Каталоги:</TextBlock>
  │ 	<TextBlock Margin="10" Grid.Row="2" Grid.Column="1" Name="FolderInformation" DockPanel.Dock="Bottom"
  │ 		   TextWrapping="Wrap" />
  │ 	<ListBox Grid.Row="1" Grid.Column="1" VerticalAlignment="Stretch"
  │ 		 SelectionChanged="FoldersListBox_OnSelectionChanged" Name="FoldersListBox"
  │ 		 Margin="10, 0" />
  │ 
  │ 	<TextBlock Grid.Row="0" Grid.Column="2" TextAlignment="Center" VerticalAlignment="Bottom" Margin="10">Список файлов:</TextBlock>
  │ 	<ListBox Grid.Column="2" Name="FilesListBox" Grid.Row="1" SelectionMode="Single"
  │ 		 SelectionChanged="FilesListBox_OnSelectionChanged"
  │ 		 Margin="10, 0" />
  │     </Grid>
  │ </Window>
  └────


  <file:WorkWithFiles/1.png>

  Код приложения:

  ┌────
  │ using System;
  │ using System.Collections.Generic;
  │ using System.Diagnostics;
  │ using System.IO;
  │ using System.Linq;
  │ using System.Windows;
  │ using System.Windows.Controls;
  │ 
  │ namespace WorkWithFiles;
  │ 
  │ /// <summary>
  │ /// Interaction logic for MainWindow.xaml
  │ /// </summary>
  │ public partial class MainWindow : Window
  │ {
  │     public MainWindow()
  │     {
  │ 	// Создаём и очищаем файл
  │ 	var streamWriter = new StreamWriter("files.txt");
  │ 	streamWriter.Write("");
  │ 	streamWriter.Close();
  │ 	InitializeComponent();
  │ 	// Заполняем поле дисков
  │ 	foreach (var drive in DriveInfo.GetDrives())
  │ 	    HardDrivesComboBox.Items.Add(drive.Name);
  │ 	HardDrivesComboBox.SelectedIndex = 0;
  │     }
  │ 
  │     private void HardDrives_OnSelected(object sender, RoutedEventArgs e)
  │     {
  │ 	FoldersListBox.Items.Clear();
  │ 	FilesListBox.Items.Clear();
  │ 	var hardDrive = HardDrivesComboBox.SelectedItem.ToString()!;
  │ 	foreach (var directory in Directory.GetDirectories(hardDrive))
  │ 	    FoldersListBox.Items.Add(directory);
  │ 	// Получаем информацию о диске
  │ 	var driveInfo = DriveInfo.GetDrives().Where(info => info.Name == hardDrive).ToList()[0];
  │ 	HardDriveInformation.Text = @$"Объем диска: {driveInfo.TotalSize / (1024 * 1024)} MB
  │ Свободное пространство: {driveInfo.TotalFreeSpace / (1024 * 1024)} MB";
  │     }
  │ 
  │ 
  │     private void FoldersListBox_OnSelectionChanged(object sender, SelectionChangedEventArgs e)
  │     {
  │ 	FilesListBox.Items.Clear();
  │ 	FolderInformation.Text = "";
  │ 	try
  │ 	{
  │ 	    var path = FoldersListBox.SelectedItem.ToString()!;
  │ 	    var directoryInfo = new DirectoryInfo(path);
  │ 	    FolderInformation.Text = @$"Полное название каталога: {directoryInfo.Name}
  │ Время создания каталога: {directoryInfo.CreationTime}
  │ Корневой каталог: {directoryInfo.Parent?.Name ?? string.Empty}";
  │ 	    foreach (var file in Directory.GetFiles(path))
  │ 		FilesListBox.Items.Add(file);
  │ 	}
  │ 	catch (NullReferenceException)
  │ 	{
  │ 	    /* При очистке поле Selection сбрасывается и нас выкидывает сюда, так как стоит проверка на null */
  │ 	}
  │ 	catch (UnauthorizedAccessException)
  │ 	{
  │ 	    MessageBox.Show("Доступ запрещён к этой папке.");
  │ 	}
  │     }
  │ 
  │     /* На открытие любого файла или при закрытии приложения
  │      производим проверку все ли записанные файлы, открывались 10 секунд назад
  │      */
  │     private void fileOpened(string? path = null)
  │     {
  │ 	HashSet<(string, DateTime)> notDelete = new();
  │ 	if (path != null)
  │ 	    notDelete.Add((path, DateTime.Now));
  │ 	var streamReader = new StreamReader("files.txt");
  │ 	while (!streamReader.EndOfStream)
  │ 	{
  │ 	    var line = streamReader.ReadLine()!;
  │ 	    if (line.Trim() != "")
  │ 	    {
  │ 		var runnedTime = DateTime.Parse(line.Split(',')[1]);
  │ 		if (DateTime.Now - runnedTime < TimeSpan.FromSeconds(10))
  │ 		    notDelete.Add((line.Split(',')[0], runnedTime));
  │ 	    }
  │ 	}
  │ 
  │ 	streamReader.Close();
  │ 	var streamWriter = new StreamWriter("files.txt");
  │ 	foreach (var pair in notDelete)
  │ 	    streamWriter.WriteLine($"{pair.Item1},{pair.Item2}");
  │ 	streamWriter.Close();
  │     }
  │ 
  │     protected override void OnClosed(EventArgs e)
  │     {
  │ 	fileOpened();
  │ 	base.OnClosed(e);
  │     }
  │ 
  │     private void FilesListBox_OnSelectionChanged(object sender, SelectionChangedEventArgs e)
  │     {
  │ 	try
  │ 	{
  │ 	    var path = FilesListBox.SelectedItem.ToString()!;
  │ 	    new Process
  │ 	    {
  │ 		StartInfo = new ProcessStartInfo(path)
  │ 		{
  │ 		    UseShellExecute = true
  │ 		}
  │ 	    }.Start();
  │ 	    fileOpened(path);
  │ 	    FilesListBox.SelectedItem = null;
  │ 	}
  │ 	catch (NullReferenceException)
  │ 	{
  │ 	}
  │     }
  │ }
  └────

  Демонстрация работы приложения:

  <file:WorkWithFiles/2.png>

  Выбран диск:

  <file:WorkWithFiles/3.png>

  Выбрана папка:

  <file:WorkWithFiles/4.png>

  Обработка ошибки с доступом:

  <file:WorkWithFiles/5.png>

  Открытие файла(`py.exe')

  <file:WorkWithFiles/6.png>

  Запись открытия данного файла:

  <file:WorkWithFiles/7.png>

  Итог работы:

  Получил практические навыки при работе с пространством имен System.IO,
  а также создал приложение "Микропроводник".


2 Дополнительные задания на работу с файловой системой
══════════════════════════════════════════════════════

  Задание 1(фрагмент модуля задания по компетенции Программные решения
  для бизнеса(2018 год)).Вы являетесь разработчиком в команде, которая
  занимается проектированием и разработкой настольных приложений,
  взаимодействующих с БД. Технические сложности пока не дают возможности
  работать с БД в полном объеме. Поэтому список фотографий для загрузки
  на форму необходимо брать из конкретной папки. Содержимое папки будет
  изменяться, поэтому не делайте «жесткой » привязки по полному пути к
  фото. Есть вероятность, что данная папка со временем будет иметь
  структуру подпапок. В этом случае поиск файлов необходимо делать во
  всех подпапках и формировать список загружаемых фото по результатам
  этого поиска. Вы разрабатываете модуль, в котором загрузка фото из
  папок на форме оформлена в виде слайдера- по 3 фото за 1 раз. Смена
  фото происходит по нажатию соответствующих кнопок. Макет формы
  представлен на рисунке 1. Алгоритм изменения изображений должен
  работать таким образом, чтобы учесть случай, когда количество фото не
  кратно 3. В этом случае,в последней группе из 2-х фото добавится самое
  первое фото в папке(сдвиг произойдет на 1 позицию) и т.д.

  <file:NbaApp/1.png>

  Для выполнения задания используйте папки с ресурсами – папку logo и
  папку Pictures.

  Код:

  Разметка:

  ┌────
  │ <Window x:Class="NbaApp.MainWindow"
  │ 	xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
  │ 	xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
  │ 	xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
  │ 	xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
  │ 	mc:Ignorable="d"
  │ 	Title="MainWindow" Height="450" Width="800"
  │ 	MinHeight="500" MinWidth="800">
  │     <Grid>
  │ 	<Grid.ColumnDefinitions>
  │ 	    <ColumnDefinition />
  │ 	    <ColumnDefinition />
  │ 	    <ColumnDefinition />
  │ 	    <ColumnDefinition />
  │ 	</Grid.ColumnDefinitions>
  │ 	<Grid.RowDefinitions>
  │ 	    <RowDefinition />
  │ 	    <RowDefinition />
  │ 	    <RowDefinition />
  │ 	    <RowDefinition />
  │ 	    <RowDefinition Height="20" />
  │ 	</Grid.RowDefinitions>
  │ 
  │ 	<Image HorizontalAlignment="Left" VerticalAlignment="Top" Margin="10" Source="res/logo/logo.jpg" />
  │ 	<TextBlock FontSize="22" FontWeight="Medium" Grid.ColumnSpan="2" HorizontalAlignment="Center"
  │ 		   VerticalAlignment="Center" Grid.Column="1">
  │ 	    NBA Management System
  │ 	</TextBlock>
  │ 	<TextBlock Grid.Row="1" Grid.Column="1" Grid.ColumnSpan="2" FontSize="18" TextWrapping="Wrap"
  │ 		   VerticalAlignment="Top" HorizontalAlignment="Center" TextAlignment="Center">
  │ 	    Welcome  to use this NBA Management system, you can redirect to different pages according to your role by clicking the buttons bellow
  │ 	</TextBlock>
  │ 	<Button Grid.Column="1" VerticalAlignment="Top" Margin="30" Foreground="White" Grid.Row="2">
  │ 	    <TextBlock Margin="10">
  │ 		<Run Foreground="White">
  │ 		    Visitor
  │ 		</Run>
  │ 	    </TextBlock>
  │ 	</Button>
  │ 	<Button Grid.Column="2" Margin="30" VerticalAlignment="Top" Foreground="White" Grid.Row="2">
  │ 	    <TextBlock Margin="10">
  │ 		<Run Foreground="White">
  │ 		    Admin
  │ 		</Run>
  │ 	    </TextBlock>
  │ 	</Button>
  │ 
  │ 	<Grid Margin="10" Grid.Row="3" Grid.ColumnSpan="4">
  │ 	    <Grid.ColumnDefinitions>
  │ 		<ColumnDefinition Width="*" />
  │ 		<ColumnDefinition Width="7*" />
  │ 		<ColumnDefinition Width="*" />
  │ 	    </Grid.ColumnDefinitions>
  │ 	    <Grid Grid.Column="1">
  │ 		<Grid.ColumnDefinitions>
  │ 		    <ColumnDefinition />
  │ 		    <ColumnDefinition />
  │ 		    <ColumnDefinition />
  │ 		</Grid.ColumnDefinitions>
  │ 		<Image Margin="10, 0" Source="{Binding Img1}" />
  │ 		<Image Margin="10, 0" Grid.Column="1" Source="{Binding Img2}" />
  │ 		<Image Margin="10, 0" Grid.Column="2" Source="{Binding Img3}" />
  │ 
  │ 	    </Grid>
  │ 
  │ 	    <Button Click="Left" Width="48" Height="48">
  │ 		<Button.Resources>
  │ 		    <Style TargetType="{x:Type Border}">
  │ 			<Setter Property="CornerRadius" Value="123" />
  │ 		    </Style>
  │ 		</Button.Resources>
  │ 		<Image Source="res/ui/left.png" Margin="3" />
  │ 	    </Button>
  │ 	    <Button Click="Right" Width="48" Height="48" Grid.Column="3">
  │ 		<Button.Resources>
  │ 		    <Style TargetType="{x:Type Border}">
  │ 			<Setter Property="CornerRadius" Value="123" />
  │ 		    </Style>
  │ 		</Button.Resources>
  │ 		<Image Source="res/ui/right.png" Margin="3" />
  │ 	    </Button>
  │ 	</Grid>
  │ 	<TextBlock Background="#8b89a4" Foreground="White" HorizontalAlignment="Stretch" TextAlignment="Center"
  │ 		   Grid.Row="4" Grid.ColumnSpan="4" FontSize="10">
  │ 	    The current season is 2016-2017, and the NBA already has a history of 71 years.
  │ 	</TextBlock>
  │     </Grid>
  │ </Window>
  └────

  <file:NbaApp/2.png>


  MainWindow.cs
  ┌────
  │ using System;
  │ using System.Collections.Generic;
  │ using System.Linq;
  │ using System.Text;
  │ using System.Threading.Tasks;
  │ using System.Windows;
  │ using System.Windows.Controls;
  │ using System.Windows.Data;
  │ using System.Windows.Documents;
  │ using System.Windows.Input;
  │ using System.Windows.Media;
  │ using System.Windows.Media.Imaging;
  │ using System.Windows.Navigation;
  │ using System.Windows.Shapes;
  │ 
  │ namespace NbaApp;
  │ 
  │ /// <summary>
  │ /// Interaction logic for MainWindow.xaml
  │ /// </summary>
  │ public partial class MainWindow : Window
  │ {
  │     private Images _images = new();
  │ 
  │     public MainWindow()
  │     {
  │ 	DataContext = _images;
  │ 	InitializeComponent();
  │     }
  │ 
  │     private void Right(object sender, RoutedEventArgs e)
  │     {
  │ 	_images.Right();
  │     }
  │ 
  │     private void Left(object sender, RoutedEventArgs e)
  │     {
  │ 	_images.Left();
  │     }
  │ }
  └────

  Images.cs
  ┌────
  │ using System;
  │ using System.Collections.Generic;
  │ using System.IO;
  │ using System.Linq;
  │ 
  │ namespace NbaApp;
  │ 
  │ public class Images : ViewModel
  │ {
  │     // Путь до картинок
  │     private const string PATH = @"C:\Users\user\Desktop\NbaApp\NbaApp\res\";
  │     private string[] _showedImages;
  │ 
  │     private int _index = 0;
  │ 
  │     // Получаем все картинки из подпапок, а также их фильтруем по *.jpg
  │     private List<string> _images = Directory.EnumerateFiles(PATH, "*.jpg", SearchOption.AllDirectories).ToList();
  │ 
  │     // Параметры для binding
  │     public string Img1
  │     {
  │ 	get => _showedImages[0];
  │ 	set => _showedImages[0] = value;
  │     }
  │ 
  │     public string Img2
  │     {
  │ 	get => _showedImages[1];
  │ 	set => _showedImages[1] = value;
  │     }
  │ 
  │     public string Img3
  │     {
  │ 	get => _showedImages[2];
  │ 	set => _showedImages[2] = value;
  │     }
  │ 
  │     public Images()
  │     {
  │ 	ShowImages();
  │     }
  │ 
  │     // Функция отображения картинок по индексу
  │     private void ShowImages()
  │     {
  │ 	if (_images.Count == 0)
  │ 	    return;
  │ 
  │ 	// Если у нас одна картинка просто зацикливаем одну картинку  и наплевать на индексы
  │ 	if (_images.Count == 1)
  │ 	    _showedImages = new[] {_images[0], _images[0], _images[0]};
  │ 	else if (_index + 3 >= _images.Count)
  │ 	{
  │ 	    var list_ = _images.GetRange(_index, _images.Count - _index);
  │ 	    list_.AddRange(_images.GetRange(0, 3 - (_images.Count - _index)));
  │ 	    _showedImages = list_.ToArray();
  │ 	}
  │ 	else
  │ 	{
  │ 	    _showedImages = _images.GetRange(_index, 3).ToArray();
  │ 	}
  │ 
  │ 	// Уведомление WPF о измененения в этих Properties
  │ 	NotifyPropertyChanged("Img1");
  │ 	NotifyPropertyChanged("Img2");
  │ 	NotifyPropertyChanged("Img3");
  │     }
  │ 
  │     // Высчитываем новый индекс при листании вправо и меняем картинки
  │     public void Right()
  │     {
  │ 	if (_images.Count == 0)
  │ 	    return;
  │ 
  │ 	// Если индекс превышает допустимое значение, получаем новый цикличный индекс, иначе просто листаем на 3
  │ 	if (_index + 3 >= _images.Count)
  │ 	    _index = 3 - (_images.Count - _index);
  │ 	else
  │ 	    _index += 3;
  │ 	/* Cуществует ошибка если индекс меньше 3, то мы не получаем новый корректно(вычитание из тройки),
  │ 	 это исправляет ошибку*/
  │ 	if (_images.Count < 3 && _index == _images.Count)
  │ 	    _index = 0;
  │ 	ShowImages();
  │     }
  │ 
  │     // Высчитываем новый индекс при листании влево и меняем картинки
  │     public void Left()
  │     {
  │ 	if (_images.Count == 0)
  │ 	    return;
  │ 	if (_index - 3 <= 0)
  │ 	    _index = Math.Abs(_images.Count + (_index - 3));
  │ 	else
  │ 	    _index -= 3;
  │ 	ShowImages();
  │     }
  │ }
  └────

  ViewModel.cs
  ┌────
  │ using System.ComponentModel;
  │ 
  │ namespace NbaApp;
  │ 
  │ // Крутой класс для уведомления WPF, что Property изменилось
  │ public abstract class ViewModel : INotifyPropertyChanged
  │ {
  │     public event PropertyChangedEventHandler? PropertyChanged;
  │ 
  │     protected void NotifyPropertyChanged(string propertyName)
  │     {
  │ 	if (PropertyChanged != null)
  │ 	    PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
  │     }
  │ }
  └────

  Демонстрация работы приложения:

  Картинки используемые в приложении:

  <file:NbaApp/3.png>

  <file:NbaApp/4.png>

  <file:NbaApp/5.png>

  <file:NbaApp/6.png>

  <file:NbaApp/7.png>

  Задание 2.(фрагмент модуля задания по компетенции Программные решения
  для бизнеса(2017 год), overdrive на 30 минут).

  <file:WorldSkillsApp/1.png>

  Код:

  ┌────
  │ using System.Globalization;
  │ 
  │ Console.WriteLine("Укажите путь до папки с фото(По умолчанию - данная директория)");
  │ var path = Console.ReadLine() ?? ".";
  │ path = path.Trim() == "" ? "." : path;
  │ Dictionary<(string, string), string> filesMap = new Dictionary<(string, string), string>();
  │ Console.WriteLine("Дубликаты: ");
  │ foreach (var filePath in Directory.EnumerateFiles(path, "*.*", SearchOption.AllDirectories))
  │ {
  │     var fileInfo = new FileInfo(filePath);
  │     if (filesMap.ContainsKey((fileInfo.Name, fileInfo.CreationTime.ToString(DateTimeFormatInfo.CurrentInfo))))
  │ 	Console.WriteLine(
  │ 	    $"{fileInfo.FullName} {filesMap[(fileInfo.Name, fileInfo.CreationTime.ToString(CultureInfo.CurrentCulture))]}");
  │     else
  │ 	filesMap.Add((fileInfo.Name, fileInfo.CreationTime.ToString(CultureInfo.CurrentCulture)),
  │ 	    fileInfo.FullName);
  │ }
  │ 
  │ idiot:
  │ Console.WriteLine("Выберите период (d - day, w - week, m - month)");
  │ var period = Console.ReadKey();
  │ Dictionary<string, List<string>> filesSorted = new Dictionary<string, List<string>>();
  │ 
  │ foreach (var pair in filesMap.Keys)
  │ {
  │     var createdTime = DateTime.Parse(pair.Item2);
  │     try
  │     {
  │ 	string key = period.Key switch
  │ 	{
  │ 	    ConsoleKey.D => $"{createdTime.DayOfYear} {createdTime.Year}",
  │ 	    ConsoleKey.W => $"{createdTime.DayOfYear / 7} {createdTime.Year}",
  │ 	    ConsoleKey.M => $"{createdTime.Month} {createdTime.Year}",
  │ 	    _ => throw new ArgumentOutOfRangeException()
  │ 	};
  │ 	if (filesSorted.ContainsKey(key))
  │ 	{
  │ 	    filesSorted[key].Add(filesMap[pair]);
  │ 	}
  │ 	else
  │ 	    filesSorted[key] = new List<string>() {filesMap[pair]};
  │     }
  │     catch (ArgumentOutOfRangeException e)
  │     {
  │ 	goto idiot;
  │     }
  │ }
  │ 
  │ Directory.SetCurrentDirectory(path);
  │ Directory.CreateDirectory("sorted");
  │ Directory.SetCurrentDirectory("sorted");
  │ foreach (var dateString in filesSorted.Keys)
  │ {
  │     var ints = dateString.Split().Select(s => int.Parse(s)).ToArray();
  │     (int what, int year) = (ints[0], ints[1]);
  │     string folderName = period.Key switch
  │     {
  │ 	ConsoleKey.D => $"{new DateTime(year, 1, 1).AddDays(what - 1).ToShortDateString().Replace("/", "-")}",
  │ 	ConsoleKey.W => new DateTime(year, 1, 1).AddDays(what * 7).ToShortDateString().Replace("/", "-") + " - " +
  │ 			new DateTime(year, 1, 1).AddDays(what * 7 + 7).ToShortDateString().Replace("/", "-"),
  │ 	ConsoleKey.M =>
  │ 	    $"{new DateTime(year, what, 1).ToShortDateString().Replace("/", "-")} - {new DateTime(year, what, 1).AddMonths(1).AddDays(-1).ToShortDateString().Replace("/", "-")}",
  │     };
  │     Console.WriteLine(folderName);
  │     Directory.CreateDirectory(folderName);
  │     foreach (var filePath in filesSorted[dateString])
  │     {
  │ 	int fileRepeat = 0;
  │ 	again:
  │ 	try
  │ 	{
  │ 	    var newFileName = new FileInfo(filePath).Name.Split('.')[0] + (fileRepeat == 0 ? "" : fileRepeat.ToString()) + "." +
  │ 			      new FileInfo(filePath).Name.Split('.')[1];
  │ 	    File.Copy(filePath, folderName + "\\" + newFileName);
  │ 	}
  │ 	catch (System.IO.IOException e)
  │ 	{
  │ 	    fileRepeat++;
  │ 	    goto again;
  │ 	}
  │     }
  │ }
  └────

  Демонстрация работы:


  Содержимое папок:

  <file:WorldSkillsApp/2.png>

  Результат работы:

  <file:WorldSkillsApp/3.png>

  По дням:

  <file:WorldSkillsApp/4.png>

  По неделям:

  <file:WorldSkillsApp/5.png>

  Все картинки, так как они были созданы в эту неделю - главное это
  название папки(10-8-2022 - 10-15-2022)

  По месяцам:

  <file:WorldSkillsApp/6.png>


3 Лабораторная работа №3
════════════════════════

  Тема: Создание собственных классов в C#.  Цель работы: получение
  практических навыков при создании и наследовании классов в C#.

  Выполнение работы:

  Задание 1. Создание классов по вариантам.

  12 вариант

  Создать класс квадратная матрица, поля класса – размерность и элементы
  матрицы. Методы класса: проверка, является ли матрица
  верхнетреугольной или нижнетреугольной, вывод матрицы. В классе
  предусмотреть методы: сложение, вычитание, умножение матриц, умножение
  матрицы на число.

  Код:

  ┌────
  │ using System;
  │ using System.Collections.Generic;
  │ using System.Linq;
  │ 
  │ namespace MyClasses;
  │ 
  │ /* Создать класс квадратная матрица, поля класса – размерность и элементы матрицы.
  │  Методы класса: проверка, является ли матрица верхнетреугольной или нижнетреугольной, вывод матрицы. 
  │  В классе предусмотреть методы: сложение, вычитание, умножение матриц, умножение матрицы на число. */
  │ 
  │ public class SquareMatrix
  │ {
  │     // Размерность матрицы
  │     private int _n;
  │ 
  │     public int N
  │     {
  │ 	get => _n;
  │ 	set
  │ 	{
  │ 	    if (value <= 0)
  │ 		throw new Exception("Размерность матрицы должна быть больше 0");
  │ 	    _n = value;
  │ 	}
  │     }
  │ 
  │     // Список содержащий элементы матрицы
  │     private List<List<int>> _matrixList = null!;
  │ 
  │     public List<List<int>> MatrixList
  │     {
  │ 	get => _matrixList;
  │ 	set
  │ 	{
  │ 	    if (value.Count != N || value[0].Count != N)
  │ 		throw new Exception("Вводимая матрица неподходит по размерности");
  │ 	    _matrixList = value;
  │ 	}
  │     }
  │ 
  │     public List<int> this[int i]
  │     {
  │ 	get { return MatrixList[i]; }
  │ 	set
  │ 	{
  │ 	    if (value.Count != N)
  │ 		throw new Exception("Вводимая строка неподходит по размерности");
  │ 	    MatrixList[i] = value;
  │ 	}
  │     }
  │ 
  │     public SquareMatrix(int n)
  │     {
  │ 	N = n;
  │ 	var matrixList = new List<List<int>>();
  │ 	for (int i = 0; i < n; i++)
  │ 	{
  │ 	    matrixList.Add(new List<int>());
  │ 	    for (int j = 0; j < n; j++)
  │ 	    {
  │ 		matrixList.Last().Add(0);
  │ 	    }
  │ 	}
  │ 
  │ 	MatrixList = matrixList;
  │     }
  │ 
  │     public SquareMatrix(int n, List<List<int>> matrixList)
  │     {
  │ 	N = n;
  │ 	MatrixList = matrixList;
  │     }
  │ 
  │     public override string ToString()
  │     {
  │ 	string output = "[\n";
  │ 	foreach (var list in MatrixList)
  │ 	{
  │ 	    output += '\t' + String.Join('\t', list) + '\n';
  │ 	}
  │ 
  │ 	output += "]";
  │ 	return output;
  │     }
  │ 
  │     // Это верхняя треугольная матрица?
  │     public bool IsUpperTriangular()
  │     {
  │ 	for (int i = 0; i < N; i++)
  │ 	{
  │ 	    for (int j = 0; j < i; j++)
  │ 	    {
  │ 		if (MatrixList[i][j] != 0)
  │ 		    return false;
  │ 	    }
  │ 	}
  │ 
  │ 	return true;
  │     }
  │ 
  │     // Это нижняя треугольная матрица?
  │     public bool IsBottomTriangular()
  │     {
  │ 	for (int i = 0; i < N; i++)
  │ 	{
  │ 	    for (int j = N - 1; j > i; j--)
  │ 	    {
  │ 		if (MatrixList[i][j] != 0)
  │ 		    return false;
  │ 	    }
  │ 	}
  │ 
  │ 	return true;
  │     }
  │ 
  │     // Сложение матриц
  │     public static SquareMatrix operator +(SquareMatrix squareMatrix, SquareMatrix squareMatrix2)
  │     {
  │ 	if (squareMatrix2.N != squareMatrix.N)
  │ 	    throw new Exception("Матрицы не совпадают по размерности");
  │ 	var newMatrix = new SquareMatrix(squareMatrix.N);
  │ 	for (int i = 0; i < squareMatrix.N; i++)
  │ 	{
  │ 	    for (int j = 0; j < squareMatrix.N; j++)
  │ 		newMatrix[i][j] = squareMatrix[i][j] + squareMatrix2[i][j];
  │ 	}
  │ 
  │ 	return newMatrix;
  │     }
  │ 
  │     // Вычитание матриц
  │     public static SquareMatrix operator -(SquareMatrix squareMatrix, SquareMatrix squareMatrix2)
  │     {
  │ 	if (squareMatrix2.N != squareMatrix.N)
  │ 	    throw new Exception("Матрицы не совпадают по размерности");
  │ 	var newMatrix = new SquareMatrix(squareMatrix.N);
  │ 	for (int i = 0; i < squareMatrix.N; i++)
  │ 	{
  │ 	    for (int j = 0; j < squareMatrix.N; j++)
  │ 		newMatrix[i][j] = squareMatrix[i][j] - squareMatrix2[i][j];
  │ 	}
  │ 
  │ 	return newMatrix;
  │     }
  │ 
  │     // Умножение матрицы на число
  │     public static SquareMatrix operator *(SquareMatrix squareMatrix, int n)
  │     {
  │ 	var newMatrix = new SquareMatrix(squareMatrix.N);
  │ 	for (int i = 0; i < squareMatrix.N; i++)
  │ 	{
  │ 	    for (int j = 0; j < squareMatrix.N; j++)
  │ 		newMatrix[i][j] = squareMatrix[i][j] * n;
  │ 	}
  │ 
  │ 	return newMatrix;
  │     }
  │ 
  │     // Перемножение матриц
  │     public static SquareMatrix operator *(SquareMatrix squareMatrix, SquareMatrix squareMatrix2)
  │     {
  │ 	if (squareMatrix2.N != squareMatrix.N)
  │ 	    throw new Exception("Матрицы не совпадают по размерности");
  │ 	var newMatrix = new SquareMatrix(squareMatrix.N);
  │ 	for (int i = 0; i < squareMatrix.N; i++)
  │ 	{
  │ 	    for (int j = 0; j < squareMatrix.N; j++)
  │ 	    {
  │ 		int cellValue = 0;
  │ 		for (int j1 = 0; j1 < squareMatrix.N; j1++)
  │ 		{
  │ 		    cellValue += squareMatrix[i][j1] * squareMatrix2[j1][j];
  │ 		}
  │ 
  │ 		newMatrix[i][j] = cellValue;
  │ 	    }
  │ 	}
  │ 
  │ 	return newMatrix;
  │     }
  │ }
  └────


  Код тестов:

  ┌────
  │ using System;
  │ using System.Collections.Generic;
  │ using NUnit.Framework;
  │ 
  │ namespace MyClasses;
  │ 
  │ public class SquareMatrixTests
  │ {
  │     [Test]
  │     public void InitTest()
  │     {
  │ 	var matrix = new SquareMatrix(2);
  │ 	List<List<int>> myMatrixList = new List<List<int>>();
  │ 	myMatrixList.Add(new List<int>() {0, 0});
  │ 	myMatrixList.Add(new List<int>() {0, 0});
  │ 	Assert.AreEqual(matrix.MatrixList, myMatrixList);
  │ 	myMatrixList[0][0] = 1;
  │ 	var matrix2 = new SquareMatrix(2, myMatrixList);
  │ 	Assert.AreEqual(matrix2.MatrixList, myMatrixList);
  │     }
  │ 
  │     [Test]
  │     public void StringTest()
  │     {
  │ 	Assert.AreEqual(new SquareMatrix(1).ToString(), "[\n\t0\n]");
  │ 	Console.WriteLine(new SquareMatrix(10).ToString());
  │     }
  │ 
  │     [Test]
  │     public void TriangularTest()
  │     {
  │ 	List<List<int>> myMatrixList = new List<List<int>>();
  │ 	myMatrixList.Add(new List<int>() {1, 0});
  │ 	myMatrixList.Add(new List<int>() {1, 1});
  │ 	var matrix = new SquareMatrix(2, myMatrixList);
  │ 	Assert.IsFalse(matrix.IsUpperTriangular());
  │ 	Assert.IsTrue(matrix.IsBottomTriangular());
  │ 	myMatrixList = new List<List<int>>();
  │ 	myMatrixList.Add(new List<int>() {1, 0, 1});
  │ 	myMatrixList.Add(new List<int>() {0, 1, 0});
  │ 	myMatrixList.Add(new List<int>() {0, 0, 1});
  │ 	matrix = new SquareMatrix(3, myMatrixList);
  │ 	Assert.IsTrue(matrix.IsUpperTriangular());
  │ 	Assert.IsFalse(matrix.IsBottomTriangular());
  │     }
  │ 
  │     class MathTests
  │     {
  │ 	[Test]
  │ 	public void MatrixAdditionTest()
  │ 	{
  │ 	    List<List<int>> myMatrixList = new List<List<int>>();
  │ 	    myMatrixList.Add(new List<int>() {1, 0});
  │ 	    myMatrixList.Add(new List<int>() {1, 1});
  │ 	    var matrix = new SquareMatrix(2, myMatrixList);
  │ 
  │ 	    Assert.AreEqual((matrix + matrix)[0], new List<int>() {2, 0});
  │ 	    Assert.AreEqual((matrix + matrix)[1], new List<int>() {2, 2});
  │ 	    Assert.AreEqual((matrix - matrix - matrix)[0], new List<int>() {-1, 0});
  │ 	    Assert.AreEqual((matrix - matrix - matrix)[1], new List<int>() {-1, -1});
  │ 	}
  │ 
  │ 	[Test]
  │ 	public void ScalarMultiplication()
  │ 	{
  │ 	    List<List<int>> myMatrixList = new List<List<int>>();
  │ 	    myMatrixList.Add(new List<int>() {1, 2});
  │ 	    myMatrixList.Add(new List<int>() {3, 4});
  │ 	    var matrix = new SquareMatrix(2, myMatrixList);
  │ 	    Assert.AreEqual((matrix * 5)[0], new List<int>() {5, 10});
  │ 	    Assert.AreEqual((matrix * 5)[1], new List<int>() {15, 20});
  │ 	}
  │ 
  │ 	[Test]
  │ 	public void Multiplication()
  │ 	{
  │ 	    List<List<int>> myMatrixList = new List<List<int>>();
  │ 	    myMatrixList.Add(new List<int>() {1, 2});
  │ 	    myMatrixList.Add(new List<int>() {3, 4});
  │ 	    var matrix = new SquareMatrix(2, myMatrixList);
  │ 	    Assert.AreEqual((matrix * matrix)[0], new List<int>() {7, 10});
  │ 	    Assert.AreEqual((matrix * matrix)[1], new List<int>() {15, 22});
  │ 	    myMatrixList = new List<List<int>>();
  │ 	    myMatrixList.Add(new List<int>() {1, 2, 3});
  │ 	    myMatrixList.Add(new List<int>() {1, 2, 3});
  │ 	    myMatrixList.Add(new List<int>() {1, 2, 3});
  │ 	    matrix = new SquareMatrix(3, myMatrixList);
  │ 	    Assert.AreEqual((matrix * matrix)[0], new List<int>() {6, 12, 18});
  │ 	    Assert.AreEqual((matrix * matrix)[1], new List<int>() {6, 12, 18});
  │ 	    Assert.AreEqual((matrix * matrix)[2], new List<int>() {6, 12, 18});
  │ 	}
  │ 
  │ 	[Test]
  │ 	public void ExtraTest()
  │ 	{
  │ 	    List<List<int>> myMatrixList = new List<List<int>>();
  │ 	    myMatrixList.Add(new List<int>() {1, 2});
  │ 	    myMatrixList.Add(new List<int>() {3, 4});
  │ 	    var matrix = new SquareMatrix(2, myMatrixList);
  │ 	    matrix = ((matrix + matrix) * 2 - matrix) * matrix;
  │ 	    Assert.AreEqual(matrix[0], new List<int>() {21, 30});
  │ 	    Assert.AreEqual(matrix[1], new List<int>() {45, 66});
  │ 	}
  │ 
  │     }
  │ }
  └────

  Результаты тестирования:

  <file:MyClasses/1.jpg>

  Задание 2.  Создать класс Пароль. Поле класса – пароль. Метод класса –
  проверка пароля с выводом информационного сообщения: «Пароль верный»
  или «Пароль неверный». Для простоты пароль будет задаваться
  программистом в основной программе. Создать класс Надежный пароль,
  который является потомком класса Пароль и имеет собственный метод
  анализа надежности пароля:
  • Пароль должен состоять не менее чем из 8 символов(слабый)
  • Пароль должен содержать как маленькие, так и большие латинские
    буквы(средний)
  • Пароль должен содержать хотя бы одну цифру(хороший)
  • Пароль должен содержать хотя бы один символ(!, $, #, %)(надежный)
  В основной программе:
  1) подключить модуль с описанными классами;
  2) разместить на форме текстовое поле для ввода пароля;
  3) в обработчике события кнопки Проверка реализовать работу с
     созданными классами.
  Усложнение. Создать класс Шифр – наследник класса Пароль. Методы
  класса – Шифрование и Дешифрование пароля с использованием «Шифра
  Цезаря».

  Шифр Цезаря, также известный как шифр сдвига, код Цезаря или сдвиг
  Цезаря — один из самых простых и наиболее широко известных методов
  шифрования.

  Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в
  открытом тексте заменяется символом, находящимся на некотором
  постоянном числе позиций левее или правее него в алфавите. Например, в
  шифре со сдвигом вправо на 3, А была бы заменена на Г, Б станет Д, и
  так далее.

  В основной программе реализовать следующие функции с использованием
  класса Шифр:
  1) В текстовое поле вводится пароль для шифрования и в зашифрованном
     виде записывается в текстовый файл.
  2) Перед проверкой пароля его необходимо считать из файла и
     дешифровать.


  Код:

  • Библиотека PasswordLibrary

    • Password.cs (Класс пароль)

      ┌────
      │ namespace PasswordLibrary;
      │ 
      │ public class Password
      │ {
      │     protected string _password;
      │ 
      │     public Password(string password)
      │     {
      │ 	_password = password;
      │     }
      │ 
      │     public bool CheckPassword(string password)
      │     {
      │ 	return password == _password;
      │     }
      │ }
      └────

    • PasswordType.cs (перечисление типов паролей)

      ┌────
      │ namespace PasswordLibrary;
      │ 
      │ public enum PasswordType
      │ {
      │     Bad,
      │     Weak,
      │     Medium,
      │     Good,
      │     Strong
      │ }
      └────

    • StrongPassword.cs (определение вида пароля)

      ┌────
      │ using System.Text.RegularExpressions;
      │ 
      │ namespace PasswordLibrary;
      │ 
      │ public class StrongPassword : Password
      │ {
      │     public Dictionary<PasswordType, string> TypeToPattern = new()
      │     {
      │ 	{PasswordType.Bad, @"[\S]{0,8}"},
      │ 	{PasswordType.Weak, @"[\S]{8,}"},
      │ 	{PasswordType.Medium, @"(?=.*[A-Z])(?=.*[a-z])(?=\S{8,})"},
      │ 	{PasswordType.Good, @"(?=.*[A-Z])(?=.*[a-z])(?=\S{8,})(?=.*[0-9])"},
      │ 	{PasswordType.Strong, @"(?=.*[A-Z])(?=.*[a-z])(?=\S{8,})(?=.*[0-9])(?=.*[!$#*])"}
      │     };
      │ 
      │     public PasswordType CheckPasswordOnStrong()
      │     {
      │ 	var passwordType = PasswordType.Weak;
      │ 	foreach (var keyValue in TypeToPattern)
      │ 	    if (Regex.IsMatch(_password, TypeToPattern[keyValue.Key]))
      │ 		passwordType = keyValue.Key;
      │ 	return passwordType;
      │     }
      │ 
      │     public StrongPassword(string password) : base(password)
      │     {
      │     }
      │ }
      └────

    • EncryptPassword.cs (шифрование пароля)

      ┌────
      │ using System.Text;
      │ 
      │ namespace PasswordLibrary;
      │ 
      │ public class EncryptPassword : Password
      │ {
      │     public EncryptPassword(string password) : base(password)
      │     {
      │     }
      │ 
      │     public string Encrypt(uint offset)
      │     {
      │ 	offset %= 26;
      │ 	var newPass = "";
      │ 	foreach (var ch in _password)
      │ 	    if (ch >= 65 && ch <= 122)
      │ 	    {
      │ 		if (ch <= 90)
      │ 		    newPass += char.ToString((char) (ch + offset >= 91
      │ 			? 65 + offset - (91 - ch)
      │ 			: ch + offset));
      │ 		else if (ch >= 97)
      │ 		    newPass += char.ToString((char) (ch + offset > 122
      │ 			? 97 + offset - (123 - ch)
      │ 			: ch + offset));
      │ 		else
      │ 		    newPass += ch;
      │ 	    }
      │ 	    else
      │ 	    {
      │ 		newPass += ch;
      │ 	    }
      │ 
      │ 	return newPass;
      │     }
      │ 
      │     public string Encrypt(int offset)
      │     {
      │ 	if (offset < 0)
      │ 	    return Decode((uint) Math.Abs(offset));
      │ 	return Encrypt((uint) offset);
      │     }
      │ 
      │     public string Decode(uint offset)
      │     {
      │ 	offset %= 26;
      │ 
      │ 	var newPass = "";
      │ 	foreach (var ch in _password)
      │ 	    if (ch >= 65 && ch <= 122)
      │ 	    {
      │ 		if (ch <= 90)
      │ 		    newPass += char.ToString((char) (ch - offset < 65
      │ 			? 91 - (offset - (ch - 65))
      │ 			: ch - offset));
      │ 		else if (ch >= 97)
      │ 		    newPass += char.ToString((char) (ch - offset < 97 ? 122 - (offset - (ch - 96)) : ch - offset));
      │ 		else
      │ 		    newPass += ch;
      │ 	    }
      │ 	    else
      │ 	    {
      │ 		newPass += ch;
      │ 	    }
      │ 
      │ 	return newPass;
      │     }
      │ 
      │     public string Decode(int offset)
      │     {
      │ 	if (offset < 0)
      │ 	    return Encrypt((uint) Math.Abs(offset));
      │ 	return Decode((uint) offset);
      │     }
      │ }
      └────

  • Тестирование (TestPassword)

    • UnitTest1.cs

      ┌────
      │ using NUnit.Framework;
      │ using PasswordLibrary;
      │ 
      │ namespace TestPassword;
      │ 
      │ public class PasswordsTests
      │ {
      │     [SetUp]
      │     public void Setup()
      │     {
      │     }
      │ 
      │     [Test]
      │     public void StrongPasswordTest()
      │     {
      │ 	Assert.AreEqual(new StrongPassword("").CheckPasswordOnStrong(), PasswordType.Bad);
      │ 	Assert.AreEqual(new StrongPassword("12345678").CheckPasswordOnStrong(), PasswordType.Weak);
      │ 	Assert.AreEqual(new StrongPassword("ASDasdasd").CheckPasswordOnStrong(), PasswordType.Medium);
      │ 	Assert.AreEqual(new StrongPassword("ASDasdasd1").CheckPasswordOnStrong(), PasswordType.Good);
      │ 	Assert.AreEqual(new StrongPassword("ASDasdasd1!").CheckPasswordOnStrong(), PasswordType.Strong);
      │     }
      │ 
      │     [Test]
      │     public void PasswordTest()
      │     {
      │ 	Assert.IsTrue(new Password("ok").CheckPassword("ok"));
      │ 	Assert.IsFalse(new Password("123").CheckPassword("ok"));
      │     }
      │ 
      │     [Test]
      │     public void EncryptTest()
      │     {
      │ 	Assert.AreEqual(new EncryptPassword("ok").Encrypt(3), "rn");
      │ 	Assert.AreEqual(new EncryptPassword("OK").Encrypt(3), "RN");
      │ 
      │ 	Assert.AreEqual(new EncryptPassword("ok1").Encrypt(3), "rn1");
      │ 	Assert.AreEqual(new EncryptPassword("okв").Encrypt(3), "rnв");
      │ 	Assert.AreEqual(new EncryptPassword("ok").Encrypt(29), "rn");
      │ 	Assert.AreEqual(new EncryptPassword("z").Encrypt(1), "a");
      │ 	Assert.AreEqual(new EncryptPassword("Z").Encrypt(1), "A");
      │ 	Assert.AreEqual(new EncryptPassword("Z").Encrypt(2), "B");
      │ 	Assert.AreEqual(new EncryptPassword("a").Decode(1), "z");
      │ 	Assert.AreEqual(new EncryptPassword("A").Decode(1), "Z");
      │ 
      │ 
      │ 	Assert.AreEqual(new EncryptPassword("rn").Decode(29), "ok");
      │ 	Assert.AreEqual(new EncryptPassword("A").Decode(0), "A");
      │ 	Assert.AreEqual(new EncryptPassword("A").Decode(0), "A");
      │ 	Assert.AreEqual(new EncryptPassword("BCDE").Encrypt(-54), "ZABC");
      │ 	// Assert.AreEqual(new EncryptPassword("a").Decode(1), "z"); BCDE
      │     }
      │ }
      └────

  • Приложение с графическим интерфейсом (PasswordC)

    • MainWindow.xaml (Разметка)

      ┌────
      │ <Window x:Class="PasswordC.MainWindow"
      │ 	xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
      │ 	xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
      │ 	xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
      │ 	xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
      │ 	mc:Ignorable="d"
      │ 	Title="MainWindow" Height="450" Width="800">
      │     <Grid>
      │ 	<Grid.RowDefinitions>
      │ 	    <RowDefinition />
      │ 	    <RowDefinition />
      │ 	    <RowDefinition />
      │ 
      │ 	</Grid.RowDefinitions>
      │ 	<TextBlock VerticalAlignment="Bottom" Text="{Binding PassStrongMessage}" HorizontalAlignment="Center" />
      │ 
      │ 	<StackPanel Grid.Row="1" Orientation="Horizontal" HorizontalAlignment="Center" VerticalAlignment="Center">
      │ 	    <TextBlock>Пароль 1:</TextBlock>
      │ 	    <TextBox Text="{Binding Password1}" Margin="10, 0" Width="100" />
      │ 	    <TextBlock Margin="10, 0">Пароль 2:</TextBlock>
      │ 	    <TextBox Text="{Binding Password2}" Margin="10, 0" Width="100" />
      │ 	    <Button Click="EncryptOnClick">Шифровать</Button>
      │ 	    <Button Margin="10, 0" Click="CheckOnClick">Проверить</Button>
      │ 
      │ 
      │ 	</StackPanel>
      │ 	<TextBlock Grid.Row="2" VerticalAlignment="Top" Text="{Binding ErrorMessage}" Foreground="Red" FontSize="20"
      │ 		   HorizontalAlignment="Center" />
      │     </Grid>
      │ </Window>
      └────

    • MainWindow.xaml.cs (Код)

      ┌────
      │ using System;
      │ using System.Collections.Generic;
      │ using System.Linq;
      │ using System.Text;
      │ using System.Threading.Tasks;
      │ using System.Windows;
      │ using System.Windows.Controls;
      │ using System.Windows.Data;
      │ using System.Windows.Documents;
      │ using System.Windows.Input;
      │ using System.Windows.Media;
      │ using System.Windows.Media.Imaging;
      │ using System.Windows.Navigation;
      │ using System.Windows.Shapes;
      │ 
      │ namespace PasswordC;
      │ 
      │ /// <summary>
      │ /// Interaction logic for MainWindow.xaml
      │ /// </summary>
      │ public partial class MainWindow : Window
      │ {
      │     public PasswordViewModel passwordViewModel = new();
      │ 
      │     public MainWindow()
      │     {
      │ 	InitializeComponent();
      │ 	DataContext = passwordViewModel;
      │     }
      │ 
      │ 
      │     private void CheckOnClick(object sender, RoutedEventArgs e)
      │     {
      │ 	passwordViewModel.Decode();
      │     }
      │ 
      │     private void EncryptOnClick(object sender, RoutedEventArgs e)
      │     {
      │ 	passwordViewModel.Encrypt();
      │     }
      │ }
      └────

    • PasswordViewModel.cs (Логика приложения (ViewModel))

      ┌────
      │ using System;
      │ using System.Collections.Generic;
      │ using System.ComponentModel;
      │ using System.IO;
      │ using System.Runtime.CompilerServices;
      │ using System.Windows;
      │ using PasswordLibrary;
      │ 
      │ namespace PasswordC;
      │ 
      │ public class PasswordViewModel : INotifyPropertyChanged
      │ {
      │     public event PropertyChangedEventHandler? PropertyChanged;
      │ 
      │     protected void NotifyPropertyChanged(string propertyName)
      │     {
      │ 	if (PropertyChanged != null)
      │ 	    PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
      │     }
      │ 
      │     public Dictionary<PasswordType, string> typeToMessage = new()
      │     {
      │ 	{PasswordType.Bad, "Ваш пароль ужасен"},
      │ 	{PasswordType.Weak, "Ваш пароль плохой"},
      │ 	{PasswordType.Medium, "Ваш пароль средней сложности"},
      │ 	{PasswordType.Good, "Ваш пароль хороший"},
      │ 	{PasswordType.Strong, "Ваш пароль сильный"}
      │     };
      │ 
      │     private string _password1 = "";
      │     private string _password2 = "";
      │ 
      │     public StrongPassword StrongPassword = new("");
      │ 
      │     public string Password1
      │     {
      │ 	get => _password1;
      │ 	set
      │ 	{
      │ 	    if (value.Trim() != "")
      │ 	    {
      │ 		_password1 = value;
      │ 		StrongPassword = new StrongPassword(_password1);
      │ 		if (!StrongPassword.CheckPassword(_password2))
      │ 		{
      │ 		    ErrorMessage = "Пароли не совпадают";
      │ 		    PassStrongMessage = "";
      │ 		}
      │ 		else
      │ 		{
      │ 		    ErrorMessage = "";
      │ 		    PassStrongMessage = typeToMessage[StrongPassword.CheckPasswordOnStrong()];
      │ 		}
      │ 	    }
      │ 	    else
      │ 	    {
      │ 		PassStrongMessage = "";
      │ 		ErrorMessage = "";
      │ 		_password1 = "";
      │ 	    }
      │ 
      │ 	    NotifyPropertyChanged("PassStrongMessage");
      │ 	    NotifyPropertyChanged("ErrorMessage");
      │ 	}
      │     }
      │ 
      │     public string Password2
      │     {
      │ 	get => _password2;
      │ 	set
      │ 	{
      │ 	    if (value.Trim() != "")
      │ 	    {
      │ 		_password2 = value;
      │ 		if (!StrongPassword.CheckPassword(_password2))
      │ 		{
      │ 		    ErrorMessage = "Пароли не совпадают";
      │ 		    PassStrongMessage = "";
      │ 		}
      │ 		else
      │ 		{
      │ 		    ErrorMessage = "";
      │ 		    PassStrongMessage = typeToMessage[StrongPassword.CheckPasswordOnStrong()];
      │ 		}
      │ 	    }
      │ 	    else
      │ 	    {
      │ 		PassStrongMessage = "";
      │ 		ErrorMessage = "";
      │ 		_password2 = "";
      │ 	    }
      │ 
      │ 	    NotifyPropertyChanged("PassStrongMessage");
      │ 	    NotifyPropertyChanged("ErrorMessage");
      │ 	}
      │     }
      │ 
      │     public string ErrorMessage { get; set; } = "";
      │     public string PassStrongMessage { get; set; } = "";
      │ 
      │     public void Encrypt()
      │     {
      │ 	if (_password1 == _password2 && _password1.Trim() != "")
      │ 	    using (StreamWriter writer = new("pass.txt"))
      │ 	    {
      │ 		var offset = new Random().Next(-100, 100);
      │ 		// var offset = 3;
      │ 		writer.WriteLine(offset);
      │ 		writer.Write(new EncryptPassword(_password1).Encrypt(offset));
      │ 	    }
      │     }
      │ 
      │     public void Decode()
      │     {
      │ 	if (_password1 == _password2 && _password1.Trim() != "")
      │ 	    using (StreamReader reader = new("pass.txt"))
      │ 	    {
      │ 		var offset = int.Parse(reader.ReadLine()!);
      │ 		var savedPass = new EncryptPassword(reader.ReadLine()!).Decode(offset);
      │ 		ErrorMessage = "";
      │ 		if (savedPass != _password1)
      │ 		    ErrorMessage = "Пароль не совпадает с сохранённым";
      │ 		else
      │ 		    MessageBox.Show("Поздравляю, вы угадали пароль:)");
      │ 		NotifyPropertyChanged("ErrorMessage");
      │ 	    }
      │     }
      │ }
      └────


  Результаты работы приложения:

  • Тестирование:

    <file:PasswordC/1.jpg>

  • Приложение с граф. интерфейсом

    <file:PasswordC/2.jpg>

    <file:PasswordC/3.jpg>

    <file:PasswordC/4.jpg>

    <file:PasswordC/5.jpg>

    <file:PasswordC/6.jpg>

    <file:PasswordC/7.jpg>

    <file:PasswordC/8.jpg>

    <file:PasswordC/9.jpg>

    <file:PasswordC/10.jpg>

    <file:PasswordC/11.jpg>

  Задание 3

  Реализовать шифрование и дешифрование строки с помощью шифра Вижинера.

  Код:

  EncryptPassword.cs (Основной класс приложения)

  ┌────
  │ using System;
  │ using System.Collections.Generic;
  │ using System.Linq;
  │ using System.Reflection.Metadata.Ecma335;
  │ 
  │ namespace VigenereCipher;
  │ 
  │ public class EncryptPassword
  │ {
  │     public List<char> alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ".ToList();
  │     private string _password;
  │ 
  │     public EncryptPassword(string password)
  │     {
  │ 	_password = password;
  │     }
  │ 
  │     private char EncryptCh(char ch, int offset)
  │     {
  │ 	var ind = alphabet.IndexOf(Char.ToUpper(ch));
  │ 	if (ind + offset > alphabet.Count - 1)
  │ 	    return Char.IsUpper(ch)
  │ 		? alphabet[offset - (alphabet.Count - ind )]
  │ 		: Char.ToLower(alphabet[offset - (alphabet.Count - ind)]);
  │ 	return Char.IsUpper(ch) ? alphabet[ind + offset] : Char.ToLower(alphabet[ind + offset]);
  │     }
  │ 
  │     private char DecodeCh(char ch, int offset)
  │     {
  │ 	var ind = alphabet.IndexOf(Char.ToUpper(ch));
  │ 	if (ind - offset < 0)
  │ 	    return Char.IsUpper(ch)
  │ 		? alphabet[^(offset - ind)]
  │ 		: Char.ToLower(alphabet[^(offset - ind)]);
  │ 
  │ 	return Char.IsUpper(ch) ? alphabet[ind - offset] : Char.ToLower(alphabet[ind - offset]);
  │     }
  │ 
  │     public string Encrypt(string key)
  │     {
  │ 	string newString = "";
  │ 	key = key.ToUpper();
  │ 	int keyIndex = 0;
  │ 	for (int i = 0; i < _password.Length; i++)
  │ 	{
  │ 	    if (!alphabet.Contains(char.ToUpper(_password[i])))
  │ 	    {
  │ 		newString += char.ToString(_password[i]);
  │ 		continue;
  │ 	    }
  │ 
  │ 	    while (alphabet.IndexOf(key[keyIndex % key.Length]) == -1) keyIndex++;
  │ 	    newString += char.ToString(EncryptCh(_password[i], alphabet.IndexOf(key[keyIndex++ % key.Length])));
  │ 	}
  │ 
  │ 	return newString;
  │     }
  │ 
  │     public string Decode(string key)
  │     {
  │ 	string newString = "";
  │ 	key = key.ToUpper();
  │ 	int keyIndex = 0;
  │ 	for (int i = 0; i < _password.Length; i++)
  │ 	{
  │ 	    if (!alphabet.Contains(char.ToUpper(_password[i])))
  │ 	    {
  │ 		newString += char.ToString(_password[i]);
  │ 		continue;
  │ 	    }
  │ 	    while (alphabet.IndexOf(key[keyIndex % key.Length]) == -1) keyIndex++;
  │ 	    newString += char.ToString(DecodeCh(_password[i], alphabet.IndexOf(key[keyIndex++ % key.Length])));
  │ 	}
  │ 
  │ 	return newString;
  │     }
  │ }
  └────

  EncryptClassTests.cs (Тесты над классом выше)

  ┌────
  │ using NUnit.Framework;
  │ 
  │ namespace VigenereCipher;
  │ 
  │ [TestFixture, Description("Тестирования класса EncryptPassword, который шифрует русский текст шифром Веженера"),
  │  Author("Pankov Vasya")]
  │ public class EncryptClassTests
  │ {
  │     [SetUp]
  │     public void Setup()
  │     {
  │     }
  │ 
  │     [TestFixture, Description("Проверка шифрования")]
  │     public class EncryptTests
  │     {
  │ 	[Test, Description("Проверка шифрования, при наличии там чисел")]
  │ 	public void EncryptWithNums()
  │ 	{
  │ 	    Assert.AreEqual(new EncryptPassword("123").Encrypt("А"), "123");
  │ 	    Assert.AreEqual(new EncryptPassword("Вася123").Encrypt("Б"), "Гбта123");
  │ 	}
  │ 
  │ 	[Test, Description("Обычная проверка шифрования")]
  │ 	public void EncryptBase()
  │ 	{
  │ 	    Assert.AreEqual(new EncryptPassword("Вася").Encrypt("А"), "Вася");
  │ 	    Assert.AreEqual(new EncryptPassword("Вася").Encrypt("Б"), "Гбта");
  │ 	    Assert.AreEqual(new EncryptPassword("Вася").Encrypt("БА"), "Гатя");
  │ 	    Assert.AreEqual(new EncryptPassword("Вася").Encrypt("АААА"), "Вася");
  │ 	    Assert.AreEqual(new EncryptPassword("Вася").Encrypt("АБВГ"), "Вбув");
  │ 	}
  │ 	[Test, Description("Шифрование с латиницей")]
  │ 	public void EncryptWithLatin()
  │ 	{
  │ 	    Assert.AreEqual(new EncryptPassword("ВасяAbc").Encrypt("А"), "ВасяAbc");
  │ 	    Assert.AreEqual(new EncryptPassword("ВасяAbc").Encrypt("Б"), "ГбтаAbc");
  │ 	}
  │ 
  │ 	[Test]
  │ 	public void EncryptExtra()
  │ 	{
  │ 	    Assert.AreEqual(new EncryptPassword("ПРОГРАММИСТЫ УЕХАЛИ В КОВОРКИНГ").Encrypt("АГДЕВСЕАГДЕВСЕ АГДЕВСЕ АГДЕВСЕ АГД"), "ПУТЗТССМЛХЧЭ ЕЙХГПН Д ЬУВСФПКЯЗ");
  │ 	    Assert.AreEqual(new EncryptPassword("ИГРА В ДОМИНО УВЛЕКАТЕЛЬНА").Encrypt("ТЕСТ"), "ЫЗВТ Ф ИАЯЫТА ЁФРЦЭТЧЦЮОТС");
  │ 
  │ 	}
  │     }
  │ 
  │     [TestFixture, Description("Проверка декодирования")]
  │     public class DecodeTests
  │     {
  │ 	[Test, Description("Обычная проверка")]
  │ 	public void DecodeBase()
  │ 	{
  │ 	    Assert.AreEqual(new EncryptPassword("Вася").Decode("А"), "Вася");
  │ 	    Assert.AreEqual(new EncryptPassword("Гбта").Decode("Б"), "Вася");
  │ 	    Assert.AreEqual(new EncryptPassword("Гатя").Decode("БА"), "Вася");
  │ 	    Assert.AreEqual(new EncryptPassword("Вася").Decode("АААА"), "Вася");
  │ 	    Assert.AreEqual(new EncryptPassword("Вбув").Decode("АБВГ"), "Вася");
  │ 	}
  │ 
  │ 	[Test, Description("Декодирование с числами")]
  │ 	public void DecodeWithNums()
  │ 	{
  │ 	    Assert.AreEqual(new EncryptPassword("123").Decode("А"), "123");
  │ 	    Assert.AreEqual(new EncryptPassword("Гбта123").Decode("Б"), "Вася123");
  │ 	}
  │ 	[Test, Description("Декодирование с латиницей")]
  │ 	public void EncryptWithLatin()
  │ 	{
  │ 	    Assert.AreEqual(new EncryptPassword("ГбтаAbc").Decode("Б"), "ВасяAbc");
  │ 	    Assert.AreEqual(new EncryptPassword("ДвубAbc").Decode("В"), "ВасяAbc");
  │ 	}
  │ 
  │ 	[Test]
  │ 	public void EncryptExtra()
  │ 	{
  │ 	    Assert.AreEqual(new EncryptPassword("ПУТЗТССМЛХЧЭ ЕЙХГПН Д ЬУВСФПКЯЗ").Decode("АГДЕВСЕАГДЕВСЕ АГДЕВСЕ АГДЕВСЕ АГД"), "ПРОГРАММИСТЫ УЕХАЛИ В КОВОРКИНГ");
  │ 	    Assert.AreEqual(new EncryptPassword("ЫЗВТ Ф ИАЯЫТА ЁФРЦЭТЧЦЮОТС").Decode("ТЕСТ"), "ИГРА В ДОМИНО УВЛЕКАТЕЛЬНА");
  │ 	}
  │     }
  │ }
  └────

  Тесты:

  <file:VigenereCipher/1.jpg>

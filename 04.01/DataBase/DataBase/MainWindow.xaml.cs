using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Data;
using System.Data.OleDb;
using Microsoft.VisualBasic;

namespace DataBase
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private string QueryString = "SELECT * FROM Students WHERE Фамилия = ?";
        private const string ConnectionString = @"Provider=Microsoft.ACE.OLEDB.12.0;Data Source=C:\Users\user\Desktop\DataBase\DataBase\db\College.mdb;Persist Security Info=False";
        OleDbConnection connection = new OleDbConnection(ConnectionString);
        public MainWindow()
        {
            InitializeComponent();
            connection.Open();
            var table = new DataTable();
            var command = new OleDbCommand(QueryString, connection);
            command.Parameters.Add("*");
            var adapter = new OleDbDataAdapter(command);
            adapter.Fill(table);
            data.ItemsSource = table.DefaultView;
            data.UpdateLayout();
            connection.Close();
        }

        private void Search(object sender, RoutedEventArgs e)
        {
            connection.Open();
            var table = new DataTable();
            var command = new OleDbCommand(QueryString, connection);
            command.Parameters.Add(Familia.Text);
            var adapter = new OleDbDataAdapter(new OleDbCommand(QueryString, connection));
        }
    }
}
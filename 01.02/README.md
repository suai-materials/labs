
# &#1057;&#1086;&#1076;&#1077;&#1088;&#1078;&#1072;&#1085;&#1080;&#1077;

1.  [Лабораторная работа № 1.](#org5d54d7f)
2.  [Лабораторная работа № 2 Часть 2 "Тестирование программ методом «белого ящика»"](#org9ad98bc)
3.  [Лабораторная работа № 3 "Тестирование программного обеспечения методом «черного ящика»"](#orgea07d96)
4.  [Лабораторная работа № 4. Модульное тестирование.](#org0571a07)
5.  [Лабораторная работа № 5. Интеграционное тестирование](#orgd7a7672)
6.  [Лабораторная работа № 6. Тестирование производительности.](#org7e5f71e)
7.  [Лабораторная работа № 7. Тестирование usability web-сайта](#org1daf260)
8.  [Лабораторная работа № 10. Тестирование интерфейса сайта.](#org39320d6)
    1.  [Тест](#orgba1aa06)
        1.  [Задание 1](#org0aacf29)
        2.  [Задание 2](#orgcc42678)
        3.  [Задание 3](#org2cea7d0)
        4.  [Задание 4](#orga3cd429)
        5.  [Задание 5](#org61ceb59)
        6.  [Задание 6](#org52c0b20)
        7.  [Задание 7](#org9652e55)
        8.  [Задание 8](#org9d69381)
        9.  [Задание 9](#org0e01c40)
        10. [Задание 10](#org753e3fb)
        11. [Задание 11](#org9f69967)
        12. [Задание 12](#orga758417)
        13. [Задание 13](#orgdd6abc8)
9.  [Лабораторная работа №11.](#orge020aa6)



<a id="org5d54d7f"></a>

# Лабораторная работа № 1.

**Тема: "Ручная откладка программного обеспесения"** **Цель.** Изучить
процесс отладки программного обеспечения ручным методом.

**Вариант 7**

**Математическая модель:**

Формула:

![img](4_sem/lab_1/vertopal_5165c98a99064b4f8cf974f2c1593af2/media/image1.png)

Даём пользователю ввести x, y, z, вычисляем по выше приведённой формуле
и выводим ответ.

**Спецификация:**

Программа предназначена для нахождения значения по формуле в зависимости
от переданных x, y, z.

**Код программы:**

mainwindow.cpp:

    #include "mainwindow.h"
    
    #include "./ui_mainwindow.h"
    
    MainWindow::MainWindow(QWidget *parent)
    
    : QMainWindow(parent)
    
    , ui(new Ui::MainWindow)
    
    {
    
    ui->setupUi(this);
    
    QPushButton::connect(ui->pushButton, &QPushButton::pressed, this,
    &MainWindow::OnClick);
    
    }
    
    MainWindow::~MainWindow()
    
    {
    
    delete ui;
    
    }
    
    void MainWindow::OnClick(){
    
    double x = ui->doubleSpinBox_2->value();
    
    double y = ui->doubleSpinBox->value();
    
    double z = ui->doubleSpinBox_3->value();
    
    double a = (x - 2 / y) + pow(sin(atan(z)), 2);
    
    ui->label_5->setText(QString::fromStdString(std::string("Ответ: ")) +
    QString::number(a));
    
    }
    
    main.cpp
    
    #include "mainwindow.h"
    
    #include <QApplication>
    
    int main(int argc, char *argv[])
    
    {
    
    QApplication a(argc, argv);
    
    MainWindow w;
    
    w.show();
    
    return a.exec();
    
    }

mainwindow.h

    #ifndef MAINWINDOW_H
    
    #define MAINWINDOW_H
    
    #include <QMainWindow>
    
    QT_BEGIN_NAMESPACE
    
    namespace Ui { class MainWindow; }
    
    QT_END_NAMESPACE
    
    class MainWindow : public QMainWindow
    
    {
    
    Q_OBJECT
    
    public:
    
    MainWindow(QWidget *parent = nullptr);
    
    ~MainWindow();
    
    void OnClick();
    
    private:
    
    Ui::MainWindow *ui;
    
    };
    
    #endif // MAINWINDOW_H

UI:

![img](4_sem/lab_1/vertopal_5165c98a99064b4f8cf974f2c1593af2/media/image2.png)

**Тестовые наборы:**

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">Тестовый набор значений</td>
<td class="org-right">Ожидаемый результат</td>
<td class="org-right">Фактический результат</td>
<td class="org-left">Ошибка,</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">обнаружена/не обнаружена</td>
</tr>


<tr>
<td class="org-left">x = 0</td>
<td class="org-right">Ответ не найден</td>
<td class="org-right">-inf</td>
<td class="org-left">Обнаружена</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">y = 0</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">z = 0</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">x = 1</td>
<td class="org-right">-0.5</td>
<td class="org-right">-0.5</td>
<td class="org-left">Не обнаружена</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">y = 1</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">z = 1</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">x = 1</td>
<td class="org-right">Ответ не найден</td>
<td class="org-right">Ответ не найден</td>
<td class="org-left">Не обнаружена</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">y = 0</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">z = 1</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">x = 1</td>
<td class="org-right">-1</td>
<td class="org-right">-1</td>
<td class="org-left">Не обнаружена</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">y = 1</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">z = 0</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">x = 2</td>
<td class="org-right">0.984615</td>
<td class="org-right">0.984615</td>
<td class="org-left">Не обнаружена</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">y = 1</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">z = 8</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">x = 200</td>
<td class="org-right">200.9933&#x2026;</td>
<td class="org-right">Нельзя ввести числа больше 100</td>
<td class="org-left">Обнаружена</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">y = 300</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">z = 500</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">x = 100</td>
<td class="org-right">99.998</td>
<td class="org-right">99.998</td>
<td class="org-left">Не обнаружена</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">y = 1000</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">z = 0</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">x = -200</td>
<td class="org-right">-198.993</td>
<td class="org-right">-198.993</td>
<td class="org-left">Не обнаружена</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">y = -300</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">z = -500</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>
</table>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-right" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-right">Ошибка</td>
<td class="org-left">Пояснение</td>
<td class="org-left">Исправление</td>
</tr>


<tr>
<td class="org-right">-inf</td>
<td class="org-left">Не обработана ошибка, деления на ноль</td>
<td class="org-left">Добавлена проверка на ноль до вычисления:</td>
</tr>


<tr>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-right">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">![img](4_sem/lab_1/vertopal_5165c98a99064b4f8cf974f2c1593af2/media/image3.png)</td>
</tr>


<tr>
<td class="org-right">Нельзя ввести числа больше 100</td>
<td class="org-left">Стоял ограничитель на ввод чисел от 0 до 99,99</td>
<td class="org-left">![img](4_sem/lab_1/vertopal_5165c98a99064b4f8cf974f2c1593af2/media/image4.png)</td>
</tr>
</tbody>
</table>


<a id="org9ad98bc"></a>

# Лабораторная работа № 2 Часть 2 "Тестирование программ методом «белого ящика»"

Цель работы: отработать навыки составления и тестирования программ как «белого ящика»; освоить на практике метода базового пути.

Вариант 13.

Задание.

Дан одномерный массив А1, А2, …, А10 целых чисел. Получить наименьшее среди А1+А6, А2+А7, …, А5+А10. 

Код программы:

    #include<iostream>
    using namespace std;
    
    int main(){
      int arr[10];
      int min;
      cout << "Enter 10 numbers" << endl;
      //        1        2     3 
      for (int i = 0; i < 10; i++){
        //  4
        cin >> arr[i];
      }
      //       5
      min = arr[0] + arr[5];
      //     6         7      8
      for (int j = 1; j < 5; j++){
         //             9                       10
         if (min > arr[j] + arr[j + 5]) min = arr[j] + arr[j + 5];
      }
      // 11 
      cout << endl;
      cout << "Min number by formul:" << endl;
      cout << min << endl;
    }

Показ работы программы:

    Enter 10 numbers
    1 2 3 4 5 6 7 8 9 10
    
    Min number by formul:
    7

Потоковый Граф:

![img](4_sem/White_box_2/images/graph.png)

Тестирование:

Решено было тестировать методом покрытия условий, так как в программе фактически идёт проверка только одного условия (R1) - остальное же повторяющиеся циклы, которые проходят от 0 до 10 и 1 до 5.

Поэтому будет достаточно трёх тестов:

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">Тест</td>
<td class="org-right">Ожидаемый результат</td>
<td class="org-right">Фактический результат</td>
<td class="org-left">Результат тестирования</td>
</tr>


<tr>
<td class="org-left">1 2 3 4 5 6 7 8 9 10</td>
<td class="org-right">7</td>
<td class="org-right">7</td>
<td class="org-left">Ошибок не найдено</td>
</tr>


<tr>
<td class="org-left">10 10 10 10 10 10 10</td>
<td class="org-right">20</td>
<td class="org-right">20</td>
<td class="org-left">Ошибок не найдено</td>
</tr>


<tr>
<td class="org-left">1 2 3 4 5 1 2 3 4 5</td>
<td class="org-right">2</td>
<td class="org-right">2</td>
<td class="org-left">Ошибок не найдено</td>
</tr>


<tr>
<td class="org-left">1 2 3 4 1 1 2 3 4 0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-left">Ошибок не найдено</td>
</tr>
</tbody>
</table>

Результаты тестирования:

Ошибки не найдены.
Пути не показаны, так как он можно сказать один: 0 1 [2 3 4] 5 [6 7 8 9 10\*] 11.

-   - если условие верно

А при неправильном вводе программа будет работать неверно.


<a id="orgea07d96"></a>

# Лабораторная работа № 3 "Тестирование программного обеспечения методом «черного ящика»"

Для каждого поля ввода данных выполните следующее:

1.  Проанализируйте значения, которые в него можно вводить. Сгруппируйте их в классы.
2.  Проанализируйте возможные граничные условия. Их можно описать, исходя из определений классов, но возможно, что в ходе этого анализа добавятся и новые классы значений.Создайте таблицу, в которой перечислите все классы значений для каждого поля ввода и все интересные тестовые при¬меры (граничные идругие особые значения).

![img](4_sem/black_box/1.png)

Классы эквивалентности:

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Входное или выходное событие</th>
<th scope="col" class="org-left">Классы эквивалентности</th>
<th scope="col" class="org-left">Тестовые примеры</th>
<th scope="col" class="org-left">Результат</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">Количество</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">Допустимые   классы</td>
<td class="org-left">Числа от 1 до 50</td>
<td class="org-left">1,   50, 1.0000000001, 49.0000000001</td>
<td class="org-left">Найден деффект</td>
</tr>


<tr>
<td class="org-left">Недопустимые   классы</td>
<td class="org-left">Числа от -∞ до 1  Числа от 50 до +∞</td>
<td class="org-left">0.0000000001,   50.0000000001, -10, 60</td>
<td class="org-left">Деффекты не   найдены</td>
</tr>


<tr>
<td class="org-left">Радиус</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">Допустимые   классы</td>
<td class="org-left">Числа от 5 до   30</td>
<td class="org-left">5, 30, 5.5,   29.5</td>
<td class="org-left">Найден деффект</td>
</tr>


<tr>
<td class="org-left">Недопустимые   классы</td>
<td class="org-left">Числа от -∞ до   5    Числа от 30 до   +∞</td>
<td class="org-left">-10, 50, 30.0000000001,   4.9999999999</td>
<td class="org-left">Деффекты не   найдены</td>
</tr>


<tr>
<td class="org-left">V</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">Допустимые   классы</td>
<td class="org-left">Числа от 20 до 400</td>
<td class="org-left">20, 20.0000000001, 399.9999999999</td>
<td class="org-left">Деффекты не   найден</td>
</tr>


<tr>
<td class="org-left">Недопустимые   классы</td>
<td class="org-left">Числа от -∞ до 20  Числа от 400   до +∞</td>
<td class="org-left">-100, 19.0000000001, 400.0000000001, 1000</td>
<td class="org-left">Деффекты не   найдены</td>
</tr>


<tr>
<td class="org-left">Температура</td>
<td class="org-left">От 20 до 100</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">Р</td>
<td class="org-left">Введенные   данные не влияют на программу</td>
<td class="org-left">Let's rock!!!</td>
<td class="org-left">Деффекты не   найдены</td>
</tr>
</tbody>
</table>

Нахождение правильности высчитывания давления:

Есть одна формула, которая здесь подходит, но необходима константа k, которую мы найдём позже.

<img src="ltximg/report_deb8e04fe6d486e63f6464e822aac4259a0ab0bb.png" alt="report_deb8e04fe6d486e63f6464e822aac4259a0ab0bb.png" />

При обычной подстановке значений в эту формулу по известным нам значениям из программы находим константу k:

<img src="ltximg/report_08c80703de67cd0427db63c7a7b62e4eeb4e5dde.png" alt="report_08c80703de67cd0427db63c7a7b62e4eeb4e5dde.png" />

k = 82.06

Проверка:

При T = 60:

![img](4_sem/black_box/images/20220405-094849_screenshot.png)

Фактически наша догадка верна, потому что надо учитывать округление и то что вещественные числа не точны.

График строится по формуле:

<img src="ltximg/report_a7f019e0e95be0025061cf9374b6363f1f651843.png" alt="report_a7f019e0e95be0025061cf9374b6363f1f651843.png" />

Его правильность мы можем проверить например в google:

График программы нашей программы:

![img](4_sem/black_box/images/20220405-095614_screenshot.png)

![img](4_sem/black_box/images/20220405-095652_screenshot.png)

Найденные дефекты:

-   В поля: радиус и количество при вводе действительного числа, он делает в поле число целым, но нижнем поле информации мы видим, что они не целые:
    
    ![img](4_sem/black_box/images/20220405-100743_screenshot.png)
-   Если при отображении графика, нажать кнопку продолжить, то можно наблюдать что графики смешиваются:
    
    ![img](4_sem/black_box/images/20220405-101005_screenshot.png)

-   При вводе максимальных значений радиуса и значений(одновременно), программа не сможет разместить все частицы и будет вылетать:
    
    ![img](4_sem/black_box/images/20220405-101228_screenshot.png)

Также при случайном радиусе и максимальном значении количества, есть шанс схватить подобную ошибку:

![img](4_sem/black_box/images/20220331-141100_screenshot.png)


<a id="org0571a07"></a>

# Лабораторная работа № 4. Модульное тестирование.

Цель работы: закрепить теоретические знания и получить практические навыки в применении модульного тестирования.

1.  Даны две дроби A/B и C/D (А, В, С, D — натуральные числа). Составить функции, возвращающие числитель и знаменатель дроби – результата умножения дроби на дробь. Ответ должен быть несократимой дробью.

В итоге был написан целый класс Fraction, который реализует множество функционала. Такое как сложение, умножение, красивый вывод и сокращение.

Так же чтобы не морочиться(с cmake и .h), я организовал тестирование с помощью google tests, прямо в этом файле.
Код программы:

    #include<iostream>
    #include<string>
    #include <gtest/gtest.h>
    
    using namespace std;
    
    class Fraction{
    private:
    
      void reduce(){
        int max = denominator > numerator? denominator: numerator;
        if (max == 1)
          return;
        for (int i = 2; i < max / 2 + 1; i++){
    	if (numerator % i == 0 && denominator % i == 0){
    	  numerator /= i;
    	  denominator /= i;
    	  reduce();
    	}
          }
        if (numerator % max == 0 && denominator % max == 0){
    	  numerator /= max;
    	  denominator /= max;
    	  reduce();
    	}
        }
    
    public:
      // Могут быть приватными, но для облегчения тестов лежат здесь. 
      int numerator; // числитель
      int denominator; // знаменатель
      Fraction(int numerator, int denominator = 1){
        this->numerator = numerator;
        this->denominator = denominator;
        reduce();
      }
    
      friend ostream& operator << (ostream& os, Fraction& fr){
        string num_str = to_string(fr.numerator);
        string den_str = to_string(fr.denominator);
        // os << " " << num_str << " " << endl;
    
        if (den_str.size() > num_str.size()){
          for (int i = 0; i < den_str.size() / 2 + 1 - (num_str.size() % 2 == 0 ? num_str.size() / 2: num_str.size() / 2 + 1); i++)
    	os << " ";
          os << num_str << endl;
          os << "-";
          for (auto ch: den_str)
    	os << "-";
          os << "-" << " (" << (fr.numerator / 1.0f) / fr.denominator << ")" << endl;
          os << " " << den_str << endl; 
        } else {
          os << " " << num_str << endl;
          os << "-";
          for (auto ch: num_str)
    	os << "-";
          os << "-" << " (" << (fr.numerator / 1.0f) / fr.denominator << ")" << endl;
          for (int i = 0; i < num_str.size() / 2 + 1 - den_str.size() / 2; i++)
    	os << " ";
          os << den_str << endl; 
        }
        os << '\r' << '\r';
        return os;
      }
    
      Fraction& operator *=(Fraction &frac1){
        this->numerator *= frac1.numerator;
        this->denominator *= frac1.denominator;
        reduce();
        return *this;
      }
      Fraction& operator *=(int num){
        Fraction fr(num, 1);
        *this *= fr;
        return *this;
      }
      Fraction operator *(Fraction &frac1){
        return Fraction(numerator * frac1.numerator, denominator *= frac1.denominator) ;
      }
      Fraction operator *(int num){
        return Fraction(numerator * num, denominator) ;
      }
    
      Fraction& operator +=(Fraction &frac1){
        numerator *= frac1.denominator;
        frac1.numerator *= denominator; 
        this->numerator += frac1.numerator;
        this->denominator *= frac1.denominator;
        reduce();
        return *this;
      }
      Fraction operator +(Fraction &frac1){
        Fraction fr(numerator, denominator);
        fr += frac1;
        return fr;
      }
    };
    
    
    
    // int main(){
    //   int a, b;
    //   cout << "Write numerator" << endl;
    //   cin >> a;
    //   cout << "Write denominator" << endl;
    //   cin >> b;
    //   Fraction fr(a, b);
    //   Fraction fr2 = fr;
    //   cout << fr2;
    //   fr2 += fr;
    //   cout << fr2;
    //   Fraction fr3 = fr2 + fr2;
    //   cout << fr3;
    //   string str = "123";
    // }
    
    TEST(FractionAddTest, ReduceCheckToOne) {
      Fraction fr1(2, 3);
      Fraction fr2(1, 3);
      Fraction fr3 = fr1 + fr2;
      EXPECT_EQ(fr3.numerator, 1);
      EXPECT_EQ(fr3.denominator, 1);
    }
    
    TEST(FractionAddTest, VariousDenominator) {
      Fraction fr1(2, 3);
      Fraction fr2(1, 9);
      Fraction fr3 = fr1 + fr2;
      EXPECT_EQ(fr3.numerator, 7);
      EXPECT_EQ(fr3.denominator, 9);
    }
    
    TEST(FractionAddTest, VariousDenominatorReduce) {
      Fraction fr1(2, 4);
      Fraction fr2(2, 5);
      Fraction fr3 = fr1 + fr2;
      EXPECT_EQ(fr3.numerator, 9);
      EXPECT_EQ(fr3.denominator, 10);
    }
    
    TEST(FractionAddTest, ImproperFractionResult){
      Fraction fr1(2, 3);
      Fraction fr2(2, 3);
      Fraction fr3 = fr1 + fr2;
      EXPECT_EQ(fr3.numerator, 4);
      EXPECT_EQ(fr3.denominator, 3);
    }
    
    TEST(DisplayTest, OneToOneBadTest){
      Fraction fr(1, 1);
      stringstream ss;
      ss << fr;
      EXPECT_STREQ(" 1\n--- (1)\n 1\n", ss.str().c_str());
    }
    
    TEST(DisplayTest, OneToOneGoodTest){
      Fraction fr(1, 1);
      stringstream ss;
      ss << fr;
      EXPECT_STREQ(" 1\n--- (1)\n 1\n\r\r", ss.str().c_str());
    }
    
    TEST(DisplayTest, IrrationalFraction){
      Fraction fr(1, 3);
      stringstream ss;
      ss << fr;
      EXPECT_STREQ(" 1\n--- (0.333333)\n 3\n\r\r", ss.str().c_str());
    }
    
    TEST(FractionMultiplyTest, Multiply){
      Fraction fr1(2, 3);
      Fraction fr2(2, 3);
      Fraction fr3 = fr1 * fr2;
      EXPECT_EQ(fr3.numerator, 4);
      EXPECT_EQ(fr3.denominator, 9);
    }
    
    TEST(FractionMultiplyTest, MultiplyAndReduce){
      Fraction fr1(2, 3);
      Fraction fr2(1, 2);
      Fraction fr3 = fr1 * fr2;
      EXPECT_EQ(fr3.numerator, 1);
      EXPECT_EQ(fr3.denominator, 3);
    }
    
    TEST(FractionMultipieTest, MultiplyWithNumber){
      Fraction fr1(2, 3);
      Fraction fr3 = fr1 * 3;
      EXPECT_EQ(fr3.numerator, 2);
      EXPECT_EQ(fr3.denominator, 1);
    }

После сборки и запуска мы получим такой результат:

    Running main() from C:\Users\user\Desktop\UNIT_tests\_deps\googletest-src\googletest\src\gtest_main.cc
    [==========] Running 10 tests from 4 test suites.
    [----------] Global test environment set-up.
    [----------] 4 tests from FractionAddTest
    [ RUN      ] FractionAddTest.ReduceCheckToOne
    [       OK ] FractionAddTest.ReduceCheckToOne (0 ms)
    [ RUN      ] FractionAddTest.VariousDenominator
    [       OK ] FractionAddTest.VariousDenominator (0 ms)
    [ RUN      ] FractionAddTest.VariousDenominatorReduce
    [       OK ] FractionAddTest.VariousDenominatorReduce (0 ms)
    [ RUN      ] FractionAddTest.ImproperFractionResult
    [       OK ] FractionAddTest.ImproperFractionResult (0 ms)
    [----------] 4 tests from FractionAddTest (15 ms total)
    
    [----------] 3 tests from DisplayTest
    [ RUN      ] DisplayTest.OneToOneBadTest
    C:\Users\user\Desktop\UNIT_tests\1.cpp:153: Failure
    Expected equality of these values:
      " 1\n--- (1)\n 1\n"
      ss.str().c_str()
        Which is: " 1\n--- (1)\n 1\n\r\r"
    With diff:
    @@ -1,3 +1,4 @@
      1
     --- (1)
    - 1\n
    + 1
    +\r\r
    
    [  FAILED  ] DisplayTest.OneToOneBadTest (2 ms)
    [ RUN      ] DisplayTest.OneToOneGoodTest
    [       OK ] DisplayTest.OneToOneGoodTest (0 ms)
    [ RUN      ] DisplayTest.IrrationalFraction
    [       OK ] DisplayTest.IrrationalFraction (0 ms)
    [----------] 3 tests from DisplayTest (14 ms total)
    
    [----------] 2 tests from FractionMultiplyTest
    [ RUN      ] FractionMultiplyTest.Multiply
    [       OK ] FractionMultiplyTest.Multiply (0 ms)
    [ RUN      ] FractionMultiplyTest.MultiplyAndReduce
    [       OK ] FractionMultiplyTest.MultiplyAndReduce (0 ms)
    [----------] 2 tests from FractionMultiplyTest (13 ms total)
    
    [----------] 1 test from FractionMultipieTest
    [ RUN      ] FractionMultipieTest.MultiplyWithNumber
    [       OK ] FractionMultipieTest.MultiplyWithNumber (0 ms)
    [----------] 1 test from FractionMultipieTest (4 ms total)
    
    [----------] Global test environment tear-down
    [==========] 10 tests from 4 test suites ran. (67 ms total)
    [  PASSED  ] 9 tests.
    [  FAILED  ] 1 test, listed below:
    [  FAILED  ] DisplayTest.OneToOneBadTest
    
     1 FAILED TEST

Как мы можем заметить, "плохой" тест функции отображения, выдал что обннаружил ошибку и в чём именно различия. 
Эти различия мы исправили в "хорошем тесте" 


<a id="orgd7a7672"></a>

# Лабораторная работа № 5. Интеграционное тестирование

Цель работы: получение навыков интеграционного тестирования.

1.  Даны две дроби A/B и C/D (А, В, С, D — натуральные числа).

Составить функции, возвращающие числитель и знаменатель дроби – результата умножения дроби на дробь. 
Ответ должен быть несократимой дробью.

1.  Даны две дроби A/B и C/D (А, В, С, D — натуральные числа).

Составить функции, возвращающие числитель и знаменатель дроби – результата сло-жения данных дробей. 
Ответ должен быть несократимой дробью.

1.  Написать функцию вычисления k! Составить функцию вычисления суммы факториалов всех четных чисел от m до n.

Модуль 1, 2(fraction.h):

    #include <iostream>
    
    #ifndef fraction_H
    #define fraction_H
    
    using namespace std;
    
    class Fraction{
     private:
        void reduce(){
    	int max = denominator > numerator? denominator: numerator;
    	if (max == 1)
    	    return;
    	for (int i = 2; i < max / 2 + 1; i++){
    	    if (numerator % i == 0 && denominator % i == 0){
    		numerator /= i;
    		denominator /= i;
    		reduce();
    	    }
    	}
    	if (numerator % max == 0 && denominator % max == 0){
    	    numerator /= max;
    	    denominator /= max;
    	    reduce();
    	}
        };
     public:
      int numerator;
      int denominator;
        Fraction(int numerator, int denominator = 1){
    	this->numerator = numerator;
    	this->denominator = denominator;
    	reduce();
        };
        friend ostream& operator << (ostream& os, Fraction& fr){
    	string num_str = to_string(fr.numerator);
    	string den_str = to_string(fr.denominator);
    	// os << " " << num_str << " " << endl;
    
    	if (den_str.size() > num_str.size()){
    	    for (int i = 0; i < den_str.size() / 2 + 1 - (num_str.size() % 2 == 0 ? num_str.size() / 2: num_str.size() / 2 + 1); i++)
    		os << " ";
    	    os << num_str << endl;
    	    os << "-";
    	    for (auto ch: den_str)
    		os << "-";
    	    os << "-" << " (" << (fr.numerator / 1.0f) / fr.denominator << ")" << endl;
    	    os << " " << den_str << endl;
    	} else {
    	    os << " " << num_str << endl;
    	    os << "-";
    	    for (auto ch: num_str)
    		os << "-";
    	    os << "-" << " (" << (fr.numerator / 1.0f) / fr.denominator << ")" << endl;
    	    for (int i = 0; i < num_str.size() / 2 + 1 - den_str.size() / 2; i++)
    		os << " ";
    	    os << den_str << endl;
    	}
    	os << '\r' << '\r';
    	return os;
        };
        Fraction& operator *=(Fraction &frac1){
    	this->numerator *= frac1.numerator;
    	this->denominator *= frac1.denominator;
    	reduce();
    	return *this;
        };
        Fraction& operator *=(int num){
    	Fraction fr(num, 1);
    	*this *= fr;
    	return *this;
        };
        Fraction operator *(Fraction &frac1){
    	return Fraction(numerator * frac1.numerator, denominator *= frac1.denominator) ;
        };
        Fraction operator *(int num){
    	return Fraction(numerator * num, denominator) ;
        };
    
        Fraction& operator +=(Fraction &frac1){
    	numerator *= frac1.denominator;
    	frac1.numerator *= denominator;
    	this->numerator += frac1.numerator;
    	this->denominator *= frac1.denominator;
    	reduce();
    	return *this;
        };
        Fraction operator +(Fraction &frac1){
    	Fraction fr(numerator, denominator);
    	fr += frac1;
    	return fr;
        };
    };
    
    #endif

Модуль 3(factorial.h):

    #ifndef UNIT_TESTS_FACTORIAL_H
    #define UNIT_TESTS_FACTORIAL_H
    
    unsigned long long factorial(unsigned char num){ // Максимальный факториал - 21
        if (num > 21) throw EXIT_FAILURE;
        unsigned long long rez = 1;
        for (int i = 2; i <= num; i++){
    	rez *= i;
        }
        return rez;
    }
    
    unsigned long long even_sum_fact(unsigned char num, unsigned char num2){
        if (num > num2 || num2 > 20) throw EXIT_FAILURE;
        unsigned long long sum = 0;
        for (int i = num; i <= num2; i++)
    	if (i % 2 == 0)
    	    sum += factorial(i);
        return sum;
    }
    
    #endif //UNIT_TESTS_FACTORIAL_H

Тестирование с помощью Google test(tests.cpp):

    #include "gtest/gtest.h"
    #include "factorial.h"
    #include "fraction.h"
    #include "string"
    
    TEST(FractionAddTest, ReduceCheckToOne) {
        Fraction fr1(2, 3);
        Fraction fr2(1, 3);
        Fraction fr3 = fr1 + fr2;
        EXPECT_EQ(fr3.numerator, 1);
        EXPECT_EQ(fr3.denominator, 1);
    }
    
    TEST(FractionAddTest, VariousDenominator) {
        Fraction fr1(2, 3);
        Fraction fr2(1, 9);
        Fraction fr3 = fr1 + fr2;
        EXPECT_EQ(fr3.numerator, 7);
        EXPECT_EQ(fr3.denominator, 9);
    }
    
    TEST(FractionAddTest, VariousDenominatorReduce) {
        Fraction fr1(2, 4);
        Fraction fr2(2, 5);
        Fraction fr3 = fr1 + fr2;
        EXPECT_EQ(fr3.numerator, 9);
        EXPECT_EQ(fr3.denominator, 10);
    }
    
    TEST(FractionAddTest, ImproperFractionResult) {
        Fraction fr1(2, 3);
        Fraction fr2(2, 3);
        Fraction fr3 = fr1 + fr2;
        EXPECT_EQ(fr3.numerator, 4);
        EXPECT_EQ(fr3.denominator, 3);
    }
    
    TEST(DisplayTest, OneToOneBadTest) {
        Fraction fr(1, 1);
        stringstream ss;
        ss <<
           fr;
        EXPECT_STREQ(" 1\n--- (1)\n 1\n", ss.str().c_str());
    }
    
    TEST(DisplayTest, OneToOneGoodTest) {
        Fraction fr(1, 1);
        stringstream ss;
        ss << fr;
        EXPECT_STREQ(" 1\n--- (1)\n 1\n\r\r", ss.str().c_str());
    }
    
    TEST(DisplayTest, IrrationalFraction) {
        Fraction fr(1, 3);
        stringstream ss;
        ss << fr;
        EXPECT_STREQ(" 1\n--- (0.333333)\n 3\n\r\r", ss.str().c_str());
    }
    
    TEST(FractionMultiplyTest, Multiply) {
        Fraction fr1(2, 3);
        Fraction fr2(2, 3);
        Fraction fr3 = fr1 * fr2;
        EXPECT_EQ(fr3.numerator, 4);
        EXPECT_EQ(fr3.denominator, 9);
    }
    
    TEST(FractionMultiplyTest, MultiplyAndReduce) {
        Fraction fr1(2, 3);
        Fraction fr2(1, 2);
        Fraction fr3 = fr1 * fr2;
        EXPECT_EQ(fr3.numerator, 1);
        EXPECT_EQ(fr3.denominator, 3);
    }
    
    TEST(FractionMultiplyTest, MultiplyWithNumber) {
        Fraction fr1(2, 3);
        Fraction fr3 = fr1 * 3;
        EXPECT_EQ(fr3.numerator, 2);
        EXPECT_EQ(fr3.denominator, 1);
    }
    
    TEST(FactorialBaseTest, ZeroFactorial){
        EXPECT_EQ(factorial(0), 1);
    }
    
    TEST(FactorialBaseTest, LessTenFactorial){
        EXPECT_EQ(factorial(1), 1);
        EXPECT_EQ(factorial(5), 120);
        EXPECT_EQ(factorial(9), 362880);
    }
    
    TEST(FactorialBaseTest, BigFactorial){
        EXPECT_STREQ(to_string(factorial(20)).c_str(), "2432902008176640000");
    }
    TEST(FactorialBaseTest_BigFactorial_Test, BadTest){
        EXPECT_STREQ(to_string(factorial(21)).c_str(), "51090942171709440000");
    }
    
    TEST(FactorialEvenSum, NUMS_EQUALS){
        EXPECT_EQ(even_sum_fact(0, 0), 1);
        EXPECT_EQ(even_sum_fact(1, 1), 0);
        EXPECT_EQ(even_sum_fact(2, 2), 2);
    }
    
    TEST(FactorialEvenSum, NUMS_NOT_EQUALS){
        EXPECT_EQ(even_sum_fact(0, 10), 3669867);
    }
    
    TEST(FactorialEvenSum_NUMS_NOT_EQUALS_Test, BIGGEST_NUMS){
        EXPECT_EQ(even_sum_fact(0, 20), 2439325392333218667);
    }

Сборщик (Cmakelists.txt):

    cmake_minimum_required(VERSION 3.14)
    
    project(UNIT_tests)
    
    add_subdirectory(.\\googletest)
    include_directories(${gtest_SOURCE_DIR}\\include ${gtest_SOURCE_DIR})
    set(CMAKE_CXX_STANDARD 17)
    
    enable_testing()
    
    add_executable(
    	my_test
    	tests.cpp
    )
    target_link_libraries(
    	my_test
    	gtest
    	gtest_main
    )
    target_link_libraries(
    	my_test
    	gmock
    	gmock_main
    )

Результаты тестирования:

![img](4_sem/UNIT_tests_2/images/20220512-145608_screenshot.png)


<a id="org7e5f71e"></a>

# Лабораторная работа № 6. Тестирование производительности.

Цель работы: научиться определять время работы программы на примере алгоритмов сортировки массивов.

Вариант 1. 

Сравнить время работы следующих алгоритмов:

1.  Сортировка массива методом выбора
2.  "Шейкерная сортировка" массива

Зафиксировать время для размерностей массива 100, 1000, 10000, 100000.

Листинг:

    #include <iostream>
    #include <time.h>
    
    #define N 100000
    
    using namespace std;
    
    
    
    
    void shakerSort(int arr[N]) {
        int control = N - 1;
        int left  = 0;
        int right = N - 1;
        int temp;
        do {
    	for (int i = left; i < right; i++) {
    	    if (arr[i] > arr[i + 1]) {
    		std::swap(arr[i], arr[i + 1]);
    		control = i;
    	    }
    	}
    	right = control;
    	for (int i = right; i > left; i--) {
    	    if (arr[i] < arr[i - 1]) {
    		std::swap(arr[i], arr[i - 1]);
    		control = i;
    	    }
    	}
    	left = control;
        } while (left < right);
    }
    
    void selection_sort(int arr[N])
    {
        for (int i = 0; i < N - 1; i++)
        {
    	int min_index = i;
    	for (int j = i + 1; j < N; j++)
    	{
    	    if (arr[j] < arr[min_index])
    	    {
    		min_index = j;
    	    }
    	}
    	if (min_index != i)
    	{
    	    swap(arr[i], arr[min_index]);
    	}
        }
    }
    
    void print_array(int arr[N]){
        for (int i = 0; i < N; i++)
    	cout << arr[i] << " ";
        cout << endl;
    }
    
    int main() {
        int arr[N];
        for (int i = 0; i < N; i++) {
    	arr[i] = rand() % N;
    	cout << arr[i] << " ";
        }
        cout << endl;
        int copy_arr[N];
        copy(begin(arr), end(arr), begin(copy_arr));
        clock_t start = clock();
        selection_sort(arr);
        clock_t end = clock();
        double sec = (double)(end - start) / CLOCKS_PER_SEC;
        cout << "Selection sorting: " << sec << " sec. " << endl;
        start = clock();
        shakerSort(copy_arr);
        end = clock();
        sec = (double)(end - start) / CLOCKS_PER_SEC;
        cout << "Shaker sorting: " << sec << " sec. ";
    }

Тесты:

-   100 элементов:
    
    ![img](4_sem/test_pros/images/1.jpg)

-   1000 элементов:
    
    ![img](4_sem/test_pros/images/2.jpg)

-   10000 элементов:
    
    ![img](4_sem/test_pros/images/3.jpg)

-   100000
    
    ![img](4_sem/test_pros/images/4.jpg)

Вывод: Шейкерная сортировка менее эффективна чем сортировка выбором


<a id="org1daf260"></a>

# Лабораторная работа № 7. Тестирование usability web-сайта

Протестировать выбранный сайт в соответствии с планом, приведенным
далее.

Сайт: 
<https://github.com>

Архитектура и Навигация

-   Соответствует ли структура сайта целями, для достижения которых он
    предназначен? 
    
    Да

-   Понятна ли схема навигации?
    
    В основном да, но некоторые элементы по моему мнению, не понятны м первого раза.

-   Можно ли определить в каком месте сайта вы находитесь?
    
    Да.

-   Как вы находите на сайте то, что вам нужно?
    
    Всё подписано и имеет соответствующую иконку.

-   Является ли разумным количество элементов в навигационных панелях?
    
    В целом да, но есть список навигации, который появляется при нажатии на пользователя и я считаю он, совсем чуть чуть перегружен.
    
    ![img](4_sem/images/20220524-102533_screenshot.png)

-   Логично ли отсортированы элементы навигационных панелей?
    
    Да, но хотелось бы иметь возможность самостоятельной сортировки их:
    
    ![img](4_sem/images/20220524-102634_screenshot.png)
    Например: я бы убрал бы для себя Marketplace и Explore бы переместил на первое место.

-   Названия гиперссылок соответствуют названиям страницы?
    
    Да.

-   Гиперссылки выделены отчетливо?
    
    Да.

-   Существует ли отчетливо выделенная ссылка на главную страницу?
    
    Да, это иконка сайта сверху слева.
    
    ![img](4_sem/images/20220524-102830_screenshot.png)

-   Существует ли возможность поиска информации на сайте?
    
    Да.
-   Существует ли карта сайта?
    
    Нет.

-   Каждая ли страница позволяет понять, на каком сайте вы находитесь?
    
    Да.

-   Может ли пользователь управлять навигацией по сайту?
    
    Нет.

Планировка и Дизайн

-   Размер страницы превышает размер окна?
    
    Да, в высоту, но по ширине, сайт отлично изменяется под нужную ширину.

-   Схема планировка повторяется на всех страницах?

-   Существует ли отчетливый фокус на каждой странице?
    
    Да

-   Эффективно ли используется выравнивание?
    
    Да

-   Эффективно ли используется группировка?
    
    Да

-   Не громоздкая ли планировка?
    
    Нет

Содержание

-   Тексты на сайте понятны и лаконичны?
    
    Да, но так как это сайт открытых репозиториев, где каждый может написать почту любую информацию, например, про дозу нормы употребления наркотиков(не пропогандирую их применение).

-   Организован ли текст в виде небольших блоков?
    
    Да, кроме текстов созданные пользователями

-   Встречаются ли в тексте грамматические и орфографические ошибки и
    опечатки?
    
    Да, кроме текстов созданные пользователями

-   Содержат ли страницы вводный текст?
    
    Нет.

-   Поддерживают ли мультимедийные компоненты задачи пользователя?
    
    Да, картинки, код и математические формулы, отлично отображаются.

-   Являются ли единицы измерения, используемые на сайт понятными и не
    вызовут ли они трудностей при использовании их иностранцами?
    
    Да.

-   Представлены ли на сайте время и дата создания страниц?
    
    Да, для страниц созданные пользователями.

-   Представлены ли на сайте номера контактных телефонов?
    
    Нет.

-   Представлены ли на сайте адреса с почтовыми индексами?
    
    Нет

Формы и Взаимодействие

-   Соответствуют ли формы задачам пользователя?
    
    Да

-   Обладают ли диалоги логичной последовательностью шагов?
    
    Да

-   Обладают ли диалоги понятной кнопкой или ссылкой для перехода к
    следующему шагу?
    
    Да

-   Являются ли диалоги последовательными и лаконичными?
    
    Да

-   Все ли элементы форм используются по назначению?
    
    Да

-   Сгруппированы ли элементы формы по своей сути?
    
    Да

-   Понятно ли выглядит кнопка отправки формы?
    
    Да

**Графика**

-   Является ли качество используемой графики приемлемым?
    
    Да

-   Оптимизированы ли графические элементы для передачи по Интернету?
    
    Да

-   Используется ли анимация? Её не слишком много? Объем файлов
    приемлемый?
    
    Да

Цвета

-   Цвета используются логично и последовательно?
    
    Да

-   Адекватно ли различаются используемые цвета в черно-белом режиме?
    
    Да, сам сайт немного чёрнобелый.

Оформление текста

-   Размер шрифта достаточно большой?
    
    Да, но в некоторый местах может быть мелковат.
-   Цвет шрифта подходящий и достаточно контрастный?
    
    Да.
-   Достаточной ли ширины поля вокруг текста?
    
    Да.

-   Гарнитура шрифта используется надлежащим образом и последовательно?
    
    Да.

Устойчивость к ошибкам

-   Возникает ли предупреждение при попытке совершения необратимых или
    дорогостоящих действий?
    
    Да

-   Можно ли отменить рискованные или дорогостоящие действия?
    
    Да

-   Перехватываются ли возникающие ошибки локально, без обращения к
    серверу?
    
    Да

-   Содержат ли страницы с сообщением о возникших ошибках полезную
    информацию?
    
    Да

-   Содержат ли страницы с пустыми результатами поиска советы по
    расширению условий поиска?
    
    Нет

-   Существует ли система помощи (справки)?
    
    Да.

-   Структурирована ли помощь по задачам пользователя? Объясняет ли она
    пользователю, как совершить то, или иное действие?
    
    Нет.

-   Система помощи контекстно-зависимая?
    
    Нет.

Платформа и Особенность и реализация

-   Загрузка страниц происходит достаточно быстро? Занимает ли она до 6
    секунд?
    
    Да.

-   Существуют ли поврежденные графические элементы?
    
    Нет

-   Работает ли сайта с браузером пользователя?
    
    Да
-   Работает ли сайт с оборудованием, которое использует пользователь?
    
    Нет
-   Работает ли сайт на мониторах высокого и низкого разрешения?
    
    Да.


<a id="org39320d6"></a>

# Лабораторная работа № 10. Тестирование интерфейса сайта.



<a id="orgba1aa06"></a>

## Тест


<a id="org0aacf29"></a>

### Задание 1

Выбери, в какой ситуации нужно провести UI-тестирование.

-   Перед тестированием всей системы проверить, что главная страница приложения открывается и пользователь может залогиниться

-   Покрыть тестами отдельный метод
-   **Проверить работу части приложения по одному сценарию с разными входными параметрами**

-   Проверить работу системы от начала до конца


<a id="orgcc42678"></a>

### Задание 2

В какой ситуации можно использовать Selenium WebDriver? 

-   **Ввести поисковый запрос на сайте yandex.ru и кликнуть по кнопке «Найти»**
-   Отправить запрос на URL <https://yandex.ru/> c телом {"name": "WebDriver"}
-   Открыть страницу yandex.ru
-   Заполнить форму регистрации на веб-странице и ввести CAPTCH


<a id="org2cea7d0"></a>

### Задание 3

Отметь, что из этого верно.

-   Теги <h1>-<h6> нужны в любом HTML-документе
-   **Самый корневой тег — <html>**
-   Внутри тега <div> может находиться только текст, который будет отображен в этой секции

-   Обязательный атрибут тега <a> — href

-   Тег <li> означает список, а <ul> элемент этого списка

-   Тег <head> отвечает за заголовки на HTML-странице. Их видно пользователю

**- Тег <ul> нужен, чтобы создать ненумерованный список**


<a id="orga3cd429"></a>

### Задание 4

Что такое локатор?

-   **Запрос, который помогает отыскать элемент на странице**
-   Модель, которая содержит все элементы страницы

-   Драйвер браузера: через него можно передавать браузеру команды и имитировать действия пользователя


<a id="org61ceb59"></a>

### Задание 5

Определи, какой элемент на странице возвратит XPath $x("html/body/div/div/header/div/p").

-   Кнопка «Выйти» в заголовке страницы

-   Картинка с аватаром

-   **Элемент с электронным адресом пользователя**


<a id="org52c0b20"></a>

### Задание 6

Определи, какой XPath соответствует кнопке «+» в правом углу. Она добавляет новое место.

-   **$x("body/div/div/main/section/button")**

-   `$x("html/body/div/div/main/section/button")`

-   `$x("body/div/div/main/section/div/button")`


<a id="org9652e55"></a>

### Задание 7

Дополни XPath — $x("html/body/div"): уточни атрибут id. Для него это root. В ответе напиши полный XPath

`$x("html/body/div[@id=’root’]")`


<a id="org9d69381"></a>

### Задание 8

Напиши XPath ко второму элементу section. Укажи значение для атрибута class. В ответе напиши полный XPath.

`$x("html/body/main/section[@class=elements-container']")`


<a id="org0e01c40"></a>

### Задание 9

Что из этого может быть узлом?

-   **Одиночный тег**

-   **Парный тег**

-   Текст

-   **HTML-комментарий**

-   Атрибут элемента


<a id="org753e3fb"></a>

### Задание 10

Выбери путь к узлу, который отвечает за ненумерованный список картинок.

-   $x("html/body/div/div/main/section[@class='profile page\_\_​section']/ul")
-   **$x("html/body/div/div/main/section[@class='places page​\_​\_section']/ul")**

-   $x("html/body/div/div/main/section[@class='places page\_\_​section']/ul/li")

-   $x("body/div/div/main/section[@class='places page\_\_​section']/ul")


<a id="org9f69967"></a>

### Задание 11

Что нужно дописать к XPath, чтобы в итоге получить текстовый узел?

-   **text()**

-   comment()

-   node()


<a id="orga758417"></a>

### Задание 12

Выбери правильный XPath для нахождения второго элемента с тегом section:

-   $x("html/body/div/div/main/section[@class='profile page​\_​\_section']")

-   **$x("html/body/div/div/main/section[@class='places page\_​\_section']")**

-   $x("html/body/div/div/main/section[class='places page\_​\_section']")


<a id="orgdd6abc8"></a>

### Задание 13

На странице Mesto найди кнопку для выхода из зарегистрированного пользователя. Определи её value и text.

-   value — 0, text — «Выйти»

-   value нет, text — logou​t​\_header

-   **value нет, text — «Выйти»**

-   value — 1, text — logou​t​\_header


<a id="orge020aa6"></a>

# Лабораторная работа №11.

Цель работы: провести UI-тестирование сайта и научиться работать с библиотекой Selenium.

Исходный код тестов:

1.  Сборщик gradle:
    
        import org.jetbrains.kotlin.gradle.tasks.KotlinCompile
        
        plugins {
            kotlin("jvm") version "1.7.20"
        }
        
        group = "su.pank"
        version = "1.0-SNAPSHOT"
        
        repositories {
            mavenCentral()
        }
        
        dependencies {
            implementation("org.seleniumhq.selenium:selenium-java:4.5.0")
            implementation("org.apache.cassandra:cassandra-all:4.0.5")
        
            testImplementation(kotlin("test"))
            testImplementation("org.junit.jupiter:junit-jupiter-params:5.9.0")
        
        }
        
        tasks.test {
            useJUnitPlatform()
        }
        
        tasks.withType<KotlinCompile> {
            kotlinOptions.jvmTarget = "1.8"
        }
2.  Код самих тестов
    
        import org.junit.jupiter.api.*
        import org.junit.jupiter.params.ParameterizedTest
        import org.junit.jupiter.params.provider.Arguments
        import org.junit.jupiter.params.provider.MethodSource
        import org.openqa.selenium.By
        import org.openqa.selenium.JavascriptExecutor
        import org.openqa.selenium.WebDriver
        import org.openqa.selenium.chrome.ChromeDriver
        import org.openqa.selenium.support.ui.ExpectedConditions
        import org.openqa.selenium.support.ui.WebDriverWait
        import java.time.Duration
        import kotlin.test.BeforeTest
        import kotlin.test.assertEquals
        
        @TestInstance(TestInstance.Lifecycle.PER_CLASS)
        @DisplayName("Test of Ya.Practicum")
        class PankSuTests {
            lateinit var driver: WebDriver
        
            companion object {
        	@JvmStatic
        	fun users() = listOf(Arguments.of("frostkslo1@yandex.ru", "qwertyqwerty"))
            }
        
            /**
             * Открытие Chrome Driver, с необходимыми параметрами
             */
            @BeforeAll
            internal fun createDriver() {
        	driver = ChromeDriver()
        	driver.get("https://qa-mesto.praktikum-services.ru")
            }
        
            @BeforeTest
            fun returnBack() {
        	driver.get("https://qa-mesto.praktikum-services.ru")
        	try {
        	    val el = driver.findElement(By.className("header__logout"))
        	    el.click()
        	    WebDriverWait(
        		driver,
        		Duration.ofSeconds(3)
        	    ).until(ExpectedConditions.elementToBeClickable(By.className("auth-form__button")))
        
        	} catch (e: Exception) {
        
        	}
        
        
            }
        
        
            /**
             * Поиск по классу, элемент страницы с надписью "Вход"
             */
            @Test
            fun findEnter() {
        	assertEquals(driver.findElement(By.className("auth-form__title")).text, "Вход")
            }
        
            /**
             * Найди все элементы с тэгом <img> по XPath
             */
            @Test
            fun findAllImg() {
        	assertEquals(driver.findElements(By.ByTagName("img")).size, 3)
            }
        
            /**
             * Найди кнопку «Войти» и кликни по ней — сделай это через поиск по XPath, используй класс и относительный путь.
             */
            @Test
            fun findEnter2() {
        	assertEquals(driver.findElement(By.ByXPath("//*[@id=\"root\"]/div/div[1]/form/div/h3")).text, "Вход")
            }
        
            /**
             * Войди на сайт https://qa-mesto.praktikum-services.ru/ с помощью пользователя, которого тебе удалось создать в уроке про локаторы.
             */
            @ParameterizedTest
            @MethodSource("users")
            fun logIn(email: String, password: String) {
        	driver.findElement(By.id("email")).sendKeys(email)
        	driver.findElement(By.id("password")).sendKeys(password)
        	driver.findElement(By.className("auth-form__button")).click()
        	WebDriverWait(
        	    driver,
        	    Duration.ofSeconds(3)
        	).until(ExpectedConditions.elementToBeClickable(By.className("profile__add-button")))
        	assertEquals(driver.findElement(By.className("header__user")).text, email)
            }
        
        
            /**
             * Найди кнопку выхода из профиля через поиск по имени класса. Получи текст кнопки и выведи на экран.
             */
            @ParameterizedTest
            @MethodSource("users")
            fun logInAndFindLogOut(email: String, password: String) {
        	driver.findElement(By.id("email")).sendKeys(email)
        	driver.findElement(By.id("password")).sendKeys(password)
        	driver.findElement(By.className("auth-form__button")).click()
        	WebDriverWait(
        	    driver,
        	    Duration.ofSeconds(3)
        	).until(ExpectedConditions.elementToBeClickable(By.className("profile__add-button")))
        	assertEquals(driver.findElement(By.className("header__logout")).text, "Выйти")
        	println("Выйти")
            }
        
            /**
             * Напиши программу, которая сделает скролл до первой найденной карточки контента, используй поиск по CSS-селектору.
             */
            @ParameterizedTest
            @MethodSource("users")
            fun logInAndFindFirstContent(email: String, password: String) {
        	driver.findElement(By.id("email")).sendKeys(email)
        	driver.findElement(By.id("password")).sendKeys(password)
        	driver.findElement(By.className("auth-form__button")).click()
        	WebDriverWait(
        	    driver,
        	    Duration.ofSeconds(5)
        	).until(ExpectedConditions.elementToBeClickable(By.className("card__like-button")))
        	(driver as JavascriptExecutor).executeScript(
        	    "arguments[0].scrollIntoView();",
        	    driver.findElement(By.ByClassName("card__image"))
        	)
            }
        
            /**
             * Моя программа, которая ищет все уникальные имена мест.
             */
            @ParameterizedTest
            @MethodSource("users")
            fun logInAndFindAllPlaces(email: String, password: String) {
        	val places = hashSetOf<String>()
        	driver.findElement(By.id("email")).sendKeys(email)
        	driver.findElement(By.id("password")).sendKeys(password)
        	driver.findElement(By.className("auth-form__button")).click()
        	WebDriverWait(
        	    driver,
        	    Duration.ofSeconds(5)
        	).until(ExpectedConditions.elementToBeClickable(By.className("card__like-button")))
        	// Thread.sleep(1100)
        	val allPlaces = driver.findElements(By.className("card__title"))
        	for (place in allPlaces) {
        	    (driver as JavascriptExecutor).executeScript("arguments[0].scrollIntoView();", place)
        	    places.add(place.text)
        	}
        	println("Всего мест ${places.size}")
        	assertEquals(places.size, 254)
        
            }
        
            /**
             * Закрытие браузера после тестов
             */
            @AfterAll
            internal fun closePage() {
        	Thread.sleep(1000)
        	driver.close()
            }
        
        }

Результат выполнение тестов:

![img](seleniumKotlinTest/1.jpg)

Ошибка вызвана плохим интернетом.

Вывод: я провёл UI-тестирование сайта и научился работать с библиотекой Selenium.


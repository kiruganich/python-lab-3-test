# ПОЛНЫЙ КУРС ЯЗЫКА C: ТЕОРИЯ И ПРАКТИКА

**Автор:** MAI Study Materials  
**Дата:** Январь 2026  
**Уровень:** Первый курс ПМИ

---

## ОГЛАВЛЕНИЕ

1. [Функции](#функции)
2. [Указатели и адресная арифметика](#указатели-и-адресная-арифметика)
3. [Массивы и адресация](#массивы-и-адресация)
4. [Динамическая память](#динамическая-память)
5. [Работа с файлами](#работа-с-файлами)
6. [Абстрактные типы данных](#абстрактные-типы-данных)

---

# ФУНКЦИИ

## Описание и вызов

### Синтаксис

```c
// ПРОТОТИП (объявление)
тип_возврата имя_функции(тип_параметра параметр1, тип_параметра параметр2);

// РЕАЛИЗАЦИЯ (определение)
тип_возврата имя_функции(тип_параметра параметр1, тип_параметра параметр2) {
    // тело функции
    return значение;
}

// ВЫЗОВ
имя_функции(аргумент1, аргумент2);
```

### Пример

```c
// Прототип
int add(int a, int b);

int main() {
    int result = add(5, 3);  // вызов
    printf("%d\n", result);  // 8
    return 0;
}

// Реализация
int add(int a, int b) {
    return a + b;
}
```

---

## Формальные и фактические параметры

**Формальные параметры** — в определении функции:
```c
int add(int a, int b) {  // a, b — формальные
    return a + b;
}
```

**Фактические параметры (аргументы)** — при вызове:
```c
add(5, 3);  // 5, 3 — фактические
```

---

## Передача параметров

### По значению (по умолчанию)

Функция получает **КОПИЮ** аргумента. Изменения не влияют на оригинал.

```c
void increment(int x) {
    x++;  // меняем КОПИЮ
}

int main() {
    int a = 5;
    increment(a);
    printf("%d\n", a);  // всё ещё 5!
}
```

### По ссылке (через указатель)

Функция получает **АДРЕС** и может менять оригинальное значение.

```c
void increment(int *x) {
    (*x)++;  // меняем через адрес
}

int main() {
    int a = 5;
    increment(&a);
    printf("%d\n", a);  // теперь 6!
}
```

### Массивы (ВСЕГДА как указатель)

```c
void fillArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        arr[i] = i * 10;  // меняем оригинальный массив
}

int main() {
    int a[5];
    fillArray(a, 5);
    printf("%d\n", a[0]);  // 0
    printf("%d\n", a[4]);  // 40
}
```

---

## Возвращение значений

```c
int getAge() {
    return 30;  // просто число
}

struct Point {
    int x, y;
};

struct Point createPoint(int x, int y) {
    struct Point p = {x, y};
    return p;  // возвращаем копию структуры
}

int *safeFunction() {
    int *p = (int *)malloc(sizeof(int));
    *p = 10;
    return p;  // OK: память на куче
}

int *dangerousFunction() {
    int x = 10;
    return &x;  // ОШИБКА! x удалится
}
```

---

## Функция как параметр (Callback)

```c
// Определяем тип: указатель на функцию
typedef int (*Operation)(int, int);

int add(int a, int b) { return a + b; }
int subtract(int a, int b) { return a - b; }

// Функция принимает другую функцию
int calculate(int a, int b, Operation op) {
    return op(a, b);  // вызываем переданную функцию
}

int main() {
    printf("%d\n", calculate(10, 5, add));       // 15
    printf("%d\n", calculate(10, 5, subtract));  // 5
}
```

---

## Рекурсия

**Обязательные части:**
1. **Базовый случай** — когда рекурсия заканчивается
2. **Рекурсивный случай** — когда вызываем сами себя

### Факториал

```c
int factorial(int n) {
    if (n <= 1)                      // БАЗОВЫЙ СЛУЧАЙ
        return 1;
    return n * factorial(n - 1);     // РЕКУРСИВНЫЙ СЛУЧАЙ
}

factorial(5);  // 5*4*3*2*1 = 120
```

### Сумма массива

```c
int sumArray(int arr[], int n) {
    if (n <= 0)
        return 0;
    return arr[n-1] + sumArray(arr, n-1);
}

int a[5] = {1, 2, 3, 4, 5};
sumArray(a, 5);  // 15
```

### Бинарный поиск

```c
int binarySearch(int arr[], int left, int right, int target) {
    if (left > right)
        return -1;  // БАЗОВЫЙ: не найдено
    
    int mid = (left + right) / 2;
    
    if (arr[mid] == target)
        return mid;
    else if (arr[mid] > target)
        return binarySearch(arr, left, mid - 1, target);
    else
        return binarySearch(arr, mid + 1, right, target);
}
```

---

## Статические переменные

### Static в функции — сохраняет значение

```c
void counter() {
    static int count = 0;  // инициализируется один раз!
    count++;
    printf("Вызов %d\n", count);
}

int main() {
    counter();  // Вызов 1
    counter();  // Вызов 2
    counter();  // Вызов 3
}
```

### Static глобальная — видна только в файле

```c
static int globalCounter = 0;  // видна только в этом .c

static void helperFunction() {  // видна только в этом .c
    printf("Helper\n");
}
```

---

# УКАЗАТЕЛИ И АДРЕСНАЯ АРИФМЕТИКА

## Что такое указатель?

**Указатель** — переменная, хранящая **адрес другой переменной**.

```c
int x = 10;
int *p = &x;  // p содержит адрес x
```

---

## Операторы & и *

### & (адрес)
```c
int x = 5;
int *p = &x;  // & = "дай адрес x"

printf("%p\n", p);     // 0x7fff5fbff8ac (адрес)
```

### * (разыменование)
```c
int x = 5;
int *p = &x;

int y = *p;        // * = "дай значение по адресу p"
printf("%d\n", y); // 5

*p = 20;           // меняем значение по адресу
printf("%d\n", x); // 20
```

---

## Объявление указателей

```c
int *p1;              // указатель на int
float *p2;            // указатель на float
char *p3;             // указатель на char
struct Point *p4;     // указатель на struct

int *p5, *p6;         // оба указатели
int *p7, x;           // p7 указатель, x — int

int **pp = &p1;       // указатель на указатель
```

---

## Адресная арифметика

**Указатель + число = сдвиг на N элементов**

```c
int arr[5] = {10, 20, 30, 40, 50};
int *p = &arr[0];

printf("%d\n", *p);         // 10
printf("%d\n", *(p + 1));   // 20
printf("%d\n", *(p + 2));   // 30
```

**Важно:** `p + 1` НЕ добавляет 1 байт, а добавляет `sizeof(int) = 4` байта!

```
Память:
Адрес:    1000    1004    1008    1012    1016
Значение: 10      20      30      40      50

p = 1000
p + 0 = 1000
p + 1 = 1004  (1000 + 1*4 = 1004)
p + 2 = 1008  (1000 + 2*4 = 1008)
```

---

## NULL указатель

```c
int *p = NULL;  // не указывает ни на что

if (p != NULL) {
    printf("%d\n", *p);  // безопасно
}

// Разыменование NULL → ОШИБКА!
int x = *p;  // undefined behavior!
```

---

## Указатели и struct

```c
struct Point {
    int x, y;
};

struct Point p = {10, 20};
struct Point *ptr = &p;

// Доступ к полям через указатель:
(*ptr).x = 5;   // способ 1
ptr->x = 5;     // способ 2 (удобнее)

printf("%d %d\n", ptr->x, ptr->y);
```

---

## Const и указатели

```c
// const данные, изменяемый указатель
const int x = 10;
const int *p = &x;

*p = 20;            // ОШИБКА!
p = &другая;        // OK

// Изменяемые данные, const указатель
int y = 10, z = 20;
int * const p = &y;

*p = 20;            // OK
p = &z;             // ОШИБКА!

// const всё
const int * const p = &x;  // const указатель на const данные

*p = 20;            // ОШИБКА!
p = &другая;        // ОШИБКА!
```

---

# МАССИВЫ И АДРЕСАЦИЯ

## Одномерные массивы

```c
int arr[5];                         // неинициализированы
int arr[5] = {10, 20, 30, 40, 50};  // с инициализацией
int arr[] = {1, 2, 3};              // размер определяется

// Обращение и адресная арифметика
arr[0] ≡ *(arr + 0) = 10
arr[1] ≡ *(arr + 1) = 20
arr[2] ≡ *(arr + 2) = 30
```

---

## Двумерные массивы

```c
int matrix[3][4] = {
    {1,  2,  3,  4},
    {5,  6,  7,  8},
    {9, 10, 11, 12}
};

printf("%d\n", matrix[0][0]);   // 1
printf("%d\n", matrix[1][2]);   // 7
printf("%d\n", matrix[2][3]);   // 12
```

**Память:** хранится **по строкам** (row-major)

### Адресная арифметика для 2D

```c
int *p = (int *)matrix;

// ФОРМУЛА: для matrix[i][j]
// index = i * num_cols + j
*(p + i * 4 + j) = matrix[i][j]

*(p + 0*4 + 0) = 1    // matrix[0][0]
*(p + 0*4 + 1) = 2    // matrix[0][1]
*(p + 1*4 + 2) = 7    // matrix[1][2]
```

---

## Трёхмерные массивы

```c
int cube[2][3][4];

// ФОРМУЛА: для cube[i][j][k]
// index = i*(rows*cols) + j*cols + k = i*12 + j*4 + k
*(p + i*12 + j*4 + k) = cube[i][j][k]
```

---

## Указатели на многомерные массивы

```c
int matrix[3][4];

int *p1 = (int *)matrix;        // указатель на int
int (*p2)[4] = matrix;          // указатель на строку (массив из 4)

// p1 + 1 = сдвиг на 4 байта (на 1 элемент)
// p2 + 1 = сдвиг на 16 байт (на 1 строку = 4 элемента)

printf("%d\n", *(p1 + 1));           // второй элемент
printf("%d\n", *(*(p2 + 1) + 1));    // matrix[1][1]
```

---

## Передача массивов в функции

```c
// Одномерный массив
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
}

// Двумерный массив (явно столбцы)
void printMatrix(int matrix[][4], int rows) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < 4; j++) {
            printf("%d ", matrix[i][j]);
        }
    }
}

// Двумерный массив (через указатель)
void printMatrix(int (*matrix)[4], int rows) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < 4; j++) {
            printf("%d ", matrix[i][j]);
        }
    }
}
```

---

# ДИНАМИЧЕСКАЯ ПАМЯТЬ

## Стек vs Куча

### Стек
```c
int x = 10;
char arr[100];
struct Point p;

// Автоматически удаляется при выходе из функции
```

- Быстро
- Ограниченный размер
- Автоматическое удаление

### Куча
```c
int *p = malloc(sizeof(int));
char *str = malloc(100);

// НЕ удаляется автоматически!
free(p);
free(str);
```

- Медленнее
- Большой размер
- Ручное управление

---

## malloc — выделение памяти

```c
void *malloc(size_t size);
```

Выделяет `size` байт на куче и возвращает адрес.

```c
// Выделить для int
int *p = (int *)malloc(sizeof(int));
*p = 42;

// Выделить массив из 10 int
int *arr = (int *)malloc(10 * sizeof(int));
arr[0] = 10;

// Выделить для строки
char *str = (char *)malloc(50);
strcpy(str, "Hello");

// Проверка успеха
if (p == NULL) {
    printf("Ошибка: malloc не выделила память\n");
    return -1;
}
```

---

## calloc — выделение и инициализация

```c
void *calloc(size_t count, size_t size);
```

Выделяет и инициализирует нулями.

```c
// 10 int, все = 0
int *arr = (int *)calloc(10, sizeof(int));
printf("%d\n", arr[0]);  // 0

free(arr);
```

| | malloc | calloc |
|---|--------|--------|
| Аргументы | один: size | два: count, size |
| Инициализация | нет (мусор) | нулями |
| Скорость | быстрее | медленнее |

---

## realloc — перевыделение памяти

```c
void *realloc(void *ptr, size_t size);
```

Изменяет размер уже выделённого блока.

```c
// Начинаем с 5 элементов
int *arr = (int *)malloc(5 * sizeof(int));
arr[0] = 10;

// Расширяем до 10
arr = (int *)realloc(arr, 10 * sizeof(int));
// Старые данные сохранены!
arr[5] = 50;

free(arr);
```

**Правильный паттерн:**
```c
int *arr = malloc(5 * sizeof(int));

int *temp = realloc(arr, 10 * sizeof(int));
if (temp == NULL) {
    printf("Ошибка\n");
    free(arr);  // освобождаем старый блок
    return -1;
}

arr = temp;  // используем новый адрес
```

---

## free — освобождение памяти

```c
void free(void *ptr);
```

Освобождает память.

```c
int *p = (int *)malloc(sizeof(int));
*p = 42;

free(p);           // освобождаем
p = NULL;          // хорошая практика: обнуляем

// Использование после free → ОШИБКА!
// printf("%d\n", *p);  // undefined behavior!
```

---

## Утечки памяти

### Забыли free
```c
void leak() {
    int *p = malloc(sizeof(int));
    *p = 10;
    // забыли free(p)!
}
```

### Потеряли указатель
```c
int *p = malloc(sizeof(int));
int *q = malloc(sizeof(int));

p = q;  // старый p потерян!
free(p);  // освобождаем q, но не старый p
```

### Выход при ошибке
```c
int *arr = malloc(100 * sizeof(int));

if (arr == NULL) {
    return;  // забыли free!
}
```

---

## Динамический массив

```c
#include <stdlib.h>

int *createArray(int size) {
    int *arr = (int *)malloc(size * sizeof(int));
    if (arr == NULL)
        return NULL;
    return arr;
}

int main() {
    int *arr = createArray(10);
    
    for (int i = 0; i < 10; i++)
        arr[i] = i * 10;
    
    for (int i = 0; i < 10; i++)
        printf("%d ", arr[i]);
    
    free(arr);
    return 0;
}
```

---

## Динамическая структура

```c
typedef struct {
    char name[50];
    int age;
} Employee;

Employee *createEmployee(char *name, int age) {
    Employee *emp = (Employee *)malloc(sizeof(Employee));
    
    if (emp == NULL)
        return NULL;
    
    strcpy(emp->name, name);  // копируем строку
    emp->age = age;           // присваиваем число
    
    return emp;
}

int main() {
    Employee *e1 = createEmployee("Alice", 30);
    
    printf("%s, %d\n", e1->name, e1->age);
    
    free(e1);
    return 0;
}
```

---

## Динамический 2D массив

```c
int **createMatrix(int rows, int cols) {
    // ШАГ 1: выделяем массив указателей
    int **matrix = (int **)malloc(rows * sizeof(int *));
    
    // ШАГ 2: для каждого указателя выделяем строку
    for (int i = 0; i < rows; i++) {
        matrix[i] = (int *)malloc(cols * sizeof(int));
    }
    
    return matrix;
}

void freeMatrix(int **matrix, int rows) {
    // ШАГ 1: освобождаем каждую строку
    for (int i = 0; i < rows; i++) {
        free(matrix[i]);
    }
    
    // ШАГ 2: освобождаем массив указателей
    free(matrix);
}

int main() {
    int rows = 3, cols = 4;
    int **matrix = createMatrix(rows, cols);
    
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            matrix[i][j] = i * cols + j;
        }
    }
    
    freeMatrix(matrix, rows);
    return 0;
}
```

---

# РАБОТА С ФАЙЛАМИ

## Основные функции

```c
#include <stdio.h>

FILE *fopen(const char *filename, const char *mode);     // открыть
int fclose(FILE *stream);                                // закрыть

fprintf(FILE *stream, const char *format, ...);          // вывод в файл
fscanf(FILE *stream, const char *format, ...);           // ввод из файла

fputs(const char *s, FILE *stream);                      // вывести строку
fgets(char *s, int size, FILE *stream);                  // прочитать строку

fputc(int ch, FILE *stream);                             // вывести символ
fgetc(FILE *stream);                                     // прочитать символ

fwrite(const void *ptr, size_t size, size_t n, FILE *f); // блок данных
fread(void *ptr, size_t size, size_t n, FILE *f);        // блок данных

fseek(FILE *stream, long offset, int whence);            // переместиться
ftell(FILE *stream);                                     // текущая позиция
rewind(FILE *stream);                                    // в начало
```

---

## Открытие и закрытие

### fopen

```c
FILE *fopen(const char *filename, const char *mode);
```

**Режимы:**
- `"r"` — чтение
- `"w"` — запись (перезапишет)
- `"a"` — добавление (в конец)
- `"r+"` — чтение + запись
- `"rb"` — чтение (бинарное)
- `"wb"` — запись (бинарное)

```c
FILE *f = fopen("input.txt", "r");
if (f == NULL) {
    printf("Ошибка: файл не найден\n");
    return -1;
}
```

### fclose

```c
fclose(f);
```

---

## Вывод в файл

### fprintf

```c
FILE *f = fopen("output.txt", "w");

fprintf(f, "Привет, мир!\n");
fprintf(f, "Число: %d\n", 42);
fprintf(f, "Вещественное: %.2f\n", 3.14159);

fclose(f);
```

### fputs

```c
FILE *f = fopen("data.txt", "w");

fputs("Строка 1\n", f);
fputs("Строка 2\n", f);

fclose(f);
```

### fputc

```c
FILE *f = fopen("chars.txt", "w");

fputc('H', f);
fputc('i', f);
fputc('\n', f);

fclose(f);
// Содержимое: Hi
```

---

## Ввод из файла

### fscanf

```c
FILE *f = fopen("input.txt", "r");

int num;
char name[50];

fscanf(f, "%d", &num);
fscanf(f, "%s", name);
fscanf(f, "%d %s", &num, name);

fclose(f);
```

### fgets

```c
FILE *f = fopen("input.txt", "r");

char line[100];

if (fgets(line, 100, f) != NULL) {
    printf("Прочитана: %s", line);
}

fclose(f);
```

### fgetc

```c
FILE *f = fopen("input.txt", "r");

int ch;
while ((ch = fgetc(f)) != EOF) {
    printf("%c", ch);
}

fclose(f);
```

---

## Циклы чтения

### Посимвольно (fgetc)

```c
FILE *f = fopen("input.txt", "r");

int ch;
while ((ch = fgetc(f)) != EOF) {
    printf("%c", ch);
}

fclose(f);
```

### Построчно (fgets)

```c
FILE *f = fopen("input.txt", "r");

char line[100];
while (fgets(line, 100, f) != NULL) {
    printf("%s", line);
}

fclose(f);
```

### С форматом (fscanf)

```c
FILE *f = fopen("input.txt", "r");

int num;
while (fscanf(f, "%d", &num) == 1) {
    printf("%d\n", num);
}

fclose(f);
```

---

## Полный пример

```c
#include <stdio.h>

int main() {
    // ШАГ 1: Открыть файл
    FILE *f = fopen("file.txt", "r");
    if (f == NULL) {
        printf("Ошибка: не могу открыть файл\n");
        return -1;
    }
    
    // ШАГ 2: Работа с файлом
    int data;
    while (fscanf(f, "%d", &data) == 1) {
        printf("%d\n", data);
    }
    
    // ШАГ 3: Проверка ошибок
    if (ferror(f)) {
        printf("Ошибка при чтении\n");
        fclose(f);
        return -1;
    }
    
    // ШАГ 4: Закрыть файл
    if (fclose(f) != 0) {
        printf("Ошибка при закрытии\n");
        return -1;
    }
    
    return 0;
}
```

---

## Навигация по файлу

### fseek

```c
fseek(f, 10, SEEK_SET);   // на 10 байт от начала
fseek(f, 5, SEEK_CUR);    // на 5 байт вперёд
fseek(f, -10, SEEK_END);  // на 10 байт назад от конца
```

### ftell

```c
long pos = ftell(f);
printf("Позиция: %ld\n", pos);
```

### rewind

```c
rewind(f);  // в начало файла
```

---

## Бинарные файлы

### fwrite

```c
typedef struct {
    int id;
    char name[50];
} Record;

FILE *f = fopen("data.bin", "wb");

Record rec1 = {1, "Alice"};
fwrite(&rec1, sizeof(Record), 1, f);

fclose(f);
```

### fread

```c
FILE *f = fopen("data.bin", "rb");

Record rec;
while (fread(&rec, sizeof(Record), 1, f) == 1) {
    printf("ID: %d, Name: %s\n", rec.id, rec.name);
}

fclose(f);
```

---

# АБСТРАКТНЫЕ ТИПЫ ДАННЫХ

## 1. СТЕК (STACK) — LIFO

**Принцип:** Last In First Out — последний вошёл, первый вышел.

### На массиве

```c
#define MAX_SIZE 100

typedef struct {
    int data[MAX_SIZE];
    int top;  // -1 = пусто
} Stack;

Stack *stackCreate() {
    Stack *s = (Stack *)malloc(sizeof(Stack));
    s->top = -1;
    return s;
}

void stackPush(Stack *s, int value) {
    if (s->top >= MAX_SIZE - 1)
        return;
    s->data[++s->top] = value;
}

int stackPop(Stack *s) {
    if (s->top == -1)
        return -1;
    return s->data[s->top--];
}

int stackPeek(Stack *s) {
    if (s->top == -1)
        return -1;
    return s->data[s->top];
}
```

---

### На динамических структурах

```c
typedef struct Node {
    int data;
    struct Node *next;
} Node;

typedef struct {
    Node *top;
} Stack;

Stack *stackCreate() {
    Stack *s = (Stack *)malloc(sizeof(Stack));
    s->top = NULL;
    return s;
}

void stackPush(Stack *s, int value) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = value;
    newNode->next = s->top;
    s->top = newNode;
}

int stackPop(Stack *s) {
    if (s->top == NULL)
        return -1;
    Node *temp = s->top;
    int value = temp->data;
    s->top = s->top->next;
    free(temp);
    return value;
}

int stackPeek(Stack *s) {
    if (s->top == NULL)
        return -1;
    return s->top->data;
}
```

---

## 2. ОЧЕРЕДЬ (QUEUE) — FIFO

**Принцип:** First In First Out — первый вошёл, первый вышел.

### На циклическом массиве

```c
typedef struct {
    int data[MAX_SIZE];
    int front;
    int rear;
    int count;
} Queue;

Queue *queueCreate() {
    Queue *q = (Queue *)malloc(sizeof(Queue));
    q->front = 0;
    q->rear = -1;
    q->count = 0;
    return q;
}

void queueEnqueue(Queue *q, int value) {
    if (q->count >= MAX_SIZE)
        return;
    q->rear = (q->rear + 1) % MAX_SIZE;
    q->data[q->rear] = value;
    q->count++;
}

int queueDequeue(Queue *q) {
    if (q->count == 0)
        return -1;
    int value = q->data[q->front];
    q->front = (q->front + 1) % MAX_SIZE;
    q->count--;
    return value;
}

int queueFront(Queue *q) {
    if (q->count == 0)
        return -1;
    return q->data[q->front];
}
```

---

### На динамических структурах

```c
typedef struct {
    Node *front;
    Node *rear;
} Queue;

Queue *queueCreate() {
    Queue *q = (Queue *)malloc(sizeof(Queue));
    q->front = NULL;
    q->rear = NULL;
    return q;
}

void queueEnqueue(Queue *q, int value) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = value;
    newNode->next = NULL;
    
    if (q->rear == NULL) {
        q->front = q->rear = newNode;
    } else {
        q->rear->next = newNode;
        q->rear = newNode;
    }
}

int queueDequeue(Queue *q) {
    if (q->front == NULL)
        return -1;
    Node *temp = q->front;
    int value = temp->data;
    q->front = q->front->next;
    
    if (q->front == NULL)
        q->rear = NULL;
    
    free(temp);
    return value;
}
```

---

## 3. ДЕК (DEQUE) — Double Ended Queue

**Принцип:** Можешь добавлять/удалять с обоих концов.

### На двусвязном списке

```c
typedef struct Node {
    int data;
    struct Node *next;
    struct Node *prev;
} Node;

typedef struct {
    Node *front;
    Node *rear;
} Deque;

void dequePushFront(Deque *d, int value) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = value;
    newNode->next = d->front;
    newNode->prev = NULL;
    
    if (d->front != NULL) {
        d->front->prev = newNode;
    } else {
        d->rear = newNode;
    }
    d->front = newNode;
}

void dequePushBack(Deque *d, int value) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = value;
    newNode->next = NULL;
    newNode->prev = d->rear;
    
    if (d->rear != NULL) {
        d->rear->next = newNode;
    } else {
        d->front = newNode;
    }
    d->rear = newNode;
}

int dequePopFront(Deque *d) {
    if (d->front == NULL)
        return -1;
    Node *temp = d->front;
    int value = temp->data;
    d->front = d->front->next;
    
    if (d->front != NULL) {
        d->front->prev = NULL;
    } else {
        d->rear = NULL;
    }
    
    free(temp);
    return value;
}

int dequePopBack(Deque *d) {
    if (d->rear == NULL)
        return -1;
    Node *temp = d->rear;
    int value = temp->data;
    d->rear = d->rear->prev;
    
    if (d->rear != NULL) {
        d->rear->next = NULL;
    } else {
        d->front = NULL;
    }
    
    free(temp);
    return value;
}
```

---

## 4. СВЯЗНЫЕ СПИСКИ

### Однонаправленный список

```c
typedef struct Node {
    int data;
    struct Node *next;
} Node;

void listInsertFirst(Node **head, int value) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = value;
    newNode->next = *head;
    *head = newNode;
}

void listInsertLast(Node **head, int value) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = value;
    newNode->next = NULL;
    
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    
    Node *current = *head;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = newNode;
}

void listDeleteFirst(Node **head) {
    if (*head == NULL)
        return;
    Node *temp = *head;
    *head = (*head)->next;
    free(temp);
}

void listDisplay(Node *head) {
    Node *current = head;
    while (current != NULL) {
        printf("%d → ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}
```

---

### Двусвязный список

```c
typedef struct Node {
    int data;
    struct Node *next;
    struct Node *prev;
} Node;

void listInsertFirst(Node **head, int value) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = value;
    newNode->next = *head;
    newNode->prev = NULL;
    
    if (*head != NULL) {
        (*head)->prev = newNode;
    }
    *head = newNode;
}

void listInsertLast(Node **head, int value) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = value;
    newNode->next = NULL;
    
    if (*head == NULL) {
        newNode->prev = NULL;
        *head = newNode;
        return;
    }
    
    Node *current = *head;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = newNode;
    newNode->prev = current;
}

void listDisplayForward(Node *head) {
    Node *current = head;
    while (current != NULL) {
        printf("%d ↔ ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

void listDisplayBackward(Node *head) {
    if (head == NULL)
        return;
    
    Node *current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    
    while (current != NULL) {
        printf("%d ↔ ", current->data);
        current = current->prev;
    }
    printf("NULL\n");
}
```

---

### Кольцевой однонаправленный список

```c
void listInsertFirst(Node **head, int value) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = value;
    
    if (*head == NULL) {
        newNode->next = newNode;
        *head = newNode;
    } else {
        Node *current = *head;
        while (current->next != *head) {
            current = current->next;
        }
        newNode->next = *head;
        current->next = newNode;
        *head = newNode;
    }
}

void listDisplay(Node *head) {
    if (head == NULL)
        return;
    Node *current = head;
    do {
        printf("%d → ", current->data);
        current = current->next;
    } while (current != head);
    printf("(начало)\n");
}
```

---

### Кольцевой двусвязный список

```c
void listInsertFirst(Node **head, int value) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = value;
    
    if (*head == NULL) {
        newNode->next = newNode;
        newNode->prev = newNode;
        *head = newNode;
    } else {
        Node *tail = (*head)->prev;
        newNode->next = *head;
        newNode->prev = tail;
        (*head)->prev = newNode;
        tail->next = newNode;
        *head = newNode;
    }
}

void listDisplayForward(Node *head) {
    if (head == NULL)
        return;
    Node *current = head;
    do {
        printf("%d ↔ ", current->data);
        current = current->next;
    } while (current != head);
    printf("(начало)\n");
}
```

---

## Сравнение АТД

| Структура | Добавление | Удаление | Особенность | Использование |
|-----------|-----------|---------|-----------|---------------|
| **Стек** | O(1) | O(1) | LIFO | Отмена (Ctrl+Z), DFS |
| **Очередь** | O(1) | O(1) | FIFO | BFS, очередь задач |
| **Дек** | O(1) | O(1) | С обоих концов | Скользящее окно |
| **Однонап. список** | O(1)* | O(1)* | Только вперёд | Простой список |
| **Двунап. список** | O(1)* | O(1)* | Обе стороны | Двусторонний |
| **Кольц. однонап.** | O(1)* | O(1)* | Циклический | Циклический обход |
| **Кольц. двунап.** | O(1)* | O(1)* | Циклический, двусторонний | Универсальный |

*После нахождения позиции (O(n))

---

## Шаблон работы с динамическими структурами

```c
// ШАГ 1: Определяем узел
typedef struct Node {
    int data;
    struct Node *next;
} Node;

// ШАГ 2: Создаём новый узел
Node *newNode = (Node *)malloc(sizeof(Node));
newNode->data = value;
newNode->next = NULL;

// ШАГ 3: Связываем узлы
newNode->next = oldNode;
oldNode->prev = newNode;

// ШАГ 4: Обновляем указатели на начало/конец
head = newNode;
tail->next = newNode;

// ШАГ 5: Удаляем узел
Node *temp = head;
head = head->next;
free(temp);

// ШАГ 6: Проверяем на NULL
if (head == NULL) {
    printf("Пусто\n");
    return;
}
```

---

**Конец полного курса C для первокурсников ПМИ МАИ**

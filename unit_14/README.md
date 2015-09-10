# Модели и базы данных

Модель - единственный и основной способ отобразить ваши данные. Она содержит поля и методы для работы с данными, которые вы храните. Как правило, каждая модель отображает одну таблицу в базе данных.

- Каждая модель это класс унаследованный от django.db.models.Model.
- Атрибут модели представляет поле в базе данных.
- Django предоставляет автоматически созданное API для доступа к даннымю

# ./manage.py startapp blog

Django следует принципу DRY. Смысл в том, чтобы определять модели в одном месте.

Частью работы с данными также являются миграции. В отличии Django миграции вынесены из файла моделей и являются просто историей, которую Django может использовать для изменения базы данных в соответствии с текущей структурой моделей.

# models.py

```
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

```
# Типы полей

## CharField
- class CharField(max_length=None[, **options])
Строковое поле для хранения коротких или длинных строк.

Виджет по умолчанию для этого поля TextInput.

### CharField принимает один дополнительный аргумент:

- CharField.max_length
Максимальная длинна(в символах) этого поля. max_length используется для проверки данных на уровне базы данных и форм Django.

# Активация моделей

первым делом мы должны указать нашему проекту, что приложение blog установлено.

```
mysite/settings.py
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
)

```
## makemigrations
```
python manage.py makemigrations blog

Migrations for 'blog':
  0001_initial.py:
    - Create model Category

```

Выполняя makemigrations, вы говорите Django, что внесли некоторые изменения в ваши модели и хотели бы сохранить их в миграции.

Миграции используются Django для сохранения изменений ваших моделей (и структуры базы данных) - это просто файлы на диске. Вы можете изучить миграцию для создания ваших моделей, она находится в файле blog/migrations/0001_initial.py, их формат удобен для чтения на случай, если вы захотите внести изменения.

В Django есть команда, которая выполняет миграции и автоматически обновляет базу данных - она называется migrate. Команда sqlmigrate получает название миграции и возвращает SQL:
```
$ python manage.py sqlmigrate blog 0001

BEGIN;
CREATE TABLE "blog_category" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(128) NOT NULL UNIQUE);

COMMIT;

```
- Полученные запросы зависят от базы данных, которую вы используете. Пример выше получен для SQLite.

- Названия таблиц созданы автоматически из названия приложения (blog) и названия модели в нижнем регистре – caregory. (Вы можете переопределить это.)

- Первичные ключи (ID) добавлены автоматически. (Вы можете переопределить и это.)

- Учитываются особенности базы данных, которую вы используете. Специфические типы данных такие как auto_increment (MySQL), serial (PostgreSQL), или integer primary key (SQLite) будут использоваться автоматически. Тоже касается и экранирование названий, что позволяет использовать в названии кавычки – например, использование одинарных или двойных кавычек.

Команда sqlmigrate не применяет миграцию к базе данных - она просто выводит запросы на экран, чтобы вы могли увидеть какой SQL создает Django. Это полезно, если вы хотите проверить что выполнит Django, или чтобы предоставить вашему администратору базы данных SQL скрипт.

### manage.py check

Если необходимо, можете выполнить python manage.py check. Эта команда ищет проблемы в вашем проекте не применяя миграции и не изменяя базу данных.


## Параметры поля

### Приведенные аргументы доступны для всех полей. Все они не обязательны.

- null
Field.null
При True Django сохранит пустое значение как NULL в базе данных. Значение по умолчанию – False.

Избегайте использования null для строковых полей таких, как CharField и TextField, т.к. пустое значение всегда будет сохранено как пустая строка, а не NULL. Если строковое поле содержит null=True, это означает, что оно может содержать два возможных “пустых” значения: NULL и пустую строку. В большинстве случаев избыточно иметь два варианты “пустых” значений. Правило Django использовать пустую строку, вместо NULL.

Для всех типов полей, вы также должны указать blank=True если вы хотите разрешить пустые значения в формах, т.к. параметр null влияет только на сохранение в базе данных.

Если хотите использовать null для BooleanField, используйте NullBooleanField вместо этого.

- blank
Field.blank
При True поле может быть пустым. Значение по умолчанию – False.

Заметим что этот параметр отличается от null. null указывается для базы данных, в то время как blank – для проверки данных. При blank=True, проверка данных в форме позволит сохранять пустое значение в поле. При blank=False поле будет обязательным.

```
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)


```

## sqlmigrate
```
./manage.py makemigrations blog
Migrations for 'blog':
  0002_category_description.py:
    - Add field description to category

./manage.py sqlmigrate blog 0002
BEGIN;
CREATE TABLE "blog_category__new" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "description" text NOT NULL, "name" varchar(128) NOT NULL UNIQUE);
INSERT INTO "blog_category__new" ("description", "id", "name") SELECT '', "id", "name" FROM "blog_category";
DROP TABLE "blog_category";
ALTER TABLE "blog_category__new" RENAME TO "blog_category";

COMMIT;


```
### db_column
- Field.db_column
Имя колонки в базе данных для хранения данных этого поля. Если этот параметр не указан, Django будет использовать название поля.

Если имя колонки это зарезервированное SQL слово, или содержит символы запрещенные в названиях переменной в Python – в частности, дефис – все нормально. Django автоматически экранирует название колонок и таблиц.

## default
- Field.default
Значение по умолчанию для поля. Это может быть значение или вызываемый(callable) объект. Если это вызываемый объект, он будет вызван при создании нового объекта.

Значение по умолчанию не может быть изменяемым значением (экземпляр модели, список, множество и т.д.)

Значение по умолчанию используется, если был создан экземпляр модели, а значение для поля не было указано. Если поле является первичным ключом, значение по умолчанию также использует и при указании None.

В предыдущих версиях значение по умолчанию не использовалось для первичного ключа, если указать None.

- editable
Field.editable
При False, поле не будет отображаться в админке или любой другой ModelForm для модели. Такие поля также пропускаются при валидации модели. Значение по умолчанию – True.

- error_messages
Field.error_messages
error_messages позволяет переопределить сообщения ошибок возвращаемых полем. Используйте словарь с ключами соответствующими необходимым ошибкам.

Ключи ошибок такие: null, blank, invalid, invalid_choice, unique и ``unique_for_date`. 

- help_text
Field.help_text
Подсказка, отображаемая под полем в интерфеисе администратора. Это полезно для описания поля, даже если модель не используется в форме.

Заметим, что, при отображении в форме, HTML-символы не экранируются. Это позволяет использовать HTML в help_text если вам необходимо. Например:
```
help_text="Please use the following format: <em>YYYY-MM-DD</em>."

```
Также вы можете использовать обычный текст и django.utils.html.escape(), чтобы экранировать HTML. Убедитесь, что вы экранируете все подсказки, которые могут определять непроверенные пользователи, чтобы избежать XSS атак.

- primary_key
Field.primary_key
При True это поле будет первичным ключом.

Если вы не укажите primary_key=True для какого-либо поля в модели, Django самостоятельно добавит AutoField для хранения первичного ключа, вы не обязаны указывать primary_key=True, если не хотите переопределить первичный ключ по умолчанию.

primary_key=True подразумевает null=False и unique=True. Модель может содержать только один первичный ключ.

Первичный ключ доступен только для чтения. Если вы поменяете значение для существующего объекта и сохраните его, будет создан новый объект.

- unique
Field.unique
При True значение поля должно быть уникальным.

Этот параметр учитывается при сохранении в базу данных и при проверке данных в модели. Если вы попытаетесь сохранить повторное значение в поле с unique, будет вызвана ошибка django.db.IntegrityError методом save().

Этот параметр можно использовать для любого типа поля кроме ManyToManyField, OneToOneField и FileField.

Заметим что, при unique равном True, не нужно указывать db_index, т.к. unique создает индекс.

- verbose_name
Field.verbose_name
Отображаемое имя поля. Если параметр не указан, Django самостоятельно создаст его используя имя атрибута поля, заменяя подчеркивание на пробелы.

- validators
Field.validators
Список проверок(“валидаторов”) выполняемых для этого поля. 

- AutoField
class AutoField(**options)
Автоинкрементное поле IntegerField. Используется для хранения ID. Скорее всего вам не придется использовать это поле, первичный ключ будет автоматически добавлен к модели. 

- IntegerField
class IntegerField([**options])
Число. Значение от -2147483648 до 2147483647 для всех поддерживаемых баз данных Django. Форма использует виджет TextInput.

- TextField
class TextField([**options])
Большое текстовое поле. Форма использует виджет Textarea.

Если указать атрибут max_length, это повлияет на поле, создаваемое виджетом Textarea. Но не учитывается на уровне модели или базы данных. Для этого используйте CharField.


## Миграции

Теперь, выполните команду migrate снова, чтобы создать таблицы для этих моделей в базе данных:

### $ python manage.py migrate

Команда migrate выполняет все миграции, которые ещё не выполнялись, (Django следит за всеми миграциями, используя таблицу в базе данных django_migrations) и применяет изменения к базе данных, синхронизируя структуру базы данных со структурой ваших моделей.

Миграции - очень мощная штука. Они позволяют изменять ваши модели в процессе развития проекта без необходимости пересоздавать таблицы в базе данных. Их задача изменять базу данных без потери данных. 

### 0001_initial.py

```
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
        ),
    ]
```

### Внесите изменения в модели (в models.py).

Выполните python manage.py makemigrations чтобы создать миграцию для ваших изменений

### 0002_category_description.py
```
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
```

### Выполните python manage.py migrate чтобы применить изменения к базе данных.

Две команды необходимы для того, чтобы хранить миграции в системе контроля версий. Они не только помогают вам, но и могут использоваться другими программистами вашего проекта.

```
./manage.py migrate
Operations to perform:
  Synchronize unmigrated apps: staticfiles, messages
  Apply all migrations: admin, blog, contenttypes, auth, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  Rendering model states... DONE
  Applying blog.0001_initial... OK
  Applying blog.0002_category_description... OK
```
## Добавим приложение blog в интерфейс администратора

Нам нужно указать, что объекты модели Category могли редактироваться в интерфейсе администратора. Для этого создадим файл blog/admin.py, и отредактируем следующим образом:

blog/admin.py
```
from django.contrib import admin

from .models import Category

admin.site.register(Category)
```

## Изучим возможности интерфейса администратора

После регистрации модели Category Django отобразит ее на главной странице

### Поля формы формируются на основе описания модели Question.

Для различных типов полей модели (CharField, TextField) используются соответствующие HTML поля. Каждое поле знает как отобразить себя в интерфейсе администратора.

### В нижней части страницы мы видим несколько кнопок:

- Save – сохранить изменения и вернуться на страницу списка объектов.

- Save and continue editing – сохранить изменения и снова загрузить страницу редактирования текущего объекта.

- Save and add another – Сохранить изменения и перейти на страницу создания нового объекта.

- Delete – Показывает страницу подтверждения удаления.

## Выполнение запросов

Важно добавить метод __unicode__() / __str__() не только для красивого отображения в консоли, но так же и потому, что Django использует строковое представление объекта в интерфейсе администратора.

```
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)

    def __unicode__(self):              # __str__ on Python 3
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __unicode__(self):              # __str__ on Python 3
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __unicode__(self):              # __str__ on Python 3
        return self.name
```

## __str__ или __unicode__?

В Python 3 все проще, просто используйте __str__().

В Python 2 необходимо определить метод __unicode__(), который возвращает unicode. Модели Django содержат метод __str__(), который вызывает метод __unicode__() и конвертирует результат в UTF-8 байтовую строку. Это означает, что unicode(p) вернет строку Unicode, и str(p) вернет обычную строку, символы которой закодированы в UTF-8. Python делает наоброт: object содержит метод __unicode__, который вызывает __str__ и конвертирует результат ASCII байтовую строку. Это отличие может вводить в заблуждение.


## Поля отношений

Django предоставляет набор полей для определения связей между моделями.

- ForeignKey
class ForeignKey(othermodel[, **options])
Связь многое-к-одному. Принимает позиционный аргумент: класс связанной модели.

```

class Blog(models.Model):
    name = models.CharField(max_length=100)
    categoty = models.ForeignKey(Category)
    tagline = models.TextField()

    def __unicode__(self):              # __str__ on Python 3
        return self.name
```


Для связи на модель из другого приложения используйте название модели и приложения. Например, если модель Category находится в приложении production, используйте:
```
class Blog(models.Model):
    categoty = models.ForeignKey('production.Category')

```
Такой способ позволяет создать циклическую зависимость между моделями из разных приложений.

В базе данных автоматом создается индекс для ForeignKey. Можно указать для db_index False, чтобы отключить такое поведение. Это может пригодиться, если внешний ключ используется для согласованности данных, а не объединения(join) в запросах, или вы хотите самостоятельно создать альтернативный индекс или индекс на несколько колонок.

Не рекомендуется использовать ForeignKey из приложения без миграций к приложению с миграциями. 

## Представление в базе данных
За кулисами, Django добавляет "_id" к названию поля для создания названия колонки. В примере выше, таблица для модели Blog будет содержать колонку categoty_id. (Такое поведение можно изменить, указав аргумент db_column) Хотя, ваш код никогда не должен использовать названий колонок, если только вы не используете чистый SQL. Вы всегда будете использовать названия полей модели.


## ForeignKey.on_delete
Когда объект, на который ссылается ForeignKey, удаляется, Django по-умолчанию повторяет поведение ограничения ON DELETE CASCADE в SQL и удаляет объекты, содержащие ForeignKey. Такое поведение может быть переопределено параметром on_delete. Например, если ваше поле ForeignKey может содержать NULL и вы хотите, чтобы оно устанавливалось в NULL после удаления связанного объекта:

#### Возможные значения для on_delete находятся в django.db.models:

- CASCADE
Каскадное удаление, значение по умолчанию.

- PROTECT
Препятствует удалению связанного объекта вызывая исключение django.db.models.ProtectedError`(подкласс :exc:`django.db.IntegrityError).

- SET_NULL
Устанавливает ForeignKey в NULL; возможно только если null равен True.

- SET_DEFAULT
Устанавливает ForeignKey в значение по умолчанию; значение по-умолчанию должно быть указано для ForeignKey.

- SET()
Устанавливает ForeignKey в значение указанное в SET(). Если указан выполняемый объект, результат его выполнения. Вызываемый объект можно использовать, чтобы избежать запросов во время импорта models.py:

- DO_NOTHING
Ничего не делать. Если используемый тип базы данных следит за целостностью связей, будет вызвано исключение IntegrityError, за исключением, когда вы самостоятельно добавите SQL правило ON DELETE для поля таблицы (возможно используя загрузочный sql).

```
./manage.py makemigrations blog
Migrations for 'blog':
  0003_author_blog.py:
    - Create model Author
    - Create model Blog

./manage.py migrate
Operations to perform:
  Synchronize unmigrated apps: staticfiles, messages
  Apply all migrations: admin, blog, contenttypes, auth, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  Rendering model states... DONE
  Applying blog.0003_author_blog... OK
```

### admin.py
```
from django.contrib import admin

# Register your models here.
from .models import Category, Blog, Author

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Author)
```

## ManyToManyField
- class ManyToManyField(othermodel[, **options])
Связь многие-ко-многим. Принимает позиционный аргумент: класс связанной модели. Работает так же как и ForeignKey, включая рекурсивную и ленивую связь.

Связанные объекты могут быть добавлены, удалены или созданы с помощью RelatedManager.

### Представление в базе данных
Django самостоятельно создаст промежуточную таблицу для хранения связи многое-ко-многим. По-умолчанию, название этой таблицы создается из названия поля и связанной модели. Так как некоторые базы данных не поддерживают длинные названия таблиц, оно будет обрезано до 64 символов и будет добавлен уникальный хеш. Это означает что вы можете увидеть такие названия таблиц author_blog_9cdf4; это нормально. Вы можете указать название промежуточной таблицы, используя параметр db_table.

```
class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __unicode__(self):              # __str__ on Python 3
        return self.headline
```

### makemigrations blog
```
./manage.py makemigrations blog
Migrations for 'blog':
  0004_entry.py:
    - Create model Entry

./manage.py migrate
Operations to perform:
  Synchronize unmigrated apps: staticfiles, messages
  Apply all migrations: admin, blog, contenttypes, auth, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  Rendering model states... DONE
  Applying blog.0004_entry... OK

```

К полям DateTimeField добавлен JavaScript виджет. Для даты добавлена кнопка “Сегодня” и календарь, для времени добавлена кнопка “Сейчас” и список распространенных значений.

### DateField
class DateField([auto_now=False, auto_now_add=False, **options])
Дата, представленная в виде объекта datetime.date Python. Принимает несколько дополнительных параметров:

- DateField.auto_now
Значение поля будет автоматически установлено в текущую дату при каждом сохранении объекта. Полезно для хранения времени последнего изменения. Заметим, что текущее время будет использовано всегда; это не просто значение по умолчанию, которое вы можете переопределить.

- DateField.auto_now_add
Значение поля будет автоматически установлено в текущую дату при создании(первом сохранении) объекта. Полезно для хранения времени создания. Заметим, что текущее время будет использовано всегда; это не просто значение по-умолчанию, которое вы можете переопределить.

В форме поле будет представлено как :class:`~django.forms.TextInput с JavaScript календарем, и кнопкой “Сегодня”. Содержит дополнительную ошибку invalid_date.

Опции auto_now_add, auto_now и default взаимоисключающие. Использование их вместе вызовет ошибку.


При использовании auto_now или auto_now_add со значением True будут установлены параметры editable=False и blank=True.

Опции``auto_now`` и auto_now_add всегда используют дату в часовом поясе по умолчанию в момент создания или изменения объекта. Если такое поведение вам не подходит, вы можете указать свою функцию как значение по умолчанию, или переопределить метод save(), вместо использования auto_now или auto_now_add. Или использовать DateTimeField вместо DateField и выполнять преобразование в дату при выводе значения.


### Получение одного объекта с помощью get
filter() всегда возвращает QuerySet, даже если только один объект возвращен запросом - в этом случае, это будет QuerySet содержащий один объект.

Если вы знаете, что только один объект возвращается запросом, вы можете использовать метод get() менеджера(Manager), который возвращает непосредственно объект:

```
one_entry = Entry.objects.get(pk=1)
```

Если результат пустой, get() вызовет исключение DoesNotExist. Это исключение является атрибутом модели, для которой выполняется запрос. Если в примере выше не существует объекта Entry с первичным ключом равным 1, Django вызовет исключение Entry.DoesNotExist.

Также Django отреагирует, если запрос get() вернет не один объект. В этом случае будет вызвано исключение MultipleObjectsReturned, которое также является атрибутом класса модели.


В большинстве случаев вы будете использовать all(), get(), filter() и exclude() для получения объектов из базы данных. 

### Ограничение выборки
Используйте синтаксис срезов для списков Python для ограничения результата выборки QuerySet. Это эквивалент таких операторов SQL как LIMIT и OFFSET.

Например, этот код возвращает 5 первых объектов (LIMIT 5):
```
Entry.objects.all()[:5]
```
Этот возвращает с шестого по десятый (OFFSET 5 LIMIT 5):

```
Entry.objects.all()[5:10]
```
Отрицательные индексы (например, Entry.objects.all()[-1]) не поддерживаются.

На самом деле, срез QuerySet возвращает новый QuerySet – запрос не выполняется. Исключением является использовании “шага” в срезе. Например, этот пример выполнил бы запрос, возвращающий каждый второй объект из первых 10:
```
Entry.objects.all()[:10:2]
```
Для получения одного объекта, а не списка (например, SELECT foo FROM bar LIMIT 1), используйте индекс вместо среза. Например, этот код возвращает первый объект Entry в базе данных, после сортировки записей по заголовку:
```
Entry.objects.order_by('headline')[0]
```
Это эквивалент:
```
Entry.objects.order_by('headline')[0:1].get()
```
Заметим, что первый пример вызовет IndexError, в то время как второй - DoesNotExist, если запрос не вернёт ни одного объекта. 

### blog/urls.py
```
from django.conf.urls import include, url

from blog import views

urlpatterns = [
    url(r'^$', views.index),
    ]
```
### urls.py
```
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('page.urls')),
    url(r'^home/', include('home.urls')),
 
    url(r'^blog/', include('blog.urls')),
 
    url(r'^$',TemplateView.as_view(template_name='index.html')),
  
]
```
### blog/views.py
```
from django.shortcuts import render
from .models import Entry
# Create your views here.

def index(request):
    result = Entry.objects.all()
    return render(request,'blog/index.html',{'result':result})
```
### templates/blog/index.html
```
{% extends "base.html" %} 
{% block title %} {{ block.super }} - SECTION NAME {% endblock %}

{% block content %} 

<h2>Index page</h2>

    {% for article in result %} 
        <div> 
            <h2><a href="#"> 
                {{ article.headline }} 
            </a></h2> 
                <span>{{ article.pub_date|date:"SHORT_DATE_FORMAT" }} | 
                      {{ article.authors|addslashes }} 
                </span>
                {{ article.body_text }} 
        </div> 
    {% endfor %}

{% endblock %}
```
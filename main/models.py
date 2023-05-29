from django.db import models

class Subject(models.Model):
    class Meta:
        verbose_name = 'Субъект'
        verbose_name_plural = 'Субъекты'

    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'{self.name}'

class Series(models.Model):
    class Meta:
        verbose_name = 'Вид страхования'
        verbose_name_plural = 'Виды страхования'

    name = models.CharField(max_length=100, verbose_name='Серия')

    def __str__(self):
        return f'{self.name}'

class Clients(models.Model):
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    name = models.CharField(max_length=100, verbose_name='Серия')
    inn = models.CharField(verbose_name='ИНН')

    def __str__(self):
        return f'{self.name}'

class Coefficient_by_type_car(models.Model):
    class Meta:
        verbose_name = 'Коэффициент по типу ТС'
        verbose_name_plural = 'Коэффициенты по типу ТС'

    coefficient = models.FloatField(verbose_name='Коэффициент')

    def __str__(self):
        return f'{self.coefficient}'

class Driver_coefficient(models.Model):
    class Meta:
        verbose_name = 'Коэффициент по водителям'
        verbose_name_plural = 'Коэффициент по водителям'

    coefficient = models.FloatField(verbose_name='Коэффициент')

    def __str__(self):
        return f'{self.coefficient}'

class Diagnostic_card(models.Model):
    class Meta:
        verbose_name = 'Наличие диагностической карты коэффициент'
        verbose_name_plural = 'Наличие диагностической карты коэффициент'

    coefficient = models.FloatField(verbose_name='Коэффициент')

    def __str__(self):
        return f'{self.coefficient}'

class Executor(models.Model):
    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    name = models.CharField(max_length=100, verbose_name='Ф.И.О.')

    def __str__(self):
        return f'{self.name}'

class Natural_legal_person(models.Model):
    class Meta:
        verbose_name = 'Физ.лицо/Юр.лицо'
        verbose_name_plural = 'Физ.лицо/Юр.лицо'

    person = models.CharField(max_length=100, verbose_name='Лицо')

    def __str__(self):
        return f'{self.person}'

class Osago(models.Model):
    class Meta:
        verbose_name = 'ОСАГО'
        verbose_name_plural = 'ОСАГО'

    series = models.ForeignKey(Series, on_delete=models.CASCADE, verbose_name='Серия')
    number = models.IntegerField(verbose_name='Номер бланка')
    policy = models.CharField(max_length=16, verbose_name='Номер полиса')
    insurant = models.ForeignKey(Clients, on_delete=models.CASCADE, verbose_name='Страхователь')
    owner = models.ForeignKey(Clients, on_delete=models.CASCADE, verbose_name='Собственник', related_name='+')
    list_display = [
        'insurant',
        'for ',
    ]
    raw_id_fields = ['insurant', 'owner',]
    car_model = models.CharField(max_length=50, verbose_name='Марка/модель ТС')
    year = models.IntegerField(verbose_name='Год выпуска ТС')
    engine_capacity = models.IntegerField(verbose_name='Объем двигателя, см3')
    government_number = models.CharField(verbose_name='Гос.№ ТС')
    VIN = models.CharField(max_length=20, verbose_name='VIN(VID)')
    chassis_number = models.CharField(max_length=50, verbose_name='Номер кузова/шасси', null=True, blank=True)
    country = models.CharField(max_length=50, verbose_name='Страна регистрации ТС')
    region = models.CharField(max_length=100, verbose_name='Регион')
    driver_1 = models.ForeignKey(Clients, on_delete=models.CASCADE, verbose_name='Информация о водителе 1', related_name='+', null=True, blank=True)
    date_of_birth_1 = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    license_number_1 = models.CharField(max_length=50, verbose_name='№ вод.удостоверения', null=True, blank=True)
    date_of_issue_drive_license_1 = models.DateField(verbose_name='Дата выдачи водительского удостоверения', null=True, blank=True)
    driver_2 = models.ForeignKey(Clients, on_delete=models.CASCADE, verbose_name='Информация о водителе 2', related_name='+', null=True, blank=True)
    date_of_birth_2 = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    license_number_2 = models.CharField(max_length=50, verbose_name='№ вод.удостоверения', null=True, blank=True)
    date_of_issue_drive_license_2 = models.DateField(verbose_name='Дата выдачи водительского удостоверения', null=True, blank=True)
    driver_3 = models.ForeignKey(Clients, on_delete=models.CASCADE, verbose_name='Информация о водителе 3', related_name='+', null=True, blank=True)
    date_of_birth_3 = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    license_number_3 = models.CharField(max_length=50, verbose_name='№ вод.удостоверения', null=True, blank=True)
    date_of_issue_drive_license_3 = models.DateField(verbose_name='Дата выдачи водительского удостоверения', null=True, blank=True)
    driver_4 = models.ForeignKey(Clients, on_delete=models.CASCADE, verbose_name='Информация о водителе 4', related_name='+', null=True, blank=True)
    date_of_birth_4 = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    license_number_4 = models.CharField(max_length=50, verbose_name='№ вод.удостоверения', null=True, blank=True)
    date_of_issue_drive_license_4 = models.DateField(verbose_name='Дата выдачи водительского удостоверения', null=True, blank=True)
    policy_date_start = models.DateField(verbose_name='Дата начало действия полиса', null=True, blank=True)
    policy_date_expiration = models.DateField(verbose_name='Дата окончания действия полиса', null=True, blank=True)
    single_tariff = models.IntegerField(verbose_name='Единый тариф', default=1680)
    coefficient_by_type_car = models.ForeignKey(Coefficient_by_type_car, on_delete=models.CASCADE, verbose_name='Коэф.по типу ТС')
    driver_coefficient = models.ForeignKey(Driver_coefficient, on_delete=models.CASCADE, verbose_name='Коэффициент по водителям')
    diagnostic_card = models.ForeignKey(Diagnostic_card, on_delete=models.CASCADE, verbose_name='Наличие диагностической карты коэффициент')
    insurance_start_date = models.DateField(verbose_name='Дата начало страхования')
    insurance_start_end = models.DateField(verbose_name='Дата окончания страхования')
    insurance_premium = models.FloatField(verbose_name='Страховая премия')
    payment_state = models.CharField(max_length=100, verbose_name='Статус полаты', default='Оплачено')
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE, verbose_name='Юр.лицо/Физ.лицо')


    def __str__(self):
        return f'{self.series} {self.number}'

#xercvtbyuinomp,[.]/'mgnvb rejlgkl /db '
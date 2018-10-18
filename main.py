#!/usr/bin/env python3
# -*- coding: utf-8-unix -*-

import datetime
import gantt

# Change font default
gantt.define_font_attributes(fill='black',
                             stroke='black',
                             stroke_width=0,
                             font_family="Verdana")

# Create two resources
md = gantt.Resource('Michał Dultz')
pc = gantt.Resource('Piotr Czajka')
ad = gantt.Resource('Andrii Donets')


# Create some tasks
t1 = gantt.Task(name='Założenie projektu FE',
                start=datetime.date(2018, 9, 10),
                duration=1,
                resources=[pc])
t2 = gantt.Task(name='Strona główna i menu',
                start=datetime.date(2018, 9, 15),
                duration=3,
                depends_of=t1,
                resources=[pc])
t3 = gantt.Task(name='Panel logowania i rejestracji',
                start=datetime.date(2018, 9, 20),
                duration=4,
                depends_of=t1,
                resources=[pc])
t4 = gantt.Task(name='Tabela CRUD',
                start=datetime.date(2018, 9, 25),
                duration=5,
                depends_of=t1,
                resources=[pc])
t5 = gantt.Task(name='Panel doktora',
                start=datetime.date(2018, 10, 2),
                duration=3,
                depends_of=t1,
                resources=[pc])
t6 = gantt.Task(name='Grafik lekarza',
                start=datetime.date(2018, 10, 8),
                duration=7,
                depends_of=[t1, t5],
                resources=[pc])
t7 = gantt.Task(name='Panel pacjenta',
                start=datetime.date(2018, 10, 18),
                duration=4,
                depends_of=t1,
                resources=[pc])
t8 = gantt.Task(name='Umawianie wizyt',
                start=datetime.date(2018, 10, 25),
                duration=5,
                depends_of=[t1, t6, t7],
                resources=[pc])
t9 = gantt.Task(name='Panel pracownika',
                start=datetime.date(2018, 10, 30),
                duration=4,
                depends_of=[t1],
                resources=[pc])
t10 = gantt.Task(name='Potwierdzanie pacjentów',
                 start=datetime.date(2018, 11, 3),
                 duration=2,
                 depends_of=[t1, t9],
                 resources=[pc])
t11 = gantt.Task(name='Portfel',
                 start=datetime.date(2018, 11, 5),
                 duration=4,
                 depends_of=[t1, t7],
                 resources=[pc])
t12 = gantt.Task(name='Panel wizyty',
                 start=datetime.date(2018, 11, 10),
                 duration=3,
                 depends_of=[t1, t5, t6],
                 resources=[pc])
t13 = gantt.Task(name='Kolejka',
                 start=datetime.date(2018, 11, 15),
                 duration=6,
                 depends_of=[t1, t12],
                 resources=[pc])

tasks = [v for k, v in locals().items() if k.startswith('t')]

p1 = gantt.Project(name='DDC Clinic')

[p1.add_task(t) for t in tasks]

p1.make_svg_for_tasks(filename='test_p1.svg',
                      today=datetime.date(2018, 9, 10))

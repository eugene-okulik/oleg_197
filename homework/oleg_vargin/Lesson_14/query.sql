insert into students (name, second_name)
values ('Oleg', 'Vargin');

insert into books (title, taken_by_student_id)
values ('Sketchbook_1', 21920);

insert into books (title, taken_by_student_id)
values ('Sketchbook_2', 21920);

insert into `groups` (title)
values ('Group for Oleg');

update students
set group_id = 21690
where id = 21920;

insert into subjects (title)
values ('Geography');

insert into subjects (title)
values ('World History');

insert into lessons (title, subject_id)
values ('Geography Lesson 1', 13319);

insert into lessons (title, subject_id)
values ('Geography Lesson 2', 13319);

insert into lessons (title, subject_id)
values ('World History Lesson 1', 13320);

insert into lessons (title, subject_id)
values ('World History Lesson 2', 13320);

insert into marks (value, lesson_id, student_id)
values (4, 73976, 21920);

insert into marks (value, lesson_id, student_id)
values (5, 73977, 21920);

insert into marks (value, lesson_id, student_id)
values (3, 73978, 21920);

insert into marks (value, lesson_id, student_id)
values (4, 73979, 21920);

select value from marks left join students on marks.student_id = students.id
where students.id = 21920;

select title from books left join students on books.taken_by_student_id = students.id
where students.id = 21920;

select students.*, marks.*, lessons.*, subjects.*
from students
    join `groups` on students.group_id = `groups`.id
    join books on students.id = books.taken_by_student_id
    join marks on students.id = marks.student_id
    join lessons on marks.lesson_id = lessons.id
    join subjects on lessons.subject_id = subjects.id
where students.id = 21920;

select value from marks left join students on marks.student_id = students.id
where students.id = 21913

select title from books left join students on books.taken_by_student_id = students.id
where students.id = 21913

select students.*, marks.*, lessons.*, subjects.*
from students
    join `groups` on students.group_id = `groups`.id
    join books on students.id = books.taken_by_student_id
    join marks on students.id = marks.student_id
    join lessons on marks.lesson_id = lessons.id
    join subjects on lessons.subject_id = subjects.id
where students.id = 21913

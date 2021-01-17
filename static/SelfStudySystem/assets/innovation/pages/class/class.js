$(document).ready(function() {
    var classId = $('.classId').text().replace('班号：', '');
    $(this).ajaxSubmit({
        url: "http://127.0.0.1:8000/api/specificApis/show/getClassData",
        type: "POST",
        data: {
            'classNumber': classId
        },
        success: function(data) {
            if (!data.error) {
                $(".req-people").text('达标人数/总人数：' + data.classs.requiredPeople + '/' + data.classs.number)
                $(".averTime").text('平均自习时长：' + (data.classs.averDurations / 3600).toFixed(2));
                var students = sort(data.data, 'studentId');
                details(students)
            } else {
                console.log(data.reason);
            }
        }
    });
});

var details = function(students) {
    var html = '';
    var l = last_students_list(students);
    for (i in students) {
        let stuId = students[i].studentId;
        let name = students[i].name;
        let number = students[i].number;
        let points = students[i].points;
        let duration = (students[i].durations / 3600).toFixed(2);
        let averTime = (students[i].averTime / 3600).toFixed(2);
        let state = students[i].state != 0 ? '是' : '否';
        var color = students[i].state != 0 ? '' :
            (l.indexOf(stuId) > -1) ? '' : 'm--font-warning';
        html += '<tr class="' + color + '">\n';
        html += '<th scope="row"><a target="_blank" href="student?studentId=' + stuId + '">' + stuId + '</a></th>\n';
        html += '<td>' + name + '</td>\n';
        html += '<td>' + number + '</td>\n';
        html += '<td>' + points + '</td>\n';
        html += '<td>' + duration + '</td>\n';
        html += '<td>' + averTime + '</td>\n';
        html += '<td>' + state + '</td>\n</tr>\n';
    }
    $('#tbody').append(html);
};



var last_students_list = function(students) {
    var stu_sortBy_points = JSON.parse(JSON.stringify(students));
    stu_sortBy_points = sort(stu_sortBy_points, 'points');
    var l = stu_sortBy_points.slice((stu_sortBy_points.length * 0.2).toFixed(0));
    return l.map(i => {
        return i.studentId
    });
}
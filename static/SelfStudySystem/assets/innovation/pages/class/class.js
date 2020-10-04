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
                details(students);
            } else {
                console.log(data.reason);
            }
        }
    });
});

var details = function(students) {
    var html = '';
    for (i in students) {
        let stuId = students[i].studentId;
        let name = students[i].name;
        let number = students[i].number;
        let points = students[i].points;
        let duration = (students[i].durations / 3600).toFixed(2);
        let averTime = (students[i].averTime / 3600).toFixed(2);
        html += '<tr>\n<th scope="row"><a target="_blank" href="student?studentId=' + stuId + '">' + stuId + '</a></th>\n';
        html += '<td>' + name + '</td>\n';
        html += '<td>' + number + '</td>\n';
        html += '<td>' + points + '</td>\n';
        html += '<td>' + duration + '</td>\n';
        html += '<td>' + averTime + '</td>\n</tr>\n';
    }
    $('#tbody').append(html);
}
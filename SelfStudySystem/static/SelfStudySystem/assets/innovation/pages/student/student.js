$(document).ready(function() {
    var studentId = $('.studentId').text().replace('学号：', '');
    $(this).ajaxSubmit({
        url: "http://127.0.0.1:8000/api/specificApis/show/getStudentData",
        type: "POST",
        data: {
            'studentId': studentId
        },
        success: function(data) {
            if (!data.error) {
                $('.name').text('姓名：' + data.student.name);
                $('.classId').text('班级：' + data.student.classNumber_id);
                $('.points').text('总积分：' + data.student.points);
                $('.number').text('自习次数：' + data.student.number);
                $('.allDuration').text('总时长：' + (data.student.durations / 3600).toFixed(2));
                $('.averTime').text('平均自习时长：' + (data.student.averTime / 3600).toFixed(2));
                var stuDatas = sort(data.data, 'id');
                details(stuDatas);
            } else {
                console.log(data.reason);
            }
        }
    });
});

var details = function(stuDatas) {
    var html = '';
    for (i in stuDatas) {
        let state = stuDatas[i].state;
        let st = new Date(stuDatas[i].startTime + ' GMT+00:00');
        let et = new Date(stuDatas[i].endTime + ' GMT+00:00');
        let point = stuDatas[i].points;
        st = st.format("yyyy-MM-dd hh:mm:ss");
        et = et.format("yyyy-MM-dd hh:mm:ss");
        if (state == 1) {
            var s = '请假';
        } else if (state == 3) {
            var s = '正常';
        } else if (state == 2) {
            continue;
        }
        html += '<tr>\n<th scope="row">' + s + '</th>\n';
        html += '<td>' + st + '</td>\n';
        html += '<td>' + et + '</td>\n';
        html += '<td>' + point + '</td>\n</tr>\n';
    }
    $("#tbody").append(html);
}
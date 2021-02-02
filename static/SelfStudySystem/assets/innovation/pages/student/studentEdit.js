$('.btn-accent').click(function() {
    var studentId = $('#studentId').text().trim().replace('编辑学生信息 学号：', '');
    console.log(studentId)
    $(this).ajaxSubmit({
        url: "/api/specificApis/student/change",
        type: "POST",
        data: {
            'studentId': studentId,
            'name': $('#name').val(),
            'sex': $('#sex').val(),
            'initPoints': $('#initPoints').val()
        },
        success: function(data) {
            if (!data.error) {
                alert("成功修改！");
                window.location.href = '/manageClass'
            } else {
                console.log(data.reason);
                alert("失败！\n原因：" + data.reason);
                window.location.href = '/manageClass'
            }
        }
    });
});
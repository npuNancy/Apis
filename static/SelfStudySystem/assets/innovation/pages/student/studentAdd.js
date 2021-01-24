$('#classNumber').val("10011801")
$('.btn-accent').click(function() {
    console.log("######")
    var sex = $('#sex').val();
    if (sex == "男") {
        var sexx = 1;
    } else {
        var sexx = 0
    }
    $(this).ajaxSubmit({
        url: "http://127.0.0.1:8000/api/specificApis/student/add",
        type: "POST",
        data: {
            'name': $('#name').val(),
            'studentId': $('#studentId').val(),
            'classNumber': $('#classNumber').val(),
            'sex': sexx,
            'initPoints': $('#initPoints').val(),
            'state': 0
        },
        success: function(data) {
            if (!data.error) {
                alert("成功添加！");
                window.location.href = 'http://127.0.0.1:8000/manageClass';
            } else {
                console.log(data.reason);
                alert("失败！\n原因：" + data.reason);
                window.location.href = 'http://127.0.0.1:8000/manageClass';
            }
        }
    });
});
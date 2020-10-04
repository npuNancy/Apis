$(document).ready(function() {
    $(this).ajaxSubmit({
        url: "http://121.196.42.250/api/specificApis/show/getAllClass",
        type: "GET",
        success: function(data) {
            if (!data.error) {
                var people = data.result.people;
                var required = data.result.requiredPeople;
                var classInfo = data.classInfo;
                $('.m-portlet__head-text').text('达标人数/总人数：' + required + '/' + people)
                details(classInfo);
            } else {
                console.log(data.reason);
            }
        }
    });
});

// 页面载入的时候显示所有班级
var details = function(classInfo) {
    var tbody = $('#tbody');
    var html = '';
    for (i in classInfo) {
        let classNumber = classInfo[i].classNumber;
        let averTime = (classInfo[i].averDurations / 3600).toFixed(2);
        let reqPeople = classInfo[i].requiredPeople;
        let allPeople = classInfo[i].number;
        let text = '<tr>\n<th scope="row"><a target="_blank" href="class?classNumber=' + classNumber + '">' + classNumber + '</a></th>\n';
        text += '<td>' + averTime + '</td>\n';
        text += '<td>' + reqPeople + '</td>\n';
        text += '<td>' + allPeople + '</td>\n</tr>\n';
        html += text;
    }
    tbody.append(html);
};
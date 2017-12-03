/**
 * Created by l on 11/30/17.
 */

function check_user_name() {
    var len = $('#userName').val().length;
    if (len<5||len>20)
    {
        $('#userName').next().html('请输入5-20个字符的用户名');
        $('#userName').next().show();
    }
    else
    {
        $.get('/user/register_exit/?userName='+$('#userName').value(),function (data) {
            if (data.count==1){
                $('#userName').next().html('用户已经存在').show();
                error_name = true;
            }else {
                $('#userName').next().hide();
                error_name = false;
            }
        });
    }

}
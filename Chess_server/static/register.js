window.onload = function(){
    var msg_legal = true;
    var push_email;
    var push_name;
    var push_password;
    var push_check;

    var $email_text = $(document.getElementById("email_text"));
    var $email_show = $(document.getElementById("email_show"));

    var $name_text = $(document.getElementById("name_text"));
    var $name_show = $(document.getElementById("name_show"));

    var $password_text = $(document.getElementById("password_text"));
    var $password_show = $(document.getElementById("password_show"));

    var $password_repid_text = $(document.getElementById("password_repid_text"));
    var $password_repid_show = $(document.getElementById("password_repid_show"));

    var $check_text = $(document.getElementById("check_text"));
    var $check_show = $(document.getElementById("check_show"));

    var $get_check = $(document.getElementById("get_check"));
    var $regist = $(document.getElementById("regist"));



// ********************************************************************
    $email_text.focus(function(){
        $email_show.html('请输入一个QQ邮箱');
    }
    )

    $email_text.blur(function(){
        var txt = $email_text.val();
        var resault = txt.search( /^([0-9\.]+)@(qq.com)/);
        if(resault==-1){
            $email_show.html('QQ邮箱格式错误');
            msg_legal = false;
        }else{
            $email_show.html('');
            push_email = txt;
            msg_legal = true;
        }
    }
    )

// ********************************************************************
    $name_text.focus(function(){
        $name_show.html('请输入一个不超过8位的昵称');
    }
    )

    $name_text.blur(function(){
        var txt = $name_text.val();
        var resault = txt.search( /\s/);
        if(resault!=-1){
            $name_show.html('昵称中包含空格');
            msg_legal = false;
        }else{
            if(txt.length>8){
                $name_show.html('昵称太长');
                msg_legal = false;
            }else if(txt.length==0){
                $name_show.html('昵称不能为空');
            }else{
                $name_show.html('');
                push_name = txt;
                msg_legal = true;              
            }
        }
    }
    )

// ********************************************************************
    $password_text.focus(function(){
        $password_show.html('密码由数字，字母或下划线组成');
    }
    )

    $password_text.blur(function(){
        var txt = $password_text.val();
        var resault = txt.search(/^[a-z0-9_-]{6,20}$/);
        if(resault==-1){
            $password_show.html('密码格式有误');
            msg_legal = false;
        // }else if(txt.length>20 || txt.length<6){
        //     $password_show.html('密码长度不符合要求');
        //     msg_legal = false;
        }else{
            $password_show.html('');
            push_password = txt;
            msg_legal = true;
        }
    }
    )

// ********************************************************************
    $password_repid_text.focus(function(){
        $password_repid_show.html('请再次输入密码');
    }
    )

    $password_repid_text.blur(function(){
        var txt = $password_repid_text.val();
        if(txt == push_password){
            $password_repid_show.html('');
            msg_legal = true;
        }else{
            $password_repid_show.html('密码不一致');
            msg_legal = false;
        }

    }
    )
// ********************************************************************
    $check_text.blur(function(){
        var txt = $check_text.val();
        var resault = txt.search(/^[0-9]{6}/);
        if(resault==-1){         
            $check_show.html('验证码格式不正确');
            msg_legal = false;
        }else{
            $check_show.html('');
            push_check = txt;
            msg_legal = true;              
        }
    }
    )
// ********************************************************************
    $regist.click(function(){
        if(msg_legal){
            if(push_email==undefined){
                $email_show.html('*必填项');
            }
            else if(push_name==undefined){
                $name_show.html('*必填项');
            }
            else if(push_password==undefined){
                console.log(push_password)
                $password_show.html('*必填项');
            }
            else if(push_check==undefined){
                $password_show.html('*必填项');
            }else{
                $email_show.html('');
                $name_show.html('');
                $password_show.html('');
                $password_show.html('');
                $check_show.html('');
                console.log('信息装载完毕')
                var push_arry = [push_email,push_name,push_password,push_check]
                console.log(push_arry)
            }
        }else{
            console.log('信息错误')
        }
        
    }
    )

// ********************************************************************
    $get_check.click(function(){
        console.log('获取验证码')
    }
    )
    
}
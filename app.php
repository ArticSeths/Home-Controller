<?php
$apt = $_REQUEST['opt'];
if($apt == 'changeState'){
    $pin = $_POST['pin'];
    echo changeState($pin);
}if($apt == 'getState'){
    $pin = $_POST['pin'];
    echo getState($pin);
}
function changeState($pin){
    return var_dump(shell_exec('/usr/bin/python /var/www/html/changeGPIO.py '. $pin. ' 2>&1'));
}
function getState($pin){
    return shell_exec('/usr/bin/python /var/www/html/getGPIO.py '. $pin. ' 2>&1');
}
?>
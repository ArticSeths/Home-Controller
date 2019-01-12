<?php
$apt = $_REQUEST['opt'];
if($apt == 'changeState'){
    $pin = $_POST['pin'];
    echo changeState($pin);
}
function changeState($pin){
    
    return var_dump(shell_exec('/usr/bin/python /var/www/html/changeGPIO.py '. $pin. ' 2>&1'));
}
?>
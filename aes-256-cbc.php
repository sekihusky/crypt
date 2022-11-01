<?php
class MyCrypt{

    public static function encrypt($payload,$key,$iv)
    {
        $encrypted = openssl_encrypt($payload, 'aes-256-cbc', $key, OPENSSL_RAW_DATA, $iv);
        return base64_encode($encrypted);
    }

    public static function decrypt($garble, $key,$iv)
    {
        $encrypted_data = base64_decode($garble);
        return openssl_decrypt($encrypted_data, 'aes-256-cbc', $key, OPENSSL_RAW_DATA, $iv);
    }

}


$key = 'fwA7SuUnwIC5cnz4ykoPjC3CwnNaQe06';
$iv =  'SoU1ZJ67w6d4fQXa' ;
$payload = 'TESTDATA123456' ;


$data = MyCrypt::encrypt($payload,$key,$iv);
echo $data ;  //pCfJ+Mi30ZBnGAN1Tz7fig==

$grable = 'pCfJ+Mi30ZBnGAN1Tz7fig==' ;
echo MyCrypt::decrypt($grable,$key,$iv);
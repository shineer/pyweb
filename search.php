<?php
header('Content-type: text/html; charset=utf-8');
$arr = array();  
$data = explode('=||=', urldecode(exec("python search.py ".urlencode($_GET['song_name'])))); 
$songs =  explode('=-=',$data[0]);
$temp = array();  
for ($i = 0; $i < (count($songs) - 1); $i++) {
    $vlues = explode('-=-', $songs[$i]);
    array_push($temp,array("song_id"=>$vlues[0], "song_name"=>$vlues[1], "song_artist"=>$vlues[2], "song_album"=>$vlues[3]));
}
$arr["songs"] = $temp;
$pages = explode('-=-', $data[1]);
$arr["pages"] = $pages;
echo json_encode($arr,JSON_UNESCAPED_UNICODE);

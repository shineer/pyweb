<?php
header('Content-type: text/html; charset=utf-8');
$vlues = explode('-=-', exec("python showreal.py ".$_GET['song_id']));
$arr = array("song_location"=>$vlues[0],"song_lyric"=>$vlues[1],"song_pic"=>$vlues[2]);
echo json_encode($arr);
<?php
function CheckURL($Features,$Project_Name,$arr)
{
    if ($arr[0]!="")
       return false;
    if ($arr[1]!=$Project_Name)
       return false;
    if ($arr[2]!=$Features)
       return false;
    if (count($arr)>=4)
       return false;
    
    return true;
}
$arr= explode("/", $_SERVER['REQUEST_URI'] );

if (CheckURL("Home","Web_Interface",$arr) )
    require '../controllers/controller_index.php';
elseif (CheckURL("About","Web_Interface",$arr))
    require "../controllers/controller_About_us.php";
elseif (CheckURL("Audio","Web_Interface",$arr))
    require "../controllers/controller_Audio.php";
elseif (CheckURL("Prediction","Web_Interface",$arr))
    require "../controllers/controller_Prediction.php";
elseif (CheckURL("Graphics","Web_Interface",$arr))
    require "../controllers/controller_Graphics.php";
elseif(in_array("github.com",$arr))
    echo "";
else 
 echo "Wrong Adrres";


?>

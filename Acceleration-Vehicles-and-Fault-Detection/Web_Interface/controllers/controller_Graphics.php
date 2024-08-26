<?php
require '../models/models_Graphics.php';
$checking=true;
if (isset($_POST["model"])==false )
 {
    $checking=false;
 }
 

 if (isset($_POST["features"])==false )
 {
    $checking=false;
 }
 
 if (isset($_POST["train"])==false)
 {
    $checking=false;
 }
 

 if (isset($_POST["lost-function"])==false )
 {
    
    $checking=false;
 }
 

 if (isset($_POST["number_of_cycel"])==false )
 {
    $checking=false;
 }
 if ($checking==false)
 {
   //Default
   $path="../Web_Interface/images/Fundal Image.jpeg";
   $height=300;
   $width=325;
 }
else
  //function GetPath($model,$features,$train,$lost_function,$cycles)
  {
   //custom
   $content=GetPath($_POST["model"],$_POST["features"],$_POST["train"],$_POST["lost-function"],$_POST["number_of_cycel"]);
   if ($content!=false)
   {
    $path=$content[0];
    $height=$content[1];
    $width=$content[2];
   }
   else
   {
    $path="../Web_Interface/images/Fundal Image.jpeg";
    $height=300;
    $width=325;
   }
  }
 /*$_POST["model"]=null;
 $_POST["train"]=null;
 $_POST["fueatures"]=null;
 $_POST["lost-function"]=null;
 $_POST["number_of_cycel"]=null;
*/



require '../view/Graphics.php' ;
?>
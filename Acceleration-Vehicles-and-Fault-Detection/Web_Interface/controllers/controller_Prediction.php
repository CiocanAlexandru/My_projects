<?php
require '../models/models_Prediction.php';
$mod=1;
$checking=true;
$content=null;
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

if ($checking==true) 
{
   $model=GetPrediction($_POST["model"],$_POST["features"],$_POST["train"],$_POST["lost-function"],$_POST["number_of_cycel"]);
   if ($model!=false) 
   { 
     $file_path=SedUploadFile($_FILES["fileToUpload"]);
     $content=Prediction($_POST["features"],$model,$file_path,$_POST["model"]);
   }
   else
   {
      $content="I don't have the model ready";
   }
}
 
require '../view/Prediction.php' ;
?>
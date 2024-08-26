<?php

function GetPrediction($model,$features,$train,$lost_function,$cycles)
{
   $content="";
   if ($model!="SVM")
   { 
     if ($train==="Normal" && $lost_function==="One function")
      {
        $content="../../Models/model_".$model."_".$features."_normaltraining_one_lost_function.h5";
        $cycles=null;
      }
     if($train==="Normal" && $lost_function!="One function")
       {
        $content="../../Models/model_".$model."_".$features."_normaltraining_multi_lost_function.h5";
       }

     if ($train==="Nkfold" && $lost_function==="One function" && $cycles==="One cycle")
       {
        $content="../../Models/model_".$model."_".$features."_kfold_one_lost_function_nocycles.h5";
       }
     if ($train==="Nkfold" && $lost_function==="One function" && $cycles!="One cycle")
       {
        $content="../../Models/model_".$model."_".$features."_kfold_one_lost_function_yescycles.h5";
       }
     if ($train==="Nkfold" && $lost_function!="One function" && $cycles==="One cycle")
      {
       $content="../../Models/model_".$model."_".$features."_kfold_multi_lost_function_categorical_crossentropy_nocycles.h5";
       $content=$content."|"."../../Models/model_".$model."_".$features."_kfold_multi_lost_function_binary_crossentropy_nocycles.h5";
      }
     if ($train==="Nkfold" && $lost_function!="One function" && $cycles!="One cycle")
      {
        $content="../../Models/model_".$model."_".$features."_kfold_multi_lost_function_categorical_crossentropy_yescycles.h5";
        $content=$content."|"."../../Models/model_".$model."_".$features."_kfold_multi_lost_function_binary_crossentropy_yescycles.h5";
      }
   }
   if($model==="SVM")
   {
    $lost_function=null;
    if ($train==="Normal")
    {
        $content="../../Models/model_".$model."_".$features."_normaltraining.pkl";
        $cycles=null;
    }
    if ($train==="Nkfold" && $cycles==="One cycle")
    {
        $content="../../Models/model_".$model."_".$features."_kfold_nocycles.pkl";
        $cycles=null;
    }
    if ($train==="Nkfold" && $cycles!="One cycle")
    {
        $content="../../Models/model_".$model."_".$features."_kfold_yescycles.pkl";
        $cycles=null;
    }

   }
   if (!file_exists($content)) 
   {
      return false;
   }
   if($train==="Normal" && $cycles!=null)
   {
     return false;
   }
   if($model==="SVM" && $train != "Normal")
   {
     return false;
   }
   if($model==="SVM" && $lost_function!=null)
   {
     return false;
   }
   return $content;
}

function SedUploadFile($File)
{
  $targetDir = "../UploadFile";
  $originalFileName = $File["name"];
    $extension = pathinfo($originalFileName, PATHINFO_EXTENSION);
    $newFileName = time() . '_' . uniqid() . '.' . $extension;
    $targetFile = $targetDir . DIRECTORY_SEPARATOR . $newFileName;

    // Muta fișierul încărcat în directorul dorit
    if (move_uploaded_file($File["tmp_name"], $targetFile)) {
        //echo "Fișierul " . basename($newFileName) . " a fost încărcat cu succes.";
    } else {
        echo "Eroare la încărcarea fișierului.";
    }
    return $newFileName; 
}

function Prediction($features,$model_name,$audiofile,$typeof_model)
{
  exec("python ../../main_project/main.py  $features $model_name $audiofile $typeof_model",$output,$ok_status);
  if ($ok_status===0)
    {
       return $output; 
    }
    else {
        echo "Execution error";
    }
  var_dump($output);
  return "Erorr";
}
?>
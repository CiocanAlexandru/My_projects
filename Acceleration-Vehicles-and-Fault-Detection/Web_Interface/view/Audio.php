<!DOCTYPE html>
<html lang="en">
    <head>
    <title>
         Acceleration Vehicles
    </title>
    <meta HTTP-EQUIV=”CACHE-CONTROL” CONTENT=”NO-CACHE”>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="icon" type="image/x-icon" href="../Web_Interface/images/favicon.png">
    <link rel="stylesheet" href="../Web_Interface/styles/style.css">
    <link rel="stylesheet" href="../Web_Interface/styles/Audio.css">
    </head>
    <body>
     <div class="upper">
        <img src="../Web_Interface/images/Above Image New .png">
        <p><a href="Home">Acceleration Vehicles and Fault Detection</a></p>
    </div>
    <div>
        <ul>
            <li><a href="Home">Home</a></li>
            <li><a href="Prediction">Prediction</a></li>
            <li><a href="Audio">Audio</a></li>
            <li><a href="Graphics">Graphics</a></li>
            <li><a href="About">About us</a></li>
        </ul>
    </div>
    <section>
        <div class="content">
        <h1>Audio</h1>
        <?php
        foreach ($content as $element)
         {
            $text=$element["name"];
            $file=$element["path"];
        echo "<div class='audio-item'>
         <p>$text</p>
         <audio controls>
         <source src='$file' type='audio/wav'>
         </audio>
         </div>";
         }
        ?>
        </div>
    </section>
    <footer>
        <p>I made you interested <br> more info  <a href="About">here!</a></p>
    </footer>
    </body>
</html>
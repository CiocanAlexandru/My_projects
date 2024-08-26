<!DOCTYPE html>
<html lang="en">
    <head>
    <title>
         Acceleration Vehicles
    </title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="icon" type="image/x-icon" href="../Web_Interface/images/favicon.png">
    <link rel="stylesheet" href="../Web_Interface/styles/style.css">
    <link rel="stylesheet" href="../Web_Interface/styles/Prediction.css">
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
            <h1>Prediction</h1>
            <?php
            if (isset($content))
            {
                echo"<p><strong>Your car shoud be and the curret state is  !!</strong></p>";
            }
            else 
            {
               echo"<p><strong>Note :The file you upload must be wav!!</strong></p>";
            }
            ?>
            <?php
            if ($content==="I don't have the model ready" && isset($content))
            {
                echo "2";
                echo "<p class='result'> <strong>$content</strong> <br> <br> <br> <br><a class='reset' href='Prediction'>Reset</a></p>";
            }
            if (is_array($content))
            {
              $content=$content[count([$content])];
              echo "<p class='result'> <strong>$content</strong> <br> <br> <br> <br><a class='reset' href='Prediction'>Reset</a></p>";
             
            } 
            if(isset($content)==false)
               echo" <form action='Prediction' method='POST' enctype='multipart/form-data'>
            <div class='file-upload'>
            <input class='audio-file' type='file' name='fileToUpload' id='fileToUpload' accept='.wav'>
            <label class='label-file' for='fileToUpload' data-file-name='No file chosen'></label>
            </div>
            <div class='options'>
            <label for='model'>Model</label>
            <select id='model' name='model'>
            <option value='FCNN'>FCNN</option>
            <option value='CNN'>CNN</option>
            <option value='SVM'>SVM</option>
            </select>
            
            <label for='features'>Fueatures</label>
            <select id='features' name='features'>
            <option value='FFT'>FFT</option>
            <option value='MFCC'>MFCC</option>
            <option value='PSD'>PSD</option>
            </select>

            <label for='train'>Traing Method</label>
            <select id='train' name='train'>
            <option value='Normal'>Normal</option>
            <option value='Nkfold'>Nkfold</option>
            </select>

            <label for='lost-function'>Lost-Function</label>
            <select id='lost-function' name='lost-function'>
            <option value='One function'>One function</option>
            <option value='Multi function'>Multi Function</option>
            </select>
            <label for='number_of_cycel'>Cycel nkfold</label>
            <select id='number_of_cycel' name='number_of_cycel'>
            <option value='One cycle'>One cycel</option>
            <option value='Multi cycle'>More cycles 3 5 7 </option>
            </select>
            <button type='submit' class='submit-button'>Submit</button>
            </div>
            </form>
            ";
             ?>
        </div>
    </section>
    <footer>
        <p>I made you interested <br> more info  <a href="About">here!</a></p>
    </footer>
    </body>
</html>
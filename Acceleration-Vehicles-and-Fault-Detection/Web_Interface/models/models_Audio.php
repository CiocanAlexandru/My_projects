
<?php

function getAudioFiles() {
    $audioFiles = [];
    $directoryPath="../../wav_";
    // Verifică dacă directorul există
    if (is_dir($directoryPath)) {
        // Deschide directorul
        if ($dirHandle = opendir($directoryPath)) {
            // Iterează prin fiecare element din director
            while (($file = readdir($dirHandle)) !== false) {
                // Verifică dacă este un fișier audio (poți adăuga și alte extensii audio)
                $fileExtension = pathinfo($file, PATHINFO_EXTENSION);
                $audioExtensions = ['mp3', 'wav', 'ogg']; // adaugă și alte extensii dacă este necesar
                if (in_array(strtolower($fileExtension), $audioExtensions)) {
                    // Adaugă perechea nume-cale în array
                    $filePath = $directoryPath . '/' . $file;
                    $audioFiles[] = ['name' => $file, 'path' => $filePath];
                }
            }
            
            // Închide directorul
            closedir($dirHandle);
        }
    }
    $randomKeys = array_rand($audioFiles, 7);
    foreach ($randomKeys as $key) {
        $randomAudioFiles[] = $audioFiles[$key];
    }

    return $randomAudioFiles;
}
?>

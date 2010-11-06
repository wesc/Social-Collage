<?

///////////////////////////////////////////////////////////////////////////////////////////
// FUNCTION: makeCollage
// fills region with images from array
///////////////////////////////////////////////////////////////////////////////////////////

function makeCollage($imgArray) {

	foreach ($imgArray as $url) {

		$size = getimagesize("$url");

		if ($size[0] > 100) {
			$w = 100;
		}
		else {
			$w = $size[0];
		}
		
		echo("<img src='$url' style='width: $w; float: left;' /> ");
	}

}


?>
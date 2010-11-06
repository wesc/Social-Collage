<?php 
// pre header php //
/*
// blocks out ie
if (strstr($_SERVER['HTTP_USER_AGENT'], "MSIE") || $_GET[ie] == "on"){
	echo("mistake");
	exit();
}


// connects to database
$db = mysql_connect("mysql.url.com", "user", "pass");
if (!$db) {  
	echo( "DB is down right now." );
	exit();
}

mysql_select_db("blips", $db);

*/  
// include functions
include("functions.php");

?>


<!-- // HEADERS // -->

<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
<head>
	
	<title>Social-Collage</title>
	
	<!-- The metas -->
	<meta name="description" content="">
	<meta name="keywords" content="">
	
	<!-- The Stylesheet -->
	<link rel="stylesheet" href="reset.css" type="text/css" media="screen" />
	<link rel="stylesheet" href="css.css" type="text/css" media="screen" />
	
	<script type="text/javascript" src="jquery-1.4.3.min.js"></script>

</head>
<body>


<div style='width 100%; border: 0px; text-align: left;'>


	<?php
		// black frame http://fc00.deviantart.net/fs17/f/2007/134/c/f/Black_frame_by_darkrose42_stock.jpg
		$imgs = array('http://www.waterfootprint.org/images/gallery/original/apple.jpg',
					'http://media.techworld.com/cmsdata/news/3241113/Apple.jpg', 
					'http://onefrugalchick.com/wp-content/uploads/2010/08/s_flip-flops.jpg','http://www.waterfootprint.org/images/gallery/original/apple.jpg',
					'http://media.techworld.com/cmsdata/news/3241113/Apple.jpg', 
					'http://onefrugalchick.com/wp-content/uploads/2010/08/s_flip-flops.jpg','http://www.waterfootprint.org/images/gallery/original/apple.jpg',
					'http://media.techworld.com/cmsdata/news/3241113/Apple.jpg', 
					'http://onefrugalchick.com/wp-content/uploads/2010/08/s_flip-flops.jpg','http://www.waterfootprint.org/images/gallery/original/apple.jpg',
					'http://media.techworld.com/cmsdata/news/3241113/Apple.jpg', 
					'http://onefrugalchick.com/wp-content/uploads/2010/08/s_flip-flops.jpg',
					'http://static.php.net/www.php.net/images/php.gif');
					
		
	?>

<img src='frame.jpeg' width='650px' style='z-index: 1; position: absolute; top: 0;' />
		<div id='C' style='width: 470px; height: 600px; border: 2px solid black; z-index: 5; position: absolute; top: 170; left: 150;'>
			<?	makeCollage($imgs); ?>
		</div>

</div>


<div class='result'></div>
<!-- // footer // -->

<script>
$.ajax({
  url: "test.html",
  cache: false,
  success: function(html){
    $("#results").append(html);
  }
});

</script>


<?php 
	// closes db
//	mysql_close($db); 
?>


<!-- tracking code -->


<!-- close html -->
</body>
</html>
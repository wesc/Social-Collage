<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
	<head>
		<title>Social Collage</title>
		<link rel="stylesheet" type="text/css" href="http://960ls.atomidata.com/static/cssserve/1/1/6/6/7/5/116675.css">
		<link rel="stylesheet" type="text/css" href="css/reset.css">
		<link rel="stylesheet" type="text/css" href="css/960.css">
		<link rel="stylesheet" type="text/css" href="css/userpage.css">
		
		<script type="text/javascript" src="jquery-1.4.3.min.js"></script>

	</head>
	<body>
		<div id="header" class="container_12">
			<div id="logo" class="grid_3 ">
				<img src="logo2.png" width='200px' style='margin-top: 10px;'></img>
			</div>
			<div id="linkbar" class="grid_7 ">
				
			</div>
			<div id="loginbar" class="grid_2 ">
				
			</div>
		</div>
	
		<div id="content" class="container_12">

<? 
//	include('search/index.html');
?>

		</div>
	
		<div id="footer" class="container_12">
			<div id="meta" class="grid_12 ">
				Meta
			</div>
		</div>
	</body>
</html>

<?

	class Collage {
		private $images = array();
		private $username = "nil";
		private $userurl = "socialcollage/userpage.php?";
		
		public function createUser($usr) {
			$username = $usr;
			$userurl = "socialcollage/userpage.php?".$username;
		}
		
		public function addImg($imgurl) {
			$images.array_push($imgurl);
		}
		
		public function printCollage() {
			echo "<div class='collage' id='".$username."collage'>";
			foreach ($images as $image) {
				echo "<div class='collageimg'>".
						"<img src = '".$image."'>".
					 "</div>"; 
			}
			echo "<div>";
		}
	}

?>

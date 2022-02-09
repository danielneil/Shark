<?php
	include_once(dirname(__FILE__).'/includes/utils.inc.php');
	$this_version = '4.4.6';
	$link_target = 'main';
?>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">

<html>

<head>
	<meta name="ROBOTS" content="NOINDEX, NOFOLLOW">
	<title>Be a Shark.</title>
	<link href="stylesheets/common.css?<?php echo $this_version; ?>" type="text/css" rel="stylesheet">
</head>


<body class='navbar'>

<div class="navbarlogo">
	<a href="https://www.github.com/danielneil/Shark" target="_blank"><img src="images/sblogo.png" height="39" width="140" border="0" alt="Be a shark" /></a>
</div>

<div class="navsection">
	<div class="navsectiontitle">General</div>
	<div class="navsectionlinks">
		<ul class="navsectionlinks">
			<li><a href="main.php" target="<?php echo $link_target;?>">Home</a></li>
			<li><a href="https://github.com/danielneil/Shark/blob/main/README.md" target="_blank">Documentation</a></li>
		</ul>
	</div>
</div>
	
<div class="navsection">
	<div class="navsectiontitle">Instruments</div>
	<div class="navsectionlinks">
		<ul class="navsectionlinks">
			<li><a href="<?php echo $cfg["cgi_base_url"];?>/status.cgi?hostgroup=all&amp;style=hostdetail" target="<?php echo $link_target;?>">{{ instrument_name_plural }}</a></li>
			<li><a href="<?php echo $cfg["cgi_base_url"];?>/status.cgi?host=all" target="<?php echo $link_target;?>">Plugins</a></li>
			<li>
				<a href="<?php echo $cfg["cgi_base_url"];?>/status.cgi?hostgroup=all&amp;style=overview" target="<?php echo $link_target;?>">{{ instrument_group_name_plural }}</a>
				<ul>
					<li><a href="<?php echo $cfg["cgi_base_url"];?>/status.cgi?hostgroup=all&amp;style=summary" target="<?php echo $link_target;?>">Summary</a></li>
				</ul>
			</li>
			<li>
				<a href="<?php echo $cfg["cgi_base_url"];?>/status.cgi?servicegroup=all&amp;style=overview" target="<?php echo $link_target;?>">Plugin Groups</a>
				<ul>
					<li><a href="<?php echo $cfg["cgi_base_url"];?>/status.cgi?servicegroup=all&amp;style=summary" target="<?php echo $link_target;?>">Summary</a></li>
				</ul>
			</li>
		</ul>
	</div>
	<div class="navbarsearch">
		<form method="get" action="<?php echo $cfg["cgi_base_url"];?>/status.cgi" target="<?php echo $link_target;?>">
			<fieldset>
				<legend>Ticker Search:</legend>
				<input type='hidden' name='navbarsearch' value='1'>
				<input type='text' name='host' size='15' class="NavBarSearchItem">
			</fieldset>
		</form>
	</div>
</div>
	
<div class="navsection">
	<div class="navsectiontitle">Trading</div>
	<div class="navsectionlinks">
		<ul class="navsectionlinks">
			<li><a href="#">General</a>
				<ul>
					<li><a href="http://<?php echo $_SERVER['SERVER_ADDR'];?>/framework/public/index.php/console" target="<?php echo $link_target;?>">Console</a></li>
				</ul>
			</li>
			<li><a href="#">Orders</a>
				<ul>
					<li><a href="http://<?php echo $_SERVER['SERVER_ADDR'];?>/framework/public/" target="<?php echo $link_target;?>">Summary</a></li>
					<li><a href="http://<?php echo $_SERVER['SERVER_ADDR'];?>/framework/public/" target="<?php echo $link_target;?>">Opened</a></li>
					<li><a href="http://<?php echo $_SERVER['SERVER_ADDR'];?>/framework/public/" target="<?php echo $link_target;?>">Executed</a></li>
					<li><a href="http://<?php echo $_SERVER['SERVER_ADDR'];?>/framework/public/" target="<?php echo $link_target;?>">Cancelled</a></li>
				</ul>
			</li>
		</ul>
	</div>
</div>	
	
<div class="navsection">
	<div class="navsectiontitle">Portfolio</div>
	<div class="navsectionlinks">
		<ul class="navsectionlinks">
			<li><a href="#">Tools</a>
				<ul>
					<li><a href="http://<?php echo $_SERVER['SERVER_ADDR'];?>/framework/public/index.php/portfolio" target="<?php echo $link_target;?>">Correlation</a></li>
					<li><a href="http://<?php echo $_SERVER['SERVER_ADDR'];?>/shark-web/portfolio/covariance_matrix.png" target="<?php echo $link_target;?>">Covariance</a></li>
				</ul>
			</li>
			<li><a href="#">Backtests</a>
                                <ul>
                                        <li><a href="http://<?php echo $_SERVER['SERVER_ADDR'];?>/framework/public/index.php/backtestreports" target="<?php echo $link_target;?>">Reports</a></li>
                                </ul>
                        </li>
		</ul>
	</div>
</div>	

<div class="navsection">
        <div class="navsectiontitle">Workbench</div>
        <div class="navsectionlinks">
                <ul class="navsectionlinks">
                        <li><a href="#">Historical Data</a>
                                <ul>
                                        <li><a href="http://<?php echo $_SERVER['SERVER_ADDR'];?>/shark-web/historical/" target="<?php echo $link_target;?>">Cache</a></li>
                                </ul>
                        </li>
                        <li><a href="#">Configuration</a>
                                <ul>
                                        <li><a href="http://<?php echo $_SERVER['SERVER_ADDR'];?>/framework/public/index.php/ConfigLogfile" target="<?php echo $link_target;?>">Logfile</a></li>
                                </ul>
			</li>
                </ul>
        </div>
</div>

</body>
</html>
